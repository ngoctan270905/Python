# Introduction

print(3 + 2) # addition ( phép cộng )
print(5 - 2) # subtraction ( phép trừ )
print(5 * 2) # multiplication ( phép nhân )
print(5 / 2) # division ( phép chia )
print(5 ** 2) # Exponential ( phép mũ )
print(5 % 2) # modulus ( lấy phần dư của phép chia )
print(5 // 2) # Floor division ( phép chia lấy phần nguyên )

# CHECKING DATA TYPES

print(type(10)) # int
print(type(3.14)) # float
print(type(1+3j)) # complex
print(type('Ngoctan')) # string
print(type(  # List
    [1,2,3]
))
print(type(     # Dictionary: kiểu mapping
    {
        "name": "tan",
        "age": 20,
        "city": "ha noi"
    }
))
print(type(    # Set
    {
        1,
        2,
        3
    }
))
print(type(    # Tuple
    (
        1,
        2,
        2
    )
))
print(type(3==3)) # Bool
print(type(3<=2)) # Bool


# 🧠 BÀI TẬP ÔN TẬP CƠ BẢN PYTHON

# 1️⃣ Tính toán cơ bản
# - Tạo 3 biến a, b, c là các số tùy ý.
# - Tính và in ra:
#   + Tổng, hiệu, tích, thương của a và b.
#   + a mũ b.
#   + Phần dư khi a chia b.
#   + Phần nguyên khi a chia b.

# 2️⃣ Kiểm tra kiểu dữ liệu
# - Tạo các biến sau và in ra kiểu dữ liệu (dùng type()):
#   + name = "Ngoc Tan"
#   + age = 20
#   + height = 1.75
#   + is_student = True
#   + skills = ["Python", "PHP", "Laravel"]
#   + info = {"name": "Tan", "city": "Hanoi"}
#   + nums = (1, 2, 3)
#   + primes = {2, 3, 5, 7}
#   + complex_num = 1 + 2j

# 3️⃣ So sánh logic (Boolean)
# - In ra kết quả của các biểu thức sau:
#   + 10 > 5
#   + 10 == 10
#   + 10 != 7
#   + 5 <= 2
#   + 7 % 2 == 1

# 4️⃣ Ứng dụng nhỏ
# - Cho trước biến `radius = 5`
# - Tính diện tích hình tròn (pi = 3.14)
# - In ra kết quả: "Diện tích hình tròn bán kính 5 là: ..."

# 👉 Gợi ý:
# - Dùng print(), type(), và các toán tử +, -, *, /, %, //, **, ==, !=, >=, <=
# - Nhớ format kết quả in ra cho dễ đọc (ví dụ: print("Tổng =", a + b))


# a = int(input("Mời bạn nhập số a:"))
# b = int(input("Mời bạn nhập số b:"))
# print("Tổng là:", a + b)
# print("Hiệu là:", a - b)
# print("Tích là:", a * b)
# print("Thương là:", a // b)
# print("a mũ b:", a ** b)
# print("a chia b:", a / b, "ta có số dư là: ", a % b)

# Bài 2
name = "Ngoc Tan"
print(name)
print(type(name))
age = 20
print(age)
print(type(age))
height = 1.70
print(height)
print(type(height))
is_student = True
print(is_student)
print(type(is_student))
skills = ([
    "python",
    "php",
    "javascript"
])
print(skills)
print(type(skills))
info = ({
    "ten" : "tan",
    "city" : "ha noi"
})
print(info)
print(type(info))
num = (1,2,3)
print(num)
print(type(num))
primes = (2,3,5,7)
print(primes)
print(type(primes))
complex_num = 1 + 2j
print(complex_num)
print(type(complex_num))

# Bài 3:
print(10 > 5)
print(10 == 10)
print(10 != 10)
print(5 <= 2)
print(7 % 2 == 1)

# Bài 4 Diện tích hình tròn là:
radius = 5
pi = 3.14
print("Diện tích của hình tròn là: ", pi * (radius ** 2))



