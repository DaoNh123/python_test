
sep = ", "

class Book:
    def __init__(self, title, price, currency, available, category_list = []):
        self.__title = title
        self.__price = price
        self.__currency = currency
        self.__available = available
        self.__categories = sep.join(category_list)

    def __str__(self):
        return f'{self.__title} : Categories: {self.__categories} - {self.__price} - {self.__currency} - {self.__available}'

    def to_dict(self):
        return {
            'title': self.__title,
            'price': self.__price,
            'currency': self.__currency,
            'available': self.__available,
            'category_list': self.__categories.split(sep),
        }

if __name__ == '__main__':
    added_book = {
        'title': 'This is added_book',
        'price' : 24.0,
        'currency': '£',
        'available': True,
    }

    book_Object = Book(**added_book)
    print(book_Object)
    print(*added_book)

    arr = ['123', 'abc', 'e234']
    joinArr = sep.join(arr)
    print(joinArr)
    print(joinArr.split(sep))
