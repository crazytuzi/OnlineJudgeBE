from django_filters import rest_framework
from .models import Announcements


class AnnouncementsFilter(rest_framework.FilterSet):

    class Meta:
        model = Announcements
        fields = []
