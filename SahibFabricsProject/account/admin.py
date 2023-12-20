from django.contrib import admin
from .models import User_model
from .models import Thaans_model
# Register your models here.
@admin.register(User_model)
class UserAdmin(admin.ModelAdmin):
    list_display= ('id','username','email','password')

@admin.register(Thaans_model)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','Thaan_Category','Thaan_Model','Thaan_Qty','Thaan_Gazana','Thaan_Price_Per_Meter','Thaan_Shop_No')