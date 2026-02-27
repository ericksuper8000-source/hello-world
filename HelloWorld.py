import re
import turtledemo.penrose

import numpy.ma.core
import pandas.conftest

var1 = 'esTo es hula un texto 2 pero tambien! es hela un 150 ejercicio que yo estaree intenntando? hola completaR'

Buscar1 = re.search('ejercicio', var1)

print (f'{Buscar1}')

Buscar2 = re.fullmatch('esTo es hula un texto 2 pero tambien! es hela un 150 ejercicio que yo estaree intenntando? hola completaR', var1)

print (f'{Buscar2}')

Buscar3 = re.findall('e', var1)

print (f'{Buscar3}')

Buscar4 = re.findall(r'\d+', var1)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\D+',var1)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\w+', var1)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\W+', var1)

print (f'{Buscar7}')

Buscar8 = re.findall(r'\w+', var1)

print (f'{Buscar8}')

Buscar9 = re.search(r'\W', var1)

print (f'{Buscar9}')

Buscar10 = re.findall(r'h.la', var1)

print (f'{Buscar10}')

Buscar11 = re.findall(r'[a-z]+', var1)

print (f'{Buscar11}')

Buscar12 = re.findall(r'[a-zA-Z0-9\W]+', var1)

print (f'{Buscar12}')

Buscar13 = re.search(r'^e', var1)

print (f'{Buscar13}')

Buscar14 = re.search(r'R$', var1)

print (f'{Buscar14}')

var2 = '''
esto
es
un
Texto
multilinea'''

var3 = 'otro ejemplo123 ! vamos a ver si caeaemos bapero no solo saeaenz sabia  esto sirv@'

Buscar15 = re.search(r'[A-Z]+', var2, flags=re.M)

print (f'{Buscar15}')

Buscar16 = re.search(r'[a-z]+', var2, flags=re.IGNORECASE)

print (f'{Buscar16}')

Buscar17 = re.search(r'[0-9]{3}\s{1}\W{1}', var3)

print (f'{Buscar17}')

Buscar18 = re.findall(r'(ae){2,4}', var3)

print (f'{Buscar18}')

Buscar19 = re.findall(r'[ab]+', var3)

print (f'{Buscar19}')

Buscar20 = re.findall(r'\d+|\W+', var3)

print (f'{Buscar20}')

Fecha = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Patron1 = r'\d{2}/\d{2}/[0-9]{4}'

Replacement = 'xxxxxxx'

Buscar21 = re.sub(Patron1, Replacement, Fecha)

print (f'{Buscar21}')

Email1 = 'sample123@sample.com'

Patron2 = r'[a-zA-Z0-9%.]+@([a-z]).?.([a-z]){2,}'

Buscar22 = re.match(Patron2, Email1)

if (Buscar22):
    print (f'Formato correcto')
else:
    print (f'Formato incorrecto')

def Exception1(Elemento):
    try:
        Numerito = int(Elemento)
        print (f'Gracias, el numero es {Numerito}')
    except ValueError:
        print (f'Error, necesito que sea un numero')

Exception1("Hola")

def Exception2(Num1, Num2):
    try:
        Resultado = Num2 + Num1
        print (f'El resultado de la operacionn es {Resultado}')
    except TypeError:
        print (f'Error, necesito que ambos elementos sean numeros')

Exception2(12, "Hola Mundo")

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
        print (f'El elemento en el indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'El indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = {
    'Nombre' : "Erick",
    'Edad' : 37
}

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error la llave esta fuera de rango')

Exception5('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Hiena')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado no existe')

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nSalamandra'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nOso')
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
    'Votante' : [True, not False, False]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [55, 14, 26],
    'Votante' : [True, False, not False]
})

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame1}')

print (f'------------')

print (f'El menor de todos es {Data_Frame_Concatenate_Age.min()} y el mayor es {Data_Frame_Concatenate_Age.max()}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'------------')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombrecito = elemento['Nombre']
    Edaccita = elemento['Edad']

    print (f'Mi nombre es {Nombrecito} y mi edad {Edaccita}')

print(f'------------')

Llaves = [f'Llave_{i}' for i in range(len(Data_Frame_Concatenate))]

print (f'{Llaves}')

Lista_Nombres = list(Data_Frame_Concatenate['Nombre'])

print (f'{Lista_Nombres}')

Diccionario_DataFrame = dict(zip(Llaves, Lista_Nombres))

print (f'{Diccionario_DataFrame}')
print (f'{Diccionario_DataFrame.keys()}')
print (f'{Diccionario_DataFrame["Llave_1"]}')
print (f'{Diccionario_DataFrame.get("Llave_4")}')

print(f'------------')

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print(f'------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print(f'------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()
'''

print (f'{Data_Frame_Concatenate.head(1)}')

print(f'------------')

print (f'{Data_Frame_Concatenate.head(3)}')

print(f'------------')

print (f'{Data_Frame_Concatenate.tail(1)}')

print(f'------------')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'El numero de filas son {Filas} y el numero de Columnas son {Columnas}')

Elemento1 = Data_Frame1.loc[0, 'Nombre']
Elemento2 = Data_Frame1.loc[1, 'Edad']
Elemento3 = Data_Frame1.loc[2, 'Votante']
Elemento4 = Data_Frame1.loc[:, 'Nombre']
Elemento5 = Data_Frame1.loc[2, :]

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')
print (f'{Elemento4}')
print (f'{Elemento5}')

print(f'------------')

Elemento6 = Data_Frame2.iloc[0, 0]
Elemento7 = Data_Frame2.iloc[1, 1]
Elemento8 = Data_Frame2.iloc[2, 2]
Elemento9 = Data_Frame2.iloc[1, :]
Elemento10 = Data_Frame2.iloc[:, 2]

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')
print (f'{Elemento9}')
print (f'{Elemento10}')

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine = 'openpyxl')

print (f'{Cargar_Excel.head()}')

print(f'------------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', names=['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, usecols="E:J")
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, index_col="familiares", usecols="E:J")
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, index_col="familiares", usecols="E:J", nrows=1)

print (f'{Cargar_Excel1.head()}')

print(f'------------')

print (f'{Cargar_Excel2.head()}')

print(f'------------')

print (f'{Cargar_Excel3.head()}')

print(f'------------')

print (f'{Cargar_Excel4.head()}')

print(f'------------')

print (f'{Cargar_Excel5.head()}')

print(f'------------')

print (f'{Cargar_Excel6.head()}')

print(f'------------')

Llaves2 = [f'Num_{i}' for i in range(len(Cargar_Excel3))]
Lista_Excel = list(Cargar_Excel3['Tres'])

print (f'{Llaves2}')
print (f'{Lista_Excel}')

Diccionario_Excel = dict(zip(Llaves2, Lista_Excel))

print (f'{Diccionario_Excel}')

print(f'------------')

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='Cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print(f'------------')

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='Cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

print(f'------------')

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt.head()}')

print(f'------------')

print (f'{Cargar_Txt}')

Lista_Animales = list(Cargar_Txt)

print(f'------------')

import pandas as pd

Ruta_Csv = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv = pd.read_csv(Ruta_Csv)

print (f'{Cargar_Csv.head()}')

print(f'------------')

Llaves3 = [f'Key{i}' for i in range(len(Cargar_Csv))]

print (f'{Llaves3}')

Lista_Nombres2 = list(Cargar_Csv['Nombre'])
Lista_Edades = list(Cargar_Csv['Edad'])

Men = min(Lista_Edades)
May = max(Lista_Edades)

print (f'La menor de las edades es {Men} y la mayor es {May}')

Diccionario_Csv = dict(zip(Llaves3, Lista_Nombres2))

print (f'{Diccionario_Csv}')

print (f'-------------')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Leer_Html)

print (f'{Cargar_Html[2].head()}')

print (f'-------------')

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

print (f'-------------')

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 2]}')
print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[1, 1:2]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodado: {Array2_Sorted}')
print (f'Acomodado: {round(Array2_Sorted_Mean, 2)}')
print (f'Acomodado: {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[0, 0:None])
Sumita4 = np.sum(Array2_Sorted[:])

print (f'El resultado de la sumita es {Sumita1}')
print (f'El resultado de la sumita es {Sumita2}')
print (f'El resultado de la sumita es {Sumita3}')
print (f'El resultado de la sumita es {Sumita4}')

print (f'-------------')

Array3 = np.array([[['e', 'p', 'k'], ['f', 'a', 'x']],    [['j', 'n', 'u'], ['m', 's', 'v']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 1]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[0, 0, ::2]}')
print (f'{Array3[0, 1, ::3]}')
print (f'{Array3[1, :, 0]}')
print (f'{Array3[0, 1, 1:2]}')
print (f'{Array3[1, 1, 0:None]}')
print (f'{Array3[1, 1, :]}')
print (f'{Array3[Array3 == "a"]}')

print (f'-------------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],            [[[6, 5, 4], [9, 8, 7]], [[0, 4, 9], [6, 3, 7]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[0, 1, 0, 2]}')
print (f'{Array4[0, 1, 0, :2]}')
print (f'{Array4[0, 1, 0, 2:]}')
print (f'{Array4[1, 0, 1, ::2]}')
print (f'{Array4[1, 0, 0, ::3]}')
print (f'{Array4[1, 1, :, 2]}')
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
Sumita7 = np.sum(Array4_Sorted[1, 1, 1, 0:None])
Sumita8 = np.sum(Array4_Sorted[1, 1, 1, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'-------------')

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El menor de los numeros es {Array_Num1_Min} y el mayor es {Array_Num1_Max}')

print (f'-------------')

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

print (f'-------------')

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 0]}')

print (f'-------------')

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 0]}')

print (f'-------------')

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 2]}')

print (f'-------------')

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

print (f'-------------')

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[0, 1, 0, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[0, 2]}')

print (f'-------------')

Tupla_Array = tuple(('Rojo', 'Verde'))
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array["Nombre"][2])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'-------------')

print (f'{Array_Gen6[3]}')

print (f'-------------')

Array_Num3 = np.arange(start=1, stop=11, step=1)
Array_Num4 = np.arange(start=2, stop=21, step=2)
Array_Num5 = np.arange(start=3, stop=31, step=3)
Array_Num6 = np.arange(start=10, stop=21, step=2)
Array_Num7 = np.arange(10)

print (f'{Array_Num3}')
print (f'{Array_Num4}')
print (f'{Array_Num5}')
print (f'{Array_Num6}')
print (f'{Array_Num7}')

print (f'-------------')

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')

print (f'-------------')

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

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

Sumita9 = np.sum(Array_Random2_Sorted, axis=0)
Sumita10 = np.sum(Array_Random2_Sorted, axis=1)
Sumita11 = np.sum(Array_Random2_Sorted[0, 0:None])
Sumita12 = np.sum(Array_Random2_Sorted[0, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

print (f'-------------')

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

print (f'-------------')

Array_Random3 = np.random.randint(low=1, high=10, size=(20))

print (f'{Array_Random3}')

Array_Random3_Reshape = np.reshape(Array_Random3, shape=(4, 5))

print (f'{Array_Random3_Reshape}')

Array_Random3_Reshape_Ravel = np.ravel(Array_Random3_Reshape)

print (f'{Array_Random3_Reshape_Ravel}')

print (f'-------------')

Lista_Array2 = ['Erick', 'Josue']

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-------------')

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concat([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'-------------')

Array_Concatenate_Split = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Split[0]}')
print (f'{Array_Concatenate_Split[1]}')
print (f'{Array_Concatenate_Split[2]}')

print (f'-------------')

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'-------------')

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'-------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'-------------')

Array_Random4 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random4}')

Sumita13 = np.sum(Array_Random4, axis=0)
Sumita14 = np.sum(Array_Random4, axis=1)
Sumita15 = np.sum(Array_Random4[1, 0, 0:None])
Sumita16 = np.sum(Array_Random4[1, 0, :])

print (f'El resultado de la sumita es {Sumita13}')
print (f'El resultado de la sumita es {Sumita14}')
print (f'El resultado de la sumita es {Sumita15}')
print (f'El resultado de la sumita es {Sumita16}')

print (f'-------------')

Lista_Sorteo = ['Erick', 'Josue']
Lista_Sorteo.append('Karlita')
Lista_Sorteo.insert(1, 'Roxana')
Lista_Sorteo.extend(['Carmelo', 'Susanita'])

print (f'{Lista_Sorteo}')

Ganador1 = np.random.choice(Lista_Sorteo, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Sorteo, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Sorteo, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-------------')

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-------------')

def Generadora1():
    for elemento in range(5):
        yield f'El numero es {elemento}'

Gen1 = Generadora1()

try:
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
except StopIteration:
    print (f'Fin del experimento')

print (f'-------------')

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
    print(f'Fin del experimento')

print (f'-------------')

def Generadora3():
    for elemento in range(5):
        if (elemento == 0):
            yield f'ZERO'
        elif (elemento == 1):
            yield f'ONE'
        elif (elemento == 2):
            yield f'TWO'
        elif (elemento == 3):
            yield f'THREE'
        elif (elemento == 4):
            yield f'FOUR'
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
    print(f'Fin del experimento')

print (f'-------------')

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int) -> int:
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
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(45)}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 36, 3.5, not True)

print (f'{Funcion_Tupla("Perro", 36, 3.5, not True)}')
print (f'{Funcion_Tupla("Perro", 36, 3.5, not True)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 36, 3.5, not True))}')

print (f'-------------')

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')

Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])

print (f'-------------')

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')
print (f'Los numeros pares de la lista son {list(Anonima3)} o incluso podrian ser {PEPE.Lista_Pares}')

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
    Lista_Closure = []
    def Closure_Interna(x):
        Lista_Closure.append(x)

        return Lista_Closure

    return Closure_Interna

Variable_Closure = Closure_Externa()

print (f'{Variable_Closure(10)}')
print (f'{Variable_Closure(26)}')
print (f'{Variable_Closure(38)}')

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
        Anonima4 = filter(lambda Num : Num % 2 == 0, Lista)
        Lista_Impares = [num for num in Lista if num % 2 != 0]

        print (f'Los elementos impares de la lista son {Lista_Impares} o incluso podrian ser {list(Anonima4)}')
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
        return Segunda(*args, **kwargs) * 3

    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(4, 6)}')

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

print (f'-------------')

from Module_Own import Pokemon as Poke

Objeto1 = Poke(PEPE.Diccionario_Poke["Poke1"], 'Electrico', 'Impact Trueno')
Objeto2 = Poke(PEPE.Diccionario_Poke["Poke2"], 'Roca', 'Sismo')
Objeto3 = Poke(PEPE.Diccionario_Poke["Poke3"], 'Agua', 'Hidro-Chorro')

Objeto3.Mostrar()

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
variable6, variable7 = not False, Objeto2.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')
print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[2]} tiene {Variable_Sumatoria} o {Sumatoria2(1, 2, 3, 4, 5)} o incluso {Objeto3.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1,  'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto2.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Este es un rango de numeros de la lista 2 {PEPE.Lista2[2:4]}')

print (f'{Lista_Uno[2]} eso es un {PEPE.Lista2[2]}?')

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

print (f'-------------')

print (f'{PEPE.__dir__()}')

print (f'-------------')

print (f'{help(PEPE)}')

print (f'-------------')

Tupla1 = ('Uno', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos')

print (f'{Tupla1}')

Tupla1 = tuple(('Uno', 'Dos', 'Tres'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')

print (f'{Tupla2[0]}')

Set_Conjunto1 = {'Roca', Objeto2.Tipo, Objeto2.Tipo, Objeto2.Tipo, Objeto2.Tipo}
Set_Conjunto1.add(Objeto1.Tipo)

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Rojo', 'Verde', 'Azul'})

print (f'{Set_Conjunto1}')

Set_Conjunto2 = {1, 2, 3, 4, 5}
Set_Conjunto3 = {4, 5}
Set_Conjunto4 = set({8})

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')
Set_Conjunto_Menu2 = frozenset({'Caramelo', 'Uva'})
Set_Conjunto_Menu3 = set({Objeto3.Ataque, Set_Conjunto_Menu2})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

print (f'-------------')

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Variable_Sumatoria,
    'Votante' : not True
}

Diccionario2 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
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

Edades = list(Data_Frame_Concatenate['Edad'])

Diccionario1 = dict({1 : "Karlita", 2 : Edades[5], 3 : variable7})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-------------')

print (f'{Diccionario2["Nombre"][2]} no puede votar ya que solo tiene {Diccionario1.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'HolaMundo')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio3 = [f'key_{i}' for i in range(len(Data_Frame_Concatenate))]

Diccionario_Vacio2["Uno"] = Objeto1.Nombre

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')
print (f'{Diccionario_Vacio3}')

print (f'-------------')

Lista_Dict_Vacio = ['Gato', 'Raton', 'Perro']

Llaves = [f'Key_{i}' for i in range(len(Lista_Dict_Vacio))]

Diccionario_Final = dict(zip(Llaves, Lista_Dict_Vacio))

print (f'{Diccionario_Final}')

print (f'-------------')

Llaves4 = [f'Llave{i}' for i in range(len(Cargar_Csv))]
Lista_Nombres2 = list(Cargar_Csv['Nombre'])

print (f'{Llaves4}')
print (f'{Lista_Nombres2}')

Diccionario_Csv2 = dict(zip(Llaves4, Lista_Nombres2))

print (f'{Diccionario_Csv2}')

print (f'-------------')

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
print (f'El tipo de dato de la variable es {type(Objeto3.Catched)}')
print (f'El tipo de dato de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato de la variable es {type(Tupla3)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de dato de la variable es {type(Diccionario_Vacio3)}')
print (f'El tipo de dato de la variable es {type(Funcion_Tupla)}')
print (f'El tipo de dato de la variable es {type(PEPE)}')
print (f'El tipo de dato de la variable es {type(Array5)}')
print (f'El tipo de dato de la variable es {type(Data_Frame1)}')
print (f'El tipo de dato de la variable es {type(Objeto2)}')
print (f'El tipo de dato de la variable es {type(PEPE.Objeto4)}')

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

if (variable1 == 'Erick' and Objeto2.Cantidad < 20):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')

if (variable2 == 'Porez' or Objeto1.Nombre == 'Graveler'):
    print (f'Al menos una de las condiciones se cumplen')
else:
    print (f'Error, ninguna de las condiciones se cumplen')

Contador1 = 0
Contador2 = 1

while (Contador1 <= 5 and Contador2 <= 5):
    print (f'Contador {Contador1}')
    Contador1+= 1
    Contador2+= 1

print (f'-------------')

Contador1 = 0
Contador2 = 1

while (Contador1 <= 5 or Contador2 <= 5):
    print (f'Contador {Contador1}')
    Contador1+= 1
    Contador2+= 1

print (f'-------------')

print (f'{dir(variable1)}')

print (f'-------------')

class Entrenador:
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Anonima2(15)
        self.Classified = variable6

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')

Objeto5 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto1.Nombre)
Objeto6 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto2.Nombre)
Objeto7 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto3.Nombre)

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

print (f'-------------')

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'-------------')

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'El elemento en la posicion {indice} es {elemento}')

print (f'-------------')

variable8 = 'esTeBAN'
letra_variable8 = variable8[0]

print (f'{variable8}')
print (f'{variable8.lower()}')
print (f'{variable8.upper()}')
print (f'{variable8.capitalize()}')

print (f'{variable8.lower().find("t")}')
print (f'{variable8.lower().index("b")}')

print (f'La letra {letra_variable8} aparece un total de {variable8.lower().count(letra_variable8)} veces')

print (f'{variable8.lower().startswith(letra_variable8)}')
print (f'{variable8.lower().endswith("n")}')

print (f'{variable8.lower().replace("ban", "POPOTAMO")}')

variable9 = 'esto es un texto cualquiera pero quiero probar si funciona'
Lista_variable9 = variable9.split(' ')

for elemento in Lista_variable9:
    print (f'{elemento}')

print (f'La cantidad de palabras digitadas son {len(Lista_variable9)}')

print (f'{PEPE.Tupla_Poke[2]} aparece en la posicion {PEPE.Tupla_Poke.index("Misty")}')

print (f'-------------')

for elemento in Diccionario_DataFrame:
    print (f'{Diccionario_DataFrame[elemento]}')

print (f'-------------')

for elemento in Diccionario1.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1

print (f'-------------')

Lista_Animales2 = ['Perro', PEPE.Lista2[2], 'Cocodrilo']
Lista_Animales2.append('Tigre')

Contador = 0

while (Contador < len(Lista_Animales2)):
    if (Lista_Animales2[Contador] == 'Cocodrilo'):
        print (f'Este bicho es un reptil')
        break
    else:
        Contador+= 1
        continue

for elemento1, elemento2 in zip(Lista_Animales2, Tupla1):
    print (f'{elemento1} -- {elemento2}')

print (f'-------------')

for elemento in range(5):
    print (f'{elemento}')

for elemento in range(995, 1000):
    print (f'{elemento}')

Lista_Numeros_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Contador = 0

while (Contador <= 5):
    print (f'Contador {Contador}')
    Contador+= 1

Minimo = min(Lista_Numeros_Mult)
Maximo = max(Lista_Numeros_Mult)

Redondeo = round(14.458795, 2)

Sumatoria4 = sum(Lista_Numeros_Mult)

print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool("")}')
print (f'{bool(False)}')
print (f'{bool(not True)}')

Todo_All = all([Lista_Uno_Copia, Set_Conjunto_Menu2, Tupla2, None])

print (f'{Todo_All}')

Uno = int("500")
Dos = str(500)
Tres = float(Dos)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')

print (f' - '.join(PEPE.Set_Conjunto_Poke))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

import Paquete.Sub_Paquete.Segundo as PEPE3

PEPE2.Saludar5()

Variable_PEPE3 = PEPE3

def Exception_Final():
    while True:
        Numero = input(f'Ingrese un numero entero: ')
        try:
            Numerito = int(Numero)
            break
        except:
            print (f'Error, necesito que ingreses un numero: ')

    return Numerito

print (f'Gracias, tu numero digitado es {Exception_Final()}')

import re

Correo = 'sample@sample.com'

Patron3 = r'[a-zA-Z0-9*/&%]+@[a-zA-Z0-9*/&%]+.[a-z]{3}'

Buscar23 = re.match(Patron3, Correo)

if (Buscar23):
    print (f'Formato valido')
else:
    print (f'Formato incorrecto')

print (f'-------------')

class Persona:
    def __init__(self, Nombre, Nacionalidad, Sexo):
        self.Nombre = Nombre
        self.Nacionalidad = Nacionalidad
        self.Sexo = Sexo

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Nacionalidad: {self.Nacionalidad}')
        print (f'Sexo: {self.Sexo}')

class Trabajador(Persona):
    def __init__(self, Nombre, Nacionalidad, Sexo, Ciudad, Profesion):
        super().__init__(Nombre, Nacionalidad, Sexo)
        self.Ciudad = Ciudad
        self.Profesion = Profesion

    def Desplegar(self):
        print (f'{self.Nombre} vive en {self.Ciudad} y su profesion es {self.Profesion}')

Objeto8 = Trabajador('Erick', 'costarricense', 'masculino', 'San Jose', 'Programador')

Objeto8.Mostrar()

Objeto8.Desplegar()

def Ejemplo1(Numerito):
    return Variable_Sumatoria * Sumatoria2(1, 2, 3, 4) + Numerito

print (f'El resultado de la operacion es {Ejemplo1(PEPE.Flotante1)}')

Resultado2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado2}')

def Ejemplo3(Cadenita):
    Lista_Cadenita = Cadenita.split(' ')

    for indice, elemento in enumerate(Lista_Cadenita, start=1):
        print (f'El elemento en la posicion {indice} es {elemento}')

    print (f'La cantidad de palabras digitadas es {len(Lista_Cadenita)}')

Ejemplo3(PEPE.Flotante3)

Lista_Alumnos = list([])

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento}: ')
        Lista.append(Alumno)

    return Lista

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nLa lista de estudiantes es {Colegio(Lista_Alumnos)}'])
    Docu.close()

with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

Lista_Alumnos2 = []

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio2(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumon {elemento}: '))

        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)

    Lista.sort(key=lambda Num : Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]

    print (f'El estudiante mas joven es {Menore} y el mayor de todos es {Mayore}')

Colegio2(Lista_Alumnos2)
