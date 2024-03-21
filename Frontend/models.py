from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Name = models.CharField(max_length=50,null=True, blank=True)
    Email_id = models.EmailField(max_length=50,null=True, blank=True)
    Subject = models.CharField(max_length=100,null=True, blank=True)
    Message = models.CharField(max_length=100,null=True, blank=True)

class RedisterDb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email_id = models.EmailField(max_length=50, null=True, blank=True, unique=True)
    Password = models.CharField(max_length=50, null=True, blank=True)

class CartDb(models.Model):
    Username = models.CharField(max_length=20, null=True, blank=True)
    Productname = models.CharField(max_length=20, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Totalprice = models.IntegerField(null=True, blank=True)


class CheckoutDb(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    State = models.CharField(max_length=20, null=True, blank=True)
    Street_Address = models.CharField(max_length=10, null=True, blank=True)
    Town = models.CharField(max_length=10, null=True, blank=True)
    Postcode = models.IntegerField(null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Email_Address = models.CharField(max_length=100, null=True, blank=True)
