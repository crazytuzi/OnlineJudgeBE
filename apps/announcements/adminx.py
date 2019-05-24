import xadmin
from .models import Announcements


class AnnouncementsAdmin(object):
    search_fields = ['title', ]


xadmin.site.register(Announcements, AnnouncementsAdmin)
