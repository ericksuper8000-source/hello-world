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

var1 = True

try:
    Numero = int(var1)
    print (f'Gracias, este es su numero {Numero}')
except ValueError:
    print (f'Necesito que ingreses un numero entero')

def Sum5(Num1, Num2):
    while True:
        try:
            Resultado_Num = Num1 + Num2
            break
        except TypeError:
            return f'Necesito que ambos elementos sean numeros'

    return Resultado_Num

print (f'El resultado de la sumatoria es {Sum5(15, 1)}')

def Div2(Num1, Num2):
    while True:
        try:
            Division = Num1 / Num2
            break
        except ZeroDivisionError:
            return f'El divisor no puede ser cero'

    return Division

print (f'{Div2(12, 7)}')

Diccionario_Exception2 = dict({'Nombre' : "Erick", 'Edad' : 36})

Lista_Exception2 = ['Erick', 'Koala', True]

def Exception_Nueva(Indice):
    try:
        return f'El elemento en el indice {Indice} es {Lista_Exception2[Indice]}'
    except IndexError:
        return f'El indice seleccionado esta fuera de rango'

print (f'{Exception_Nueva(3)}')

def Exception_Nueva2(Llave):
    try:
        yield f'El elemento en la llave {Llave} es {Diccionario_Exception2[Llave]}'
    except KeyError:
        yield f'La llave seleccionada esta fuera de rango, no existe'

Variable_Next = Exception_Nueva2("Carolina")

print (f'{next(Variable_Next)}')

try:
    import Module_Own as POPO
except ImportError:
    print (f'El import seleccionado no existe o es incorrecto')

try:
    with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.writelines([f'\nHola Bebe'])
        Docu.close()
except FileNotFoundError:
    print (f'El archivo no se encontro, no existe este txt')

with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Cargar_Csv)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Cargar_Csv)

plt.show()

def Generator1():
    for elemento in range(5):
                yield elemento

Gen_1 = Generator1()

print (f'{next(Gen_1)}')
print (f'{next(Gen_1)}')
print (f'{next(Gen_1)}')
print (f'{next(Gen_1)}')
print (f'{next(Gen_1)}')

def Generator2():
    for elemento in range(5):
        if (elemento % 2 == 0):
            yield f'PAR'
        else:
            yield f'IMPAR'

Gen_2 = Generator2()

print (f'{next(Gen_2)}')
print (f'{next(Gen_2)}')
print (f'{next(Gen_2)}')
print (f'{next(Gen_2)}')
print (f'{next(Gen_2)}')

print (f'--------------')

def Generator3():
    for elemento in range(5):
        if (elemento % 2 == 0):
            yield f'PAR'
        else:
            yield f'IMPAR'

Gen_3 = Generator3()

try:
    print (f'{next(Gen_3)}')
    print (f'{next(Gen_3)}')
    print (f'{next(Gen_3)}')
    print (f'{next(Gen_3)}')
    print (f'{next(Gen_3)}')
    print(f'{next(Gen_3)}')
except StopIteration:
    print (f'Aqui termina el ejercicio')

import re

variable0_1 = 'este es un texto cualquiera que va a tener el numero 1 y tambien el numero 123 pero lo mas importante es un @ arroba'

Buscador1 = re.search('numero', variable0_1)

print (f'{Buscador1}')

Buscador2 = re.findall('a', variable0_1)

print (f'{Buscador2}')

Buscador3 = re.fullmatch('este iso es un texto cualquiera que va a tener oso el Numero 1 y tambien aso el numero 123 pero lo mas Importante es un @ arroba eso', variable0_1)

print (f'{Buscador3}')

Buscador4 = re.search('\d', variable0_1)

print (f'{Buscador4}')

Buscador5 = re.findall('\d+', variable0_1)

print (f'{Buscador5}')

Buscador6 = re.fullmatch('\d+', variable0_1)

print (f'{Buscador6}')

Buscador7 = re.search('.so', 'eso')
Buscador8 = re.findall('.so', 'eso')
Buscador9 = re.fullmatch('.so', 'eso')

print (f'{Buscador7}')
print (f'{Buscador8}')
print (f'{Buscador9}')

Buscador10 = re.search('[a-z]', variable0_1)
Buscador101 = re.findall('[a-z]', variable0_1)
Buscador102 = re.fullmatch('[a-z]', variable0_1)

print (f'{Buscador10}')
print (f'{Buscador101}')
print (f'{Buscador102}')

Buscador13 = re.search('^este', variable0_1)
Buscador14 = re.search('arroba$', variable0_1)

print (f'{Buscador13}')
print (f'{Buscador14}')

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un
Long
String'''

variable4 = Sum5(Variable_Sumatoria, Objeto3.Cantidad)
variable5 = PEPE.Division_Flotante
variable6, variable7 = True, Objeto2.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke3"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

def Ejemplo_Sum(*args):
    return sum(args)

print (f'{PEPE.Tupla_Poke[2]} tiene {Variable_Sumatoria}, {Ejemplo_Sum(1, 2, 3, 4, 1)} o incluso {Objeto3.Cantidad} {PEPE.Diccionario_Poke["Poke1"]}s')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

Snake_Case1, Snake_Case2, Snake_Case3 = PEPE.Tupla_Poke

print (f'{Snake_Case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto1.Cantidad, Ejemplo_Sum(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Un rango de elementos de la lista 2 es {PEPE.Lista2[2:4]}')

print (f'{Lista_Uno[2]} acaba de ver un {PEPE.Lista2[2]} por primera vez en su vida')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Ejemplo_Sum(Anonima2(250), 150, 50, 200, 100)

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

Tupla1 = ('Uno', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos')

print (f'{Tupla1}')

Tupla1 = tuple(('Uno', 'Dos', 'Tres'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Funcion_Tupla())}')

Set_Conjunto1 = {'Electrico', Objeto1.Tipo, Objeto1.Tipo, Objeto1.Tipo, Objeto1.Tipo}
Set_Conjunto1.add('Fuego')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Electric', 'Fire', 'Water'})

print (f'{Set_Conjunto1}')

Set_Conjunto2 = {1, 2, 3, 4, 5}
Set_Conjunto3 = {3, 4}
Set_Conjunto4 = set({8})

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})
Set_Conjunto_Menu3 = set({Objeto3.Nombre, Set_Conjunto_Menu2})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Variable_Sumatoria,
    'Votante' : variable7
}

Diccionario2 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [36, 20, 6],
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
print (f'{Diccionario2.get("Edad")[1]}')

Diccionario1["Nombre"] = variable1

print (f'{Diccionario1}')

del Diccionario1["Nombre"]
Diccionario1.pop("Edad")

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')

Diccionario1 = dict({1 : "Karlita", 2 : 6, 3 : False})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'{Diccionario1.get(1)} no puede votar, ya que solo tiene {Diccionario2["Edad"][2]} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'Hola Mundo')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2["Dos"] = variable2

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
print (f'El tipo de dato de la variable es {type(Objeto2.Catched)}')
print (f'El tipo de dato de la variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de dato de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato de la variable es {type(Tupla1)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de dato de la variable es {type(Diccionario_Vacio1)}')
print (f'El tipo de dato de la variable es {type(Funcion_Diccionario)}')
print (f'El tipo de dato de la variable es {type(PEPE)}')
print (f'El tipo de dato de la variable es {type(Array5)}')
print (f'El tipo de dato de la variable es {type(Data_Frame2)}')

if (Diccionario3['Ingresos'] > 500):
    if (Diccionario3['Gastos'] < 200):
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200):
        print (f'Ingresos Altos, Gastos Al Maximo')
    elif (Diccionario3['Gastos'] > 200):
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] == 500):
    if (Diccionario3['Gastos'] < 200):
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200):
        print (f'Ingresos Minimos, Gastos Al Maximo')
    elif (Diccionario3['Gastos'] > 200):
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] < 500):
    if (Diccionario3['Gastos'] < 200):
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200):
        print (f'Ingresos Bajos, Gastos Al Maximo')
    elif (Diccionario3['Gastos'] > 200):
        print (f'Ingresos Bajos, Gastos Altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')

print (f'{variable1.__dir__()}')

class Entrenador:
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Variable_Sumatoria
        self.Classified  = True

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')

Objeto4 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto1.Nombre)
Objeto5 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto2.Nombre)
Objeto6 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto3.Nombre)

Objeto5.Desplegar()

Negativo = -5

print (f'{int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima5 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable}')
print (f'{list(Anonima5)}')
print (f'{Lista_Iterable}')

print (f'El binario de {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, ingrese una cadena de texto')

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')

for elemento1, elemento2 in zip(Lista_Uno_Copia, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')

variable8 = 'eSteBAN'
variable8_letra = variable8[0]

print (f'{variable8}')
print (f'{variable8.lower()}')
print (f'{variable8.upper()}')
print (f'{variable8.capitalize()}')

print (f'{variable8.lower().find("t")}')
print (f'{variable8.lower().index("b")}')

print (f'La letra {variable8_letra} aparece un total de {variable8.lower().count(variable8_letra)} veces')

print (f'{variable8.lower().startswith(variable8_letra)}')
print (f'{variable8.lower().endswith("n")}')

print (f'{variable8.lower().replace("ban", "POPOTAMO")}')

variable9 = 'esto es un texto cualquiera solo para ver si la mica funciona'

variable9_lista = variable9.split(' ')

for indice, elemento in enumerate(variable9_lista, start=1):
    print (f'En la posicion {indice} aparece el elemento {elemento}')

print (f'La cantidad de palabras escritas es {variable9_lista.__len__()}')

print (f'{PEPE.Tupla_Poke[2]} aparece en la poscion {PEPE.Tupla_Poke.index("Misty")}')

for elemento in Diccionario1:
    print (f'{Diccionario1[elemento]}')

for elemento in Diccionario2.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Contador1 = 0

while (Contador1 <= 5):
    print (f'El contador es {Contador1}')
    Contador1+= 1

Contador1 = 0

while (Contador1 < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador1] * 100}')
    Contador1+= 1

Lista_Animales = ['Zorro', 'Gato', 'Raton', 'Perro']

Contador1 = 0

while (Contador1 < len(Lista_Animales)):
    if (Lista_Animales[Contador1] == 'Raton'):
        print (f'Mouse')
        break
    else:
        Contador1+= 1
        continue

for elemento in range(5):
    print (f'{elemento}')

for elemento in range(995, 1000):
    print (f'{elemento}')

Lista_Numeros_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Num_Min = min(Lista_Numeros_Mult)
Num_Max = max(Lista_Numeros_Mult)
Redondeo = round(14.458795, 2)
Sumatoria_Final = sum(Lista_Numeros_Mult)

print (f'El menor de los numeros es {Num_Min} y el mayor es {Num_Max}')

print (f'El numero redondeado 14.458795 es {round(Redondeo)}')

print (f'{bool(False)}')
print (f'{bool("")}')
print (f'{bool(None)}')
print (f'{bool(0)}')

Todo_All = all([Lista_Animales, Tupla1, Set_Conjunto4, None])

print (f'{Todo_All}')

Uno = str("500")
Dos = int(Uno)
Tres = float(Uno)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')

print (f' - '.join(PEPE.Set_Conjunto_Poke))

def Ej_Final(Numero):
    return f'{Variable_Sumatoria * Objeto1.Cantidad + Numero}'

print (f'El resultado de la operacion es {Ej_Final(PEPE.Flotante1)}')

Resultado_Final = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado_Final}')

def Contadore(Listilla):
    Lista_Numero = Listilla.split(' ')
    for elemento in Lista_Numero:
        print (f'{elemento}')

    print (f'La cantidad de palabras digitadas son {Lista_Numero.__len__()}')

Contadore(PEPE.Flotante3)

Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio1(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento}: ')
        Lista.append(Alumno)

    return Lista

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nLa lista de estudiantes es {Colegio1(Lista_Alumnos)}')
    Docu.close()

with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

Lista_Alumnos2 = list([])

Contador = int(input(f'Ingrese el numero de estudiantes: '))


def Colegio2(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]

        Lista.append(Estudiante)

    Lista.sort(key=lambda Num: Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]

    print(f'El menor de los estudiantes es {Menore} y el mayor de los estudiantes es {Mayore}')


Colegio2(Lista_Alumnos2)

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

variable_PEPE3 = PEPE3

def Fin():
    while True:
        Numero = input(f'Ingrese un numero entero: ')
        try:
            Numerito = int(Numero)
            break
        except ValueError:
            print (f'Error, necesito que ingreses un numero')

    return Numerito

print (f'Gracias, el numero digitado es {Fin()}')