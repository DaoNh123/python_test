from unittest import case

import pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup

def textToNum(num_text):
    match num_text:
        case 'One':
            return 1
        case 'Two':
            return 2
        case 'Three':
            return 3
        case 'Four':
            return 4
        case 'Five':
            return 5

if __name__ == '__main__':
    response = requests.get('https://books.toscrape.com/catalogue/page-50.html')
    if response.status_code != 200:
        print(response.status_code)
        print('Could not fetch the page')
        exit(1)

    print('Successfully fetched the page')

    soup = BeautifulSoup(response.content, 'html5lib' )

    print(soup.find("article").prettify(), end="\n ____ \n")
    # articles = soup.find_all('article')

    first_article = soup.find('article')
    starRatingTag = first_article.find('p', attrs={'class':'star-rating'})
    print(starRatingTag, end="\n ____ \n")

    star = textToNum(starRatingTag.get('class')[1])
    print(star, end="\n ____ \n")
