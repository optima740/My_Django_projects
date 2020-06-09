from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class PayCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Customer
        fields = ('first_name', 'last_name', 'award')

class RedemtionForm(UserChangeForm):

    class Meta:
        model = Redemption
        fields = ('username', 'email')