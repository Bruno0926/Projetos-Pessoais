import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

arq = pd.read_csv('dados/dataset.csv')

vendas = arq.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values('Valor_Venda', ascending= False).head()

print('o segmento com maior numero de vendas foi: ', vendas.head(1))

plt.figure(figsize=(16,6))
plt.pie(vendas['Valor_Venda'], labels = vendas['Segmento'], startangle=90)
plt.title = 'Segmento maiores vendas'
plt.show()



