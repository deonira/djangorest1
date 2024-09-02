from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('add/', views.CarBrandCreateView.as_view(), name='car-add'),
    path('<int:pk>/', views.CarBrandDetailView.as_view(), name='car-detail'),
    path('', views.CarBrandListView.as_view(), name='car-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]