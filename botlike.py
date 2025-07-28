# 1 - Navegar até o site https://www.instagram.com
import webbrowser
import pyautogui
from time import sleep

def logout():
    pyautogui.click(1385, 648, duration=2)
    pyautogui.click(1765, 215, duration=2)
    pyautogui.click(1578, 405, duration=2)
    
while True:
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(1)

    # 2 - Entrar com meu usuário
    pyautogui.click(1699,392,duration=1)
    sleep(1)
    pyautogui.typewrite('devaprender')
    sleep(1)

    # 3 - Entrar com a minha senha
    pyautogui.click(1786,588,duration=1)
    sleep(1)
    pyautogui.typewrite('k4WO%H2#FS%PDRSpL')
    sleep(1)

    # 4 - Clicar em "log in"
    pyautogui.click(1957,655,duration=1)
    sleep(20)

    # 5 - Clicar em "Not now" para não salvar navegador
    pyautogui.click(1690,703,duration=1)
    sleep(20)

    # 6 - fechar janela de "salvar senha"
    pyautogui.click(1562,68,duration=1)
    sleep(1)

    # 7 - Pesquisar pela pagina'
    pyautogui.click(1696,655,duration=1)
    sleep(1)
    pyautogui.typewrite('nike')
    sleep(1)

    # 8 - Entrar na página
    pyautogui.move(0,50,duration=1)
    sleep(1)
    pyautogui.click()
    sleep(20)

    # 9 - Clicar na postagem mais recente
    pyautogui.click(1658,695,duration=1)
    sleep(10)

    # 10 - Verificar se já curti ou não aquela postagem
    coracao = pyautogui.locateCenterOnScreen('coracao.png')
    sleep(1)

    # 11 - Se já tiver curtido, fazer nada, e pausar o bot por 24 horas
    if coracao is not None:
        sleep(86400)

    # 12 - Se não tiver curtido, curtir a foto
    elif coracao == None:
        pyautogui.click(1658,696,duration=1)
        sleep(5)
        # 13 - Se não tiver curtido, comentar na foto
        pyautogui.click(1695,659,duration=1)
        sleep(3)
        pyautogui.click(1698,654,duration=1)
        sleep(1)
        pyautogui.typewrite('Gostei dessa foto!')
        sleep(5)
        pyautogui.click(1695,652,duration=1)

        # 14 - Pausar por 24 horas
        sleep(86400)
