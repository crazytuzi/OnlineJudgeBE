from rest_framework import serializers
from .models import Contests
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
        return obj.end_time > timezone.now()

    class Meta:
        model = Contests
        fields = "__all__"
