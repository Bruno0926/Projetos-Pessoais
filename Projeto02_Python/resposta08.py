import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

arq = pd.read_csv('dados/dataset.csv')

arq['Desconto'] = np.where(arq['Valor_Venda'] > 1000, 0.15, 0.10)
#print(arq.head())

# print(arq['Desconto'].value_counts())
arq['Valor_Desconto'] =  arq['Valor_Venda'] - (arq['Valor_Venda'] * arq['Desconto'])

#print(arq['Valor_Desconto'])

media_antiga = arq['Valor_Venda'].mean()
media_nova = arq['Valor_Desconto'].mean()

print('media antiga: ', media_antiga, ' media nova: ', media_nova)

#foi calculado a nova média com base em todos os descontos aplicados. De 10 e 15%




