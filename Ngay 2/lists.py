# # Dùng list
# danh_sach = list("python") # dùng list sẽ tách từng phần tử
# print(danh_sach)
#
# # Dùng dấu []
# danh_sach1 = ["python", "php", "laravel"] # Khi dùng [] thì danh sách sẽ chứa được nhiều giá trị
# print(danh_sach1)
#
# fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
# web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
# countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
#
# print("fruits: ", fruits, len(fruits))
# print("vegetables: ", vegetables, len(vegetables))
# print("animal_products: ", animal_products, len(animal_products))
# print("web_techs: ", web_techs, len(web_techs))
# print("countries: ", countries, len(countries))
#
# test_list = [1, "ngoc tan", True, {"hihi"}]
# print(test_list)
# print(type(test_list))
# print(len(test_list)),
#
# danh_sach_2 = ['Nguyen Ngoc Tan', 20, {"php", "laravel"}, 11]
# print(danh_sach_2)
# tim_phan_tu = danh_sach_2[0]
# print(tim_phan_tu)
# tim_phan_tu2 = danh_sach_2[1]
# print(tim_phan_tu2)
# tim_phan_tu3 = danh_sach_2[2]
# print(tim_phan_tu3)
#
# last_index = len(danh_sach_2) - 1
# last_danh_sach = danh_sach_2[last_index]
# print(last_danh_sach)
# last_index2 = danh_sach_2[-1]
# print(last_index2)
#
#
# a = ["php", "python", "java", "c++"]
# print(a)
# list_a = a[-1]
# print(list_a)
# list_b = a[-4]
# print(list_b)
#
# # Giari nén danh sách
# list_kk = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# gia_tri_a, gia_tri_b, * rest = list_kk
# print(gia_tri_a)
# print(gia_tri_b)
# print(rest)
#
# o_giua = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'Tan']
# one_o_giua, two_o_giua, three_o_giua, * rust, night_cuoi = o_giua
# print(one_o_giua)
# print(two_o_giua)
# print(three_o_giua)
# print(rust)
# print(night_cuoi)
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits = fruits[0:5]
# print(all_fruits)
# tu1den3 = fruits[1:4]
# print(tu1den3)
# tu2denhet = fruits[2:]
# print(tu2denhet)
# caicuoi = fruits[::5]
# print(caicuoi)
# soam = fruits[-4:]
# print(soam)
# daonguoc = fruits[::-1]
# print(daonguoc)
from os import remove

# # Sửa dổi phần tử trong danh sách
# update = ['banana', 'orange', 'mango', 'lemon'] # khai báo 1 danh sách có đầy đủ index
# update[0] = 'apple' # sửa phần tử index của 0 là phần tử đầu tiên
# print(update)
# update[1] = 'banana'
# print(update)
# update[2] = 'lemon'
# print(update)
# last_index = len(update) - 1
# update[last_index] = 'mango'
# print(update)

# Kiểm tra xem phần tử có thuộc danh sách không
# danh_sach = ['banana', 'orange', 'mango', 'lemon']
# kiem_tra = 'banana' in danh_sach
# print(danh_sach)
# print(kiem_tra)
# kiem_tra2 = 'orange' in danh_sach
# print(kiem_tra2)
# kiem_tra3 = 'huhu' in danh_sach
# print(kiem_tra3)

# Thêm phần tử mới vào danh sách dùng append()
# danh_sach_trong = [] # khởi tạo 1 danh sách trống
# danh_sach_trong.append('Hello')
# danh_sach_trong.append('World')
# print(danh_sach_trong)


# Chèn mục vào danh sách dùng insert(index, '')
# danh_sach = [1,2,3,4,5,6,7,8,9]
# danh_sach.insert(1, 'Hello')
# print(danh_sach)
# danh_sach.insert(4, 'Đây là trước số 4 vì đã thêm Hello')
# print(danh_sach)

# Xóa mục trong danh sách dùng remove()
# fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
# fruits.remove('banana')
# print(fruits)

# Xóa mục dùng pop() : pop sẽ xóa theo index nếu để mặc định thì xóa phần tử cuối cùng
# fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
# fruits.pop(0)
# print(fruits)

# Xóa mục bằng del : del có thể xóa theo index hoặc xóa theo phạm vi hoặc xóa tất cả
# fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
# del fruits[0]
# print(fruits)
# del fruits[1:]
# print(fruits)
# del fruits
# print(fruits)


# Xóa các mục bằng danh sách dùng clear : clear sẽ làm trống danh sách đó
# fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
# fruits.clear()
# print(fruits)


# Bài tập
# Khai báo danh sách rỗng
danh_sach_rong = []
print(danh_sach_rong)

# Khai báo danh sách có nhiều hơn 5 mục
danh_sach_co_nhieu_hon_5muc = ['php', 'laravel', 'python', 'java', 'c++', 'js']
#tìm độ dài danh sách dùng len()
print(len(danh_sach_co_nhieu_hon_5muc))

# Lấy phần tử đầu tiên, phần tử ở giữa và phần tử cuối cùng của danh sách
dau = danh_sach_co_nhieu_hon_5muc[0]
print(dau)
giua = len(danh_sach_co_nhieu_hon_5muc) // 2
so_giua =   danh_sach_co_nhieu_hon_5muc[giua]
print(so_giua)
cuoi = danh_sach_co_nhieu_hon_5muc[-1]
print(cuoi)

# Khai báo một danh sách có tên là mixed_data_types,
# điền (tên, tuổi, chiều cao, tình trạng hôn nhân, địa chỉ) của bạn
mixed_data_types = ['Tấn', 20, 1.70, 'Chưa kết hôn', 'Hà Nội']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print("Số lượng công ty là:", len(it_companies))
congty1 = it_companies[0]
middle_compani = len(it_companies) // 2
middle_giua = it_companies[middle_compani]
print(middle_giua)
congtycuoi = it_companies[-1]
print(congtycuoi)

# sửa công ty
it_companies[0] = 'Facebooks'
print(it_companies)

# thêm công ty dùng append()
it_companies.append('CNTT')
print(it_companies)

middle_compani2 = len(it_companies) // 2
# chèn công ty vào giữa dùng insert(index, '')
it_companies.insert(middle_compani2, 'CNTT')
print(it_companies)

# Đổi 1 công ty thành chữ in hoa dùng upper
index = 0
it_companies[index] = it_companies[index].upper()
print(it_companies)

# Nối danh sách lại với nhau thành 1 chuỗi duy nhất dùng join
# join_companies = ','.join(it_companies)
# print(join_companies)

# Kiểm tra xem công ty có tồn tại không dùng in
kiemtra_companies = 'Google' in it_companies
print(kiemtra_companies)

# Sắp xếp danh sách bằng phương thức sort()
# it_companies.sort()
# print(it_companies)
# # sắp sếp theo thứ tự giảm dần dùng reverse()
# it_companies.reverse()
# print(it_companies)

# xóa 3 công ty đầu tiên khỏi danh sách có thể dùng remove(), pop(), hoac del
# remove chỉ xóa chay được 1 phần tử
# pop sẽ xóa đc phần thử theo index, và nếu để trống sẽ xóa phần tử cuối cùng
# còn del thì linh hoạt có thể xóa theo phạm vi [0:10] hoặc xóa luôn biến

# Remove
# it_companies.remove('FACEBOOKS')
# it_companies.remove('Google')
# print(it_companies)

# pop()
# delete_companies = it_companies.pop(0)
# print(it_companies)

# tốt nhất dùng del
del it_companies[0:2]
print(it_companies)
del it_companies[5:]
print(it_companies)

# xóa công ty ở giữa
companies_middle = len(it_companies) // 2
print(companies_middle)
del it_companies[companies_middle]
print(it_companies)

# xóa tất cả thì dùng clear
it_companies.clear()
print(it_companies)

# Nối 2 danh sách lại với nhau dùng merged
backend = ['PHP', 'Laravel', 'Python', 'Java']
frontend = ['Vuejs', 'Angularjs', 'Reactjs']

merged = backend + frontend
print(merged)

# Sao chép danh sách nối dùng copy()

full_stack = merged.copy()
print(full_stack)

# Tìm Redux
vi_tri_redux = full_stack.index('Java')
# Chèn SQL & Python vào
full_stack.insert(vi_tri_redux + 1, 'SQL')
full_stack.insert(vi_tri_redux + 2, 'NodeJS')
print(full_stack)









