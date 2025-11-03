from django.contrib import admin
from .models import Category, Author, Book


# --- Tuỳ chỉnh hiển thị cho Book ---
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date', 'is_available')  # Các cột hiển thị
    list_filter = ('is_available', 'category')  # Bộ lọc bên phải
    search_fields = ('title',)  # Cho phép tìm theo tiêu đề
    list_editable = ('is_available',)  # Chỉnh trực tiếp is_available trong danh sách
    list_per_page = 10  # Phân trang


# --- Tuỳ chỉnh hiển thị cho Author ---
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'book_count')  # Hiển thị tên + số sách

    def book_count(self, obj):
        return obj.book_set.count()  # Đếm số sách liên quan
    book_count.short_description = 'Số lượng sách'  # Đặt tên cho cột


# --- Tuỳ chỉnh hiển thị cho Category ---
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
