from rest_framework import serializers
from .models import Contests, ContestRankList
from django.utils import timezone


class ContestsSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    creator = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()

    def get_creator(self, obj):
        if obj.create_by is not None:
            return obj.create_by.username
        else:
            return None

    def get_state(self, obj):
        if obj.start_time > timezone.now():
            return 0
        elif obj.end_time < timezone.now():
            return 2
        else:
            return 1

    class Meta:
        model = Contests
        fields = "__all__"


class ContestRankListSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    preaccepted_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    username = serializers.SerializerMethodField()
    timeused = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_timeused(self, obj):
        return obj.preaccepted_time - obj.contest.start_time

    class Meta:
        model = ContestRankList
        fields = "__all__"
