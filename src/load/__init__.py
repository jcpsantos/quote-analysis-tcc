from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import pandas as pd

def get_quote(path, inst, cod, value, driver):
    valor_de_compra = value
    data = datetime.date.today()
    #Acessando o portal finance do Yahoo
    driver.get(path)
    
    #Coletando os valores
    content = driver.page_source
    soup = BeautifulSoup(content)

    abertura = []
    horario = []

    valor_atual_=soup.find_all('span', attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    abertura_ =soup.find_all('span', attrs={'class':"Trsdu(0.3s)"})
    horario_ = soup.find_all('div', attrs={'id':'quote-market-notice'})
    
    #Carregando os valores
    for va in valor_atual_:
        valor_atual = va.get_text()
    
    for a in abertura_:
        abertura.append(a.get_text())

    for hr in horario_:
        horario.append(hr.get_text())
    
    #Criando o dataframe
    df = pd.DataFrame({'instituicao':[inst],"codigo": [cod], "data":[data], "horario": [horario[0]],'valor_compra':[valor_de_compra], 'abertura':[float(abertura[18])], 'valor_atual': [float(valor_atual)]})
    
    return df