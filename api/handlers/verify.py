import os
from enum import Enum
from lxml import etree
from django.http import HttpResponse

from . import manager
from .common import session, headers

webvpnAuthURL = 'https://cas.webvpn.nefu.edu.cn/cas/login?service=https%3A%2F%2Fwebvpn-443.webvpn.nefu.edu.cn%2Fusers%2Fauth%2Fcas%2Fcallback%3Furl'
webvpnURLPrefix = 'https://cas.webvpn.nefu.edu.cn'

# 程序支持的服务类型枚举
class SupportServiceEnum(Enum):
    JWZX_SZDL = manager.JWZX_SZDLManager()
    def __eq__(self, __o: Enum) -> bool:
        return self.name == __o.name and self.value == __o.value

# TODO 存储 cookies, 读取 cookies，若在 exp time 内则无需重新登录

# 登录 WebVPN
# 注意：在所有需要验证的操作之前必须先进行登录操作
# @return _webvpn_key | error_msg
def webvpn(username: str, password: str) -> tuple[bool, str]:
    session.cookies.clear()
    # set jsession cookie
    # parse params: 'lt' 'execution' '_eventId'
    resp = session.get(webvpnAuthURL, headers=headers)
    tree = etree.HTML(resp.text)
    lt = tree.xpath('//*[@id="lt"]/@value')
    execution = tree.xpath('//*[@name="execution"]/@value')
    _eventId = tree.xpath('//*[@name="_eventId"]/@value')

    # 调用学校的 rsa 脚本生成 rsa 数据
    command = os.popen('node ./resource/rsa.js {} {} {}'.format(username, password, lt))
    rsa = command.buffer.read().decode('utf-8')
    command.close()

    data = {
        'rsa': rsa,
        'ul': len(username),
        'pl': len(password),
        'lt': lt,
        'execution': execution,
        '_eventId': _eventId
    }
    ## cas auth -> webvpn
    # 其中，因返回状态码为302，框架自动重定向到附带 ticket 的 Location 所指 cas 验证服务器，进而通过验证获取用户 token,储存在 cookie
    # 若对相关 cas 验证流程感兴趣可看 https://djangocas.dev/blog/cas-101-introduction-to-cas-central-authentication-service/
    resp = session.post(webvpnAuthURL, headers=headers, data=data)
    if needWebVPNAuth(resp):
        return False, webvpnAuthErrorMsg(resp)
    return True, session.cookies.get('_webvpn_key')

def needWebVPNAuth(resp: HttpResponse) -> bool:
    return resp.url.startswith(webvpnURLPrefix)

def webvpnAuthErrorMsg(resp: HttpResponse) -> str:
    tree = etree.HTML(resp.text)
    return tree.xpath('//*[@id="errormsg"]/text()')[0]
    

# # 学校提供的服务实体类
# class ServiceItem:
#     def __init__(self, title: str, href: str) -> None:
#         # 数字东林
#         self.Title = title
#         # https://i.webvpn.nefu.edu.cn:443
#         self.Href = href
#     def __str__(self) -> str:
#         return 'Title: {} -> Href: {}'.format(self.Title, self.Href)

# # 打印 webvpn 服务列表
# def printServiceItemList(webvpnPage: str):
#         tree = etree.HTML(webvpnPage)
#         menuList = list[ServiceItem]()
#         elementList = tree.xpath('/html/body/div[5]/div/ul/li/a')
#         for node in elementList:
#             title = node.xpath('@data-original-title')
#             href = node.xpath('@href')
#             menuList.append(ServiceItem(title[0], href[0]))
#         print(menuList)
