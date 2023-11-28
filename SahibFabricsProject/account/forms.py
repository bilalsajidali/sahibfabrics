from django import forms
from .models import Suits_model

class AddStock_form(forms.ModelForm):
    class Meta():
        model=Suits_model
        fields=['Suit_Category','Suit_Model','Suit_Qty','Suit_Gazana','Suit_Price_Per_Meter','Suit_Shop_No']
        widgets={
            'Suit_Category':forms.TextInput(attrs={'class':'form-control'}),
            'Suit_Model':forms.TextInput(attrs={'class':'form-control'}),
            'Suit_Qty':forms.TextInput(attrs={'class':'form-control'}),
            'Suit_Gazana':forms.TextInput(attrs={'class':'form-control'}),
            'Suit_Price_Per_Meter':forms.TextInput(attrs={'class':'form-control'}),
            'Suit_Shop_No':forms.TextInput(attrs={'class':'form-control'}),
            
        }