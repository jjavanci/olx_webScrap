import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def make_request(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    return response

def parse_html(html, tag, a_class):
    soup = BeautifulSoup(html, 'html.parser')
    anuncios = soup.find_all(tag, class_= a_class)
    return anuncios

def obter_elemento_texto(info, tag, classe):
    elemento = info.find(tag, class_=classe)
    if elemento:
        return elemento.get_text()
    else:
        return None
    
def extract_car_info(infos, link, ano, km):
    nome = obter_elemento_texto(infos, 'h1', 'bYQcLm')     
    preco_atual = obter_elemento_texto(infos, 'h2', 'ad__sc-1leoitd-0 bJHaGt sc-hSdWYo dDGSHH')
    preco_anunciado = obter_elemento_texto(infos, 'span', 'ad__sc-1leoitd-1 bMUiTp sc-hSdWYo htqcWR')         
    model = obter_elemento_texto(infos, 'a', 'sc-EHOje lePqYm')
    
    return{
        'link': link,
        'nome': nome,
        'ano': ano,
        'km': km,
        'preco_atual': preco_atual,
        'preco_anunciado': preco_anunciado,
        'model': model
    }

url = f'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/vw-volkswagen/gol/estado-sp/regiao-de-presidente-prudente'
print(url)
    
site = make_request(url)
tag = 'div'
a_class = 'hrShZb'
anuncios = parse_html(site.content, tag, a_class)

data = []

i = 1

for anuncio in anuncios:
    print('PÁGINA 1')
    print(f'ANUNCIO {i}')
    link = anuncio.find('a', class_='gIhjul')['href']
    km = anuncio.find('span').get_text()
    ano = anuncio.findAll('span')[1].get_text()
    
    site = make_request(link)
    tag = 'div'
    a_class = 'eCUDNu'
    infos = parse_html(site.content, tag, a_class)

    info = infos[0]
    
    data.append(extract_car_info(info, link, ano, km))
    
    i += 1
    print('#####################################################')
    print()
    
   
for i in range(2, round(235/50)+2):
    j = 1
    url = f'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/vw-volkswagen/gol/estado-sp/regiao-de-presidente-prudente?o={i}'
    print(f'PÁGINA {i}')
    
    site = make_request(url)
    tag = 'div'
    a_class = 'hrShZb'
    anuncios = parse_html(site.content, tag, a_class)
    
    for anuncio in anuncios:
        print(f'PÁGINA {i}')
        print(f'ANUNCIO {j}')
        link = anuncio.find('a', class_='gIhjul')['href']
        km = anuncio.find('span').get_text()
        ano = anuncio.findAll('span')[1].get_text()
        
        site = make_request(link)
        tag = 'div'
        a_class = 'eCUDNu'
        infos = parse_html(site.content, tag, a_class)

        info = infos[0]
        
        data.append(extract_car_info(info, link, ano, km))
        
        
        j += 1
        print('#####################################################')
        print()

df = pd.DataFrame(data)
print(df)
df.to_csv('anuncios.csv', index=False) 