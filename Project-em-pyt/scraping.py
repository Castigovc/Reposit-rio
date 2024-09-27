from bs4 import BeautifulSoup
import pandas as pd
import requests
import os

lista = []
print('  Web scraping   ')
c = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'

header = {'User-Agent': c}

link = 'https://g1.globo.com/'
response = requests.get(link, headers=header)

os.system('cls')

script = response.content  # propriedade do request que traz o script em HTML do site

b = BeautifulSoup(script, 'html.parser')  # faz a transformação do script para HTML

# Obtém todas as notícias
noticias = b.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    
    if titulo:  # Verifica se o título foi encontrado
        link = titulo.get('href', 'Link não disponível')  # Usa .get() para evitar o KeyError
        sub = noticia.find('ul', attrs={'class': 'bstn-relateditems'})
        
        if sub:
            lista.append([titulo.text, sub.text, link])
        else:
            lista.append([titulo.text, 'Sem sub titulo', link])
    else:
        print("Erro: Título não encontrado em uma das notícias.")

print()

# Cria o DataFrame com os dados extraídos
new = pd.DataFrame(lista, columns=['Titulo', 'Subtitulo', 'Links'])
print(new)

# Salvar os dados em um arquivo CSV (opcional)
# new.to_csv('Nome_do_arquivo.csv', index=False)
