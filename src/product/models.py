from django.db import models

# Create your models here. PRODUCT
class Product(models.Model):
        title = models.CharField(max_length=120)
        description = models.TextField(blank=True, null=True)
        price = models.DecimalField(decimal_places=2, max_digits=10000)
        summary = models.TextField(blank=True, null=True)
        featured = models.BooleanField()

# USER
class User(models.Model):
        # userID = models.AutoField()
        name = models.CharField(max_length=30)
        family = models.CharField(max_length=50)
        ssn = models.BigIntegerField()
        email = models.EmailField(unique=True)
        phoneNumber = models.DecimalField(decimal_places=0, max_digits=11)
        iban = models.CharField(max_length=24)

