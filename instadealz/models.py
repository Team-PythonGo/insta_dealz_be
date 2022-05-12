from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    image = models.CharField(default="", max_length=256)
    name = models.CharField(max_length=256)
    description = models.TextField(default="")
    details = models.TextField(default="")
    price = models.IntegerField(default=0)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
