from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Books(models.Model):
    title = models.CharField(max_length=100) 
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    url = models.URLField(max_length=100)
    created_at = models.DateField(null=True, editable=False, blank=True, auto_now_add=True)
