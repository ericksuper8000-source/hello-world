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
print (f'-----------')
print (f'-----------')
print (f'-----------')
print (f'-----------')
print (f'-----------')
print (f'-----------')
print (f'-----------')


