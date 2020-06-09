from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),
    path('dashboard/',include('dashboard.urls',namespace='dashboard')),
    path('users/',include('users.urls',namespace='users')),
    path('schools/',include('schools.urls',namespace='schools')),
    path('equipment/',include('equipment.urls',namespace='equipment')),
    path('', LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout', LogoutView.as_view(template_name='account/login.html'),name='logout'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

