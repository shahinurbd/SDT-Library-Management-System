from django.urls import path
from books import views

urlpatterns = [
    path('', views.view_category, name='category-list')
]