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

# Bài tập

# age = int(input("Vui lòng nhập tuổi của bạn: "))
# if age >= 18: # Nếu người dùng từ 18t trở lên
#     print('Bạn đã đủ tuổi lái xe')
# else: # nếu chưa đủ tuổi lái xe
#     print('Bạn phải chờ thêm', 18 - age, 'năm nữa.')

# my_age = 20
# your_age = int(input('Vui lòng nhập tuổi của bạn: '))
#
# if your_age > my_age:
#     chenh_lech = your_age - my_age
#     if chenh_lech == 1:
#         print('You are 1 year older than me.')
#     else:
#         print(f'You are {chenh_lech} years older than me.')
# else:
#     print('Bạn nhỏ hơn tôi', my_age - your_age, 'tuổi')

# ab = int(input('Vui lòng nhập 1 số: '))
# bc = int(input('Vui lòng nhập 1 số: '))
#
# if ab > bc:
#     print('Số', ab, 'lớn hơn số', bc)
# elif ab < bc:
#     print('Số', ab, 'nhỏ hơn số', bc)
# else:
#     print('2 số bằng nhau.')

# point = int(input('Vui lòng nhập điểm số của bạn: '))
# if 80 <= point <= 100:
#     print('Điểm của bạn thuộc loại: A')
# elif 70 <= point <= 89:
#     print('Điểm số của bạn thuộc loại: B ')
# elif 60 <= point <= 69:
#     print('Điểm số của bạn thuộc loại: C')
# elif 50 <= point <= 59:
#     print('Điểm của bạn thuộc loại: D')
# else:
#     print('Điểm của bạn thuộc loại F')


# mua = int(input('Vui lòng nhập tháng: '))
# if mua == 3 or mua == 4 or mua == 5:
#     print('Tháng bạn vừa nhập thuộc mùa xuân')
# elif mua == 6 or mua == 7 or mua == 8:
#     print('Tháng bạn vừa nhập thuộc mùa hạ')
# elif mua == 9 or mua == 10 or mua == 11:
#     print('Tháng bạn vừa nhập thuộc mùa thu')
# elif mua == 12 or mua == 1 or mua == 2:
#     print('Tháng bạn vừa nhập thuộc mùa đông')
# else:
#     print('Vui lòng nhập tháng hợp lệ ( Tháng 1 --> Tháng 12 )')

# fruits = ['banana', 'orange', 'mango', 'lemon']
#
# new_fruits = input('Thêm hoa quả: ')
# if new_fruits in fruits: #Dùng in để kiểm tra xem new_fruits có trong danh sách fruits không
#     print('Sản phẩm này đã có trong danh sách')
# else:
#     fruits.append(new_fruits)
#     print('Sản phẩm đã thêm vào danh sách: ', new_fruits)
#     print('Danh sách mới là: ', fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    print('Person có skill rồi nhé')
    middle_skills = len(person['skills']) // 2
    skill = person['skills'][middle_skills]
    print('Skills ở giữa danh sách là: ', skill)
    if 'Python' in person['skills']:
        print('Skill có Python nhé')
    else:
        print('Skill không có python')

    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('Anh ấy là nhà phát triển Frontend')
    elif 'MongoDB' in person['skills'] and 'Python' in person['skills'] and 'Node' in person['skills']:
        print('Anh ấy là nhà phát triển back-end')
else:
    print('Person không có skills')

if person['is_marred'] == True and person['country'] == 'Finland':
    print('Anh ấy sống ở Phần Lan, anh ấy đã kết hôn')


