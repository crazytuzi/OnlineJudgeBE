import xadmin
from .models import Submissions


class SubmissionsAdmin(object):
    search_fields = ['user', ]


xadmin.site.register(Submissions, SubmissionsAdmin)
