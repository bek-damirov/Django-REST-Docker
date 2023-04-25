from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return f'{self.username}'


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=30)
    telegram_chat_id = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.user}'



