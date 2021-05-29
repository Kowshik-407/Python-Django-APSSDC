from django.urls import path
from FirstApp import views

urlpatterns = [
    path('aphome/', views.aphome),
    path('apabout/', views.apabout),
]