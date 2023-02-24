from django.urls import re_path
from providers import views

from providers import views

urlpatterns = [
    re_path(r'^api/providers$', views.providerApi),
    re_path(r'^api/providers/([0-9]+)$', views.providerApi),
    re_path(r'^api/medicines$', views.medicine_api),
    re_path(r'^api/medicines/([0-9]+)$', views.medicine_api),
]