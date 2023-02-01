import requests, logging
from ..models import User

logging.basicConfig(level=logging.DEBUG)

session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# 最后一个登录的用户实例
latestUser: User = None
# 已登录的用户实例 dict
userDict = dict()

def UpdateUser(user: User):
    userDict[user.id] = user
    global latestUser
    latestUser = user
    print('Update user: {}'.format(latestUser))