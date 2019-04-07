from rest_framework import filters, status
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from .models import UserCollect, UserAcceptedProblems, UserChallengingProblems
from .serializers import UserCollectSerializer, UserAcceptedProblemSerializer, UserChallengingProblemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserCollectFilter, UserAcceptedProblemFilter, UserChallengingProblemFilter

# Create your views here.


class UserCollectListViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    queryset = UserCollect.objects.all()
    serializer_class = UserCollectSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = UserCollectFilter
    ordering_fields = ('create_time',)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_anonymous or request.user != instance.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()


class UserAcceptedProblemListViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    queryset = UserAcceptedProblems.objects.all()
    serializer_class = UserAcceptedProblemSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = UserAcceptedProblemFilter
    ordering_fields = ('create_time',)


class UserChallengingProblemListViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    queryset = UserChallengingProblems.objects.all()
    serializer_class = UserChallengingProblemSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = UserChallengingProblemFilter
    ordering_fields = ('create_time',)
