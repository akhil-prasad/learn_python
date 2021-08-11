import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr="email address of the sender"
toaddr="Email address of the reciever"
msg=MIMEMultipart()
msg['From']=fromaddr
msg['To']=toaddr
msg['Subject']="subject of the mail"
body="Body of the mail"

msg.attach(MIMEText(body,'plain'))
filename='chat.txt'
attachment=open('D:\PYTHON\chat.txt','rb')
p=MIMEBase('application','octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('content-Dispositon',"attachment; filename= %s" %filename)
msg.attach(p)

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('prasadakhil414@gmail.com', 'quest@123')
message= "good morning"

s.sendmail("prasadakhil414@gmail.com", 'agilpkv@gmail.com', message)
print("Message send successful")
s.quit()
