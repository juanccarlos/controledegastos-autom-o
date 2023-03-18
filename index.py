import pyautogui
import time
import pandas as pd
import pyperclip

pyautogui.PAUSE = 1

# abrir o navegador
pyautogui.press('win')
pyautogui.write('chorme')
pyautogui.press('enter')

#entrar na url desejada
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press('enter')

#esperando 5 segundo para carregar a página
time.sleep(5) 

#preenche os campos login, senha e baixa a base de dados
pyautogui.click(x=606, y=384)
pyautogui.write('login')

pyautogui.click(x=667, y=454)
pyautogui.write('senha')

pyautogui.click(x=784, y=533)

time.sleep(3)

pyautogui.click(x=446, y=398)
pyautogui.click(x=830, y=201)
pyautogui.click(x=907, y=598)


#entra e lê a base de dados
tabela = pd.read_csv(r"C:\\Users\\juann\\Downloads\\Compras.csv", sep=';')
print(tabela)

#pega o valor que corresponde a chave
total_gasto = tabela['ValorFinal'].sum()
quantidade = tabela['Quantidade'].sum()
preco_medio = total_gasto / quantidade
print(total_gasto)
print(quantidade)
print(preco_medio)

pyautogui.press('win')
pyautogui.write('chorme')
pyautogui.press('enter')
pyautogui.write('https://mail.google.com/mail/u/0/#inbox')
pyautogui.press('enter')

time.sleep(5)

#envia um Email personalizado
pyautogui.click(x=110, y=191)
pyautogui.write('joedson100os@hotmail.com')
pyautogui.press('tab')

pyautogui.press('tab')
pyperclip.copy('relatório de vendas')
pyautogui.hotkey('ctrl', 'v')

pyautogui.press('tab')


texto = f'''
Segue o relatório de compras

Total Gasto: {total_gasto}
Quantidade de Produtos: {quantidade}
Preço Médio: {preco_medio}

Qualquer dúvida, é só fala.
Att., Juan
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')