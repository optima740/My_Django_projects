from crispy_forms.helper import FormHelper
from django import forms
from .models import *
# формы.
from django.urls import reverse


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ('title', 'address')
    def __init__(self, *args, **kwargs):
        super(EnterpriseForm, self).__init__(*args, **kwargs)

    # this helper object allows us to customize form
        self.helper = FormHelper()


    # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'get'


    # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

