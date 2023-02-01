import json, base64, datetime

from django.db import transaction
from .models import User, Token
from .utils import Base64Padding

@transaction.atomic
def create_user(username: str, password: str, webvpn_key: str) -> User:
    exp = parse_token(webvpn_key)
    token = Token(webvpn_key=webvpn_key, exp_time=exp)
    token.save()
    print('Generate token: ' + str(token))
    user = User(username=username, password=password, token=token)
    user.save()
    return user

@transaction.atomic
def update_user(username: str, password: str, webvpn_key: str) -> User:
    user = User.objects.get(username=username)
    user.token.webvpn_key = webvpn_key
    user.token.exp_time = parse_token(webvpn_key)
    user.token.save()
    user.password = password
    user.save()
    return user

# @return exp time
def parse_token(webvpn_key: str) -> datetime:
    encode = Base64Padding(webvpn_key.split('.')[1])
    payload: dict = json.loads(base64.b64decode(encode))
    return datetime.datetime.fromtimestamp(payload['exp'])