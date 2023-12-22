from django.db import models
import datetime
from Musicians.models import Musicians
# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    musician = models.ForeignKey(Musicians, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
