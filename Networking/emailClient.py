import smtplib
from email.mime.text import MIMEText

body = "This is a test email from Python application"

msg = MIMEText(body)
msg["from"] = "boyanapalliakhil45@gmail.com"
msg["to"] = "boyanapalliakhil45@gmail.com"
msg["Subject"] = "Hy"

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("boyanapalliakhil45@gmail.com","sildfpglthfwyhln")

server.send_message(msg)

print("Mail Sent")

server.quit()