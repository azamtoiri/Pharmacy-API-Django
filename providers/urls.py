from django.urls import path

from providers import views

urlpatterns = [
    # region: Providers url
    path('api/providers/create', views.ProviderCreateView.as_view(), name='providers_create'),
    path('api/providers/', views.ProviderListView.as_view(), name='providers_list'),
    path('api/providers/<int:pk>', views.ProviderDetailView.as_view(), name='providers_detail'),
    # endregion

    # region: Medicines url
    path('api/medicines/create', views.MedicineCreateView.as_view(), name='medicine_create'),
    path('api/medicines/', views.MedicineListView.as_view(), name='medicine_list'),
    path('api/medicines/<int:pk>', views.MedicineDetailView.as_view(), name='medicine_detail'),
    # endregion
]