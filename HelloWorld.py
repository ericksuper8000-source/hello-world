import http.cookiejar


def Exception1(variable):
    Numero = variable
    try:
        Numerito = int(Numero)
        print (f'Gracias, tu numero digitado es {Numerito}')
    except ValueError:
        print (f'Error, ingrese un numero')

Exception1(15)

def Exception2(Num1, Num2):
    try:
        Sumatoria = Num1 + Num2
        print (f'El resultado de la sumatoria es {Sumatoria}')
    except TypeError:
        print (f'Error, ambos elementos deben ser numeros')

Exception2(12, 'Hola')

def Exception3(Num1, Num2):
    try:
        Div = Num1 / Num2
        print (f'El resultado de la division es {round(Div, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(12, 0)

Lista_Exception4 = list(['Erick', 'Josue', 'Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento en la posicion {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, El indice, esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El elemento en la posicion {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, La llave esta fuera de rango')

Exception5('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Cocodrilo')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo seleccionado es incorrecto')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

try:
    import Module_Own as PEPE
except ImportError:
    print (f'El modulo seleccionado no existe, error')

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nTigre'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nAvestruz')
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
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke1"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke2"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke3"]}\n')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Set_Conjunto_Poke)])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

import pandas as pd

DataFrame1 = pd.DataFrame({
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
})

DataFrame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [64, 14, 26],
    'Votante' : [True, False, not False]
})

DataFrame1_Age = DataFrame1['Edad']

DataFrame_Concatenate = pd.concat([DataFrame2, DataFrame1])

print (f'{DataFrame1_Age}')

print (f'---------------')

print (f'{DataFrame1}')

print (f'---------------')

print (f'{DataFrame_Concatenate.info()}')

print (f'---------------')

print (f'El menor de la lista es {DataFrame1_Age.min()} y el mayor de la lista es {DataFrame1_Age.max()}')

print (f'---------------')

for indice, elemento in DataFrame_Concatenate.iterrows():
    Nombres = elemento['Nombre']

    print (f'Mi nombre es {Nombres}')

print (f'---------------')

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=DataFrame_Concatenate)

plt.show()

print (f'---------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=DataFrame_Concatenate)

plt.show()

print (f'---------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=DataFrame_Concatenate)

plt.show()

'''

print (f'{DataFrame_Concatenate.head(1)}')
print (f'---------------')
print (f'{DataFrame_Concatenate.head(3)}')
print (f'---------------')
print (f'{DataFrame_Concatenate.tail(1)}')
print (f'---------------')

Filas, Columnas = DataFrame_Concatenate.shape

print (f'La cantidad de filas es {Filas} y la de columnas son {Columnas}')

Buscar1 = DataFrame1.loc[0, 'Nombre']
Buscar2 = DataFrame1.loc[1, 'Edad']
Buscar3 = DataFrame1.loc[2, 'Votante']
Buscar4 = DataFrame1.loc[:, 'Nombre']
Buscar5 = DataFrame1.loc[1, :]

print (f'{Buscar1}')
print (f'{Buscar2}')
print (f'{Buscar3}')
print (f'{Buscar4}')
print (f'{Buscar5}')

print (f'---------------')

Buscar6 = DataFrame2.iloc[0, 0]
Buscar7 = DataFrame2.iloc[1, 1]
Buscar8 = DataFrame2.iloc[2, 2]
Buscar9 = DataFrame2.iloc[:, 0]
Buscar10 = DataFrame2.iloc[2, :]

print (f'{Buscar6}')
print (f'{Buscar7}')
print (f'{Buscar8}')
print (f'{Buscar9}')
print (f'{Buscar10}')

print (f'---------------')

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine = 'openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'---------------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, names=['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, index_col='embarcado')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, usecols='E:I', index_col='tarifa')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, usecols='E:I', index_col='tarifa', nrows=1)

print (f'{Cargar_Excel1.head()}')

print (f'---------------')

print (f'{Cargar_Excel2.head()}')

print (f'---------------')

print (f'{Cargar_Excel3.head()}')

print (f'---------------')

print (f'{Cargar_Excel4.head()}')

print (f'---------------')

print (f'{Cargar_Excel5.head()}')

print (f'---------------')

print (f'{Cargar_Excel6.head()}')

print (f'---------------')

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='Cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'---------------')

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='Cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

print (f'---------------')

print (f'{DataFrame1_Age}')

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'---------------')

print (f'{Cargar_Txt.head()}')

print (f'---------------')

import pandas as pd

Ruta_Csv = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv = pd.read_csv(Ruta_Csv)

print (f'{Cargar_Csv.head()}')

print (f'---------------')

for indice, elemento in Cargar_Csv.iterrows():
    Apellido = elemento['Apellido']

    print (f'Mi apellido es {Apellido}')

print (f'---------------')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Cargar_Html = pd.read_html(Response.text)

print (f'{Cargar_Html[2].head()}')

print (f'---------------')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Leer_Html)

print (f'{Cargar_Html[1].head()}')

print (f'---------------')

import numpy as np

Array1 = np.array([1, 2, 3])

print (f'{Array1}')
print (f'{Array1.ndim}') # 1
print (f'{Array1.shape}') # 1x3
print (f'{Array1.size}') # 3
print (f'{Array1.dtype}') # int64
print (f'{Array1[0]}')
print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[1:2]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 <= 2]}')

print (f'---------------')

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 2]}')
print (f'{Array2[0, :2]}')
print (f'{Array2[0, 2:]}')
print (f'{Array2[1, ::2]}')
print (f'{Array2[0, ::3]}')
print (f'{Array2[1, 1:2]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[0, :]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Media = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Media, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[1, 0:None])
Sumita4 = np.sum(Array2_Sorted[1, :])

print (f'El resultado de la sumita es {Sumita1}')
print (f'El resultado de la sumita es {Sumita2}')
print (f'El resultado de la sumita es {Sumita3}')
print (f'El resultado de la sumita es {Sumita4}')

print (f'---------------')

Array3 = np.array([[['r', 'i', 'k'], ['f', 'l', 'v']],        [['u', 'j', 'a'], ['x', 'z', 'w']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 1]}')
print (f'{Array3[0, 1, :2]}')
print (f'{Array3[0, 1, 2:]}')
print (f'{Array3[1, 0, ::2]}')
print (f'{Array3[1, 1, ::3]}')
print (f'{Array3[0, 0, 1:2]}')
print (f'{Array3[1, :, 0]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "a"]}')

print (f'---------------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],     [[[6, 5, 4], [9, 8, 7]], [[0, 5 ,1], [7, 3, 0]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # Int64
print (f'{Array4[1, 1, 0, 2]}')
print (f'{Array4[1, 1, 0, :2]}')
print (f'{Array4[1, 1, 0, 2:]}')
print (f'{Array4[0, 1, 1, ::2]}')
print (f'{Array4[0, 0, 0, ::3]}')
print (f'{Array4[1, 0, 1, 1:2]}')
print (f'{Array4[0, 1, :, 1]}')
print (f'{Array4[1, 1, 1, 0:None]}')
print (f'{Array4[1, 1, 1, :]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado {Array4_Sorted}')
print (f'Media {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[0, 1, 0, 0:None])
Sumita8 = np.sum(Array4_Sorted[0, 1, 0, :])

print (f'El resultado de la sumatoria es {Sumita5}')
print (f'El resultado de la sumatoria es {Sumita6}')
print (f'El resultado de la sumatoria es {Sumita7}')
print (f'El resultado de la sumatoria es {Sumita8}')

print (f'---------------')

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_Min = np.min(Array_Num1)
Array_Max = np.max(Array_Num1)

print (f'El menor de los numeros es {Array_Min} y el mayor de los numeros es {Array_Max}')

print (f'---------------')

Array_Num2 = np.arange(25)

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

Array_Num2_Reshape_Column_Min = np.min(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Column_Max = np.max(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Row_Min = np.min(Array_Num2_Reshape, axis=1)
Array_Num2_Reshape_Row_Max = np.max(Array_Num2_Reshape, axis=1)

print (f'Los menores de las columnas son {Array_Num2_Reshape_Column_Min}')
print (f'Los mayores de las columnas son {Array_Num2_Reshape_Column_Max}')
print (f'Los menores de las filas son {Array_Num2_Reshape_Row_Min}')
print (f'Los mayores de las filas son {Array_Num2_Reshape_Row_Max}')

print (f'---------------')

Array_Zero = np.zeros(shape=(2, 3))

print (f'{Array_Zero}')
print (f'{Array_Zero.ndim}')
print (f'{Array_Zero.shape}')
print (f'{Array_Zero.size}')
print (f'{Array_Zero.dtype}')
print (f'{Array_Zero[1, 2]}')

print (f'---------------')

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 1]}')

print (f'---------------')

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[0, 2]}')

print (f'---------------')

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[2]}')

Lista_Array1 = list([])

for elemento in Array_Gen2:
    Lista_Array1.append(str(elemento))

print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'---------------')

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[0, 1, 0, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 1]}')

print (f'---------------')

Tupla_Array = ('Rojo', 'Verde')
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array["Nombre"][2])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'---------------')

print (f'{Array_Gen6[3]}')

print (f'---------------')

Array_Num3 = np.arange(start=1, stop=6, step=1)
Array_Num4 = np.arange(start=2, stop=11, step=2)
Array_Num5 = np.arange(start=3, stop=31, step=3)
Array_Num6 = np.arange(start=10, stop=21, step=2)
Array_Num7 = np.arange(10)

print (f'{Array_Num3}')
print (f'{Array_Num4}')
print (f'{Array_Num5}')
print (f'{Array_Num6}')
print (f'{Array_Num7}')

print (f'---------------')

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')

print (f'---------------')

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')
print (f'{Array_Random2.ndim}')
print (f'{Array_Random2.shape}')
print (f'{Array_Random2.size}')
print (f'{Array_Random2.dtype}')
print (f'{Array_Random2[1, 0]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado {Array_Random2_Sorted}')
print (f'Media {Array_Random2_Sorted_Mean}')
print (f'Sumatoria {Array_Random2_Sorted_Sum}')

print (f'---------------')

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Sum = Arr1 + Arr2
Rest = Arr1 - Arr2
Mult = Arr1 * Arr2
Div = Arr1 / Arr2
Array_Random1_Cien = Array_Random1 + 100

print (f'El resultado de la operacion es {Sum}')
print (f'El resultado de la operacion es {Rest}')
print (f'El resultado de la operacion es {Mult}')
print (f'El resultado de la operacion es {Div}')
print (f'El resultado de la operacion es {Array_Random1_Cien}')

print (f'---------------')

Array_Random3 = np.random.randint(low=1, high=10, size=(20))

print (f'{Array_Random3}')

Array_Random3_Reshape = np.reshape(Array_Random3, shape=(4, 5))

print (f'{Array_Random3_Reshape}')

Array_Random3_Reshape_Ravel = np.ravel(Array_Random3_Reshape)

print (f'{Array_Random3_Reshape_Ravel}')

print (f'---------------')

Lista_Array2 = ['Erick', 'Josue', 'Perez']

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'---------------')

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concat([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'---------------')

Array_Concatenate_Split = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Split[0]}')
print (f'{Array_Concatenate_Split[1]}')
print (f'{Array_Concatenate_Split[2]}')

print (f'---------------')

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'---------------')

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'---------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'---------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'---------------')

ArrayRandom4 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{ArrayRandom4}')

Sumita9 = np.sum(ArrayRandom4, axis=0)
Sumita10 = np.sum(ArrayRandom4, axis=1)
Sumita11 = np.sum(ArrayRandom4[1, 0, 0:None])
Sumita12 = np.sum(ArrayRandom4[1, 0, :])

print (f'{Sumita9}')
print (f'{Sumita10}')
print (f'{Sumita11}')
print (f'{Sumita12}')

print (f'---------------')

Tupla_Array2 = tuple(('Erick', 'Josue', 'Karlita', 'Carmelo', 'Susanita', 'Roxana'))

Ganador1 = np.random.choice(Tupla_Array2, size=(1), replace=False)
Ganador2 = np.random.choice(Tupla_Array2, size=(2), replace=False)
Ganador3 = np.random.choice(Tupla_Array2, size=(2, 3), replace=False)

print (f'{Ganador1}')
print (f'{Ganador2}')
print (f'{Ganador3}')

print (f'---------------')

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'---------------')

def Generadora1():
    for elemento in range(5):
        yield f'El elemento es {elemento}'

Gen1 = Generadora1()

try:
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
except StopIteration:
    print (f'El experimento termina aqui')

print (f'---------------')

def Generadora2():
    for elemento in range(5):
        if (elemento % 2 == 0):
            yield f'PAR'
        else:
            yield f'IMPAR'

Gen2 = Generadora2()

try:
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
except StopIteration:
    print(f'El experimento termina aqui')

print (f'---------------')

def Generadora3():
    for elemento in range(5):
        if (elemento == 0):
            yield f'{elemento} se escribe Zero in english'
        elif (elemento == 1):
            yield f'{elemento} se escribe One in english'
        elif (elemento == 2):
            yield f'{elemento} se escribe Two in english'
        elif (elemento == 3):
            yield f'{elemento} se escribe Three in english'
        elif (elemento == 4):
            yield f'{elemento} se escribe Four in english'
        else:
            print (f'Error de codigo')

Gen3 = Generadora3()

try:
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
except StopIteration:
    print(f'El experimento termina aqui')

print (f'---------------')

import re

'''
Search1 = re.search()
Search2 = re.findall()
Search3 = re.fullmatch()
Search4 = re.match() '''

variable0 = 'este es un texto que lleva el numero 3 pero tambien el 45, pero @ lo mas importate es ! que vamos a practicar * expresiones regulares'

# Encuentre un unico numero en la variable

Search1 = re.search('\d', variable0)

print (f'{Search1}')

# Encuentre todos los numeros en la cadena

Search2 = re.findall('\d+', variable0)

print (f'{Search2}')

# Encuentre todo menos los numeros

Search3 = re.findall('\D+', variable0)

print (f'{Search3}')

# Encuentre todo menos los caracters especiales

Search4 = re.findall('\w+', variable0)

print (f'{Search4}')

# Encuentre unicamente caracteres especiales

Search5 = re.findall('\W+', variable0)

print (f'{Search5}')

# Encuentre unicamente espacios

Search6 = re.findall('\s+', variable0)

print (f'{Search6}')

# Encuentre unicamente lo que no tiene espacios

Search7 = re.findall('\S+', variable0)

print (f'{Search7}')

variable0_1 = 'hola esto es un hela yyy ademas puuede quee unnnnnnn hula tambien pero no se'

Search8 = re.findall('h.la', variable0_1)

print (f'{Search8}')

#Buscar los textos que contengan mas de una letra e

Search9 = re.findall('e{0,2}', variable0_1)

print (f'{Search9}')

# Buscar 0 o mas numeros en la cadena

Search10 = re.findall('\d?', variable0)

print (f'{Search10}')

variable0_2 = 'color o colur'
Coincidencia1 = 'col[ou]?r'
Coincidencia2 = 'h[o,u,e]?la'

Search11 = re.findall(Coincidencia1, variable0_2)

print (f'{Search11}')

Search12 = re.findall(Coincidencia2, variable0_1)

print (f'{Search12}')

Search13 = re.findall('un{4,}+', variable0_1)

print (f'{Search13}')

# Buscar la palabra especifica

Search14 = re.findall('[puuede]', variable0_1)

print (f'{Search14}')

# Busque solo palabras minusculas

variable0_3 = 'Este sEra un EjemPLO de UN HIPOpotamo'

Search15 = re.findall('[a-z]', variable0_3)

print (f'{Search15}')

Search16 = re.findall('[A-Z]', variable0_3)

print (f'{Search16}')

Search17 = re.findall('[a-zA-Z]', variable0_3)

print (f'{Search17}')

Search18 = re.findall('[a-zA-Z0-9\W\S]', variable0)

print (f'{Search18}')

Search19 = re.search('^hola', variable0_1)

print (f'{Search19}')

Search20 = re.search('se$', variable0_1)

print (f'{Search20}')

variable0_4 = 'Pera $150'

Patron = 'Pera \$(\d+)'

Search21 = re.search(Patron, variable0_4)

if Search21:
    Finale = Search21.group(1)

    print (f'El numero de peras es {Finale}')





