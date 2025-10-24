# try:
#     # Khối code có khả năng gây lỗi
#     x = int(input("Nhập số: "))
#     print(10 / x)
# except ZeroDivisionError:
#     # Xử lý khi chia cho 0
#     print("Không thể chia cho 0!")
# except ValueError:
#     # Xử lý khi nhập không phải số
#     print("Vui lòng nhập số hợp lệ!")
# except Exception as e:
#     # Bắt tất cả các lỗi khác
#     print("Có lỗi xảy ra:", e)
# else:
#     # Thực hiện nếu không có lỗi
#     print("Thao tác thành công!")
# finally:
#     # Luôn chạy, dù có lỗi hay không
#     print("Kết thúc chương trình.")


# ĐÓNG GÓI VÀ GIẢI NÉN ĐỐI SỐ TRONG PYTHON
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

# GIẢI NÉN DANH SÁCH
lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))

numbers = range(2, 7)
print(list(numbers))

test = [2, 9]
ket_qua = range(*test)
print(list(ket_qua))

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct))

# Danh sách đóng gói




