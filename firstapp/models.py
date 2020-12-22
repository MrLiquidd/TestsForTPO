from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Client(models.Model):
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    pol = models.CharField(max_length=50)
    age = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return self.login


class History(models.Model):
    author = models.ForeignKey(Client, on_delete=models.CASCADE)
    result = models.TextField()

    def __str__(self):
        return self.result
