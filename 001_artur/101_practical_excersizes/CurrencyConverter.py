import requests
from bs4 import BeautifulSoup as BS
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
btc_to_usd = 'https://www.google.com/search?q=btc+to+usd&oq=btc+to+usd&aqs=chrome..69i57j69i60l3j69i65.8692j0j1&sourceid=chrome&ie=UTF-8'
response = requests.get(btc_to_usd, headers=headers)
soup = BS(response.content, 'html.parser')

data = soup.find('span', class_='pclqee')
print(data.text)
print(float(data.text.replace(' ', ' ')))
print(data['data-value'])