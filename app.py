import pyautogui

import webbrowser

# 1) Navegue até o site https://cursoautomacao.netlify.app/

webbrowser.open('https://cursoautomacao.netlify.app/')

# 2) Encontre e clique no campo "Digite seu nome" dentro de 
# "exemplos Alertas" e digite seu nome

pyautogui.moveTo(1187,285, duration=2)
pyautogui.scroll(-2500)
pyautogui.click(1282,197, duration=3)
pyautogui.write('Douglas Santiago')


# 3) Clique em alerta, para gerar a alerta

pyautogui.click(1056,245, duration=3)

# 4) Feche a alerta
pyautogui.click(1641,220, duration=3)

# 5) Suba a página totalmente para cima

pyautogui.scroll(2500)

# 6) Desça apenas o suficiente para conseguir chegar até a secção 
# que contém os arquivos para o quais irá fazer o download e click 
# no botão de download para realizar
# o downlaod dos arquivos excel e pdf.

pyautogui.scroll(-3800)
pyautogui.click(1185,357, duration=1)
pyautogui.click(1180,497, duration=1)

# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert('Você terminou')



