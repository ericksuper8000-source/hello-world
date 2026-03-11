import itertools


class Poke1:
    def __init__(self, Nombre, Tipo, Ataque):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque
        self.Cantidad = 18 * 2
        self.Catched = not True

class Poke1_Hijo(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Desplegar(self):
        print (f'{self.Nombre} es de tipo {self.Tipo} / {self.Sub_Tipo}')

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')

Objeto1 = Poke1_Hijo('Pikachu', 'Electrico', 'Impact Trueno', 'Acero')

Objeto1.Mostrar()
print (f'Yo tengo {Objeto1.Cantidad} {Objeto1.Nombre}s')

Objeto1.Desplegar()

class Camara:
    def Tomar_Foto(self):
        print (f'La fotografia se ha tomado')

class Musica:
    def Reproducir_Musica(self):
        print (f'La musica se ha reproducido')

class Smartphone(Camara, Musica):
    def Encender_Smartphone(self):
        print (f'El smartphone ha sido encendido')

Objeto2 = Smartphone()

Objeto2.Tomar_Foto()
Objeto2.Reproducir_Musica()
Objeto2.Encender_Smartphone()

Lista_Dict1 = ['Erick', 'Josue', 'Karlita']

Key1 = [f'Key{i}' for i in range(len(Lista_Dict1))]

print (f'{Key1}')

Diccionario0 = dict(zip(Key1, Lista_Dict1))

print (f'{Diccionario0}')

print (f'{Diccionario0}')
print (f'{Diccionario0.keys}')
print (f'{Diccionario0["Key0"]}')
print (f'{Diccionario0.get("Key1")}')

print (f'----------')

import pandas as pd

Ruta_Csv1 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

Key2 = [f'Key_{i}' for i in range(len(Cargar_Csv1))]

print (f'{Key2}')

Lista_Dict2 = list(Cargar_Csv1['Nombre'])

print (f'{Lista_Dict2}')

Diccionario00 = dict(zip(Key2, Lista_Dict2))

print (f'{Diccionario00}')
print (f'{Diccionario00.keys()}')
print (f'{Diccionario00["Key_1"]}')
print (f'{Diccionario00.get("Key_2")}')

print (f'----------')

import re

Texto1 = 'este es hola un texto ₡150 pero lo mas interesante! es hala que ₡66 colones no es lo mismo que hela tener ₡0 en el bolsillo'

Buscar1 = re.findall(r'₡(\d+)', Texto1)

print (f'{Buscar1}')

Lista_Buscar1 = list([])

for elemento in Buscar1:
    Lista_Buscar1.append(int(elemento))

print (f'{Lista_Buscar1}')

Telefono1 = '8888-8888'

Buscar2 = bool(re.match(r'[0-9]{4}\-\d{4}', Telefono1))

if (Buscar2 == True):
    print (f'El formato del numero de telefono es correcto')
else:
    print (f'Error, formato incorrecto')

Texto2 = 'Tu tarjeta caduca en 03/10/2026, es necesario que visites una sucursal antes de esta fecha'

Pattern1 = r'\d{2}\/[0-9]{2}\/\d{4}'

Hidden_Phone = 'XX/XX/XXXX'

Buscar3 = re.sub(Pattern1, Hidden_Phone, Texto2)

print (f'{Buscar3}')

Email1 = 'sample@sample.com'

Pattern2 = r'^[a-zA-Z0-9./*-+?_-]+\@[a-zA-Z]+\.[a-z]{2,}$'

Buscar4 = bool(re.match(Pattern2, Email1))

if (Buscar4 == True):
    print (f'El formato del correo es correcto')
else:
    print (f'El formato del correo es incorrecto')

print (f'----------')

Texto3 = 'este es hola un texto ₡150 pero lo mas interesante! es hala que ₡66 colones no es lo mismo que hela tener ₡0 en el bolsillo'

Buscar5 = re.search(r'\d+', Texto3)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\d+', Texto3)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\D+', Texto3)

print (f'{Buscar7}')

Buscar8 = re.findall(r'\w+', Texto3)

print (f'{Buscar8}')

Buscar9 = re.findall(r'\W+', Texto3)

print (f'{Buscar9}')

Buscar10 = re.findall(r'\s+', Texto3)

print (f'{Buscar10}')

Buscar11 = re.findall(r'[\S+]', Texto3)

print (f'{Buscar11}')

Buscar12 = re.findall(r'h.la', Texto3)

print (f'{Buscar12}')

Buscar13 = re.findall(r'hol[a]{3}', 'holaaa')

print (f'{Buscar13}')

Buscar14 = re.findall(r'hol[a]{4,}', 'holaaa')

print (f'{Buscar14}')

Buscar15 = re.findall(r'hol[a]{3,6}', 'holaaaa')

print (f'{Buscar15}')

Buscar16 = re.fullmatch(r'hol[a]*', 'hol')

print (f'{Buscar16}')

Buscar17 = re.fullmatch(r'hol[a]+', 'hol')

print (f'{Buscar17}')

Buscar18 = re.fullmatch(r'hol[a]?', 'hol')

print (f'{Buscar18}')

Buscar19 = re.findall(r'[abl]{3}', 'hablablr')

print (f'{Buscar19}')

Texto4 = 'este es hola un texto ₡150 pero lo mas interesante! es hala que ₡66 colones no es lo mismo colonescolones que hela tener ₡0 en el bolsillo'

Buscar20 = re.findall(r'(colones){2,}', Texto4)

print (f'{Buscar20}')

import re

Ruta_Csv2 = 'C:\\python-data-analyzer\\data\\sales.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

Elemento1 = Cargar_Csv2.groupby('product')['quantity'].sum()
Elemento1_Mayor = Elemento1.idxmax()
Elemento1_Menor = Elemento1.idxmin()

Cantidad_Mayor = Elemento1.max()
Cantidad_Menor = Elemento1.min()

print (f'El producto que vendio mas fue {Elemento1_Mayor} y vendio {Cantidad_Mayor} productos')
print (f'El producto que vendio menos fue {Elemento1_Menor} y vendio {Cantidad_Menor} productos')

print (f'{Elemento1}')

import pandas as pd
from datetime import datetime

'''Fecha = input(f'Ingrese una fecha con formato YY-MM-DD: ')

try:
    Fech = datetime.strptime(Fecha, '%Y-%m-%d').date()
    Fech_Formateado = pd.to_datetime(Fech)
    Cargar_Csv2['date'] = pd.to_datetime(Cargar_Csv2['date'])
except ValueError:
    print (f'Error, formato incorrecto')
    exit()

Encontrado = Cargar_Csv2[Cargar_Csv2['date'].dt.date == Fech_Formateado.date()]

if (Encontrado.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    Elemento2 = Cargar_Csv2.groupby('product')['quantity'].sum()
    Elemento2_1 = Elemento2.max()
    Elemento2_1_1 = Elemento2.idxmax()
    print (f'GENIAL! El producto que vendio mas fue {Elemento2_1_1} con {Elemento2_1} unidades')

    Elemento2_2 = Elemento2.min()
    Elemento2_2_1 = Elemento2.idxmin()
    print (f'GENIAL! El producto que vendio menos fue {Elemento2_2_1} con {Elemento2_2} unidades')
    
'''

Cargar_Csv2['TOTALE'] = Cargar_Csv2['quantity'] * Cargar_Csv2['price']

print (f'{Cargar_Csv2}')

import Module_Own as PEPE

def Exception1(Numero):
    try:
        Numerito = int(Numero)
        print (f'Gracias, tu numero es {Numerito}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Exception1(9)

def Exception2(Num1, Num2):
    try:
        Resultado = Num2 + Num1
        print (f'El resutlado de la operacion es {Resultado}')
    except TypeError:
        print (f'Error, ambos elementos deben ser numeros')

Exception2(12, "hola")

def Exception3(Num1, Num2):
    try:
        Div = Num1 / Num2
        print (f'El resultado de la division es {round(Div, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(12, 0)

Lista_Exception4 = ['Erick', 'Josue', 'Karlita']

def Exception5(Indice):
    try:
        print (f'El elemento en la posicion {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, indice fuera de rango')

Exception5(2)

Diccionario_Exception5 = dict({'Nombre' : "Josue", 'Edad' : 20})

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception5('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Leon')
        Docu.close()

except FilenotFoundError:
    print (f'Error, el archivo no fue encontrado')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nNutria'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nElefante')
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
    'Edad' : [18 * 2, 20, 6],
    'Votante' : [True, not False, False]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [55, round(50/5), 26],
    'Votante' : [True, False, not False]
})

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame_Concatenate}')

print (f'----------')

print (f'{Data_Frame_Concatenate_Age}')

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()} y la mayor es {Data_Frame_Concatenate_Age.max()}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'----------')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombrecito = elemento['Nombre']

    print (f'Mi nombre es {Nombrecito}')

print (f'----------')

Elemento2 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Elemento2_Mayor = Elemento2.idxmax()
Elemento2_Menor = Elemento2.idxmin()
Elemento1_Mayor_Edad = Elemento2.max()
Elemento1_Menor_Edad = Elemento2.min()

print (f'{Elemento2}')

print (f'El mayor de la lista es {Elemento2_Mayor} y su edad es {Elemento1_Mayor_Edad}')
print (f'El menor de la lista es {Elemento2_Menor} y su edad es {Elemento1_Menor_Edad}')

'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()'''

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'-----------')

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'-----------')

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'-----------')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'Tenemos {Filas} Filas y {Columnas} Columnas')

Elemento3 = Data_Frame1.loc[0, 'Nombre']
Elemento4 = Data_Frame1.loc[1, 'Edad']
Elemento5 = Data_Frame1.loc[2, 'Votante']
Elemento6 = Data_Frame1.loc[1, :]
Elemento7 = Data_Frame1.loc[:, 'Nombre']

print (f'{Elemento3}')
print (f'{Elemento4}')
print (f'{Elemento5}')
print (f'{Elemento6}')
print (f'{Elemento7}')

Elemento8 = Data_Frame2.iloc[0, 0]
Elemento9 = Data_Frame2.iloc[1, 1]
Elemento10 = Data_Frame2.iloc[2, 2]
Elemento11 = Data_Frame2.iloc[0, :]
Elemento12 = Data_Frame2.iloc[:, 2]

print (f'{Elemento8}')
print (f'{Elemento9}')
print (f'{Elemento10}')
print (f'{Elemento11}')
print (f'{Elemento12}')

print (f'-----------')

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel)

print (f'{Cargar_Excel.head()}')

print (f'-----------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, names=['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, index_col='tiquete')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:J', index_col='cabina')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:J', index_col='cabina', nrows=1)

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

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='Cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'-----------')

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='Cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

Lista_DataFrame_Concatenate = list(Data_Frame_Concatenate['Nombre'])

print (f'{Lista_DataFrame_Concatenate}')

for elemento in enumerate(Lista_DataFrame_Concatenate):
    print (f'{elemento[0]} -- {elemento[1]}')

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'-----------')

print (f'{Cargar_Txt.head()}')

print (f'-----------')

import pandas as pd

Ruta_Csv3 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

print (f'-----------')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Leer_Html)

print (f'{Cargar_Html[2].head()}')

print (f'-----------')

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
print (f'{Array1[Array1 <= 1]}')

print (f'-----------')

Array2 = np.array([[4, 5, 6], [7, 8, 9]])

print (f'{Array2}')
print (f'{Array2.ndim}') #
print (f'{Array2.shape}') #
print (f'{Array2.size}') #
print (f'{Array2.dtype}') #
print (f'{Array2[1, 0]}')
print (f'{Array2[0, :2]}')
print (f'{Array2[0, 2:]}')
print (f'{Array2[1, ::2]}')
print (f'{Array2[0, ::3]}')
print (f'{Array2[1, 1:2]}')
print (f'{Array2[:, 1]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[0, :]}')
print (f'{Array2[Array2 <= 4]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumado: {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[0, 0:None])
Sumita4 = np.sum(Array2_Sorted[0, :])

print (f'Sumita: {Sumita1}')
print (f'Sumita: {Sumita2}')
print (f'Sumita: {Sumita3}')
print (f'Sumita: {Sumita4}')

print (f'-----------')

Array3 = np.array([[['e', 'j', 'k'], ['a', 'f', 'n']],       [['s', 'm', 'z'], ['r', 'i', 'o']]])

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
print (f'{Array3[1, 1, 1:2]}')
print (f'{Array3[1, :, 0]}')
print (f'{Array3[1, 0, 0:None]}')
print (f'{Array3[1, 0, :]}')
print (f'{Array3[Array3 == "a"]}')


print (f'-----------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 6, 2]]],          [[[3, 2, 1], [6, 5, 4]], [[9, 8, 7], [4, 3, 7]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') #
print (f'{Array4.shape}') #
print (f'{Array4.size}') #
print (f'{Array4.dtype}') #
print (f'{Array4[0, 1, 0, 2]}')
print (f'{Array4[1, 1, 0, :2]}')
print (f'{Array4[1, 1, 0, 2:]}')
print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[0, 0, 1, ::3]}')
print (f'{Array4[1, 1, 0, 1:2]}')
print (f'{Array4[0, 1, :, 1]}')
print (f'{Array4[1, 1, 1, 0:None]}')
print (f'{Array4[1, 1, 1, :]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[1, 1, 0, 0:None])
Sumita8 = np.sum(Array4_Sorted[1, 1, 0, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'-----------')

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_Max = np.max(Array_Num1)
Array_Min = np.min(Array_Num1)

print (f'El menor de los numeros es {Array_Min} y el mayor es {Array_Max}')

print (f'-----------')

Array_Num2 = np.arange(start=1, stop=26, step=1)

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

print (f'-----------')

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 0]}')

print (f'-----------')

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[1, 2]}')

print (f'-----------')

Array_Gen1 = np.full(shape=(2, 3), fill_value = PEPE.Diccionario_Poke['Poke1'])

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[0, 1]}')

print (f'-----------')

Array_Gen2 = np.full(shape=(5), fill_value='FUECOCO')

Lista_Array_Gen2 = list([])

for elemento in Array_Gen2:
    Lista_Array_Gen2.append(str(elemento))

print (f'{Lista_Array_Gen2}')
print (f'{type(Lista_Array_Gen2)}')

print (f'-----------')

Array_Gen3 = np.full(shape=(2, 3), fill_value=Array4[0, 1, 1, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 1]}')

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

print (f'-----------')

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')

print (f'-----------')

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

print (f'-----------')

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2,3,7])

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

print (f'-----------')

Array_Num8 = np.arange(start=1, stop=21, step=1)

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

Lista_Array = ['Erick', 'Josue', 'Karlita']

Array5 = np.array(Lista_Array)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-----------')

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concatenate([Array6, Array7])

print (f'{Array_Concatenate}')

Array_Concatenate_Split = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Split[0]}')
print (f'{Array_Concatenate_Split[1]}')
print (f'{Array_Concatenate_Split[2]}')

print (f'-----------')

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'-----------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'-----------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'-----------')

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-----------')

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Sumita9 = np.sum(Array_Random3, axis=0)
Sumita10 = np.sum(Array_Random3, axis=1)
Sumita11 = np.sum(Array_Random3[0, 1, 0:None])
Sumita12 = np.sum(Array_Random3[0, 1, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

print (f'-----------')

Lista_Array2 = ['Erick', 'Josue', 'Karlita', 'Carmelo', 'Susanita', 'Roxana']

Ganador1 = np.random.choice(Lista_Array2, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Array2, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Array2, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-----------')

Array_Linspace = np.linspace(start=0, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-----------')

def Generadora1():
    for elemento in range(5):
        yield f'{elemento}'

Gen1 = Generadora1()

try:
    print (f'El elemento es {next(Gen1)}')
    print (f'El elemento es {next(Gen1)}')
    print (f'El elemento es {next(Gen1)}')
    print (f'El elemento es {next(Gen1)}')
    print (f'El elemento es {next(Gen1)}')
    print (f'El elemento es {next(Gen1)}')
except StopIteration:
    print (f'Fin del experimento')

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
            yield f'Error'

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
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(44)}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.6, 20, not False)

print (f'{Funcion_Tupla("Perro", 3.6, 20, not False)}')
print (f'{Funcion_Tupla("Perro", 3.6, 20, not False)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.6, 20, not False))}')

print (f'-----------')

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')

Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])

print (f'-----------')

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7,8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')
print (f'Los numeros pares de la lista son {list(Anonima3)} o incluso podrian ser {PEPE.Lista_Par}')

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
    Lista_Closure = []
    def Closure_Interno(x):
        Lista_Closure.append(x)

        return Lista_Closure

    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(24)}')
print (f'{Variable_Closure(39)}')

def Crear_Multiplicador(x):
    def Multiplicador(y):
        return x * y

    return Multiplicador

Variable_Mult1 = Crear_Multiplicador(2)
Variable_Mult2 = Crear_Multiplicador(3)

print (f'El resultado de la multiplicacion es {Variable_Mult1(10)}')
print (f'El resultado de la multiplicacion es {Variable_Mult2(10)}')

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    if (Any_Impar == True):
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impares = [num for num in Lista if num % 2 != 0]

        print (f'Los elementos impares son {list(Anonima4)} y tambien {Lista_Impares}')
    else:
        print (f'No hay elementos impares')

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
def Sumatoria3(Num1, Num2):
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(4, 7)}')

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


# Crea una clase pokemon con tipo, nombre, ataque y una variable capturado en el  Modulo_Propio

# Usemos un unico elemento del modulo saludar con la instruccion "from Saludar import Diccionario_Poke", ya no se necesita usar Saludar

# Creemos una clase hija que herede todas las caracteristicas de la clase pokemon

# Ahora vamos a hacer un ejercicio de herencia multiple con 3 clases, una clase camara, otra reproductor musica y otra clase smartphone, smartphone hereda de las clases padre. Solamente tendra un metodo accion cada una



# Como declarar dos variables string?
# Como declarar una variable long string?
# Como declarar una variable integer?
# Como declarar una varible decimal
# Como declarar dos variables booleanas?
# Declare dos variables en la misma linea
# Agrega un comentario simple
# Agregue un comentario compuesto
# Imprime un texto con una variable string
# Imprime dos varibles string concatenadas
# Imprime una concatenacion de una varible texto y un integer
# borra una variable
# Juegue con los operadores de pertenencia in / not in
# Declare una variable con Snake Case

# ***********************  Listas   **********************

# Declara una lista con string

# Usemos un unico elemento del modulo saludar con la instruccion "from Saludar import Lista1" y cambiemosle el nombre con “as”, ya no se necesita usar Saludar

# Declara una lista con diferentes tipos de datos En  Modulo_Propio
# Declara una lista de solo numeros En  Modulo_Propio
# Cree una lista con la funcion list En  Modulo_Propio

# Ahora vamos a sacar del modulo propio varias listas al mismo tiempo 1 y 4 con la instruccion from Modulo_Propio import Lista1, Lista4

# Muestre en consola la cantidad de elementos en una de las listas con la funcion len
# Agrega un elemento aleatorio a la lista con .append()
# Inserta un elemento en una posición específica con .insert(posición, elemento)
# Agreguemos varios elementos a la lista con extend(['Cada elemento se ingresa asi'])
# Haz alguna operacion matematica con los valores de la lista 3
# Despliegue en consola el resultado
# Imprima un rango de elementos de la lista, por ejemplo del valor en la posicion 0 al 2 con [x:y]
# Concatene un elemento de la primer lista y de la segunda lista e imprima en consola
# Imprima todos los elemento de alguna de las tres listas
# Cambie el valor de un elemento de una lista
# Ahora muestre todos los elementos de la lista incluyendo el que cambio
# Borre un valor de una lista usando del
# Borra otro elemento usando .remove(elemento textual) y muestra la lista
# Borre 1 elemento de la lista utilizando el metodo pop('Indice')
# Borre 1 elemento de la lista utilizando el metodo pop('Indice negativo para borrar el ultimo elemento')
# Elimine todos los elementos de una lista con el metodo clear()
# Ordena la lista 3 numerica en orden ascendente con .sort()
# Ordena la lista 3 numerica orden descendente .sort(reverse=True)
# Invierte el orden de la lista con .reverse()

# User la funcion dunder "dir" sobre el Modulo_Propio para ver todas sus caracteristicas incluyendo todos los elementos que creamos a mano

# ********************************************************

# Cree una tupla
# Cree una tupla con la funcion tuple
# Cree una tupla sin parentesis
# Cree una tupla sin parentesis de un solo elemento
# En que se diferencia una lista de una tupla?
# Intente cambiar un elemento de la tupla para obtener un error
# Muestre en consola todos los elementos de la tupla
# Muestre con un print un elemento de la tupla

# Cree un set o conjunto
# Cree un set con la funcion set
# Cual es la diferencia entre una lista, una tupla y un set o conjunto?
# Muestre los elementos totales del conjunto
# Intente agregar un elemento al set con .add()
# Reconstruya el conjunto con nuevos elementos
# Intente agregar un elemento repetido del conjunto para obtener un error

# TEORIA DE CONJUNTOS, CONJUNTOS SETS SIMPLES Y FROZENSETS *****
# Creamos dos conjuntos, uno tiene 3 elementos que salen en un super conjunto mayor conjunto1, conjunto2
# Usemos el metodo .issubset() para saber si el conjunto 2 es un subconjunto de 1, osea que sus elementos salen en el conjunto mayor, devolvera True
# Usemos el metodo .issuperset() para saber si el conjunto 1 es un super conjunto de 2
# Ahora comparemos si en el conjunto 2 hay algun elemento que se repita en conjunto 1 con .isdisjoint()
# El restaurante tiene un menú fijo de jugos. Este menú nunca cambia, entonces hagamos un set con frozenset({}) de 3 sabores que no pueden cambiar
# Intentar agregar un nuevo sabor con el metodo .add() para obtener un error
# Ahora hacemos otro set_conjunto con 3 sabores, pero este es un set normal
# Intentar agregar un nuevo sabor con el metodo .add()

# Crea un diccionario
# Cree un Diccionario con la funcion dict
# Muestre cada una de las llaves de un diccionario con el metodo keys
# Imprima un Elemento del diccionario
# Despliegue otro elemento del diccionario con la funcion get()
# Imprima Todo el diccionario
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

# Hagamos un diccionario vacio con fromkeys, luego una lista de elementos y agregue los elementos de la lista al diccionario con un ciclo    i=0


# A partir de los elementos del csv file, vamos a crear primero una lista de llaves, luego vamos a tomar los nombres y agregarlos a una lista
# finalmente vamos a crear un diccionario y emparejar las llaves creadas y los nombres y mostramos el nuevo diccionario creado



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
# Ahora vamos a hacer un if con un and
# Ahora vamos a hacer un if con un or

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




# Validar si el correo electronico tiene el formato correcto por medio de expresiones regulares

'''

import re

email = 'example@example.com'

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.match(pattern, email)

if result:
	print (f'Valido')
else:
	print (f'Invalido')

'''

Expresiones regulares en Python
Excepciones
Importar modulos
Escribir en un txt file
DataFrames de Pandas
Graficos con Matplotlit
Trabarjar con archivos excel
Trabajar con archivos csv
Trabajar con informacion de una pagina web
Arreglos con numpy
Funciones Generadoras
Funciones
Funciones anidadas
Funciones Lambda
Decoradores de funciones
Funciones Type hint
Funciones Closure
Clases
Variables
Listas
Tuplas
Conjuntos
Diccionarios
Condicionales
Ciclo For
Ciclo While
Data inputs







Esto es un programa que solicita una fecha y la compara con una entrada de un documento csv. Si no la encuentra mostrara un mensaje de error, si el formato es incorrecto mostrara un mensaje de error, si la encuentra mostrara el mensaje que la fecha se encontro x numero de veces.

Importar pandas
from datetime import datetime
Crear la ruta del csv
Cargar el archivo csv
Pedir la fecha por medio de un input
hacer un try except valueerror
en el try primero vamos a asegurarnos co datetime.strptime que el formato es el correcto
en el try luego hay que asegurarnos que la fecha esta formateda to_datetime
en el try despues hay que asegurarse que la fecha del csv esta formateada to_datetime
si no, el excep muestra un error ojo necesita un exit()
Hacemos una variable encontrado, igualamos == entrada del csv .dt.date contra la fecha ingresada date()
if encontrado.empty
else
exito

'''

# Estudiemos clases y herencia

class Pokemon:
    def __init__(self, Nombre, Tipo, Ataque):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque
        self.Cantidad = 18 * 2
        self.Catched = not True

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')

class Poke2(Pokemon):
    def __init__(self, Nombre, Tipo, Ataque, City, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.City = City
        self.Sub_Tipo = Sub_Tipo

    def Desplegar(self):
        print (f'{self.Nombre} se encuentra en {self.City} y tiene tipos {self.Tipo} / {self.Sub_Tipo}')

Objeto1 = Poke2('Pikachu', 'Electrico', 'Impact Trueno', 'Kanto', 'Acero')

Objeto1.Mostrar()

print (f'-----------')

Objeto1.Desplegar()