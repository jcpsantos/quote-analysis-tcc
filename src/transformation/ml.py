import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
from fbprophet import Prophet
import datetime as dt
import warnings

warnings.filterwarnings("ignore")

def fit_model(df):
    df = df[['Close']]
    df['ds'] = df.index
    df = df.rename(columns={"Close": "y"})
    
    m = Prophet(interval_width=0.95, yearly_seasonality=True, weekly_seasonality=True, changepoint_prior_scale=2, daily_seasonality=True)
    m.add_country_holidays(country_name='BR')
    m.add_seasonality(name='monthly', period=30.5, fourier_order=5, prior_scale=0.02)
    m.fit(df)
    
    return m

def pred_model(m, period):
    future = m.make_future_dataframe(periods=period)
    future = future[future['ds'].dt.dayofweek < 5]
    forecast = m.predict(future)
    return forecast