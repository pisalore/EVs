from django.views.generic.base import TemplateView
import os


class IndexTemplateView(TemplateView):

    def get_template_names(self):
        print(os.getenv('DEBUG'))
        if os.getenv('DEBUG'):
            template_name = 'index-dev.html'
        else:
            template_name = 'index.html'
        return template_name
