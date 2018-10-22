from django_filters import rest_framework
import django_filters
from django.contrib.auth import get_user_model
User = get_user_model()


class UsersFilter(rest_framework.FilterSet):
    username = django_filters.CharFilter()
    email = django_filters.CharFilter()

    class Meta:
        model = User
        fields = ['username', 'email']
