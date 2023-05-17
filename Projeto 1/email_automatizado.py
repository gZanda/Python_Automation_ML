# 1° acessar o sistema da empresa
# 2° Login no sistema - https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema
# 3° Baixa o .CSV
# 4° Calcular Indicadores
# 5° Enviar um Email

# Comandos mais usados:
# pyautogui.click(x,y,clicks=quantidade,button="left"/"right")   -> Clica
# pyautogui.write   -> Escreve
# pyautogui.press   -> Tecla única 
# pyautogui.hotkey  -> Combinação de Teclas
# pyautogui.drag    -> Arrasta
# pyautogui.scroll  -> Scroll

# Como Descobrir a posição do Mouse para Clicar ?
# time.sleep(3)
# print(pyautogui.position())
# time.sleep(60)

# Lembrar de MAXIMIZAR a janela se precisar 

# PYPERCLIP - Copia textos DO PRÓPRIO CÓDIGO

#-------------------------------------------------------------------------------------------

# MEDIDAS DO MOUSE = TELA DIVIDIDA - BROWSER NA ESQUERDA

# pyautogui - Automação MOUSE & TECLADO
import pyautogui, time, pandas, pyperclip

# Testar Click
# time.sleep(3)
# print(pyautogui.position())
# time.sleep(100)

pyautogui.PAUSE = 0.5 # Pausa de 1 Seg para cada comando

# 1° -------------------------------------

# pyautogui.press("win")
# pyautogui.write("brave")
# pyautogui.press("enter")

pyautogui.hotkey("alt","tab")
pyautogui.hotkey("ctrl","t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

#2° -------------------------------------

# Pausa para o Site carregar
time.sleep(3)   # "Pausa" de 5 seg nesse local do código apenas

pyautogui.press("tab")
pyautogui.write("ZaaZ Python Master")
pyautogui.press("tab")
pyautogui.write("Senha Foda")
pyautogui.press("tab")
pyautogui.press("enter")
# OU - pyautogui.click(x=465,y=461)

#3° -------------------------------------

time.sleep(3)
pyautogui.click(x=385,y=385,button="right")
time.sleep(1)
pyautogui.click(x=506,y=761)
time.sleep(5)   # Pausa de Verificação do DRIVE
pyautogui.press("enter")
time.sleep(5)   # Pausa de Download

#4° -------------------------------------

# Ler CSV
tabela = pandas.read_csv(r"C:\Users\Zanda\Desktop\Compras.csv", sep=";")

# Somar Valores Finais
gasto = tabela["ValorFinal"].sum()

# Somar Quantidade
quantidade = tabela["Quantidade"].sum()

# Preço médio
medio = gasto/quantidade

# 5° -------------------------------------

texto = f"""Prezados,

Segue o relatório de compras :)

Total Gasto: R${gasto:,.2f}
Quantidade de Produtos: R${quantidade:,.2f}
Preço Médio: R${medio:,.2f}

Agradeço :)
"""

pyautogui.hotkey("ctrl","t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=44,y=166)
time.sleep(2)   
pyautogui.write("gabriel.goncalves@estudante.ufla.br")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("Automatic Py")
pyautogui.press("tab")

pyperclip.copy(texto)           # Copiar o texto da variável para o "CTRL C"
pyautogui.hotkey("ctrl","v")    # Cola
pyautogui.hotkey("ctrl","enter")
