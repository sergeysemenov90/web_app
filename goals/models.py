from django.contrib.auth.models import User
from django.db import models


class Goals(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
