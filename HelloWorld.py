import Module_Own as PEPE
from pandas.io.sas.sas_constants import encoding_length
from soupsieve.util import lower

with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
    Documento_SobreEscribir = Docu.write(f'Durazno')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

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
    'Edad' : [36, 20, 6],
    'Votante' : [True, True, False]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [66, 16, 26],
    'Votante' : [True, False, True]
})

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

print (f'{Data_Frame1}')

print (f'----------------')

Data_Frame1_Age = Data_Frame1["Edad"]

print (f'{Data_Frame1_Age}')

print (f'La menor de las edades es {Data_Frame1_Age.min()} y la mayor de las edades es {Data_Frame1_Age.max()}')

print (f'----------------')

print (f'{Data_Frame2.info()}')

print (f'----------------')

print (f'{Data_Frame_Concatenate}')

print (f'----------------')

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'----------------')

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'----------------')

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'----------------')

Fila, Columna = Data_Frame_Concatenate.shape

print (f'La cantidad de filas es {Fila} y la de columnas es {Columna}')

print (f'----------------')

Elemento1 = Data_Frame1.loc[0, "Nombre"]

print (f'{Elemento1}')

Elemento2 = Data_Frame2.loc[2, "Edad"]

print (f'{Elemento2}')

Elemento3 = Data_Frame1.iloc[1, 2]

print (f'{Elemento3}')

Elemento4 = Data_Frame2.iloc[0, 1]

print (f'{Elemento4}')

print (f'----------------')

Elemento5 = Data_Frame1.loc[:, "Nombre"]

print (f'{Elemento5}')

print (f'----------------')

Elemento6 = Data_Frame2.iloc[:, 2]

print (f'{Elemento6}')

print (f'----------------')

Elemento7 = Data_Frame1.loc[1, :]

print (f'{Elemento7}')

print (f'----------------')

Elemento8 = Data_Frame2.iloc[0, :]

print (f'{Elemento8}')

import pandas as pd

import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine='openpyxl')

print (f'{Cargar_Excel}')

print (f'----------------')

Elemento9 = Cargar_Excel.loc[0, "nombre"]
Elemento10 = Cargar_Excel.loc[1, "cabina"]
Elemento11 = Cargar_Excel.loc[2, "clase"]

print (f'{Elemento9}')
print (f'{Elemento10}')
print (f'{Elemento11}')

print (f'----------------')

Elemento12 = Cargar_Excel.iloc[0, 3]
Elemento13 = Cargar_Excel.iloc[1, 7]
Elemento14 = Cargar_Excel.iloc[2, 2]

print (f'{Elemento12}')
print (f'{Elemento13}')
print (f'{Elemento14}')

print (f'----------------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=["Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez"])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col="tarifa")
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:K", index_col="cabina")
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:K", index_col="cabina", nrows=1)

print (f'{Cargar_Excel1}')

print (f'----------------')

print (f'{Cargar_Excel2}')

print (f'----------------')

print (f'{Cargar_Excel3}')

print (f'----------------')

print (f'{Cargar_Excel4}')

print (f'----------------')

print (f'{Cargar_Excel5}')

print (f'----------------')

print (f'{Cargar_Excel6}')

print (f'----------------')

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by = "Cinco", ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'----------------')

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by = "Cinco", ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'----------------')

print (f'{Cargar_Txt.head()}')

print (f'----------------')

import pandas as pd

Ruta_Csv = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv = pd.read_csv(Ruta_Csv)

print (f'{Cargar_Csv.head()}')

print (f'----------------')

import pandas as pd

import requests

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Cargar_Html = pd.read_html(Response.text)

print (f'{Cargar_Html[2].head()}')

print (f'----------------')

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

print (f'----------------')

Array2 = np.array([[6, 9, 0], [3, 2, 1]])

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
print (f'{Array2[1, 1:2]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[0, :]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[1, 0:None])
Sumita4 = np.sum(Array2_Sorted[1, :])

print (f'El resultado de la sumita es {Sumita1}')
print (f'El resultado de la sumita es {Sumita2}')
print (f'El resultado de la sumita es {Sumita3}')
print (f'El resultado de la sumita es {Sumita4}')

print (f'----------------')

Array3 = np.array([[['e', 'i', 'm'], ['f', 'l', 'u']],      [['v', 'x', 's'], ['w', 'r', 'n']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[0, 1, 1]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[1, 1, ::3]}')
print (f'{Array3[0, 0, 1:2]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "e"]}')

print (f'----------------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],       [[[6, 5, 4], [9, 8, 7]], [[4, 3, 8], [6, 1, 7]]]])

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

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 2]}')

print (f'{Array4[1, 1, 0, :2]}')
print (f'{Array4[1, 1, 0, 2:]}')
print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[0, 1, 1, ::3]}')
print (f'{Array4[0, 0, 0, 1:2]}')
print (f'{Array4[1, 1, :, 1]}')
print (f'{Array4[0, 1, 0, 0:None]}')
print (f'{Array4[0, 1, 0, :]}')
print (f'{Array4[Array4 <= 2]}')

print (f'----------------')

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El numero menor de la lista es {Array_Num1_Min} y el mayor es {Array_Num1_Max}')

print (f'----------------')

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

print (f'----------------')

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 1]}')

print (f'----------------')

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 2]}')

print (f'----------------')

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 1]}')

print (f'----------------')

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

print (f'{Array_Gen2}')

Lista_Array1 = list([])

for elemento in enumerate(Array_Gen2):
    Lista_Array1.append(str(elemento[1]))

print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'----------------')

Array_Gen3 = np.full(shape=(2, 3), fill_value = int(Array4[0, 1, 1, 2]))

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 0]}')

print (f'----------------')

Tupla_Array1 = ('Rojo', 'Negro')
Set_Conjunto_Array1 = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value = Tupla_Array1)
Array_Gen5 = np.full(shape=(2, 1), fill_value = Set_Conjunto_Array1)
Array_Gen6 = np.full(shape=(4, 1), fill_value = Diccionario_Array["Nombre"][1])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'----------------')

print (f'{Array_Gen6[2]}')

print (f'----------------')

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

print (f'----------------')

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')

print (f'----------------')

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

print (f'{Array_Random2_Sorted}')
print (f'{round(Array_Random2_Sorted_Mean, 2)}')
print (f'{Array_Random2_Sorted_Sum}')

Sumita9 = np.sum(Array_Random2_Sorted, axis=0)
Sumita10 = np.sum(Array_Random2_Sorted, axis=1)
Sumita11 = np.sum(Array_Random2_Sorted[0, 0:None])
Sumita12 = np.sum(Array_Random2_Sorted[0, :])

print (f'El resultado de la sumita {Sumita9}')
print (f'El resultado de la sumita {Sumita10}')
print (f'El resultado de la sumita {Sumita11}')
print (f'El resultado de la sumita {Sumita12}')

print (f'----------------')

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

print (f'----------------')

Array_Num8 = np.arange(20)

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'----------------')

Lista_Array2 = ["Erick", "Josue", "Karlita"]

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'----------------')

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

print (f'----------------')

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'----------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'----------------')

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Sumita13 = np.sum(Array_Random3, axis=0)
Sumita14 = np.sum(Array_Random3, axis=1)
Sumita15 = np.sum(Array_Random3[1, 0, 0:None])
Sumita16 = np.sum(Array_Random3[1, 0, :])

print (f'El resultado de la sumita es {Sumita13}')
print (f'El resultado de la sumita es {Sumita14}')
print (f'El resultado de la sumita es {Sumita15}')
print (f'El resultado de la sumita es {Sumita16}')

print (f'----------------')

Tupla_Array2 = tuple(("Erick", "Josue", "Karlita", "Roxana", "Susanita", "Carmelo"))

Ganador1 = np.random.choice(Tupla_Array2, size=(1), replace=False)
Ganador2 = np.random.choice(Tupla_Array2, size=(2), replace=False)
Ganador3 = np.random.choice(Tupla_Array2, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'----------------')

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'----------------')

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(7, 2)}')

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

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(87)}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla('Perro', 36, 3.5, False)

print (f'{Funcion_Tupla("Perro", 36, 3.5, False)}')
print (f'{Funcion_Tupla("Perro", 36, 3.5, False)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 36, 3.5, False))}')

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

print (f'El resultado de la multiplicacion es {Anonima1(150 ,3)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

Any_Par = any(num % 2 == 0 for num in PEPE.Lista_Numeros)

Lista_Pares = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'Los numeros pares de la lista son {list(Anonima3)} o incluso podrian ser {Lista_Pares}')
print (f'{Any_Par}')

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

    return Interna("PEREZ GUTIERREZ")

Externa("ERICK JOSUE")

def Closure_Externo():
    Lista_Closure = list([])
    def Closure_Interno(x):
        Lista_Closure.append(x)

        return Lista_Closure

    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(20)}')
print (f'{Variable_Closure(31)}')

def Closure_Crear_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y

    return Closure_Multiplicador

Variable_Closure1 = Closure_Crear_Multiplicador(2)
Variable_Closure2 = Closure_Crear_Multiplicador(3)

print (f'El multiplicador 1 es {Variable_Closure1(10)}')
print (f'El multiplicador 2 es {Variable_Closure2(10)}')

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
        return Segunda(*args, **kwargs) - 10

    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(5, 9)}')

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonathan'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)

    return Tercera

@Primera
def Usuario2(Nombre:str, Apellido:str) -> str:
    return f'Mi nombre es {Nombre} {Apellido}'

print (f'{Usuario2("Erick", "Josue")}')

from Module_Own import Pokemon as Poke

Objeto1 = Poke(PEPE.Diccionario_Poke["Poke1"], 'Electrico', 'Impact Trueno')
Objeto2 = Poke(PEPE.Diccionario_Poke["Poke2"], 'Roca', 'Sismo')
Objeto3 = Poke(PEPE.Diccionario_Poke["Poke3"], 'Agua', 'Hidro Chorro')

Objeto2.Mostrar()

print (f'Yo tengo {Objeto3.Cantidad} {PEPE.Diccionario_Poke["Poke3"]}s')

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
variable6, variable7 = True, Objeto3.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')
print (f'Mi nombre es {Lista_Uno[0]} {variable2}')
print (f'Yo tengo {Variable_Sumatoria} {PEPE.Diccionario_Poke["Poke2"]}s')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

Snake_Case1, Snake_Case2, Snake_Case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables {Snake_Case2}')

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto1.Cantidad, Variable_Sumatoria)

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Un rango de elementos es {PEPE.Lista2[2:4]}')

print (f'{Lista_Uno[1]} tiene un {PEPE.Lista2[3]}')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, 200, 100)

print (f'{Lista_Cuatro}')

del Lista_Uno[1]
Lista_Uno.remove('Coco Rayado')
Lista_Uno.pop(-2)
Lista_Uno.pop(-1)
Lista_Uno.pop(-1)

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno_Copia = Lista_Uno.copy()

Lista_Uno.clear()

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'{PEPE.__dir__()}')

Tupla1 = ('Rojo', 'Verde', 'Azul')

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Green', 'Blue'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')

Set_Conjunto1 = {5, 5, 5, 5, 5, 5, 5}
Set_Conjunto1.add(6)

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({1, 2, 3})

print (f'{Set_Conjunto1}')

Set_Conjunto2 = set({1, 2, 3, 4, 5})
Set_Conjunto3 = {4, 5}
Set_Conjunto4 = {9}

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')

Set_Conjunto_Menu = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})
Set_Conjunto_Menu3 = {Set_Conjunto_Menu2, Objeto2.Nombre}

print (f'{Set_Conjunto_Menu}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Variable_Sumatoria,
    'Votante' : Objeto1.Catched
}

Diccionario2 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [36, 20, 6],
    'Votante' : [True, True, False]
}

Diccionario3 = {
    'Ingresos' : 501,
    'Gastos' : 199,
    'Vacio' : "q"
}

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

Diccionario1 = dict({1 : "Karlita", 2 : 2, 3 : False})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'{Diccionario1.get(1)} no puede votar ya que solo tiene {Diccionario2["Edad"][2]} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABCD', Saludar_Dos())
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = PEPE.Diccionario_Poke['Poke1']

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la variable es {PEPE.Division_Flotante}')
print (f'El resultado de la variable es {int(abs(Division_Baja))}')
print (f'El resultado de la variable es {Exponente}')
print (f'El resultado de la variable es {Modulo}')

print (f'El tipo de dato es {type(variable1)}')
print (f'El tipo de dato es {type(variable4)}')
print (f'El tipo de dato es {type(PEPE.Division_Flotante)}')
print (f'El tipo de dato es {type(Objeto1.Catched)}')
print (f'El tipo de dato es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato es {type(Tupla1)}')
print (f'El tipo de dato es {type(Set_Conjunto_Menu)}')
print (f'El tipo de dato es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de dato es {type(Diccionario1)}')
print (f'El tipo de dato es {type(Funcion_Tupla)}')
print (f'El tipo de dato es {type(PEPE)}')
print (f'El tipo de dato es {type(Array5)}')
print (f'El tipo de dato es {type(Data_Frame_Concatenate)}')

if (Diccionario3["Ingresos"] > 500):
    if (Diccionario3["Gastos"] < 200):
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario3["Gastos"] == 200):
        print (f'Ingresos Altos, Gastos Al Limite')
    elif (Diccionario3["Gastos"] > 200):
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3["Ingresos"] == 500):
    if (Diccionario3["Gastos"] < 200):
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario3["Gastos"] == 200):
        print (f'Ingresos Minimos, Gastos Al Limite')
    elif (Diccionario3["Gastos"] > 200):
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3["Ingresos"] < 500):
    if (Diccionario3["Gastos"] < 200):
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario3["Gastos"] == 200):
        print (f'Ingresos Bajos, Gastos Al Limite')
    elif (Diccionario3["Gastos"] > 200):
        print (f'Ingresos Bajos, Gastos Altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')

print (f'{dir(variable1)}')

class Entrenador:
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Variable_Sumatoria
        self.Clasificado = True

    def Desplegar(self):
        print (f'{self.Trainer}, just catched a {self.Favorite} while visiting {self.City}')

Objeto4 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto1.Nombre)
Objeto5 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto2.Nombre)
Objeto6 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto3.Nombre)

Objeto5.Desplegar()

Negativo = -5

print (f'{int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]
Anonima4 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)

print (f'{Any_Iterable}')
print (f'{Lista_Iterable}')
print (f'{list(Anonima4)}')

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3["Vacio"]) == True):
    print (f'Gracias por la informadcion')
else:
    print (f'Error, ingrese una cadena de texto')

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'El elemento en la posicion {indice} es {elemento}')

for elemento1, elemento2 in zip(Lista_Uno_Copia, Set_Conjunto1):
    print (f'{elemento1} -- {elemento2}')

variable8 = 'eSteBAN'
letra = variable8[0]

print (f'{variable8}')
print (f'{variable8.lower()}')
print (f'{variable8.upper()}')
print (f'{variable8.capitalize()}')

print (f'{variable8.lower().index("t")}')
print (f'{variable8.lower().find("b")}')

print (f'La letra {letra} aparece un total de {variable8.lower().count(letra)} veces')

print (f'{variable8.lower().startswith(letra)}')
print (f'{variable8.lower().endswith("n")}')

print (f'{variable8.lower().replace("ban", "POPOTAMO")}')

variable9 = 'esto es un texto cualquiera, pero por el momento quiero ver si esta picha sirve'

Lista_variable9 = variable9.split(' ')

for elemento in enumerate(Lista_variable9):
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'{PEPE.Tupla_Poke[2]} aparece en la posicion {PEPE.Tupla_Poke.index("Misty")}')

for elemento in Diccionario2:
    print (f'{Diccionario2[elemento]}')

for elemento in Diccionario3.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Contador = 0

while (Contador <= len(PEPE.Lista_Numeros)):
    print (f'El contador es {Contador}')
    Contador+= 1

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1

Lista_Animales = []
Lista_Animales.append(PEPE.Lista2[2])
Lista_Animales.insert(0, 'Ballena')
Lista_Animales.extend(['Leon', 'Rana'])

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Ballena'):
        print (f'El mayor mamifero viviente')
        break
    else:
        Contador+= 1
        continue

for elemento1, elemento2 in zip(Set_Conjunto1, Tupla2):
    print (f'{elemento2} -- {elemento1}')

for elemento in range(5):
    print (f'{elemento}')

for elemento in range(995, 1000):
    print (f'{elemento}')

Lista_Numeros_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Num_Menor = min(Lista_Numeros_Mult)
Num_Mayor = max(Lista_Numeros_Mult)

print (f'El menor es {Num_Menor} y el mayor es {Num_Mayor}')

print (f'El redondeado de 14.458795 es {round(14.458795, 2)}')

print (f'El resultado de la sumatoria es {sum(Lista_Numeros_Mult)}')

print (f'{bool(0)}')
print (f'{bool(None)}')
print (f'{bool("")}')
print (f'{bool(False)}')

Todo_All = all([Set_Conjunto1, Tupla1, Diccionario3, 0])

print (f'{Todo_All}')

Uno = str(500)
Dos = int("500")
Tres = float(Dos)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')

print (f' - '.join(Lista_Uno_Copia))

def Ejemplo1(Numero:int) -> int:
    return Numero * Variable_Sumatoria + Objeto3.Cantidad

print (f'El resultado de la operacion es {Ejemplo1(PEPE.Flotante1)}')

def Ejemplo2(Operacion):
    Resultado2 = eval(Operacion)
    return Resultado2

print (f'El resultado de la operacion es {Ejemplo2(PEPE.Flotante2)}')

def Ejemplo3(Cadenita):
    Lista_Cadenita = Cadenita.split(' ')
    for elemento in enumerate(Lista_Cadenita):
        print (f'{elemento[0]} -- {elemento[1]}')

    print (f'La cantidad de palabras digitadas son {Lista_Cadenita.__len__()}')

Ejemplo3(PEPE.Flotante3)

Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del estudiante {elemento}: ')
        Lista.append(Alumno)

    return Lista

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nLa lista de estudiantes que asistieron hoy es {Colegio(Lista_Alumnos)}'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

Lista_Alumnos2 = list([])

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio2(Lista):
    for elemento in range(Contador):
        Alumno_Name = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Age = int(input(f'Ingrese la edad del alumno {elemento}: '))
        Estudiante = [Alumno_Name, Alumno_Age]
        Lista.append(Estudiante)

    Lista.sort(key = lambda Num : Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]

    print (f'El menor de los alumnos es {Menore} y el mayor es {Mayore}')

Colegio2(Lista_Alumnos2)

def Ejemplo_Final():
    while True:
        Numerito = input(f'Ingrese un numero: ')
        try:
            Numero = int(Numerito)
            break
        except:
            print (f'Error, necesito que ingreses un numero')

    return Numero

print (f'Gracias, el numero ingresado es {Ejemplo_Final()}')

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3