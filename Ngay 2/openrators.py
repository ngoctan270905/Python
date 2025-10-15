# Biến và kiểu dữ liệu
age = 20
height = 1.71
complex_nums = 2 + 3j
print(age)
print(height)
print(complex_nums)

# Nhập liệu và tính toán cơ bản
# Tinh dien tich tam giac
chieu_dai_day = float(input("Mời bạn nhập chiều dài đáy: "))
chieu_cao = float(input("Mời bạn nhập chiều cao:"))
print(chieu_dai_day)
print(chieu_cao)

dien_tich = 1/2 * chieu_dai_day * chieu_cao
print("Diện tích của tam giác là:", dien_tich)
#
#
# # Tính chu vi của tam giác
canh_a = float(input("Mời bạn nhập cạnh a: "))
canh_b = float(input("Mời bạn nhập cạnh b: "))
canh_c = float(input("Mời bạn nhập cạnh c: "))

chu_vi = canh_a + canh_b + canh_c
print("Chu vi của tam giác là:", chu_vi)
print("Chu vi là:", canh_a + canh_b + canh_c)

# Tính diện tích và chu vi hình chữ nhật
chieu_dai = float(input("Mời bạn nhập chiều dài: "))
chieu_rong = float(input("Mời bạn nhập chiều rộng: "))
dien_tich_hinhchunhat = chieu_dai * chieu_rong
chu_vi_hinhchunhat = (chieu_dai + chieu_rong)*2
print("Diện tích hình chữ nhật là: ", dien_tich_hinhchunhat)
print("Chu vi hình chữ nhật là: ", chu_vi_hinhchunhat)

# Tính diện tích và chu vi của tam giác
pi = 3.14
ban_kinh = float(input("Mời bạn nhập bán kính của hình tròn: "))
dien_tich_hinhtron = pi * ban_kinh * ban_kinh
chu_vi_hinhtron = int(2 * pi * ban_kinh)

print("Diện tích hình tròn là: ", dien_tich_hinhtron)
print("Chu vi hình tròn là: ", chu_vi_hinhtron)

# Tính giá trị y của phương trình: y = x² + 6x + 9.
# Thử nhiều giá trị của x và xác định giá trị x nào khiến y = 0.

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True










