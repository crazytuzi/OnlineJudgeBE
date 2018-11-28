from rest_framework import filters
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Submissions, SubmissionToken
from rest_framework import viewsets, status
from .serializers import SubmissionsSerializer, SubmissionTokenSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SubmissionsFilter
from judge.client import http_post
from judge import token

# Create your views here.


class SubmissionsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "page"
    max_page_size = 100


class SubmissionsListViewSet(
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    queryset = Submissions.objects.all()
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
        self.perform_create(serializer)
        http_post(serializer.data)
        re_dict = serializer.data
        headers = self.get_success_headers(serializer.data)
        return Response(
            re_dict,
            status=status.HTTP_201_CREATED,
            headers=headers)

    def perform_update(self, serializer):
        return serializer.save()

    def perform_destroy(self, instance):
        return instance.delete()


class SubmissionTokenListViewSet(
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    queryset = SubmissionToken.objects.all()
    serializer_class = SubmissionTokenSerializer

    def update(self, request, *args, **kwargs):
        data = request.data
        submissionToken = SubmissionToken.objects.get(pk=data["id"])
        if submissionToken.token != data["token"]:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if token.certify_token(token.key, submissionToken.token) == False:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        submission = submissionToken.submission
        submission.result = data["result"]
        submission.time_cost = data['time_cost']
        submission.memory_cost = data['memory_cost']
        submission.problem.update_submission(
            submission.result, submission.user)
        submission.save()
        submissionToken.delete()
        return Response(status=status.HTTP_200_OK)
