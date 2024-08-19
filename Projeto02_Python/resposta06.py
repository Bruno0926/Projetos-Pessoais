import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

arq = pd.read_csv('dados/dataset.csv')

arq['Data_Pedido'] = pd.to_datetime(arq['Data_Pedido'], dayfirst= True)
arq['Ano'] = arq['Data_Pedido'].dt.year

resp6 = arq.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()

print(resp6)




