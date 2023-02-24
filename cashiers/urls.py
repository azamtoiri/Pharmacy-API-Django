from django.urls import re_path
from cashiers import views


urlpatterns = [
    re_path(r'^api/cashiers$', views.cashierApi),
    re_path(r'^api/cashiers/([0-9]+)$', views.cashierApi),
    re_path(r'^api/accounts$', views.accountApi),
    re_path(r'^api/accounts/([0-9]+)$', views.accountApi),
]
