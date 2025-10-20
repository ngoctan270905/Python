# Loops trong python


# Vòng lặp while
count = 0
while count < 5:  # Lặp lại khi count nhỏ hơn 5 khi count >= 5 thì điều kiện false và vòng lặp dừng
    print(count)
    count = count + 1
# Break and continue : Break: Dừng vòng lặp hoàn toàn. , Continue: Bỏ qua vòng hiện tại, chuyển sang vòng tiếp theo.
    if count == 3: # nếu count = 3 thì break sẽ dừng vòng lặp ( bỏ qua cả else )
        break
else:
    print('Gía trị khiến vòng lặp dừng: ', count)

count2 = 0
while count2 < 5:
    if count2 == 3:
        count2 = count2 + 1
        continue # continue sẽ dừng toàn bộ điều kiện này và tiếp tục vòng lặp mới
    print(count2)
    count2 = count2 + 1

# Vòng lặp for
# lặp với danh sách
numbers = [1,2,3,4,5]
for number in numbers: # lặp qua từng danh sách và gán giá trị vào number
    print(number)

# lặp với chuỗi
languages = 'Python'
for language in languages: # lặp qua từng phần tử trong chuỗi và gán giá trị vào language
    print(language)

# cách 2 : lặp qua index
languages2 = 'Python'
for i in range(len(languages2)): # lặp qua từng chỉ số trong ds, len lấy độ dài danh sách, range sẽ tạo dãy số range()
    print(languages2[i]) # hiển thị phần tử ở thứ [i] trong danh sách

# lặp với tuple
languages3 = (1,2,3,4,5)
for language_tuple in languages3:
    print(language_tuple)

# vòng lặp for với từ điển
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person: # chỉ lay key
    print('Các key có trong dictionary là: ', key)
# Lấy cả key và value
for key, value in person.items(): #lặp từng phần tử trong person để lấy key và value
    print(key, ':', value)

# Vòng lặp for với set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

for company in it_companies:
    print('Từng phần tử của it_conpanies là:', company)


# BREAK VÀ CONTINUE
# Dùng break khi muốn dừng vòng lặp trước khi hoàn tất
numbers = (0,1,2,3,4,5)
for number in numbers: # lặp qua từng phần tử
    print(number)
    if number == 4: # nếu = 4 thì dừng vòng lặp
        break

# Dùng continue khi muốn dừng vòng lặp hiện tại và sang vòng lặp mới
number_fors = (1,2,3,4,5)
for number_for in number_fors:
    print(number_for)
    if number_for == 4:
        continue
    if number_for != 5:
        print('Vòng lặp tiếp theo là:', number_for + 1)
    else:
        print('vòng lặp đã dừng')

# Hàm phạm vi : dùng range() để tạo các dãy số
for number_for in range(5):
    print(number_for)

# Vòng lặp lồng nhau
persons = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for k in person:
    if k == 'skills': # nếu k = 'skills' thì thực hiện vòng for dưới
        for skill in person['skills']: # lặp từng phần tử trong value của key: skills
            print('Value của skills là:', skill)

#
number_fors2 = (1,2,3,4,5)
for number_fors2 in range(5):
    print(number_fors2)
else:
    print('Vòng lặp ket thuc')



