import asyncio


class graph_executions:
    def __init__(self):
        pass

    def request_parser(self, request, response, params, meta_data=None, permissions=None):
        self.request = request
        self.res = response(request)
        self.person_id = self.res.auth_puid()
        self.meta_data = meta_data
        self.function_args = {}
        strategy = params.pk_fetch_strategy
        if strategy == 0:  # "requests"
            self.primary_key = self.request.query_params.get(params.pk_field)
            if not self.primary_key:
                self.primary_key = request.data.get(params.pk_field)
        elif strategy == 1:  # "meta"
            self.primary_key = self.meta_data["preferences"]
        elif strategy == 2:  # "person"
            self.primary_key = self.person_id
        return self
