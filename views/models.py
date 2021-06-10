from django.db import models
from classific.models import Image

# Create your models here.
class Infrerence(models.Model):
    image= models.ForeignKey(Image,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=244)
