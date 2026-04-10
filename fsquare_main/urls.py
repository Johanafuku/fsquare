from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, ContactView, LegalView, AboutView
from django.contrib.auth import views as auth_views
from users.views import CustomLoginView

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('contact/', ContactView.as_view(),name='contact'),
    path('legal/', LegalView.as_view(),name='legal'),
    path('about/', AboutView.as_view(), name='about'),
    path('users/', include('users.urls')),
    path('designs/', include('designs.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('selections/', include('matching.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='password_change.html',
        success_url='/'
    ), name='password_change'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
