from conf.settings import GERDAU_DAY, RUMO_DAY, EMAIL_USER, PASSWORD, EMAIL_FROM, TABELA, MARFRIG_DAY
import pandas as pd
from extract import get_quote, extract_data_qt
from transformation import variation, bind, horario, get_predict_df
from transformation.ml import pred_model, fit_model         
from save import save_df_as_image, graph_candlestick
from save.email import send_email
from rich import print
import schedule
import datetime
import time
import warnings

warnings.filterwarnings("ignore")


def main():
    list_days = [0,1,2,3,4]
    hoje = int(datetime.datetime.today().weekday())

    if hoje in list_days:

        #Graficos Candlestick
        df_gerdau_ml = extract_data_qt('GGBR4.SA')
        df_rumo_ml = extract_data_qt('RAIL3.SA')
        df_marfrig_ml = extract_data_qt('MRFG3.SA')
        graph_candlestick(df_gerdau_ml, 'Gerdau', 'GGBR4')
        graph_candlestick(df_rumo_ml, 'Rumo', 'RAIL3')
        graph_candlestick(df_marfrig_ml, 'Marfrig', 'MRFG3')

        #Dados Gerdau
        path = GERDAU_DAY
        inst = "Gerdau"
        cod = "GGBR4"
        df_gerdau = get_quote(path, inst, cod, 15.57)

        #Dados do Rumo SA
        path = RUMO_DAY
        inst = "Rumo"
        cod = 'RAIL3'
        df_rumo = get_quote(path, inst, cod, 23.12)

        #Dados do Rumo SA
        path = MARFRIG_DAY
        inst = "Marfrig"
        cod = 'MRFG3'
        df_marfrig = get_quote(path, inst, cod, 14.43)

        df_gerdau = variation(df_gerdau)
        df_rumo = variation(df_rumo)
        df_marfrig = variation(df_marfrig)

        ml_gerdau = fit_model(df_gerdau_ml)
        print ("Modelo [green]Gerdau[/green] treinado")
        ml_rumo = fit_model(df_rumo_ml)
        print ("Modelo [green]Rumo[/green] treinado")
        ml_marfrig = fit_model(df_marfrig_ml)
        print ("Modelo [green]Marfrig[/green] treinado")
        models = [ml_gerdau, ml_rumo, ml_marfrig]

        try:
            fct_gerdau30 = pred_model(ml_gerdau, 30)
            fct_rumo30 = pred_model(ml_rumo, 30)
            fct_marfrig30 = pred_model(ml_marfrig, 30)

            fct_gerdau365 = pred_model(ml_gerdau, 365)
            fct_rumo365 = pred_model(ml_rumo, 365)
            fct_marfrig365 = pred_model(ml_marfrig, 365)

            df_gerdau = get_predict_df(df_gerdau, fct_gerdau30, "+30d")
            df_gerdau = get_predict_df(df_gerdau, fct_gerdau365, "+365d")
            print ("Predição [green]Gerdau[/green] concluida")
            df_rumo = get_predict_df(df_rumo, fct_rumo30, "+30d")
            df_rumo = get_predict_df(df_rumo, fct_rumo365, "+365d")
            print ("Predição [green]Rumo[/green] concluida")
            df_marfrig = get_predict_df(df_marfrig, fct_marfrig30, "+30d")
            df_marfrig = get_predict_df(df_marfrig, fct_marfrig365, "+365d")
            print ("Predição [green]Marfrig[/green] concluida")
        except:
            print("[bold red]Predição não realizada")

        df = bind([df_gerdau, df_rumo, df_marfrig])
        df['horario'] = df[['horario']].applymap(horario)

        save_df_as_image(df, TABELA)

        send_email(EMAIL_USER, PASSWORD,EMAIL_FROM)

        print ("[green]Executado com sucesso!")
    else:
        print ("[yellow]A BV está fechada!")

schedule.every(1).days.at("10:20").do(main)
schedule.every(1).days.at("15:20").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)

