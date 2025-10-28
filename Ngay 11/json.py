import json

# Python dict sang JSON
person = {
    "name": "Nguyễn Văn A",
    "age": 25,
    "city": "Hà Nội",
    "languages": ["Python", "JavaScript"]
}

# Chuyển sang JSON string
json_string = json.dumps(person, ensure_ascii=False, indent=2)
print(json_string)

# JSON string sang Python dict
json_data = '{"name": "Trần Thị B", "age": 30}'
python_dict = json.loads(json_data)
print(python_dict["name"])

# Lưu vào file
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=2)

# Đọc từ file
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(loaded_data)