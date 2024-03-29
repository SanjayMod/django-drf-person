from django.db import models

# Create your models here.


class Person(models.Model):
    """ Model: Person """

    # Field declarations
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
