from django.contrib.auth.hashers import make_password
from django.forms import ModelForm

from apps.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_password(self):
        return make_password(self.cleaned_data['password'])


class UpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('phone', 'first_name', 'last_name', 'location', 'email', 'organization_name', 'image', 'birthday')

