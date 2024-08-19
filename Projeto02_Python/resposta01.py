import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

arq = pd.read_csv('dados\dataset.csv')

categoria = arq[arq['Categoria'] == "Office Supplies"]
cidade = categoria.groupby('Cidade')['Valor_Venda'].sum()
maior_venda = cidade.idxmax()

print('a cidade com o maior valor eh: ' + maior_venda)













