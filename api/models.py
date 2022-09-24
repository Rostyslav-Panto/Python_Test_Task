from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(default=timezone.now)


@receiver(post_save, sender=User)
def create_my_user(sender, instance, created, **kwargs):
    if created:
        MyUser.objects.create(user=instance)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=120, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    positive = models.BooleanField()
    date = models.DateField(default=date.today)

    class Meta:
        unique_together = (
            'author',
            'post_id'
        )
