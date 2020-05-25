from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button
from django import forms
from ..models import *

class CarEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CarEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'

        self.helper.add_input(Button('delete', 'Delete', onclick='window.location.href="{}"'.format('delete')))

    brand = forms.CharField(max_length=32)
    model = forms.CharField(max_length=32)
    color = forms.CharField(max_length=16)
    fuel_util = forms.CharField(max_length=5)
    of_enterprise = forms.CharField(max_length=16)

    class Meta:
        model = Car
        fields = ('brand', 'model', 'color', 'fuel_util')