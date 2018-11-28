import xadmin
from .models import UserCollect, UserAcceptedProblems


class UserCollectAdmin(object):
    search_fields = ['user', ]


class UserAcceptedProblemAdmin(object):
    search_fields = ['user', ]


xadmin.site.register(UserCollect, UserCollectAdmin)
xadmin.site.register(UserAcceptedProblems, UserAcceptedProblemAdmin)
