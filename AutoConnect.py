from pywinauto import application
import time
import os

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
time.sleep(5)

app = application.Application()
app.start(
    'C:\CREON\STARTER\coStarter.exe /prj:cp /id:id /pwd:pwd /pwdcert:pwdcert /autostart')
time.sleep(60)
