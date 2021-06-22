from django.conf import settings
from django.conf.urls.static import static
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

    # API
    path('api/', include('users.api.urls')),
    path('api/', include('events.api.urls')),
    path('api/', include('notifications.api.urls')),

    path("accounts/", include('django_registration.backends.one_step.urls')),
    path("accounts/", include('django.contrib.auth.urls')),
    path('accounts/', include('rest_registration.api.urls')),

    path('api-auth/', include('rest_framework.urls')),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)