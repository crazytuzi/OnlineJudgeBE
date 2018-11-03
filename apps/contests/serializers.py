from rest_framework import serializers
from .models import Contests


class ContestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contests
        fields = "__all__"
