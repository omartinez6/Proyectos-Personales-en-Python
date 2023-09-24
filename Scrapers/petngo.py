import requests
from bs4 import BeautifulSoup
from datetime import datetime

tiempo = datetime.now().strftime('%d%m%Y %H%M%S')

def precios(url,categoria,subcategoria):
    for page in range(1,50,1):
        url_formateada = f'{url}?page={page}'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'}

        response = requests.get(url_formateada, headers=headers)
        soup = BeautifulSoup(response.text,'html.parser')

        articulos = soup.find_all('div', class_='sf__pcard-content text-left')

        for articulo in articulos:
            producto = articulo.find('a').contents[0].strip()
            print(producto)


perros_alimento_natural = 'https://www.petngo.com.mx/collections/alimento-natural-para-perros-mexico'

precios(perros_alimento_natural,'perros','alimento natural')