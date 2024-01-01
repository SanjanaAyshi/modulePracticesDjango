from django.db import models

# Create your models here.


class Musicians(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    PhoneNumber = models.IntegerField()
    InstrumentType = models.CharField(max_length=500)

    def __str__(self):
        return f'name: {self.firstname} {self.lastname}'
