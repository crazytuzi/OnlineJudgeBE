from rest_framework import serializers
from .models import Problems, ContentProblems


class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = "__all__"


class ContestProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentProblems
        fields = "__all__"
