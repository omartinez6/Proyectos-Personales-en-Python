import requests
from bs4 import BeautifulSoup
from datetime import datetime

tiempo = datetime.now().strftime("%d%m%Y %H%M%S")

def precios(url,categoria):
    for page in range(1):
        url_formateada = f'{url}&page={page}'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'}

        response = requests.get(url_formateada, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        articulos = soup.find_all('div', class_='col-xs-8 col-sm-12 details')

        for item in range(0,len(articulos),2):
            if articulos[item].find('div',class_='content-name'):
                producto = articulos[item].find('div',class_='content-name').text.strip()
            else:
                producto = ''
            if articulos[item].find('span',class_='easyBuyPrice'):
                precio_easy_buy = articulos[item].find('span',class_='easyBuyPrice').text.strip()
            else:
                precio_easy_buy = ''
            if articulos[item].find(id='precio'):
                precio_promocion = articulos[item].find(id='precio').contents[0].strip()
            else:
                precio_promocion = ''
            if articulos[item].find(id='antes'):
                precio_lista = articulos[item].find(id='antes').contents[0].split()[1]
            elif articulos[item].find('div',class_='price no-promotion-price normal-price'):
                precio_lista = articulos[item].find('div',class_='price no-promotion-price normal-price').text.strip()
            elif articulos[item].find('div',class_='price no-promotion-price'):
                precio_lista = articulos[item].find('div',class_='price no-promotion-price').text.strip()
            else:
                precio_lista = ''
            print(f'\'{producto}\',"{precio_easy_buy}","{precio_promocion}","{precio_lista}",{categoria}\n')

perros = 'https://www.petco.com.mx/petco/en/PRODUCTOS/Perro/c/01-00-00?q=%3AbestSeller'
gatos = 'https://www.petco.com.mx/petco/en/PRODUCTOS/Gato/c/02-00-00?q=%3AbestSeller'
reptiles = 'https://www.petco.com.mx/petco/en/PRODUCTOS/Reptiles/c/05-00-00?q=%3AbestSeller'
mamiferos = 'https://www.petco.com.mx/petco/en/PRODUCTOS/Mam%C3%ADferos/c/03-00-00?q=%3AbestSeller'
aves = 'https://www.petco.com.mx/petco/en/PRODUCTOS/Aves/c/04-00-00?q=%3AbestSeller'
peces = 'https://www.petco.com.mx/petco/en/PRODUCTOS/Peces/c/06-00-00?q=%3AbestSeller'
farmacia_perros = 'https://www.petco.com.mx/petco/en/PRODUCTOS/Farmacia/Farmacia-Perro/c/07-01-00?q=%3AbestSeller'
farmacia_gatos = 'https://www.petco.com.mx/petco/en/PRODUCTOS/Farmacia/Farmacia-Gato/c/07-02-00?q=%3AbestSeller'
alimento_prescripcion = 'https://www.petco.com.mx/petco/en/App/Farmacia-Alimento-prescripci%C3%B3n-Perro-y-Gato/c/1010?q=%3AbestSeller'

archivo = f'G:/.shortcut-targets-by-id/1E_5fKDjUxJlHjWTcIKwpWdxcVqIH6Sc8/Salud Animal/Scrapers/Alimento y accesorios/Precios/petco {tiempo}.csv'
with open(archivo, 'a') as archivo:
    archivo.write(f'producto,precio easy buy,precio promoción,precio de lista,categoría\n')
    precios(perros,'perros')
    precios(gatos,'gatos')
    precios(reptiles,'reptiles')
    precios(mamiferos,'mamíferos')
    precios(aves,'aves')
    precios(peces,'peces')
    precios(farmacia_perros,'farmacia perros')
    precios(farmacia_gatos,'farmacia gatos')
    precios(alimento_prescripcion,'alimento de prescripción')