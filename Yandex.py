import requests
import urllib

headers = {'Authorization': 'мой_токен'}
response = requests.get("https://cloud-api.yandex.net/v1/disk/resources?path=Ph", headers=headers, params={"path": "C:\\User\denaz\PycharmProjects\\untitled\gif"})
print(response.text)
with open('gif/unnamed.jpg', 'rb') as f:
    resp = requests.put(response.url, files = {"file":f})
#https://cloud-api.yandex.net/v1/disk/resources?path=Ph
