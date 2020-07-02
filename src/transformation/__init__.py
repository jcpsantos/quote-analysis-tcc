import pandas as pd 

def variation (df):
    df['variacao']=df["valor_atual"].sub(df['valor_compra'])
    return df

def bind(dataframes):
    df = pd.concat(dataframes)
    return df