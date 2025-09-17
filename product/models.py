from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField(default="")

    image=models.ImageField(upload_to="products/")
  
    class Meta:
        db_table="products"

