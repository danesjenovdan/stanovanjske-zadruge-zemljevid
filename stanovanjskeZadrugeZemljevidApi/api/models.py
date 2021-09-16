from django.db import models

class Map(models.Model):
    map = models.JSONField()

class Message(models.Model):
    index = models.PositiveIntegerField()
    text = models.TextField()
