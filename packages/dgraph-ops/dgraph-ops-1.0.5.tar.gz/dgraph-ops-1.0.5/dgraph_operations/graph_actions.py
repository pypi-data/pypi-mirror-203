from .node_connector import graph_engine
from home.res_gateway import response
import time
from .executors import graph_executions
import asyncio


class graph_actions:
    def __init__(self, request,entity=None, meta_data=None, permissions=None):
        self.request = request
        self.res = response(request)
        self.entity_id = self.res.auth_puid()
        self.meta_data = meta_data
        self.function_args = {}
        strategy = self.pk_fetch_strategy
        if strategy == 0:  # "requests"
            self.primary_key = self.request.query_params.get(self.pk_field)
            if not self.primary_key:
                try:
                    self.primary_key = request.data.get(self.pk_field)
                except:
                    self.primary_key = None
        elif strategy == 1:  # "from preference"
            self.entity_id = self.meta_data["preferences"].get("preferences").get(entity).get("entity_id")
        elif strategy == 2:  # "person "
            self.primary_key = self.res.person(meta_data)
            

    def get(self):
        # try:
        if 1 > 0:
            if self.primary_key:
                try:
                    processed_data = self.dqquery.get(self.entity_id,
                        self.primary_key).get(self.entity)
                except: #TODO COMBINE THIS WITH THE ABOVE   
                    processed_data = self.dqquery.get(
                        self.primary_key).get(self.entity)

                len_data = len(processed_data)

                if len_data == 0:
                    return self.res.out(["ok", [], "no data"])

                if len_data < 2:
                    processed_data= processed_data[0]
                    self.function_args["processed_data"] = processed_data
                # try:
                if 1 > 0:
                    if self.add_functions:
                        processed_data = self.plugin_func(self.add_functions,
                                                          method="GET")
                # except:
                #     pass
                return self.res.out(["ok", processed_data, "success"])
            else:
                # x = self.dqquery.all()
                try:
                    result = self.dqquery.all(self.entity_id).get(self.entity)

                except:
                    result = {}

                print("result = ", result)
                len_data = len(result)

                if len_data == 0:
                    return self.res.out(["ok", [], "no data"])
                for processed_data in result:
                    self.function_args.update(
                        {"processed_data": processed_data})
                    if self.add_functions:
                        processed_data = self.plugin_func(self.add_functions,
                                                          method="GET", processed_data=processed_data)
            if processed_data:
                return self.res.paginated(["ok", result, "success"])
            else:
                return self.res.out(["error", [], "error"])
        # except:
        #     return self.res.out(["error", "", "error"])

    def ser_check(self):
        print("request data = ", self.request.data)
        ser = self.serializer(
            data=self.request.data,
            context={'request': self.request}
        )
        if ser.is_valid():
            processed = graph_engine(ser.validated_data,
                                     self.fields(self.entity)(), self.primary_key)
            data = processed.connect()
            return True, data, ser.validated_data
        else:
            return False, ser.errors, []

    async def process_data(self, function, **kwargs):
        return function(**kwargs)

    async def create_task(self, function, **kwargs):
        task = asyncio.create_task(self.process_data(function, **kwargs))
        return True

    def execute_async(self, function, **kwargs):
        return asyncio.run(self.create_task(function, **kwargs))

    def plugin_func(self, function, **kwargs):
        processed_data = kwargs.get("processed_data")
        for func in function:
            if kwargs["method"] in func["methods"]:
                processed_data = func["function"](self)
        return processed_data

    def modify(self, **kwargs):
        processed_data = kwargs["processed_data"]
        ser_data = kwargs["ser_data"]
        processed_data.update(
            {self.entity+".modified_on": time.time()})
        if self.entity_id:
            processed_data.update(
                {self.entity+".modified_by": self.entity_id})
        processed_data["id"] = self.primary_key
        self.function_args.update({"processed_data": processed_data,
                                   "ser_data": ser_data})

        if self.add_functions:
            processed_data = self.plugin_func(self.add_functions,
                                              method="PUT", processed_data=processed_data)

        self.dqquery.create(processed_data)
        # if any field in ser_data is of type "list", delete it
        for key, value in ser_data.items():
            if isinstance(value, list):
                try:
                    getattr(self.dqquery,"delete_"+key)(self.primary_key, value)
                except:
                    pass

    def create(self, **kwargs):
        processed_data = kwargs["processed_data"]
        print("proicessed_data = ", processed_data)
        ser_data = kwargs["ser_data"]

        processed_data.update({self.entity+".created_on": time.time()})
        if self.entity_id:
            processed_data.update(
                {self.entity+".created_by": self.entity_id})
        uid = self.dqquery.create(processed_data)
        processed_data["id"] = uid
        self.function_args.update({"processed_data": processed_data,
                                   "ser_data": ser_data})
        if self.add_functions:
            processed_data = self.plugin_func(self.add_functions,
                                              method="POST", processed_data=processed_data)

    def put(self):
        status, processed_data, ser_data = self.ser_check()
        if status:
            try:
                self.execute_async(
                    self.modify, processed_data=processed_data, ser_data=ser_data)
                return self.res.out(["ok", [], "modified"])
            except:
                return self.res.out(["error", processed_data, "error"])
        else:
            return self.res.out(["error", processed_data, "error"])

    def post(self):
        status, processed_data, ser_data = self.ser_check()
        print("status, processed data, ser data = ", status, processed_data, ser_data)
        if status:
            try:
                self.execute_async(
                    self.create, processed_data=processed_data, ser_data=ser_data)
                return self.res.out(["ok", [], "added"])
            except:
                return self.res.out(["error", processed_data, "error"])
        else:
            return self.res.out(["error", processed_data, "error"])

    def delete(self):
        item = self.request.query_params.get(self.pk_field)
        if not item:
            item = self.request.data.get(self.pk_field)
        if type(item) != list:
            item = [item]

        try:
            self.dqquery.delete(item, self.primary_key)
            return self.res.out(["ok", "item deleted", "success"])
        except:
            return self.res.out(["error", "", "error"])
