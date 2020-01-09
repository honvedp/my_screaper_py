from bs4 import BeautifulSoup
import requests

response = requests.get('https://hu.wikipedia.org/wiki/Kezd%C5%91lap')

html = response.text
soup = BeautifulSoup(html, 'html.parser')

print(soup.title)
print(soup.p)