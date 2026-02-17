def Exception1(Num1):
    Numerito = Num1
    try:
        Numerito2 = int(Numerito)
        print (f'Gracias, el numero ingresado es {Numerito2}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Exception1(45)

def Exception2(Num1, Num2):
    try:
        Operacion = Num1 + Num2
        print (f'El resultado de la operacion es {Operacion}')
    except TypeError:
        print (f'Error, ambos elementos deberian ser numeros')

Exception2(12, 7)

def Exception3(Num1, Num2):
    try:
        Div = Num1 / Num2
        print (f'El resultado de la division es {round(Div, 2)}')
    except ZeroDivisionError:
        print (f'Error, El divisor no puede ser un zero')

Exception3(12, 7)

Lista_Exception4 = ['Erick', 'Josue', 'Karlita']

def Exception4(Indice):
    try:
        print (f'El elemento en el {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'El indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El elemento con la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, La llave esta fuera de rango')

Exception5('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Pera')
        Docu.close()
except FileNotFoundError:
    print (f'El archivo seleccionado no existe')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado no existe')

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nUvas'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nManzana')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nFresa Sabrosa', '\nFresa Sabrosa', '\nFresa Sabrosa'])
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
    'Edad' : [64, 14, 28],
    'Votante' : [True, False, True]
})

Data_Frame1_Age = Data_Frame1['Edad']

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

print (f'{Data_Frame1_Age}')

print (f'--------------')

print (f'{Data_Frame1}')

print (f'--------------')

print (f'El menor de los elementos es {Data_Frame1_Age.min()} y el mayor de los elementos es {Data_Frame1_Age.max()}')

print (f'--------------')

print (f'{Data_Frame_Concatenate.info()}')

print (f'--------------')

print (f'{Data_Frame_Concatenate}')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Edad = elemento['Edad']
    if (Edad >= 36):
        print (f'{Edad} - Esta es la mayor de las edades')
        break
    else:
        print (f'{Edad} es menor que 36')

print (f'--------------')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombre = elemento['Nombre']
    print (f'Su nombre es {Nombre}')

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'--------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'--------------')

'''

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'--------------')

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'--------------')

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'--------------')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'La cantidad de Filas es {Filas} y la cantidad de Columnas es {Columnas}')

Elemento1 = Data_Frame1.loc[0, 'Nombre']
Elemento2 = Data_Frame1.loc[1, 'Edad']
Elemento3 = Data_Frame1.loc[2, 'Votante']
Elemento4 = Data_Frame1.loc[:, 'Nombre']
Elemento5 = Data_Frame1.loc[2, :]

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')

print (f'--------------')

print (f'{Elemento4}')

print (f'--------------')

print (f'{Elemento5}')

print (f'--------------')

Elemento6 = Data_Frame1.iloc[0, 0]
Elemento7 = Data_Frame1.iloc[1, 1]
Elemento8 = Data_Frame1.iloc[2, 2]
Elemento9 = Data_Frame1.iloc[0, :]
Elemento10 = Data_Frame1.iloc[1, :]

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')

print (f'--------------')

print (f'{Elemento9}')

print (f'--------------')

print (f'{Elemento10}')

print (f'--------------')

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'
Cargar_Excel = pd.read_excel(Ruta_Excel, engine='openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'--------------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tarifa')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols='E:K', index_col='embarcado')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols='E:K', index_col='embarcado', nrows=1)

print (f'{Cargar_Excel1.head()}')

print (f'--------------')

print (f'{Cargar_Excel2.head()}')

print (f'--------------')

print (f'{Cargar_Excel3.head()}')

print (f'--------------')

print (f'{Cargar_Excel4.head()}')

print (f'--------------')

print (f'{Cargar_Excel5.head()}')

print (f'--------------')

print (f'{Cargar_Excel6.head()}')

print (f'--------------')

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='Cinco', ascending=True)
Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='Cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted}')

print (f'--------------')

print (f'{Cargar_Excel3_Sorted_Descending}')

print (f'--------------')

for indice, elemento in Data_Frame2.iterrows():
    Edad = elemento['Edad']
    if (Edad > 30):
        print (f'{Edad}')
    else:
        print (f'No hay edad mayor a 30 años')

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'--------------')

print (f'{Cargar_Txt.head()}')

print (f'--------------')

for indice, elemento in Cargar_Txt.iterrows():
    Fruta = elemento
    print (f'{Fruta}')

print (f'--------------')

import pandas as pd

Ruta_Csv = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv = pd.read_csv(Ruta_Csv)

print (f'{Cargar_Csv.head()}')

for indice, elemento in Cargar_Csv.iterrows():
    Last_Name = elemento['Apellido']

    print (f'{Last_Name}')

print (f'--------------')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Cargar_html = pd.read_html(Response.text)

print (f'{Cargar_html[2].head()}')

print (f'--------------')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_html = pd.read_html(Leer_Html)

print (f'{Cargar_html[2].head()}')

print (f'--------------')

import numpy as np

Array1 = np.array([1, 2, 3])

print (f'{Array1}')
print (f'{Array1.ndim}') # 1
print (f'{Array1.shape}') # 1x3
print (f'{Array1.size}') # 3
print (f'{Array1.dtype}') # int64
print (f'{Array1[1]}')
print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[1:2]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 <= 2]}')

print (f'--------------')

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 0]}')
print (f'{Array2[0, :2]}')
print (f'{Array2[0, 2:]}')
print (f'{Array2[1, ::2]}')
print (f'{Array2[0, ::3]}')
print (f'{Array2[:, 1]}')
print (f'{Array2[1, 1:2]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[0, :]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[1, 0:None])
Sumita4 = np.sum(Array2_Sorted[1, :])

print (f'{Array2_Sorted}')
print (f'{Array2_Sorted_Mean}')
print (f'{Array2_Sorted_Sum}')

print (f'--------------')

print (f'{Sumita1}')
print (f'{Sumita2}')
print (f'{Sumita3}')
print (f'{Sumita4}')

print (f'--------------')

Array3 = np.array([[['e', 'j', 'a'], ['s', 'd', 'k']],      [['l', 'i', 'n'], ['u', 'm', 'w']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 2]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[1, 1, 1:2]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "a"]}')

print (f'--------------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],         [[[6, 5, 4], [9, 8, 7]], [[0, 4, 1], [7, 3, 8]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[0, 1, 0, 1]}')
print (f'{Array4[0, 1, 0, :2]}')
print (f'{Array4[0, 1, 0, 2:]}')
print (f'{Array4[1, 1, 0, ::2]}')
print (f'{Array4[1, 1, 0, ::3]}')
print (f'{Array4[1, 1, :, 0]}')
print (f'{Array4[0, 0, 1, 1:2]}')
print (f'{Array4[1, 1, 0, 0:None]}')
print (f'{Array4[1, 1, 0, :]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[0, 1, 0, 0:None])
Sumita8 = np.sum(Array4_Sorted[0, 1, 0, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'--------------')

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_Menor = np.min(Array_Num1)
Array_Mayor = np.max(Array_Num1)

print (f'El menor de los numeros es {Array_Menor} y el mayor es {Array_Mayor}')

print (f'--------------')

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

print (f'--------------')

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 0]}')

print (f'--------------')

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 2]}')

print (f'--------------')

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 1]}')

print (f'--------------')

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[2]}')

Lista_Array1 = list([])

for elemento in enumerate(Array_Gen2):
    Lista_Array1.append(str(elemento[1]))

print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'--------------')

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[1, 0, 1, 1:2])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 1]}')

print (f'--------------')

Tupla_Array = ('Rojo', 'Verde')
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array['Nombre'][2])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'--------------')

print (f'{Array_Gen6[3]}')

print (f'--------------')

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

print (f'--------------')

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')
print (f'{Array_Random1.ndim}')
print (f'{Array_Random1.shape}')
print (f'{Array_Random1.size}')
print (f'{Array_Random1.dtype}')
print (f'{Array_Random1[5]}')

print (f'--------------')

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')
print (f'{Array_Random2.ndim}')
print (f'{Array_Random2.shape}')
print (f'{Array_Random2.size}')
print (f'{Array_Random2.dtype}')
print (f'{Array_Random2[1, 1]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

print (f'--------------')

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

print (f'--------------')

Array_Num8 = np.arange(20)

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'--------------')

Lista_Array2 = list['Erick', 'Josue', 'Perez', 'Gutierrez']

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'--------------')

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concat([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'--------------')

Array_Concatenate_Split = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Split[0]}')
print (f'{Array_Concatenate_Split[1]}')
print (f'{Array_Concatenate_Split[2]}')

print (f'--------------')

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'--------------')

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'--------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'--------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'--------------')

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Sumita9 = np.sum(Array_Random3, axis=0)
Sumita10 = np.sum(Array_Random3, axis=1)
Sumita11 = np.sum(Array_Random3[1, 0, 0:None])
Sumita12 = np.sum(Array_Random3[1, 0, :])

print (f'{Sumita9}')
print (f'{Sumita10}')
print (f'{Sumita11}')
print (f'{Sumita12}')

print (f'--------------')

Lista_Array2 = list(['Erick', 'Josue', 'Karlita', 'Roxana', 'Susanita', 'Carmelo'])

Ganador1 = np.random.choice(Lista_Array2, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Array2, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Array2, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'--------------')

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'--------------')

def Generadora1():
    for elemento in range(5):
        yield elemento

Gen1 = Generadora1()

try:
    print (f'El elemento es {next(Gen1)}')
    print (f'El elemento es {next(Gen1)}')
    print (f'El elemento es {next(Gen1)}')
    print (f'El elemento es {next(Gen1)}')
    print (f'El elemento es {next(Gen1)}')
    print (f'El elemento es {next(Gen1)}')
except StopIteration:
    print (f'El experimento termina aqui')

print (f'--------------')

def Generadora2():
    for elemento in range(5):
        if (elemento % 2 == 0):
            yield f'PAR'
        else:
            yield f'IMPAR'

Gen2 = Generadora2()

try:
    print (f'El elemento es {next(Gen2)}')
    print (f'El elemento es {next(Gen2)}')
    print (f'El elemento es {next(Gen2)}')
    print (f'El elemento es {next(Gen2)}')
    print (f'El elemento es {next(Gen2)}')
    print (f'El elemento es {next(Gen2)}')
except StopIteration:
    print (f'El experimento termina aqui')

print (f'--------------')

def Generadora3():
    for elemento in range(5):
        if (elemento == 0):
            yield f'El numero es {elemento}'
        elif (elemento == 1):
            yield f'El numero es {elemento}'
        elif (elemento == 2):
            yield f'El numero es {elemento}'
        elif (elemento == 3):
            yield f'El numero es {elemento}'
        elif (elemento == 4):
            yield f'El numero es {elemento}'
        else:
            yield f'Error de codigo'

Gen3 = Generadora3()

try:
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
except StopIteration:
    print (f'El experimento termina aqui')

print (f'--------------')

import re

variable0 = 'esto es un texto pero el numero 1 y tambien el numero 45 apareceran durante 260 todo el texto'
variable0_1 = '123456a784t'

Buscador1 = re.search('tambien', variable0)

print (f'{Buscador1}')

Buscador2 = re.findall('e', variable0)

print (f'{Buscador2}')

Buscador3 = re.fullmatch('esto es un texto pero el numero 1 y tambien el numero 45 apareceran durante todo el texto', variable0)

print (f'{Buscador3}')

# Buscar un numero

Buscador4 = re.search('\d', variable0)

print (f'{Buscador4}')

# Buscar todos los numeros

Buscador5 = re.findall('\d+', variable0)

print (f'{Buscador5}')

# Buscar lo que no es un digito numerico

Buscador6 = re.findall('\D+', variable0_1)

print (f'{Buscador6}')

# Tome unicamente los characteres normales

Buscador7 = re.search(r'\w+', 'Hola123!')

print (f'{Buscador7}')

# Tome unicamente los characteres especiales

Buscador8 = re.search(r'\W+', 'Hola123!')

print (f'{Buscador8}')

# Buscar solo los espacios en la cadena

Buscador9 = re.findall('\s+', variable0)

print (f'{Buscador9}')

# Buscar solo lo que no tiene espacios en la cadena

Buscador10 = re.findall('\S+', variable0)

print (f'{Buscador10}')

# Buscar todos los bloques que tengan h.la

Buscador11 = re.findall(r'H.la', 'vamos a ver si Hola es igual a Hela o incluso podria ser lo mismo que Hila')

print (f'{Buscador11}')

# Buscar la coincidencia una unica vez

Buscador12 = re.search(r'H.la?', 'vamos a ver si Hola es igual a Hela o incluso podria ser lo mismo que Hila')

print (f'{Buscador12}')

# Buscar la coincidencia dos veces

Buscador13 = re.findall(r's{1}a{1}', 'sabor, saber, sabir, sola, sela')

print (f'{Buscador13}')

Buscador14 = re.findall('ho{4,10}', 'h, hoooo, hoooooooooo, ho, hoo')

print (f'{Buscador14}')

variable0_2 = 'este Sera un eSteBAN ejemplo para Saber si esto sive o nO'

# Buscamos todas las palabras minusculas

Buscador15 = re.findall('[a-z]+', variable0_2)

print (f'{Buscador15}')

# Buscamos todas las palabras mayusculas

Buscador16 = re.findall('[A-Z]+', variable0_2)

print (f'{Buscador16}')

# Buscamos todos los numeros del 0 al 9

Buscador17 = re.findall('[0-9]+', variable0)

print (f'{Buscador17}')

# Todo menos eSteBAN

Buscador18 = re.findall('[^eSteBAN]', variable0_2)

print (f'{Buscador18}')

# Inicia con esto?

Buscador19 = re.search('^esto', variable0)

print (f'{Buscador19}')

# Termina con texto?

Buscador20 = re.search('texto$', variable0)

print (f'{Buscador20}')

if (Buscador20):
    print (f'EL texto termina con la palabra texto')
else:
    print (f'Error en la expresion regular')

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2):
        return Num1 + Num2

    return Sumatoria_Interna(4)

Variable_Sumatoria = Sumatoria_Externa(3)

print (f'El resultado de la sumatoria es {Variable_Sumatoria}')

if (PEPE.Par(Variable_Sumatoria) == True):
    print (f'El numero es par')
else:
    print (f'El numero es impar')

PEPE.Usuario(Saludar_Dos(), 'MASCULINO')

def Usuario_Externo():
    def Usuario_Interno(Sexo):
        Genero = Sexo.lower()
        if (Genero == 'masculino'):
            return True
        else:
            return False

    return Usuario_Interno('MASCULINO')

Variable_Usuario = Usuario_Externo()

if (Variable_Usuario == True):
    print (f'YOU ARE A MAN')
else:
    print (f'YOU ARE A WOMAN')

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding = 'UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(37)}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 36, 3.5, not True)

print (f'{Funcion_Tupla("Perro", 36, 3.5, not True)}')
print (f'{Funcion_Tupla("Perro", 36, 3.5, not True)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 36, 3.5, not True))}')

