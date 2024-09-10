from django import forms
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at",)

    def clean_name(self):
        wrong_list = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
                      'обман', 'полиция', 'радар')
        cleaned_data = self.cleaned_data['name']
        for wrong_str in wrong_list:
            if wrong_str in cleaned_data:
                raise forms.ValidationError('не стоит использовать это слово в названии')

        return cleaned_data

    def clean_description(self):
        wrong_list = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
                      'обман', 'полиция', 'радар')
        cleaned_data = self.cleaned_data['description']
        for wrong_str in wrong_list:
            if wrong_str in cleaned_data:
                raise forms.ValidationError(f'не стоит использовать слово "{wrong_str}" в описании')

        return cleaned_data


class VersionProductForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
