from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, default='В процессе')
