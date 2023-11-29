from django.db import models



# Create your models here.

class User_model(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)


class Suits_model(models.Model):
    Suit_Category=models.CharField(max_length=100)
    Suit_Model=models.CharField(max_length=200)
    Suit_Qty=models.IntegerField()
    Suit_Gazana=models.IntegerField()
    Suit_Price_Per_Meter=models.IntegerField()
    Suit_Shop_No=models.CharField(max_length=3)