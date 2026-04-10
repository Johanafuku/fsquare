from django.urls import path
from .views import UploadView, designer_dashboard

urlpatterns = [
    path('upload/', UploadView.as_view(), name='upload-design'),
    path('dashboard/', designer_dashboard, name='designer-dashboard'),
]
