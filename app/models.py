from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email=models.CharField(unique=True)
    

# Create your models here.
class Task(models.Model):
    fk=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)

