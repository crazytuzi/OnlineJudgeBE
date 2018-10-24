from urllib import request
from rest_framework.renderers import JSONRenderer

url = 'http://192.168.2.223:8888/app'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
}
jr = JSONRenderer()


def http_post(ReturnDict):
    data = jr.render(ReturnDict)
    req = request.Request(url, data=data, headers=headers)
    res = request.urlopen(req)
