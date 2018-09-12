from django.conf.urls import url

from .views import (
    PagePublicView,
    CategorieActeDetailView,
    ActeDetailView,
)

urlpatterns = [
    url(r'^$', PagePublicView.as_view(), name='page-public-home'),
    url(r'^categorie-acte/(?P<slug>[\w-]+)/$', CategorieActeDetailView.as_view(), name='page-public-categorie-acte'),
    url(r'^acte/(?P<slug>[\w-]+)/$', ActeDetailView.as_view(), name='page-public-acte'),
]
