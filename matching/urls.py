from django.urls import path
from .views import match_design

urlpatterns = [
    path('<int:design_id>/match/', match_design, name='match-design'),
]
