from django import forms
from .models import Item

INPUT_CLASSES = 'w-1/3 px-6 py-3 bg-gray-50 rounded-xl'

class NewItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ("category","name","description","price","image")

        widgets = {
            'category' : forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'name' : forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description' : forms.Textarea(attrs={
                'class': 'w-full px-6 py-4 bg-gray-50 rounded-xl',
            }),
            'price' : forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
           
        }

    

