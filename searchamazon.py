from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import time
import webbrowser

# Junta os termos
search_term = ' '.join(sys.argv[1:])

print('Abrindo Amazon...')

driver = webdriver.Chrome()
driver.get('https://www.amazon.com.br')

time.sleep(3)

# Encontra a barra de pesquisa
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys(search_term)
search_box.send_keys(Keys.RETURN)

print(f'Pesquisando por: {search_term}')
time.sleep(5)

# Captura links de produtos
links = driver.find_elements(By.CSS_SELECTOR, 'a.a-link-normal.s-no-outline')

product_urls = []

for link in links:
    href = link.get_attribute('href')
    if href and '/dp/' in href:
        clean_url = href.split('?')[0]
        if clean_url not in product_urls:
            product_urls.append(clean_url)

print(f'Encontrados {len(product_urls)} produtos únicos.')

num_open = min(5, len(product_urls))

for i in range(num_open):
    print('Abrindo:', product_urls[i])
    webbrowser.open(product_urls[i])

driver.quit()
