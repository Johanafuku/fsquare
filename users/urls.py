from django.urls import path
from .views import register_designer, register_supplier

urlpatterns = [
    path('register/designer/', register_designer, name='register-designer'),
    path('register/supplier/', register_supplier, name='register-supplier'),
]