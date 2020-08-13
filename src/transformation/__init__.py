import pandas as pd 
import re
from rich import print

def variation (df):
    df['variacao']=df["atual"].sub(df['compra'])
    return df

def bind(dataframes):
    df = pd.concat(dataframes)
    return df

def horario(val):
    print(val)
    num = re.sub("[A-Za-z]", "", val)
    num = re.sub("\.", "", num)
    return num

def get_predict_df(df, forecast, column):
    df[column] = round(forecast[["yhat"]].tail(1),2).values
    return df