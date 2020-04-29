from django.db import models
from django.utils.timezone import now
# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=50)
    shop_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date_time= models.DateTimeField(default=now)