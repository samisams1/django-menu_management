from django.urls import path
from . import views

urlpatterns = [
    path('menus/', views.MenuListCreateView.as_view(), name='menu-list-create'),
    path('menus/<int:pk>/', views.MenuDetailView.as_view(), name='menu-detail'),
]