from django import forms
from register.models import Register_mdl


class RegisterForm(forms.ModelForm):
    class Meta():
        model = Register_mdl
        fields = ["name","surname","email","password"]
