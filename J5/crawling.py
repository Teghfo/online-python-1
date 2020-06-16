####   requests , bs4 , selenium
import requests    #### http request(get, post)
from bs4 import BeautifulSoup

response = requests.get('https://www.isna.ir/service/Science-Academia')

# print(response.status_code)

# print(response.headers['content-type'])

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup)

result = soup.find_all('div', class_='desc')

with open('isna_data', 'w') as f:
    for elm in result:
        f.write(elm.text)
