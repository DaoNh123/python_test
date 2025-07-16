from Utils import *
import pandas as pd
from parquetUtils import *
from book2 import *

if __name__ == '__main__':

    df = pd.read_csv('books.csv')
    books = df.to_dict(orient='records')
    book_objects = []
    for book in books:
        book_object = Book(**book)
        book_objects.append(book_object)

    # First time append
    append_parquet_batch ([book_object.to_dict() for book_object in book_objects][:5])
    append_parquet_batch ([book_object.to_dict() for book_object in book_objects][5:10])
    read_parquet_batch()

    print("   ___   ")
    # table = pq.read_table("parquet_data")
    # # Convert thành DataFrame nếu cần
    # df = table.to_pandas()
    # dict = df.to_dict(orient='records')
    # print(len(dict))
    # print(df.head(10))

    for book_object in book_objects:
        book_object.categories = 'new categories'

    # Append to update 3 records
    append_parquet_batch([book_object.to_dict() for book_object in book_objects[7:10]])

    read_parquet_batch()