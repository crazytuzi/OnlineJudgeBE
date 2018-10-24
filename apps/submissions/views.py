from rest_framework import filters
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Submissions
from rest_framework import viewsets, status
from .serializers import SubmissionsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SubmissionsFilter
from judge.client import http_post

# Create your views here.


class SubmissionsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "page"
    max_page_size = 100


class SubmissionsListViewSet(
        mixins.UpdateModelMixin,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    queryset = Submissions.objects.get_queryset().order_by('id')
    serializer_class = SubmissionsSerializer
    pagination_class = SubmissionsPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = SubmissionsFilter
    ordering_fields = ('submit_time',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        submission = self.perform_create(serializer)
        http_post(serializer.data)
        re_dict = serializer.data
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_update(self, serializer):
        return serializer.save()

    def perform_destroy(self, instance):
        return instance.delete()
