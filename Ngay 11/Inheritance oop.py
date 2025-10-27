# INHERITANCE ( tính kế thừa trong OOP )
class DongVat:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def an(self):
        return f"{self.ten} đang ăn"

    def ngu(self):
        return f"{self.ten} đang ngủ"

class Cho(DongVat):
    def __init__(self, ten, tuoi, giong):
        super().__init__(ten, tuoi)
        self.giong = giong

    def thong_tin(self):
        return f"Tên: {self.ten} - Tuổi: {self.tuoi} - Gioong: {self.giong}"
    # Thêm method riêng
    def sua(self):
        return f"{self.ten} gâu gâu"

class Meo(DongVat):
    def keu(self):
        return f"{self.ten} Meo Meo"

cho = Cho('Lulu', 20, 'Ta')
print(cho.an())
print(cho.ngu())
print(cho.ten)
print(cho.sua())
print(cho.thong_tin())

meo = Meo('Tom', 20)
print(meo.keu())

# Ghi đè method

class DongVat2:
    def __init__(self, ten):
        self.ten = ten

    def keu(self):
        return f"{self.ten} đang kêu"
class Cho2(DongVat2):
    def keu(self):
        return f"{self.ten} Gâu gâu"
cho2 = Cho2('Lili')
print(cho2.keu())

# Sử dụng super() để mở rộng method
class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def gioi_thieu(self):
        return f"Tooi la: {self.ten} - {self.tuoi}"

class SinhVien(Nguoi):
    def __init__(self, ten, tuoi, truong):
        super().__init__(ten, tuoi)
        self.truong = truong

    def gioi_thieu(self):
        thong_tin_co_ban = super().gioi_thieu()
        return f"{thong_tin_co_ban} {self.truong}"



nguoi = Nguoi('Tấn', 20)
print(nguoi.gioi_thieu())
nguoi2 = SinhVien('Tấn', 20, 'THPT B THANH LIÊM')
print(nguoi2.gioi_thieu())

#vd thuc te
class NhanVien:
    so_luong = 0
    def __init__(self, ten, tuoi, luong_co_ban):
        self.ten = ten
        self.tuoi = tuoi
        self.luong_co_ban = luong_co_ban
        NhanVien.so_luong = NhanVien.so_luong + 1

    def tinh_luong(self):
        return self.luong_co_ban

    def thong_tin(self):
        return f"Nhân viên: {self.ten} - {self.tuoi}tuổi - Lương: {self.luong_co_ban}"

class LapTrinhVien(NhanVien):
    def __init__(self, ten, tuoi, luong_co_ban, ngon_ngu):
        super().__init__(ten, tuoi, luong_co_ban)
        self.ngon_ngu = ngon_ngu

    def tinh_luong(self):
        return self.luong_co_ban * 1.3

    def thong_tin(self):
        return f"{super().thong_tin()} - Ngôn ngũ: {self.ngon_ngu}"

class QuanLy(NhanVien):
    def __init__(self, ten, tuoi, luong_co_ban, so_nhan_vien):
        super().__init__(ten, tuoi, luong_co_ban)
        self.so_nhan_vien = so_nhan_vien

    # ghi đè method tính lương
    def tinh_luong(self):
        bonus = self.so_nhan_vien * 100000
        return self.luong_co_ban * 1.3 + bonus

    def thong_tin(self):
        return f"{super().thong_tin()} - Quản lí {self.so_nhan_vien} nhân viên"


nv1 = NhanVien("Bình", 25, 5000000)
ltv = LapTrinhVien("An", 28, 10000000, "Python")
ql = QuanLy("Hùng", 35, 15000000, 10)

print(nv1.thong_tin())
print(ltv.thong_tin())
print(ql.thong_tin())
print(f"Tổng số nhân viên: {NhanVien.so_luong}")

    

