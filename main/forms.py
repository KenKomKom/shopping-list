from django import forms
from main.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
    error_messages = {
                'name' : {'required':"WOI"}
                }
    input_attrs = {
                'type' : 'text',
                'placeholder' : 'Nama Kamu'
                }

    
    nama = forms.CharField(label='anjing', required=True, max_length=27,\
                            widget=forms.TextInput(attrs=input_attrs), error_messages={'required' : 'WOI!'})