# 🧠 Danh sách các loại lỗi (Exceptions) trong Python

Dưới đây là bảng tổng hợp các **lỗi (exceptions)** thường gặp trong Python, kèm mô tả ngắn gọn về ý nghĩa của từng loại lỗi.

| STT | Tên lỗi | Mô tả |
|-----|----------|-------|
| 1 | **SyntaxError** | Lỗi cú pháp – khi mã Python viết sai quy tắc ngôn ngữ. |
| 2 | **IndentationError** | Lỗi thụt đầu dòng sai. |
| 3 | **NameError** | Gọi biến chưa được định nghĩa. |
| 4 | **TypeError** | Thao tác giữa các kiểu dữ liệu không tương thích. |
| 5 | **ValueError** | Giá trị của biến không hợp lệ dù kiểu dữ liệu đúng. |
| 6 | **IndexError** | Truy cập phần tử ngoài phạm vi danh sách/tuple. |
| 7 | **KeyError** | Truy cập khóa không tồn tại trong dictionary. |
| 8 | **ZeroDivisionError** | Chia cho 0. |
| 9 | **AttributeError** | Gọi thuộc tính hoặc phương thức không tồn tại của đối tượng. |
| 10 | **ImportError** | Không thể import được module hoặc hàm. |
| 11 | **ModuleNotFoundError** | Module không tồn tại khi import. |
| 12 | **FileNotFoundError** | Không tìm thấy file khi mở. |
| 13 | **IOError** | Lỗi nhập/xuất tệp tin hoặc thiết bị. |
| 14 | **OSError** | Lỗi hệ điều hành (file, thư mục, quyền truy cập, v.v.). |
| 15 | **RuntimeError** | Lỗi xảy ra trong quá trình chạy nhưng không thuộc loại cụ thể nào khác. |
| 16 | **AssertionError** | Biểu thức `assert` bị sai. |
| 17 | **RecursionError** | Gọi đệ quy quá sâu, vượt giới hạn hệ thống. |
| 18 | **MemoryError** | Hết bộ nhớ RAM khi chạy chương trình. |
| 19 | **EOFError** | Không nhận được dữ liệu đầu vào (input) như mong đợi. |
| 20 | **KeyboardInterrupt** | Người dùng dừng chương trình bằng Ctrl + C. |
| 21 | **PermissionError** | Không có quyền truy cập vào file hoặc thư mục. |
| 22 | **StopIteration** | Đối tượng iterator không còn phần tử để lặp. |
| 23 | **FloatingPointError** | Lỗi tính toán số thực (floating point). |
| 24 | **OverflowError** | Kết quả số học vượt giới hạn biểu diễn của Python. |
| 25 | **NotImplementedError** | Phương thức chưa được cài đặt trong lớp con. |

---

> 📘 **Ghi nhớ:** Python có hàng chục loại lỗi khác nhau, nhưng chỉ cần nắm chắc khoảng 10–15 loại phổ biến là đủ cho hầu hết các tình huống lập trình thực tế.
