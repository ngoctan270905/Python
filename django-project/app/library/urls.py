from django.urls import path
from . import views

urlpatterns = [
    path('book_list', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/create', views.book_create, name='book_create'),

    path('books/<int:pk>/toggle/', views.toggle_book_status, name='toggle_book_status'),

]
