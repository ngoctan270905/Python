import re

text = "Số điện thoại của tôi là 0123456789 và email là user@example.com"

# Tìm kiếm
result = re.search(r"\d{10}", text)  # Tìm 10 chữ số
if result:
    print(f"Tìm thấy: {result.group()}")

# Tìm tất cả
emails = re.findall(r"\w+@\w+\.\w+", text)
print(f"Email: {emails}")

# Thay thế
new_text = re.sub(r"\d", "*", text)  # Thay số thành *
print(new_text)

# Tách chuỗi
words = re.split(r"\s+", "Python  is   awesome")  # Tách theo khoảng trắng
print(words)

# Kiểm tra pattern
phone = "0987654321"
if re.match(r"^0\d{9}$", phone):
    print("Số điện thoại hợp lệ")