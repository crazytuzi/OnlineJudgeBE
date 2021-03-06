from django.db import models
from django.contrib.auth import get_user_model
from contests.models import Contests
from problems.models import Problems
from Utlis.JudgeStatus import JudgeStatus

# Create your models here.
User = get_user_model()


class Submissions(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    contest = models.ForeignKey(
        Contests,
        verbose_name="比赛",
        blank=True,
        null=True)
    problem = models.ForeignKey(Problems, verbose_name="题目")
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name="提交时间")
    result = models.IntegerField(
        db_index=True,
        default=JudgeStatus.PENDING,
        verbose_name="结果")
    memory_cost = models.IntegerField(default=0, verbose_name="运行时间")
    time_cost = models.IntegerField(default=0, verbose_name="运行内存")
    language = models.IntegerField(default=0, verbose_name="编程语言")
    code = models.TextField(default=None, verbose_name="代码")

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-submit_time']
        verbose_name = "提交记录"
        verbose_name_plural = verbose_name
        db_table = "submissions"


class SubmissionToken(models.Model):
    submission = models.ForeignKey(Submissions)
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.submission.user.username

    class Meta:
        verbose_name = "提交记录Token"
        verbose_name_plural = verbose_name
        db_table = "submission_token"
