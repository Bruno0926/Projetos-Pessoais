import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

arq = pd.read_csv('dados/dataset.csv')

arq['Desconto'] = np.where(arq['Valor_Venda'] > 1000, 0.15, 0.10)
print(arq.head())

print(arq['Desconto'].value_counts())

