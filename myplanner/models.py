from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_name = models.CharField(max_length=100)
    completed = models.BooleanField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task_name


class Quote(models.Model):
    quote_text = models.CharField(max_length=500)
    author = models.CharField(default="annonymous", max_length=250)

    def __str__(self):
        return self.quote_text + '--' + self.author + '--'

