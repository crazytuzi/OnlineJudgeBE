import requests
from . import Token
from . import DRSalgorithm
import json
from rest_framework.renderers import JSONRenderer
from submissions.models import Submissions, SubmissionToken
from problems.models import Problems
DRS = DRSalgorithm.DRSalgorithm()
jr = JSONRenderer()


def http_post(data):
    jdata = json.loads(jr.render(data).decode("utf-8"))
    problem = Problems.objects.get(pk=jdata["problem"])
    if problem.parent_problem is not None:
        jdata["problem"] = problem.parent_problem.id
    submissionToken = SubmissionToken.objects.create(
        submission=Submissions.objects.get(pk=jdata["id"]),
        token=Token.generate_token(Token.key)
    )
    jdata["id"] = submissionToken.id
    jdata["token"] = submissionToken.token
    url = DRS.getUrl()
    req = requests.post(url, json=jdata)
    DRS.update(url, req.elapsed.total_seconds())
