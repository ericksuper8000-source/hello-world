import Module_Own as PEPE

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
    'Nombre' : ["Carmelo", "Roxana", "Roberto"],
    'Edad' : [66, 17, 46],
    'Votante' : [True, False, True]
})

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

Data_Frame1_Age = Data_Frame1['Edad']

print (f'{Data_Frame1}')

print (f'------------------')

print (f'El menor de las edades es {Data_Frame1_Age.min()} y el mayor de las edades es {Data_Frame1_Age.max()}')

print (f'------------------')

print (f'{Data_Frame_Concatenate.info()}')

print (f'------------------')

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'------------------')

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'------------------')

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'------------------')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'La cantidad de filas es {Filas} y la cantidad de columnas es {Columnas}')

Elemento1 = Data_Frame1.loc[0, "Nombre"]
Elemento2 = Data_Frame2.iloc[1, 2]
Elemento3 = Data_Frame2.loc[1, "Edad"]

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')

import pandas as pd

import openpyxl

Ruta_Excel1 = 'C:\\Repo\\Book.xlsx'

Cargar_Excel1 = pd.read_excel(Ruta_Excel1, engine = 'openpyxl')

print (f'{Cargar_Excel1.head()}')

Elemento4 = Cargar_Excel1.loc[0, "nombre"]
Elemento5 = Cargar_Excel1.loc[1, "cabina"]
Elemento6 = Cargar_Excel1.loc[2, "clase"]
Elemento7 = Cargar_Excel1.iloc[0, 3]
Elemento8 = Cargar_Excel1.iloc[1, 9]
Elemento9 = Cargar_Excel1.iloc[2, 2]

print (f'{Elemento4}')
print (f'{Elemento5}')
print (f'{Elemento6}')

print (f'{Elemento7}')
print (f'{Elemento8}')
print (f'{Elemento9}')

Elemento10 = Cargar_Excel1.loc[:, "cabina"]
Elemento11 = Cargar_Excel1.iloc[1, :]

print (f'{Elemento10}')

print (f'------------------')

print (f'{Elemento11}')

print (f'------------------')

import pandas as pd

import openpyxl

Ruta_Excel2 = 'C:\\Repo\\Book.xlsx'

Cargar_Excel2 = pd.read_excel(Ruta_Excel2, engine = 'openpyxl')

print (f'{Cargar_Excel2.head()}')

print (f'------------------')

Cargar_Excel3 = pd.read_excel(Ruta_Excel2, engine = 'openpyxl', sheet_name=1)
Cargar_Excel4 = pd.read_excel(Ruta_Excel2, engine = 'openpyxl', sheet_name=0, header=0)
Cargar_Excel5 = pd.read_excel(Ruta_Excel2, engine = 'openpyxl', sheet_name=0, header=0, names=["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"])
Cargar_Excel6 = pd.read_excel(Ruta_Excel2, engine = 'openpyxl', sheet_name=0, header=0, index_col="tarifa")
Cargar_Excel7 = pd.read_excel(Ruta_Excel2, engine = 'openpyxl', sheet_name=0, header=0, usecols="E:I", index_col="tarifa")
Cargar_Excel8 = pd.read_excel(Ruta_Excel2, engine = 'openpyxl', sheet_name=0, header=0, usecols="E:I", index_col="tarifa", nrows=1)

print (f'{Cargar_Excel3.head()}')

print (f'------------------')

print (f'{Cargar_Excel4.head()}')

print (f'------------------')

print (f'{Cargar_Excel5.head()}')

print (f'------------------')

print (f'{Cargar_Excel6.head()}')

print (f'------------------')

print (f'{Cargar_Excel7.head()}')

print (f'------------------')

print (f'{Cargar_Excel8.head()}')

Elemento12 = Cargar_Excel8["sexo"]

print (f'{Elemento12}')

Cargar_Excel5_Sorted = Cargar_Excel5.sort_values(by = "Five", ascending=True)

print (f'{Cargar_Excel5_Sorted}')

print (f'------------------')

Cargar_Excel5_Sorted_Descending = Cargar_Excel5.sort_values(by = "Five", ascending=False)

print (f'{Cargar_Excel5_Sorted_Descending}')

print (f'------------------')

print (f'{Data_Frame2["Nombre"]}')

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'------------------')

print (f'{Cargar_Txt.head()}')

print (f'------------------')

import pandas as pd

Ruta_Csv = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv = pd.read_csv(Ruta_Csv)

print (f'{Cargar_Csv.head()}')

print (f'------------------')

import pandas as pd

import requests

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Cargar_Html = pd.read_html(Response.text)

print (f'{Cargar_Html[2].head()}')

print (f'------------------')

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

print (f'------------------')

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[0, 0]}')
print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[0, 1:2]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[1, 0:None])
Sumita4 = np.sum(Array2_Sorted[1, :])

print (f'Acomodados: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

print (f'El resultado de la sumita es {Sumita1}')
print (f'El resultado de la sumita es {Sumita2}')
print (f'El resultado de la sumita es {Sumita3}')
print (f'El resultado de la sumita es {Sumita4}')

print (f'------------------')

Array3 = np.array([[['e', 'i', 'k'], ['s', 'a', 'l']],     [['v', 'm', 'x'], ['f', 'd', 'i']]])

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
print (f'{Array3[1, 1, 1:2]}')
print (f'{Array3[1, :, 0]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "a"]}')

print (f'------------------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [9, 8, 7]]],       [[[6, 5, 4], [3, 2, 1]], [[5, 2, 9], [8, 6, 1]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[0, 1, 0, 2]}')
print (f'{Array4[1, 0, 0, :2]}')
print (f'{Array4[1, 0, 0, 2:]}')
print (f'{Array4[0, 1, 1, ::2]}')
print (f'{Array4[1, 0, 1, ::3]}')
print (f'{Array4[1, 1, 1, 1:2]}')
print (f'{Array4[1, 0, :, 2]}')
print (f'{Array4[0, 0, 1, 0:None]}')
print (f'{Array4[0, 0, 1, :]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[1, 0, 1, 0:None])
Sumita8 = np.sum(Array4_Sorted[1, 0, 1, :])

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'------------------')

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El numero menor de la lista es {Array_Num1_Min} y el mayor es {Array_Num1_Max}')

print (f'------------------')

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

print (f'------------------')

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 2]}')

print (f'------------------')

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 1]}')

print (f'------------------')

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke3"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 1]}')

print (f'------------------')

Array_Gen2 = np.full(shape=(5), fill_value = "Fuecoco")

Lista_Array1 = list([])

for elemento in enumerate(Array_Gen2):
    Lista_Array1.append(str(elemento[1]))

print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'------------------')

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[0, 1, 1, 0])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 0]}')

print (f'------------------')

Tupla_Array1 = tuple(("Rojo", "Negro"))
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value = Tupla_Array1)
Array_Gen5 = np.full(shape=(2, 1), fill_value = Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value = Diccionario_Array["Nombre"][0])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'------------------')

print (f'{Array_Gen6[3]}')

print (f'------------------')

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

print (f'------------------')

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')

print (f'------------------')

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')
print (f'{Array_Random2.ndim}')
print (f'{Array_Random2.shape}')
print (f'{Array_Random2.size}')
print (f'{Array_Random2.dtype}')
print (f'{Array_Random2[1, 2]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodados: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

print (f'------------------')

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Sum = Arr1 + Arr2
Rest = Arr1 - Arr2
Mult = Arr1 * Arr2
Div = Arr1 / Arr2
Array_Random1_Cien = Array_Random1 + 100

print (f'{Sum}')
print (f'{Rest}')
print (f'{Mult}')
print (f'{Div}')
print (f'{Array_Random1_Cien}')

print (f'------------------')

Array_Num8 = np.arange(20)

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

print (f'------------------')

Lista_Array2 = ["Erick", "Josue", "Perez", "Gutierrez"]

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'------------------')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'------------------')

Array6 = np.array([1, 2, 3])
Array7 = np.array([4, 5, 6])

Array_Concatenate = np.concat([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'------------------')

Array_Concatenate_Split = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Split[0]}')
print (f'{Array_Concatenate_Split[1]}')
print (f'{Array_Concatenate_Split[2]}')

print (f'------------------')

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'------------------')

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'------------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'------------------')

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

print (f'------------------')

Tupla_Array2 = ('Erick', 'Josue', 'Karlita', 'Roberto', 'Alana', 'Susanita')

Ganador1 = np.random.choice(Tupla_Array2, size=(1), replace=False)
Ganador2 = np.random.choice(Tupla_Array2, size=(2), replace=False)
Ganador3 = np.random.choice(Tupla_Array2, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'------------------')

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'------------------')

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2):
        return Num1 + Num2

    return Sumatoria_Interna(3)

Variable_Sumatoria = Sumatoria_Externa(4)

print (f'El resultado de la sumatoria es {Variable_Sumatoria}')

if (PEPE.Par(Variable_Sumatoria) == True):
    print (f'El numero es par')
else:
    print (f'El numero es impar')

PEPE.Usuario(Saludar_Dos(), "MASCULINO")

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
    Documento_Agregar = Docu.writelines([f'\nSu contrasena temporal es {PEPE.Contrasena(123)}'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 36, 3.5, False)

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

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')
print (f'Los numeros pares de la lista son {list(Anonima3)}')

def Primera(Segunda):
    def Tercera(*args):
        return Segunda(*args) - 42

    return Tercera

@Primera
def Operacion(Numero):
    Local = Numero
    return PEPE.Var_Global + Local

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
print (f'{Variable_Closure(27)}')
print (f'{Variable_Closure(34)}')

def Crear_Multiplicador(x):
    def Multiplicador(y):
        return x * y

    return Multiplicador

Variable_Multiplicador1 = Crear_Multiplicador(2)
Variable_Multiplicador2 = Crear_Multiplicador(3)

print (f'El multiplicador es {Variable_Multiplicador1(10)}')
print (f'El multiplicador es {Variable_Multiplicador2(10)}')

def Filtrador(Lista):
    any_impares = any(num % 2 != 0 for num in Lista)
    if (any_impares == True):
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impares = [num for num in Lista if num % 2 != 0]

        print (f'Los numeros impares son {Lista_Impares} o podrian ser {list(Anonima4)}')

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

print (f'El resultado de la sumatoria es {Sumatoria3(2, 6)}')

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonathan'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)

    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    print (f'Mi nombre es {Nombre} {Apellido}')

Usuario2("Erick", "Perez")

from Module_Own import Pokemon as Poke

Objeto1 = Poke(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto2 = Poke(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')
Objeto3 = Poke(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'HidroChorro')

Objeto2.Mostrar()

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = "Perez"
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

print (f'{PEPE.Tupla_Poke[2]} tiene {Variable_Sumatoria} o  {Sumatoria2(1, 2, 3, 4, 5)} o incluso {Objeto3.Cantidad} pokemones')

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

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Un rango de elementos es {PEPE.Lista2[2:4]}')

print (f'yo {Lista_Uno[1]} vi un {PEPE.Lista2[2]} cuando fui al zoologico')

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

Tupla1 = ('Uno', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos')

print (f'{Tupla1}')

Tupla1 = tuple(('Uno', 'Dos', 'Tres'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Variable_Funcion_Tupla)}')

Set_Conjunto1 = {'Electrico', Objeto1.Tipo, Objeto1.Tipo, Objeto1.Tipo, Objeto1.Tipo, Objeto1.Tipo}
Set_Conjunto1.add('Roca')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Electrico', 'Roca', Objeto3.Tipo})

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
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, Objeto2.Ataque})

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
    'Edad' : [36, 20, 6],
    'Votante' : [True, True, False]
}

Diccionario3 = dict({'Ingresos' : 500, 'Gastos' : 200, 'Vacio' : ""})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1["Nombre"]}')
print (f'{Diccionario1.get("Edad")}')

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2["Nombre"][1]}')
print (f'{Diccionario2.get("Edad")[2]}')

# Cambie un elemento del diccionario
# Elimine un elemento del diccionario con el metodo pop()
# Muestre el diccionario con los nuevos elementos
# Reconstruya el diccionario con nuevos valores, ojo las llaves ahora seran numeros - Cree un Diccionario con la funcion dict
# Haga un diccionario2 pero con varios elementos por indice, varios nombres, varias edades, etc
# Imprima en consola una concatenacion de dos elementos del diccionario
# Muestre cada una de las llaves de un diccionario con el metodo keys
# Haga una operacion matematica con un elemento de una lista o tupla y uno del diccionario
# Concatene un elemento de una lista con una tupla
# Concatene un elemento de una lista con el diccionario
# Creamos un diccionario vacio, solo con los keys pero sin valores por medio de la funcion dict.fromkeys([])
# Ahora creamos un diccionario en el que todos los keys tengan el mismo valor Diccionario_Vacio = dict.fromkeys('ABCD', "Carmelo")

# Declare una variable y asignele una division flotante
# Declare una variable y asignele una potenciacion o exponente **
# Declare una variable y asignele una division baja //
# Declare una variable y asignele un resto o modulo %
# Muestre en consola el tipo de dato de una variable float, un string, una lista, una tupla, un conjunto y un diccionario
# Despliegue el resultado de la division flotante y de la division baja

# ***********************  Condicionales   **********************

# Crea una llave condicional con if simple - Contar la cantidad de caracteres de una cadena de texto con len, haga un if condition
# Crea una llave condicional con if y else simple
# Ahora crea un condicional con if, elif y else
# Ahora crea un condicional con multiples elif
# Ahora un ejercicio con varios if anidados - declaras dos variables, ingresos y gastos, si los ingresos son mayores a x y los gastos menores a x, entonces estas bien, etc

# ***********************  Metodos / Funciones mas utilizadas   **********************

# Declare una variable string, con un print y dir muestre todos los métodos y atributos disponibles para una variable u objeto
# use help para ver que hace un metodo

#**********

# Declare una clase Persona, cree un objeto y defina un metodo
# Metodos magicos vs metodos normales
# dunder methods porque empiezan y terminan con __)
# x = 'Ejemplo'
# len(x) o tambien
# x.__len__()
# Metodos normales x.upper()

#**********

# abs(x) → Escribe un programa que reciba un número negativo y devuelva su valor absoluto.
# any(iterable) → Comprueba si al menos un número de una lista es par.
# bin(x) → Convierte un número entero dado por el usuario a binario.
# bool(x) → Determina si una cadena ingresada por el usuario está vacía o no.
# divmod(a, b) → Pide dos números y muestra el cociente y el residuo de su división.
# Haz un ciclo for enumerate con un unico elemento, ese unico elemento mostrara el indice con elemento[0] y el valor con elemento[1]
# enumerate(iterable) → Crea una lista de frutas y muestra cada una con su posición en la lista.
# Haga el texto de una variable todo minuscula con el metodo lower
# Haga el texto de una variable todo mayuscula con el metodo upper
# Haga la primera letra de una variable mayuscula con el metodo capitalize
# Busque una letra en especifico en una cadena de texto con el metodo find e index
# Cuantas veces esta la letra a en una cadena con el metodo count
# Verifiquemos si una cadena comienza con x letra con el metodo startswith
# Verifiquemos si una cadena termina con x letra con el metodo endswith
# Reemplace una parte de una cadena con el metodo replace(Este tiene dos parametros, lo que se quiere cambiar y lo nuevo)
# Tome una variable de texto y separe cada elemento de la variable en una lista separada por ',' utilizando el metodo split()

# Busque un elemento en una lista o tupla con index, ojo find no es un metodo para listas
# Declare una variable y asignele una copia de una lista con el metodo copy()
# Borrar todos los elementos de un diccionario con clear()
# Eliminar un elemento del diccinario con pop()
# Recorra todos los elementos de un diccionario con un ciclo for normal
# Recorramos tdos los elementos de un diccionario con la funcio .items()

#### VARIABLES 2.0

# Vamos a usar la tecnica de desempaquetado de variables creando una tupla de 3 elementos y agregando cada elemento de la tupla a 3 variables, ojo, no usar indices

### CICLOS WHILE

# Creamos una lista con los numeros 1, 2, 3, 4, 5, hagamos un ciclo for que multiple cada uno de estos numeros y los muestre en consola
# Creamos ahora una lista con 3 animales, los recorremos con un ciclo for, inmediatamente se evalua con un if si la variable es igual al segundo animal, lo muestra y se detiene el ciclo. Ojo, usar el break y el continue
# Hagamos un for anidado con la funcion zip(), creamos dos listas del mismo tamaño
# Hagamos un ciclo for con la funcion range de 0 a 5 con un unico parametro
# Hagamos un ciclo for con la funcion range de 1 a 10 con dos parametros
# Creamos una lista con 4 numeros, ahora creamos otra listsa Lista_Multiplicado y agregamos cada numero de la primera lista a la segunda x 10

#### Ciclo WHILE
# Creamo un ciclo while simple con un contador que se ejecutara mientras contador sea menor a 10


#### Funciones creadas directamente por python (Funciones Build-In)

# Encontrar el numero mayor de una lista con la funcion max()
# Encontrar el numero menor de una lista con la funcion min()
# Redondear el numero 14.458795 a dos decimales con la funcion round() con dos parametros
# Retornemos False con la funcion bool() usando False, 0, "", None
# Retornemos un False agregando varios elementos a una variable con la funcion all() pero al menos uno debe ser False, 0, "", None
# Cree una variable y sumele todos los elementos de una Tupla, Lista, Set con la funcion sum()

# Imprime en pantalla    print()    
# Solicita datos al usuario     input()
# Devuelve la longitud de una secuencia    len()
# Devuelve el tipo de un objeto    type()
# Convierte un número a texto y viceversa  str(), int(), float()
# Despliegue los numeros de 90 a 100 con range()
# Imprime los elementos de una lista con su posición.     enumerate()
# Combina dos listas y muéstralas juntas    zip()
# Ordena una lista de números con sort, sort(reverse = True) reverse()

# Verifique si un elemento de una tupla es par con any()
# Cree una list(), tuple(), set(), dict()
# Cree una lista de 4 palabras por ejemplo mi nombre completo y unalas con la funcion print ("-".join(Lista))

# Divide un texto por espacios con split()

# ***********************  Data Inputs   **********************

# Input lo que nos devuelve siempre es texto, aunque se ingresen numeros
# Declare una variable y asignele un input, pida que ingrese un numero
# Esa variable debe convertirse en integer con la funcion int
# Haga una operacion matematica con esta variable y muestrela

# eval(expression) → Permite al usuario ingresar una operación matemática como texto y muestra el resultado.

# Vamos a crear un programa en el que por medio de un input le pidamos a un usuario ingresar una cadena de texto
# Esta cadena de texto sera guardada en una variable matriz con la funcion split separando cada palabra por un espacio
# Ahora vamos a usar la funcion dunder len para contar cuantas palabras ingreso el usuario

# Creamos una lista vacia, Ahora creamos un programa que pida la cantidad de alumnos
# Luego con un for range, se recorre el ciclo y se pide el nombre de la cantidad de alumnos
# Por medio de un append agregamos cada nombre a la lista vacia
# Mostramos los elementos del filtro, cada nombre digitado

# Ahora vamos a hacer un programa que pida nombres y edades, vamos a evaluar cual es el mayor y cual es el menor
# Y vamos a desplegar que el mayor es el profesor y el menor es el alumno menor

# Usemos elementos de un modulo por medio de un import
# Renombremos un modulo con la instrucion "as" Saludar as OtroNombre



##############################     ENRUTAMIENTO DE MODULOS     ######################################

''' Hay un modulo llamado Modulo_Propio2 dentro de una carpeta alternativa, importemos esta carpeta alternativa
por medio del nombre de la carpeta Nueva.Modulo_Propio2, y despleguemos algun elemento de Modulo Propio2,
Como el nombre del import se vuelve grandisimo, usemos "as" para renombrarlo y que sea mas facil manejarlo'''


##############################     PAQUETES (Es una carpeta con muchos archivos python)     ######################################

''''''Un paquete es una carpeta con muchos archivos, lo mas importante es que esta carpeta para ser
Considerara un paquete debe tener un archivo llamado __init__.py, esto lo convierte en paquete
Si dentro de esta carpeta paquete agregamos una sub carpeta con __init__.py, esto se vuelve un sub paquete.'''




Alumnos = []

Cantidad = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Cantidad):
        Alumno = input(f'Ingrese el nombre del alumno {elemento}: ')
        Edad = int(input(f'Ingrese la edad del alumno {elemento}: '))
        Estudiante = [Alumno, Edad]
        Lista.append(Estudiante)
        Lista.sort(key = lambda Num : Num[1])

    Estudiante = Lista[0][0]
    Profesor = Lista[-1][0]

    print (f'El profesor es {Profesor} y el estudiante menor es {Estudiante}')


Colegio(Alumnos)


---------------------------




[Excepciones]
Una excepcion es un bloque de codigo que se mostrara en caso de que el codigo se rompa. Por ejemplo digamos que tenemos un codigo que pide un numero pero ingresamos una cadena de texto. Entonces el codigo se detendra y mostrara un mensaje de error hasta que agreguemos el numero.

def Ejemplo():
    while True:
        Numero1 = input(f'Ingrese un numero: ')
        try:
            Numerito = int(Numero1)
            break
        except:
            print (f'Error, eso no es un numero')

    return Numerito

print (f'{Ejemplo()}')

xxx
