# faz o selenium funcionar e abrir o google
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from winotify import Notification

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

ferias = False

# abre e loga no ava
navegador.get("https://ava.uniube.br/login/")
navegador.find_element('xpath', '//*[@id="usuarioLogin"]').send_keys("SEU RA")
navegador.find_element('xpath', '//*[@id="senhaView"]').send_keys("SUA SENHA")
navegador.find_element('xpath', '//*[@id="loginPage"]/div[3]/form/div[3]/div[1]/button').click()
try:
    navegador.find_element('xpath', '//*[@id="Botoes"]/a[2]').click()
except:
    pass

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
if not ferias:
    arquivos = int(navegador.find_element(By.XPATH, '//*[@id="info_arquivos"]/div[2]/span[1]').text)
else:
    arquivos = 0

QuestD = int(navegador.find_element(By.XPATH, '//*[@id="info_acqa"]/div[2]/span[1]').text)
QuestO = int(navegador.find_element(By.XPATH, '//*[@id="info_acqf"]/div[2]/span[1]').text)


# informações das aulas
try:
    aula1 = navegador.find_element(By.XPATH, '//*[@id="info_aulas_hoje"]/div[2]/div[2]/div[1]/h2').text
    sala1 = navegador.find_element(By.XPATH, '//*[@id="info_aulas_hoje"]/div[2]/div[2]/div[2]/div[1]/span').text

    navegador.find_element('xpath', '//*[@id="prox_aula"]/i').click()

    aula2 = navegador.find_element(By.XPATH, '//*[@id="info_aulas_hoje"]/div[2]/div[3]/div[1]/h2').text
    sala2 = navegador.find_element(By.XPATH, '//*[@id="info_aulas_hoje"]/div[2]/div[3]/div[2]/div[1]/span').text

    NAul = Notification(app_id="UNIUBE", title="Aulas hoje", msg=f"1 horario: {aula1}\n"
                                                                 f"{sala1}\n"
                                                                 f"2 horario: {aula2}\n"
                                                                 f"{sala2}\n")
except:
    NAul = Notification(app_id="UNIUBE", title="Aulas hoje", msg="Sem aulas hoje")

# faz um pop up

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
NComu.show()
NSae.show()
NNew.show()
NAul.show()
