from datetime import date

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=120, unique=True)
    description = models.TextField()


class Feedback(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    positive = models.BooleanField()
    date = models.DateField(default=date.today)
