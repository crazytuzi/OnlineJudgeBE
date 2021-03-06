from rest_framework import serializers
from .models import Submissions, SubmissionToken


class SubmissionsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    submit_time = serializers.DateTimeField(
        read_only=True, format="%Y-%m-%d %H:%M:%S")
    parent = serializers.SerializerMethodField(read_only=True)

    def get_username(self, obj):
        return obj.user.username

    def get_parent(self, obj):
        if obj.problem.parent_problem is not None:
            return obj.problem.parent_problem.problem_id
        else:
            return None

    def create(self, validated_data):
        problem = validated_data['problem']
        validated_data['time_cost'] = problem.time_limit
        validated_data['memory_cost'] = problem.memory_limit
        validated_data['contest'] = problem.contest
        return Submissions.objects.create(**validated_data)

    class Meta:
        model = Submissions
        fields = "__all__"


class SubmissionTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionToken
        fields = "__all__"
