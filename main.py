import logging
logging.basicConfig(level=logging.INFO)

import os, sys
projectPath = os.path.abspath(os.path.dirname(__file__))
for root, dirs, files in os.walk(projectPath):
    if root.endswith('__'):
        continue
    sys.path.append(root)
    logging.debug(root)


from handler import login, router
from handler.manager import JWZX_SZDLManager
import utils

webvpnPage = login.webvpn()
service = router.selectService(webvpnPage)
_ = login.service(service)

manager = JWZX_SZDLManager()
manager.login()

manager.queryClassSchedule()




