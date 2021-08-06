from django.db import models

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=25, null=False, blank=False)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField()

    def __str__(self):
        return self.username
