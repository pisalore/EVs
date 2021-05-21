from django.contrib import admin
from django.urls import path, include, re_path
from django_registration.backends.one_step.views import RegistrationView
from core.views import IndexTemplateView

from users.forms import EvUserForm, EvOrganizerForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/register/user/",
         RegistrationView.as_view(
             form_class=EvUserForm,
             success_url="/",
             template_name='django_registration/registration_form_user.html'
         ), name='django_registration_register_user'),

    path("accounts/register/organizer/",
         RegistrationView.as_view(
             form_class=EvOrganizerForm,
             success_url="/",
             template_name='django_registration/registration_form_organizer.html'
         ), name='django_registration_register_organizer'),

    path("accounts/", include('django_registration.backends.one_step.urls')),
    path("accounts/", include('django.contrib.auth.urls')),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]
