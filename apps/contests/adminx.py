import xadmin
from .models import Contests


class ContestsAdmin(object):
    search_fields = ['title', ]


xadmin.site.register(Contests, ContestsAdmin)
