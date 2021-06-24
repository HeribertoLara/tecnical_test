from django.db import models
from addresses.models import Address

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    adress=models.ManyToManyField(Address, related_name='users')

    def __str__(self):
        return f'{self.full_name}'
