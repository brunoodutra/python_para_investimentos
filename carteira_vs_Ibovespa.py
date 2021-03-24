# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:29:00 2021

@author: Bruno Dutra
"""
#%% bibliotecas
# PYTHON para finanças 
import pandas as pd
import numpy as np
from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
 
from plotly.offline import plot
import plotly.graph_objs as go


#%% Base de dados com mais ações
#acoes= data.DataReader(name=['EQTL3.SA','CSAN3.SA','MGLU3.SA','WEGE3.SA','BOVA11'], data_source='yahoo', start='2017-01-01' )
acoes=['B3SA3','VALE3','CNTO3','MGLU3','WEGE3','BOVA11']
# adc o .SA no nome de cada ação para carregar no banco de dados
for i in range(np.size(acoes)):
    acoes[i]=acoes[i]+".SA"
    
acoes_df = pd.DataFrame()
for acao in acoes:
     acoes_df[acao] = data.DataReader(acao, data_source='yahoo', start='2017-01-01')['Close']

#acoes_df = acoes_df.rename(columns={'B3SA3.SA': 'B3','EQTL.SA': 'EQTL', 'CSAN3.SA': 'CSAN', 'WEGE3.SA': 'WEGE',
 #                                   'MGLU3.SA': 'MGLU',  'BOVA11.SA': 'BOVA'})
 
# substitui o .SA do nome de cada ação para visualização dos dados
for i in range(np.size(acoes)):
    acoes_df = acoes_df.rename(columns={acoes[i]:acoes[i].replace('.SA', '')})
                           
#soma todos os valores nulos
acoes_df.isnull().sum()

#Verifica como está o shape do dataframe
acoes_df.shape
 
#apaga registros nulos
acoes_df.dropna(inplace=True)

acoes_df.to_csv('acoes.csv')

acoes_df = pd.read_csv('acoes.csv')

#%% gráfico com dados normalizados pelo primeiro valor da ação na data escolida
acoes_df_normalizado=acoes_df.copy()

for i in acoes_df.columns[1:]:
  acoes_df_normalizado[i] = acoes_df[i]/acoes_df[i][0]
  
# faz a média das ações contidas na carteira e cria uma nova coluna referente a carteira 
acoes_df['carteira']=acoes_df[acoes_df.columns[:-1]].mean(1)

#acoes_df_normalizado.plot(x='Date',figsize=(15,7),title='historico - normalizado')

acoes_df_normalizado[['Date','carteira','BOVA11']].plot(x='Date',title='Carteira vs BOVA11')
