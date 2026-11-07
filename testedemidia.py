import os
import shutil
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
time.sleep(20)

contatos = ['+558688107169', 'Wilba']
mensagem = 'Olá '
mensagem2 = '. Esse é o último teste de robô pode ignorar, boa noite!'

# 1. Trata o nome do arquivo criando uma cópia com nome simples/limpo
arquivo_original = "˖_𖥔 ݁ @bbiimaii ⁺₊.jpg"
arquivo_temp = "imagem_temp.jpg"

if os.path.exists(arquivo_original):
    shutil.copy(arquivo_original, arquivo_temp)

caminho_midia = os.path.abspath(arquivo_temp)
time.sleep(7)
def buscar_e_enviar(texto_mensagem, contato_nome, texto_mensagem2):
    actions = ActionChains(driver)
    
    # Foca na busca
    actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('/').key_up(Keys.ALT).key_up(Keys.CONTROL).perform()
    time.sleep(1.5)
    
    # Abre o contato
    actions.send_keys(contato_nome).perform()
    time.sleep(2)
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(2)
    
    # Envia o texto
    actions.send_keys(f"{texto_mensagem}{contato_nome}{texto_mensagem2}").perform()
    time.sleep(1)
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(2)

def enviar_midia(caminho_arquivo):
    try:
        # Encontra todos os inputs de arquivo e seleciona o primeiro (mídia/imagens)
        inputs_file = driver.find_elements(By.XPATH, '//input[@type="file"]')
        
        if inputs_file:
            # Injeta a mídia diretamente sem precisar clicar no ícone de clipe/anexo
            inputs_file[0].send_keys(caminho_arquivo)
            time.sleep(3)  # Aguarda a pré-visualização carregar
            
            # Clica no botão verde de enviar ou pressiona ENTER
            try:
                send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
                send_btn.click()
            except:
                # Se não encontrar o botão pelo ícone, simula o ENTER
                actions = ActionChains(driver)
                actions.send_keys(Keys.ENTER).perform()
                
            print("Mídia enviada com sucesso!")
        else:
            print("Input de arquivo não localizado na página.")
            
    except Exception as e:
        print(f"Erro ao enviar mídia: {e}")

# Executa para os contatos
for contato in contatos:
    buscar_e_enviar(mensagem, contato, mensagem2)
    time.sleep(2)
    enviar_midia(caminho_midia)
    time.sleep(3)

# Limpa a imagem temporária ao terminar
if os.path.exists(arquivo_temp):
    os.remove(arquivo_temp)