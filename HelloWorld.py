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

print (f'--------------')

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')

Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')
print (f'Los numeros pares de la lista son {PEPE.Lista_Par} o incluso podrian ser {list(Anonima3)}')

def Primera(Segunda):
    def Tercera(*args):
        return Segunda(*args) - 42

    return Tercera

@Primera
def Operacion(Numero:int) -> int:
    Local = Numero
    return PEPE.Global + Local

print (f'El resultado de la operacion es {Operacion(12)}')

def Externa(Nombre):
    def Interna(Apellido:str) -> str:
        print (f'Mi nombre es {Nombre} {Apellido}')

    return Interna('PEREZ GUTIERREZ')

Externa('ERICK JOSUE')

def Closure_Externo():
    Lista_Closure = list([])
    def Closure_Interno(x):
        Lista_Closure.append(x)

        return Lista_Closure

    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(24)}')
print (f'{Variable_Closure(37)}')

def Crear_Multiplicador(x):
    def Multiplicador(y):
        return x * y

    return Multiplicador

Variable_Mult1 = Crear_Multiplicador(2)
Variable_Mult2 = Crear_Multiplicador(3)

print (f'El multiplicador 1 es {Variable_Mult1(10)}')
print (f'El multiplicador 2 es {Variable_Mult2(10)}')

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    if (Any_Impar == True):
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impares = [num for num in Lista if num % 2 != 0]

        print (f'Los numeros impares de la lista son {list(Anonima4)} o incluso podrian ser {Lista_Impares}')
    else:
        print (f'Error, no hay elementos impares en la lista')

Filtrador(PEPE.Lista_Numeros)

def Primera(Segunda):
    def Tercera():
        print (f'ANTES')
        Segunda()
        print (f'DESPUES')

    return Tercera

@Primera
def Saludar4():
    print (f'Hola Mundo')

Saludar4()

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) + 2

    return Tercera

@Primera
def Sumatoria3(Num1, Num2):
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(7, 1)}')

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonathan'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)

    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    print (f'Mi nombre es {Nombre} {Apellido}')

Usuario2('Erick', 'Perez')

from Module_Own import Pokemon as Poke

Objeto1 = Poke(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto2 = Poke(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')
Objeto3 = Poke(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro')

Objeto2.Mostrar()

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un
Long
String'''

variable4 = Objeto1.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = not False, Objeto3.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[2]} tiene {Variable_Sumatoria} {Sumatoria2(1, 2, 3, 4)} o incluso {Objeto3.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

Snake_Case1, Snake_Case2, Snake_Case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables {Snake_Case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto2.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y su residuo es {Residuo}')

print (f'Un rango de elementos de la lista 2 es {PEPE.Lista2[2:4]}')

print (f'{Lista_Uno[1]}, eso es un {PEPE.Lista2[2]}?')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, 200, 100)

print (f'{Lista_Cuatro}')

del Lista_Uno[1]
Lista_Uno.remove('Coco Rayado')
Lista_Uno.pop(-2)
Lista_Uno.pop(-1)
Lista_Uno.pop(-1)

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Lista_Uno_Copia = Lista_Uno.copy()

Lista_Uno.clear()

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'{PEPE.__dir__()}')

print (f'-----------')

print (f'{help(PEPE)}')

print (f'-----------')

Tupla1 = ('Uno', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos')

print (f'{Tupla1}')

Tupla1 = tuple(('One', 'Two', 'Three'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')

Set_Conjunto1 = {'Roca', 'Roca', 'Roca', 'Roca', 'Roca'}
Set_Conjunto1.add(Objeto1.Tipo)

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Rock', 'Electricity', 'Water'})

print (f'{Set_Conjunto1}')

Set_Conjunto2 = {1, 2, 3, 4, 5}
Set_Conjunto3 = {4, 5}
Set_Conjunto4 = set({8})

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})

Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, Objeto1.Tipo})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Variable_Sumatoria,
    'Votante' : variable6
}

Diccionario2 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, True, False]
}

Diccionario3 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1["Nombre"]}')
print (f'{Diccionario1.get("Edad")}')

Diccionario1["Nombre"] = Lista_Uno_Copia[0]

print (f'{Diccionario1}')

del Diccionario1["Nombre"]
Diccionario1.pop("Edad")

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')

Diccionario1 = dict({1 : "Karlita", 2 : Variable_Sumatoria, 3 : not True})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'{Diccionario2.get("Nombre")[2]} no puede votar, ya que solo tiene {Diccionario1[2]} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', PEPE.Lista2[2])
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = Saludar_Dos()

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'El tipo de dato de la variable es {type(variable1)}')
print (f'El tipo de dato de la variable es {type(variable4)}')
print (f'El tipo de dato de la variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de dato de la variable es {type(variable7)}')
print (f'El tipo de dato de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato de la variable es {type(Variable_Funcion_Tupla)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de dato de la variable es {type(Diccionario_Vacio1)}')
print (f'El tipo de dato de la variable es {type(Funcion_Tupla)}')
print (f'El tipo de dato de la variable es {type(PEPE)}')
print (f'El tipo de dato de la variable es {type(Objeto3)}')
print (f'El tipo de dato de la variable es {type(Array_Concatenate)}')
print (f'El tipo de dato de la variable es {type(Data_Frame1_Age)}')

if (Diccionario3['Ingresos'] > 500):
    if (Diccionario3['Gastos'] < 200):
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200):
        print (f'Ingresos Altos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200):
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] == 500):
    if (Diccionario3['Gastos'] < 200):
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200):
        print (f'Ingresos Minimos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200):
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] < 500):
    if (Diccionario3['Gastos'] < 200):
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200):
        print (f'Ingresos Bajos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200):
        print (f'Ingresos Bajos, Gastos Altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')

if (Variable_Sumatoria < 100 and Saludar_Dos() == 'Carmelo'):
    print (f'Ambas condiciones son correctas')
else:
    print (f'Error, al menos una de las condiones no se cumple')

if (Diccionario1.get(2) == 'Karlita' or Saludar_Dos() == 'Carmlo'):
    print (f'Al menos una de las dos condiciones es correcta')
else:
    print (f'Ninguna de las condiciones se cumple')

print (f'{dir(variable1)}')

class Entrenador:
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = 15
        self.Classified  = Objeto3.Catched

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')

Objeto4 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto1.Nombre)
Objeto5 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto2.Nombre)
Objeto6 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto3.Nombre)

Objeto6.Desplegar()

Negativo = -5

print (f'{int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]
Anonima5 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)

print (f'{Any_Iterable}')
print (f'{Lista_Iterable}')
print (f'{list(Anonima5)}')

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, ingrese una cadena de texto')

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')

print (f'----------')

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'----------')

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'El elemento en la posicion {indice} es {elemento}')

print(f'----------')

for indice, elemento in Cargar_Csv.iterrows():
    Identificador = elemento['Nombre']

    print (f'Mi nombre es {Identificador}')

print(f'----------')

variable8 = 'eSteBAN'
letra8 = variable8[0]

print (f'{variable8}')
print (f'{variable8.lower()}')
print (f'{variable8.upper()}')
print (f'{variable8.capitalize()}')

print (f'{variable8.lower().find("t")}')
print (f'{variable8.lower().index("b")}')

print (f'La letra {letra8} aparece un total de {variable8.lower().count(letra8)} veces')

print (f'{variable8.lower().startswith(letra8)}')
print (f'{variable8.lower().endswith("n")}')

print (f'{variable8.lower().replace("ban", "POPOTAMO")}')

variable9 = 'esto es una cadena de texto de practica'
Lista_variable9 = variable9.split(' ')

for elemento in Lista_variable9:
    print (f'{elemento}')

print (f'La cantidad de palabras digitadas son {len(Lista_variable9)}')

print (f'{PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

for elemento in Diccionario1:
    print (f'{Diccionario1[elemento]}')

print(f'----------')

for elemento in Diccionario2.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'El resultado {Contador} es {PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1

Lista_Animales = ['Ave', 'Lagarto', 'Tortuga']
Lista_Animales.append('Leon')

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Lagarto'):
        print (f'Este reptil es terrorifico')
        break
    else:
        Contador+= 1
        continue

for elemento1, elemento2 in zip(Tupla1, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')

for elemento in range(5):
    print (f'{elemento}')

for elemento in range(995, 1000):
    print (f'{elemento}')

print(f'----------')

Lista_Numeros_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1

print(f'----------')

Menor = min(Lista_Numeros_Mult)
Mayor = max(Lista_Numeros_Mult)
Redondeo = round(14.458795, 2)
Sumatoria4 = sum(Lista_Numeros_Mult)

print (f'El numero menor de la lista es {Menor} y el mayor es {Mayor}')
print (f'El redondeo de 14.458795 es {Redondeo}')
print (f'El resultado de la sumatoria es {Sumatoria4}')

print (f'{bool(None)}')
print (f'{bool("")}')
print (f'{bool(False)}')
print (f'{bool(0)}')

Todo_All = all([Lista_variable9, Tupla2, Set_Conjunto_Menu1, None])

print (f'{Todo_All}')

Uno = int("500")
Dos = str(500)
Tres = float(Dos)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')

print (f' - '.join(Set_Conjunto_Menu1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

def Ejemplo1(Numero):
    return Variable_Sumatoria * Objeto2.Cantidad + Numero

print (f'El resultado de la sumatoria es {Ejemplo1(PEPE.Flotante1)}')

Resultado2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado2}')

def Cadena(Floto):
    Cade = Floto
    while True:
        try:
            Cadenita = str(Cade)
            Lista_Cadenita = Cadenita.split(' ')

            for elemento in enumerate(Lista_Cadenita):
                print (f'El elemento en la posicion {elemento[0]} es {elemento[1]}')

            print (f'La cantidad de palabras digitadas son {len(Lista_Cadenita)}')
            break
        except:
            print (f'Error, necesito que ingreses una cadena')

Cadena(PEPE.Flotante3)

Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio1(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del estudiante {elemento}: ')
        Lista.append(Alumno)

    return Lista

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nLa lista de estudiantes es {Colegio1(Lista_Alumnos)}'])
    Docu.close()

with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

Lista_Alumnos2 = []

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio2(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)

    Lista.sort(key = lambda Num : Num[1])

    Menore = Lista[0][0]
    Mayore = Lista[-1][0]

    print (f'El menor de los estudiantes es {Menore} y el mayor de los estudiantes es {Mayore}')

Colegio2(Lista_Alumnos2)

def Exception_Final():
    while True:
        Numero = input(f'Ingrese un numero entero: ')
        try:
            Numerito = int(Numero)
            break
        except:
            print (f'Error, necesito que ingreses un numero entero')

    return Numerito

print (f'Gracias, el numero ingresado es {Exception_Final()}')

import re

email = 'ericksuper80@gmail.com'

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

resultado = re.match(pattern, email)

if (resultado):
    print (f'Formato correcto')
else:
    print (f'Error, el formato es incorrecto')