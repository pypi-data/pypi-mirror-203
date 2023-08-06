
from home.api_handler import zView



class ViewSet(zView):
    

    def get(self, request, entity=None, *args, **kwargs):
        meta_data = self.meta_data
        return self.action(request, meta_data).get()

    def post(self, request, entity=None, *args, **kwargs):
        meta_data = self.meta_data
        return self.action(request, meta_data).post()

    def put(self, request, entity=None, *args, **kwargs):
        meta_data = self.meta_data
        return self.action(request, meta_data).put()

    def delete(self, request, entity=None, *args, **kwargs):
        meta_data = self.meta_data
        return self.action(request, meta_data).delete()
