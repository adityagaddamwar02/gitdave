from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=50)
    def __str__(self):
        return self.firstname
        return self.lastname
        return self.Email

