import pandas as pd
import matplotlib.pyplot as plt

Ruta_Csv1 = 'C:\\python-data-analyzer\\data\\sales.csv'

Cargar_Csv = pd.read_csv(Ruta_Csv1)

Cargar_Csv['Total'] = Cargar_Csv['quantity'] * Cargar_Csv['price']

print (f'{Cargar_Csv}')

Calcular1 = Cargar_Csv.groupby('product')['Total'].sum()
Mayor = Calcular1.idxmax()
Menor = Calcular1.idxmin()

print (f'El producto que vendio mas fue {Mayor} y la cantidad vendida fue ${Calcular1.max()}')
print (f'El producto que vendio menos fue {Menor} y la cantidad vendida fue ${Calcular1.min()}')

Key1 = [f'Key{i}' for i in range(len(Cargar_Csv))]

print (f'{Key1}')

Lista1 = list(Cargar_Csv['product'])
Lista2 = list(Cargar_Csv['Total'])

Diccionario = dict(zip(Key1, Lista1))

for elemento in Diccionario.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Lista3 = list(Calcular1)

print (f'{Lista3}')

print (f'{max(Lista3)}')

