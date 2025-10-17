# DICTIONARIES TRONG PYTHON

person = {
    'name': 'Tấn',
    'age': 20,
    'que_quan': 'Hà Nam',
    'skill': ['Python', 'Java', 'PHP', 'Javascript'],
    'is_student': True,
    'dia_chi': {
        'ngo':39,
        'duong': 'hồ tùng mậu'
    }
}
print("Độ dài của dictionaries: ", len(person))

#TRUY CẬP CÁC MỤC TRONG DICTIONARIES dùng person['']

print(person['name'])
print(person['age'])
print(person['que_quan'])
print(person['skill'])
print(person['is_student'])
print(person['dia_chi']['ngo'])

# Kiểm tra xem tồn tại hay không dùng phương thức get

print(person.get('huhu', 'Không có thông tin'))

# Thêm phần tử mới vào dictionaries
# thêm mới thì person[''] = ''
# thêm vào mục đã có thì .append('')
person['test_create'] = 'Create'
print(person)
person['skill'].append('HTML')
print(person)

# Sửa đổi các mục trong từ điển giống thêm
person['test_create'] = 'Update'
print(person)

# Kiểm tra khóa trong từ điển:
print('test_create' in person)

# Xóa cặp khóa và giá trị khỏi từ điển dùng pop() hoặc popitem() hoặc del
# pop() : xóa mục có tên khóa được chỉ định
# popitem(): xóa mục cuối cùng
# del : xóa 1 mục có tên khóa được chỉ định
value = person.pop('test_create')
print(value)
print(person)
# value = person.popitem()
# print(value)
# print(person)
del person['dia_chi']
print(person)

# Thay đổi dictionaries thành danh sách các mục dùng items()
list_dict = person.items()
print(list_dict)

# Xóa từ điển dùng clear() hoặc del
# person.clear()
# print(person)
#
# del person
# print(person)

# Sao chép từ điển dùng copy()
copy_person = person.copy()
print(copy_person)

# Lấy khóa từ điển dưới dạng danh sách dùng keys()
person_key = person.keys()
print(person_key)

# Lấy giá trị từ điển dưới dạng danh sách dùng values
person_value = person.values()
print(person_value)

dog = {
    'name': 'Cun',
    'color': 'Yellow',
    'age': 3,
    'Giống': 'Chó ta'
}

students = {
    'name': 'Nguyễn Ngọc Tấn',
    'age': 20,
    'Giới tính': 'Nam',
    'Tình trạng hôn nhân': 'Chưa kết hôn',
    'skill': ['Python', 'Java', 'PHP', 'Javascript'],
    'country': 'Việt Nam',
    'city': 'Hà Nội'
}
# Lấy độ dài của từ điển sinh viên
print("Độ dài của từ điển sinh viên là:", len(students), 'từ điển')

# Lấy giá trị của skill and kiểm tra datatype , nó phải là one list
skill = students.get('skill')
print("Gía trị của skill là:", skill)
print(type(skill)) # dùng type để kiểm tra datatype

# Update giá trị của skill, bằng cách thêm one or two skill dùng append()
students['skill'].append('HTML') # thêm 1 skill dùng append()
print(students)
students['skill'].extend(['Laravel', 'Reactjs']) # Thêm 2 skill dùng extend()
print(students)

# Lấy các keys dictionary dưới dạng list dùng keys()
student_keys = students.keys() # keys()
print("Các key của students là:", student_keys)

# Lấy các values dictionary dưới dạng list dùng values()
student_value = students.values()
print('Values của student là:', student_value)

# Thay đổi dictionary thành list các bộ dữ liệu bằng phương thức items()
students_item = students.items()
print("Đã chuyển từ dictionary thành list dữ liệu:", students_item)

# Delete one các mục trong dictionary pop(), popitems(), del
students.pop('city') # xóa key theo chỉ định
print(students)
students.popitem() # xóa key cuối danh sách
print(students)

# Delete dictionary dùng del
del students















