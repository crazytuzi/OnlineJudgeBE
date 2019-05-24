from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Announcements
from .serializers import AnnouncementsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AnnouncementsFilter

# Create your views here.


class AnnouncementsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class AnnouncementsListViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer
    pagination_class = AnnouncementsPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = AnnouncementsFilter
    ordering_fields = ('create_time',)
