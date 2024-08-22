import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

arq = pd.read_csv('dados/dataset.csv')

#erro, falando que a data no arquivo não está no formato de data... ??
arq['Data_Pedido'] = pd.to_datetime(arq['Data_Pedido'])

arq['Ano'] = arq['Data_Pedido'].dt.year
arq['Mes'] = arq['Data_Pedido'].dt.month

vendas = arq.groupby(['Ano', 'Mes', 'Segmento'])['Valor_Venda'].mean()

print('a media eh: ', vendas)




