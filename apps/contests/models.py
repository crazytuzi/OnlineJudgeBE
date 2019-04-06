from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
from django.utils import timezone

User = get_user_model()


class Contests(models.Model):
    contest_id = models.IntegerField(
        db_index=True, default=0, verbose_name="比赛编号")
    title = models.CharField(unique=True, max_length=255, verbose_name="标题")
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    create_by = models.ForeignKey(
        User, blank=True, verbose_name="创建人", null=True)

    def isOverdue(self):
        return self.end_time < timezone.now()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "比赛"
        verbose_name_plural = verbose_name
        ordering = ['-end_time']
        db_table = "contests"


class ContestRankList(models.Model):
    contest = models.ForeignKey(Contests, verbose_name="比赛")
    user = models.ForeignKey(User, verbose_name="用户")
    accepted = models.IntegerField(default=0, verbose_name="通过数量")
    preaccepted_time = models.DateTimeField(
        auto_now_add=True, verbose_name="上一次通过时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "比赛排名"
        verbose_name_plural = verbose_name
        ordering = ['-accepted', 'preaccepted_time', 'create_time']
        db_table = "contestranklist"
