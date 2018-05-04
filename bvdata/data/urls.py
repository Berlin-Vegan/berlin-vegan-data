from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter

from .views import (
    DashboardView,
    GastroUpdateView,
    HomeView,
    GastroNewView,
    ApiGastroLocationsJson,
    GastroDeleteView,
    GastroSubmitView,
    GastroSubmitListView,
    GastroSubmitEditView,
    GastroViewSet,
    GastrosClosedView,
    GastroSubmitDeleteView,
)

app_name = 'data'

router = DefaultRouter()
router.register(r'gastro', GastroViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/GastroLocations.json', ApiGastroLocationsJson.as_view(), name='api'),

    # listviews
    # open
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #closed
    path('gastros-closed/', GastrosClosedView.as_view(), name='gastros-closed'),

    path('gastro-new/', GastroNewView.as_view(), name='gastro-new'),
    path('location/gastro/<str:id_string>/edit/', GastroUpdateView.as_view(), name='gastro-update'),
    path('location/gastro/<str:id_string>/delete/', GastroDeleteView.as_view(), name='gastro-delete'),

    path('gastro-submit-list/', GastroSubmitListView.as_view(), name='gastro-submit-list'),
    path('gastro-submit/<int:id>/edit/', GastroSubmitEditView.as_view(), name='gastro-submit-edit'),
    path('gastro-submit/<int:id>/delete/', GastroSubmitDeleteView.as_view(), name='gastro-submit-delete'),

    # public
    path('gastro-submit/', GastroSubmitView.as_view(), name='gastro-submit'),

    # auth urls
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # django rest framework
    re_path(r'^rest-api/', include(router.urls)),


]
