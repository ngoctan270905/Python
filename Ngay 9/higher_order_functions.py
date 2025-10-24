#CHỨC NĂNG NHƯ 1 THAM SỐ
def tinh_tong(x):
    return sum(x)

def ham_bac_cao(f, lst):
    tinh_tong = f(lst)
    return tinh_tong

hihi = ham_bac_cao(tinh_tong, [1,2,3,4,5,6])
print(hihi)

# Chức năng như 1 giá trị trả về
def greeting():
    def say_hello():
        return "Hello"
    return say_hello()

# Lấy hàm
lay_ham = greeting()
print(lay_ham)

def get_operation(ob):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    if ob == '+':
        return add
    elif ob == '-':
        return subtract
    elif ob == '*':
        return multiply
lay_ham = get_operation('+')
print(lay_ham(1, 2))
lay_ham1 = get_operation('-')
print(lay_ham1(2, 1))
lay_ham2 = get_operation('*')
print(lay_ham2(2, 3))

def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def ham_bac_cao(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

test = ham_bac_cao('square')
print(test(5))

# Đóng cửa Closure
def add_ten():
    ten = 10

    def add(num):
        return num + ten

    return add

lay_ham = add_ten() # lay_ham sẽ lưu thông tin của biến ten = 10
print(lay_ham(10))

def make_multiplier(n):
    """Tạo hàm nhân với số n"""
    def multiply(x):
        return x * n  # 'n' được nhớ bởi closure
    return multiply

lay_ham = make_multiplier(10) # nhớ đc n = 10
print(lay_ham(10))


#DECORETOR
import time

def timer_decorator(function):
    def wrapper():
        start = time.time()
        result = function()  # Chạy hàm gốc
        end = time.time()
        print(f"Thời gian: {end - start:.4f} giây")
        return result
    return wrapper

@timer_decorator
def slow_function():
    return "Xong!"

print(slow_function())
# Output:
# Thời gian: 2.0012 giây
# Xong!


# CÁC HÀM BẬC CAO TÍCH HỢP SẴN
# hàm map(function, iterable) # function: hàm đc gọi cho từng phần tử, interable : các danh sách
number = [1,2,3,4,5]

def square(x):
    return x ** 2

numbers_squared = map(square, number)
print(list(numbers_squared))

numbers_squareds = map(lambda x: x**2, number)
print(list(numbers_squareds))

# chuyển đổi kiểu dữ liệu
numbers_str = ['1', '2', '3', '4', '5']  # iterable
number_int = map(int, numbers_str)
print(list(number_int))

# duyệt qua danh sách tên
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def in_hoa(name):
    return name.upper()

name_upper = map(in_hoa, names)# duyệt qua danh sách name và gán từng dữ liệu vào function
print(list(name_upper))

# dùng lambda
names_upper = map(lambda name: name.upper(), names)
print(list(names_upper))

#HÀM HỌC : FILTER
# filter ( function, interable )
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(f"Các số chẵn là: {list(even_numbers)}")

def is_odd(num):
    if num % 2 != 0:
        return True
    return False
odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))

# Lọc tên dài nhất
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def ten_dai_nhat(ten):
    if len(ten) > 7:
        return True
    return False
ten_dai = filter(ten_dai_nhat, names)
print(list(ten_dai))

from functools import reduce

# Hàm REDUCE
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15

# Bfai tập
# MAP: duyệt và biến đổi phần tử
# FILTER: duyệt và lọc từng phần tử theo điều kiện
# REDUCE: Gộp toàn bộ danh sách thành 1 giá trị duy nhất
# Hàm bậc cao là hàm có thể nhận hàm khác làm tham số, hoặc trả về 1 hàm khác làm kết quả
# Hàm closue là hàm đc lồng ở bên trong nhớ đc biến bao ngoài ngay cả khi chương trình đã chạy kết thúc
# Hàm decorator là hàm trang trí giúp thay đổi logic thêm logic mà ko cần phải sửa code gốc

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for quoc_gia in countries:
    print(f"Quốc gia: {quoc_gia}")
for ten in names:
    print(f"Tên là: {ten}")
for so in numbers:
    print(f"Số là: {so}")

def upper_country(x):
    return x.upper()

contry_upper = map(upper_country, countries)
print(list(contry_upper))

def binh_phuong(a):
    return a ** a

thay_doi_binh_phuong = map(binh_phuong, numbers)
print(list(thay_doi_binh_phuong))

def in_hoa(name):
    return name.upper()
in_hoa_ten = map(in_hoa, names)
print(list(in_hoa_ten))

def loc_quoc_gia(loc):
   return 'land' in loc
loc_land = filter(loc_quoc_gia, countries)
print(list(loc_land))

def loc_ki_tu(quoc_gia):
    if len(quoc_gia) == 6:
        return True
    return False

loc_ki_tu = filter(loc_ki_tu, countries)
print(list(loc_ki_tu))

def loc_ki_tu2(quoc_gia2):
    if len(quoc_gia2) > 6:
        return True
    return False

loc_ki_tu = filter(loc_ki_tu2, countries)
print(list(loc_ki_tu))

def loc_ki_tu3(quoc_gia3):
    if quoc_gia3[0] == 'E':
        return True
    return False
loc_ki_tu3 = filter(loc_ki_tu3, countries)
print(list(loc_ki_tu3))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ket_qua = reduce(
    lambda x, y: x + y,
    filter(
        lambda x: x > 5,
        map(lambda x: x * 2, arr)
    )

)
print(ket_qua)

def get_string_lists(lst):
    return [item for item in lst if isinstance(item, str)]

list_test = ['Hihi', 10, 7.65, 'HUHU']
ket_qua = get_string_lists(list_test)
print(ket_qua)







