from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "比赛"
        verbose_name_plural = verbose_name
        ordering = ['-end_time']
        db_table = "contests"

    def status(self):
        pass
