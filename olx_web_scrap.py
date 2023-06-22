import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-sp'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')
carros = soup.find_all('div', class_='hrShZb')

#ultima_pagina = soup.find_all('span', class_='sc-1bofr6e-1 hEtrnt sc-ifAKCX bVUFRk')[-1]

list_link_carro = []
list_nome_carro = []
list_preco_carro = []
list_info_carro = []
list_info_carro1 = []
list_info_carro2 = []
list_info_carro3 = []

i = 0

for carro in carros:

    try:
        link_carro = carro.find('a', class_='gIhjul')
        nome_carro = carro.find('h2', class_='hUnWqk').get_text()
        preco_carro = carro.find('h3', class_='bytyxL').get_text()#[3:]
        info_carro = carro.findAll('span')[0].get_text()
        info_carro1 = carro.findAll('span')[1].get_text()
        info_carro2 = carro.findAll('span')[2].get_text()
        info_carro3 = carro.findAll('span')[3].get_text()
    
    except:
        nome_carro = 'n/c'
        preco_carro = 'n/c'
        info_carro = "n/c"
        info_carro1 = "n/c"
        info_carro2 = "n/c"
        info_carro3 = "n/c"
        #print("IndexError")

    i += 1
    """print(url)
    print(link_carro.get('href'))
    print()
    print(nome_carro)
    print()
    print(preco_carro)
    print()
    print(info_carro)
    print(info_carro1)
    print(info_carro2)
    print(info_carro3)
    print()
    print('####################################################################################################################')"""

    list_link_carro.append(link_carro.get('href'))
    list_nome_carro.append(nome_carro)
    list_preco_carro.append(preco_carro)
    list_info_carro.append(info_carro)
    list_info_carro1.append(info_carro1)
    list_info_carro2.append(info_carro2)
    list_info_carro3.append(info_carro3)


print(str(i) + ' anúncios')
print('FIM PÁGINA 1')


for i in range(2, 101):
    
    url = f'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-sp?o={i}'
    #print(url)
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    carros = soup.find_all('div', class_='hrShZb')
    
    for carro in carros:

        try:
            link_carro = carro.find('a', class_='gIhjul')
            nome_carro = carro.find('h2', class_='hUnWqk').get_text()
            preco_carro = carro.find('h3', class_='bytyxL').get_text()#[3:]
            info_carro = carro.findAll('span')[0].get_text()
            info_carro1 = carro.findAll('span')[1].get_text()
            info_carro2 = carro.findAll('span')[2].get_text()
            info_carro3 = carro.findAll('span')[3].get_text()
    
        except:
            nome_carro = 'n/c'
            preco_carro = 'n/c'
            info_carro = "n/c"
            info_carro1 = "n/c"
            info_carro2 = "n/c"
            info_carro3 = "n/c"
            #print("IndexError")
        """
        print(url)
        print(link_carro.get('href'))
        print()
        print(nome_carro)
        print()
        print(preco_carro)
        print()
        print(info_carro)
        print(info_carro1)
        print(info_carro2)
        print(info_carro3)
        print()
        print('####################################################################################################################')"""

        list_link_carro.append(link_carro.get('href'))
        list_nome_carro.append(nome_carro)
        list_preco_carro.append(preco_carro)
        list_info_carro.append(info_carro)
        list_info_carro1.append(info_carro1)
        list_info_carro2.append(info_carro2)
        list_info_carro3.append(info_carro3)
    
    print('####Página ' + str(i))
""""
print(list_link_carro)
print(list_nome_carro)
print(list_preco_carro)
print(list_info_carro)
print(list_info_carro1)
print(list_info_carro2)
print(list_info_carro3)"""

anuncios_carro_dict = {'link': list_link_carro, 'nome': list_nome_carro, 'preco': list_preco_carro, 'info':list_info_carro, 'info1': list_info_carro1, 'info2':list_info_carro2, 'info3': list_info_carro3}
#print(anuncios_carro_dict)
#print(type(anuncios_carro_dict))

df = pd.DataFrame(anuncios_carro_dict)
print(df)

df.to_csv('anúncios.csv', index=False)