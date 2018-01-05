from django.contrib.auth import views as auth_views
from django.urls import path

from .views import DashboardView, GastroUpdateView, HomeView, GastroNewView, ApiGastroLocationsJson

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/GastroLocations.json', ApiGastroLocationsJson.as_view(), name='api'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('gastro-new/', GastroNewView.as_view(), name='gastro-new'),
    path('location/gastro/<str:id_string>/edit/', GastroUpdateView.as_view(), name='gastro-update'),

    # auth urls
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

]
