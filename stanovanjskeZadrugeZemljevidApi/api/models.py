from django.db import models


class Map(models.Model):
    map = models.JSONField()


class Message(models.Model):
    index = models.PositiveIntegerField()
    text = models.TextField()


class Token(models.Model):
    token = models.CharField(max_length=255)
    used = models.BooleanField(default=False)
    used_message = models.BooleanField(default=False)
    admin_token = models.BooleanField(default=False)
