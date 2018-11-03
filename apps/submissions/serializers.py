from rest_framework import serializers
from .models import Submissions, SubmissionToken


class SubmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submissions
        fields = "__all__"


class SubmissionTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionToken
        fields = "__all__"
