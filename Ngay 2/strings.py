#STRING

leet = 'hello'
print(leet)
print(len(leet)) # Dùng len để xem chuỗi này có bao nhiêu kí tự

greet_ting = "Hello, World!"
print(greet_ting)
print(len(greet_ting))

sentence = "Tôi sẽ chinh phục Python trong 30 ngày"
print(sentence)
print(len(sentence))

multi_string = """Tôi là sinh viên mới ra trường ,
Tôi muốn chinh phục Python trong 30 ngày"""
print(multi_string)

# Nối chuỗi với nhau
first_name = "Nguyễn"
last_name = "Tấn"
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name))
print(len(full_name))


# Thoát chuỗi

print("Tôi tên là Nguyễn Ngọc Tấn.\nCòn bạn?.")
print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')

print("Hello \\ World!")
print("Hello World! Xin chào \'thế giới\'")
print("Hello World! Xin chào \"thế giới\"")

# Định dạng chuỗi
# a = 5
# b = 10
# print(f"{a} + {b} = {a + b}")
# hihi = "Nguyễn Ngọc"
# huhu = "Tấn"
# print(f"{hihi} + {huhu} = {hihi + huhu}")
# c = 10
# d = 15
#
# print(f"{c} / {d} = {c/d:.2f}")

# a = "Hello World!"
# print(len(a))
# a,b,c,d,e,f,g,h,i,j,k,l = a
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)
# print(i)
# print(j)
# print(k)
# print(l)

language = "Python"

first_letter = language[0] #0 là bắt đầu
second_letter = language[1]
second_letters = language[-1] #-1 là cuối cùng
last_index = len(language) - 1
last_letters = language[last_index]
print(first_letter)
print(second_letter)
print(last_index)
print(last_letters)
print(second_letters)


ten = "Nguyễn Ngọc Tấn"
ten_3 = ten[0:6]
print(ten_3)
ten6 = ten[7:11]
print(ten6)
ten_het = ten[8:]
print(ten_het)
ten_cuoi = ten[-8:]
print(ten_cuoi)
test = ten[::-1]
print(test)

# Bỏ qua kí tự dùng step
languagekk = 'Python'
pto = languagekk[0:6:2]
print(pto)  # Pto

# Hàm sửa chuỗi: Capitalize, Swapcase, Replace
# Hàm kiểm tra chuỗi: Startswith
# Hàm lâấy thông tin là: count , len, index
# Hàm tách hoặc nối : split , join

## capitalize(): Chuyển ký tự đầu tiên của chuỗi thành chữ hoa
challenge = 'thirty days of python'
print(challenge.capitalize())  # 'Thirty days of python'


## count(): Đếm số lần xuất hiện của một chuỗi con trong chuỗi
challenge = 'thirty days of python'
print(challenge.count('y'))        # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th'))       # 2


## endswith(): Kiểm tra chuỗi có kết thúc bằng chuỗi con chỉ định không
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False


## expandtabs(): Thay thế ký tự tab bằng khoảng trắng, mặc định tab = 8 ký tự
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'


## find(): Trả về vị trí xuất hiện đầu tiên của chuỗi con
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0


## format(): Định dạng chuỗi cho đẹp hơn
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)  # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'Diện tích hình tròn bán kính {} là {}'.format(str(radius), str(area))
print(result)  # Diện tích hình tròn bán kính 10 là 314.0


## index(): Trả về vị trí của chuỗi con (giống find())
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0


## isalnum(): Kiểm tra chuỗi có phải **chỉ chứa chữ và số** không
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'thirty days of python'
print(challenge.isalnum())  # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum())  # False


## isalpha(): Kiểm tra chuỗi có **chỉ chứa chữ cái** không
challenge = 'thirty days of python'
print(challenge.isalpha())  # False
num = '123'
print(num.isalpha())        # False


## isdecimal(): Kiểm tra ký tự có phải **số thập phân nguyên** không
num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False


## isdigit(): Kiểm tra ký tự có phải số không
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())  # True


## isidentifier(): Kiểm tra chuỗi có phải tên biến hợp lệ không
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, vì bắt đầu bằng số
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


## islower(): Kiểm tra tất cả chữ cái có phải chữ thường không
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False


## isupper(): Kiểm tra tất cả chữ cái có phải chữ hoa không
challenge = 'thirty days of python'
print(challenge.isupper()) # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


## isnumeric(): Kiểm tra ký tự có phải số không
num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False


## join(): Nối chuỗi từ một list
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML#, CSS#, JavaScript#, React'


## strip(): Xóa khoảng trắng hoặc ký tự thừa ở đầu và cuối chuỗi
challenge = ' thirty days of python '
print(challenge.strip())  # 'thirty days of python'


## replace(): Thay thế chuỗi con
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'


## split(): Tách chuỗi thành list theo khoảng trắng
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']


## title(): Chuyển chuỗi thành dạng **viết hoa chữ cái đầu mỗi từ**
challenge = 'thirty days of python'
print(challenge.title()) # 'Thirty Days Of Python'


## swapcase(): Đảo ngược chữ hoa thành chữ thường và ngược lại
challenge = 'thirty days of python'
print(challenge.swapcase())   # 'THIRTY DAYS OF PYTHON'
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # 'tHIRTY dAYS oF pYTHON'


## startswith(): Kiểm tra chuỗi có bắt đầu bằng chuỗi con chỉ định không
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False







