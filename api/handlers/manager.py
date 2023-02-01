import imgkit
from lxml import etree
from . import common, verify
from .common import session, headers

class Manager(object):
    pass

# 数字东林实现
class SZDLManager(Manager):
    def login(self) -> tuple[bool, str]:
        user = common.latestUser
        if user == None:
            return False, 'Please login first'
        return verify.webvpn(user.username, user.password)

# 数字东林 - 教务在线实现
class JWZX_SZDLManager(SZDLManager):
    # @return: 是否成功，若不成功则附带返回失败信息
    def login(self) -> tuple[bool, str]:
        success, err = super().login()
        if success == False:
            return False, err
        url = 'https://i.webvpn.nefu.edu.cn/dcp/forward.action?path=dcp/core/appstore/menu/jsp/redirect&appid=b52ff9537b47447e8ec713e64a1c3dc9&ac=0'
        resp = session.get(url, headers=headers)

        tree = etree.HTML(resp.text)
        if verify.needWebVPNAuth(resp):
            return False, verify.webvpnAuthErrorMsg(resp)      
        return True, 'Hello {}'.format(tree.xpath('//*[@id="Top1_divLoginName"]/text()')[0])
        
    # @return: 是否成功，若不成功则附带返回失败信息
    def queryClassSchedule(self) -> tuple[bool, str]:
        url = 'https://jwcnew.webvpn.nefu.edu.cn/dblydx_jsxsd/xskb/xskb_list.do'
        data = {
            # 课表放大
            'sfFD': 1,
            # 学年学期
            'xnxq01id': '2022-2023-1',
            # 周次
            # 'zc': 1
        }
        resp = session.post(url, headers=headers, data=data)
        
        if verify.needWebVPNAuth(resp):
            return False, verify.webvpnAuthErrorMsg(resp)
        tree = etree.HTML(resp.text)
        table = tree.xpath('//*[@id="kbtable"]')[0]
        table = etree.tostring(table, encoding='utf-8').decode()
        path = 'static/class-table.png'
        result = imgkit.from_string(table, path)
        return (True, path) if type(result) == bool else (False, str(result))