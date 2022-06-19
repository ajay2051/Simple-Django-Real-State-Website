from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name='listing'),
    path('listing_retrieve/<int:pk>/',views.listing_retrieve, name='listing_retrieve'),
    path('listing_create/', views.listing_create, name='listing_create'),
    path('listing_update/<int:pk>/',views.listing_update, name='listing_update'),
    path('listing_delete/<int:pk>/',views.listing_delete, name='listing_delete'),
]