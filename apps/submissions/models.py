from django.db import models
from django.contrib.auth import get_user_model
from contests.models import Contests
from problems.models import Problems

# Create your models here.
User = get_user_model()


class JudgeStatus:
    COMPILE_ERROR = -2
    WRONG_ANSWER = -1
    ACCEPTED = 0
    CPU_TIME_LIMIT_EXCEEDED = 1
    REAL_TIME_LIMIT_EXCEEDED = 2
    MEMORY_LIMIT_EXCEEDED = 3
    RUNTIME_ERROR = 4
    SYSTEM_ERROR = 5
    PENDING = 6
    JUDGING = 7
    PARTIALLY_ACCEPTED = 8


class Submissions(models.Model):
    submission_id = models.IntegerField(db_index=True, default=0)
    user = models.ForeignKey(User)
    contest = models.ForeignKey(Contests)
    problem = models.ForeignKey(Problems)
    submit_time = models.DateTimeField(auto_now_add=True)
    result = models.IntegerField(db_index=True, default=JudgeStatus.PENDING)
    memory_cost = models.IntegerField(default=0)
    time_cost = models.IntegerField(default=0)
    code = models.TextField(default=None)

    def check_permission(self):
        pass
