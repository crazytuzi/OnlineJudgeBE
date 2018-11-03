import xadmin
from .models import UserCollect


class UserCollectAdmin(object):
    search_fields = ['user', ]


xadmin.site.register(UserCollect, UserCollectAdmin)
