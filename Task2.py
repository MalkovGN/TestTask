import requests
from bs4 import BeautifulSoup as Soup

letter_counter = {}
flag = True
a = ord('а')
alphabet = ''.join([chr(i).upper() for i in range(a, a + 32)])
alphabet = alphabet[:6] + 'Ё' + alphabet[6:]

for letter in alphabet:
    letter_counter[letter] = 0
letter_counter['H'] = 0  # On 22nd page the name of animal in English (started with letter 'H')

url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
page = requests.get(url).text
while flag:
    soup = Soup(page, 'html.parser')
    animals = soup.find('div', class_='mw-category-generated').find_all('a')
    for animal in animals:
        if animal.text[0] != 'A':  # First English letter
            letter_counter[animal.text[0]] += 1
        else:
            flag = False
    links = soup.find('div', id='mw-pages').find_all('a')
    for link in links:
        if link.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + link.get('href')
            page = requests.get(url).text

del letter_counter['H']
for key, value in letter_counter.items():
    print(key + ':', value)
