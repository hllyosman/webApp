from django import forms
from .models import Staff, Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['last_name', 'first_name', 'last_kana', 'first_kana', 'email', 'tel', 'ctgry', 'pcharge', 'inquiry']

        widgets = {
            'last_name' : forms.TextInput(attrs={'placeholder': '姓'}),
            'first_name' : forms.TextInput(attrs={'placeholder': '名'}),
            'last_kana' : forms.TextInput(attrs={'placeholder': 'セイ'}),
            'first_kana' : forms.TextInput(attrs={'placeholder': 'メイ'}),
        }
