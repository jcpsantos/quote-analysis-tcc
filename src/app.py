from conf.settings import GERDAU_DAY, RUMO_DAY, EMAIL_USER, PASSWORD, EMAIL_FROM, TABELA
import pandas as pd
from extract import get_quote, extract_data_qt
from transformation import variation, bind
from save import save_df_as_image, graph_candlestick
from save.email import send_email
import schedule
import datetime
import time


def main():
    list_days = [0,1,2,3,4]
    hoje = int(datetime.datetime.today().weekday())

    if hoje in list_days:

        #Graficos Candlestick
        df_gerdau_ml = extract_data_qt('GGBR4.SA')
        df_rumo_ml = extract_data_qt('RAIL3.SA')
        graph_candlestick(df_gerdau_ml, 'Gerdau', 'GGBR4')
        graph_candlestick(df_rumo_ml, 'Rumo', 'RAIL3')

        #Dados Gerdau
        path = GERDAU_DAY
        inst = "Gerdau"
        cod = "GGBR4"
        df_gerdau = get_quote(path, inst, cod, 15.57)

        #Dados do Rumo SA
        path = RUMO_DAY
        inst = "Rumo SA"
        cod = 'RAIL3'
        df_rumo = get_quote(path, inst, cod, 23.12)

        df_gerdau = variation(df_gerdau)
        df_rumo = variation(df_rumo)

        df = bind([df_gerdau, df_rumo])

        save_df_as_image(df, TABELA)

        send_email(EMAIL_USER, PASSWORD,EMAIL_FROM)

        print ("Executado com sucesso!")
    else:
        print ("A BV está fechada!")

schedule.every(1).days.at("10:20").do(main)
schedule.every(1).days.at("15:20").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)

