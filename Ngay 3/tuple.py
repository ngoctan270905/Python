# TUPLE TRONG PYTHON

# 🧩 Bài tập: Cấp độ 1

# 1. Tạo một tuple trống=

# 2. Tạo một tuple chứa tên của các chị/em gái và anh/em trai (có thể tưởng tượng cũng được)

# 3. Nối hai tuple (brothers và sisters) lại với nhau và gán vào biến siblings

# 4. Cho biết bạn có bao nhiêu anh chị em

# 5. Chỉnh sửa tuple siblings để thêm tên cha và mẹ, rồi gán kết quả vào biến family_members

tuples = ()
print(tuples)

brothers = ('Tấn', 'Tú')
sisters = ('Linh', 'Quỳnh')
siblings = brothers + sisters
print(siblings)
print("Có tổng", len(siblings), "anh chị em")
siblings = list(siblings)
print(siblings)
siblings.append('Tuấn')
siblings.append('Hưng')
print(siblings)
family_members = siblings.copy()
print(family_members)

# 🧩 Bài tập: Cấp độ 2

# 1. Giải nén (unpack) các phần tử anh chị em và cha mẹ từ tuple family_members

# 2. Tạo 3 tuple: fruits (trái cây), vegetables (rau củ) và animal_products (sản phẩm từ động vật).
#    Sau đó nối 3 tuple này lại với nhau và gán vào biến food_stuff_tp.

# 3. Chuyển tuple food_stuff_tp thành danh sách (list) và gán vào biến food_stuff_lt.

# 4. Cắt (slice) phần tử hoặc các phần tử ở giữa từ tuple hoặc list food_stuff_tp / food_stuff_lt.

# 5. Cắt 3 phần tử đầu tiên và 3 phần tử cuối cùng từ danh sách food_stuff_lt.

# 6. Xóa hoàn toàn tuple food_stuff_tp.

# 7. Kiểm tra xem một phần tử có tồn tại trong tuple hay không:
#    - Kiểm tra xem 'Estonia' có phải là quốc gia Bắc Âu (nordic country) không.
#    - Kiểm tra xem 'Iceland' có phải là quốc gia Bắc Âu không.

# Gợi ý dữ liệu:
# nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

* siblings, father, mother = family_members
print("Anh chị em gồm:", siblings)
print("Cha mẹ gồm:", [father, mother])

fruits = ('Cam','Quýt','Chuối','Dưa hấu', 'Táo')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter', 'yoghurt')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)
food_stuff_lt = food_stuff_tp.copy()
print(food_stuff_lt)

middle_stuff = len(food_stuff_lt) // 2
print(middle_stuff)
middle_stuff_read = food_stuff_lt[middle_stuff]
print("Phần tử đã cắt ở giữa là: ", middle_stuff_read)
print(food_stuff_lt)
three_stuff_dau = food_stuff_lt[:3]
print(three_stuff_dau)
three_stuff_cuoi = food_stuff_lt[-3:]
print(three_stuff_cuoi)

food_stuff_lt.clear()
print(food_stuff_lt)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)
kiem_tra = 'Estonia' in nordic_countries
print(kiem_tra)
kiem_tra = 'Iceland' in nordic_countries
print(kiem_tra)






