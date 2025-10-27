# 1. xây dụng lớp cơ bản ( class / object, scope )
class Book: # class cha book
    def __init__(self, ma_sach, tieu_de, tac_gia, so_luong_ton_kho):
        self.__ma_sach = ma_sach
        self.tieu_de = tieu_de
        self.tac_gia = tac_gia
        self.so_luong_ton_kho = so_luong_ton_kho

    def get_ma_sach(self): # lấy mã sách vì đang ở private
        return self.__ma_sach

    # hàm trả về thông tin sách dfahng chuỗi'
    def get_info(self):
        return (f"Mã sách: {self.__ma_sach} - Tiêu đề: {self.tieu_de}"
                f" - Tác giả: {self.tac_gia} - Số lượng: {self.so_luong_ton_kho}")

    # method cập nhật số lượng tồn kho
    def update_stock(self, so_luong_thay_doi):
        so_luong_moi = self.so_luong_ton_kho + so_luong_thay_doi
        # kiểm tra tránh âm
        if so_luong_moi < 0:
            print('Lỗi không thể cạp nhật. số lượng tồn kho không được âm')
            return False


        self.so_luong_ton_kho = so_luong_moi
        print(f"Đã cập nhật tồn kho sách {self.tieu_de} - Tồn kho mới: {self.so_luong_ton_kho}")
        return True




# test = Book('PH123','Dế mèn phiêu lưu kí', 'Nguyễn Tấn', 100)
# print(test.get_info())
# print(test.get_ma_sach())
# print(test.update_stock(100))
# print(test.update_stock(-190))

# class con kế thừa từ book
class PhysicalBook(Book):
    def __init__(self, ma_sach, tieu_de, tac_gia, so_luong_ton_kho, trang_thai_vat_li):
        # dùng supper() để kế thừa dữ liệu từ cha
        super().__init__(ma_sach, tieu_de, tac_gia, so_luong_ton_kho)
        self.trang_thai_vat_li = trang_thai_vat_li

    # ghi đè phương thức get_info của cha
    def get_info(self):
        # lấy thông tin cũ từ class cha trước
        thong_tin_sach_tu_cha = super().get_info()

        return f"{thong_tin_sach_tu_cha} - Trạng thái hiện tại: {self.trang_thai_vat_li}"

# test = PhysicalBook('PH123','Dế mèn phiêu lưu kí',
#                     'Nguyễn Tấn', 100, 'hỏng')
# print(test.get_info())

# class con kế thừa từ Book
class EBook(Book):
    def __init__(self, ma_sach, tieu_de, tac_gia, so_luong_ton_kho, dinh_dang_file):
        super().__init__(ma_sach, tieu_de, tac_gia, so_luong_ton_kho)
        self.dinh_dang_file = dinh_dang_file

    def get_info(self):
        thong_tin_sach_tu_cha = super().get_info()
        return f"{thong_tin_sach_tu_cha} - EBOOK - Định dạng file: {self.dinh_dang_file}"

# test = EBook('PH123','Dế mèn phiêu lưu kí',
#                     'Nguyễn Tấn', 100, 'PDF')
# print(test.get_info())


# Polymorphism
def display_books(danh_sach_sach): # hàm hiển thị thông tin sách
    print('======Danh sách trong thư viện======')
    if not danh_sach_sach: # nếu ko có danh sách nào
        print('Chưa có sách nào trong thư viện')
        return # trả về none dừng sớm

    for i, sach in enumerate(danh_sach_sach, 1):
        print(f"{i}. {sach.get_info()}") # tự gọi theo version

# danh_sach_sach = [test]
# print(display_books(danh_sach_sach))




