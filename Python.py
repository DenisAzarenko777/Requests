# -*- coding: utf-8 -*-
import urllib
import httplib2
import json
import uritemplate

headers = {'Authorization': 'AgAAAABDmj3oAADLW-_Zo1wKokfgtju9vgR0prQ'}
connection = httplib2.
resource_url = 'https://cloud-api.yandex.net/v1/disk/resources?path=Ph'

def request(method, url, query=None):
    if query:
        qs = urllib.urlencode(query)
        url = '%s?%s' % (url, qs)
    connection.request(method, url, headers=headers)
    resp = connection.getresponse()
    content = resp.read()
    obj = json.loads(content) if content else None
    status = resp.status
    if status == 201:
        # получаем созданный объект
        obj = request(obj['method'], obj['href'])
    return obj

if __name__ == '__main__':
    # создаём папку
    path = '/foo'
    folder = request('PUT', resource_url, {'path': path})

    # перемещаем папку и получаем перемещённую
    new_path = '/bar'
    folder = request('POST', '%s/move' % resource_url, {'path': new_path, 'from': path})

    # копируем папку и получаем новую папку
    copy_path = '/foobar'
    folder_copy = request('POST', '%s/copy' % resource_url, {'path': copy_path, 'from': new_path})

    # удаляем папки
    request('DELETE', resource_url, {'path': new_path})
    request('DELETE', resource_url, {'path': copy_path})