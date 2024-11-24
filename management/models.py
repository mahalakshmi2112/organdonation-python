from django.db import models

# Create your models here.
class Donor(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    blood_type=models.CharField(max_length=3)
    organ=models.CharField(max_length=50)
    contactinfo=models.CharField(max_length=50)
    class meta:
        db_table="donor"
class Recipient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    blood_type=models.CharField(max_length=3)
    organ=models.CharField(max_length=15)
    contactinfo=models.CharField(max_length=50)
    class meta:
        db_table="recipient"