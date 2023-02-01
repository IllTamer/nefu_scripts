from django.db import models
from django.utils import timezone
from requests.cookies import RequestsCookieJar 
# Create your models here.

# 用户 Token
class Token(models.Model):
    id = models.AutoField(primary_key=True)
    webvpn_key = models.CharField('_webvpn_key', max_length=512)
    exp_time = models.DateTimeField()
    cookie_text = models.TextField()
    def expire(self) -> bool:
        return self.exp_time <= timezone.now()
    def __str__(self) -> str:
        return 'Token(id: {}, webvpn_key: {}, exp_time: {})'.format(self.id, self.webvpn_key, self.exp_time)

# 登录用户
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return 'User(id: {}, username: {}, password: {}, token: {})'.format(self.id, self.username, self.password, self.token)