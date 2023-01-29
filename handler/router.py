import logging
from enum import Enum
from lxml import etree

# 学校提供的服务实体类
class ServiceItem:
    def __init__(self, title: str, href: str) -> None:
        # 数字东林
        self.Title = title
        # https://i.webvpn.nefu.edu.cn:443
        self.Href = href
    def __str__(self) -> str:
        return 'Title: {} -> Href: {}'.format(self.Title, self.Href)

# 程序支持的服务类型枚举
class SupportService(Enum):
    数字东林 = 'https://i.webvpn.nefu.edu.cn:443'
    def __eq__(self, __o: Enum) -> bool:
        return self.name == __o.name and self.value == __o.value

def selectService(webvpnPage: str) -> SupportService:
    while True:
        tree = etree.HTML(webvpnPage)
        menuList = list[ServiceItem]()
        elementList = tree.xpath('/html/body/div[5]/div/ul/li/a')
        for node in elementList:
            title = node.xpath('@data-original-title')
            href = node.xpath('@href')
            menuList.append(ServiceItem(title[0], href[0]))

        for i, m in enumerate(menuList):
            print('[{}] -> {}'.format(i, m.Title))
        index = int(input('请输入想要进入的系统索引'))
        selectM = menuList[index]
        print('已选定 {}'.format(selectM.Title))
        for service in SupportService:
            if service.value != selectM.Href:
                continue
            return service
        logging.info('This item "{}" is not supported'.format(selectM.Title))

