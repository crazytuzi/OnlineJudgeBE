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
    submission_id = models.IntegerField(
        db_index=True, default=0, verbose_name="提交编号")
    user = models.ForeignKey(User, verbose_name="用户")
    contest = models.ForeignKey(Contests, verbose_name="比赛")
    problem = models.ForeignKey(Problems, verbose_name="题目")
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name="提交时间")
    result = models.IntegerField(
        db_index=True,
        default=JudgeStatus.PENDING,
        verbose_name="结果")
    memory_cost = models.IntegerField(default=0, verbose_name="运行时间")
    time_cost = models.IntegerField(default=0, verbose_name="运行内存")
    code = models.TextField(default=None, verbose_name="代码")

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = "提交记录"
        verbose_name_plural = verbose_name
        db_table = "submissions"

    def check_permission(self):
        pass
