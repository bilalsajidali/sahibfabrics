from django.contrib import admin
from .models import User
from .models import Suits_model
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ('id','name','email','password')

@admin.register(Suits_model)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','Suit_Category','Suit_Model','Suit_Qty','Suit_Gazana','Suit_Price_Per_Meter','Suit_Shop_No')