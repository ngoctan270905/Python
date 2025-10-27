class Sach:
    def __init__(self, ten_sach, tac_gia, gia, so_trang):
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.gia = gia
        self.so_trang = so_trang

    def thong_tin(self):
        return f"""
        === THÔNG TIN SÁCH ===
        Tên sách: {self.ten_sach}
        Tác giả: {self.tac_gia}
        Giá: {self.gia}
        Số trang: {self.so_trang}
"""

    def giam_gia(self, phan_tram):
        giam_gia_sach = self.gia * ( 1 - phan_tram/100)
        return f"Sách đã được giảm: {phan_tram}%. Gía khuyến mãi là: {giam_gia_sach}"

sach1 = Sach('Dế mèn phiêu lưu kí', 'Nguyễn Tấn', 10000000, 200)
print(sach1.thong_tin())
print(sach1.giam_gia(10))

class Hinh_Chu_Nhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        dien_tich = self.chieu_dai * self.chieu_rong
        return f"Diện tích của hình chữ nhật là: {dien_tich}"

    def chu_vi(self):
        chu_vi = (self.chieu_dai + self.chieu_rong) * 2
        return f'Chu vi hình chữ nhật là: {chu_vi}'

hinhchunhat1 = Hinh_Chu_Nhat(10, 15)
print(hinhchunhat1.tinh_dien_tich())
print(hinhchunhat1.chu_vi())

class SinhVien:
    def __init__(self, ten, mssv):
        self.ten = ten
        self.mssv = mssv
        self.danh_sach_diem = []

    def them_diem(self, diem):
        if 0 <= diem <= 10:
            self.danh_sach_diem.append(diem)
            print(f"Thêm điểm vào danh sách thành công. Danh sách điểm hiện tại là: {self.danh_sach_diem}")
        else:
            print('Điểm phải từ 1 đến 10')
            print('Thêm điểm thất bại')

    def tinh_diem_trung_binh(self):
        if len(self.danh_sach_diem) == 0:
            return 0
        return round(sum(self.danh_sach_diem) / len(self.danh_sach_diem), 2)

sinhvien1 = SinhVien('Nguyễn Tấn', 'ph49720')
sinhvien1.them_diem(1)
sinhvien1.them_diem(5)
sinhvien1.them_diem(10)
sinhvien1.them_diem(100)

print(f"Điểm trung bình của {sinhvien1.ten} là: {sinhvien1.tinh_diem_trung_binh()}")


