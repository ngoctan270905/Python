from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.utils.text import slugify
from .models import Post

# method hiển thị danh sách
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            slug = slugify(title)
            Post.objects.create(title=title, content=content, slug=slug)
            return redirect('post_list')

    return render(request, 'blog/post_create.html')
