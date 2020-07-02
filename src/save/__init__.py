import imgkit
import pandas as pd 

def save_df_as_image(df, path):
    imgkit.from_string(df.to_html(), path)