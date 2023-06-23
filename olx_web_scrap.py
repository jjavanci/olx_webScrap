import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def make_request(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    return response

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    anuncios = soup.find_all('div', class_='hrShZb')
    return anuncios

def extract_car_info(anuncio):
    try:
        link = anuncio.find('a', class_='gIhjul')['href']
        nome = anuncio.find('h2', class_='hUnWqk').get_text()
        preco = anuncio.find('h3', class_='bytyxL').get_text()
        info = [anuncio.findAll('span')[0].get_text()[:-3], anuncio.findAll('span')[1].get_text(), anuncio.findAll('span')[2].get_text(), anuncio.findAll('span')[3].get_text()]
        km = info[0]
        ano = info[1]
        combustivel = info[2]
        cambio = info[3]

    except:
        link = 'n/c'
        nome = 'n/c'
        preco = 'n/c'
        info = 'n/c'
        km = 'n/c'
        ano = 'n/c'
        combustivel = 'n/c'
        cambio = 'n/c'

    return {
        'link': link,
        'nome': nome,
        'preco': preco,
        'km': km,
        'ano': ano,
        'combutivel': combustivel,
        'cambio': cambio
    }

url = 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/vw-volkswagen/gol/estado-sp?rs='
site = make_request(url)
anuncios = parse_html(site.content)

anuncios_info = []

for anuncio in anuncios:
    anuncio_info = extract_car_info(anuncio)
    anuncios_info.append(anuncio_info)

print('###PÁGINA 1###')
print(len(anuncios_info))

#Código para as demais páginas
for i in range(2, 101):
    url = f'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/vw-volkswagen/gol/estado-sp?o={i}'
    site = make_request(url)
    anuncios = parse_html(site.content)

    for anuncio in anuncios:
        anuncio_info = extract_car_info(anuncio)
        anuncios_info.append(anuncio_info)

    print(f'###PÁGINA {i}###')
    print(len(anuncios_info))

print(len(anuncios_info))


df = pd.DataFrame(anuncios_info)
print(df)
df.to_csv('carros.csv', index=False)