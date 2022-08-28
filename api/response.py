from django.http.response import HttpResponse, JsonResponse

from datetime import datetime
from bson.objectid import ObjectId
from django.core.serializers.json import DjangoJSONEncoder

class CustomJsonEncoder(DjangoJSONEncoder):

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)

        if isinstance(obj, datetime):
            return int(obj.timestamp() * 1000)

        return super(CustomJsonEncoder, self).default(obj)



class JSONResponse(JsonResponse):
    def __init__(
        self,
        data,
        encoder=CustomJsonEncoder,
        safe=True,
        json_dumps_params=None,
        **kwargs
    ):
        super(JSONResponse, self).__init__(
            data, encoder, safe, json_dumps_params, **kwargs
        )



class OK(JSONResponse):

    def __init__(self,data,encoder=CustomJsonEncoder,safe=True,json_dumps_params=None,**kwargs):

        kwargs.pop("status", None)
        kwargs["status"] = 200

        super(JSONResponse, self).__init__(
            data, encoder, safe, json_dumps_params, **kwargs
        )
