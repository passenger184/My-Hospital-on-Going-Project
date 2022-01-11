from django.urls import path
from . import views

urlpatterns = [
    path('',  views.main, name='main'),
    path('add/', views.add, name='add'),
    path('update/', views.search, name='search'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/', views.search1, name='search1'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('confirm/delete/<int:pk>/', views.confirm, name='confirm'),
] 