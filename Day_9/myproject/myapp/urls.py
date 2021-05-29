from django.urls import path
from . import views # from myapp import views

urlpatterns = [
    path('addbook/',views.addBook,name='books'),
]