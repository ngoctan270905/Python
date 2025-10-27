#Định nghĩa Class
class ConNguoi:
    # class atribute - chung to tất cả đối tượng
    loai = "Hihi"

    def __init__(self, ten, tuoi):
        # thuộc tính thể hiện - riêng cho từng đối tượng
        self.ten = ten
        self.tuoi = tuoi

# Tạo object
nguoi1 = ConNguoi("Tấn", 20)
nguoi2 = ConNguoi("Tú", 25)

print(nguoi1.ten, nguoi2.ten)
print(nguoi1.loai, nguoi2.loai)

class SinhVien:
    #Hàm init tự động chạy khi tạo object mới
    def __init__(self, ten, mssv, diem=0):
        self.ten = ten
        self.mssv = mssv
        self.diem = diem
        print(f"Đã tạo sinh viên: {ten}")

sinhvien1 = SinhVien("Lan", "PH49720")
sinhvien2 = SinhVien('Tấn', 'PH49888', 9)

class HinhTron:
    def __init__(self, ban_kinh):
        # SET đại diện cho 1 object cho phép truy cập các thuộc tính và method của object
        self.ban_kinh = ban_kinh # self.ban_kinh thuộc về 1 object

    def tinh_dien_tich(self):
        return 3.14 * self.ban_kinh ** 2

hinh1 = HinhTron(5)
hinh2 = HinhTron(6)
print(f"Diện tích hình tròn số 1 là: {hinh1.tinh_dien_tich()}")
print(f"Diện tích hình tròn số 2 là: {hinh2.tinh_dien_tich()}")


#METHOD PHƯƠNG THỨC
# lớp tài khoản
class TaiKhoan:
    def __init__(self, ten, so_du):
        self.ten = ten
        self.so_du = so_du

    def nap_tien(self, so_tien):
        self.so_du = self.so_du + so_tien
        return f"Đã nạp số tiền {so_tien}. Số tiền mới là: {self.so_du}"

    def rut_tien(self, so_tien):
        self.so_du = self.so_du - so_tien
        return f"Đã rút số tiền {so_tien}. Số dư còn lại là: {self.so_du}"

    def xem_so_du(self):
        return f"{self.ten} có số dư: {self.so_du}"

tai_khoan = TaiKhoan("Tấn", 2000000)
print(tai_khoan.nap_tien(20000))
print(tai_khoan.rut_tien(20000))
print(tai_khoan.xem_so_du())
print(tai_khoan.rut_tien(20000))

# . Class Attributes vs Instance Attributes
class NhanVien:
    # class atribuute dùng chung
    cong_ty ='ABCXYZ'
    so_luong_nhan_vien = 0

    def __init__(self, ten, luong):
        # thuộc tính riêng biệt
        self.ten = ten
        self.luong = luong
        NhanVien.so_luong_nhan_vien = NhanVien.so_luong_nhan_vien + 1

nv1 = NhanVien('Nguyen Ngoc Tan', 10000000)
nv2 = NhanVien('Nguyen Ngoc Tuan', 10000000)
print(f"Nhân viên : {nv1.cong_ty}")
print(f"Nhân viên: {nv1.ten}")
print(f"Số lượng nhân viên là: {NhanVien.so_luong_nhan_vien}")

# VD Thuc te

class XeMay:
    loai_phuong_tien = 'Xe 2 bánh'

    def __init__(self, hang, mau, gia, xang=0):
        self.hang = hang
        self.mau = mau
        self.gia = gia
        self.xang = xang
        self.dangchay = False

    def do_xang(self, lit):
        self.xang = self.xang + lit
        return f"Đã đổ {lit}L xăng. Xăng hiện tại còn: {self.xang}L"

    def khoi_dong(self):
        if self.xang > 0:
            self.dangchay = True
            return 'Xe đã khởi động!'
        return 'Xe không đủ xăng để khởi động'

    def di_chuyen(self, km):
        xang_can = km * 0.02
        if self.dangchay and self.xang >= xang_can:
            self.xang = self.xang - xang_can
            return f"Đã đi được {km}km. Xăng còn lại là{self.xang:.2f}"

    def tat_may(self):
        self.dangchay = False
        return "Đã tắt máy"

    def thong_tin(self):
        trang_thai = 'Đang chạy' if self.dangchay else 'Đã tắt máy'
        return f"""
        === Thông tin xe ===
        Hãng: {self.hang}
        Màu: {self.mau}
        Giá: {self.gia}
        Xăng còn: {self.xang}L
        Trạng thái: {trang_thai}
"""



xe1 = XeMay("Honda", "Đỏ", 100000000)
print(xe1.do_xang(5))
print(xe1.khoi_dong())
print(xe1.di_chuyen(100))
print(xe1.tat_may())
print(xe1.thong_tin())
print(xe1.khoi_dong())
print(xe1.thong_tin())

# Bài tập thực hành
class HocSinh:
    def __init__(self, ten, toan, van, anh):
        self.ten = ten
        self.toan = toan
        self.van = van
        self.anh = anh

    def tinh_diem_trung_binh(self):
        return (self.toan + self.van + self.anh) / 3

    def xep_loai(self):
        dtb = self.tinh_diem_trung_binh()
        if dtb >= 8:
            return 'DTB của bạn là giỏi'
        elif dtb >= 6.5:
            return 'DTB của bạn là Khá'
        elif dtb >= 4.5:
            return 'DTB của bạn là Trung bình'
        else:
            return 'Yếu'

hocsinh1 = HocSinh('Nguyễn Tấn', 10, 10, 10)
print(f"Điểm trung bình của {hocsinh1.ten} là: {hocsinh1.tinh_diem_trung_binh()}")
print(hocsinh1.xep_loai())







