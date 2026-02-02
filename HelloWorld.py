Numero = 20

def Funcion_Exception1():
    while True:
        Numero
        try:
            Numerito = int(Numero)
            break
        except ValueError:
            print (f'Error, necesito un numero entero')

    return Numerito

print (f'Gracias por el numero {Funcion_Exception1()}')

def Funcion_Exception2(Num1, Num2):
    try:
        Resultado = Num1 + Num2
        return Resultado
    except TypeError:
        return f'Error, necesito que ambos valores sean numeros'

print (f'{Funcion_Exception2(12, 5)}')

def Funcion_Exception3(Num1, Num2):
    try:
        Resultado = Num1 / Num2
        return Resultado
    except ZeroDivisionError:
        return f'El divisor no puede ser cero'

print (f'{Funcion_Exception3(15, 2)}')

Lista_Exception = list([])
Lista_Exception.extend(["Erick", "Josue", "Karlita"])

def Funcion_Exception4(Indice):
    try:
        print (f'El elemento en la posicion {Indice} es {Lista_Exception[Indice]}')
    except IndexError:
        print (f'El indice ingresado esta fuera de rango')

Funcion_Exception4(3)

Diccionario_Exception = dict.fromkeys(['Nombre', 'Edad'])

Set_Conjunto_Exception = {'Erick', 36}

for indice, elemento in enumerate(Set_Conjunto_Exception, start=1):
    if (elemento == 'Erick'):
        Diccionario_Exception['Nombre'] = elemento
    elif (elemento == 36):
        Diccionario_Exception['Edad'] = elemento
    else:
        continue

print (f'{Diccionario_Exception}')

def Funcion_Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception[Llave]}')
    except KeyError:
        print (f'La llave ingresada esta fuera de rango')

Funcion_Exception5("Votante")

try:
    import Module_Own as PEPE
except ImportError:
    print (f'El import seleccionado es incorrecto')

try:
    with open ('C:\\Repo\\HolaMundo.tx', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Durazno')
        Docu.close()

    with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
        Documento_Linea = Docu.readline()
        print (f'{Documento_Linea}')
        Docu.close()
except FileNotFoundError:
    print (f'El archivo no existe')

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
    'Edad' : [36, 20, 6],
    'Votante' : [True, True, False]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [67, 14, 26],
    'Votante' : [True, False, True]
})

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

print (f'{Data_Frame1}')

Data_Frame1_Age = Data_Frame1["Edad"]

print (f'{Data_Frame1_Age}')

print (f'La menor de las edades es {Data_Frame1_Age.min()} y la mayor de las edades es {Data_Frame1_Age.max()}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'--------------------')

Ruta_Csv = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv = pd.read_csv(Ruta_Csv)

print (f'{Cargar_Csv.head()}')

print (f'--------------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Cargar_Csv)

plt.show()

print (f'--------------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Ruta_Csv = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv = pd.read_csv(Ruta_Csv)

sns.barplot(x = 'Apellido', y = 'Edad', data=Cargar_Csv)

plt.show()

print (f'--------------------')

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'--------------------')

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'--------------------')

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'--------------------')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'El numero de filas es {Filas} y el de columnas es {Columnas}')

Elemento1 = Cargar_Csv.loc[0, "Edad"]
Elemento2 = Cargar_Csv.loc[0, "Nombre"]
Elemento3 = Cargar_Csv.loc[0, "Apellido"]

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')

Elemento4 = Cargar_Csv.loc[:, "Nombre"]

print (f'{Elemento4}')

Elemento5 = Cargar_Csv.loc[0, :]

print (f'{Elemento5}')

print (f'--------------------')

Elemento6 = Cargar_Csv.iloc[0, 0]
Elemento7 = Cargar_Csv.iloc[0, 1]
Elemento8 = Cargar_Csv.iloc[0, 2]
Elemento9 = Cargar_Csv.iloc[:, 1]
Elemento10 = Cargar_Csv.iloc[2, :]

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')
print (f'{Elemento9}')
print (f'{Elemento10}')

print (f'--------------------')

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine='openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'--------------------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=["Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez"])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tiquete')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:J", index_col='tiquete')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:J", index_col='tiquete', nrows=1)

print (f'{Cargar_Excel1.head()}')

print (f'--------------------')

print (f'{Cargar_Excel2.head()}')

print (f'--------------------')

print (f'{Cargar_Excel3.head()}')

print (f'--------------------')

print (f'{Cargar_Excel4.head()}')

print (f'--------------------')

print (f'{Cargar_Excel5.head()}')

print (f'--------------------')

print (f'{Cargar_Excel6.head()}')

print (f'--------------------')

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='Cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'--------------------')

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='Cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

print (f'--------------------')

print (f'{Cargar_Excel3["Seis"]}')

print (f'--------------------')

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt.head()}')

print (f'--------------------')

print (f'{Cargar_Txt}')

print (f'--------------------')

import pandas as pd

import requests

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Cargar_Html = pd.read_html(Response.text)

print (f'{Cargar_Html[2].head()}')

print (f'--------------------')

import numpy as np

Array1 = np.array([1, 2, 3])

print (f'{Array1}')
print (f'{Array1.ndim}') # 3
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

print (f'--------------------')

Array2 = np.array([[6, 2, 8], [5, 6, 7]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 1]}')
print (f'{Array2[0, :2]}')
print (f'{Array2[0, 2:]}')
print (f'{Array2[1, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[0, 1:2]}')
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

Sumatoria1 = np.sum(Array2_Sorted, axis=0)
Sumatoria2 = np.sum(Array2_Sorted, axis=1)
Sumatoria3 = np.sum(Array2_Sorted[0, 0:None])
Sumatoria4 = np.sum(Array2_Sorted[0, :])

print (f'{Sumatoria1}')
print (f'{Sumatoria2}')
print (f'{Sumatoria3}')
print (f'{Sumatoria4}')

print (f'--------------------')

Array3 = np.array([[['e', 'i', 'j'], ['d', 'k', 'x']],     [['a', 's', 'm'], ['o', 'n', 'r']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 1]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[1, 0, 1:2]}')
print (f'{Array3[0, :, 2]}')
print (f'{Array3[1, 1, 0:None]}')
print (f'{Array3[1, 1, :]}')
print (f'{Array3[Array3 == "a"]}')

print (f'--------------------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]],         [[7, 8, 9], [3, 2, 1]]],                           [[[6, 5, 4], [9, 8, 7]],           [[0, 4, 5], [2, 8, 6]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[0, 1, 0, 2]}')
print (f'{Array4[1, 1, 1, :2]}')
print (f'{Array4[1, 1, 1, 2:]}')
print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[0, 1, 1, ::3]}')
print (f'{Array4[0, 0, 1, 1:2]}')
print (f'{Array4[1, 0, :, 1]}')
print (f'{Array4[0, 1, 0, 0:None]}')
print (f'{Array4[0, 1, 0, :]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado {Array4_Sorted}')
print (f'Media {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria {Array4_Sorted_Sum}')

Sumatoria5 = np.sum(Array4_Sorted, axis=0)
Sumatoria6 = np.sum(Array4_Sorted, axis=1)
Sumatoria7 = np.sum(Array4_Sorted[1, 0, 1, 0:None])
Sumatoria8 = np.sum(Array4_Sorted[1, 0, 1, :])

print (f'{Sumatoria5}')
print (f'{Sumatoria6}')
print (f'{Sumatoria7}')
print (f'{Sumatoria8}')

print (f'--------------------')

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El numero menor de la lista es {Array_Num1_Min} y el numero mayor es {Array_Num1_Max}')

print (f'--------------------')

Array_Num2 = np.arange(25)

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

Array_Num2_Reshape_Column_Min = np.min(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Column_Max = np.max(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Row_Min = np.min(Array_Num2_Reshape, axis=1)
Array_Num2_Reshape_Row_Max = np.max(Array_Num2_Reshape, axis=1)

print (f'Los menores de las columnas son {Array_Num2_Reshape_Column_Min}')
print (f'Los mayores de las filas son {Array_Num2_Reshape_Column_Max}')
print (f'Los menores de las columnas son {Array_Num2_Reshape_Row_Min}')
print (f'Los mayores de las filas son {Array_Num2_Reshape_Row_Max}')

print (f'--------------------')

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 1]}')

print (f'--------------------')

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 2]}')

print (f'--------------------')

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 0]}')

print (f'--------------------')

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[3]}')

Lista_Array1 = list([])

for indice, elemento in enumerate(Array_Gen2, start=1):
    Lista_Array1.append(str(elemento))

print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'--------------------')

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[0, 1, 0, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[0, 0]}')

print (f'--------------------')

Tupla_Array = ('Rojo', 'Negro')
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value = Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value = Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value = Diccionario_Array["Nombre"][1])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'--------------------')

print (f'{Array_Gen6[3]}')

print (f'--------------------')

Array_Num3 = np.arange(start=1, stop=6, step=1)
Array_Num4 = np.arange(start=2, stop=6, step=2)
Array_Num5 = np.arange(start=3, stop=6, step=3)
Array_Num6 = np.arange(start=10, stop=6, step=2)
Array_Num7 = np.arange(10)

print (f'{Array_Num3}')
print (f'{Array_Num4}')
print (f'{Array_Num5}')
print (f'{Array_Num6}')
print (f'{Array_Num7}')

print (f'--------------------')

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')

print (f'--------------------')

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')
print (f'{Array_Random2.ndim}')
print (f'{Array_Random2.shape}')
print (f'{Array_Random2.size}')
print (f'{Array_Random2.dtype}')
print (f'{Array_Random2[1, 2]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Media = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado {Array_Random2_Sorted}')
print (f'Media {round(Array_Random2_Sorted_Media, 2)}')
print (f'Sumatoria {Array_Random2_Sorted_Sum}')

Sumatoria9 = np.sum(Array_Random2_Sorted, axis=0)
Sumatoria10 = np.sum(Array_Random2_Sorted, axis=1)
Sumatoria11 = np.sum(Array_Random2_Sorted[1, 0:None])
Sumatoria12 = np.sum(Array_Random2_Sorted[1, :])

print (f'{Sumatoria9}')
print (f'{Sumatoria10}')
print (f'{Sumatoria11}')
print (f'{Sumatoria12}')

print (f'--------------------')

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

print (f'--------------------')

Array_Num8 = np.arange(20)

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'--------------------')

Lista_Array2 = ['Erick', 'Josue', 'Karlita']

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'--------------------')

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concat([Array6, Array7])

print (f'{Array_Concatenate}')

Array_Concatenate_Split = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Split[0]}')
print (f'{Array_Concatenate_Split[1]}')
print (f'{Array_Concatenate_Split[2]}')

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'--------------------')

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'--------------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'--------------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'--------------------')

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Sumita1 = np.sum(Array_Random3, axis=0)
Sumita2 = np.sum(Array_Random3, axis=1)
Sumita3 = np.sum(Array_Random3[1, 0, 0:None])
Sumita4 = np.sum(Array_Random3[1, 0, :])

print (f'{Sumita1}')
print (f'{Sumita2}')
print (f'{Sumita3}')
print (f'{Sumita4}')

print (f'--------------------')

Tupla_Sorteo = tuple(('Erick', 'Josue', 'Karlita', 'Susanita', 'Roxana', 'Carmelo'))

Ganador1 = np.random.choice(Tupla_Sorteo, size=(1), replace=False)
Ganador2 = np.random.choice(Tupla_Sorteo, size=(2), replace=False)
Ganador3 = np.random.choice(Tupla_Sorteo, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'--------------------')

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'--------------------')

def Generadora1():
    for elemento in range(5):
        yield elemento

Gen1 = Generadora1()

print (f'{next(Gen1)}')
print (f'{next(Gen1)}')
print (f'{next(Gen1)}')
print (f'{next(Gen1)}')
print (f'{next(Gen1)}')

print (f'--------------------')

def Generadora2():
    for elemento in range(5):
        if (elemento % 2 == 0):
            yield f'El numero es par'
        else:
            yield f'El numero es impar'

Gen2 = Generadora2()

print (f'{next(Gen2)}')
print (f'{next(Gen2)}')
print (f'{next(Gen2)}')
print (f'{next(Gen2)}')
print (f'{next(Gen2)}')

print (f'--------------------')

def Generadora3():
        for elemento in range(5):
                if (elemento % 2 == 0):
                    yield f'PAR'
                else:
                    yield f'IMPAR'

Gen3 = Generadora3()

try:
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print(f'{next(Gen3)}')
except StopIteration:
    print (f'Este es el final del Generador 3')

print (f'--------------------')

import re

variable0 = 'esto es un texto solo para ver 5 si esta vara sirve o no 6'

Buscar1 = re.search('texto', variable0)

print (f'{Buscar1}')

Buscar2 = re.findall('a', variable0)

print (f'{Buscar2}')

print (f'--------------------')

Buscar3 = re.fullmatch('esto es un texto solo para ver si esta vara sirve o no', variable0)

print (f'{Buscar3}')

Buscar4 = re.search('\d', variable0)

print (f'{Buscar4}')

Buscar5 = re.search('\d+', variable0)

print (f'{Buscar5}')

Buscar6 = re.search('hol.', 'hole')

print (f'{Buscar6}')

Buscar7 = re.fullmatch('[a-zA-Z0-9]', 'hola123')

print (f'{Buscar7}')

print (f'--------------------')

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

PEPE.Par(Variable_Sumatoria)

PEPE.Usuario(Saludar_Dos(), 'MASCULINO')

def Usuario_Externa():
    def Usuario_Interna(Sexo):
        Genero = Sexo.lower()
        if (Genero == 'masculino'):
            return True
        else:
            return False

    return Usuario_Interna('MASCULINO')

Variable_Usuario = Usuario_Externa()

if (Variable_Usuario == True):
    print (f'YOU ARE A MAN')
else:
    print (f'YOU ARE A WOMAN')

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(87)}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.5, 60, "False")

print (f'{Funcion_Tupla("Perro", 3.5, 60, "False")}')
print (f'{Funcion_Tupla("Perro", 3.5, 60, "False")[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.5, 60, "False"))}')

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')

Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])

def Opera(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Opera(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def Opera2(Nombre, *args):
    return f'{Nombre} tu numero favorito es {sum(args)}'

print (f'{Opera2("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')

print (f'El doble de la variable {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

print (f'Los numeros pares de la lista son {list(Anonima3)}')

Any_Par = any(num % 2 == 0 for num in PEPE.Lista_Numeros)

Lista_Pares = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Par}')

print (f'{Lista_Pares}')

def Primera(Segunda):
    def Tercera(*args):
        return Segunda(*args) - 42

    return Tercera

@Primera
def Operacion(Numero:int) -> int:
    Local = Numero
    return PEPE.Global + Local

print (f'El resultado de la sumatoria es {Operacion(12)}')

def Externa(Nombre):
    def Interna(Apellido):
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

print (f'El multiplicador es {Variable_Mult1(10)}')
print (f'El multiplicador es {Variable_Mult2(10)}')

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
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
        return Segunda(*args, **kwargs) - 13

    return Tercera

@Primera
def Sum3(Num1, Num2):
    return Num2 + Num1

Resultado_Sumatoria3 = Sum3(7, 6)

print (f'El resultado de la operacion es {Sum3(12, 1)}')

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

Objeto2.Mostrar()
