from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(
        max_length=100,
        unique=True,
        blank=False,
        verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/default.jpg')
    accepted_num = models.IntegerField(default=0)
    submission_num = models.IntegerField(default=0)
    ranking = models.IntegerField(default=0)

    def add_submission_number(self):
        self.submission_num = models.F("submission_num") + 1
        self.save(update_fields=["submission_num"])

    def add_accepted_number(self):
        self.accepted_num = models.F("accepted_num") + 1
        self.save(update_fields=["accepted_num"])

    def sortUserRankList(self):
        objects = UserProfile.objects.order_by(
            "-accepted_num",
            "submission_num",
            "user__date_joined")
        for i in range(0, objects.count()):
            obj = objects.all()[i]
            obj.ranking = i + 1
            obj.save()

    class Meta:
        ordering = ["ranking"]
