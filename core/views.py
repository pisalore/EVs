from django.views.generic.base import TemplateView
from django.conf import settings


class IndexTemplateView(TemplateView):

    def get_template_names(self):
        template_name = 'index.html'
        return template_name
