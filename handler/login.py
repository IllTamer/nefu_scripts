import os, sys, logging, requests
from lxml import etree

import utils
from router import SupportService
from common import session, headers

username = ''
password = ''

webvpnURL = 'https://cas.webvpn.nefu.edu.cn/cas/login?service=https%3A%2F%2Fwebvpn-443.webvpn.nefu.edu.cn%2Fusers%2Fauth%2Fcas%2Fcallback%3Furl'

# 登录 WebVPN
# 注意：在所有需要验证的操作之前必须先进行登录操作
def webvpn() -> str:
    # set jsession cookie
    # parse params: 'lt' 'execution' '_eventId'
    resp = session.get(webvpnURL, headers=headers)
    tree = etree.HTML(resp.text)
    lt = tree.xpath('//*[@id="lt"]/@value')
    execution = tree.xpath('//*[@name="execution"]/@value')
    _eventId = tree.xpath('//*[@name="_eventId"]/@value')

    # 调用学校的 rsa 脚本生成 rsa 数据
    command = os.popen('node resource/rsa.js {} {} {}'.format(username, password, lt))
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
    resp = session.post(webvpnURL, headers=headers, data=data)
    utils.assertStatus('Cas authorization failed, content:', resp)
    return resp.text

# 登录主服务
# 注意：在进行对各子服务的操作之前必须先进行主服务登录操作
def service(service: SupportService) -> str:
    if service == SupportService.数字东林:
        resp = session.get(service.value, headers=headers)
        utils.assertStatus('Service authorization failed, content:', resp)
        # 数字东林主页为 js 懒加载，获取 service cookie 后直接访问目标服务即可
        return ''
    else:
        logging.warn('Unknown service: ' + service)
