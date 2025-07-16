from Utils import *
import pandas as pd
from parquetUtils import *
from book2 import *

if __name__ == '__main__':
    # rootUrl = 'https://books.toscrape.com'
    # books = getBooksInfoRecursion(rootUrl)
    url2 = 'https://books.toscrape.com//catalogue/page-50.html'
    books = getBooksInfoRecursion(url2)

    save_to_csv(books, 'books.csv')

    readBooks = pd.read_csv('books.csv')
    print(readBooks.head(3).T)

    update_book("Frankenstein", {"categories": "Poetry2", "price": 42.11})

    readUpdatedBooks = pd.read_csv('books.csv')
    print(readUpdatedBooks.head(3).T)