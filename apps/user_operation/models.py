from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from problems.models import Problems

# Create your models here.
User = get_user_model()


class UserCollect(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户")
    problems = models.ForeignKey(Problems, verbose_name="题目")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name
        unique_together = ("user", "problems")

    def __str__(self):
        return self.user.username
