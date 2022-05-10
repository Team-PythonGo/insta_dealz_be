from email.policy import default
from django.contrib.auth import get_user_model
from django.db import models


class Thing(models.Model):
    image=models.ImageField(default="")
    name = models.CharField(max_length=256)
    


    def __str__(self):
        return self.name
