from django.db import models


class User(models.Model):
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
