from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/create/', views.book_create, name='book_create'),

    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),

    path('editorials/', views.editorial_list, name='editorial_list'),
    path('editorials/<int:pk>/', views.editorial_detail, name='editorial_detail'),
]
