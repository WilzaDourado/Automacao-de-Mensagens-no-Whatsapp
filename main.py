from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://web.whatsapp.com/')

print("Aguardando 20 segundos para escaneamento do QR Code...")
time.sleep(20) # Dê tempo suficiente para logar e a tela carregar completamente

contatos = ['Wilba']
mensagem = 'Bom dia '

def buscar_e_enviar(contato_nome, texto_mensagem):
    actions = ActionChains(driver)
    
    # 1. Pressiona o atalho do WhatsApp Web para focar na pesquisa (Ctrl + Alt + /)
    actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('/').key_up(Keys.ALT).key_up(Keys.CONTROL).perform()
    time.sleep(1.5)
    
    # 2. Digita o nome do contato e dá ENTER para abrir a conversa
    actions.send_keys(contato_nome).perform()
    time.sleep(2)
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(2)
    
    # 3. Digita a mensagem (o foco vai direto para o chat) e envia
    actions.send_keys(f"{texto_mensagem}{contato_nome}").perform()
    time.sleep(1)
    actions.send_keys(Keys.ENTER).perform()

# Executa o loop
for contato in contatos:
    buscar_e_enviar(contato, mensagem)
    time.sleep(2)