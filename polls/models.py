from django.db import models

# Create your models here.


class Question(models.Model):
    q_text = models.CharField(max_length=200)
    p_date = models.DateTimeField("published date")


class Choice(models.Model):
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

