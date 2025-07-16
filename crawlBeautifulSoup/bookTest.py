import pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    response = requests.get('https://books.toscrape.com')
    if response.status_code != 200:
        print('Could not fetch the page')
        exit(1)

    print('Successfully fetched the page')

    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup, end='\n ___ \n')

    # print(soup.find("article").prettify())
    articles = soup.find_all('article')

    # books = []
    # for article in articles:
    #     title = article.h3.a.attrs['title']
    #     price_tag = article.find('p', class_='price_color')
    #     available = True if article.find('p', attrs={'class': ['instock', 'availability']}) else False
    #     books.append({
    #         'title': title,
    #         'price': float(price_tag.text[1:]),
    #         'currency': price_tag.text[:1],
    #         'available': available,
    #     })
    #
    # for book in books:
    #     print(book)

    # data_frame = pandas.DataFrame(books)
    # data_frame.to_csv('books.csv', index=False, encoding='utf-8', float_format='%.2f')
    #
    # added_book = {
    #     'title': 'added_book',
    #     'price' : 24.0,
    #     'currency': books[0]['currency'],
    #     'available': True,
    # }
    # new_df = pd.DataFrame([added_book])
    # new_df.to_csv('books.csv', index=False, encoding='utf-8', mode='a', header=False, float_format='%.2f')