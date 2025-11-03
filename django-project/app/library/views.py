from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Book, Category, Author
from django.utils import timezone

def book_list(request):
    # --- Lấy từ khóa tìm kiếm ---
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    author_id = request.GET.get('author', '')

    books = Book.objects.filter(is_available=True)

    # --- Tìm kiếm theo title hoặc tác giả ---
    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(authors__name__icontains=query)
        ).distinct()

    # --- Lọc theo danh mục ---
    if category_id:
        books = books.filter(category_id=category_id)

    # --- Lọc theo tác giả ---
    if author_id:
        books = books.filter(authors__id=author_id)

    # --- Phân trang 5 sách mỗi trang ---
    paginator = Paginator(books.order_by('title'), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # --- Truyền dữ liệu cho select filter ---
    categories = Category.objects.all()
    authors = Author.objects.all()

    context = {
        'page_obj': page_obj,
        'query': query,
        'categories': categories,
        'authors': authors,
        'selected_category': category_id,
        'selected_author': author_id,
    }

    return render(request, 'library/book_list.html', context)

def book_detail(request, book_id):
    # Lấy thông tin sách theo ID
    book = get_object_or_404(Book, id=book_id)

    context = {
        'book': book,
    }
    return render(request, 'library/book_detail.html', context)

def book_create(request):
    categories = Category.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        author_ids = request.POST.getlist('authors')
        published_date = request.POST.get('published_date')
        is_available = request.POST.get('is_available') == 'on'

        if title and category_id and published_date:
            category = Category.objects.get(id=category_id)
            book = Book.objects.create(
                title=title,
                category=category,
                published_date=published_date,
                is_available=is_available
            )
            # Gán tác giả (nhiều-một)
            book.authors.set(author_ids)
            return redirect('book_list')  # Sau khi tạo xong thì quay về danh sách sách

    return render(request, 'library/book_create.html', {
        'categories': categories,
        'authors': authors
    })

def toggle_book_status(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.is_available = not book.is_available
    book.save()
    return redirect('book_list')
