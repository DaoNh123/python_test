# # import requests
# # from bs4 import BeautifulSoup
# #
# # # Gửi yêu cầu GET đến website
# # url = 'https://quotes.toscrape.com/'
# # response = requests.get(url)
# #
# # # Phân tích nội dung HTML với BeautifulSoup
# # soup = BeautifulSoup(response.text, 'html.parser')
# #
# # # Tìm tất cả các thẻ chứa quote
# # quotes = soup.find_all('span', class_='text')
# # authors = soup.find_all('small', class_='author')
# #
# # # In ra kết quả
# # for quote, author in zip(quotes, authors):
# #     print(f'{quote.text} — {author.text}')
#
#
# # # Ex2:
# # import requests
# # URL = "https://www.geeksforgeeks.org/data-structures/"
# #
# # headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# #
# # r = requests.get(url=URL, headers=headers)
# # print(r.content)
# # print(r.content)
#
#
# ## Ex3:
# # import requests
# # from bs4 import BeautifulSoup
# #
# # URL = "http://www.values.com/inspirational-quotes"
# # r = requests.get(URL)
# #
# # soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
# # print(soup.prettify())
#
# ## Ex4:
# # Python program to scrape website and save quotes from website
# import requests
# from bs4 import BeautifulSoup
# import csv
#
# URL = "http://www.values.com/inspirational-quote"
# r = requests.get(URL)
#
# soup = BeautifulSoup(r.content, 'html5lib')
#
# print(soup.prettify())
#
# quotes = []  # a list to store quotes
# table = soup.find('div', attrs={'id': 'all_quotes'})
#
# for row in table.findAll('div',
#                          attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
#     quote = {}
#     quote['theme'] = row.h5.text
#     quote['url'] = row.a['href']
#     quote['img'] = row.img['src']
#     quote['lines'] = row.img['alt'].split("#")[0]
#     quote['author'] = row.img['alt'].split("#")[1]
#     quotes.append(quote)
#
#     filename = 'inspirational_quotes.csv'
#     with open(filename, 'w', newline='') as f:
#         w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
#         w.writeheader()
#         for quote in quotes:
#             w.writerow(quote)