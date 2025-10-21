# 🐍 Python Data Structures – Cheatsheet

Tổng hợp các **cấu trúc dữ liệu cơ bản trong Python**: `list`, `dict`, `set`, `tuple`  
Cùng với các thao tác thường dùng như **thêm, sửa, xóa, duyệt, cập nhật**.

---

## 🧩 1️⃣ LIST – Danh sách (mutable)

### 🔹 Đặc điểm:
- Có **thứ tự**, cho phép **trùng lặp**.  
- **Có thể thay đổi (mutable)**.  
- Dùng để chứa nhiều giá trị khác nhau.

### 🔹 Cú pháp cơ bản:
```python
a = [1, 2, 3]
```

### 🔹 Thao tác thường dùng:
| Mục đích | Cú pháp | Ví dụ |
|-----------|----------|--------|
| Thêm 1 phần tử | `list.append(x)` | `a.append(10)` |
| Thêm nhiều phần tử | `list.extend([x, y])` | `a.extend([20, 30])` |
| Chèn vào vị trí | `list.insert(i, x)` | `a.insert(1, "Hello")` |
| Xóa theo giá trị | `list.remove(x)` | `a.remove(10)` |
| Xóa theo vị trí | `list.pop(i)` | `a.pop(2)` |
| Xóa toàn bộ | `list.clear()` | `a.clear()` |
| Cập nhật phần tử | `list[i] = new_value` | `a[0] = "New"` |
| Duyệt danh sách | `for item in a:` | — |

---

## 🧩 2️⃣ DICTIONARY – Từ điển (key–value)

### 🔹 Đặc điểm:
- Lưu dữ liệu theo cặp **key: value**.  
- Không có thứ tự cố định (Python 3.7+ thì có).  
- Key không trùng lặp.

### 🔹 Cú pháp cơ bản:
```python
info = {"name": "An", "age": 20}
```

### 🔹 Thao tác thường dùng:
| Mục đích | Cú pháp | Ví dụ |
|-----------|----------|--------|
| Thêm / Cập nhật | `dict[key] = value` | `info["age"] = 21` |
| Xóa theo key | `dict.pop(key)` | `info.pop("age")` |
| Xóa cặp cuối | `dict.popitem()` | — |
| Xóa toàn bộ | `dict.clear()` | — |
| Duyệt key | `for k in dict:` | — |
| Duyệt value | `for v in dict.values():` | — |
| Duyệt cả key-value | `for k,v in dict.items():` | — |

---

## 🧩 3️⃣ SET – Tập hợp (unique, unordered)

### 🔹 Đặc điểm:
- Không có thứ tự.  
- Không trùng lặp.  
- Dùng để lọc trùng, hoặc làm toán tập hợp.

### 🔹 Cú pháp cơ bản:
```python
s = {1, 2, 3}
```

### 🔹 Thao tác thường dùng:
| Mục đích | Cú pháp | Ví dụ |
|-----------|----------|--------|
| Thêm phần tử | `set.add(x)` | `s.add(5)` |
| Thêm nhiều phần tử | `set.update([...])` | `s.update([6,7])` |
| Xóa phần tử | `set.remove(x)` | `s.remove(5)` |
| Xóa an toàn (nếu có) | `set.discard(x)` | `s.discard(10)` |
| Xóa toàn bộ | `set.clear()` | — |
| Hợp tập hợp | `set1.union(set2)` | `s1 | s2` |
| Giao tập hợp | `set1.intersection(set2)` | `s1 & s2` |
| Hiệu | `set1.difference(set2)` | `s1 - s2` |

---

## 🧩 4️⃣ TUPLE – Bộ dữ liệu cố định (immutable)

### 🔹 Đặc điểm:
- Giống list nhưng **không thể thay đổi (immutable)**.  
- Dùng để lưu dữ liệu cố định, an toàn.

### 🔹 Cú pháp cơ bản:
```python
t = (1, 2, 3)
```

### 🔹 Thao tác thường dùng:
| Mục đích | Cú pháp | Ghi chú |
|-----------|----------|----------|
| Truy cập | `t[i]` | — |
| Cắt lát | `t[start:end]` | — |
| Duyệt | `for x in t:` | — |
| Không thể thêm/xóa/sửa | ❌ | immutable |

---

## ⚡ Tổng hợp nhanh:

| Loại | Có thứ tự | Thay đổi được | Cho phép trùng | Cấu trúc |
|------|------------|---------------|----------------|----------|
| **list** | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| **dict** | ✅ (Python 3.7+) | ✅ | 🚫 (key không trùng) | `{'a': 1, 'b': 2}` |
| **set** | 🚫 | ✅ | 🚫 | `{1, 2, 3}` |
| **tuple** | ✅ | 🚫 | ✅ | `(1, 2, 3)` |

---

📘 *Tác giả: ChatGPT – Python Quick Notes*
