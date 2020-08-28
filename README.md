# Quote Analysis
Projeto de analises de investimentos

Esse projeto realiza uma analise das ações GGBR4 (Gerdau), RAIL3 (Rumo) e MRFG3 (Marfrig) onde foi realizada uma analise exploratoria dessas ações utilizando a biblioteca **Yfinance** para recuperar os dados históricos dessas ações e em cima disso criado um relatório/dashboard utilizando o <a href="https://datastudio.google.com/">Data Studio</a>, também é realizado um relatório diário onde é realizado um webscrapping dos dados mais atualizados no site da <a href="https://finance.yahoo.com/">Yahoo Finance</a> e os dados enviados por e-mail. 
Também faz parte desse projeto a utilização de machine learning para verificar as tendências dessas ações no curto e longo prazo. 

## Bibliotecas Importantes 
- <a href="https://pandas.pydata.org/docs/">Pandas</a>
- <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup</a>
- <a href="https://pypi.org/project/yfinance/">Yfinance</a>
- <a href="https://facebook.github.io/prophet/docs/quick_start.html">Prophet</a>

## Pacotes
<a href="https://github.com/jcpsantos/quote-analysis-tcc/blob/master/requirements.txt">Requirements</a>
```
$ pip install -r requirements.txt
```

## Analise Exploratoria
<a href="https://github.com/jcpsantos/quote-analysis-tcc/blob/master/analises/analise_exploratoria.ipynb">Notebook</a>

## Analises Utilizando Machine Learning
- <a href="https://github.com/jcpsantos/quote-analysis-tcc/blob/master/ml/lstm_ml.ipynb">LSTM</a>
- <a href="https://github.com/jcpsantos/quote-analysis-tcc/blob/master/ml/prophet_ml.ipynb">Prophet</a>

## Relatório Diario (via E-mail)
<a href="https://github.com/jcpsantos/quote-analysis-tcc/blob/master/relat%C3%B3rio/Relat%C3%B3rio%20via%20E-mail%20-%20An%C3%A1lise%20das%20a%C3%A7%C3%B5es%2025_08_2020.pdf">Exemplo</a>

## Relatório/Dashboard
<a href="https://datastudio.google.com/s/ugfkDCXvYCQ">Dashboard</a>

<iframe width="600" height="450" src="https://datastudio.google.com/embed/reporting/48f61161-0c26-48f7-87e2-449731832db4/page/2qocB" frameborder="0" style="border:0" allowfullscreen></iframe>
