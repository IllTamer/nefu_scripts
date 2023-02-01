import os

from django.apps import AppConfig
from threading import Lock

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    lock = Lock()
    
    def ready(self) -> None:
        ApiConfig.lock.acquire()
        try:
            run_once = os.environ.get('CMDLINERUNNER_RUN_ONCE') 
            if run_once is not None: return
            os.environ['CMDLINERUNNER_RUN_ONCE'] = 'True' 
            Init() 
        except Exception as e:
            print(e)
        finally:
            ApiConfig.lock.release()

def Init():
    pass