import mysql.connector

# Kết nối tới MySQL Server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hocvien"
)

mycursor = mydb.cursor(buffered=True)

# Tạo database
mycursor.execute("CREATE DATABASE IF NOT EXISTS hocvien")
print("Database đã được tạo!")

# # Hiển thị danh sách databases
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# Insert một record
sql = "INSERT INTO sinhvien (hoten, tuoi, lop, diem) VALUES (%s, %s, %s, %s)"
val = ("Nguyễn Văn A", 20, "CNTT01", 8.5)

mycursor.execute(sql, val)
mydb.commit()  # Quan trọng: phải commit!

print(f"Đã thêm {mycursor.rowcount} record, ID:", mycursor.lastrowid)

# Insert nhiều records
sql = "INSERT INTO sinhvien (hoten, tuoi, lop, diem) VALUES (%s, %s, %s, %s)"
val = [
    ("Trần Thị B", 21, "CNTT01", 7.5),
    ("Lê Văn C", 19, "CNTT02", 9.0),
    ("Phạm Thị D", 22, "CNTT01", 6.5),
    ("Hoàng Văn E", 20, "CNTT02", 8.0)
]

mycursor.executemany(sql, val)
mydb.commit()

print(f"Đã thêm {mycursor.rowcount} records")

# Select tất cả
mycursor.execute("SELECT * FROM sinhvien")
results = mycursor.fetchall()

for row in results:
    print(row)

print("\n--- Chỉ lấy một số cột ---")
mycursor.execute("SELECT hoten, diem FROM sinhvien")
for (hoten, diem) in mycursor:
    print(f"{hoten}: {diem} điểm")

# fetchone() - lấy 1 record
mycursor.execute("SELECT * FROM sinhvien")
result = mycursor.fetchone()
print("\nRecord đầu tiên:", result)

# Where đơn giản
sql = "SELECT * FROM sinhvien WHERE lop = %s"
val = ("CNTT01",)

mycursor.execute(sql, val)
for row in mycursor.fetchall():
    print(row)

# Where với nhiều điều kiện
sql = "SELECT * FROM sinhvien WHERE diem > %s AND tuoi >= %s"
val = (7.0, 20)

mycursor.execute(sql, val)
for row in mycursor.fetchall():
    print(row)

# Sử dụng LIKE
sql = "SELECT * FROM sinhvien WHERE hoten LIKE %s"
val = ("%Văn%",)  # Tìm tên có chữ "Văn"

mycursor.execute(sql, val)
for row in mycursor.fetchall():
    print(row)

# Sắp xếp tăng dần (ASC)
mycursor.execute("SELECT * FROM sinhvien ORDER BY diem ASC")
print("Sắp xếp theo điểm tăng dần:")
for row in mycursor.fetchall():
    print(row)

# Sắp xếp giảm dần (DESC)
mycursor.execute("SELECT * FROM sinhvien ORDER BY diem DESC")
print("\nSắp xếp theo điểm giảm dần:")
for row in mycursor.fetchall():
    print(row)

# Sắp xếp nhiều cột
mycursor.execute("SELECT * FROM sinhvien ORDER BY lop, diem DESC")
print("\nSắp xếp theo lớp, sau đó điểm giảm dần:")
for row in mycursor.fetchall():
    print(row)