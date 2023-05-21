import pandas
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split    # Para ensinar a IA automaticamente
from sklearn.linear_model import LinearRegression       # Para usar modelo de REGRESSÃO LINEAR
from sklearn.ensemble import RandomForestRegressor      # Para usar modelo de ÁRVORE DE DECISÃO
from sklearn.metrics import r2_score                    # Para conferir a qualidade da PREVISÃO


# 1° Ler base de dados ----------------------------------------------------------------------------------

tabela = pandas.read_csv("barcos_ref.csv")
print(tabela.info(),"\n") # Dados estão ok - Limpos ( números e sem NAN )

# 2° Correlacionar os dados da Tabela --------------------------------------------------------------------

print(tabela.corr()["Preco"])

corr_preco = tabela.corr()[["Preco"]]  # Calculando correlação e exibindo o PREÇO

# 3° Plotar um gráfico -----------------------------------------------------------------------------------

sns.heatmap(corr_preco, cmap="Oranges", annot=True) # Criar com o Seaborn
plt.show()  # Mostrar com Matplot

# 4° Criar I.A -------------------------------------------------------------------------------------------

# Y = Dado a ser PREVISTO
y = tabela["Preco"] 

# X = Dados a serem usados para APRENDER
x = tabela.drop("Preco", axis=1)    # Tudo menos a coluna do preço

# Montar as bases de TREINO
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)   # Precisa ser NESSA ORDEM

# Criar uma I.A com REGRESSÃO e uma com ÁRVORE DE DECISÃO
modelo_regressao = LinearRegression()
modelo_arvore = RandomForestRegressor()

# Passar os dados de Treino
modelo_regressao.fit(x_treino, y_treino)
modelo_arvore.fit(x_treino, y_treino)

# Fazer Previsão de Treino
previsao_regressao = modelo_regressao.predict(x_teste)
previsao_arvore = modelo_arvore.predict(x_teste)

# Comparar precisão da Previsão - r2 score
print("\nResultados r2:")
print("Regressao:",r2_score(y_teste, previsao_regressao))   # Pior
print("Arvore:",r2_score(y_teste, previsao_arvore))         # Melhor

# Plotar precisão ( Para observar )
tabela_aux = pandas.DataFrame()                         # Criar uma nova tabela auxiliar
tabela_aux["y_teste"] = y_teste                         # Adicionar uma coluna nela
tabela_aux["Previsoes Arvore"] = previsao_arvore        # Adicionar uma coluna nela
tabela_aux["Previsoes Regressao"] = previsao_regressao  # Adicionar uma coluna nela

# Cria um gráfico para observar a precisão
sns.lineplot(data = tabela_aux)
plt.show()

# 5° usar para fazer novas previsões --------------------------------------------------------------------
tabela_resultado = pandas.read_csv("novos_barcos.csv")   # Novos dados
previsao = modelo_arvore.predict(tabela_resultado)       # Fazer previsão
tabela_resultado["Valor Previsto"] = pandas.Series([])   # Fazer nova coluna na tabela a ser Exibida
tabela_resultado["Valor Previsto"] = previsao            # Associar os valores da previsão na tabela

# Printar valores previstos
print("\nPrevisoes: ")
for i in previsao:
    print("Previsao:",i)

# Printar tabela
print(tabela_resultado)