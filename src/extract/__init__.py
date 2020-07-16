import urllib.request
from bs4 import BeautifulSoup
import datetime
import pandas as pd

def get_quote(path, inst, cod, value):
    valor_de_compra = value
    data = datetime.date.today()
    
    #Acessando o portal finance do Yahoo
    content = urllib.request.urlopen(path).read()
    soup = BeautifulSoup(content,'lxml')

    abertura = []
    horario = []

    abertura_ =soup.find_all('span', attrs={'class':"Trsdu(0.3s)"})
    horario_ = soup.find_all('div', attrs={'id':'quote-market-notice'})
    
    for a in abertura_:
        abertura.append(a.get_text())

    for hr in horario_:
        horario.append(hr.get_text())

    valor_atual = abertura[0]
    
    #Criando o dataframe
    df = pd.DataFrame({'instituicao':[inst],"codigo": [cod], "data":[data], "horario": [horario[0]],'valor_compra':[valor_de_compra], 'abertura':[float(abertura[3])], 'valor_atual': [float(valor_atual)]})
    
    return df