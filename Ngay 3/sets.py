# SETS trong Python

#set là một taajp hợp duy nhất, không thứ tự
# nó giúp loại bỏ giữ liệu trùng lap , kiểm tra phần tử nhanh,

my_set = {'item1', 'item2', 'item3'} # Set sẽ được thể hiện qua {}
print(len(my_set))

# Kiểm tra 1 mục
print("Item 4 có ở trong my_set không??", 'item4' in my_set)

# Thêm mục dùng add() đối với set
my_set.add('item4')
print(my_set)

# Thêm nhiều mục bằng update
my_set.update(['item5', 'item6'])
print(my_set)

my_set.update(('item7', 'item8'))
print(my_set)

them = ('item9', 'item10', 'item11')
my_set.update(them)
print(my_set)

# xóa các mục khỏi tập hợp dùng remove()
#xóa bằng remove()
my_set.remove('item11')
print(my_set)
# xóa bằng pop() , xóa bằng pop() set sẽ xóa ngẫu nhiên 1 phần tử v có thể xem đc phần tử đã xóa
my_set.pop()
remove_item = my_set.pop()
print(remove_item)

# xóa tất cả phần tử thì dùng clear
my_set.clear()
print(my_set)

# xóa luôn tập hợp thì dùng del
# del my_set
# print(my_set)

# chuyển đổi danh sách thành tập hợp
lists = ['item1', 'item2', 'item3']
my_set = set(lists)
print(my_set)

# Khi dùng union thì sẽ trả về 1 set mới
set1 = {'item1', 'item2', 'item3'}
set2 = {'item4', 'item5', 'item6'}
full_set = set1.union(set2)
print(full_set)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))

# dùng update sẽ chèn vfo 1 tập hợp nhất định, nó tự loại bỏ những phần tử trungf lặp
fruits.update(vegetables)
print(fruits)

# GIAO ĐIỂM INTERSECTION
# giao điểm là các phần tử sẽ có mặt ở trong các set

sets1 = {'item1', 'item2', 'item3'}
sets2 = {'item4', 'item5', 'item6', 'item3'}
set_intersection = sets1.intersection(sets2)
print(set_intersection)

# Tập con và tập siêu
# Tập con (issubset): set A là tập con của set B nếu mọi phần tử của A đều có trong B
# Tập siêu (issuperset): set A là tập siêu của set B nếu mọi phần tử của B đều có trong A

set_a = {'item1', 'item2', 'item3', 'item4'}
set_b = {'item4', 'item5', 'item6', 'item3', 'item1', 'item2', 'item7'}
print("Set a là tập con của set b:", set_a.issubset(set_b))
print("Set b là tập con của set a?", set_b.issubset(set_a))

set_c = {'item1', 'item2', 'item3', 'item4', 'item5', 'item6'}
set_d = {'item1', 'item2', 'item3', 'item4'}
print("Set d là tập con của set c?", set_d.issubset(set_c))
print("Set c là tập siêu của set d?", set_c.issuperset(set_d))


# Sự khác biệt giữa 2 tập hợp
su_khac_biet1 = {'item1', 'item2', 'item3', 'item4'}
su_khac_biet2 = {'item4', 'item5', 'item6'}
print(su_khac_biet1.difference(su_khac_biet2))
print(su_khac_biet2.difference(su_khac_biet1))

# Tìm hiệu số đối xứng giữa 2 tập hợp dùng symmetric_difference
print(su_khac_biet1.symmetric_difference(su_khac_biet2))
print(su_khac_biet2.symmetric_difference(su_khac_biet1))

# Tham gia các tập hợp dùng isdisjoint để kiểm tra 2 tập hợp có bị chạm điểm không True False
even_number = {1, 2, 3, 4, 5, 6}
old_number = {7, 8, 9, 10, 11, 12}
print(even_number.isdisjoint(old_number))

# Bai tap
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Độ dài của it_companies là: ", len(it_companies))
it_companies.add('Twiter')
print(it_companies)
it_companies.update(['Dell', 'Hp', 'Asus'])
print(it_companies)
it_companies.remove('Twiter')
print(it_companies)
it_companies.discard('Test')
print(it_companies)

print("Sự khác biệt giữa remove và discard:\nremove khi xóa"
      " phần tử không có trong set sẽ báo lỗi\nCòn discard xóa"
      " phần tử ngoài set sẽ ko báo lỗi mà tự động bỏ qua ")

# Bài tập 2
C = A.union(B)
print("Tập mới C là:", C)
giao_diem = A.intersection(B)
print("Giao điểm giữa A và B là:", giao_diem)
print("A là tập con của B? Đúng hay sai?", A.issubset(B))
print("A và B có rời nhau không??", A.isdisjoint(B))

del A
del B

# Bài tập 3
age_set = set(age)
print(age_set)
print("Độ dài của danh sách là: ", len(age))
print("Độ dài của tập hợp là: ", len(age_set))

# 2. Giải thích sự khác biệt giữa các kiểu dữ liệu sau:
# Chuỗi (string), Danh sách (list), Bộ (tuple) và Tập hợp (set)

# 🔹 Chuỗi (string)
# - Là dãy ký tự nằm trong dấu nháy đơn hoặc nháy kép.
# - Có thể chứa chữ, số, ký tự đặc biệt.
# - Không thể thay đổi (immutable).
# - Có thể truy cập từng phần tử bằng chỉ số.
text = "Python"
print(text[0])   # P

# 🔹 Danh sách (list)
# - Là tập hợp có thứ tự (ordered) của nhiều phần tử.
# - Có thể chứa nhiều kiểu dữ liệu khác nhau.
# - Có thể thay đổi (mutable): thêm, xóa, sửa phần tử.
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)   # [1, 2, 3, 4, 5]

# 🔹 Bộ (tuple)
# - Giống list nhưng không thể thay đổi (immutable).
# - Có thứ tự (ordered).
# - Dùng khi dữ liệu cố định, không muốn thay đổi.
coordinates = (10, 20)
# coordinates[0] = 15  ❌ lỗi vì tuple không thể thay đổi

# 🔹 Tập hợp (set)
# - Là tập hợp **không có thứ tự** (unordered) và **không có phần tử trùng lặp**.
# - Không thể truy cập bằng chỉ số.
# - Dùng cho các phép toán tập hợp (union, intersection, difference...).
fruits = {"apple", "banana", "apple", "orange"}
print(fruits)  # {'banana', 'apple', 'orange'} (phần tử trùng bị loại bỏ)

