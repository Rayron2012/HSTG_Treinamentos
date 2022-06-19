# lista = ["Rayron", "Frank", "Kazinho", "Geyvid", "Nelson", "Leo", "Vitu"]
# genero = ["Dueko", "Gay", "Banido", "Web Gado", "Gasta tempo com NFT falido", "Korno", "Sulista"]
# nome = input("Digite o nome para descobrir o genero: ")
# nome = nome.capitalize()
#
# if nome in lista:
#     nome.capitalize()
#     i = lista.index(nome)
#
#     print("O nome {} é {} ".format(nome,genero[i]))
#
# else:
#     print("Digite o nome certo porraaaa! ")

# ---------------------------

# Padrão

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date

# criando um navegador
# navegador = webdriver.Chrome()
#
# # Chemando site
# navegador.get("https://www.google.com.br")
#
# # Pesquisar valor /.SENDKEYS PARA ESCREVER NA BARRA
# navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("DL Meta")
#
# #  dar enter
#
# navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#
# # entrar no dl
#
# navegador.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3').click()
#
# navegador.find_element(By.XPATH, '//*[@id="svelte"]/main/div/div[2]/div[1]/div/a/div/div[2]/img').click()
#
# navegador.find_element(By.XPATH, '//*[@id="svelte"]/main/div/div[4]/div[2]/div[2]/div[3]/div/div/a/div[2]').get_attribute("alt")

# ------------------------------------------

navegador = webdriver.Chrome()

# Chemando site
navegador.get("http://grupobem.callbox.com.br/login.php")

# Pesquisar valor /.SENDKEYS PARA ESCREVER NA BARRA
navegador.find_element(By.XPATH, '//*[@id="nome"]').send_keys("rayron.candido")

navegador.find_element(By.XPATH, '//*[@id="page"]/form/table/tbody/tr[3]/td/input').send_keys("Gbem2021")

#  dar enter

navegador.find_element(By.XPATH, '//*[@id="page"]/form/table/tbody/tr[5]/td/input').send_keys(Keys.ENTER)

navegador.find_element(By.XPATH, '//*[@id="Aba_2"]').click()

navegador.find_element(By.XPATH, '//*[@id="show_filtro"]/b').click()

navegador.find_element(By.XPATH, '//*[@id="filtro_conteudo"]/table/tbody/tr[1]/td[2]').click()

navegador.find_element(By.XPATH, '//*[@id="dataIni"]').click()

navegador.find_element(By.XPATH, '//*[@id="dataIni"]').send_keys(Keys.CONTROL + 'a')

navegador.find_element(By.XPATH, '//*[@id="dataIni"]').send_keys(Keys.DELETE)




# navegador.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3').click()
#
# navegador.find_element(By.XPATH, '//*[@id="svelte"]/main/div/div[2]/div[1]/div/a/div/div[2]/img').click()
#
# navegador.find_element(By.XPATH, '//*[@id="svelte"]/main/div/div[4]/div[2]/div[2]/div[3]/div/div/a/div[2]').get_attribute("alt")