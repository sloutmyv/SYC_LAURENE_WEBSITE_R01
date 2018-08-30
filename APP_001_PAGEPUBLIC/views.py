from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Praticien, Cabinet, Profession

# Vue qui affiche la page principale "home"
class PagePublicView(TemplateView):
    template_name = "APP_001_PAGEPUBLIC/001_home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PagePublicView, self).get_context_data(*args, **kwargs)
        # context['title'] = "Home"
        context['praticien'] = Praticien.objects.all().first()
        context['cabinet'] = Cabinet.objects.all().first()
        context['profession'] = Profession.objects.all().first()
        return context
