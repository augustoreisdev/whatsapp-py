'''automacao de envio de parciais - LIQ'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

resposta = input('Deseja iniciar o código? (Y/N)').upper()
if resposta == 'Y':
    # Abre o Chrome
    chrome_options = Options()
    # chrome_options.add_argument(
    #     "user-data-dir=C:/Users/user_Augusto/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    try:
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=chrome_options)
    except:    
        driver = webdriver.Chrome( options=chrome_options)

    driver.get('https://web.whatsapp.com/')
    element = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]'))
    )

    # Contatos/Grupos - Informar o nome(s) de Grupos ou Contatos que serao enviadas as mensagens
    contatos = ['LIQ - Gestores',
                'LIQ - INTELIGÊNCIA',
                'Gestores TIM e LIQ TSU',
                'LIQ & TSP Gestão',
                'Líderes Varejo | LIQ SPi',
                'LIQ/TIM Reino Varejo TSP']

    # contatos = ['gp regionais',
    #             'gp intelig',
    #              'gp tsu',
    #              'gp tsp gestao',
    #              'gp tsp 1',
    #              'gp tsp 2']

    # Mensagem - Mensagem que sera enviada
    mensagem = 'Parcial de vendas:'

    # Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo
    # no windows o caminho deve ser passado com barra invertida */* )
    regional = ["D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT 1.jpg",
                "D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT 2.jpg",
                "D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO 1.jpg",
                "D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO 2.jpg"]
    supervisor = ["D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT TCN.jpeg",
                  "D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT TNE.jpeg",
                  "D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT TSE.jpeg",
                  "D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT TSP.jpeg",
                  "D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT TSU.jpeg",
                  "D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO TCN.jpeg",
                  "D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO TNE.jpeg",
                  "D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO TSE.jpeg",
                  "D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO TSP.jpeg",
                  "D:/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO TSU.jpeg"]

    # Funcao que pesquisa o Contato/Grupo

    def buscar_contato(contato):
        campo_pesquisa = driver.find_element(
            By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
        sleep(1)
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contato)
        campo_pesquisa.send_keys(Keys.ENTER)
        sleep(2)

    # Funcao que envia a mensagem
    # copyable-text selectable-text
    def enviar_mensagem(mensagem):
        campo_mensagem = driver.find_element(
            By.CSS_SELECTOR, 'p.selectable-text')
        campo_mensagem.click()
        sleep(1)
        campo_mensagem.send_keys(str(mensagem))
        campo_mensagem.send_keys(Keys.ENTER)

    # Funcao que envia midia como mensagem

    def enviar_midia(midia):
        driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
        sleep(2.2)
        attach = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        attach.send_keys(midia)
        espera1 = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "span[data-icon='send']"))
        )
        send = driver.find_element(By.CSS_SELECTOR, "span[data-icon='send']")
        send.click()

    # Percorre todos os contatos/Grupos e envia as mensagens
    for contato in contatos:
        # parcial regional grupo gestores
        if contato == contatos[0]:
            buscar_contato(contato)
            enviar_mensagem(mensagem)
            enviar_midia("\n".join(regional))
            sleep(1)

        # todas as imagens de supervisor no inteligencia
        elif contato == contatos[1]:
            buscar_contato(contato)
            enviar_mensagem(mensagem)
            enviar_midia('\n'.join(supervisor))
            sleep(1)
        elif contato == contatos[2]:  # supervisor tsu varejo e out
            buscar_contato(contato)
            enviar_mensagem(mensagem)
            enviar_midia(supervisor[4] + '\n' + supervisor[9])
            sleep(1)
        elif contato == contatos[3]:  # supervisor tsp varejo e out
            buscar_contato(contato)
            enviar_mensagem(mensagem)
            enviar_midia(supervisor[3] + '\n' + supervisor[8])
            sleep(1)
        # supervisor tsp varejo
        elif contato == contatos[4] or contato == contatos[5]:
            buscar_contato(contato)
            enviar_mensagem(mensagem)
            enviar_midia(supervisor[8])
            sleep(1)
    sleep(10)
    driver.quit()
else:
    print('Obrigado por usar o código')
