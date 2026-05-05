from django.urls import path
from .views import supplier_list, supplier_dashboard, supplier_profile, delete_supplier_image

urlpatterns = [
    path('supplier-list/', supplier_list, name='supplier-list'),
    path('dashboard/', supplier_dashboard, name='supplier-dashboard'),
    path('profile/', supplier_profile, name='supplier-profile'),
    path("delete-image/<int:image_id>/", delete_supplier_image, name="delete-supplier-image"),  
    ]
