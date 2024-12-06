from django import forms
from .models import UserAccount
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class meta:
        model = UserAccount
        fields = ['username', 'password1', 'password2', 'email', 'role']


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['username', 'password', 'email', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }

    # Optional: Custom validation to confirm passwords match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.data.get('confirmPassword')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data
