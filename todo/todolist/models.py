from django.db import models

# Create your models here.


class Card(models.Model):

    title = models.CharField(max_length=128)
    content=models.CharField(max_length=512)
    date = models.DateField()


    def __str__(self):
        return self.title