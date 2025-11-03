from django.core.management.base import BaseCommand
from library.models import Category, Author, Book
from django.utils import timezone
import random
from datetime import timedelta

class Command(BaseCommand):
    help = "Seed database with sample data for testing"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Đang tạo dữ liệu mẫu..."))

        # --- 1. Tạo danh mục ---
        categories = [
            "Fiction",
            "Non-Fiction",
            "Science",
            "History",
            "Biography",
        ]
        for cat_name in categories:
            Category.objects.get_or_create(name=cat_name)
        self.stdout.write(self.style.SUCCESS("Tạo danh mục thành công."))

        # --- 2. Tạo tác giả ---
        authors = []
        for i in range(1, 11):
            author, created = Author.objects.get_or_create(
                name=f"Tác giả {i}",
                defaults={"bio": f"Tiểu sử của tác giả {i}."},
            )
            authors.append(author)
        self.stdout.write(self.style.SUCCESS("Tạo 10 tác giả thành công."))

        # --- 3. Tạo sách ---
        all_categories = list(Category.objects.all())
        for i in range(1, 21):
            book = Book.objects.create(
                title=f"Sách số {i}",
                category=random.choice(all_categories),
                published_date=timezone.now().date() - timedelta(days=random.randint(0, 1000)),
                is_available=random.choice([True, False]),
            )
            # Gán ngẫu nhiên 1-3 tác giả
            random_authors = random.sample(authors, k=random.randint(1, 3))
            book.authors.set(random_authors)

        self.stdout.write(self.style.SUCCESS("✅ Tạo 20 sách mẫu thành công."))
        self.stdout.write(self.style.SUCCESS("🎉 Hoàn tất seed dữ liệu!"))
