from django import forms
from users.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        field = "__all__"
