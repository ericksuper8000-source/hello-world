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

def Generadora1():
    for elemento in range(1, 6):
        yield f'El elemento es {elemento}'

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

print (f'--------')

def Generadora2():
    for elemento in range(1, 6):
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

print (f'--------')

def Generadora3():
    for elemento in range(1, 6):
        if (elemento == 1):
            yield f'ONE'
        elif (elemento == 2):
            yield f'TWO'
        elif (elemento == 3):
            yield f'THREE'
        elif (elemento == 4):
            yield f'FOUR'
        elif (elemento == 5):
            yield f'FIVE'
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

print (f'--------')

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int) -> int:
        return Num1 + Num2

    return Sumatoria_Interna(3)

Variable_Sumatoria = Sumatoria_Externa(4)

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
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(123)}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

print (f'--------')

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.6, 100, False)

print (f'{Funcion_Tupla("Perro", 3.6, 100, False)}')
print (f'{Funcion_Tupla("Perro", 3.6, 100, False)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.6, 100, False))}')

print (f'--------')

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')

Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])

print (f'--------')

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre} tu numero favorito es {sum(args)}'

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

def Closure_Externo():
    Lista_Closure = list([])
    def Closure_Interno(x):
        Lista_Closure.append(x)

        return Lista_Closure

    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(25)}')
print (f'{Variable_Closure(33)}')

def Crear_Multiplicador(x):
    def Multiplicador(y):
        return x * y

    return Multiplicador

Mult1 = Crear_Multiplicador(2)
Mult2 = Crear_Multiplicador(3)

print (f'El multiplicador es {Mult1(10)}')
print (f'El multiplicador es {Mult2(10)}')

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
def Saludar3():
    print (f'Hola Mundo')

Saludar3()

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 12

    return Tercera

@Primera
def Sumatoria3(Num1, Num2):
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(4, 8)}')

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'JONATHAN'
        Apellido = 'SMITH'
        return Segunda(Nombre, Apellido)

    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    print (f'Mi nombre es {Nombre} {Apellido}')

Usuario2("Erick", "Perez")

print (f'--------')

from Module_Own import Pokemon as Poke

class Hija_Poke(Poke):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Desplegando(self):
        print (f'{self.Nombre} es de tipo {self.Tipo} / {self.Sub_Tipo}')

Objeto1 = Poke(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto2 = Poke(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')
Objeto3 = Hija_Poke(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Objeto2.Mostrar()

print (f'--------')

Objeto3.Desplegando()

class Erick:
    def Hablar1(self):
        print (f'Hola Erick')

class Josue:
    def Hablar2(self):
        print (f'Hola Josue')

class Karlita(Erick, Josue):
    def Hablar3(self):
        print (f'Hola Karlita')

Objeto4 = Karlita()

Objeto4.Hablar1()
Objeto4.Hablar2()
Objeto4.Hablar3()

print (f'--------')

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
variable6, variable7 = Objeto3.Catched, not False

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')
print (f'Mi nombre es {Lista_Uno[0]} {variable2}')
print (f'{PEPE.Tupla_Poke[2]} tiene {Variable_Sumatoria} o {Sumatoria2(1, 2, 3, 4, 5)} o incluso podrian ser {Objeto3.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto3.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Este es un rango de elementos de la lista 2 {PEPE.Lista2[2:4]}')

print (f'{Lista_Uno[1]} eso que esta ahi es un {PEPE.Lista2[2]}?')

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

print (f'{help(PEPE)}')

Tupla1 = ('Agua', Objeto2.Tipo, Objeto3.Sub_Tipo, Objeto3.Sub_Tipo, Objeto3.Sub_Tipo, Objeto3.Sub_Tipo, Objeto3.Sub_Tipo)

print (f'{Tupla1}')

Tupla1 = tuple(('Water', 'Fire', 'Electricity'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{Tupla1}')
print (f'{Tupla2}')
print (f'{Tupla3}')

Set_Conjunto1 = {'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo'}
Set_Conjunto1.add('Verde')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Red', 'Blue', 'Green'})

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

Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, Objeto2.Nombre})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

print (f'--------')

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Variable_Sumatoria,
    'Votante' : not False
}

Diccionario2 = {
    'Nombre' : ['Erick', 'Josue', 'Karlita'],
    'Edad' : [37, 10*2, 6],
    'Votante' : [True, not False, False]
}

Diccionario3 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1["Nombre"]}')
print (f'{Diccionario1.get("Edad")}')

print (f'--------')

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2["Nombre"][1]}')
print (f'{Diccionario2.get("Edad")[2]}')

print (f'--------')

Diccionario1["Nombre"] = Lista_Uno_Copia[0]

print (f'{Diccionario1}')

del Diccionario1["Nombre"]
Diccionario1.pop("Edad")

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')

Diccionario1 = dict({1 : "Karlita", 2 : 6, 3 : False})

print (f'{Diccionario1}')

print (f'{Diccionario2["Nombre"][2]} no puede votar ya que solo tiene {Diccionario1.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABCD', 'Hola Mundo')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = Objeto3.Nombre

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')

Lista_Dict1 = ['Erick', 'Josue', 'Karlita']
Key3 = [f'Key{i}' for i in range(Lista_Dict1.__len__())]

print (f'{Key3}')

Diccionario_Vacio3 = dict(zip(Key3, Lista_Dict1))

print (f'{Diccionario_Vacio3}')
print (f'{Diccionario_Vacio3.keys()}')
print (f'{Diccionario_Vacio3["Key2"]}')
print (f'{Diccionario_Vacio3.get("Key1")}')

Diccionario_Vacio4 = dict([])
i = 0

for elemento in Lista_Dict1:
    Diccionario_Vacio4[i] = elemento
    i+= 1

print (f'{Diccionario_Vacio4}')

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
print (f'{type(variable6)}')
print (f'{type(Lista_Uno_Copia)}')
print (f'{type(Tupla_Array)}')
print (f'{type(Set_Conjunto_Array)}')
print (f'{type(Diccionario_Vacio2)}')
print (f'{type(Funcion_Correo2)}')
print (f'{type(PEPE)}')
print (f'{type(Objeto4)}')
print (f'{type(Array7)}')
print (f'{type(Data_Frame2)}')

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

if (variable1 == 'Erick' and Objeto1.Nombre == 'Graveler'):
    print (f'AMBAS CONDICIONES SE CUMPLEN')
else:
    print (f'AL MENOS UNA DE LAS CONDICIONES NO SE CUMPLEN')

if (variable1 == 'Josue' or Objeto1.Nombre == 'Graveler'):
    print (f'BIEN')
else:
    print (f'MAL')

print (f'{dir(variable1)}')

class Entrenador:
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Variable_Sumatoria
        self.Classified = variable7

    def Desplegar(self):
        print (f'{self.Trainer}, just catched a {self.Favorite} while visiting {self.City}')

Objeto5 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto1.Nombre)
Objeto6 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto2.Nombre)
Objeto7 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto3.Nombre)

Objeto6.Desplegar()

Negativo = -7

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

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'El elemento en la posicion {indice} es {elemento}')

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

variable9 = 'este es un elemento cualquiera pero quiero ver si sirve o no'

Lista_variable9 = variable9.split(' ')

for elemento in Lista_variable9:
    print (f'{elemento}')

print (f'La cantidad de palabras digitadas es {len(Lista_variable9)}')

print (f'{PEPE.Tupla_Poke[2]} aparece en la posicion {PEPE.Tupla_Poke.index("Misty")}')

print (f'--------')

for elemento in Diccionario1:
    print (f'{Diccionario1[elemento]}')

print (f'--------')

for elemento in Diccionario2.items():
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'--------')

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'El numero es {PEPE.Lista_Numeros[Contador]}')
    Contador+= 1

Lista_Animales = ['Ballena']
Lista_Animales.append('Cocodrilo')
Lista_Animales.insert(1, PEPE.Lista2[2])
Lista_Animales.extend(['Leon'])

print (f'{Lista_Animales}')

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Koala'):
        print (f'Este bicho es de Australia')
        break
    else:
        Contador+= 1
        continue

for elemento1, elemento2 in zip(Lista_Animales, Tupla1):
    print (f'{elemento2} - {elemento1}')

for elemento in range(5):
    print (f'{elemento}')

for elemento in range(995, 1000):
    print (f'{elemento}')

Lista_Numeros_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1

Numero_Menor = min(Lista_Numeros_Mult)
Numero_Mayor = max(Lista_Numeros_Mult)
Sumatoria4 = sum(Lista_Numeros_Mult)
Redondeo = round(14.458795, 2)

print (f'El numero menor es {Numero_Menor} y el mayor es {Numero_Mayor}')

print (f'El numero redondeado es {Redondeo}')

print (f'El resultado de la sumatoria es {Sumatoria4}')

print (f'{bool(False)}')
print (f'{bool(not True)}')
print (f'{bool(0)}')
print (f'{bool(None)}')
print (f'{bool("")}')

Todo_All = all([Lista_Uno_Copia, Tupla1, Set_Conjunto2, 0])

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

print (f'El resultado de la operacion es {Ejemplo1(PEPE.Flotante1)}')

Resultado2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado2}')

def Ejemplo3(Cadenita):
    Lista_Cadenita = Cadenita.split(' ')
    for elemento in enumerate(Lista_Cadenita):
        print (f'{elemento[0]} -- {elemento[1]}')

    print (f'La cantidad de palabras digitadas son {len(Lista_Cadenita)}')

Ejemplo3(PEPE.Flotante3)

Lista_Alumnos = []

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumnos = input(f'Ingrese el nombre del alumno {elemento}: ')
        Lista.append(Alumnos)

    return Lista

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nLa lista de estudiantes es {Colegio(Lista_Alumnos)}'])
    Docu.close()

with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

Lista_Alumnos2 = list([])

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio2(Lista):
    for elemento in range(Contador):
        Alumno_Name = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Age = int(input(f'Ingrese la edad del alumno {elemento}: '))
        Estudiante = [Alumno_Name, Alumno_Age]
        Lista.append(Estudiante)

    Lista.sort(key = lambda Num :  Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]

    print (f'El menor de los alumnos es {Menore} y el mayor de los alumnos es {Mayore}')

Colegio2(Lista_Alumnos2)

def Exception_Finale():
    while True:
        Numero = input(f'Ingrese un numero entero: ')
        try:
            Numerito = int(Numero)
            break
        except:
            print (f'Error, necesito que ingreses un numero entero')

    return Numerito

print (f'Gracias por ingresar el numero {Exception_Finale()}')