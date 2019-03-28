from django_filters import rest_framework
import django_filters
from .models import UserCollect, UserAcceptedProblems, UserChallengingProblems
from Utlis.NullFilter import NullFilter


class UserCollectFilter(rest_framework.FilterSet):
    class Meta:
        model = UserCollect
        fields = ['user', 'problem']


class UserAcceptedProblemFilter(rest_framework.FilterSet):
    iscontest = NullFilter(field_name="problem__contest")
    problem__contest = django_filters.NumberFilter()

    class Meta:
        model = UserAcceptedProblems
        fields = ['user', 'iscontest', 'problem__contest']


class UserChallengingProblemFilter(rest_framework.FilterSet):
    class Meta:
        model = UserChallengingProblems
        fields = ['user']
