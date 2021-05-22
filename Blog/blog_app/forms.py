from captcha.fields import CaptchaField
from django import forms
from .models import BlogPost

class CaptchaForm(forms.Form):
    # Verification code field
    captcha = CaptchaField() 

class BlogForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=("title","content","image","public")