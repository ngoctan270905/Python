#CASTING TRONG PYTHON
# Casting là chuyển 1 giá trị từ kiểu dữ liệu này sang kiểu dữ liệu khác
test = str(120)
print(type(test))

# 🧩 Bài tập Casting #1
# ---------------------------------------------------
# Viết chương trình Python yêu cầu người dùng nhập hai giá trị bất kỳ (dạng chuỗi).
# Sau đó:
#   - Ép hai giá trị đó sang số thực (float)
#   - Tính tổng, hiệu, tích, thương của hai số đó
#   - In kết quả ra màn hình với định dạng rõ ràng.
#
# 💡 Gợi ý:
#   - Dùng input() để lấy dữ liệu từ người dùng
#   - Dùng float() để ép kiểu
#   - Dùng f-string để in cho gọn: print(f"Tổng = {tong}")

a = input("Mời bạn nhập số a:")
b = input("Mời bạn nhập số b:")
a = float(a)
b = float(b)

print(a)
print(type(a))
print(b)
print(type(b))

print("Tổng của 2 số là:", a + b)
print("Hiệu của 2 số là:", a - b)
print("Tích của 2 số là:", a * b)
print("Thương của 2 số là:", a / b)

