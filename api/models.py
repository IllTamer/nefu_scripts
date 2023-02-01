import pytz
from django.db import models
from django.utils import timezone
from requests.cookies import RequestsCookieJar 
# Create your models here.

TimeZone = pytz.timezone('UTC')

# 用户 Token
class Token(models.Model):
    id = models.AutoField(primary_key=True)
    webvpn_key = models.CharField('_webvpn_key', max_length=512)
    exp_time = models.DateTimeField()
    cookie_text = models.TextField(default="[]")

    def set_cookies(self, cookies: RequestsCookieJar):
        self.cookie_text = str(cookies.items())

    def get_cookies(self) -> RequestsCookieJar:
        cookies = RequestsCookieJar()
        for cok in eval(self.cookie_text):
            cookies.set(cok[0], cok[1])
        return cookies
    
    # 是否过期
    def expire(self) -> bool:
        return self.exp_time.replace(tzinfo=TimeZone) <= timezone.now()
    
    def __str__(self) -> str:
        return 'Token(id: {}, webvpn_key: {}, exp_time: {}, cookie_text: {})'.format(self.id, self.webvpn_key, self.exp_time, self.cookie_text)

# 登录用户
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return 'User(id: {}, username: {}, password: {}, token: {})'.format(self.id, self.username, self.password, self.token)