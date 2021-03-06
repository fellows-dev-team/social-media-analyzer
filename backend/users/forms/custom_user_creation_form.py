from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from ..models import SiteUser


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control text-white',
                'placeholder': 'Password',
            }
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control text-white',
                'placeholder': 'Password',
            }
        )

    class Meta(UserCreationForm.Meta):
        model = SiteUser
        fields = ('username', 'email', 'timezone')

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'username',
                    'required': True,
                    'class': 'form-control text-white',
                    'name': 'Username',
                },
            ),
            'email': forms.TextInput(
                attrs={
                    'required': True,
                    'class': 'form-control text-white',
                    'placeholder': 'Email',
                }
            ),
            'timezone': forms.Select(
                attrs={
                    'required': True,
                    'class': 'form-control text-white',
                }
            )
        }
