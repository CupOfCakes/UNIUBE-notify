# UNIUBE-notify

Este software em Python automatiza tarefas relacionadas ao portal da UNIUBE. Ele funciona da seguinte forma:

Automação de Login: Faz login na sua conta da UNIUBE utilizando suas credenciais de forma segura.

Web Scraping: Realiza scraping no portal para coletar informações específicas, como:

Notificações: Utiliza o winotify para alertar o usuário sobre:

- Aulas do dia.
- Novas mensagens recebidas.
- Alerta de pendências financeiras.
- Novos arquivos e questões onlines lançados.
- Comunicados.

Esse software serve para facilitar a vida dos estudante da UNIUBE

# 📌 Configuração Passo a Passo

1️⃣ Configuração do Arquivo Python (.pyw)

No arquivo NotificacaoFacul.pyw, você precisará inserir suas credenciais.

Abra o arquivo .pyw em qualquer editor de código (exemplo: PyCharm, VS Code, Notepad++).

Vá até as linhas 26 e 27 e substitua pelos seus dados:

sua_ra = "SEU_RA_AQUI"
sua_senha = "SUA_SENHA_AQUI"

2️⃣ Configuração do Arquivo Batch (.bat)

O arquivo rodar_notificacao.bat serve para executar o script Python automaticamente.

Abra o arquivo .bat em um editor de texto.

Adicione o caminho do Python instalado e o caminho do arquivo .pyw.

Para encontrar o caminho do Python, abra o Prompt de Comando (CMD) e execute:

where python

Substitua no .bat com o caminho correto:

C:\Caminho\Para\Python.exe C:\Caminho\Para\NotificacaoFacul.pyw

3️⃣ Configuração do Arquivo XML

O arquivo notificacao_task.xml é usado para agendar a tarefa no Windows Task Scheduler.

Abra o arquivo .xml em um editor de texto.

Defina a data e horário de início:

Linha 14: Escolha o dia e a hora que o script começará a rodar diariamente.

<StartBoundary>AAAA-MM-DDTHH:MM:SS</StartBoundary>

Exemplo: Para iniciar em 26 de fevereiro de 2025 às 12:00:

<StartBoundary>2025-02-26T12:00:00</StartBoundary>

Opcional: Agendar um segundo horário no mesmo dia:

Linha 22: Configure um segundo horário, se necessário.

<StartBoundary>2025-02-26T16:30:00</StartBoundary>

Definir o caminho do arquivo .bat:

Linha 27: Substitua pelo caminho correto do seu arquivo .bat.

<Command>C:\Caminho\Para\rodar_notificacao.bat</Command>

Linha 31: Remova os símbolos de comentário para ativar esta configuração caso esteja usando um notebook ou qualquer dispositivo alimentado por bateria.

<!-- <DontStopIfGoingOnBatteries>true</DontStopIfGoingOnBatteries> -->

✅ Importando a Tarefa no Agendador do Windows

Após configurar o arquivo XML, siga os passos para importá-lo:

Abra o Agendador de Tarefas no Windows (taskschd.msc).

No painel à direita, clique em Importar Tarefa....

Selecione o arquivo notificacao_task.xml e clique em Abrir.

Verifique as configurações e clique em OK.
