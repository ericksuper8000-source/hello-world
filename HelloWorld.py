import Module_Own as PEPE

with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
    Documento_SobreEscribir = Docu.write(f'Melocoton')
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
    'Edad' : [66, 14, 26],
    'Votante' : [True, False, True]
})

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

Data_Frame1_Age = Data_Frame1["Edad"]

print (f'{Data_Frame1}')

print (f'------------------')

Data_Frame_Concatenate_Age = Data_Frame_Concatenate["Edad"]

print (f'La edad menor de la lista es {Data_Frame1_Age.min()} y la mayor es {Data_Frame1_Age.max()}')
print (f'La edad menor de la lista es {Data_Frame_Concatenate_Age.min()} y la mayor es {Data_Frame_Concatenate_Age.max()}')

print (f'{Data_Frame1.info()}')

print (f'------------------')

print (f'{Data_Frame_Concatenate}')

print (f'------------------')

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'------------------')

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'------------------')

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'------------------')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'La cantidad de Filas es {Filas} y el de columnas es {Columnas}')

Elemento1 = Data_Frame1.loc[2, "Nombre"]

print (f'El elemento 1 es {Elemento1}')

Elemento2 = Data_Frame2.iloc[0, 2]

print (f'El elemento 2 es {Elemento2}')

Elemento3 = Data_Frame1.loc[0, "Nombre"]

print (f'El nombre de la fila cero es {Elemento3}')

Elemento4 = Data_Frame1.loc[:, "Edad"]

print (f'{Elemento4}')

Elemento5 = Data_Frame2.iloc[1, 2]

print (f'El resultado del iloc es {Elemento5}')

Elemento6 = Data_Frame2.iloc[:, 1]

print (f'El resultado del iloc es {Elemento6}')

print (f'------------------')

Elemento7 = Data_Frame1.iloc[0, :]

print (f'{Elemento7}')

print (f'------------------')

import pandas as pd

import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine = 'openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'------------------')

Cargar_Excel = pd.read_excel(Ruta_Excel, engine = 'openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'------------------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, names=["Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez"])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, index_col="cabina")
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, usecols="E:I", index_col="tarifa")
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, usecols="E:I", nrows=1, index_col="tarifa")

print (f'{Cargar_Excel1.head()}')

print (f'------------------')

print (f'{Cargar_Excel2.head()}')

print (f'------------------')

print (f'{Cargar_Excel3.head()}')

print (f'------------------')

print (f'{Cargar_Excel4.head()}')

print (f'------------------')

print (f'{Cargar_Excel5.head()}')

print (f'------------------')

print (f'{Cargar_Excel6.head()}')

Elemento8 = Cargar_Excel3.loc[:, "Cinco"]

print (f'Elemento {Elemento8}')

print (f'------------------')

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by="Cinco", ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'------------------')

Cargar_Excel3_Sorted_Ascending = Cargar_Excel3.sort_values(by="Cinco", ascending=False)

print (f'{Cargar_Excel3_Sorted_Ascending}')

print (f'------------------')

Elemento9 = Cargar_Excel3["Seis"]

print (f'{Elemento9}')

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

print (f'{Cargar_Csv}')

Elemento10 = Cargar_Csv.iloc[2, 1]

print (f'Tu nombre es {Elemento10}')

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

Array2 = np.array([[4, 3, 5], [7, 8, 0]])

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
print (f'{Array2[0, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2, axis=0)
Sumita2 = np.sum(Array2, axis=1)
Sumita3 = np.sum(Array2[0, 0:None])
Sumita4 = np.sum(Array2[0, :])

print (f'El resultado de la sumita es {Sumita1}')
print (f'El resultado de la sumita es {Sumita2}')
print (f'El resultado de la sumita es {Sumita3}')
print (f'El resultado de la sumita es {Sumita4}')

print (f'------------------')

Array3 = np.array([[['e', 'u', 'm'], ['f', 'd', 'x']],           [['i', 'n', 'l'], ['j', 's', 'a']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 1]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[1, 1, ::2]}')
print (f'{Array3[0, 1, ::3]}')
print (f'{Array3[1, 0, 1:2]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[1, 1, 0:None]}')
print (f'{Array3[1, 1, :]}')
print (f'{Array3[Array3 == "i"]}')

print (f'------------------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],       [[[6, 5, 4], [9, 8, 7]], [[0, 3, 7], [6, 1, 8]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 0]}')
print (f'{Array4[0, 1, 0, :2]}')
print (f'{Array4[0, 1, 0, 2:]}')
print (f'{Array4[1, 0, 1, ::2]}')
print (f'{Array4[0, 1, 0, ::3]}')
print (f'{Array4[1, 1, 0, 1:2]}')
print (f'{Array4[0, 1, 0, 0:None]}')
print (f'{Array4[1, 1, 1, :]}')
print (f'{Array4[0, 0, :, 2]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado es {Array4_Sorted}')
print (f'Media es {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria es {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[1, 1, 1, 0:None])
Sumita8 = np.sum(Array4_Sorted[1, 1, 1, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'------------------')

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')
print (f'{Array_Num1.ndim}')
print (f'{Array_Num1.shape}')
print (f'{Array_Num1.size}')
print (f'{Array_Num1.dtype}')
print (f'{Array_Num1[4]}')

Menor = np.min(Array_Num1)
Mayor = np.max(Array_Num1)

print (f'El numero menor de la lista es {Menor} y el mayor es {Mayor}')

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
print (f'{Array_Ones[0, 0]}')

print (f'------------------')

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 0]}')

print (f'------------------')

Array_Gen2 = np.full(shape=(5), fill_value = "Fuecoco")

Lista_Array1 = list([])

for indice, elemento in enumerate(Array_Gen2, start=0):
    Lista_Array1.append(str(elemento))

print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'------------------')

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[1, 0, 1, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 1]}')

print (f'------------------')

Tupla_Array = ('Rojo', 'Verde')
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array['Nombre'][1])

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
print (f'{Array_Random2[0, 2]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Ordenado: {Array_Random2_Sorted}')
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

print (f'El resultado de la sumatoria es {Sum}')
print (f'El resultado de la sumatoria es {Rest}')
print (f'El resultado de la sumatoria es {Mult}')
print (f'El resultado de la sumatoria es {Div}')
print (f'El resultado de la sumatoria es {Array_Random1_Cien}')

print (f'------------------')

Array_Random3 = np.random.randint(low=1, high=10, size=(20))

print (f'{Array_Random3}')

Array_Random3_Reshape = np.reshape(Array_Random3, shape=(4, 5))

print (f'{Array_Random3_Reshape}')

Array_Random3_Reshape_Ravel = np.ravel(Array_Random3_Reshape)

print (f'{Array_Random3_Reshape_Ravel}')

print (f'------------------')

Lista_Array2 = [1, 2, 3, 4, 5, 6]

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'------------------')

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

print (f'------------------')

for Matriz in Array3:
    for Fila in Matriz:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'------------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'------------------')

Array_Random4 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random4}')

Sumita9 = np.sum(Array_Random4, axis=0)
Sumita10 = np.sum(Array_Random4, axis=1)
Sumita11 = np.sum(Array_Random4[1, 0, 0:None])
Sumita12 = np.sum(Array_Random4[1, 0, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

print (f'------------------')

Tupla_Array2 = tuple(("Erick", "Josue", "Karlita", "Susanita", "Roberto", "Carmelo", "Roxana"))

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
        if (Genero == "masculino"):
            return True
        else:
            return False

    return Usuario_Interno("MASCULINO")

Variable_Usuario = Usuario_Externo()

if (Variable_Usuario == True):
    print (f'YOU ARE A MAN')
else:
    print (f'YOU ARE A WOMAN')

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(45)}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 36, 3.5, True)

print (f'{Funcion_Tupla("Perro", 36, 3.5, True)}')
print (f'{Funcion_Tupla("Perro", 36, 3.5, True)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 36, 3.5, True))}')

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
print (f'Los numeros pares de la lista son {list(Anonima3)} o incluso podria ser {PEPE.Lista_Pares}')

def Primera(Segunda):
    def Tercera(*args):
        return Segunda(*args) - 42

    return Tercera

@Primera
def Operacion(Numero):
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
print (f'{Variable_Closure(25)}')
print (f'{Variable_Closure(37)}')

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
        return Segunda(*args, **kwargs) - 20

    return Tercera

@Primera
def Sumatoria3(Num1, Num2):
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(12, 8)}')

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = "Jonathan"
        Apellido = "Smith"
        return Segunda(Nombre, Apellido)

    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    print (f'Mi nombre es {Nombre} {Apellido}')

Usuario2("Erick", "Perez")

from Module_Own import Pokemon as Poke

Objeto1 = Poke(PEPE.Diccionario_Poke["Poke1"], 'Electrico', 'Impact Trueno')
Objeto2 = Poke(PEPE.Diccionario_Poke["Poke2"], 'Roca', 'Sismo')
Objeto3 = Poke(PEPE.Diccionario_Poke["Poke3"], 'Agua', 'Hidro Chorro')

Objeto1.Mostrar()

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
variable6, variable7 = True, Objeto2.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Concatenacion simple {PEPE.Diccionario_Poke["Poke3"]}')
print (f'Mi nombre es {Lista_Uno[0]} {variable2}')
print (f'{PEPE.Tupla_Poke[2]} tiene {Variable_Sumatoria}, {Sumatoria2(1, 2, 3, 4, 5)} o incluso {Objeto2.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

Snake_Case1, Snake_Case2, Snake_Case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables {Snake_Case2}')

print (f'La cantidad de elementos en la lista 1 son {Lista_Uno.__len__()}')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto1.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Un rango de elementos de la lista 2 son {PEPE.Lista2[2:4]}')

print (f'{Lista_Uno[0]} le gustan los {PEPE.Lista2[2]}s')

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

print (f'{Tupla2}')

Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')

Set_Conjunto1 = {"Rojo", "Rojo", "Rojo", "Rojo", "Rojo"}
Set_Conjunto1.add('Negro')

print (f'{Set_Conjunto1}')
print (f'{Set_Conjunto1.__len__()}')

Set_Conjunto1 = set({"Red", "Blue", "Green"})

print (f'{Set_Conjunto1}')

Set_Conjunto2 = {1, 2, 3, 4, 5}
Set_Conjunto3 = {4, 5}
Set_Conjunto4 = set({8})

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')

Set_Conjunto_Menu1 = {"Chocolate", "Vainilla"}
Set_Conjunto_Menu1.add("Fresa")
Set_Conjunto_Menu2 = frozenset({"Caramelo"})
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, Objeto1.Nombre})

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

Diccionario3 = {
    'Ingresos' : 501,
    'Gastos' : 199,
    'Vacio' : "q"
}

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1["Nombre"]}')
print (f'{Diccionario1.get("Edad")}')

Diccionario1["Nombre"] = variable1

print (f'{Diccionario1}')

del Diccionario1["Nombre"]
Diccionario1.pop("Edad")

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')

Diccionario1 = dict({1 : Diccionario2["Nombre"][2], 2 : Sumatoria2(1, 2, 3), 3 : variable6})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'{Diccionario1.get(1)} no puede votar, ya que solo tiene {Diccionario2["Edad"][2]} añitos')

Diccionario_Vacio1 = dict.fromkeys("ABCD", Objeto2.Nombre)
Diccionario_Vacio2 = dict.fromkeys(["Uno", "Dos", "Tres"])
Diccionario_Vacio2["Dos"] = Saludar_Dos()

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
print (f'{type(variable4)}')
print (f'{type(PEPE.Division_Flotante)}')
print (f'{type(Objeto1.Catched)}')
print (f'{type(Lista_Uno_Copia)}')
print (f'{type(PEPE.Tupla_Poke)}')
print (f'{type(Set_Conjunto_Menu1)}')
print (f'{type(Set_Conjunto_Menu2)}')
print (f'{type(Diccionario_Vacio2)}')
print (f'{type(Funcion_Tupla)}')
print (f'{type(Objeto1)}')
print (f'{type(Poke)}')
print (f'{type(Array_Concatenate)}')
print (f'{type(Data_Frame_Concatenate)}')
print (f'{type(PEPE)}')

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
        self.Classified = True

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')

Objeto4 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto1.Nombre)
Objeto5 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto2.Nombre)
Objeto6 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto3.Nombre)

Objeto5.Desplegar()

Negativo = -5

print (f'{int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]
Anonima5 = filter(lambda num : num % 2 == 0, PEPE.Lista_Numeros)

print (f'{Any_Iterable}')
print (f'{Lista_Iterable}')
print (f'{list(Anonima5)}')

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3["Vacio"]) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, ingrese una cadena de texto')

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')

for elemento in Set_Conjunto1:
    print (f'{elemento}')

for indice, elemento in enumerate(Set_Conjunto_Menu1, start=1):
    print (f'El elemento en la posicion {indice} es {elemento}')

variable8 = 'eSteBAN'
letra = variable8[0]

print (f'{variable8}')
print (f'{variable8.lower()}')
print (f'{variable8.upper()}')
print (f'{variable8.capitalize()}')

print (f'{variable8.lower().find("t")}')
print (f'{variable8.lower().index("b")}')

print (f'La letra {letra} aparece un total de {variable8.lower().count(letra)} veces')

print (f'{variable8.lower().startswith(letra)}')
print (f'{variable8.lower().endswith("n")}')

print (f'{variable8.lower().replace("ban", "POPOTAMO")}')

variable9 = "este es un nuevo ejemplo de texto para recorrer ciclos"

Lista_variable9 = variable9.split(' ')

print (f'La cantidad de palabras digitadas son {Lista_variable9.__len__()}')

for elemento in enumerate(Lista_variable9):
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'{PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

for elemento in Diccionario1:
    print (f'{Diccionario1[elemento]}')

for elemento in Diccionario2.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1

Contador = 0

Lista_Animales = list([])
Lista_Animales.extend(['Jaguar', 'Condor'])
Lista_Animales.append('Cocodrilo')
Lista_Animales.insert(1, 'Tiburon')

print (f'{Lista_Animales}')

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Condor'):
        print (f'El ave mas grande del planeta')
        break
    else:
        Contador+= 1
        continue

for elemento1, elemento2 in zip(Lista_Uno_Copia, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')

for elemento in range(5):
    print (f'{elemento}')

for elemento in range(995, 1000):
    print (f'{elemento}')

Lista_Numeros_Multiplicados = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Multiplicados}')

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1

Menor = min(Lista_Numeros_Multiplicados)
Mayor = max(Lista_Numeros_Multiplicados)

Redondeado = round(14.458795, 2)

Sumatoria4 = sum(Lista_Numeros_Multiplicados)

print (f'El numero menor de la lista es {Menor} y el mayor es {Mayor}')

print (f'El numero 14.458795 redondeado es {Redondeado}')

print (f'El resultado de la sumatoria es {Sumatoria4}')

print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool("")}')
print (f'{bool(False)}')

Todo_All = all([Lista_Uno_Copia, Tupla1, Diccionario2, None])

print (f'{Todo_All}')

Uno = str(500)
Dos = int("500")
Tres = float(Dos)

print (f'{Uno}')
print (f'{Dos}')
print (f'{Tres}')

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')

print (f' - '.join(PEPE.Set_Conjunto_Poke))

def Word_Counter(Palabras):
    Lista_Palabras = Palabras.split(' ')
    print (f'La cantidad de palabras digitadas es {Lista_Palabras.__len__()}')

    for indice, elemento in enumerate(Lista_Palabras, start=1):
        print (f'La palabra en la posicion {indice} es {elemento}')

Word_Counter(PEPE.Flotante1)

def Operacion2(Numero):
    return int(Numero) * Sumatoria2(1, 2, 3, 4, 5) + Objeto1.Cantidad

print (f'El resultado de la operacion es {Operacion2(PEPE.Flotante2)}')

Resultado3 = eval(PEPE.Flotante3)

print (f'El resultado de la operacion es {Resultado3}')

Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento}: ')
        Lista.append(Alumno)

    return Lista

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nLa lista de estudiantes que asistieron hoy es {Colegio(Lista_Alumnos)}'])
    Docu.close()

with open (Ruta_Txt, encoding='UTF-8') as Docu:
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

    print (f'El alumno mas joven es {Menore} y el mayor es {Mayore}')

Colegio2(Lista_Alumnos2)

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

variable_PEPE3 = PEPE3

def Ejemplo():
    while True:
        Numero = input(f'Ingrese un numero entero: ')
        try:
            Numerito = int(Numero)
            break
        except:
            print (f'Error, necesito un numero entero')

    return Numerito

print (f'Gracias, el numero ingresado es {Ejemplo()}')