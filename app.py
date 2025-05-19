import requests
from bs4 import BeautifulSoup

# get the HTML content of the page
url = 'https://www.templetonspirits.com/whiskey'
response = requests.get(url)
html = response.text

# parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all whiskey cards
cards = soup.find_all('div', class_='bg-white rounded-lg overflow-hidden shadow-md')

# Dictionary to group items by category
whiskey_by_category = {}

for card in cards:
    name = card.find('h3', class_='font-bold text-lg mb-1')
    category = card.find('p', class_='text-gray-600 text-sm')

    if name and category:
        category_text = category.text.strip()
        name_text = name.text.strip()

        # Add name under the right category
        if category_text not in whiskey_by_category:
            whiskey_by_category[category_text] = []
        whiskey_by_category[category_text].append(name_text)

# Print grouped output
for category, items in whiskey_by_category.items():
    print(f"\n{category}:")
    for i, item in enumerate(items, start=1):
        print(f"  {i}) {item}")
