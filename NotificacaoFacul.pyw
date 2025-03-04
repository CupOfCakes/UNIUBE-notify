from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from winotify import Notification
from pygame import mixer
import time

# configura o navegador
options = Options()
options.add_argument("--headless")  # Modo headless
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/91.0.4472.124 Safari/537.36")

# Inicializa o navegador
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service, options=options)

# abre e loga no ava
navegador.get("https://ava.uniube.br/login/")
navegador.find_element('xpath', '//*[@id="usuarioLogin"]').send_keys("SEU RA")
navegador.find_element('xpath', '//*[@id="senhaView"]').send_keys("SUA SENHA")
navegador.find_element('xpath', '//*[@id="loginPage"]/div[3]/form/div[3]/div[1]/button').click()

try:
    navegador.find_element('xpath', '//*[@id="DIV_ANDAMENTO"]/div/div/div/div[2]/div[2]/button/span').click()
except:
    pass

while True:
    try:
        navegador.find_element('xpath', '//*[@id="Botoes"]/a[2]').click()
    except:
        break

while True:
    try:
        time.sleep(4)
        navegador.find_element('xpath', '//*[@id="acessar"]/button').click()
    except:
        break

# pega o valor da mensalidade a pagar e data limite
try:
    mensalidade = navegador.find_element(By.XPATH, '//*[@id="info_financeiro"]/div[2]/div/span[2]/span').text
    limite = navegador.find_element(By.XPATH, '//*[@id="info_financeiro"]/div[2]/div/span[1]').text

    NMens = Notification(app_id="UNIUBE", title="Mensalidade Uniube", msg=f"valor:{mensalidade}\nvencimento:{limite}", )
except:
    mensalidade = navegador.find_element(By.XPATH, '//*[@id="info_financeiro"]/div[2]/span').text
    NMens = Notification(app_id="UNIUBE", title="Mensalidade Uniube", msg=f"{mensalidade}", )


# pega os comunicados e soma
ComunicadoUniube = int(navegador.find_element(By.XPATH, '//*[@id="info_comunicacao"]/div[2]/div[1]/span[2]').text)
ComunicadoCurso = int(navegador.find_element(By.XPATH, '//*[@id="info_comunicacao"]/div[2]/div[2]/span[2]').text)

try:
    ComunicadoTiraDuvidas = int(navegador.find_element(By.XPATH, '//*[@id="info_comunicacao"]/div[2]/div[3]/span[2]').text)
except:
    ComunicadoTiraDuvidas = 0
    ferias = True

comunicacoes = ComunicadoUniube + ComunicadoTiraDuvidas + ComunicadoCurso

# pega os comunicados do sae e soma
SaeComplementar = int(navegador.find_element(By.XPATH, '//*[@id="info_sae"]/div[2]/div[1]/span[2]').text)
SaeFBParcial = int(navegador.find_element(By.XPATH, '//*[@id="info_sae"]/div[2]/div[1]/span[2]').text)
SaeFinalizado = int(navegador.find_element(By.XPATH, '//*[@id="info_sae"]/div[2]/div[1]/span[2]').text)

sae = SaeComplementar + SaeFinalizado + SaeFBParcial

# pega os arquivos e questões não visualizados
try:
    arquivos = int(navegador.find_element(By.XPATH, '//*[@id="info_arquivos"]/div[2]/span[1]').text)
except:
    arquivos = 0

QuestD = int(navegador.find_element(By.XPATH, '//*[@id="info_acqa"]/div[2]/span[1]').text)
QuestO = int(navegador.find_element(By.XPATH, '//*[@id="info_acqf"]/div[2]/span[1]').text)


# informações das aulas
try:
    aula1 = navegador.find_element(By.XPATH, '//*[@id="info_aulas_hoje"]/div[2]/div[2]/div[1]/h2').text
    sala1 = navegador.find_element(By.XPATH, '//*[@id="info_aulas_hoje"]/div[2]/div[2]/div[2]/div[1]/span').text

    try:
        navegador.find_element('xpath', '//*[@id="prox_aula"]/i').click()
    
        aula2 = navegador.find_element(By.XPATH, '//*[@id="info_aulas_hoje"]/div[2]/div[3]/div[1]/h2').text
        sala2 = navegador.find_element(By.XPATH, '//*[@id="info_aulas_hoje"]/div[2]/div[3]/div[2]/div[1]/span').text
    
        NAul = Notification(app_id="UNIUBE", title="Aulas hoje", msg=f"1 horario: {aula1}\n"
                                                                     f"{sala1}\n"
                                                                     f"2 horario: {aula2}\n"
                                                                     f"{sala2}\n")
    except:
        NAul = Notification(app_id="UNIUBE", title="Aulas hoje", msg=f"1 horario: {aula1}\n"
                                                                     f"{sala1}\n")
except:
    NAul = Notification(app_id="UNIUBE", title="Aulas hoje", msg="Sem aulas hoje")

# faz os pop ups
NMens.add_actions(label="ir ao site", launch="https://ava.uniube.br/login/")
NComu = Notification(app_id="UNIUBE", title="Comunicados", msg=f"Novos comunicados: {comunicacoes}")
NComu.add_actions(label="ir ao site", launch="https://ava.uniube.br/login/")
NSae = Notification(app_id="UNIUBE", title="SAE", msg=f"Comunicados do SAE: {sae}")
NSae.add_actions(label="ir ao site", launch="https://ava.uniube.br/login/")
NNew = Notification(app_id="UNIUBE", title="Arquivos e Questões", msg=f"Novos arquivos: {arquivos}\n"
                                                                      f"Questões fechadas: {QuestO}\n"
                                                                      f"Questões Abertas: {QuestD}")
NNew.add_actions(label="ir ao site", launch="https://ava.uniube.br/login/")

NAul.add_actions(label="ir ao site", launch="https://ava.uniube.br/login/")

# mostra os pop ups
NMens.show()
time.sleep(1)

NComu.show()
time.sleep(1)

NSae.show()
time.sleep(1)

NNew.show()
time.sleep(1)

NAul.show()

# roda um som
mixer.init()
mixer.music.load(r"HK notify.mp3") #se o arquivo de audio não estiver na mesma pasta deste arquivo, coloque o caminho do audio
mixer.music.play()

while mixer.music.get_busy():
    pass
