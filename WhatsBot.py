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

resposta = input('type Y for defalut, T for testing').upper()

if resposta == 'Y':
    # Contatos/Grupos - Informar o nome(s) de Grupos ou Contatos que serao enviadyas as mensagens
    contatos = ['Ability - Gestores',
                'ABILITY - INTELIGÊNCIA',
                'Gestão TIM + Ability TSU',
                'Líderes Multi | Ability TSP',
                'Ability/Tim Reino Multi',
                'OUT Ability | TSP']
elif resposta == 'T':
    contatos = ['gp regionais',
                'gp intelig',
                 'gp tsu',
                 'gp tsp gestao',
                 'gp tsp 1',
                 'gp tsp 2']
else:
    print('Obrigado por usar o código')

# Abre o Chrome
chrome_options = Options()
chrome_options.add_argument(
    "user-data-dir=C:/Users/AUGUSTO/AppData/Local/Google/Chrome/User Data")
chrome_options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])
try:
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
except:    
    print("usando arquivo local")
    driver = webdriver.Chrome( options=chrome_options, executable_path='chromedriver')

driver.get('https://web.whatsapp.com/')

element = WebDriverWait(driver, 90).until(
    EC.presence_of_element_located(
        (By.ID, 'side'))
)
sleep(3)




# Mensagem - Mensagem que sera enviada
mensagem = 'Parcial de vendas:'

# Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo
# no windows o caminho deve ser passado com barra invertida */* )
regional = ["G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT 1.jpg",
            "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT 2.jpg",
            "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO 1.jpg",
            "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO 2.jpg"]
supervisor = [  "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT TCN.jpeg",
                "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT TNE.jpeg",
                "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT TSE.jpeg",
                "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT TSP.jpeg",
                "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/OUT TSU.jpeg",
                "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO TCN.jpeg",
                "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO TNE.jpeg",
                "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO TSE.jpeg",
                "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO TSP.jpeg",
                "G:/Meu drive/LIQ/PARCIAL DE VENDAS/IMAGENS PARCIAL/VAREJO TSU.jpeg"]

# Funcao que pesquisa o Contato/Grupo

def buscar_contato(contato):
    campo_pesquisa = driver.find_element(
        By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    sleep(1)

# Funcao que envia a mensagem
# copyable-text selectable-text
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    campo_mensagem.click()
    sleep(1)
    campo_mensagem.send_keys(str(mensagem)+Keys.ENTER)
    # campo_mensagem.send_keys(Keys.ENTER)

# Funcao que envia midia como mensagem

def enviar_midia(midia):
    driver.find_element(By.CSS_SELECTOR, "span[data-icon='attach-menu-plus']").click()
    sleep(2.2)
    attach = driver.find_element(By.CSS_SELECTOR, "input[accept='image/*,video/mp4,video/3gpp,video/quicktime']")
    attach.send_keys(midia)
    espera1 = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "span[data-icon='send']"))
    )
    sleep(0.5)
    send = driver.find_element(By.CSS_SELECTOR, "span[data-icon='send']")
    send.click()
    sleep(3)

# Percorre todos os contatos/Grupos e envia as mensagens    
for contato in contatos:
    # parcial regional grupo gestores
    if contato == contatos[0]:
        
        buscar_contato(contato)
        enviar_mensagem(mensagem)
        enviar_midia("\n".join(regional))

    # todas as imagens de supervisor no inteligencia
    elif contato == contatos[1]:
        buscar_contato(contato)
        enviar_mensagem(mensagem)
        enviar_midia('\n'.join(supervisor))
        sleep(2)
       
    elif contato == contatos[2]:  # supervisor tsu varejo e out
        buscar_contato(contato)
        enviar_mensagem(mensagem)
        enviar_midia(supervisor[4] + '\n' + supervisor[9])


    # supervisor tsp varejo
    elif contato == contatos[3] or contato == contatos[4]:
        buscar_contato(contato)
        enviar_mensagem(mensagem)
        enviar_midia(supervisor[8])
    elif contato == contatos[5]:  # supervisor tsp  out
        buscar_contato(contato)
        enviar_mensagem(mensagem)
        enviar_midia(supervisor[3])
        
sleep(10)
driver.quit()
