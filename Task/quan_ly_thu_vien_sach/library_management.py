# lớp đại diện cho người dùng thư viện
class User:
    def __init__(self,ma_nguoi_dung,ten):
        self.__ma_nguoi_dung = ma_nguoi_dung # private
        self.ten = ten
        self.danh_sach_muon = []

    def get_ma_nguoi_dung(self):
        return self.__ma_nguoi_dung

    # method xử lí mượn sách
    def borrow_book(self, ma_sach):
        if ma_sach in self.danh_sach_muon:
            print(f"Hiện tại bạn đã mượn sách '{ma_sach}' rồi")
            return False

        self.danh_sach_muon.append(ma_sach) # append để thêm
        print(f"{self.ten} đã mượn sách '{ma_sach}' thành công")
        return True

    def return_book(self, ma_sach):
        if ma_sach not in self.danh_sach_muon:
            print(f"Hiện tại bạn chưa mượn sách '{ma_sach}'")
            return False

        self.danh_sach_muon.remove(ma_sach)  # remove để xóa
        print(f"{self.ten} đã trả sách '{ma_sach}' thành công")
        return True

    def get_borrowed_books(self):
        return self.danh_sach_muon.copy() # dùng copy để bảo vệ dữ liệu

    def get_info(self):
        so_sach_muon = len(self.danh_sach_muon)
        return f"{self.ten} (ID: {self.__ma_nguoi_dung}) - Đang mượn: {so_sach_muon} quyển sách"

# # Tạo 1 người dùng
# user1 = User("U001", "Nguyễn Tấn")
# user1.borrow_book("S001")
# user1.borrow_book("S001")
# print("Danh sách sách đang mượn:", user1.get_borrowed_books())
# user1.return_book("S001")
# user1.return_book("S003")
# print(user1.get_info())

# Iterators
class Library:
    def __init__(self):
        self.danh_sach_sach = []
        self._current_index = 0 # iterator

    # thêm sách vào thư viện
    def add_book(self, sach):
        self.danh_sach_sach.append(sach)
        print(f"Đã thêm sách: {sach.get_info()}")

    # tìm sách theo mã sách
    def find_book(self, ma_sach):
        # vòng lặp lấy sách trong danh_sach_sach
        for sach in self.danh_sach_sach:

            if sach.get_ma_sach() == ma_sach:
                return sach
        return None

    def  borrow_book_for_user(self, user, ma_sach):
        # tìm sách
        sach = self.find_book(ma_sach)
        if sach is None:
            print(f"Không tìm thấy sách có mã '{ma_sach}")
            return False

        if sach.so_luong_ton_kho <= 0:
            print(f"Sách {sach.tieu_de} đã hết")
            return False

        if user.borrow_book(sach):
            sach.update_stock(-1) # giảm tồn kho
            return True
        return False

    # xử lí trả sách
    def return_book_from_user(self, user, ma_sach):
        sach = self.find_book(ma_sach)
        if sach is None:
            print(f"Không tìm thấy sách có mã '{ma_sach}'")
            return False
        if user.borrow_book(sach):
            sach.update_stock(1)  # tăng tồn kho vì khách trả
            return True
        return False

    # method iterator

    def __iter__(self):
        self._current_index = 0
        return self

    def __next__(self):
        if self._current_index >= len(self.danh_sach_sach):
            raise StopIteration

        # lấy sách hiện tại
        sach = self.danh_sach_sach[self._current_index]
        self._current_index += 1
        return sach

    def get_all_books(self):
        return self.danh_sach_sach.copy()












