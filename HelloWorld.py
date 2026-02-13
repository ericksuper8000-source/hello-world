def Exception1(Volatil):
    Numerito = Volatil
    try:
        Numero = int(Numerito)
        return f'Gracias, el numero digitado es {Numero}'
    except ValueError:
        return f'Error, necesito que ingrese un numero'

print (f'{Exception1("Hola")}')

def Exception2(Num1, Num2):
    try:
        return Num1 + Num2
    except TypeError:
        return f'Error, necesito que ambos elementos sean numeros'

print (f'{Exception2(12, "Hola")}')

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        return f'Gracias, la division es {round(Divi, 2)}'
    except ZeroDivisionError:
        return f'Error, el divisor no puede ser cero'

print (f'{Exception3(12, 0)}')

Lista_Exception4 = list(['Erick', 'Josue', 'Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento con indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'El indice esta fuera de rango, error')

Exception4(3)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave seleccionada esta fuera de rango')

Exception5('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Pantera')
        Docu.close()
except FileNotFoundError:
    print (f'El archivo seleccinado no existe')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

try:
    import Module_Own as PEPE
except ImportError:
    print (f'El Modulo seleccinado no existe')

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nBallena'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSerpiente')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nFresas Sabrosas', '\nFresas Sabrosas', '\nFresas Sabrosas'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke1"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke2"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke3"]}\n')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Set_Conjunto_Poke)])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

import pandas as pd

Data_Frame1 = pd.DataFrame({
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, True, False]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [60, 14, 27],
    'Votante' : [True, False, True]
})

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

Data_Frame1_Age = Data_Frame1["Edad"]

print (f'{Data_Frame1}')

print (f'La menor de las edades es {Data_Frame1_Age.min()} y la mayor de las edades es {Data_Frame1_Age.max()}')

print (f'-------------------')

print (f'{Data_Frame1_Age}')

print (f'-------------------')

print (f'{Data_Frame_Concatenate.info()}')

print (f'-------------------')

print (f'{Data_Frame_Concatenate}')

print (f'-------------------')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombrecitos = elemento['Nombre']
    Editas = elemento['Edad']

    print (f'La edad de {Nombrecitos} es {Editas}')

print (f'-------------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'-------------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'-------------------')

print (f'{Data_Frame_Concatenate.head(1)}')
print (f'-------------------')
print (f'{Data_Frame_Concatenate.head(3)}')
print (f'-------------------')
print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'-------------------')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'El numero de filas es {Filas} y el numero de Columnas es {Columnas}')

Buscar1 = Data_Frame1.loc[0, 'Nombre']
Buscar2 = Data_Frame1.loc[1, 'Edad']
Buscar3 = Data_Frame1.loc[2, 'Votante']
Buscar4 = Data_Frame1.loc[:, 'Nombre']
Buscar5 = Data_Frame1.loc[2, :]

print (f'{Buscar1}')
print (f'{Buscar2}')
print (f'{Buscar3}')

print (f'-------------------')

print (f'{Buscar4}')

print (f'-------------------')

print (f'{Buscar5}')

print (f'-------------------')

Buscar6 = Data_Frame1.iloc[0, 0]
Buscar7 = Data_Frame1.iloc[1, 1]
Buscar8 = Data_Frame1.iloc[2, 2]
Buscar9 = Data_Frame1.iloc[:, 2]
Buscar10 = Data_Frame1.iloc[2, :]

print (f'{Buscar6}')
print (f'{Buscar7}')
print (f'{Buscar8}')

print (f'-------------------')

print (f'{Buscar9}')

print (f'-------------------')

print (f'{Buscar10}')

print (f'-------------------')

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine = 'openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'-------------------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, names=['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, index_col='cabina')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, usecols='E:J', index_col='cabina')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, usecols='E:J', index_col='cabina', nrows=1)

print (f'{Cargar_Excel1.head()}')

print (f'-------------------')

print (f'{Cargar_Excel2.head()}')

print (f'-------------------')

print (f'{Cargar_Excel3.head()}')

print (f'-------------------')

print (f'{Cargar_Excel4.head()}')

print (f'-------------------')

print (f'{Cargar_Excel5.head()}')

print (f'-------------------')

print (f'{Cargar_Excel6.head()}')

print (f'-------------------')

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='Cinco', ascending=True)
Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='Cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted}')

print (f'-------------------')

print (f'{Cargar_Excel3_Sorted_Descending}')

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'-------------------')

print (f'{Cargar_Txt.head()}')

print (f'-------------------')

import pandas

Ruta_Csv = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv = pd.read_csv(Ruta_Csv)

print (f'{Cargar_Csv}')

print (f'-------------------')

for indice, elemento in Cargar_Csv.iterrows():
    Apel = elemento['Apellido']
    if (Apel == 'Sandoval'):
        print (f'Como el playo de teletica')
    else:
        print (f'El apellido {indice} no me suena')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Cargar_Html = pd.read_html(Response.text)

print (f'{Cargar_Html[2].head()}')

print (f'-------------------')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Lectura_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Lectura_Html)

print (f'{Cargar_Html[2].head()}')

print (f'-------------------')

