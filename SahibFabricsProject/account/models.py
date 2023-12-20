from django.db import models



# Create your models here.

class User_model(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)


class Thaans_model(models.Model):
    Thaan_Category = models.CharField(max_length=100)    
    Thaan_Model=models.CharField(max_length=200)
    Thaan_Qty=models.IntegerField()
    Thaan_Gazana=models.IntegerField()
    Thaan_Price_Per_Meter=models.IntegerField()
    Thaan_Shop_No=models.CharField(max_length=3)