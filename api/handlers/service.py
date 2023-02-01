import json, base64, datetime

from django.db import transaction
from . import common, verify, utils
from ..models import User, Token

@transaction.atomic
def create_user(username: str, password: str, webvpn_key: str) -> User:
    exp = parse_token(webvpn_key)
    token = Token(webvpn_key=webvpn_key, exp_time=exp)
    token.set_cookies(common.session.cookies)
    token.save()
    user = User(username=username, password=password, token=token)
    user.save()
    return user

@transaction.atomic
def update_user(username: str, password: str, webvpn_key: str) -> User:
    user = User.objects.get(username=username)
    user.token.webvpn_key = webvpn_key
    user.token.exp_time = parse_token(webvpn_key)
    user.token.set_cookies(common.session.cookies)
    user.token.save()
    user.password = password
    user.save()
    return user

# @return exp time
def parse_token(webvpn_key: str) -> datetime:
    encode = utils.Base64Padding(webvpn_key.split('.')[1])
    payload: dict = json.loads(base64.b64decode(encode))
    return datetime.datetime.fromtimestamp(payload['exp'])

# 刷新用户登录状态
# - 若用户名不存在，则插入到数据库
# @return 成功为 True, user.Id 失败为 False, errMsg
def RefreshUser(username: str, password: str) -> tuple[bool, int | str]:
    user: User = common.userDict.get(username)
    if user != None and user.username == username and user.password == password:
        if user.token.expire() == False:
            # cached
            common.session.cookies = user.token.get_cookies()
            return True, user.id
    # 加锁保证 cookies 安全
    common.lock.acquire()
    try:
        success, webvpn_key = verify.webvpn(username, password)
        
        if success:
            if user != None:
                user = update_user(username, password, webvpn_key)
            else:
                user = create_user(username, password, webvpn_key)
            common.UpdateUser(user)
            return True, user.id
    except Exception as e:
        print(e)
        return False, webvpn_key
    finally:
        common.lock.release()