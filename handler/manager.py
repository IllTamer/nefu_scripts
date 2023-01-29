import logging
from lxml import etree
from common import session, headers

class Manager(object):
    pass

# 数字东林实现
class SZDLManager(Manager):
    pass

# 数字东林 - 教务在线实现
class JWZX_SZDLManager(SZDLManager):
    # @return: 是否成功，若不成功则附带返回页面
    def login(self) -> tuple[bool, str]:
        url = 'https://i.webvpn.nefu.edu.cn/dcp/forward.action?path=dcp/core/appstore/menu/jsp/redirect&appid=b52ff9537b47447e8ec713e64a1c3dc9&ac=0'
        resp = session.get(url, headers=headers)

        success = resp.status_code == 200
        if success:
            tree = etree.HTML(resp.text)
            logging.info('Hello {}'.format(tree.xpath('//*[@id="Top1_divLoginName"]/text()')[0]))
        
        return success, '' if success else resp.text
    
    def queryClassSchedule(self) -> tuple[bool, str]:
        url = 'https://jwcnew.webvpn.nefu.edu.cn/dblydx_jsxsd/xskb/xskb_list.do'
        data = {

        }
        resp = session.get(url, headers=headers, data=data)
        
        success = resp.status_code == 200
        if success:
            tree = etree.HTML(resp.text)
            tree.xpath('//*[@id="kbtable"]/tbody')
            return True, ''
        return False, resp.text