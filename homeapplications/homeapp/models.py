from django.db import models

class Person(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=600)
    date = models.DateField()
    image = models.ImageField(upload_to='homeapp/images' ,default="") # Not Recommended

    # Shows name of Product in DB
    def __str__(self):
        return self.name