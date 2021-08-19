from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    inventor = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    comment = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.product_name

class Engineers(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    details = models.CharField(max_length=200,default="")
    profile_pic = models.ImageField(upload_to="tuts/images",default="")

    def __str__(self):
        return self.name