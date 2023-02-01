import requests
from requests.cookies import RequestsCookieJar

session = requests.session()
cookies: RequestsCookieJar = session.cookies
cookies.items()