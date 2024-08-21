from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.CarBrandCreateView.as_view(), name='car-add'),
    path('<int:pk>/', views.CarBrandDetailView.as_view(), name='car-detail'),
    path('', views.CarBrandListView.as_view(), name='car-list'),
]