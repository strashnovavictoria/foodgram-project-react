from django import forms
from django.forms import widgets

from recipes.models import Tag


class ColorPicker(widgets.Input):
    input_type = 'text'
    template_name = 'recipes/color_picker_2.html'


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        widgets = {
            'color': ColorPicker,
        }
        fields = '__all__'
