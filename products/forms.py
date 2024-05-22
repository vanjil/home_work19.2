from django import forms
from .models import Product
from .mixins import CrispyFormMixin

class ProductForm(CrispyFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('views_counter',)  # Или используйте fields, если хотите явно указать поля
        widgets = {
            'available': forms.widgets.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Примените дополнительные стили или настройки, если необходимо

    def clean_name(self):
        name = self.cleaned_data.get('name')
        prohibited_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]
        for word in prohibited_words:
            if word in name.lower():
                raise forms.ValidationError(f"Название не должно содержать запрещенные слова: {word}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        prohibited_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]
        for word in prohibited_words:
            if word in description.lower():
                raise forms.ValidationError(f"Описание не должно содержать запрещенные слова: {word}")
        return description
