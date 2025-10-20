# Bài tập: Cấp độ 1

# 1. Lặp lại từ 0 đến 10 bằng vòng lặp for, làm tương tự bằng vòng lặp while.

# 2. Lặp lại từ 10 đến 0 bằng vòng lặp for, làm tương tự bằng vòng lặp while.

# 3. Viết một vòng lặp thực hiện bảy lệnh gọi tới print() để in ra hình tam giác:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######

# 4. Sử dụng vòng lặp lồng nhau để tạo ra nội dung sau:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

# 5. In bảng bình phương từ 0 đến 10:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

# 6. Lặp lại danh sách ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] bằng vòng lặp for và in ra các mục.

# 7. Sử dụng vòng lặp for để lặp từ 0 đến 100 và chỉ in ra các số chẵn.

# 8. Sử dụng vòng lặp for để lặp từ 0 đến 100 và chỉ in ra các số lẻ.


# Bài tập: Cấp độ 2

# 1. Sử dụng vòng lặp for để lặp từ 0 đến 100 và in tổng của tất cả các số.
# Expected: The sum of all numbers is 5050.

# 2. Sử dụng vòng lặp for để lặp từ 0 đến 100 và in ra tổng của tất cả các số chẵn và tổng của tất cả các số lẻ.
# Expected: The sum of all evens is 2550. And the sum of all odds is 2500.


# Bài tập: Cấp độ 3

# 1. Vào thư mục data và sử dụng tệp countries.py. Lặp qua các quốc gia và trích xuất tất cả các quốc gia có chứa từ "land".

# 2. Đây là danh sách trái cây ['chuối', 'cam', 'xoài', 'chanh']. Đảo ngược thứ tự bằng vòng lặp.

# 3. Vào thư mục data và sử dụng tệp countries_data.py.

# 4. Tổng số ngôn ngữ trong dữ liệu là bao nhiêu?

# 5. Tìm mười ngôn ngữ được nói nhiều nhất từ dữ liệu.

# 6. Tìm 10 quốc gia đông dân nhất thế giới.

# Bài 1
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
i = 0

for number in numbers:
    print(number)
while i < 11:
    print(i)
    i = i + 1

# Bài 2:
numbers_two = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
a = 10
for numbers_two in range(10, -1, -1):
    print(numbers_two)

while a >= 0:
    print(a)
    a = a - 1

# Bài 3:
for i in range(1, 8):
    print('#' * i)

# Bài 4:
cot = 8
hang = 8
for ii in range(cot):
    for jj in range(hang):
        print('#', end=' ')
    print()

# Bài 5:
for n in range(11):
    print(n, 'x', n, '=', n * n)

# Bài 6:
skills = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for skill in skills:
    print('Skill trong danh sách là: ', skill)

# Bài 7:
even_numbers = []
for a in range(101):
    if a % 2 == 0:
        even_numbers.append(a)
print('Các số chẵn từ 0 đến 100 là: ', even_numbers)

# Bài 8:
old_numbers = []
for b in range(101):
    if b % 2 != 0:
        old_numbers.append(b)
print('Các số lẻ từ 0 đến 100 là: ', old_numbers)

# Dạng 2:
# Bài 1:
total = 0
for c in range(101):
    total = total + c
print('Tổng của tất cả các số là: ', total)

# Bài 2:
total_chan = 0
total_le = 0
for d in range(101):
    if d % 2 == 0:
        total_chan = total_chan + d
    else:
        total_le = total_le + d
print('Tổng của các số chẵn là: ', total_chan)
print('Tổng của các số lẻ là: ', total_le)

# Bài 3:
luu_tru = []
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
for abc in countries:
    if 'land' in abc:
        luu_tru.append(abc)
print('Các quốc gia có chứa từ land là: ', luu_tru)













