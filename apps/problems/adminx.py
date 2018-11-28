import xadmin
from .models import Problems, ContentProblems


class ProblemsAdmin(object):
    search_fields = ['title', ]


class ContestProblemsAdmin(object):
    search_fields = ['title', ]


xadmin.site.register(Problems, ProblemsAdmin)
xadmin.site.register(ContentProblems, ContestProblemsAdmin)
