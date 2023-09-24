import requests
from bs4 import BeautifulSoup
from datetime import datetime

tiempo = datetime.now().strftime('%d%m%Y %H%M%S')

def precios(url,categoria):
    for page in range(1, 51, 1):
        url_formateada = f'{url}?page={page}'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'}

        response = requests.get(url_formateada, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        alimentos = soup.find_all('div',class_='product-detail content-center')

        for alimento in alimentos:
            producto = alimento.find('a').contents[0]
            precio = alimento.find(id='ProductPrice').contents[0].strip()
            archivo.write(f'"{producto}","{precio}",{categoria}\n')

perros = 'https://maskota.com.mx/collections/perros'
gatos = 'https://maskota.com.mx/collections/gatos'
roedores = 'https://maskota.com.mx/collections/roedores'
aves = 'https://maskota.com.mx/collections/aves'
reptiles = 'https://maskota.com.mx/collections/reptiles'
peces = 'https://maskota.com.mx/collections/peces'
pequenas_especies = 'https://maskota.com.mx/collections/pequenas-especies'

archivo = f'G:/.shortcut-targets-by-id/1E_5fKDjUxJlHjWTcIKwpWdxcVqIH6Sc8/Salud Animal/Scrapers/Alimento y accesorios/Precios/+kota {tiempo}.csv'
with open(archivo, 'a') as archivo:
    archivo.write(f'producto,precio,categoría\n')
    precios(perros,'perros')
    precios(gatos,'gatos')
    precios(roedores,'roedores')
    precios(aves,'aves')
    precios(reptiles,'reptiles')
    precios(peces,'peces')
    precios(pequenas_especies,'pequeñas especies')