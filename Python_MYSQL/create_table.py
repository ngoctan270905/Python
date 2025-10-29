import mysql.connector

# Kết nối với database cụ thể
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hocvien"
)

mycursor = mydb.cursor()

# Tạo bảng sinh viên
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS sinhvien (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hoten VARCHAR(255) NOT NULL,
        tuoi INT,
        lop VARCHAR(50),
        diem FLOAT
    )
""")

print("Bảng đã được tạo!")

# # Hiển thị các bảng
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)