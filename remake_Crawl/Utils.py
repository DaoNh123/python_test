import pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup
from book2 import Book
from urllib.parse import urljoin
import os

rootUrl = 'https://books.toscrape.com'
def getSoupHTML(url):
    response = requests.get(url)
    response.raise_for_status()  # Tự động raise HTTPError nếu lỗi 404, 500, v.v.

    print(f'✅ Successfully fetched the page {url}')
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

# def getBooksInfo(url):
#     soupHTML = getSoupHTML(url)
#     articles = soupHTML.find_all('article')
#     books = []
#     for article in articles:
#         title = article.h3.a.attrs['title']
#         price_tag = article.find('p', class_='price_color')
#         available = True if article.find('p', attrs={'class': ['instock', 'availability']}) else False
#         books.append({
#             'title': title,
#             'price': float(price_tag.text[1:]),
#             'currency': price_tag.text[:1],
#             'available': available,
#             'categories':'',
#         })
#
#     return books

# def get_data_from_main_page(fileCsvName):
#     rootUrl = 'https://books.toscrape.com'
#     i = 1
#     books = []
#     while True:
#         try:
#             url = f'{rootUrl}/catalogue/page-{i}.html'
#             print(url)
#             soupHTML = getSoupHTML(url)
#             found_books = getBooksInfo(url)
#
#             books += found_books
#             print(f"{i}: ✅ Found {len(books)} books")
#             i += 1
#         except requests.exceptions.HTTPError as e:
#             print(f"⚠️ HTTP error occurred: {e}")
#             break
#         except requests.exceptions.RequestException as e:
#             print(f"⚠️ Request failed: {e}")
#             break
#
#         if (i > 5): break  # break for fast test
#
#     print(f"len(books): {len(books)}")
#     save_to_csv(books, fileCsvName)
#     print("___ Have got all data from main page ___")
def save_to_csv(books, filename):
    books_df = pandas.DataFrame(books)
    books_df.to_csv(filename, index=False, encoding='utf-8', float_format='%.2f')


def get_books_link ():
    global rootUrl
    soupHTML = getSoupHTML(rootUrl)

    a_category_tag  = [
        a for a in soupHTML.select('li > a')
        if a.text.strip() != 'next'
    ]

    endpointList = [a.get('href') for a in a_category_tag]
    category_List = [
        a.text.strip() for a in a_category_tag
    ]


    return dict(zip(category_List, endpointList))


def getBooksInfoRecursion(url):
    soupHTML = getSoupHTML(url)
    articles = soupHTML.find_all('article')
    print(url)
    books = []
    for article in articles:
        title = article.h3.a.attrs['title']
        price_tag = article.find('p', class_='price_color')
        available = True if article.find('p', attrs={'class': ['instock', 'availability']}) else False
        price = float(price_tag.text[1:])
        currency = price_tag.text[:1]

        image_tag = article.find('img', attrs={'alt': title})
        image_name = get_image(url, image_tag.get('src'))

        books.append({
            'title': title,
            'price': price,
            'currency': currency,
            'available': available,
            'categories':'',
            'img_name': image_name,
        })

    nextTag  = [
        a for a in soupHTML.select('li > a')
        if a.text.strip() == 'next'
    ]

    if len(nextTag) > 0:
        endpoint = nextTag[0].get('href')
        return books + getBooksInfoRecursion(urljoin(url, endpoint))
    else:
        return books

def get_image(url, endpoint_image):
    absolute_image_url = urljoin(url, endpoint_image)

    os.makedirs("images", exist_ok=True)

    img_data = requests.get(absolute_image_url).content
    filename = os.path.basename(absolute_image_url.split("?")[0])

    with open(os.path.join("images", filename), "wb") as f:
        f.write(img_data)
    print(f"Downloaded: {filename}")
    return filename

def update_book(title, new_data, csv_path='books.csv'):
    # Đọc file CSV
    df = pd.read_csv(csv_path)

    # Ép kiểu cột tương ứng về object để tránh lỗi dtype
    for col in new_data:
        if col in df.columns:
            df[col] = df[col].astype('object')  # hoặc df[col].astype(str) nếu bạn chắc chắn là chuỗi

    # Kiểm tra tồn tại
    if not (df['title'] == title).any():
        print(f"[❌] Không tìm thấy sách có tiêu đề: {title}")
        return

    # Cập nhật từng trường
    for key, value in new_data.items():
        if key in df.columns:
            df.loc[df['title'] == title, key] = value
        else:
            print(f"[⚠️] Cột '{key}' không tồn tại trong CSV!")

    # Ghi lại vào file
    df.to_csv(csv_path, index=False)
    print(f"[✅] Đã cập nhật sách: {title}")


if __name__ == '__main__':
    pass
