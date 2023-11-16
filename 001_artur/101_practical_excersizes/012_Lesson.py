# Smotri Visual Studio Code urok po(vvedeniju v html) eto byl predidushii
# pip uninstall udalit bibiliotekjue
# source venv/bin/activate (zapustit) venv ne zabyvat ego aktivirovat
import requests
import re
# from requests.exceptions import HTTPError
# url = 'https://xkcd.com/353/'
# response = requests.get(url, timeout=10)
# # 200 success
# # 300 redirect
# # 400 client error
# # 500 server error
# # print(response.headers)
# for url in ['https://api.github.com','https://api.github.com/invalid' ]:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'Http Error occured: {http_err}')
#     else:
#         print('Success')
import bs4
from bs4 import BeautifulSoup as BS
url = "https://www.gammatest.net/course/python"
response = requests.get(url)
headers = {'User-Agent'}
soup = BS(response.content, 'html.parser')
# print(type(soup))
# print(soup.prettify())
# print(soup.title.text)
# print(soup.a)
# print(soup.body)
# print(soup.div['class'])
# print(soup.a['href'])

# match = soup.find('div', class_='col-md-8') #ne zozdaejom class kak dlja objectoorientirovannogo poetomu(class_) metod find naxodit pervyj popavshijsja
# print(match.table.text)
# matches = soup.find_all('a')
# for match in matches:
#     print(match['href'])
# print(soup.div.get_attribute_list('href')) #vydast [NONE]
# print(soup.find_all(re.compile('^me'))) ishet vse metatag
# print(soup.find_all(re.compile('^t?')))
# print(soup.find_all(re.compile('md')))
# print(soup.find_all(['a', 'title']))
# # print(soup.find_all(text='Eesti keeles'))
# print(soup.find_all(string=True))
# matches = (soup.title.findNext()).findNext()
# matches = (soup.title.findPreviouse())
# matches = (soup.td.find_next_sibling())
# matches = (soup.td.find_next('div'))
matches = (soup.td.find_parents())
print(matches)
