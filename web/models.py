from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name
