from django.db import models
from datetime import datetime
from django.contrib.auth.admin import User


class Post(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField(default=datetime.now)
    text=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    show=models.BooleanField(default=False,)
    