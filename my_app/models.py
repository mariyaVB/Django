from django.db import models


class Painter(models.Model):
    name = models.CharField(max_length=40)
    biography = models.TextField(default=None)


class QuestionAnswer(models.Model):
    question = models.CharField(max_length=200)
    date_question = models.DateField(auto_now_add=True)









