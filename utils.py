import sys, logging, requests

def assertStatus(message: str, resp: requests.Response):
    if (resp.status_code != 200):
        logging.warning(message)
        logging.warning(resp.text)
        sys.exit(-1)

def save2File(filename: str, content: str):
    f = open(filename, 'w')
    f.write(content)
    f.close()