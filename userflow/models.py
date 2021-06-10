from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    picture=models.ImageField(upload_to="profiles/",null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField(null=True)

    def delete(self,*args,**kwargs):
        self.picture.delete()
        super().delete(*args,**kwargs)