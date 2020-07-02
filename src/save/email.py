import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd 
from conf.settings import TABELA
import datetime

def send_email(user,password,from_email=[]):
    # conexão com os servidores do google
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    # username ou email para logar no servidor
    username = user
    password = password
    
    from_addr = user
    to_addrs = from_email
    
    # Create the root message and fill in the from, to, and subject headers
    msg = MIMEMultipart('related')
    msg['Subject'] = 'Análise das ações '+str(datetime.date.today().strftime("%d/%m/%Y"))
    msg['From'] = from_addr
    msg['To'] = ', '.join(to_addrs)
    msg.preamble = 'Segue as acoes do dia '+str(datetime.date.today().strftime("%d/%m/%Y"))+"\n"
    
    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)
    
    msgText = MIMEText('Segue as acoes do dia '+str(datetime.date.today().strftime("%d/%m/%Y"))+"\n")
    msgAlternative.attach(msgText)
    
    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText('<b>Segue tabela com as ações compradas </b>.<br><img src="cid:image1">', 'html')
    msgAlternative.attach(msgText)
    
    file = TABELA
    # This example assumes the image is in the current directory
    fp = open(file, 'rb')
    msgImage = MIMEImage(fp.read(), _subtype="png")
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)
    
    # conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # para interagir com um servidor externo precisaremos
    # fazer login nele
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()