# Conditional trong python

# ĐIỀU KIỆN IF ELSE
a = -3
if a > 0:
    print(a, 'lớn hơn 0')
else:
    print(a, 'nhỏ hơn 0')

# ĐIỀU KIỆN IF ELIF ELSE ( khi cần xử lí nhiều điều kiện )
b = 0
if b > 0:
    print("B lớn hơn 0")
elif b < 0:
    print("B nhỏ hơn 0")
else:
    print("B bằng 0")

# ĐIỀU KIỆN LỒNG NHAU

c = 6
if c > 0:
    if c % 2 == 0: # Kiểm tra xem C có chia hết cho 2 không
        print("C là số chẵn") # nếu / hết cho 2 thì là số chắn
    else:
        print('C là số lẻ') # ko thì else hiển thị số lẻ
elif c == 0:
    print('C là số không')
else:
    print('C nhỏ hơn 0')

# ĐIỀU KIỆN VÀ TOÁN TỬ LOGIC

d = -1
if d > 0 and d % 2 == 0:
    print('d là số nguyên chẵn và dương')
elif d > 0 and d % 2 != 0:
    print('d là số nguyên dương')
elif d == 0:
    print('d là số không')
else:
    print('d là số âm')

# TOÁN TỬ LOGIC IF VÀ OR
user = 'Tấn'
acess_level = 3

# Nếu user là 'admin' hoặc cấp độ truy cập >= 4 thì user sẽ có quyền truy cập
if user == 'admin' or acess_level >= 4:
    print('Đã cấp quyền truy cập')
else:  # nếu không đáp ứng điều kiện trên thì in thông báo thất bại
    print('Truy cập thất bại')

# # Bài tập
# age = int(input('Vui lòng nhập tuổi của bạn: '))
#
# if age >= 18: # Nếu người dùng từ 18 tuổi trở lên
#     print('Bạn đã đủ tuổi để lái xe')
# else:
#     print('Bạn chưa đủ tuổi để lái xe.', 'Hãy chờ thêm', 18 - age, 'năm nữa')

# 2.
my_age = 20
your_age = int(input('Nhập tuổi của bạn: '))

if your_age > my_age:
    chenh_lech = your_age - my_age
    if chenh_lech == 1:
        print('Bạn lớn hơn tôi 1 year')
    else:
        print(f'Bạn lớn hơn tôi {chenh_lech} years ')



