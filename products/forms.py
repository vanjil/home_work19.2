from django import forms
from .models import Announcement
from .mixins import CrispyFormMixin

class AnnouncementForm(CrispyFormMixin, forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'category', 'year', 'price', 'location', 'contact_info', 'photo']
        exclude = ('views_counter',)
        widgets = {
            'available': forms.widgets.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)#переопределиние инициализации , возможность добавить функцию в будущем

    def clean_title(self):
        title = self.cleaned_data.get('title')
        prohibited_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]
        for word in prohibited_words:
            if word in title.lower():
                raise forms.ValidationError(f"Название не должно содержать запрещенные слова: {word}")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        prohibited_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]
        for word in prohibited_words:
            if word in description.lower():
                raise forms.ValidationError(f"Описание не должно содержать запрещенные слова: {word}")
        return description
