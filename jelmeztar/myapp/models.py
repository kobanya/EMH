from django.db import models
from django.contrib.auth.models import User


class MyData(models.Model):
    # itt jönnek a mezők definíciói, például:
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
