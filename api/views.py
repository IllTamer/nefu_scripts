from django.http import HttpRequest, HttpResponse
from . import service

from .utils import SuccessJsonResp, FailedJsonResp
from .handlers import common, verify
from .handlers.verify import SupportServiceEnum

# ping server
def ping(request: HttpRequest):
    return HttpResponse('pong')

# register account
def register(request: HttpRequest):
    username = request.GET['username']
    password = request.GET['password']
    success, webvpn_key = verify.webvpn(username, password)
    
    if success:
        if service.User.objects.filter(username=username).exists():
            user = service.update_user(username, password, webvpn_key)
        else:
            user = service.create_user(username, password, webvpn_key)
        common.UpdateUser(user)
        return SuccessJsonResp(data=str(user))
    return FailedJsonResp(data=webvpn_key)

# login exists account
def login(request: HttpRequest):
    username = request.GET['username']
    user = service.User.objects.get(username=username)
    if user != None:
        # check exp time
        common.UpdateUser(user)
        return SuccessJsonResp(data=user.id)
    return FailedJsonResp()

# login service
def loginService(request: HttpRequest, name: str):
    success, data = False, None
    if name == SupportServiceEnum.JWZX_SZDL.name:
        success, data = SupportServiceEnum.JWZX_SZDL.value.login()
    return SuccessJsonResp(data=data) if success else FailedJsonResp(data=data)

# execute service function
def doService(request: HttpRequest, name: str):
    success, data = False, None
    if name == SupportServiceEnum.JWZX_SZDL.name:
        success, data = SupportServiceEnum.JWZX_SZDL.value.queryClassSchedule()
        if success:
            image = open(data, "rb")
            return HttpResponse(image.read(), content_type='image/jpg')
    return SuccessJsonResp(data=data) if success else FailedJsonResp(data=data)