# UNIUBE-notify

Descrição em português:
Este software em Python automatiza tarefas relacionadas ao portal da UNIUBE. Ele funciona da seguinte forma:

Automação de Login: Faz login na sua conta da UNIUBE utilizando suas credenciais de forma segura.

Web Scraping: Realiza scraping no portal para coletar informações específicas, como:

Notificações: Utiliza o winotify para alertar o usuário sobre:

Aulas do dia.
Novas mensagens recebidas.
Alerta de pendências financeiras.
Novos arquivos e questões onlines lançados.
Comunicados.

Esse software serve para facilitar a vida dos estudante da UNIUBE
segue como configurar em português e em ingles
# Description in English:
This software in Python automates tasks related to the UNIUBE portal. It works as follows:

Login Automation: Logs you into your UNIUBE account using your credentials in a secure way.

Web Scraping: Performs scraping on the portal to collect specific information, such as:

Notifications: Uses winotify to alert the user about:

Classes of the day.
New messages received.
Alerts about financial issues.
New files and online questions released.
communications.

This software makes life easier for UNIUBE students
here's how to set it up in Portuguese and English

-------------------------------------------------------------------------------------------------
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



# 📌 Step-by-step configuration

1️⃣ Python file configuration (.pyw)

In the NotificacaoFacul.pyw file, you will need to enter your credentials.

Open the .pyw file in any code editor (e.g. PyCharm, VS Code, Notepad++).

Go to lines 26 and 27 and replace them with your data:

your_ra = “YOUR_RA_HERE”
your_password = “YOUR_PASSWORD_HERE”

2️⃣ Batch file configuration (.bat)

The file run_notification.bat is used to run the Python script automatically.

Open the .bat file in a text editor.

Add the path of the installed Python and the path of the .pyw file.

To find the Python path, open Command Prompt (CMD) and run:

where python

Replace the .bat with the correct path:

C:\Caminho\Para\Python.exe C:\Caminho\Para\NotificacaoFacul.pyw

3️⃣ XML file configuration

The file notificacao_task.xml is used to schedule the task in Windows Task Scheduler.

Open the .xml file in a text editor.

Set the start date and time:

Line 14: Choose the day and time that the script will start running daily.

<StartBoundary>YYYY-MM-DDTHH:MM:SS</StartBoundary>

Example: To start on February 26, 2025 at 12:00:

<StartBoundary>2025-02-26T12:00:00</StartBoundary>

Optional: Schedule a second time slot on the same day:

Line 22: Set up a second schedule if necessary.

<StartBoundary>2025-02-26T16:30:00</StartBoundary>

Set the path of the .bat file:

Line 27: Replace with the correct path of your .bat file.

<Command>C:\Caminho\Para\rodar_notificacao.bat</Command>

Line 31: Remove the comment symbols to activate this setting if you are using a notebook or any battery-powered device.

<!-- <DontStopIfGoingOnBatteries>true</DontStopIfGoingOnBatteries> -->

✅ Importing the Task into the Windows Scheduler

After configuring the XML file, follow the steps to import it:

Open the Task Scheduler in Windows (taskschd.msc).

In the right-hand pane, click Import Task....

Select the notification_task.xml file and click Open.

Check the settings and click OK.
