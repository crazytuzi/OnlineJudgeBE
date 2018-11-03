import xadmin
from .models import Problems


class ProblemsAdmin(object):
    search_fields = ['title', ]


xadmin.site.register(Problems, ProblemsAdmin)
