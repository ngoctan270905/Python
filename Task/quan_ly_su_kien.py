import numpy as np

def quan_ly_su_kien(danh_sach_su_kien):
    while True: # dùng vòng lặp để người dùng có thể thao tác lieen tục
        print('')
        print('QUẢN LÍ SỰ KIỆN')
        print('1. Thêm sự kiện mới')
        print('2. Xóa sự kiện theo mã')
        print('3. Cập nhật số lượng vé còn lại')
        print('4. Xem thông tin sự kiện theo mã')
        print('5. Hiển thị toàn bộ danh sách sự kiện')
        print('6. Tính giá vé trung bình')
        print('7. Thoát')
        print('')

        lua_chon = int(input('Lựa chọn của bạn: '))

        if lua_chon == 1:
            print('THÊM SỰ KIỆN MỚI')
            ma_su_kien = input('Nhập mã sự kiện: ')
            ten_su_kien = input('Nhập tên sự kiện: ')
            gia_ve = float(input('Nhập giá vé: '))
            ve_con_lai = int(input('Nhập vé còn lại: '))

            su_kien_moi = {
                'ma_su_kien': ma_su_kien,
                'ten_su_kien': ten_su_kien,
                'gia_ve': gia_ve,
                've_con_lai': ve_con_lai,
            }

            danh_sach_su_kien.append(su_kien_moi)
            print('Đã thêm sự kiện thành công')

        elif lua_chon == 2:
            print('XÓA SỰ KIỆN')
            ma_xoa = input('Nhập mã sự kiện cần xóa: ')

            kiem_tra_ma = False
            for su_kien in danh_sach_su_kien:
                if su_kien['ma_su_kien'] == ma_xoa:
                    danh_sach_su_kien.remove(su_kien)
                    kiem_tra_ma = True
                    print('Sự kiện đã được xóa thành công')
                    break
            if not kiem_tra_ma:
                print('Mã sự kiện không tồn tại, vui lòng nhập đúng')


        elif lua_chon == 5:
            print('Danh sách sự kiện hiện tại')
            for i, su_kien in enumerate(danh_sach_su_kien, start=1):
                print(f"{i}. Mã SK: {su_kien['ma_su_kien']} - Tên SK: {su_kien['ten_su_kien']} - Giá vé: {su_kien['gia_ve']} - Vé còn lại: {su_kien['ve_con_lai']}")





def main():
    # tạo dữ liệu mẫu , list
    danh_sach_su_kien = [
        {"ma_su_kien": "SK001", "ten_su_kien": "Hội chợ sách mùa xuân", "gia_ve": 50000.0, "ve_con_lai": 200},
        {"ma_su_kien": "SK002", "ten_su_kien": "Triển lãm tranh thiếu nhi", "gia_ve": 70000.0, "ve_con_lai": 150},
        {"ma_su_kien": "SK003", "ten_su_kien": "Lễ hội ẩm thực Việt", "gia_ve": 100000.0, "ve_con_lai": 300},
        {"ma_su_kien": "SK004", "ten_su_kien": "Workshop làm gốm nghệ thuật", "gia_ve": 120000.0, "ve_con_lai": 80},
        {"ma_su_kien": "SK005", "ten_su_kien": "Chương trình hòa nhạc đường phố", "gia_ve": 60000.0, "ve_con_lai": 250}
    ]
    # Tạo dictionary gồm key và value: value sẽ chứa set
    nha_tai_tro = {
        "NTT001": ("Công ty Cổ phần Văn Hóa Việt", 5000000.0),
        "NTT002": ("Tập đoàn Sách Toàn Cầu", 8000000.0),
        "NTT003": ("Công ty TNHH Nghệ Thuật Trẻ", 3000000.0),
        "NTT004": ("Tập đoàn Ẩm Thực ABC", 10000000.0),
        "NTT005": ("Ngân hàng XYZ", 15000000.0)
    }

    quan_ly_su_kien(danh_sach_su_kien)


# main chạy chính
if __name__ == "__main__":
    main()
