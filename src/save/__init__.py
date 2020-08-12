from conf.settings import GRAFICO
import imgkit
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from rich import print

def save_df_as_image(df, path):
    imgkit.from_string(df.to_html(), path)
    print ("[bold]Tabela salva! :smiley:")

def graph_candlestick(df, title, name):
    month = datetime.today().month - 1
    year = datetime.today().year
    
    df = df[df.index.year == year]
    df = df[df.index.month >= month]
    
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

    fig.update_layout(
        title=title+" - "+name)

    image = "graph_{0}.png".format(name)
    fig.write_image(GRAFICO+image)
    print ("Gráfico [bold][green] {0} [/bold][/green] salvo com sucesso! [green bold]:tada:".format(name))
