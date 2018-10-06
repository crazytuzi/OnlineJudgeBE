from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """
    用户
    """
    email = models.EmailField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.TextField(
        default=f"{settings.AVATAR_URI_PREFIX}/default.png")
    accepted_number = models.IntegerField(default=0)
    submission_number = models.IntegerField(default=0)

    def add_accepted_number(self):
        self.accepted_number = models.F("accepted_number") + 1
        self.save()

    def add_submission_number(self):
        self.submission_number = models.F("submission_number") + 1
        self.save()
