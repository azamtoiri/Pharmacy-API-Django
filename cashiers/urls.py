from django.urls import path
from cashiers import views

urlpatterns = [
    # cashiers
    path('api/cashiers/create', views.CashierCreateView.as_view(), name="create_cashiers"),
    path('api/cashiers/', views.CashierListView.as_view(), name="get_cashiers"),
    path('api/cashiers/<int:pk>', views.CashierDetailView.as_view(), name="cashiers_detail"),

    # accounts
    path('api/accounts/create', views.AccountCreateView.as_view(), name="create_account"),
    path('api/accounts/', views.AccountListView.as_view(), name="get_account"),
    path('api/accounts/<int:pk>', views.AccountDetailView.as_view(), name="accounts_detail"),
]