from django.db import models
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    is_mvp = models.BooleanField()
    hire_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name