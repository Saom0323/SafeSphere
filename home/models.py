from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class EmergencyReport(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    emergency_type = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name