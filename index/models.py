from django.db import models

# Create your models here.


class Contect(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    concern = models.TextField(max_length=250)

    def __str__(self):
        return self.name
