# VARIABLES TRONG PYTHON
# Variable la bien, dung de luu tru gia tri
# Khai bao bien: ten_bien = gia_tri
# không cần khai báo kiểu dữ liệu mặc định python sẽ tự động xác định kiểu dữ liệu

# Tên biến phải bắt đầu bằng chữ cái hoặc dấu gạch dưới (_)
# Tên biến không được chứa ký tự đặc biệt và không được trùng với từ khóa

# Ví dụ khai báo biến
a = 5 # python tự động xác định a là kiểu int
b = 3.14 # python tự động xác định b là kiểu float
name = "Tan" # python tự động xác định name là kiểu str
is_student = True # python tự động xác định is_student là kiểu bool

# Ví dụ đặt tên biến đúng quy tắc
my_name1 = "Tan" # đúng
name_123 = "Tan" # đúng
# 1name = "Tan" # sai, bắt đầu bằng số
print(my_name1)
print(name_123)

# Đặt nhiều biến cùng lúc
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

# Đặt nhiều biến cùng giá trị 
# Đặt kiểu này thì các biến bằng nhau
x = y = z = 5
print(x)
print(y)
print(z)

# Gán giá trị của biến này cho biến khác
a = 10
b = a
print(b) # In ra 10

name = "Tan"
ten = name
print(ten) # In ra Tan

# Ep kieu du lieu ( type casting )
# Casting la chuyen doi kieu du lieu cua bien sang kieu du lieu khac 
# Cac ham ep kieu du lieu co ban trong python: int(), float(), str(), bool() 
#int(): chuyen sang so nguyen
#float(): chuyen sang so thuc
#str(): chuyen sang chuoi
#bool(): chuyen sang kieu bool (True hoac False)

#VD ep tu str sang int
a = "5" # a la kieu str
b = int(a) # => b se ep kieu str sang int
print(b) # In ra 5
print(type(b)) # In ra <class 'int'>

#VD ep tu float sang int
c = 3.11 # c la kieu float
d = int(c) # => d se ép kieu tu float sang int
print(d) # In ra 3
print(type(d)) # In ra <class 'int'>

#VD ep tu str sang chuoi
e = str(10) # e duoc ep kieu int sang str
print(e) # In ra 10
print(type(e)) # In ra <class 'str'>

#VD ep tu int sang float
f = 5 # f la kieu int
g = float(f) # => g se ep kieu int sang float
print(g) # In ra 5.0
print(type(g)) # In ra <class 'float'>


# VD 
name = 'Tan'
age = 20
height = 1.70
is_student = True

print("Ten cua toi la:", name)
print(type(name))
print("Tuoi cua toi la:", age)
print("Chieu cao cua toi la:", height)
print("Toi la sinh vien:", is_student)


# Bài tập Python:
# 1. Tạo biến: ten, tuoi, chieu_cao
# 2. In ra câu:
#    "Xin chào [ten], bạn [tuoi] tuổi, cao [chieu_cao] m."
# 3. Ép kiểu 'tuoi' sang str khi nối chuỗi

ten = "Nguyen Ngoc Tan"
tuoi = 20
casting_tuoi = str(tuoi) # ép kieu tuoi tu int sang string
chieu_cao = 1.71
casting_chieu_cao = str(chieu_cao) # ép kieu chieu_cao tu float sang string

# Dung ep kieu thu cong
print("Xin chao " + ten + ", ban hien " + casting_tuoi + " tuoi, ban cao " + casting_chieu_cao + " m")
# dung f-string
print(f"Xin chao {ten}, ban hien dang {tuoi} tuoi, chieu cao cua ban la {chieu_cao} m")

# Bài tập Python

# 1. Khai báo biến
# Tạo các biến:
# ten → str
# tuoi → int
# chieu_cao → float
# is_student → bool

# 2. In ra thông tin cá nhân
# In ra câu:
# "Xin chào [ten], bạn [tuoi] tuổi, cao [chieu_cao] m., học sinh? [is_student]"

# Sử dụng cả 2 cách:
# Cách 1: Nối chuỗi + ép kiểu
# Cách : f-string

# 3. Gán giá trị của biến này cho biến khác
# Tạo biến mới ten_hoc_vien và gán bằng ten
# In ra ten_hoc_vien

# 4. Gán nhiều biến cùng lúc
# Tạo 3 biến a, b, c và gán cùng giá trị là 10
# In ra tất cả biến

# 5. Ép kiểu
# Tạo biến diem = "8.5" (str)
# Ép diem sang float và in ra giá trị + kiểu dữ liệu

# 6. Bài tập mở rộng (tùy chọn)
# Tạo 2 biến x = 5, y = 2
# Tính tổng, hiệu, tích, thương, chia lấy phần nguyên và lũy thừa
# In ra kết quả cùng với kiểu dữ liệu từng phép tính

ten1 = "Tan"
tuoi1 = 20
casting_tuoi1 = str(tuoi1)
chieu_cao1 = 1.71
casting_chieu_cao1 = str(chieu_cao1)
is_student1 = True
casting_is_student1 = str(is_student1)
#cach 1
print("Xin chao " + ten1 + ", ban hien " + casting_tuoi1 + " tuoi, ban cao " + casting_chieu_cao1 + " va dang la hoc sinh " + casting_is_student1)
print(f"Xin chao {ten1}, ban {tuoi1}, cao {chieu_cao1}, va dang la hoc sinh {is_student}")

ten_hoc_vien = ten1
print("ten_hoc_vien:", ten_hoc_vien)

a = b = c = 10
print(a)
print(b)
print(c)

diem = "8.5"
casting_diem = float(diem)
print("Diem cua ban la:", casting_diem)
print(type(casting_diem))

x = 5
y = 2

print("Tong cua x va y la:", x + y)
print(type(x+y))
print("Hiệu cua x va y la:", x - y)
print(type(x-y))
print("Tich cua x va y la:", x * y)
print(type(x*y))
print("Thuong cua x va y la:", x / y)
print(type(x/y))
# Neu muon chi lay phan nguyen thi dung //
print("Thuong cua x va y la:", x // y)
print(type(x//y))



# BIẾN TOÀN CỤC








