from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from problems.models import Problems

# Create your models here.


User = get_user_model()


class UserCollect(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    problem = models.ForeignKey(Problems, verbose_name="题目")
    create_time = models.DateTimeField(
        default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name
        unique_together = ("user", "problem")
        db_table = "user_collect"

    def __str__(self):
        return self.user.username


class UserAcceptedProblems(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    problem = models.ForeignKey(Problems, verbose_name="题目")
    create_time = models.DateTimeField(
        default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户通过题目"
        verbose_name_plural = verbose_name
        unique_together = ("user", "problem")
        db_table = "user_acceptedproblems"

    def __str__(self):
        return self.user.username
