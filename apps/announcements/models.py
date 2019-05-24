from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Announcements(models.Model):
    title = models.CharField(unique=True, max_length=255, verbose_name="标题")
    content = models.CharField(max_length=255, verbose_name="内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    create_by = models.ForeignKey(
        User, blank=True, verbose_name="创建人", null=True)
    class Meta:
        verbose_name = "公告"
        verbose_name_plural = verbose_name
        db_table = "announcements"
