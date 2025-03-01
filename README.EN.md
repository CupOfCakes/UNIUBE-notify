# UNIUBE-notify

This software in Python automates tasks related to the UNIUBE portal. It works as follows:

Login Automation: Logs you into your UNIUBE account using your credentials in a secure way.

Web Scraping: Performs scraping on the portal to collect specific information, such as:

Notifications: Uses winotify to alert the user about:

- Classes of the day.
- New messages received.
- Alerts about financial issues.
- New files and online questions released.
- communications.

This software makes life easier for UNIUBE students

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
