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

def obter_elemento_texto(info, tag, classe):
    elemento = info.find(tag, class_=classe)
    if elemento:
        return elemento.get_text()
    else:
        return None

def scrapy_initial_page(regiao, modelo, carro):
    url = f'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/{modelo}/{carro}/estado-sp/{regiao}'
    print(url)

    site = make_request(url)
    tag = 'div'
    a_class = 'hrShZb'
    anuncios = parse_html(site.content, tag, a_class)
    j = 1

    for anuncio in anuncios:
        print(f'PÁGINA 1')
        print(f'ANUNCIO {j}')
        link = anuncio.find('a', class_='gIhjul')['href']
        km = anuncio.find('span').get_text()
        ano = anuncio.findAll('span')[1].get_text()
    
        site = make_request(link)
        tag = 'div'
        a_class = 'eCUDNu'
        infos = parse_html(site.content, tag, a_class)
        
        if infos == []:
            print('Erro')
            print('Erro')
            print('Erro')
            print('Erro')
            print('Erro')
            anuncio = {
            'Regiao': None,
            'Link': None,
            'Nome': None,
            'km': None,
            'Ano': None,
            'Preço Atual': None,
            'Preço Anunciado': None,
            'Modelo': None
        }
        else:

            info = infos[0]
    
            nome = obter_elemento_texto(info, 'h1', 'bYQcLm')
            preco_atual = obter_elemento_texto(info, 'h2', 'ad__sc-1leoitd-0 bJHaGt sc-hSdWYo dDGSHH')
            preco_anunciado = obter_elemento_texto(info, 'span', 'ad__sc-1leoitd-1 bMUiTp sc-hSdWYo htqcWR')
            model = obter_elemento_texto(info, 'a', 'sc-EHOje lePqYm')
        
            print(f'Regiao: {regiao}')
            print(f'Link: {link}')
            print(f'Nome: {nome}')
            print(f'km: {km}')
            print(f'Ano: {ano}')
            print(f'Preço Atual: {preco_atual}')
            print(f'Preço Anunciado: {preco_anunciado}')
            print(f'Modelo: {model}')
        
            anuncio = {
                'Regiao': regiao,
                'Link': link,
                'Nome': nome,
                'km': km,
                'Ano': ano,
                'Preço Atual': preco_atual,
                'Preço Anunciado': preco_anunciado,
                'Modelo': model
            }
            
        data.append(anuncio)
    
        j += 1
        print('#'*60)
        print()

def scrapy_other_pages(regiao, modelo, carro, pages):
    url = f'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/{modelo}/{carro}/estado-sp/{regiao}?o={pages}'
    print(url)

    site = make_request(url)
    tag = 'div'
    a_class = 'hrShZb'
    anuncios = parse_html(site.content, tag, a_class)
    j = 1

    for anuncio in anuncios:
        print(f'PÁGINA {i}')
        print(f'ANUNCIO {j}')
        print(url)
        link = anuncio.find('a', class_='gIhjul')['href']
        km = anuncio.find('span').get_text()
        ano = anuncio.findAll('span')[1].get_text()
    
        site = make_request(link)
        tag = 'div'
        a_class = 'eCUDNu'
        infos = parse_html(site.content, tag, a_class)
        print(f'Infos: {type(infos)}')

        if infos == []:
            print('Erro')
            print('Erro')
            print('Erro')
            print('Erro')
            print('Erro')
            anuncio = {
            'Regiao': None,
            'Link': None,
            'Nome': None,
            'km': None,
            'Ano': None,
            'Preço Atual': None,
            'Preço Anunciado': None,
            'Modelo': None
        }
        else:

            info = infos[0]
    
            nome = obter_elemento_texto(info, 'h1', 'bYQcLm')
            preco_atual = obter_elemento_texto(info, 'h2', 'ad__sc-1leoitd-0 bJHaGt sc-hSdWYo dDGSHH')
            preco_anunciado = obter_elemento_texto(info, 'span', 'ad__sc-1leoitd-1 bMUiTp sc-hSdWYo htqcWR')
            model = obter_elemento_texto(info, 'a', 'sc-EHOje lePqYm')
        
            print(f'Regiao: {regiao}')
            print(f'Link: {link}')
            print(f'Nome: {nome}')
            print(f'km: {km}')
            print(f'Ano: {ano}')
            print(f'Preço Atual: {preco_atual}')
            print(f'Preço Anunciado: {preco_anunciado}')
            print(f'Modelo: {model}')
        
            anuncio = {
                'Regiao': regiao,
                'Link': link,
                'Nome': nome,
                'km': km,
                'Ano': ano,
                'Preço Atual': preco_atual,
                'Preço Anunciado': preco_anunciado,
                'Modelo': model
            }
            
        data.append(anuncio)
            
        j += 1
        print('#'*60)
        print()


data = []
modelo = 'vw-volkswagen'
carro = 'gol'
regioes = [['sao-paulo-e-regiao', round(3440/50)],
            ['vale-do-paraiba-e-litoral-norte', round(894/50)],
            ['baixada-santista-e-litoral-sul', round(306/50)],
            ['regiao-de-bauru-e-marilia', round(370/50)],
            ['regiao-de-sorocaba', round(778/50)],
            ['regiao-de-ribeirao-preto', round(672/50)],
            ['regiao-de-sao-jose-do-rio-preto', round(617/50)],
            ['regiao-de-presidente-prudente', round(262/50)],
            ['grande-campinas', round(1056/50)]]


scrapy_initial_page('sao-paulo-e-regiao', modelo, carro)

for i in range(2, round(3440/50)+1):
    scrapy_other_pages('sao-paulo-e-regiao', modelo, carro, i)


scrapy_initial_page('vale-do-paraiba-e-litoral-norte', modelo, carro)

for i in range(2, round(894/50)+1):
    scrapy_other_pages('vale-do-paraiba-e-litoral-norte', modelo, carro, i)


scrapy_initial_page('baixada-santista-e-litoral-sul', modelo, carro)

for i in range(2, round(306/50)+1):
    scrapy_other_pages('baixada-santista-e-litoral-sul', modelo, carro, i)


scrapy_initial_page('regiao-de-bauru-e-marilia', modelo, carro)

for i in range(2, round(370/50)+1):
    scrapy_other_pages('regiao-de-bauru-e-marilia', modelo, carro, i)


scrapy_initial_page('regiao-de-sorocaba', modelo, carro)

for i in range(2, round(778/50)+1):
    scrapy_other_pages('regiao-de-sorocaba', modelo, carro, i)


scrapy_initial_page('regiao-de-ribeirao-preto', modelo, carro)

for i in range(2, round(672/50)+1):
    scrapy_other_pages('regiao-de-ribeirao-preto', modelo, carro, i)


scrapy_initial_page('regiao-de-sao-jose-do-rio-preto', modelo, carro)

for i in range(2, round(617/50)+1):
    scrapy_other_pages('regiao-de-sao-jose-do-rio-preto', modelo, carro, i)


scrapy_initial_page('regiao-de-presidente-prudente', modelo, carro)

for i in range(2, round(262/50)+1):
    scrapy_other_pages('regiao-de-presidente-prudente', modelo, carro, i)


scrapy_initial_page('grande-campinas', modelo, carro)

for i in range(2, round(1056/50)+1):
    scrapy_other_pages('grande-campinas', modelo, carro, i)

# loop para captar todas a regiões (estava dando "index out of range" antes de terminar)
#for regiao in regioes:
 #   scrapy_initial_page(regiao[0], modelo, carro)

#for regiao in regioes:
 #   for i in range(2, regiao[1]+1):
  #      scrapy_other_pages(regiao[0], modelo, carro, i)

#Teste por página
#i = 13
#scrapy_other_pages('vale-do-paraiba-e-litoral-norte', modelo, carro, i)


df = pd.DataFrame(data)
print(df)