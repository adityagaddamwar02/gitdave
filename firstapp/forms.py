from django import forms
from firstapp.models import User


class User(forms.ModelForm):
    class Meta:
        model=User
        fiels='__all__'
