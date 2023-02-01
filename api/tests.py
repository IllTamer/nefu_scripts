import requests, time, ast
from requests.cookies import RequestsCookieJar

print(time.time())
for i in range(30000):
    cookies = ast.literal_eval("[('BIGipServercas_new_pool', '1079904778.25371.0000'), ('BIGipServershuzi_pool', '694028810.25627.0000'), ('CASTGC', 'TGT-2020211063-83507-v7XeqqyKMG5R4f163IW1A6fwLy4opJricn3lTaBxBChsml5GeI-cas'), ('JSESSIONID', 'BB89A4D08F4DB1AC903B0317BC951250'), ('Language', 'zh_CN'), ('SERVERID', 'Server1'), ('_astraeus_session', 'RHliaXhhOXFaYlVLL1R0YVRGV0NpREViM0lTRzZpS0k2OEtzMWFodVoyUmU0cU9Jd0xkY0Faei9uN00ybmlrK2czZ1NmZ1FJajZXb0NGcEoyVEkzbGluV1V3T0JGejc2NEk2cG5UU2Rpd0szRFd3anJmeWFGV0g3UlNYOXMvaS9Wa0NORTJ3REdaOVJyNTFDWWZZeDFVYU9HbjFSVVgzVlZPbk1rOHZSWUhEaGN0QzZjcFZCZGFYVlJ4ZG5hVUdrNGZzZk5GTmc0dnJmYVlBTk1FMjhTU2JGSkgwNWJ0emExODZGVjdkU1B5cFJ5d3A1UTI1OXludk56Qyt4OEMrNVNXZnhzK0RxQUtmVVVBMjRSMDduckFqVXdLSnlkV3RSTDZTa2RORXhZNWp0dVlVbEZuTGxnZzBiRE8zbkFuZ0stLWNLRmFOVUE2ZEhjRGVwMnVBZWNsOVE9PQ%3D%3D--0ea618b023c4261959ef449f440f0c400b93efb2'), ('_webvpn_key', 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjAyMDIxMTA2MyIsImdyb3VwcyI6WzFdLCJpYXQiOjE2NzUyNjIyODIsImV4cCI6MTY3NTM0ODY4Mn0.E6TDg8Ki1J9I0QJMBnHvcKvhoKSKyySpaJxelUMRQpg'), ('key_dcp_v6', 'TPQNYZdMXfnlyIHdEbookJVq304echOqZnsG_mSjgzQRzaQ-veCK!1676244532'), ('webvpn_username', '2020211063%7C1675262282%7Cb4acb5454870f4293005183d7aaa7531e79cbcc3')]")
    # cookies: list[tuple] = [
    #     ('_webvpn_key', 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMjAyMDIxMTA2MyIsImdyb3VwcyI6WzFdLCJpYXQiOjE2NzUyNjIyODIsImV4cCI6MTY3NTM0ODY4Mn0.E6TDg8Ki1J9I0QJMBnHvcKvhoKSKyySpaJxelUMRQpg'), 
    #     ('webvpn_username', '2020211063%7C1675262282%7Cb4acb5454870f4293005183d7aaa7531e79cbcc3'), 
    #     ('BIGipServercas_new_pool', '1079904778.25371.0000'), 
    #     ('JSESSIONID', 'zZUNYN7b6raPaQYzkn-1o0zkSxKnUOtt3zuwHYpCSQvHDCCAye4U!1186892427'), 
    #     ('Language', 'zh_CN'), 
    #     ('CASTGC', 'TGT-2020211063-83507-v7XeqqyKMG5R4f163IW1A6fwLy4opJricn3lTaBxBChsml5GeI-cas'), 
    #     ('BIGipServershuzi_pool', '694028810.25627.0000'), 
    #     ('key_dcp_v6', 'TPQNYZdMXfnlyIHdEbookJVq304echOqZnsG_mSjgzQRzaQ-veCK!1676244532'), 
    #     ('SERVERID', '125'), 
    #     ('JSESSIONID', 'BB89A4D08F4DB1AC903B0317BC951250'), 
    #     ('SERVERID', 'Server1'), 
    #     ('_astraeus_session', 'RHliaXhhOXFaYlVLL1R0YVRGV0NpREViM0lTRzZpS0k2OEtzMWFodVoyUmU0cU9Jd0xkY0Faei9uN00ybmlrK2czZ1NmZ1FJajZXb0NGcEoyVEkzbGluV1V3T0JGejc2NEk2cG5UU2Rpd0szRFd3anJmeWFGV0g3UlNYOXMvaS9Wa0NORTJ3REdaOVJyNTFDWWZZeDFVYU9HbjFSVVgzVlZPbk1rOHZSWUhEaGN0QzZjcFZCZGFYVlJ4ZG5hVUdrNGZzZk5GTmc0dnJmYVlBTk1FMjhTU2JGSkgwNWJ0emExODZGVjdkU1B5cFJ5d3A1UTI1OXludk56Qyt4OEMrNVNXZnhzK0RxQUtmVVVBMjRSMDduckFqVXdLSnlkV3RSTDZTa2RORXhZNWp0dVlVbEZuTGxnZzBiRE8zbkFuZ0stLWNLRmFOVUE2ZEhjRGVwMnVBZWNsOVE9PQ%3D%3D--0ea618b023c4261959ef449f440f0c400b93efb2')
    # ]
print(time.time())
print(cookies)

# session = requests.session()
# cookiesEntity: RequestsCookieJar = session.cookies
# for cok in cookies:
#     cookiesEntity.set(cok[0], cok[1])
# print(cookiesEntity.items())