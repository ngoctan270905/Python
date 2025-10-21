# QUẢN LÍ CỬA HÀNG SÁCH

# 1.Khởi tạo dữ liệu kiến thức về biến, datatypes, comment, syntax, number, string
# khai báo 1 list danh sách sách ( mỗi cuốn là dictionary )
list_sach = [
    {
        'ten_sach': 'Doraemon',  # string
        'gia': 100000,  # float, int
        'ton_kho': 100,  # int
        'so_luong_da_ban': 0  # int
    },
    {
        'ten_sach': 'Pikachu',
        'gia': 100000,
        'ton_kho': 100,
        'so_luong_da_ban': 0
    },
    {
        'ten_sach': 'Dế mèn phiêu lưu kí',
        'gia': 100000,
        'ton_kho': 100,
        'so_luong_da_ban': 0
    },
    {
        'ten_sach': 'Nobita',
        'gia': 100000,
        'ton_kho': 100,
        'so_luong_da_ban': 0
    },
    {
        'ten_sach': '7 viên ngọc rồng',
        'gia': 100000,
        'ton_kho': 100,
        'so_luong_da_ban': 0
    },
]


# Operators, casting, function
# bắt 3 tham số đc truyền vào từ main
def tinh_hoa_don(sach_mua, so_luong_mua, loai_khach_hang):

    # tính tổng tiền theo công thức

    if loai_khach_hang.lower() == 'vip':
        print('Bạn là khách vip nên đã được giảm 10% tổng tiền. Chúc mừng bạn')
        tong_tien = sach_mua['gia'] * so_luong_mua
        tong_tien = tong_tien - ( tong_tien * 0.1 )
    else:
        tong_tien = sach_mua['gia'] * so_luong_mua

    # cập nhật tồn kho = cách tồn kho của sp đang mua - số lượng khách hàng mua
    sach_mua['ton_kho'] = sach_mua['ton_kho'] - so_luong_mua
    # cập nhật số lượng đã bán  = số lượng mua ban đầu của sp đang mua + số lượng khách hàng mua
    sach_mua['so_luong_da_ban'] = sach_mua['so_luong_da_ban'] + so_luong_mua

    print(f"Tổng tiền hóa đơn là: {tong_tien} VND")
    print('Cảm ơn bạn đã mua hàng nhé.')
    print('')
    return True

def kiem_tra_ton_kho(sach_mua, so_luong_mua):
    if so_luong_mua < 0: # nếu số lượng mua < 0
        print('Số lượng mua phải bắt đầu từ 1')
        return False # Kết quả False vòng while ở main sẽ lặp lại

    if so_luong_mua > sach_mua['ton_kho']:
        print('Số lượng vượt quá tồn kho, vui lòng nhập lại')
        return False #

    return True # True main nhận đc kết quả và break sẽ dừng vòng lặp

def tao_ma_giam_gia(ten_khach_hang, loai_khach_hang):
    if loai_khach_hang.lower() == 'vip':
        return ten_khach_hang.upper() + '_VIP'
    elif loai_khach_hang.lower() == 'thuong':
        return ten_khach_hang.upper() + '_REG'

def thong_ke_sach(list_sach):
    print('THỐNG KÊ SÁCH')
    print('1. Sách có lượt bán trên 10?')
    print('2. Sách bán chạy nhất?')
    menu_thong_ke = int(input('Chọn menu: '))
    if menu_thong_ke == 1:
        print('Danh sách bán trên 10 quyển')
        co_sach = False
        for sach in list_sach:
            if sach['so_luong_da_ban'] > 10:
                print(f"Tên sách: {sach['ten_sach']} - {sach['so_luong_da_ban']}")
                co_sach = True
        if not co_sach:
            print('Không có quyển nào bán tren 10 quyển:')
        print('')
    elif menu_thong_ke == 2:
        sach_ban_chay_nhat = list_sach[0]
        i = 0
        while i < len(list_sach):
            if list_sach[i]['so_luong_da_ban'] > sach_ban_chay_nhat['so_luong_da_ban']:
                sach_ban_chay_nhat = list_sach[i]
            i = i + 1
        print(f"Sách bán chạy nhất: {sach_ban_chay_nhat['ten_sach']} - Đã bán: {sach_ban_chay_nhat['so_luong_da_ban']}")


# hàm main là hàm chính chạy đầu tiên
def main():
    print('Chào mừng đến cửa hàng sách!')
    ten_khach_hang = input('Nhập tên của bạn: ').strip() # dùng strip để laoij bỏ khoảng trắng
    loai_khach_hang = input('Bạn thuộc loại khách hàng nào? (Thường/VIP)?: ').strip()
    ma_giam_gia = tao_ma_giam_gia(ten_khach_hang, loai_khach_hang)
    print(f"Mã giảm giá của bạn là: {ma_giam_gia}")

    while True:  # tạo vòng lặp
        print('------------Danh sách sách hiện có---------------')
        # dùng for lặp list_sach ( enumerate ) để lấy được index và giá trị rồi gán cho i và sách
        for i, sach in enumerate(list_sach, start=1): # start = 1 để số thứ tự bắt đầu từ 1
            print(f"{i}. {sach['ten_sach']} - Giá: {sach['gia']} - Tồn kho: {sach['ton_kho']} - Đã bán: {sach['so_luong_da_ban']}")


        print('Menu: 1.Mua sách    2.Thoát    3.Thống kê')
        menu = int(input())
        if menu == 1:
            ten_sach_mua = input('Nhập tên sách bạn muốn mua:').strip()
        elif menu == 2:
            print('Cảm ơn bạn đã ghé qua hàng của mình nhé.')
            continue # continue sẽ dừng vòng lặp này và quay về vòng lặp tiếp
        elif menu == 3:
            thong_ke_sach(list_sach) # gọi đến hàm thong kê sách
            continue
        else:
            print('Chỉ được chọn 1 trong 2 menu ở trên')

        # kiểm tra sách tồn tại
        sach_mua = None
        for sach in list_sach: # lặp list sách để tìm sách
            if sach['ten_sach'].lower() == ten_sach_mua.lower(): # nếu tên sách = tên sách đã nhập ( ten_sach_mua )
                sach_mua = sach # thì biến sách mua đc gán trị từ sach vào
                break # dừng và chuyển sang logic tiếp
        if not sach_mua: # n
            print('Sách không tồn tại, vui lòng nhập đúng')
            continue

        while True: # vòng lặp chương trình đến khi nhận được kết quả True từ hàm kiểm tra tồn kho
            so_luong_mua = int(input('Số lượng: '))
            if kiem_tra_ton_kho(sach_mua, so_luong_mua):
                break

       # sau khi nhập tt và ktra xong thì sẽ gọi hàm tinh_hoa_don đồng thời truyền 3 tham số để xử lí
        tinh_hoa_don(sach_mua, so_luong_mua, loai_khach_hang)



main()
