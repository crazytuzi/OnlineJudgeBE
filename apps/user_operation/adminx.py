import xadmin
from .models import UserCollect, UserAcceptedProblems, UserChallengingProblems


class UserCollectAdmin(object):
    search_fields = ['user', ]


class UserAcceptedProblemAdmin(object):
    search_fields = ['user', ]


class UserChallengingProblemAdmin(object):
    search_fields = ['user', ]


xadmin.site.register(UserCollect, UserCollectAdmin)
xadmin.site.register(UserAcceptedProblems, UserAcceptedProblemAdmin)
xadmin.site.register(UserChallengingProblems, UserChallengingProblemAdmin)
