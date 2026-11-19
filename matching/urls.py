from django.urls import path
from .views import match_design
from .api_views import matching_results_api

urlpatterns = [
    path('<int:design_id>/match/', match_design, name='match-design'),
    path('api/design/<int:design_id>/', matching_results_api, name='matching-results-api'),
]
