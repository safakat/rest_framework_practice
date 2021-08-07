from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
# Create your models here.

sex_choice = (('MALE','Male'),('Female','Female'),('Others','Others'))
file_location = FileSystemStorage(location='/media/images')
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sex = models.CharField(choices=sex_choice,max_length=10,default='Others')
    image = models.ImageField(null = True, blank = True)

    # On save update the image name
    def save(self, *args, **kwargs):
        self.image = "hello.jpg"
        return super(Profile, self).save(*args,**kwargs)


    def __str__(self):
        return str(self.user)
