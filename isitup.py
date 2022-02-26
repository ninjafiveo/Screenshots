from unittest import result
from bs4 import BeautifulSoup
import requests

url = input('Enter the URL: (duckduckgo.com) : ')
req = requests.get('https://isitup.org/'+url)

soup = BeautifulSoup(req.text, 'html.parser' )

out_box = soup.find('div', {'id':'container'})

result = out_box.find('p').text

print(result)
