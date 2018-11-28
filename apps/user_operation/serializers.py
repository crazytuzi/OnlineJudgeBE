from rest_framework import serializers
from .models import UserCollect, UserAcceptedProblems


class UserCollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCollect
        fields = "__all__"


class UserAcceptedProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAcceptedProblems
        fields = "__all__"
