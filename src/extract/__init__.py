import urllib.request
from bs4 import BeautifulSoup
import datetime
import pandas as pd
from retrying import retry
import pandas_datareader.data as web
import yfinance as yf
from rich import print

@retry(stop_max_attempt_number=7, wait_fixed = 2000)
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
    try:
        df = pd.DataFrame({'instituicao':[inst],"codigo": [cod], "data":[data], "horario": [horario[0]],'compra':[valor_de_compra], 'abertura':[float(abertura[3])], 'atual': [float(valor_atual)]})
    except:
        df = pd.DataFrame({'instituicao':[inst],"codigo": [cod], "data":[data], "horario": [horario[0]],'compra':[valor_de_compra], 'abertura':[float(abertura[12])], 'atual': [float(abertura[9])]})
    
    print("[bold]Dataframe [green]{0} [/green]criado!".format(inst))
    return df

def extract_data_qt(quote):
    yf.pdr_override()
    df = web.get_data_yahoo(quote, period='5y')
    return df

__all__ = ['get_quote', 'extract_data_qt']