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

from Module_Own import Pokemon as Poke
from Module_Own import Poke_Hija as Poke_Son

Objeto3 = Poke(PEPE.Diccionario_Poke["Poke1"], 'Electrico', 'Impact Trueno')
Objeto4 = Poke_Son(PEPE.Diccionario_Poke["Poke2"], 'Roca', 'Sismo', 'Acero')
Objeto5 = Poke(PEPE.Diccionario_Poke["Poke3"], 'Agua', 'Hidro-Chorro')

Objeto4.Mostrar()
Objeto4.Desplegar()

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un
Long
String'''

variable4 = Objeto3.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = not False, Objeto5.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[2]} tiene {Variable_Sumatoria} {Sumatoria2(1, 2, 3, 3, 4)} o incluso {Objeto3.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elemento')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

def Exception6(Num1, Num2):
    try:
        Cociente, Residuo = divmod(Num1, Num2)
        print (f'El cociente es {Cociente} y el residuo es {Residuo}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')
        exit()

Exception6(Objeto4.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'Un rango de elementos de la lista 2 seria {PEPE.Lista2[2:4]}')

print (f'{Lista_Uno[1]}, eso que esta ahi es un {PEPE.Lista2[2]}?')

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

print (f'------------')

print (f'{help(PEPE)}')

print (f'------------')

Tupla1 = ('Uno', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos')

print (f'{Tupla1}')

Tupla1 = tuple(('Uno', 'Dos', 'Tres'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')

Set_Conjunto1 = {'Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde'}
Set_Conjunto1.add('Azul')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Red', 'Green', 'Blue'})

print (f'{Set_Conjunto1}')

Set_Conjunto2 = {1, 2, 3, 4, 5}
Set_Conjunto3 = {4, 5}
Set_Conjunto4 = set({8})

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')
Set_Conjunto_Menu2 = frozenset({'Caramelo', 'Mora'})
Set_Conjunto_Menu3 = set({Objeto4.Tipo, Set_Conjunto_Menu2})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Variable_Sumatoria,
    'Votante' : True
}

Diccionario2 = {
    'Nombre' : ["Erick", Lista_Uno_Copia[1], "Karlita"],
    'Edad' : [18 * 2, 20, 6],
    'Votante' : [True, not False, False]
}

Diccionario3 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

print (f'------------')

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1["Nombre"]}')
print (f'{Diccionario1.get("Edad")}')

print (f'------------')

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2["Nombre"][0]}')
print (f'{Diccionario2.get("Edad")[1]}')

print (f'------------')

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3["Ingresos"]}')
print (f'{Diccionario3.get("Gastos")}')

print (f'------------')

Diccionario1["Nombre"] = Lista_Uno_Copia[0]

print (f'{Diccionario1}')

del Diccionario1["Nombre"]
Diccionario1.pop("Edad")

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')

Diccionario1 = dict({1 : "Karlita", 2 : 7, 3 : Variable_Funcion_Tupla[3]})

print (f'{Diccionario1}')

print (f'{Diccionario2["Nombre"][2]} no puede votar ya que solo tiene {Diccionario1.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', "Hola")
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = Objeto5.Ataque

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')

print (f'------------')

Lista_Dict3 = list(Cargar_Csv3['Nombre'])

print (f'{Lista_Dict3}')

Key3 = [f'Key{i}' for i in range(len(Lista_Dict3))]

print (f'{Key3}')

Diccionario000 = dict(zip(Key3, Lista_Dict3))

for elemento in Diccionario000.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'El tipo de valor de la variable es {type(variable1)}')
print (f'El tipo de valor de la variable es {type(variable4)}')
print (f'El tipo de valor de la variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de valor de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de valor de la variable es {type(Tupla1)}')
print (f'El tipo de valor de la variable es {type(Diccionario2)}')
print (f'El tipo de valor de la variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de valor de la variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de valor de la variable es {type(Funcion_Tupla())}')
print (f'El tipo de valor de la variable es {type(Array5)}')
print (f'El tipo de valor de la variable es {type(Data_Frame_Concatenate)}')
print (f'El tipo de valor de la variable es {type(PEPE)}')
print (f'El tipo de valor de la variable es {type(Objeto3)}')

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

if (variable1 == "Erick" and Objeto3.Cantidad > 50):
    print (f'AND COMPLETE')
else:
    print (f'AT LEAST ONE CONDITION IS NOT MET')

if (variable1 == "Carmelo" or Objeto3.Cantidad > 50):
    print (f'OR COMPLETE')
else:
    print (f'BOTH CONDITIONS ARE NOT MET')

print (f'{dir(variable1)}')

class Entrenador:
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Variable_Sumatoria
        self.Classified = not False

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')

Objeto6 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto3.Nombre)
Objeto7 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto4.Nombre)
Objeto8 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto5.Nombre)

Objeto7.Desplegar()

Negativo = -9

print (f'{int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]
Anonima5 = filter(lambda num :  num % 2 == 0, PEPE.Lista_Numeros)

print (f'{Any_Iterable}')
print (f'{Lista_Iterable}')
print (f'{list(Anonima5)}')

print (f'El binario de {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

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
letra_variable8 = variable8[0]

print (f'{variable8}')
print (f'{variable8.lower()}')
print (f'{variable8.upper()}')
print (f'{variable8.capitalize()}')

print (f'{variable8.lower().find("t")}')
print (f'{variable8.lower().index("b")}')

print (f'{variable8.lower().startswith(letra_variable8)}')
print (f'{variable8.lower().endswith("n")}')

print (f'La letra {letra_variable8} aparece un total de {variable8.lower().count(letra_variable8)}')

print (f'{variable8.lower().replace("ban", "POPOTAMO")}')

variable9 = 'esto es un texto cualquiera, lo que deseamos es ver si esta picha sirve'

variable9_Lista = variable9.split(' ')

for elemento in variable9_Lista:
    print (f'{elemento}')

print (f'La cantidad de palabras digitadas es {variable9_Lista.__len__()}')

print (f'{PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

for elemento in Diccionario1:
    print (f'{Diccionario1[elemento]}')

for elemento in Diccionario2.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'El numero es {PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1

Contador = 0

Lista_Animales = list([])
Lista_Animales.append('Cocodrilo')
Lista_Animales.insert(0, PEPE.Lista2[2])
Lista_Animales.extend(['Avestruz', 'Gato'])

print (f'{Lista_Animales}')

print (f'------------')

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Avestruz'):
        print (f'Parajote este {Contador}')
        break
    else:
        Contador+= 1
        continue

for elemento1, elemento2 in zip(Lista_Animales, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')

for elemento in range(5):
    print (f'{elemento}')

for elemento in range(995, 1000):
    print (f'{elemento}')

Lista_Numeros_Mult = [num  * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1


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