from email.message import MIMEPart
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr ="email of the sender "
toaddr="email address of the reciever"
msg=MIMEMultipart()
msg['From']= fromaddr
msg['To']=toaddr
msg['subject']="subject of the mail"
body="body of the mail"
msg.attach(MIMEText(body,'plain'))
filename="akhil.py"
attachment = open("D:\PYTHON", "rb")
p=MIMEBase('application','octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('content-Disposition',"attachment; filename= %s",filename)
msg.attach(p)


import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('prasadakhil414@gmail.com', 'quest@123')
message= "good morning"

s.sendmail("prasadakhil414@gmail.com", 'akhilprasad194@gmail.com', message)
print("Message send successful")
s.quit()

