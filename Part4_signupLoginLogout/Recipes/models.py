from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title