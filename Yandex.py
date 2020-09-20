import requests
import urllib
headers = {'Authorization': "<Мой токен>"}
response = requests.get("https://cloud-api.yandex.net/v1/disk/resources?path=Ph", headers=headers, params={"path": "C:\\User\denaz\PycharmProjects\\untitled"})
with open('ph.jpg', 'rb') as f:
    resp = requests.put(response.url, files = {"ph.jpg":f})
print(response.url)
