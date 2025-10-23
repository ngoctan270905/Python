language = 'Python'
lst = list(language)
print(lst)

lst_comprehension = [i for i in language]
print(lst_comprehension)

# Tạo số
numbers = [i for i in range(11)]
print(numbers)

squares = [i * i for i in range(11)] # giá trị i * i
print(squares)

numbers = [(i, i*i) for i in range(11)] # tuple (i, i*i)
print(numbers)

# sinh s ố chẵn bằng list comprehension
even_number = [i for i in range(21) if i % 2 == 0]
print(even_number)

# số lẻ
old_number = [i for i in range(30) if i % 2 != 0]
print(old_number)

# loc ra số chẵn dương từ danh sách
numberss = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
loc = [i for i in numberss if i % 2 == 0 and i > 0]
print(f"Số dương chẵn là: {loc}")

# Mảng 3 chiều
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Danh sách chưa làm phẳng: {list_of_lists}")
flatten_list = [number for i in list_of_lists for number in i]
print('Danh sách đc làm phẳng: ', flatten_list)

# HÀM THÔNG THƯỜNG
def nhan_doi(x):
    return x * 2
print(nhan_doi(10))

# Hàm lambda
nhan_doi = lambda x: x*2
print(nhan_doi(10))

def add_two_nums(a, b):
    return a + b
print(add_two_nums(1, 2))

add_two_nums = lambda a, b: a+b
print(add_two_nums(1, 2))

# HÀM LAMBDA BÊN TRONG HÀM KHÁC
def power(x):
    return lambda n: x ** n
cuber = power(3)(4)
print(cuber)

# BÀI TẬP
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
loc_so_am = [i for i in numbers if i <= 0 ]
print(f"Số âm và số 0 là: {loc_so_am}")

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lam_phang = [number for i in list_of_lists for list in i for number in list]
print(lam_phang)

danh_sach = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(danh_sach)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
cat_chuoi = [[country[0].upper(), country[0][:3].upper(), country[1].upper()]
             for lay_ds_1 in countries
             for country in lay_ds_1]
print(cat_chuoi)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
chuyen_thanh_ds = [{'country':country[0].upper(), 'city':country[1].upper()}
                   for lay_ds in countries
                   for country in lay_ds]
print(chuyen_thanh_ds)

names = [[('Asabeneh', 'Yetayeh')],
         [('David', 'Smith')],
         [('Donald', 'Trump')],
         [('Bill', 'Gates')]]
full_name = [f"{first} {last}"
             for lay_ds in names
             for (first, last) in lay_ds]
print(full_name)



