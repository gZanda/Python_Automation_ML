from selenium import webdriver
import pandas

# 1° Abrir o navegador
navegador = webdriver.Firefox()
navegador.get("https://www.google.com.br/?hl=pt-BR")

# 2° Importar a base de dados
tabela = pandas.read_excel("commodities.xlsx")
print(tabela)

# 3° Pegar o preço atual de cada produto ( algum site )
navegador.get("https://www.melhorcambio.com/milho-hoje")    # Abre o site
navegador.find_element("xpath",'//*[@id="comercial"]')      # Pega o campo da cotação

# O que podemos fazer com esse campo ?
# .send_keys() - Escrever
# .click()
# .get_attribute() - Pegar os dados

# 4° Atualizar o Preço na base de dados

# 5° Decidir comprar ou não

# 6° Exportar a base Atualizada
