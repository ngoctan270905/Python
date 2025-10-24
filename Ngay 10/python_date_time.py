import datetime
print(dir(datetime))

from datetime import datetime


# Nhận thông tin ngày và giờ
now = datetime.now()
print(f"Thời gian hiện tại là: {now}")

day = now.day # lấy ngày hiện tại
month = now.month # lấy tháng hiện tại
year = now.year # lấy năm hiện tại
hour = now.hour  # lấy giờ hiện tại
minute = now.minute # lấy phút hiện tại
second = now.second # lấy giây hiện tại
timestamp = now.timestamp()
print(timestamp)
print(f"Ngày hôm nay là: {day}-{month}-{year} {hour}:{minute}:{second} ")

# Định dạng đầu ra ngày bằng strftime
new_year = datetime(2020, 1, 1, 1,00,00)
print(new_year)

now = datetime.now()
t = now.strftime("%H:%M:%S")
print(t)

time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)

time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

#Chuyển đổi chuỗi thành thời gian bằng strptime

date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)


# Bài tập

thoi_gian_hien_tai = datetime.now()
print(f"Thời gian hiện tại là: {thoi_gian_hien_tai}")
dinh_dang_ngay = now.strftime("%m/%d/%Y, %H:%M:%S")
print('Định dạng ngày: ', dinh_dang_ngay)

date_strings = "5 December, 2019"
date_objects = datetime.strptime(date_strings, "%d %B, %Y")
print('Chuyển chuỗi thành time: ', date_objects)

now = datetime.now()

# thời gian năm mới

new_year = datetime(now.year + 1,1,1)
# khoảng thời gian còn lại
time_left = new_year - now
print('Thời gian còn lại tới năm 2026:', time_left)

