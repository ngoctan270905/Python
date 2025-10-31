from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # danh sách post
    path('create/', views.post_create, name='post_create'),  # thêm post mới
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),  # chi tiết post

]
