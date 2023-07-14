from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)


    def __str__(self):
        return self.email, self.email, self.password
