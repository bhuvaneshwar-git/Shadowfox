import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
headers = {'User-Agent': 'Mozilla/5.0'}


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').text.strip()
    author = quote.find('small', class_='author').text.strip()
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]

    print(f"Quote: {text}")
    print(f"Author: {author}")
    print(f"Tags: {', '.join(tags)}")
    print('-' * 60)
