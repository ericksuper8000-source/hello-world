import matplotlib.dviread

List1 = list(['Erick', 'Josue', 'Karlita'])

Key1 = [f'Key{i}' for i in range(len(List1))]

print (f'{Key1}')

Dict1 = dict(zip(Key1, List1))

print (f'{Dict1}')

import pandas as pd

Ruta_Csv1 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

Key2 = [f'Key_{i}' for i in range(len(Cargar_Csv1))]

List2 = list(Cargar_Csv1['Nombre'])

print (f'{Key2}')
print (f'{List2}')

Dict2 = dict(zip(Key2, List2))

print (f'{Dict2}')

class Persona:
    def __init__(self, Nombre, Genero, Edad):
        self.Nombre = Nombre
        self.Genero = Genero
        self.Edad = Edad

    def Mostrar(self):
        print (f'{self.Nombre} es de genero {self.Genero} y su edad son {self.Edad} años')

class Trabajador(Persona):
    def __init__(self, Nombre, Genero, Edad, Profesion, Ciudad):
        super().__init__(Nombre, Genero, Edad)
        self.Profesion = Profesion
        self.Cuidad = Ciudad

    def Desplegar(self):
        print (f'{self.Nombre}, tu profesion es {self.Profesion} y vives en {self.Cuidad}')

Objeto1 = Trabajador(Dict2['Key_2'], 'Femenino', 6, 'Estudiante', 'San Jose')

Objeto1.Mostrar()
Objeto1.Desplegar()

print (f'--------------------')

class Camara:
    def tomar_fotos(self):
        print (f'Has tomado una fotografia')

class Reproductor:
    def reproducir_musica(self):
        print (f'Has reproducido la musica')

class SmartPhone(Camara, Reproductor):
    def encender_smartphone(self):
        print (f'El smartphone ha sido encendido')

Objeto2 = SmartPhone()

Objeto2.tomar_fotos()
Objeto2.reproducir_musica()
Objeto2.encender_smartphone()

print (f'--------------------')
'''
import pandas as pd
from datetime import datetime

Ruta_Csv2 = 'C:\\python-data-analyzer\\data\\sales.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

Fecha = input(f'Ingrese una fecha con formato YY-MM-DD: ')

try:
    Formato = datetime.strptime(Fecha, '%Y-%m-%d').date()
    Formato_Correcto = pd.to_datetime(Formato)
    Cargar_Csv2['date'] = pd.to_datetime(Cargar_Csv2['date'])
except ValueError:
    print (f'Formato incorrecto')
    exit()

Encontrado = Cargar_Csv2[Cargar_Csv2['date'].dt.date == Formato_Correcto.date()]

if (Encontrado.empty):
    print (f'No se han encontrado ventas en {Formato_Correcto}')
else:
    print (f'Genial! se han encontado {len(Encontrado)} ventas en esta fecha: {Formato_Correcto}')

'''

import re

Email1 = 'usuario123@empresa.cr'

Pattern1 = r'^[a-zA-Z0-9_+-.#]+@[a-zA-Z0-9]+\.\D{2,}$'

Buscar1 = bool(re.match(Pattern1, Email1))

print (f'{Buscar1}')

Texto1 = "El cliente compró 3 camisas por 25000 colones y 2 pantalones por 40000 colones."

Buscar2 = re.findall(r'\d+', Texto1)

Lista_Buscar2 = []

print (f'{Buscar2}')

for indice, elemento in enumerate(Buscar2, start=1):
    Lista_Buscar2.append(int(elemento))

print (f'{Lista_Buscar2}')
print (f'{type(Lista_Buscar2)}')

print (f'------------')

Texto2 = "Se pagaron ₡25000 por materiales, ₡7800 por transporte y ₡150000 por maquinaria."

Buscar3 = re.findall(r'₡(\d+)', Texto2)
Lista_Buscar3 = list([])

print (f'{Buscar3}')

for elemento in enumerate(Buscar3):
    Lista_Buscar3.append(int(elemento[1]))

print (f'{Lista_Buscar3}')
print (f'{type(Lista_Buscar3)}')

print (f'------------')

phone_number = '8888-8888'

Pattern2 = r'^[0-9]{4}\-\d{4}$'

Buscar4 = bool(re.match(Pattern2, phone_number))

if (Buscar4 == True):
    print (f'Formato correcto')
else:
    print (f'Formato incorrecto')

def Funcion_Correo(Correo):
    Email2 = Correo
    Pattern3 = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.com$'
    Buscar5 = bool(re.match(Pattern3, Email2))

    return Buscar5

if (Funcion_Correo('juan123@gmail.com') == True):
    print (f'Formato de correo electronico correcto')
else:
    print (f'Formato de correo electronico incorrecto')

print (f'------------')

def Funcion_Correo2(Correo):
    Email3 = Correo
    Pattern4 = r'^[a-zA-Z0-9]{1}(\.[a-zA-Z0-9]+)?@[a-zA-Z]+\.com$'
    Buscar6 = bool(re.match(Pattern4, Email3))

    return Buscar6

print (f'{Funcion_Correo2("samp.le@sample.com")}')

import re

Texto3 = 'ESTO ES un eje45mplo cualquiera, $10.00000 pero hola lo que  hela deseo es ver 9 si la mica funciona @14 orrectamente hala'

Buscar7 = re.search(r'\d+', Texto3)
Buscar8 = re.findall(r'\d+', Texto3)
Buscar9 = re.findall(r'\$(\d+)', Texto3)

print (f'{Buscar7}')
print (f'{Buscar8}')
print (f'{Buscar9}')

Buscar10 = re.findall(r'(\.[0-9]+)?', Texto3)

print (f'{Buscar10}')

Buscar11 = re.findall(r'\D+', Texto3)

print (f'{Buscar11}')

Buscar12 = re.findall(r'\w+', Texto3)
Buscar13 = re.findall(r'\W+', Texto3)

print (f'{Buscar12}')

print (f'------------')

print (f'{Buscar13}')

Buscar14 = re.search(r'\s+', Texto3)
Buscar15 = re.findall(r'\S+', Texto3)

print (f'{Buscar14}')
print (f'{Buscar15}')

Buscar16 = re.findall(r'h.la', Texto3)

print (f'{Buscar16}')

Buscar17 = re.findall(r'\d+', Texto3)
Buscar18 = re.findall(r'\d?', Texto3)
Buscar19 = re.findall(r'\d*', Texto3)
Buscar20 = re.findall(r'\d{2}', Texto3)
Buscar21 = re.findall(r'\d{1,}', Texto3)
Buscar22 = re.findall(r'\d{1,2}', Texto3)

print (f'{Buscar17}')
print (f'{Buscar18}')
print (f'{Buscar19}')
print (f'{Buscar20}')
print (f'{Buscar21}')
print (f'{Buscar22}')

Buscar23 = re.fullmatch(r'ESTO ES un eje45mplo cualquiera, \$10.00000 pero hola lo que  hela deseo es ver 9 si la mica funciona \@14 orrectamente hala', Texto3)

print (f'{Buscar23}')

Pattern6 = r'[A-Z]+|(\$10.00000){1}'

Buscar24 = re.findall(Pattern6, Texto3)

print (f'{Buscar24}')

Texto4 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern7 = r'[0-9]{2}/\d{2}/[0-9]{4}'

Replacement = 'Fecha Oculta'

Nueva_Fecha = re.sub(Pattern7, Replacement, Texto4)

print (f'{Nueva_Fecha}')

def Exception1(Num):
    Numero = Num
    try:
        Numerito = int(Numero)
        return f'Gracias, el numero digitado es {Numerito}'
    except ValueError:
        return f'Error, necesito que ingreses un numero'

print (f'{Exception1(5)}')

def Funcion2(Num1, Num2):
    try:
        Resultado = Num1 + Num2
        return f'El resultado de la operacion es {Resultado}'
    except TypeError:
        return f'Error, ambos elementos deben ser numeros'

print (f'{Funcion2(12, "Hola")}')

def Exception3(Num1, Num2):
    try:
        Div = Num1 / Num2
        return f'El resultado de la division es {round(Div, 2)}'
    except ZeroDivisionError:
        return f'Error, el divisor no puede ser un cero'

print (f'{Exception3(12, 0)}')

Lista_Exception4 = ['Erick', 'Josue', 'Karlita']

def Exception4(Indice):
    try:
        print (f'El elemento con el indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El elemento con la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception5("Votante")

try:
    with open('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Durazno')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo seleccionado no fue encontrado')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')

try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado es incorrecto')

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
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [55, 14, 26],
    'Votante' : [True, False, not False]
})

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

print (f'{Data_Frame1["Nombre"]}')

print (f'--------')

print (f'{Data_Frame1}')

print (f'--------')

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame_Concatenate_Age}')

print (f'--------')

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()} y la mayor de las edades es {Data_Frame_Concatenate_Age.max()}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'--------')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombre = elemento['Nombre']
    Edad = elemento['Edad']

    print (f'Mi nombre es {Nombre} y mi edad es {Edad}')

print (f'--------')

''''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'--------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'--------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

'''

print (f'--------')

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'--------')

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'--------')

print (f'{Data_Frame_Concatenate.tail(1)}')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'La cantidad de filas son {Filas} y la cantidad de columnas son {Columnas}')

Elemento1 = Data_Frame1.loc[0, 'Nombre']
Elemento2 = Data_Frame1.loc[1, 'Edad']
Elemento3 = Data_Frame1.loc[2, 'Votante']
Elemento4 = Data_Frame1.loc[:, 'Edad']
Elemento5 = Data_Frame1.loc[2, :]

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')
print (f'{Elemento4}')
print (f'{Elemento5}')

print (f'--------')

Elemento6 = Data_Frame2.iloc[0, 0]
Elemento7 = Data_Frame2.iloc[1, 1]
Elemento8 = Data_Frame2.iloc[2, 2]
Elemento9 = Data_Frame2.iloc[0, :]
Elemento10 = Data_Frame2.iloc[:, 1]

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')
print (f'{Elemento9}')
print (f'{Elemento10}')

print (f'--------')

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine='openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'--------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col="tarifa")
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:J")
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:J", nrows=1)

print (f'{Cargar_Excel1.head()}')

print (f'--------')

print (f'{Cargar_Excel2.head()}')

print (f'--------')

print (f'{Cargar_Excel3.head()}')

print (f'--------')

print (f'{Cargar_Excel4.head()}')

print (f'--------')

print (f'{Cargar_Excel5.head()}')

print (f'--------')

print (f'{Cargar_Excel6.head()}')

print (f'--------')

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='Five', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'--------')

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='Five', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'--------')

print (f'{Cargar_Txt.head()}')

print (f'--------')

import pandas as pd

Ruta_Csv2 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2.head()}')

print (f'--------')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Leer_Html)

print (f'{Cargar_Html[1].head()}')

print (f'--------')

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

print (f'--------')

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
print (f'{Array2[0, 1:2]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[0, :]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodado {Array2_Sorted}')
print (f'Media {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[1, 0:None])
Sumita4 = np.sum(Array2_Sorted[1, :])

print (f'El resultado de la sumita es {Sumita1}')
print (f'El resultado de la sumita es {Sumita2}')
print (f'El resultado de la sumita es {Sumita3}')
print (f'El resultado de la sumita es {Sumita4}')

print (f'--------')

Array3 = np.array([[['a', 'b', 'c'], ['d', 'e', 'f']],                    [['g', 'h', 'i'], ['j', 'k', 'l']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 1]}')
print (f'{Array3[1, 1, :2]}')
print (f'{Array3[1, 1, 2:]}')
print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[1, 0, 1:2]}')
print (f'{Array3[0, :, 1]}')
print (f'{Array3[1, 1, 0:None]}')
print (f'{Array3[1, 1, :]}')
print (f'{Array3[Array3 == "a"]}')

print (f'--------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 4, 5]]],           [[[3, 2, 1], [6, 5, 4]], [[9, 8, 7], [1, 6, 3]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 2]}')
print (f'{Array4[1, 1, 0, :2]}')
print (f'{Array4[1, 1, 0, 2:]}')
print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[0, 1, 0, ::3]}')
print (f'{Array4[1, 0, 0, 1:2]}')
print (f'{Array4[0, 1, :, 2]}')
print (f'{Array4[1, 0, 1, 0:None]}')
print (f'{Array4[1, 0, 1, :]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[1, 0, 0, 0:None])
Sumita8 = np.sum(Array4_Sorted[1, 0, 0, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'--------')

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_Min = np.min(Array_Num1)
Array_Max = np.max(Array_Num1)

print (f'El menor de los numeros es {Array_Min} y el mayor es {Array_Max}')

print (f'--------')

Array_Num2 = np.arange(25)

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

Array_Num2_Reshape_Column_Min = np.min(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Column_Max = np.max(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Row_Min = np.min(Array_Num2_Reshape, axis=1)
Array_Num2_Reshape_Row_Max = np.max(Array_Num2_Reshape, axis=1)

print (f'Los menores de las columnas son {Array_Num2_Reshape_Column_Min}')
print (f'Los menores de las columnas son {Array_Num2_Reshape_Column_Max}')
print (f'Los menores de las columnas son {Array_Num2_Reshape_Row_Min}')
print (f'Los menores de las columnas son {Array_Num2_Reshape_Row_Max}')

print (f'--------')

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 1]}')

print (f'--------')

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 0]}')

print (f'--------')

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[0, 1]}')

print (f'--------')

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

print (f'{Array_Gen2}')

Lista_Fuecoco = []

for elemento in Array_Gen2:
    Lista_Fuecoco.append(str(elemento))

print (f'{Lista_Fuecoco}')
print (f'{type(Lista_Fuecoco)}')

print (f'--------')

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[0, 0, 1, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 1]}')

print (f'--------')

Tupla_Array = ('Rojo', 'Azul')
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array["Nombre"][1])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'--------')

print (f'{Array_Gen6[3]}')

print (f'--------')

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

print (f'--------')

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')

print (f'--------')

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
Sumita11 = np.sum(Array_Random2_Sorted[1, 0:None])
Sumita12 = np.sum(Array_Random2_Sorted[1, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

print (f'--------')

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

print (f'--------')

Array_Num8 = np.arange(20)

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'--------')

Lista_Array1 = ['Erick', 'Josue', 'Karlita']

Array5 = np.array(Lista_Array1)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'--------')

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concatenate([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'--------')

Array_Concatenate_Split = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Split[0]}')
print (f'{Array_Concatenate_Split[1]}')
print (f'{Array_Concatenate_Split[2]}')

print (f'--------')

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'--------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'--------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'--------')

for Matriz2 in Array3:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'--------')

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


print (f'--------')

Lista_Participantes = list(['Erick', 'Josue', 'Karlita', 'Carmelo', 'Susanita', 'Roxana'])

Ganador1 = np.random.choice(Lista_Participantes, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Participantes, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Participantes, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'--------')

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'--------')