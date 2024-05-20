from django.forms import ModelForm
from django import forms

from products.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('views_counter',)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        for word in prohibited_words:
            if word in name.lower():
                raise forms.ValidationError(f"Название не должно содержать запрещенные слова: {word}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        for word in prohibited_words:
            if word in description.lower():
                raise forms.ValidationError(f"Описание не должно содержать запрещенные слова: {word}")
        return description