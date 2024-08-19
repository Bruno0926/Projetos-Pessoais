import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

arq = pd.read_csv('dados\dataset.csv')

vendas = arq.groupby('Data_Pedido')['Valor_Venda'].sum()
print(vendas.head())

plt.figure(figsize=(20,6))
vendas.plot(x = 'Data_Pedido', y = 'Valor_Venda', color = 'blue')
plt.title = 'Grafico Venda_Pedido'

plt.show()







