import os

from dotenv import load_dotenv

load_dotenv()

GERDAU_DAY = os.getenv("GERDAU_DAY")
RUMO_DAY = os.getenv("RUMO_DAY")
MARFRIG_DAY = os.getenv("MARFRIG_DAY")
EMAIL_USER = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("PASSWORD")
EMAIL_FROM = [os.getenv("EMAIL_FROM1"), os.getenv('EMAIL_USER')]
TABELA = os.getenv("TABELA")
GRAFICO = os.getenv("GRAFICO")