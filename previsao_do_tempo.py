# Desenvolvedor Brevetecno
# Python 3.7
# 2019

from requests_html import HTMLSession

session = HTMLSession()

# Previsão do tempo se baseia nas estásticas do Google
url = 'https://www.google.com.br/search?q=previsao+do+tempo&oq=previsao+do+tempo&ie=UTF-8'

#URL resultado da busca no Google por: previsao do tempo
r = session.get(url)

# Abaixo estão os seletores CSS de cada elemento da pagina

# Pega o local
selector_city = '#wob_loc'
city = r.html.find(selector_city, first=True).text

# Pega a situação do tempo
selector_state = '#wob_dc'
state = r.html.find(selector_state, first=True).text

# Pega a temperatura
selector_temp = '#wob_tm'
temp = r.html.find(selector_temp, first=True).text


# Mostra os resultados
print('='*50)
print('Local: {}'.format(city))
print('Temperatura: {}º Celsius'.format(temp))
print('Situação do tempo: {}'.format(state))
print('='*50)
