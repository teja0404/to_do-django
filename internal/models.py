from django.db import models

# Create your models here.

class names(models.Model):

    first_name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.first_name


    