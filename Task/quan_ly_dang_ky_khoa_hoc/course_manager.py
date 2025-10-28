import json
import re
from datetime import datetime
import pendulum

# danh sách khóa học mẫu (Dictionary)
COURSES = {
    "KH001": {"name": "Lập trình Python từ A-Z", "price": 1200000},
    "KH002": {"name": "Khoa học Dữ liệu cho Người mới bắt đầu", "price": 1500000},
    "KH003": {"name": "Thiết kế Web với ReactJS", "price": 1800000},
}

# tên file để lưu trữ dữ liệu
JSON_FILE = "registrations.json"

# Method kiểm tra dữ liệu đầu vào
def validate_input(name, email, course_code):
    # kiểm tra tên dùng try except
    try:
        if len(name) < 3:
            raise ValueError('Tên phải có ít nhất 3 kí tự')
    except TypeError:
        raise ValueError('Tên không được để trống')

    # kiểm tra định dạng -  dùng regEx
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, email):
        raise ValueError('Định dạng không hợp lệ')

    # kiểm tra định dạng khóa học dùng regex
    course_code_regex = r"^KH\d{3}$"
    if not re.match(course_code_regex, course_code):
        raise ValueError('Mã khóa học không đúng định dạng')

    # kiểm tra mã khóa học có tồn tại terong danh sacsg không
    if course_code not in COURSES:
        raise ValueError(f"Mã khóa học {course_code} không tồn tại")

    return True

# tính toán chi phí khóa học
def calculate_cost(course_code, quantity, promo_code):
    # lấy giá gốc từ danh sách khóa học
    base_price = COURSES[course_code]["price"]

    # tính tổng chi phí
    total_cost = base_price * quantity

    # áp dụng chi phí dựa trên mã ưu đãi
    if promo_code == 'SUMMER25':
        discount = 0.25
    elif promo_code == 'EARLYBIRD':
        discount = 0.15
    else:
        discount = 0.0

    final_cost = total_cost * ( 1 - discount )

    return round(final_cost, 2)


def save_registration(registration_data):
    """
    Lưu thông tin đăng ký vào tệp JSON.
    """
    try:
        # Cố gắng đọc dữ liệu hiện có từ tệp
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            all_registrations = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Nếu tệp không tồn tại hoặc rỗng/lỗi, tạo danh sách mới
        all_registrations = []

    # Thêm đăng ký mới vào danh sách
    all_registrations.append(registration_data)

    # Ghi lại toàn bộ danh sách vào tệp
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        # indent=4 giúp file JSON dễ đọc hơn
        json.dump(all_registrations, f, ensure_ascii=False, indent=4)


def load_registrations():
    print("\n--- DANH SÁCH HỌC VIÊN ĐÃ ĐĂNG KÝ ---")
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            registrations = json.load(f)
            if not registrations:
                print("Chưa có đăng ký nào.")
                return

            for reg in registrations:
                # Sử dụng String Formatting để in thông tin
                print(
                    f"Đăng ký của {reg['name']}: "
                    f"Khóa học {reg['course_code']}, "
                    f"Ngày {reg['registration_date']}, "
                    f"Chi phí {reg['cost']:,} VNĐ"
                )
    except FileNotFoundError:
        print("Chưa có dữ liệu đăng ký nào được tạo.")
    except json.JSONDecodeError:
        print("Lỗi: Tệp dữ liệu registrations.json bị hỏng.")


def main():
    """
    Hàm chính điều khiển luồng của chương trình.
    """
    while True:
        try:
            # 1. Yêu cầu người dùng nhập thông tin (User Input)
            print("\n--- HỆ THỐNG ĐĂNG KÝ KHÓA HỌC ---")
            name = input("Nhập họ tên của bạn: ")
            email = input("Nhập email: ")
            print("Các mã khóa học có sẵn:", list(COURSES.keys()))
            course_code = input("Nhập mã khóa học (ví dụ: KH001): ").upper()

            # 2. Kiểm tra dữ liệu đầu vào
            validate_input(name, email, course_code)

            # 3. Yêu cầu nhập thông tin chi phí
            quantity_str = input("Nhập số lượng khóa học muốn đăng ký: ")
            quantity = int(quantity_str)  # Có thể gây ValueError nếu không phải số
            if quantity <= 0:
                raise ValueError("Số lượng phải là một số nguyên dương.")

            promo_code = input("Nhập mã ưu đãi (nếu có, ví dụ: SUMMER25): ").upper()

            # 4. Tính toán chi phí
            cost = calculate_cost(course_code, quantity, promo_code)

            # 5. Lấy ngày đăng ký hiện tại (Sử dụng Pendulum)
            registration_date = pendulum.now('Asia/Ho_Chi_Minh').to_formatted_date_string()

            # 6. Tạo thông báo xác nhận (String Formatting)
            confirmation_message = (
                f"\n Chúc mừng {name} đã đăng ký khóa học {course_code} "
                f"vào ngày {registration_date}!"
            )
            print(confirmation_message)

            cost_message = (
                f"Tổng chi phí cho {quantity} khóa học là: {cost:,.0f} VNĐ."
            )
            print(cost_message)

            # 7. Chuẩn bị dữ liệu và lưu vào JSON
            registration_data = {
                "name": name,
                "email": email,
                "course_code": course_code,
                "registration_date": registration_date,
                "cost": cost
            }
            save_registration(registration_data)
            print(" Đã lưu thông tin đăng ký thành công!")

            # 8. Hiển thị tất cả các đăng ký
            load_registrations()

        except ValueError as ve:
            # Bắt lỗi từ validate_input hoặc lỗi chuyển đổi kiểu
            print(f"\n Lỗi đầu vào: {ve}. Vui lòng thử lại.")
        except Exception as e:
            # Bắt các lỗi không lường trước khác
            print(f"\n Đã xảy ra lỗi không mong muốn: {e}. Vui lòng thử lại.")

        # Hỏi người dùng có muốn tiếp tục không
        another = input("\nBạn có muốn thực hiện đăng ký khác không? (y/n): ").lower()
        if another != 'y':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break


# --- Chạy chương trình ---
if __name__ == "__main__":
    main()

