from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('library/', include('library.urls')),
    path('blog/', include('blog_project.urls')),
    path('todo_app/', include('todo_app.urls')),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
