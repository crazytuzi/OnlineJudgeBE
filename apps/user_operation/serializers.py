from rest_framework import serializers
from .models import UserCollect


class UserCollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCollect
        fields = "__all__"
