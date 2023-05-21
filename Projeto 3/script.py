from selenium import webdriver
import pandas

# Comandos do navegador.get --------------------------------------------

# .send_keys() -> Escrever
# .click() 
# .get_attribute() -> Pegar os dados

# -----------------------------------------------------------------------

# 1° Abrir o navegador

navegador = webdriver.Firefox()
navegador.get("https://www.google.com.br/?hl=pt-BR")

# 2° Importar a base de dados

tabela = pandas.read_excel("commodities.xlsx")

# 3° Pegar o preço atual de cada produto ( algum site )

# Pegar todos
for linha in tabela.index:
    produto = tabela.loc[linha,"Produto"]

    # Abre OS SITES CORRETOS
    link = f"https://www.melhorcambio.com/{produto}-hoje" 
    # Formatar o link
    link = link.replace("ó","o").replace("á","a").replace("ã","a").replace("é","e").replace("ç","c").replace("ú","u")
    print("Entrando em:",link)
    navegador.get(link)

    # Pegando cotação
    cotacao = navegador.find_element("xpath",'//*[@id="comercial"]').get_attribute('value')      # Pega o campo da cotação pelo xpath

    # A cotação precisa ser formatada ( Ela vem como String )
    cotacao = cotacao.replace("." , "")
    cotacao = cotacao.replace("," , ".")
    cotacao = float(cotacao)

    print(cotacao)

    # 4° Atualizar o Preço na base de dados
    tabela.loc[linha,"Preço Atual"] = cotacao # Linha, Coluna a ser editada
    print(tabela)
    print("--------------------------------------------------------------\n")

# 5° Decidir comprar ou não

tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]   # Muda toda a coluna
print(tabela)

# 6° Exportar a base Atualizada

# Fechar Navegador
navegador.quit()

# Exportar
print("Tabela Exportada :3")
tabela.to_excel("comoddities_Atualizado.xlsx",index=False) # Não exporta os índices da tabela