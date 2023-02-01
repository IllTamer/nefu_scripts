from django.http import HttpRequest, HttpResponse
from .handlers import service, common

from .handlers.utils import SuccessJsonResp, FailedJsonResp
from .handlers.verify import SupportServiceEnum

# TODO 放在更合适的地方
common.Init()

# ping server
def Ping(request: HttpRequest):
    return HttpResponse('pong')

# register account
def Login(request: HttpRequest):
    username = request.GET['username']
    password = request.GET['password']
    
    success, data = service.RefreshUser(username, password)
    if success:
        return SuccessJsonResp(data=data)
    return FailedJsonResp(data=data)

# login service
def LoginService(request: HttpRequest, name: str):
    success, data = False, None
    if name == SupportServiceEnum.JWZX_SZDL.name:
        success, data = SupportServiceEnum.JWZX_SZDL.value.login()
    return SuccessJsonResp(data=data) if success else FailedJsonResp(data=data)

# execute service function
def DoService(request: HttpRequest, name: str):
    success, data = False, None
    if name == SupportServiceEnum.JWZX_SZDL.name:
        success, data = SupportServiceEnum.JWZX_SZDL.value.queryClassSchedule()
        if success:
            image = open(data, "rb")
            return HttpResponse(image.read(), content_type='image/jpg')
    return SuccessJsonResp(data=data) if success else FailedJsonResp(data=data)