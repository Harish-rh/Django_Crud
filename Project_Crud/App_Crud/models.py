from django.db import models


class RegisterForm(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
