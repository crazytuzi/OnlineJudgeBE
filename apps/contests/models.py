from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Contests(models.Model):
    contest_id = models.IntegerField(db_index=True, default=0)
    title = models.CharField(unique=True, max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(User, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "contest"
        db_table = "contests"

    def status(self):
        pass
