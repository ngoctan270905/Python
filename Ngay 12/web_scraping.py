# import requests
# from bs4 import BeautifulSoup
#
# # B1: Gửi request tới trang
# url = "https://vnexpress.net"
# response = requests.get(url)
#
# # B2: Phân tích HTML bằng BeautifulSoup
# soup = BeautifulSoup(response.text, "html.parser")
#
# # B3: Tìm các tiêu đề bài viết
# titles = soup.find_all("h3", class_="title-news")
#
# # B4: In ra kết quả
# for i, title in enumerate(titles[:10], 1):
#     print(f"{i}. {title.text.strip()}")

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books[:5]:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    link = book.h3.a["href"]
    print(f"{title} - {price} - {link}")

