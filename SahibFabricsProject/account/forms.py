from django import forms
from .models import Thaans_model
from .models import User_model

class AddStock_form(forms.ModelForm):
    class Meta():
        model=Thaans_model
        fields=['Thaan_Category','Thaan_Model','Thaan_Qty','Thaan_Gazana','Thaan_Price_Per_Meter','Thaan_Shop_No']
        widgets={
            'Thaan_Category':forms.TextInput(attrs={'class':'form-control'}),
            'Thaan_Model':forms.TextInput(attrs={'class':'form-control'}),
            'Thaan_Qty':forms.TextInput(attrs={'class':'form-control'}),
            'Thaan_Gazana':forms.TextInput(attrs={'class':'form-control'}),
            'Thaan_Price_Per_Meter':forms.TextInput(attrs={'class':'form-control'}),
            'Thaan_Shop_No':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class register_form(forms.ModelForm):
    class Meta():
        model=User_model
        fields=['username','email','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
           
        }