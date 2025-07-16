from datetime import datetime


class Book:
    sep = ", "

    def __init__(self, title, price, currency, available, categories, img_name):
        self.__title = title
        self.__price = price
        self.__currency = currency
        self.__available = available
        self.__categories = categories
        self.__img_name = img_name
        self.updated_at = datetime.now()

    def __str__(self):
        return (f'{self.__title} : Categories: {self.__categories} - {self.__price} - {self.__currency} - {self.__available}'
                f'Image_name: {self.__img_name}')

    def to_dict(self):
        return {
            'title': self.__title,
            'price': self.__price,
            'currency': self.__currency,
            'available': self.__available,
            'categories': self.__categories,
            'img_name': self.__img_name,
            'updated_at': self.updated_at,
        }
    @property
    def categories(self):
        return self.__categories
    @categories.setter
    def categories(self, categories):
        self.__categories = categories

if __name__ == '__main__':
    pass
    # added_book = {
    #     'title': 'This is added_book',
    #     'price' : 24.0,
    #     'currency': '£',
    #     'available': True,
    # }
    #
    # book_Object = Book(**added_book)
    # print(book_Object)
    # print(*added_book)
