#from django import forms
import re
from django.contrib.auth.models import User
from django import forms
from django.contrib import auth

from ChatBot.views.misc.Constants import *


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ValidatingPasswordChangeForm(auth.forms.PasswordChangeForm):
    MIN_LENGTH = 8

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')

        # At least MIN_LENGTH long
        if len(password1) < self.MIN_LENGTH:
            raise forms.ValidationError(PASS_LENGTH_ERROR)

        if re.search(r'(?=(?:.*[A-Z]){2})', password1) is None:
            raise forms.ValidationError(PASS_UPPERCASE_ERROR)

        if re.search(r'(?=(?:.*[0-9]){2})', password1) is None:
            raise forms.ValidationError(PASS_NUMBER_ERROR)

        if re.search(r'(?=(?:.*[!@#$%&*-+]){2})', password1) is None:
            raise forms.ValidationError(PASS_SYMBOL_ERROR)
