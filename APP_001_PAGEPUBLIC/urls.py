from django.conf.urls import url

from .views import (
    PagePublicView,
)

urlpatterns = [
    url(r'^$', PagePublicView.as_view(), name='page-public-home'),
]
