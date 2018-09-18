from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateView

from .models import Praticien, Cabinet, Profession, CategorieActe, Acte, ActeHonoraires

# Vue qui affiche la page principale "home"
class PagePublicView(TemplateView):
    template_name = "APP_001_PAGEPUBLIC/001_home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PagePublicView, self).get_context_data(*args, **kwargs)
        context['praticien'] = Praticien.objects.all().first()
        context['cabinet'] = Cabinet.objects.all().first()
        context['profession'] = Profession.objects.all().first()
        context['categorieacte'] = CategorieActe.objects.all()
        return context

# Vue qui affiche les différentes vues détaillant les catégories d'actes
class CategorieActeDetailView(DetailView):
    template_name = "APP_001_PAGEPUBLIC/010_categorieacte_detail.html"

    def get_queryset(self):
        return CategorieActe.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(CategorieActeDetailView, self).get_context_data(*args, **kwargs)
        context['praticien'] = Praticien.objects.all().first()
        context['cabinet'] = Cabinet.objects.all().first()
        context['profession'] = Profession.objects.all().first()
        context['categorieacte'] = CategorieActe.objects.all()
        return context

# Vue qui affiche les différentes vues détaillant les actes
class ActeDetailView(DetailView):
    template_name = "APP_001_PAGEPUBLIC/011_acte_detail.html"

    def get_queryset(self):
        return Acte.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ActeDetailView, self).get_context_data(*args, **kwargs)
        context['praticien'] = Praticien.objects.all().first()
        context['cabinet'] = Cabinet.objects.all().first()
        context['profession'] = Profession.objects.all().first()
        context['categorieacte'] = CategorieActe.objects.all()
        return context

# Vue qui affiche la page principale "home"
class HonorairesView(TemplateView):
    template_name = "APP_001_PAGEPUBLIC/012_honoraires.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HonorairesView, self).get_context_data(*args, **kwargs)
        context['praticien'] = Praticien.objects.all().first()
        context['cabinet'] = Cabinet.objects.all().first()
        context['profession'] = Profession.objects.all().first()
        context['categorieacte'] = CategorieActe.objects.all()
        context['honoraire'] = ActeHonoraires.objects.all()
        return context
