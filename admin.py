from django.contrib import admin
from .models import User_model
from .models import Product
from .models import Client
from .models import Invoice



# Register your models here.
@admin.register(User_model)
class UserAdmin(admin.ModelAdmin):
    list_display= ('id','username','email','password')

@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','category','name','qty','gazana','price','shop')

@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','address','city','phone','balance')


@admin.register(Invoice)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','invoice_number','customer','total_amount')

    