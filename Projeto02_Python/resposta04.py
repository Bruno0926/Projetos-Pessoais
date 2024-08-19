import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

arq = pd.read_csv('dados\dataset.csv')

vendas = arq.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values('Valor_Venda', ascending = False).head(10)

print(vendas)

plt.figure(figsize= (16, 6))
sns.barplot(data = vendas, x = 'Cidade', y = 'Valor_Venda').set(title = 'Cidades maiores 10 vendas')
plt.xticks(rotation = 90)
plt.show()






