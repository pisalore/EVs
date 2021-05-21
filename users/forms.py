from django import forms
from django_registration.forms import RegistrationForm

from users.models import EvUser


class EvUserForm(RegistrationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Date of Birth'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta(RegistrationForm.Meta):
        model = EvUser
        fields = ["first_name", "last_name", "username", "password1", "password2", "email", "city",
                  "birthday"]


class EvOrganizerForm(RegistrationForm):
    organization_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Institution/Organization'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Date of Birth'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta(RegistrationForm.Meta):
        model = EvUser
        fields = ["organization_name", "password1", "password2", "email"]
