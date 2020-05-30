from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPage(TemplateView):
    template_name = 'about.html'
