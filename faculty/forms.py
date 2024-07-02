from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField
import random ,string

class Faculty_register(forms.Form):
    email = forms.EmailField()
    captcha = CaptchaField()