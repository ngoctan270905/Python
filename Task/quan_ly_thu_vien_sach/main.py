# Import các class từ modules
from book_management import Book, PhysicalBook, EBook, display_books
from library_management import User, Library


def main():
    print('')
    print("HỆ THỐNG QUẢN LÝ THƯ VIỆN TRỰC TUYẾN")

    thu_vien = Library()
    print("THÊM SÁCH VÀO THƯ VIỆN")

    # 3 sách giấy (PhysicalBook)
    sach1 = PhysicalBook("B001", "Đắc Nhân Tâm", "Dale Carnegie", 5, "mới")
    sach2 = PhysicalBook("B002", "Nhà Giả Kim", "Paulo Coelho", 3, "cũ")
    sach3 = PhysicalBook("B003", "Sapiens", "Yuval Noah Harari", 4, "mới")

    # 2 sách điện tử (EBook)
    sach4 = EBook("E001", "Clean Code", "Robert C. Martin", 10, "PDF")
    sach5 = EBook("E002", "Python Crash Course", "Eric Matthes", 8, "EPUB")

    # Thêm vào thư viện
    thu_vien.add_book(sach1)
    thu_vien.add_book(sach2)
    thu_vien.add_book(sach3)
    thu_vien.add_book(sach4)
    thu_vien.add_book(sach5)
    print("TẠO NGƯỜI DÙNG")

    user1 = User("U001", "Nguyễn Văn An")
    user2 = User("U002", "Trần Thị Bình")

    print(f" {user1.get_info()}")
    print(f" {user2.get_info()}")

    print("MƯỢN SÁCH")

    # User 1 mượn 2 sách
    print(f"\n{user1.ten} mượn sách:")
    thu_vien.borrow_book_for_user(user1, "B001")  # Đắc Nhân Tâm
    thu_vien.borrow_book_for_user(user1, "E001")  # Clean Code

    # User 2 mượn 2 sách
    print(f"\n{user2.ten} mượn sách:")
    thu_vien.borrow_book_for_user(user2, "B002")  # Nhà Giả Kim
    thu_vien.borrow_book_for_user(user2, "E002")  # Python Crash Course

    print("TRẢ SÁCH")

    # User 1 trả 1 sách
    print(f"\n{user1.ten} trả sách:")
    thu_vien.return_book_from_user(user1, "B001")  # Trả Đắc Nhân Tâm

    print("DUYỆT SÁCH BẰNG ITERATOR")

    print("\nSử dụng vòng lặp for (Iterator):")
    for i, sach in enumerate(thu_vien, 1):
        print(f"{i}. {sach.get_info()}")


    display_books(thu_vien.get_all_books())

    print("SÁCH ĐANG MƯỢN CỦA TỪNG NGƯỜI DÙNG")

    def hien_thi_sach_muon(user, thu_vien):

        print(f"\n{user.get_info()}")
        sach_muon = user.get_borrowed_books()

        if not sach_muon:
            print("  (Chưa mượn sách nào)")
        else:
            for ma_sach in sach_muon:
                sach = thu_vien.find_book(ma_sach)
                if sach:
                    print(f"  - {sach.get_info()}")

    hien_thi_sach_muon(user1, thu_vien)
    hien_thi_sach_muon(user2, thu_vien)

# Chạy chương trình
if __name__ == "__main__":
    main()
