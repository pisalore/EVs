from django import forms
from django_registration.forms import RegistrationForm

from users.models import EvUser


class EvUserForm(RegistrationForm):
    city = forms.CharField(max_length=100)

    class Meta(RegistrationForm.Meta):
        model = EvUser
        fields = ["username", "password1", "password2", "email", "city"]
