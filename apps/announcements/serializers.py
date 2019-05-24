from rest_framework import serializers
from .models import Announcements


class AnnouncementsSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    creator = serializers.SerializerMethodField()

    def get_creator(self, obj):
        if obj.create_by is not None:
            return obj.create_by.username
        else:
            return None

    class Meta:
        model = Announcements
        fields = "__all__"
