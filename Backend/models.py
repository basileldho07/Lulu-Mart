from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=200, null=True, blank=True)
    ProfileImage = models.ImageField(upload_to="image", null=True, blank=True)

class ProductDb(models.Model):
    Category_Name = models.CharField(max_length=50,null=True, blank=True)
    Products_Name = models.CharField(max_length=50,null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100,null=True, blank=True)
    ProductImage = models.ImageField(upload_to="image", null=True, blank=True)
