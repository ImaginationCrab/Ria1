from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    def __str__(self):
        return self