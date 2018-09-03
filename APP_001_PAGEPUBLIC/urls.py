from django.conf.urls import url

from .views import (
    PagePublicView,
    CategorieActeDetailView,
)

urlpatterns = [
    url(r'^$', PagePublicView.as_view(), name='page-public-home'),
    url(r'^(?P<slug>[\w-]+)/$', CategorieActeDetailView.as_view(), name='page-public-categorie-acte'),
]
