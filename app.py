import requests
from bs4 import BeautifulSoup

# Step 1: Get the HTML content of the page
url = 'http://quotes.toscrape.com'
response = requests.get(url)
html = response.text

# Step 2: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Step 3: Find and print all quotes
quotes = soup.find_all('span', class_='text')
for quote in quotes:
    print(quote.text)