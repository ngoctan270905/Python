# đọc file dùng read (r)
with open("dulieu.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

with open("danhsach.txt", "r", encoding="utf-8") as file:
    lines = file.readlines() # đọc tất cả dòn của file và trả về 1 ;list
    print(f"Số dòng: {len(lines)}")
    print("Danh sách:")
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.strip()}")

with open("students.csv", "r", encoding="utf-8") as file:
    header = file.readline()  # Đọc dòng
    print("DANH SÁCH SINH VIÊN:")
    print("-" * 40)

    for line in file:
        name, age, score = line.strip().split(",")
        print(f"Tên: {name:20} | Tuổi: {age} | Điểm: {score}")

with open("numbers.txt", "r", encoding="utf-8") as file:
    total = 0
    for line in file:
        numbers = line.strip().split()
        for num in numbers:
            total = total + int(num)
    print(f"Tổng các số: {total}")

from datetime import datetime

with open("diary.txt", "a", encoding="utf-8") as file:
    today = datetime.now().strftime("%d/%m/%Y")
    file.write(f"Ngày 3 ({today}): Học File Handling\n")



print("Đã thêm nội dung vào diary.txt")

# Đọc lại để xem
with open("diary.txt", "r", encoding="utf-8") as file:
    print(file.read())





