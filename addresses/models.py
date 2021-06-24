from django.db import models

# Create your models here.
class Address(models.Model):
    postal_code=models.IntegerField()
    municipality=models.CharField(max_length=100)
    state =models.CharField(max_length=100)


    def __str__(self):
        return f'direccion de {self.municipality}'