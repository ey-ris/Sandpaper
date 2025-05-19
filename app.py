import requests
from bs4 import BeautifulSoup

# get the HTML content of the page
url = 'http://quotes.toscrape.com'
response = requests.get(url)
html = response.text

# parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# find all quote blocks
blocks = soup.find_all('div', class_='quote')

# find quotes and authors in blocks
for block in blocks:
    quote = block.find('span', class_='text')
    author = block.find('small', class_='author')
    print(quote.text + ' - ' + author.text)