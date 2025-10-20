# Bài tập
#1
def add_two_numbers(a, b):
    total = a + b
    return total
print('Tổng của a va b là: ', add_two_numbers(a = 10, b = 15))

#2
def dien_tich_hinh_tron(r):
    pi = 3.14
    dien_tich = pi * r * r
    return dien_tich
print('Diện tích của hình tròn là: ', dien_tich_hinh_tron(5))

#3
def add_all_nums(*nums):
    total = 0
    for num in nums:
        # dùng isinstance để kiểm tra kiểu dữ liệu
        if not isinstance(num, (int, float)): # kiểm tra xem num có phải int hoặc float ko
            return f"Lỗi: {num} không phải là 1 số" # nếu ko sẽ báo lỗi
        total = total + num
    return total
print('Tổng tất cả các số là: ', add_all_nums(10, 'abc', 15, 20))

#4
def doi_nhiet_do_c_sang_f(do_c):
    do_f = (do_c * 9/5) + 32
    return do_f
print('Độ C chuyển sang độ F là: ', doi_nhiet_do_c_sang_f(35), 'độ F')

#5
def check_season(thang):
    if thang in [1,2,3,4]:
        return 'Mùa xuân'
    elif thang in [5,6,7]:
        return 'Mùa hạ'
    elif thang in [8,9,10]:
        return 'Mùa xuân'
    elif thang in [11, 12]:
        return 'Mùa đông'
    else:
        return ('Tháng ko hợp lệ : Tháng từ 1 - 12')
print('Tháng này thuộc: ', check_season(12))

# lấy danh sách làm tham số và in ra từng phần tử của danh sách
def print_list(lists):
    for list in lists:
        print(list)
print_list(['Táo','Chuối','Cam'])
