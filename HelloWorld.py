variable1 = 69

def Ejemplo1(vari):
    try:
        Numero = int(vari)
        print (f'Gracias, el numero ingresado es {Numero}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Ejemplo1(variable1)

def Ejemplo2(Num1, Num2):
    try:
        return Num1 + Num2
    except TypeError:
        return f'Error, necesito que ambos elementos sean numeros'

print (f'{Ejemplo2(12, 3)}')

def Ejemplo3(Num1, Num2):
    try:
        return Num1 / Num2
    except ZeroDivisionError:
        return f'Error, el divisor no puede ser un numero zero'

print (f'{Ejemplo3(12, 6)}')

Lista_Ejemplo4 = list(['Erick', 'Josue', 'Karlita'])

def Ejemplo4(Indice):
    try:
        print (f'El elemento en la posicion {Indice} es {Lista_Ejemplo4[Indice]}')
    except IndexError:
        print (f'El indice seleccionado esta fuera de rango')

Ejemplo4(3)

Diccionario_Ejemplo5 = dict({'Nombre' : "Erick", 'Edad' : 36})

def Ejemplo5(Llave):
    try:
        print (f'El elemento de la llave {Llave} es {Diccionario_Ejemplo5[Llave]}')
    except KeyError:
        print (f'La llave seleccionada no esta dentro del rango')

Ejemplo5("Votante")

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Durazno')
        Docu.close()
except FileNotFoundError:
    print (f'El archivo no fue encontrado')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

try:
    import Module_Own as PEPE
except ImportError:
    print (f'El modulo seleccinado no existe')

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nManzana'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nUvas')
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

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke1"]}')
        Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke2"]}')
        Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke3"]}\n')
        Docu.close()
except FileNotFoundError:
    print (f'Error de archivo')

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
    'Edad' : [37, 14, 26],
    'Votante' : [True, False, True]
})

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

Data_Frame1_Age = Data_Frame1['Edad']

print (f'La menor de las edades es {Data_Frame1_Age.min()} y el mayor de las edades es {Data_Frame1_Age.max()}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'-----------')

print (f'{Data_Frame1}')

print (f'-----------')

print (f'{Data_Frame2["Nombre"]}')

print (f'-----------')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Data_Nombre = elemento['Nombre']
    Data_Edad = elemento['Edad']

    print (f'Mi nombre es {Data_Nombre} y su edad es {Data_Edad}')

print (f'-----------')

Ruta_Csv = 'C:\\Repo\\Base_Datos.csv'
Cargar_Csv = pd.read_csv(Ruta_Csv)

print (f'{Cargar_Csv.head()}')

print (f'-----------')

for indice, elemento in Cargar_Csv.iterrows():
    No = elemento['Nombre']
    Pe = elemento['Apellido']

    print (f'Hola {No} {Pe}')

print (f'-----------')

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Ruta_Csv = 'C:\\Repo\\Base_Datos.csv'
Cargar_Csv = pd.read_csv(Ruta_Csv)

sns.lineplot(x = 'Nombre', y = 'Edad', data=Cargar_Csv)

plt.show()

'''


print (f'-----------')

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Ruta_Csv = 'C:\\Repo\\Base_Datos.csv'
Cargar_Csv = pd.read_csv(Ruta_Csv)

sns.barplot(x = 'Nombre', y = 'Edad', data=Cargar_Csv)

plt.show()

'''

print (f'-----------')

print (f'{Cargar_Csv.head(1)}')

print (f'-----------')

print (f'{Cargar_Csv.head(3)}')

print (f'-----------')

print (f'{Cargar_Csv.tail(1)}')

print (f'-----------')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'La cantidad de filas son {Filas} y las columnas son {Columnas}')

print (f'-----------')

Elemento1 = Data_Frame1.loc[0, 'Nombre']
Elemento2 = Data_Frame1.loc[1, 'Edad']
Elemento3 = Data_Frame1.loc[2, 'Votante']
Elemento4 = Data_Frame1.loc[:, 'Edad']
Elemento5 = Data_Frame1.loc[2, :]

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')

print (f'-----------')

print (f'{Elemento4}')

print (f'-----------')

print (f'{Elemento5}')

print (f'-----------')

Elemento6 = Data_Frame2.iloc[0, 0]
Elemento7 = Data_Frame2.iloc[1, 1]
Elemento8 = Data_Frame2.iloc[2, 2]
Elemento9 = Data_Frame2.iloc[:, 1]
Elemento10 = Data_Frame2.iloc[0, :]

print (f'-----------')

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')

print (f'-----------')

print (f'{Elemento9}')

print (f'-----------')

print (f'{Elemento10}')

print (f'-----------')

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'
Cargar_Excel = pd.read_excel(Ruta_Excel, engine = 'openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'-----------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, names=["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, index_col='embarcado')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, usecols='E:K', index_col='embarcado')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, usecols='E:K', index_col='embarcado', nrows=0)

print (f'{Cargar_Excel1.head()}')

print (f'-----------')

print (f'{Cargar_Excel2.head()}')

print (f'-----------')

print (f'{Cargar_Excel3.head()}')

print (f'-----------')

print (f'{Cargar_Excel4.head()}')

print (f'-----------')

print (f'{Cargar_Excel5.head()}')

print (f'-----------')

print (f'{Cargar_Excel6.head()}')

print (f'-----------')

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='Five', ascending=True)
Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='Five', ascending=False)

print (f'{Cargar_Excel3_Sorted}')

print (f'-----------')

print (f'{Cargar_Excel3_Sorted_Descending}')

print (f'-----------')

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'
Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt.head()}')

print (f'-----------')

print (f'{Cargar_Txt}')

print (f'-----------')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Cargar_Html = pd.read_html(Response.text)

print (f'{Cargar_Html[2].head()}')

print (f'-----------')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Documento = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Documento)

print (f'{Cargar_Html[2].head()}')

print (f'-----------')

import numpy as np

Array1 = np.array([1, 2, 3])

print (f'{Array1}')
print (f'{Array1.ndim}') # 1
print (f'{Array1.shape}') # 1x3
print (f'{Array1.size}') # 3
print (f'{Array1.dtype}') # int64
print (f'{Array1[2]}')
print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[1:2]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 <= 2]}')

print (f'-----------')

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
print (f'{Array2[1, ::3]}')
print (f'{Array2[0, 1:2]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodados: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[0, 0:None])
Sumita4 = np.sum(Array2_Sorted[0, :])

print (f'{Sumita1}')
print (f'{Sumita2}')
print (f'{Sumita3}')
print (f'{Sumita4}')


print (f'-----------')

Array3 = np.array([[['r', 'k', 'a'], ['i', 'n', 'd']],       [['f', 's', 'w'], ['x', 'u', 'o']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 1]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 1, ::3]}')
print (f'{Array3[1, 1, 1:2]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "a"]}')

print (f'-----------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],            [[[6, 5, 4], [9, 8, 7]], [[0, 4, 8], [7, 3, 1]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 1, 0, 1]}')
print (f'{Array4[0, 1, 0, :2]}')
print (f'{Array4[0, 1, 0, 2:]}')
print (f'{Array4[1, 1, 0, ::2]}')
print (f'{Array4[1, 1, 1, ::3]}')
print (f'{Array4[0, 1, 0, 1:2]}')
print (f'{Array4[1, 0, :, 2]}')
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

print (f'-----------')

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Minimo = np.min(Array_Num1)
Maximo = np.max(Array_Num1)

print (f'El menor de los numeros es {Minimo} y el mayor es {Maximo}')

print (f'-----------')

Array_Num2 = np.arange(25)

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

print (f'-----------')

Array_Num2_Reshape_Column_Min = np.min(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Column_Max = np.max(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Row_Min = np.min(Array_Num2_Reshape, axis=1)
Array_Num2_Reshape_Row_Max = np.max(Array_Num2_Reshape, axis=1)

print (f'En las columnas los menores son {Array_Num2_Reshape_Column_Min}')
print (f'En las columnas los mayores son {Array_Num2_Reshape_Column_Max}')
print (f'En las filas los menores son {Array_Num2_Reshape_Row_Min}')
print (f'En las filas los mayores son {Array_Num2_Reshape_Row_Max}')

print (f'-----------')

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 1]}')

print (f'-----------')

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 2]}')

print (f'-----------')

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[0, 1]}')

print (f'-----------')

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

print (f'{Array_Gen2}')

Lista_Array1 = []

for elemento in Array_Gen2:
    Lista_Array1.append(str(elemento))

print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-----------')

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[0, 1, 1, 1:2])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 0]}')

print (f'-----------')

Tupla_Array = ('Rojo', 'Verde')
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array["Nombre"][2])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'-----------')

print (f'{Array_Gen6[3]}')

print (f'-----------')

Array_Num3 = np.arange(start=1, stop=6, step=1)
Array_Num4 = np.arange(start=2, stop=12, step=2)
Array_Num5 = np.arange(start=3, stop=33, step=3)
Array_Num6 = np.arange(start=2, stop=22, step=2)
Array_Num7 = np.arange(10)

print (f'{Array_Num3}')
print (f'{Array_Num4}')
print (f'{Array_Num5}')
print (f'{Array_Num6}')
print (f'{Array_Num7}')

print (f'-----------')

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')

print (f'-----------')

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')
print (f'{Array_Random2.ndim}')
print (f'{Array_Random2.shape}')
print (f'{Array_Random2.size}')
print (f'{Array_Random2.dtype}')
print (f'{Array_Random2[1, 2]}')

print (f'-----------')

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Sum = Arr1 + Arr2
Rest = Arr1 - Arr2
Mult = Arr1 * Arr2
Div = Arr1 / Arr2

Array_Random1_Cien = Array_Random1 + 100

print (f'El resutlado de la operacion es {Sum}')
print (f'El resutlado de la operacion es {Rest}')
print (f'El resutlado de la operacion es {Mult}')
print (f'El resutlado de la operacion es {Div}')
print (f'El resutlado de la operacion es {Array_Random1_Cien}')

print (f'-----------')

Array5 = np.arange(20)

print (f'{Array5}')

Array5_Reshape = np.reshape(Array5, shape=(4, 5))

print (f'{Array5_Reshape}')

Array5_Reshape_Ravel = np.ravel(Array5_Reshape)

print (f'{Array5_Reshape_Ravel}')

print (f'-----------')

Lista_Array2 = ['Erick', 'Josue', 'Karlita']

Array_Num8 = np.array(Lista_Array2)

print (f'{Array_Num8}')
print (f'{type(Array_Num8)}')

print (f'-----------')

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concat([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'-----------')

Array_Concatenate_Split = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Split[0]}')
print (f'{Array_Concatenate_Split[1]}')
print (f'{Array_Concatenate_Split[2]}')

print (f'-----------')

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'-----------')

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-----------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'-----------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'-----------')

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Sumita9 = np.sum(Array_Random3, axis=0)
Sumita10 = np.sum(Array_Random3, axis=1)
Sumita11 = np.sum(Array_Random3[1, 0, 0:None])
Sumita12 = np.sum(Array_Random3[1, 0, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

print (f'-----------')

Tupla_Array2 = tuple(('Erick', 'Josue', 'Karlita', 'Roxana', 'Carmelo', 'Susanita'))

Ganador1 = np.random.choice(Tupla_Array2, size=(1), replace=False)
Ganador2 = np.random.choice(Tupla_Array2, size=(2), replace=False)
Ganador3 = np.random.choice(Tupla_Array2, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-----------')

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-----------')

def Generadora1():
    for elemento in range(5):
        yield f'El elemento es {elemento}'

Gen1 = Generadora1()

try:
    print(f'{next(Gen1)}')
    print(f'{next(Gen1)}')
    print(f'{next(Gen1)}')
    print(f'{next(Gen1)}')
    print(f'{next(Gen1)}')
    print(f'{next(Gen1)}')
except StopIteration:
    print (f'El experimento termina aqui')

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
    print (f'El experimento termina aqui')

def Generadora3():
    for indice, elemento in enumerate(Lista_Array2, start=1):
        yield f'Mi nombre es {elemento}'

Gen3 = Generadora3()

try:
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
except StopIteration:
    print (f'El experimento termina aqui')

import re

variable2 = 'esto es un texto cualquiera que tiene el numero 4 y tambien podriamos decir que 5 es parte de la cadena'

Buscar1 = re.search('esto', variable2)
Buscar2 = re.findall('e', variable2)
Buscar3 = re.fullmatch('esto es un texto cualquiera que tiene el numero 4 y tambien podriamos decir que 5 es parte de la cadena', variable2)

print (f'{Buscar1}')
print (f'{Buscar2}')
print (f'{Buscar3}')

Buscar4 = re.search('\d', variable2)
Buscar5 = re.findall('\d+', variable2)
Buscar6 = re.fullmatch('\d+', '123')

print (f'{Buscar4}')
print (f'{Buscar5}')
print (f'{Buscar6}')

Buscar7 = re.search('[a-z]', variable2)
Buscar8 = re.search('^esto', variable2)
Buscar9 = re.search('cadena$', variable2)

print (f'{Buscar7}')
print (f'{Buscar8}')
print (f'{Buscar9}')

Buscar10 = re.search('h.la', 'helado')

print (f'{Buscar10}')

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

print (f'El resultado de la operacion es {Variable_Sumatoria}')

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

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nSu contrasena temporal es {PEPE.Contrasena(43)}'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.5, 60, True)

print (f'{Funcion_Tupla("Perro", 3.5, 60, True)}')
print (f'{Funcion_Tupla("Perro", 3.5, 60, True)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.5, 60, True))}')

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
print (f'Los numeros pares de la lista son {list(Anonima3)}')

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
    def Interna(Apellido):
        print (f'Mi nombre es {Nombre} {Apellido}')

    return Interna('PEREZ GUTIERREZ')

Externa('ERICK JOSUE')

def Closure_Externa():
    Lista_Closure = list([])
    def Closure_Interna(x):
        Lista_Closure.append(x)
        return Lista_Closure

    return Closure_Interna

Variable_Closure = Closure_Externa()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(28)}')
print (f'{Variable_Closure(34)}')

def Crear_Multiplicador(x):
    def Multiplicador(y):
        return x * y

    return Multiplicador

Variable_Mult1 = Crear_Multiplicador(2)
Variable_Mult2 = Crear_Multiplicador(3)

print (f'El mult 1 es {Variable_Mult1(10)}')
print (f'El mult 2 es {Variable_Mult2(10)}')

def Filtrador(Lista):
    Any_Impar = any(num % 2 == 0 for num in Lista)
    if (Any_Impar == True):
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impares = [num for num in Lista if num % 2 != 0]

        print (f'Los numeros impares de la lista son {list(Anonima4)} o incluso podrian ser {Lista_Impares}')
    else:
        print (f'No hay elementos impares en la lista')

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
        return Segunda(*args, **kwargs) - 11

    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(4, 7)}')

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

Objeto1 = Poke(PEPE.Diccionario_Poke["Poke1"], 'Electrico', 'Impact Trueno')
Objeto2 = Poke(PEPE.Diccionario_Poke["Poke2"], 'Roca', 'Sismo')
Objeto3 = Poke(PEPE.Diccionario_Poke["Poke3"], 'Agua', 'HidroChorro')

Objeto3.Mostrar()

print (f'Mi {PEPE.Diccionario_Poke["Poke1"]} es de tipo {Objeto1.Tipo}')

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable3 = Lista_Uno[0]
variable4 = 'Perez'
variable5 = '''Esto
Es
Un
Long
String'''

variable6 = Variable_Sumatoria
variable7 = PEPE.Division_Flotante
variable8, variable9 = True, Objeto3.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombrecito = elemento['Nombre']

    print (f'{Nombrecito}')

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable4}')

print (f'{PEPE.Tupla_Poke[2]} tiene {variable6}, {Sumatoria2(1, 2, 3, 4, 5)} o incluso podrian ser {Objeto2.Cantidad} pokemones')

del variable7

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable5)

Snake_Case1, Snake_Case2, Snake_Case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables {Snake_Case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

import pandas as pd
import requests
import io

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Pagina = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Pagina)

print (f'{Cargar_Html2[1].head()}')

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame1)

plt.show()

'''

Cociente, Residuo = divmod(Objeto2.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Un rango de elementos es {PEPE.Lista2[2:4]}')

print (f'{Lista_Uno[0]} acaba de ver un {PEPE.Lista2[2]}')

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
Lista_Uno.reverse()
print (f'{Lista_Cuatro}')

print (f'{PEPE.__dir__()}')

Tupla1 = ('Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde')

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Green', 'Blue'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Variable_Funcion_Tupla)}')

Set_Conjunto1 = {'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo'}
Set_Conjunto1.add('Verde')
Set_Conjunto1.add('Negro')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Red', 'Blue', 'Pink'})

print (f'{Set_Conjunto1}')

Set_Conjunto2 = {1, 2, 3, 4, 5}
Set_Conjunto3 = {4, 5}
Set_Conjunto4 = set({8})

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

print (f'{Set_Conjunto_Menu1}')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, Objeto2.Ataque})

print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Variable_Sumatoria,
    'Votante' : Objeto3.Catched
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

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2["Nombre"][0]}')
print (f'{Diccionario2.get("Edad")[2]}')

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3["Ingresos"]}')
print (f'{Diccionario3.get("Gastos")}')

Diccionario1["Nombre"] = Lista_Uno_Copia[0]

print (f'{Diccionario1}')

del Diccionario1["Nombre"]
Diccionario1.pop("Edad")

print (f'{Diccionario1}')

Diccionario1 = dict({1 : "Karlita", 2 : Variable_Sumatoria, 3 : variable9})

print (f'{Diccionario1}')

print (f'{Diccionario1.get(1)} no puede votar ya que solo tiene {Diccionario2["Edad"][2]} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'Hola')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = Objeto1.Tipo

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'{type(variable1)}')
print (f'{type(Variable_Sumatoria)}')
print (f'{type(Objeto2.Catched)}')
print (f'{type(PEPE.Division_Flotante)}')
print (f'{type(Lista_Uno_Copia)}')
print (f'{type(Set_Conjunto_Menu1)}')
print (f'{type(Set_Conjunto_Menu2)}')
print (f'{type(Tupla1)}')
print (f'{type(Diccionario_Ejemplo5)}')
print (f'{type(Funcion_Tupla)}')
print (f'{type(PEPE)}')
print (f'{type(Data_Frame_Concatenate)}')
print (f'{type(Array_Num8)}')

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

print (f'{dir(variable3)}')

class Entrenador:
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Variable_Sumatoria
        self.Classified = variable8

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')

Objeto4 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto1.Nombre)
Objeto5 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto2.Nombre)
Objeto6 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto3.Nombre)

Objeto6.Desplegar()

Negativo = -6

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
    print (f'Error, necesito que ingreses una cadena de texto')

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')

for indice, elemento in Data_Frame1.iterrows():
    Edaditas = elemento['Edad']

    print (f'{Edaditas}')

for elemento in enumerate(Set_Conjunto_Menu1):
    print (f'{elemento[0]} -- {elemento[1]}')

for indice, elemento in enumerate(Set_Conjunto1, start=1):
    print (f'El elemento en la posicion {indice} es {elemento}')

variable10 = 'eSteBAN'
letra_variable10 = variable10[0]

print (f'{variable10}')
print (f'{variable10.lower()}')
print (f'{variable10.upper()}')
print (f'{variable10.capitalize()}')

print (f'{variable10.lower().find("t")}')
print (f'{variable10.lower().index("b")}')

print (f'La letra {letra_variable10} aparece un total de {variable10.lower().count(letra_variable10)} veces')

print (f'{variable10.lower().startswith(letra_variable10)}')
print (f'{variable10.lower().endswith("n")}')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = 'este es un texto cualquiera para practicar'

Lista_variable11 = variable11.split(' ')

for elemento in Lista_variable11:
    print (f'{elemento}')

print (f'Usted ingreso un total de {Lista_variable11.__len__()} palabras')

print (f'{PEPE.Tupla_Poke[2]} aparece en la posicion {PEPE.Tupla_Poke.index("Misty")}')

for elemento in Diccionario1:
    print (f'{Diccionario1[elemento]}')

print (f'-------')

for elemento in Diccionario2.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1

Contador = 0

Lista_Animales = list(['Jirafa', PEPE.Lista2[2], 'Cocodrilo'])
Lista_Animales.append('Leon')

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Koala'):
        print (f'Me gusta el osito koala')
        break
    else:
        Contador+= 1
        continue

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1

for elemento1, elemento2 in zip(Lista_Uno_Copia, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')

for elemento in range(5):
    print (f'{elemento}')

for elemento in range(995, 1000):
    print (f'{elemento}')

Lista_Numeros_Mult = [num  * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Menor = min(Lista_Numeros_Mult)
Mayor = max(Lista_Numeros_Mult)
Sumatoria4 = sum(Lista_Numeros_Mult)
Redondeado = round(14.458795, 2)

print (f'El menor de los numeros es {Menor} y el mayor es {Mayor}')
print (f'El redondeado de 14.458795 es {Redondeado}')
print (f'El resultado de la sumatoria es {Sumatoria4}')

print (f'{bool(False)}')
print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool("")}')

Todo_All = all([Lista_Uno_Copia, Set_Conjunto_Menu1, ""])

print (f'{Todo_All}')

Uno = str('500')
Dos = int(Uno)
Tres = float(Dos)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')

print (f' - '.join(PEPE.Set_Conjunto_Poke))

def Flotante1(Numero):
    return Variable_Sumatoria * Objeto3.Cantidad + Numero

print (f'El resultado de la sumatoria es {Flotante1(PEPE.Flotante1)}')

def Flotante2():
    while True:
        Numero = input(f'Ingrese un numero entero: ')
        try:
            Numerito = int(Numero)
            break
        except:
            print (f'Error, necesito que ingrese un numero entero')

    return Numerito

print (f'Gracias, su numero digitado es {Flotante2()}')

Resultado3 = eval(PEPE.Flotante3)

print (f'El resultado de la operacion es {Resultado3}')

def Flotante4(Cadenita):
    Lista_Cadenita = Cadenita.split(' ')
    for elemento in enumerate(Lista_Cadenita):
        print (f'{elemento[0]} -- {elemento[1]}')

    print (f'El numero de palabras digitadas es {Lista_Cadenita.__len__()}')

Flotante4(PEPE.Flotante4)

Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio1(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del estudiante {elemento}: ')
        Lista.append(Alumno)

    return Lista

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nLa lista de estudiantes es {Colegio1(Lista_Alumnos)}')
    Docu.close()

with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

Lista_Alumnos2 = list([])

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio2(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del estudiante {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del estudiante {elemento}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)

    Lista.sort(key = lambda Num : Num[1])

    Menore = Lista[0][0]
    Mayore = Lista[-1][0]

    print (f'El menor de los estudiantes es {Menore} y el mayor de los estudiantes es {Mayore}')

Colegio2(Lista_Alumnos2)

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3