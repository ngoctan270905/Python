
def quan_ly_nha_tai_tro(nha_tai_tro):
    while True: # VÒNG LĂjp
        print('')
        print('QUẢN LÍ NHÀ TÀI TRỢ')
        print('1. Thêm nhà tài trợ mới')
        print('2. Xóa nhà tài trợ')
        print('3. Cập nhật số tiền của nhà tài trợ')
        print('4. Tìm và in thông tin nhà tài trợ theo mã')
        print('5. Xem danh sách tất cả nhà tài trợ')
        print('6. Thoát')

        lua_chon = input('Lựa chọn của bạn: ')

        if lua_chon == '1':
            print('THÊM NHÀ TÀI TRỢ')
            ma = input('Nhập mã nhà tài trợ: ').strip()
            if ma in nha_tai_tro: # dùng in để kiểm tra xem ma có tồn tại trong nha_tai_tro chưa
                print('Mã nhà tài trợ này đã tồn tại')
                continue # nếu tồn tại dừng vòng lặp hiện tại chuyển sang cái mới
            ten = input('Nhập tên nhà tài trợ:').strip()
            so_tien = float(input('Nhập số tiền tài trợ: '))

            if so_tien < 1000000: # kiểm tra
                print('Số tiền tài trợ phải từ 1.000.000đ trở lên: ')
                continue

            nha_tai_tro[ma] = (ten, so_tien) # th êm dữ liệu vào trong dict
            print('Thêm nhà tài trợ thành công')

        if lua_chon == '2':
            print('XÓA NHÀ TÀI TRỢ')
            ma = input('Nhập mã tài trợ cần xóa: ').strip()
            if ma in nha_tai_tro:
                del nha_tai_tro[ma]
                print('Đã xóa nhà tài trợ thành công')
            else:
                print('Mã nhà tài trợ không tồn tại')

        if lua_chon == '3':
            print('Cập nhật số tiền của nhà tài trợ')
            ma = input('Nhập mã tài trợ cần cập nhật: ').strip()
            if ma in nha_tai_tro:
                ten = nha_tai_tro[ma][0]
                so_tien = float(input('Nhập số tiền tài trợ mới: '))
                nha_tai_tro[ma] = (ten, so_tien)
                print('Cập nhật số tiền của nhà tài trợ thành công')
            else:
                print('Mã nhà tài trợ không tồn tại')

        if lua_chon == '4':
            print('THÔNG TIN TÀI TRỢ')
            ma = input('Nhập mã tài trợ cần tìm: ').strip()
            if ma in nha_tai_tro:
                (ten, so_tien) = nha_tai_tro[ma]
                print(f"Mã: {ma} - Tên nhà tài trợ: {ten} - Số tien tài trợ: {so_tien}")



        if lua_chon == '5':
            print('DANH SÁCH NHÀ TÀI TRỢ')
            for i, ma in enumerate(nha_tai_tro, start=1): # lặp lấy key của dict
                ten, so_tien = nha_tai_tro[ma] # ma se la key và nha_tai_tro[ma] lưu value ten, so_tien của tuple
                print(f"{i}. Mã tài trợ: {ma} - Tên nhà tài trợ: {ten} - Số tiền tài trợ: {so_tien}")

        if lua_chon == '6':
            break


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

        if lua_chon == 1: # chọn menu 1
            print('THÊM SỰ KIỆN MỚI')
            # tạo biến để lưu trữ dữ liệu từ input
            ma_su_kien = input('Nhập mã sự kiện: ').strip() # strip để bỏ khoảng trắng
            ten_su_kien = input('Nhập tên sự kiện: ').strip()
            gia_ve = float(input('Nhập giá vé: '))
            ve_con_lai = int(input('Nhập vé còn lại: '))

            # tạo dict để lưu thông tin vừa nhập
            su_kien_moi = {
                'ma_su_kien': ma_su_kien,
                'ten_su_kien': ten_su_kien,
                'gia_ve': gia_ve,
                've_con_lai': ve_con_lai,
            }

            danh_sach_su_kien.append(su_kien_moi) # dùng append() trong list để thêm
            print('Đã thêm sự kiện thành công')

        elif lua_chon == 2: # lựa chọn 2
            print('XÓA SỰ KIỆN')
            ma_xoa = input('Nhập mã sự kiện cần xóa: ').strip()

            kiem_tra_ma = False # tạo biến để kiểm tra mã trong ds = False . nếu tìm thấy mã thì sẽ thành True
            for su_kien in danh_sach_su_kien:
                if su_kien['ma_su_kien'].lower() == ma_xoa.lower(): # nếu mã sự kiện = mã xóa nhập từ ng dùng
                    danh_sach_su_kien.remove(su_kien) # dùng remove để xóa trong list
                    kiem_tra_ma = True # tìm thấy mã và xóa thành công biến sẽ thành True
                    print('Sự kiện đã được xóa thành công')
                    break # dừng lại
            if not kiem_tra_ma: # nếu ko tìm thấy mã sẽ thực hiện lệnh này
                print('Mã sự kiện không tồn tại, vui lòng nhập đúng')

        elif lua_chon == 3:
            print('CẬP NHẬT SỐ LƯỢNG VÉ')
            ma_cap_nhat = input('Nhập mã sự kiện cần sửa: ').strip()

            kiem_tra_ma = False
            for su_kien in danh_sach_su_kien:
                if su_kien['ma_su_kien'].lower() == ma_cap_nhat.lower():
                    print(f"Mã sự kiện {su_kien['ma_su_kien']} đang có số vé còn lại là: {su_kien['ve_con_lai']}")
                    so_ve_moi = int(input('Nhập số vé mới: '))
                    if so_ve_moi < 0: # kiểm tra đầu vào
                        print('Số vé phải là số dương')
                    else:
                        su_kien['ve_con_lai'] = so_ve_moi # cập nhật thông tin key của dict
                        print(f"Cập nhật số vé cho sự kiện '{su_kien['ten_su_kien']}' thành công")
                    kiem_tra_ma = True
                    break
            if not kiem_tra_ma:
                print('Mã sự kiện không tồn tại. Vui lòng nhập chính xác.')

        elif lua_chon == 4:
            print('XEM THÔNG TIN SỰ KIỆN')
            ma_can_xem = input('Nhập mã sự kiện để xem: ').strip()
            kiem_tra_ma = False
            for su_kien in danh_sach_su_kien:
                if su_kien['ma_su_kien'].lower() == ma_can_xem.lower():
                 print(f"Mã sự kiện: {su_kien['ma_su_kien']} - Tên SK: {su_kien['ten_su_kien']} - Giá vé: {su_kien['gia_ve']} - Vé còn lại: {su_kien['ve_con_lai']}")
                 kiem_tra_ma = True
                 break
            if not kiem_tra_ma:
                print('Mã không tồn tại . Vui lòng nhập chính xác')


        elif lua_chon == 5:
            print('Danh sách sự kiện hiện tại')
            for i, su_kien in enumerate(danh_sach_su_kien, start=1): # dùng enumerate để lấy đc index và sk
                print(f"{i}. Mã SK: {su_kien['ma_su_kien']} - Tên SK: {su_kien['ten_su_kien']} - Giá vé: {su_kien['gia_ve']} - Vé còn lại: {su_kien['ve_con_lai']}")

        elif lua_chon == 6:
            print('THỐNG KÊ GIÁ VÉ')
            if len(danh_sach_su_kien) > 0:
                danh_sach_gia = [ su_kien['gia_ve'] for su_kien in danh_sach_su_kien ] # list gias
                # danh_sach_gia = []
                # for su_kien in danh_sach_su_kien:
                #     danh_sach_gia.append(su_kien['gia_ve'])

                gia_trung_binh = sum(danh_sach_gia) / len(danh_sach_gia) # sum là tổng # len là các giá
                print(f"Gía vé trung bình của mỗi sự kiện là: {gia_trung_binh}")
            else:
                print('Danh sách sự kiện đang trống')

        elif lua_chon == 7:
            print('CHào bạn.')
            break

def main():
    # tạo dữ liệu mẫu , list
    danh_sach_su_kien = [
        {"ma_su_kien": "SK001", "ten_su_kien": "Hội chợ sách mùa xuân", "gia_ve": 50000.0, "ve_con_lai": 200},
        {"ma_su_kien": "SK002", "ten_su_kien": "Triển lãm tranh thiếu nhi", "gia_ve": 70000.0, "ve_con_lai": 150},
        {"ma_su_kien": "SK003", "ten_su_kien": "Lễ hội ẩm thực Việt", "gia_ve": 100000.0, "ve_con_lai": 300},
        {"ma_su_kien": "SK004", "ten_su_kien": "Workshop làm gốm nghệ thuật", "gia_ve": 120000.0, "ve_con_lai": 80},
        {"ma_su_kien": "SK005", "ten_su_kien": "Chương trình hòa nhạc đường phố", "gia_ve": 60000.0, "ve_con_lai": 250}
    ]
    # Tạo dictionary gồm key và value: value sẽ chứa tuple
    nha_tai_tro = {
        "NTT001": ("Công ty Cổ phần Văn Hóa Việt", 5000000.0),
        "NTT002": ("Tập đoàn Sách Toàn Cầu", 8000000.0),
        "NTT003": ("Công ty TNHH Nghệ Thuật Trẻ", 3000000.0),
        "NTT004": ("Tập đoàn Ẩm Thực ABC", 10000000.0),
        "NTT005": ("Ngân hàng XYZ", 15000000.0)
    }

    print('1. Quản lí sự kiện')
    print('2. Quản lí nhà tài trợ')
    menu = int(input('Vui lòng chọn menu: '))

    if menu == 1:
        quan_ly_su_kien(danh_sach_su_kien)
    elif menu == 2:
        quan_ly_nha_tai_tro(nha_tai_tro)


# main chạy chính
if __name__ == "__main__":
    main()
