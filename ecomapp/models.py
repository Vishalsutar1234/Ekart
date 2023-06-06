from django.db import models

# Create your models here.
class Product(models.Model):
    CAT=((1,'Mobile'),(2,'Cloths'),(3,'Shoes'))
    name=models.CharField(max_length=50,verbose_name="Product Name")
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    price=models.FloatField(verbose_name="Product Price")
    status=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to="image")

    def __str__(self):
        
        return self.name
