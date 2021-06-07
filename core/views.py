from django.views.generic.base import TemplateView
import os


class IndexTemplateView(TemplateView):

    def get_template_names(self):
        if os.getenv('DEBUG') == 'True':
            template_name = 'index-dev.html'
        else:
            template_name = 'index.html'
        return template_name
