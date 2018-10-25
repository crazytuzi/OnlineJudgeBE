import requests
from . import token
import json
from rest_framework.renderers import JSONRenderer
from submissions.models import Submissions, SubmissionToken
url = 'http://127.0.0.1:8888/app/'
jr = JSONRenderer()


def http_post(data):
    jdata = json.loads(jr.render(data).decode("utf-8"))
    submissionToken = SubmissionToken.objects.create(
        submission=Submissions.objects.get(pk=jdata["id"]),
        token=token.generate_token(token.key)
    )
    # jdata need reset
    jdata["id"] = submissionToken.id
    jdata["token"] = submissionToken.token
    requests.post(url, json=jdata)
