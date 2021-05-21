from django import forms
from django_registration.forms import RegistrationForm

from evsapp import settings
from users.models import EvUser


class EvUserForm(RegistrationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Your Birthday'}),
                               input_formats=settings.DATE_INPUT_FORMATS)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    def __init__(self, *args, **kwargs):
        super(EvUserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super(EvUserForm, self).save(commit=False)
        user.is_organizer = False
        if commit:
            user.save()
        return user

    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     if EvUser.objects.filter(email=email).exists():
    #         raise ValidationError("Email exists")
    #     return self.cleaned_data

    class Meta(RegistrationForm.Meta):
        model = EvUser
        fields = ["first_name", "last_name", "username", "password1", "password2", "email", "city",
                  "birthday"]


class EvOrganizerForm(RegistrationForm):
    organization_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Institution/Organization'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    def __init__(self, *args, **kwargs):
        super(EvOrganizerForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        organizer = super(EvOrganizerForm, self).save(commit=False)
        organizer.is_organizer = True
        if commit:
            organizer.save()
        return organizer

    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     if EvUser.objects.filter(email=email).exists():
    #         raise ValidationError("Email exists")
    #     return self.cleaned_data

    class Meta(RegistrationForm.Meta):
        model = EvUser
        fields = ["username", "organization_name", "password1", "password2", "email"]
