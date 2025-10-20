# FUNCTION TRONG PYTHON
# Hàm không có tham số
from pyexpat.errors import messages


def generate_full_name():
    first_name = 'Nguyễn'
    last_name = 'Tấn'
    space = ' '
    full_name = first_name + space + last_name
    # hàm ko lưu giá trị
    # print(full_name)
    # muốn lưu giá trị thì dùng return
    return full_name
print(generate_full_name())

def add_two_numbers():
    a = 1
    b= 2
    total = a + b
    # hàm không lưu giá trị
    # print(total)
    return total
print(add_two_numbers())

# HÀM CÓ THAM SỐ
def greeting(name):
    message = 'Hello ' + name
    return message
print(greeting('Tấn'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def test(x):
    return x * x
print(test(2))

def sum_of_number(n):
    total = 0
    for i in range(n+1):
        total = total + i
    return total
print(sum_of_number(10))

# hàm 2 tham số
def full_names(first_name, last_name):
    full_namee = first_name + ' ' + last_name
    return full_namee
print('Full name: ', full_names(last_name='Tấn', first_name='Nguyễn'))

def weight_of_object(khoi_luong, trong_luc):
    weight = str(khoi_luong * trong_luc) + 'N'
    return weight
print('Trọng lượng của 1 vật tính bằng N: ',weight_of_object(100,9.81))

def is_even(n):
    if n % 2 == 0:
        print('even')
        return True
    return False
print(is_even(n = 10))
print(is_even(7))

def find_even_numbers(n):
    even_numbers = []
    for i in range(n + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
print(find_even_numbers(10))

# Hàm có tham số mặc định
def greeting3(name = 'Tấn'):
    message = 'Hello ' + name
    return message
print(greeting3(name = 'Tú'))

# Số lượng đối số
def sum_all_nums(*nums):
    totaler = 0
    for num in nums:
        totaler = totaler + num
    return totaler
print(sum_all_nums(10,20,30,40,50,60,70,80,90))

def show_students(*names):
    print('Danh sách học viên')
    for name in names:
        print('-', name)
show_students('Tấn', 'Tú', 'Trọng')

# Hàm có tham số mặc định và tham số tùy ý
def generate_groups(team, *huhu):
    print(team)
    for i in huhu:
        print(i)
generate_groups('ABCDE', 'Face', 'Mentor')



