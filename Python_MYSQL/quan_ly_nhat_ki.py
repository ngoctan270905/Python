import mysql.connector
from mysql.connector import errorcode

# --- CẤU HÌNH KẾT NỐI DATABASE ---
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '' # Thay đổi mật khẩu của bạn ở đây
}
DB_NAME = 'project_progress'

def setup_database(cursor):
    """Tạo cơ sở dữ liệu và các bảng cần thiết."""
    try:
        # 1. Tạo cơ sở dữ liệu nếu chưa tồn tại
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
        cursor.execute(f"USE {DB_NAME}")
        print(f"Cơ sở dữ liệu '{DB_NAME}' đã sẵn sàng.")

        # 2. Tạo bảng 'members' nếu chưa tồn tại
        create_members_table_query = """
        CREATE TABLE IF NOT EXISTS members (
            member_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            role VARCHAR(50)
        ) ENGINE=InnoDB;
        """
        cursor.execute(create_members_table_query)
        print("Bảng 'members' đã được tạo hoặc đã tồn tại.")

        # 3. Tạo bảng 'weekly_progress' nếu chưa tồn tại
        create_progress_table_query = """
        CREATE TABLE IF NOT EXISTS weekly_progress (
            progress_id INT AUTO_INCREMENT PRIMARY KEY,
            member_id INT,
            week_number INT,
            hours_worked FLOAT,
            tasks_completed INT,
            notes TEXT,
            FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """
        cursor.execute(create_progress_table_query)
        print("Bảng 'weekly_progress' đã được tạo hoặc đã tồn tại.")

    except mysql.connector.Error as err:
        print(f"Lỗi khi thiết lập database: {err}")
        exit(1)

def add_data(connection, cursor):
    """Thêm dữ liệu mẫu vào các bảng."""
    print("\n--- Thêm dữ liệu mẫu ---")

    # Dữ liệu mẫu cho bảng 'members'
    members_data = [
        ("Phạm Nhật An", "Developer"),
        ("Trần Thị Bình", "Designer"),
        ("Lê Văn Cường", "Project Manager"),
        ("Nguyễn Thị Dung", "Tester"),
        ("Hoàng Văn Em", "Developer")
    ]

    # Dữ liệu mẫu cho bảng 'weekly_progress'
    progress_data = [
        # Tuần 1
        (1, 1, 40.5, 5, "Thiết lập môi trường và cấu trúc dự án."),
        (2, 1, 38.0, 3, "Thiết kế giao diện trang chủ."),
        (3, 1, 42.0, 7, "Lập kế hoạch và phân chia công việc."),
        (4, 1, 35.0, 10, "Viết kịch bản kiểm thử cho module đăng nhập."),
        (5, 1, 41.0, 6, "Phát triển API đăng nhập."),
        # Tuần 2
        (1, 2, 42.0, 8, "Hoàn thành API sản phẩm."),
        (2, 2, 39.5, 4, "Tạo wireframe cho trang sản phẩm."),
        (3, 2, 40.0, 5, "Theo dõi tiến độ và báo cáo."),
        (4, 2, 36.5, 12, "Kiểm thử API sản phẩm."),
        (5, 2, 44.0, 9, "Tối ưu hóa query database.")
    ]

    try:
        # Thêm thành viên
        insert_members_query = "INSERT INTO members (name, role) VALUES (%s, %s)"
        cursor.executemany(insert_members_query, members_data)

        # Thêm tiến độ
        insert_progress_query = """
        INSERT INTO weekly_progress (member_id, week_number, hours_worked, tasks_completed, notes) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.executemany(insert_progress_query, progress_data)

        connection.commit() # Lưu các thay đổi vào database
        print("Đã thêm 5 thành viên và 10 bản ghi tiến độ thành công.")
    except mysql.connector.Error as err:
        print(f"Lỗi khi thêm dữ liệu: {err}")
        connection.rollback() # Hoàn tác nếu có lỗi

def query_progress(cursor, week_num):
    """Truy vấn và hiển thị tiến độ của một tuần cụ thể."""
    print(f"\n--- Báo cáo tiến độ Tuần {week_num} (Top 5) ---")

    query = """
    SELECT m.name, wp.hours_worked, wp.tasks_completed, wp.notes
    FROM weekly_progress AS wp
    JOIN members AS m ON wp.member_id = m.member_id
    WHERE wp.week_number = %s
    ORDER BY wp.tasks_completed DESC
    LIMIT 5;
    """

    try:
        cursor.execute(query, (week_num,))
        results = cursor.fetchall()

        if not results:
            print(f"Không tìm thấy dữ liệu cho tuần {week_num}.")
            return

        for name, hours, tasks, notes in results:
            print(f"\t- {name}: {hours} giờ, {tasks} nhiệm vụ, Ghi chú: {notes}")

    except mysql.connector.Error as err:
        print(f"Lỗi khi truy vấn dữ liệu: {err}")

def update_progress(connection, cursor, progress_id, new_hours, new_notes):
    """Cập nhật một bản ghi tiến độ cụ thể."""
    print(f"\n--- Cập nhật tiến độ (ID: {progress_id}) ---")

    update_query = """
    UPDATE weekly_progress
    SET hours_worked = %s, notes = %s
    WHERE progress_id = %s;
    """

    try:
        cursor.execute(update_query, (new_hours, new_notes, progress_id))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"Đã cập nhật thành công bản ghi có ID = {progress_id}.")
        else:
            print(f"Không tìm thấy bản ghi nào có ID = {progress_id} để cập nhật.")
    except mysql.connector.Error as err:
        print(f"Lỗi khi cập nhật dữ liệu: {err}")
        connection.rollback()

def delete_progress(connection, cursor, week_num):
    """Xóa tất cả các bản ghi tiến độ của một tuần cụ thể."""
    print(f"\n--- Xóa dữ liệu tiến độ của Tuần {week_num} ---")

    delete_query = "DELETE FROM weekly_progress WHERE week_number = %s;"

    try:
        cursor.execute(delete_query, (week_num,))
        connection.commit()
        print(f"Đã xóa {cursor.rowcount} bản ghi của tuần {week_num}.")
    except mysql.connector.Error as err:
        print(f"Lỗi khi xóa dữ liệu: {err}")
        connection.rollback()

def generate_summary(cursor):
    """Tạo báo cáo tổng kết cho từng thành viên."""
    print("\n--- Báo cáo tổng kết toàn bộ dự án ---")

    summary_query = """
    SELECT m.name, SUM(wp.hours_worked) as total_hours, SUM(wp.tasks_completed) as total_tasks
    FROM members AS m
    JOIN weekly_progress AS wp ON m.member_id = wp.member_id
    GROUP BY m.member_id, m.name
    ORDER BY total_hours DESC;
    """

    try:
        cursor.execute(summary_query)
        results = cursor.fetchall()

        if not results:
            print("Chưa có dữ liệu để tổng kết.")
            return

        for name, total_hours, total_tasks in results:
            print(f"\t- {name}: Tổng {total_hours:.2f} giờ, {total_tasks} nhiệm vụ")

    except mysql.connector.Error as err:
        print(f"Lỗi khi tạo báo cáo: {err}")

def cleanup_database(connection, cursor):
    """Xóa bảng weekly_progress để dọn dẹp."""
    print("\n--- Dọn dẹp dữ liệu ---")

    try:
        cursor.execute(f"USE {DB_NAME}")
        cursor.execute("DROP TABLE IF EXISTS weekly_progress;")
        connection.commit()
        print("Đã xóa bảng 'weekly_progress' thành công.")
    except mysql.connector.Error as err:
        print(f"Lỗi khi dọn dẹp: {err}")

def main():
    """Hàm chính điều khiển luồng của chương trình."""
    connection = None
    try:
        # Kết nối đến MySQL server
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # 1. Thiết lập cơ sở dữ liệu và bảng
        setup_database(cursor)

        # 2. Thêm dữ liệu mẫu
        add_data(connection, cursor)

        # 3. Truy vấn tiến độ tuần 1
        query_progress(cursor, 1)

        # 4. Cập nhật một bản ghi (ví dụ: progress_id = 1)
        update_progress(connection, cursor, 1, 45.0, "Hoàn thành sớm và tối ưu hóa code.")

        # Kiểm tra lại sau khi cập nhật
        query_progress(cursor, 1)

        # 5. Tạo báo cáo tổng kết trước khi xóa
        generate_summary(cursor)

        # 6. Xóa dữ liệu của tuần 2
        delete_progress(connection, cursor, 2)

        # Tạo lại báo cáo để thấy sự thay đổi
        generate_summary(cursor)

        # 7. Dọn dẹp (xóa bảng) nếu cần
        # Bỏ comment dòng dưới nếu bạn muốn xóa bảng weekly_progress sau khi chạy
        # cleanup_database(connection, cursor)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Lỗi: Sai username hoặc password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Lỗi: Cơ sở dữ liệu không tồn tại.")
        else:
            print(f"Lỗi kết nối MySQL: {err}")
    finally:
        # Đảm bảo kết nối luôn được đóng
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("\nĐã đóng kết nối MySQL.")

# Chạy chương trình
if __name__ == "__main__":
    main()