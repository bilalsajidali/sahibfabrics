from django import forms
from .models import Product
from .models import User_model
from .models import Client
from .models import Invoice


class AddStock_form(forms.ModelForm):
    THAAN_CATEGORY_CHOICES = [
        ('', '-----'),
        ('Cotton', 'Cotton'),
        ('Karandi', 'Karandi'),
        ('washnwear', 'Washnwear'),
        ('Latha', 'Latha'),
        ('Boski', 'Boski'),
        ('Khaddar', 'Khaddar'),
        ('BoxPacking', 'BoxPacking'),
        ('Other', 'Other'),
    ]
    
    
    category = forms.ChoiceField(choices=THAAN_CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        shop_choices=['1']
        model = Product
        fields = ['category', 'name', 'qty', 'gazana', 'price', 'shop']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'qty': forms.TextInput(attrs={'class': 'form-control'}),
            'gazana': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            }

    SHOP_CHOICES=[('', '-----'),
                ('61','61'),
                ('100','100'),
                ('392','392')]
    shop = forms.ChoiceField(choices=SHOP_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


        

class client_form(forms.ModelForm):
    class Meta():
        model=Client
        fields=['name','address','city','phone','balance']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'balance':forms.TextInput(attrs={'class':'form-control'}),
            
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

#testing

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'invoice_date', 'customer']