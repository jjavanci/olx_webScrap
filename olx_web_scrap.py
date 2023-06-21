import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-sp'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')
#carros = soup.find_all('li', class_='hqJEoJ')
#carros = soup.find_all('ul', class_='glvDlr')
carros = soup.find_all('div', class_='hrShZb')

carro = carros[1]
link_carro = carro.find('a', class_='gIhjul')
nome_carro = carro.find('h2', class_='hUnWqk').get_text()
preco_carro = carro.find('h3', class_='bytyxL').get_text()#[3:]
info_carro = carro.findAll('span')[0].get_text()
info_carro1 = carro.findAll('span')[1].get_text()
info_carro2 = carro.findAll('span')[2].get_text()
info_carro3 = carro.findAll('span')[3].get_text()

print(len(carros))
#print(carro)
print(link_carro)
print()
print(nome_carro)
print()
print(preco_carro)
print()
print(info_carro)
print(info_carro1)
print(info_carro2)
print(info_carro3)