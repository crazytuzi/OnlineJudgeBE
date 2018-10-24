import requests
from rest_framework.renderers import JSONRenderer

url = 'http://127.0.0.1:8888/app/'
jr = JSONRenderer()


def http_post(returndict):
    data = jr.render(returndict)
    requests.post(url, data=data)
