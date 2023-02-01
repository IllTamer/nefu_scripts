import json
# from django.apps import apps
# from django.db import models
from django.http import HttpResponse 

def Base64Padding(data):
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    return data

def SuccessJsonResp(*, data: object = ..., msg: str = ...) -> HttpResponse:
    data = None if type(data) == type(Ellipsis) else data
    msg = 'success' if type(msg) == type(Ellipsis) else msg
    return HttpResponse(JsonEntity(0, data, msg))

def FailedJsonResp(*, data: object = ..., msg: str = ...) -> HttpResponse:
    data = None if type(data) == type(Ellipsis) else data
    msg = 'failed' if type(msg) == type(Ellipsis) else msg
    return HttpResponse(JsonEntity(-1, data, msg))

def Save2File(filename: str, content: str):
    f = open(filename, 'w')
    f.write(content)
    f.close()

class JsonEntity():
    def __init__(self, status: int, data: object, msg: str) -> None:
        self.status = status
        self.data = data
        self.msg = msg
    def __str__(self) -> str:
        return json.dumps({
            "status": self.status,
            "data": self.data,
            "msg": self.msg
        })
# # 获取 model 中定义字段的名称
# def get_model_field_name(model_field: models.Field) -> str:
#   app_name = 'api'
#   modelobj = apps.get_model(app_name, model_field.model)
#   field_dic={}
#   for field in modelobj._meta.fields:
#     field_dic[field.name] = field.verbose_name
#     # print('字段类型:',type(field).__name__)  #返回的是‘charfield','textfield',等这些类型
#   return field_dic.get('name')