import os
import glob

from Task.quan_ly_su_kien import bao_cao_thong_ke


# Tạo nhật kí tuần
def create_weekly_log():
    print('Tạo nhật kí tuần')
    try:
        week_number = int(input('Nhập số tuần: '))
        hours = float(input('Nhập số giờ làm việc: '))
        tasks = int(input('Nhập số nhiệm vụ hoàn thành: '))
        notes = input('Nhập ghi chú: ')

        # tạo file name theo tuần
        file_name = f"week_{week_number}.txt"

        # Ghi thông tin vào file
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(f"Tuần: {week_number}\n")
            file.write(f"Số giờ làm việc: {hours}\n")
            file.write(f"Số nhiệm vụ hoàn thành: {tasks}\n")
            file.write(f"Ghi chú: {notes}\n")

        print(f"Đã tạo nhật kí tuần {week_number} thành công.")

    except ValueError:
        print('Vui lòng nhập định dạng hợp lệ.')
    except Exception as e:
        print(f"Lỗi không xác định. {e}")

# create_weekly_log()

# xem nhật kí tuần
def read_weekly_log():
    print('Đọc nhật kí tuần')
    try:
        week_number = int(input('Nhập số tuần cần đọc: '))
        file_name = f"week_{week_number}.txt"

        # kiểm tra xem file tồn tại k
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as file:
                content = file.read()
                print(content)
        else:
            print(f"Nhật kí tuần {week_number} không tồn tại")

    except ValueError:
        print('Vui lòng nhập định dạng hợp lệ')
    except Exception as e:
        print(f"Lỗi không xác định. {e}")

# read_weekly_log()

# update nhật kí tuần
def update_weekly_log():
    print('Cập nhật nhật kí tuần')
    try:
        week_number = int(input('Nhập số tuần cần sửa: '))
        file_name = f"week_{week_number}.txt"

        # Nhập thông tin mới
        hours = float(input('Nhập số giờ làm việc mới: '))
        tasks = int(input('Nhập số nhiệm vụ hoàn thành mới: '))
        notes = input('Nhập ghi chú mới: ')

        # ghi đè nội dung mới, chế độ "w sẽ xóa nội dung cũ
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(f"Tuần: {week_number}\n")
            file.write(f"Số giờ làm việc: {hours}\n")
            file.write(f"Nhiệm vụ hoàn thành: {tasks}\n")
            file.write(f"Ghi chú: {notes}\n")

        print(f"Đã cập nhật nhật kí tuần {week_number} thành công.")
    except ValueError:
        print('Vui lòng nhập đúng định dạng.')
    except Exception as e:
        print(f"Lỗi không xác định. {e}")

def delete_weekly_log():
    print('Xóa nhật kí tuần')
    try:
        week_number = int(input('Nhập số tuần cần xóa: '))
        file_name = f"week_{week_number}.txt"

        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"Xóa nhật kí tuần {week_number} thành công")
        else:
            print('Không tìm thấy nhật kí tuần')
    except ValueError:
        print('Vui lòng nhập đúng định dạng')
    except Exception as e:
        print(f"Lỗi không xác định. {e}")


def main():
    print("CHƯƠNG TRÌNH QUẢN LÝ NHẬT KÝ TUẦN LÀM VIỆC")


    while True:
        print("\n--- MENU ---")
        print("1. Tạo nhật ký tuần mới")
        print("2. Đọc nhật ký tuần")
        print("3. Cập nhật nhật ký tuần")
        print("4. Xóa nhật ký tuần")
        print("5. Tạo báo cáo tổng kết")
        print("6. Thoát")

        try:
            choice = input("\nNhập lựa chọn (1-6): ").strip()

            if choice == "1":
                create_weekly_log()
            elif choice == "2":
                read_weekly_log()
            elif choice == "3":
                update_weekly_log()
            elif choice == "4":
                delete_weekly_log()
            elif choice == "5":
                bao_cao_thong_ke()
            elif choice == "6":
                print("\nTạm biệt! Hẹn gặp lại")
                break
            else:
                print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1-6.")

        except KeyboardInterrupt:
            print("\n\nChương trình bị ngắt!")
            break
        except Exception as e:
            print(f"Lỗi không xác định: {e}")


# Chạy chương trình
if __name__ == "__main__":
    main()