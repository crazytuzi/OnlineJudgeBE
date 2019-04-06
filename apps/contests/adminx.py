import xadmin
from .models import Contests, ContestRankList


class ContestsAdmin(object):
    search_fields = ['title', ]


class ContestRankListAdmin(object):
    search_fields = ['contest', 'user']


xadmin.site.register(Contests, ContestsAdmin)
xadmin.site.register(ContestRankList, ContestRankListAdmin)
