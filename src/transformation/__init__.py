import pandas as pd 
import re
from rich import print

def variation (df):
    df['variacao']=df["valor_atual"].sub(df['valor_compra'])
    return df

def bind(dataframes):
    df = pd.concat(dataframes)
    return df

def horario(val):
    print(val)
    num = re.sub("[A-Za-z]", "", val)
    num = re.sub(":", "", num, 1)
    return num