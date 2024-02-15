from django.db import models



class User_model(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)


class Product(models.Model):
    category = models.CharField(max_length=100,null=True)    
    name=models.CharField(max_length=200,null=True)
    qty=models.IntegerField(null=True)
    gazana=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    shop=models.CharField(max_length=3,null=True)
    
    def __str__(self):
        return self.name

class Client(models.Model):
    name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=500,null=True)
    city=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=15,null=True)
    balance=models.IntegerField(default=0,null=True)

    def __str__(self):
        return self.name


#testing

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    invoice_date = models.DateField()
    #customer = models.ForeignKey('Client', on_delete=models.CASCADE)
    customer=models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add any other fields relevant to your invoices

    def __str__(self):
        return self.invoice_number
