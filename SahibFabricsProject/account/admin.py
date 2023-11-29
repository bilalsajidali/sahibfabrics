from django.contrib import admin
from .models import User_model
from .models import Suits_model
# Register your models here.
@admin.register(User_model)
class UserAdmin(admin.ModelAdmin):
    list_display= ('id','username','email','password')

@admin.register(Suits_model)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','Suit_Category','Suit_Model','Suit_Qty','Suit_Gazana','Suit_Price_Per_Meter','Suit_Shop_No')