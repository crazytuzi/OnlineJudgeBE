import xadmin
from .models import Submissions, SubmissionToken


class SubmissionsAdmin(object):
    search_fields = ['user', ]


class SubmissionTokenAdmin(object):
    search_fields = ['submission', ]


xadmin.site.register(Submissions, SubmissionsAdmin)
xadmin.site.register(SubmissionToken, SubmissionTokenAdmin)
