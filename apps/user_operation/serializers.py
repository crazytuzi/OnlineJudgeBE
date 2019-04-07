from rest_framework import serializers
from .models import UserCollect, UserAcceptedProblems, UserChallengingProblems


class UserCollectSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(
        read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = UserCollect
        fields = "__all__"


class UserAcceptedProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAcceptedProblems
        fields = "__all__"


class UserChallengingProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChallengingProblems
        fields = "__all__"
