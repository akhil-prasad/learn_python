import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('prasadakhil414@gmail.com', 'quest@123')
message= "good morning"

s.sendmail("prasadakhil414@gmail.com", 'akhilprasad194@gmail.com', message)
print("Message send successful")
s.quit()
