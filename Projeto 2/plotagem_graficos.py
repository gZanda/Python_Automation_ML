# Objetivo: Analisar os dados e encontrar clientes ideais ( MAIOR NOTA )

# plotly = Criar gráficos
import pandas, plotly.express as plot

# 1° Importar a Base de dados ----------------------------------------------------

# Ela tem caracteres especiais ( precisa de "encoding")
tabela = pandas.read_csv("clientes.csv", encoding="latin" ,sep=";")

# 2° Visualizar Esses Dados ------------------------------------------------------

# Problemas: Coluna "Unnamed: 8"
tabela = tabela.drop("Unnamed: 8", axis=1)   # Coluna = 1 , Linha = 2
print(tabela)

# 3° Tratar os dados -------------------------------------------------------------

# Análise das tabela
print(tabela.info())

# Valores Com formato errado : Salário está como "object" ( texto ) -> Número
tabela["Salário Anual (R$)"] = pandas.to_numeric(tabela["Salário Anual (R$)"], errors="coerce") # Coerce = Deixa os erros Vazio
print(tabela.info())

# Valores Vazios :
tabela =  tabela.dropna() # Remove TODOS os Vazios
print(tabela.info())

# 4° Análise Inicial -------------------------------------------------------------
print(tabela.describe()) # Médias, Desvio padrão, # que está pra baixo

# 5° Análise Completa - ( Características do cliente ) ---------------------------

# Gráfico Prof x Notas
# grafico = plot.histogram(tabela, x="Profissão",y="Nota (1-100)", histfunc="avg", text_auto=True) # dados, x, y, função do Histograma, exibir valor
# grafico.show() # Exibe na WEB

# # Gráfico Salário x Nota
# grafico = plot.histogram(tabela, x="Salário Anual (R$)",y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10) # dados, x, y, função do Histograma, exibir valor, número de colunas
# grafico.show() 

# Gráficos para cada Coluna x Nota
for coluna in tabela.columns:
    grafico = plot.histogram(tabela, x=coluna,y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    grafico.show()

# RESUMO DA COLETA - Cliente Ideal ---------------------------------------------

# Cliente + 10 anos
# Salário não faz diferença
# Top profissão: Entretenimento, Artista
# Pior profissão: Construção
# Experiência de trabalho: 10 e 15 anos de experiência
# Família: Até 7 pessoas