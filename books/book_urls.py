from django.urls import path
from books import views

urlpatterns = [
    path('', views.view_books, name='book-list')
]
