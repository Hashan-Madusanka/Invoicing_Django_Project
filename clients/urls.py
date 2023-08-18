from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_client, name='create_client'),
    path('search-clients/', views.search_clients, name='search_clients'),
    path('view-clients/', views.view_clients, name='view_clients'),
]