from django.urls import path
from .views import supplier_list, supplier_dashboard, supplier_profile

urlpatterns = [
    path('supplier-list/', supplier_list, name='supplier-list'),
    path('dashboard/', supplier_dashboard, name='supplier-dashboard'),
    path('profile/', supplier_profile, name='supplier-profile'),
    
]
