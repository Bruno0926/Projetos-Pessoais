import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

arq = pd.read_csv('dados\dataset.csv')

vendas = arq.groupby('Estado')['Valor_Venda'].sum().reset_index()
print(vendas)

# GRÁFICO MAIS SMPLES:

# plt.figure(figsize=(16,6))
# vendas.plot(x = 'Estado', y = 'Valor_Venda', color = 'green')
# plt.title = 'Vendas_Estado'

# MELHOR GRÁFICO:
plt.figure(figsize=(16,6))
sns.barplot(data = vendas, x = 'Estado', y = 'Valor_Venda').set(title = 'Vendas por estado')
plt.xticks(rotation = 90) # deixa os nomes em "90" graus
plt.show()

