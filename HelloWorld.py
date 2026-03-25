import statistics

import django.core.checks
import pandas as pd
from datetime import datetime

Ruta_Csv1 = 'C:\\python-data-analyzer\\data\\sales.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')
'''
while True:
    Fecha = input(f'Ingrese una fecha con formato YY-MM-DD: ')

    try:
        Fech = datetime.strptime(Fecha, '%Y-%m-%d').date()
        Fech_Formateada = pd.to_datetime(Fech)
        Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
        break
    except ValueError:
        print(f'Error, formato incorrecto')

Comparado = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech_Formateada.date()]

if (Comparado.empty):
    print (f'No hay ventas en esta fecha')
else:
    Buscar1 = Comparado.groupby('date')['quantity'].sum()
    Buscar1_Max = Buscar1.idxmax()
    Buscar1_Min = Buscar1.idxmin()
    Buscar1_Max_Cant = Buscar1.max()
    Buscar1_Min_Cant = Buscar1.min()

    print (f'En la fecha {Buscar1_Max} se vendieron un total de {Buscar1_Max_Cant} unidades')'''

try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el import no fue encontrado')

from Module_Own import Pokemon as Poke

print (f'--------------')

class Hija_Poke(Poke):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto1 = Poke(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto2 = Hija_Poke(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Acero')
Objeto3 = Poke(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro')

Poke.Mostrar(Objeto2)
Objeto2.Mostrar()

print (f'--------------')

class Camara():
    def Tomar_Fotografia(self):
        print (f'Fotografia Tomada')

class Reproductor_Musica:
    def Reproducir_Musica(self):
        print (f'Musica Reproducida')

class Smartphone(Camara, Reproductor_Musica):
    def Encender_Smartphone(self):
        print (f'Smartphone Encendido')

Objeto4 = Smartphone()

Objeto4.Encender_Smartphone()
Objeto4.Reproducir_Musica()
Objeto4.Tomar_Fotografia()

print (f'--------------')

class Atacante():
    def __init__(self, Damage, Weapon, Attack_Position):
        self.Damage = Damage
        self.Weapon = Weapon
        self.Attack_Position = Attack_Position

    def Mostrar(self):
        print (f'Damage: {self.Damage}')
        print (f'Weapon: {self.Weapon}')
        print (f'Attack_Position: {self.Attack_Position}')

class Curador:
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life

    def Mostrar(self):
        print (f'Healing: {self.Healing}')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}')

class Paladin(Atacante, Curador):
    def __init__(self, Damage, Weapon, Attack_Position, Healing, Potion, Life, Name):
        Atacante.__init__(self, Damage, Weapon, Attack_Position)
        Curador.__init__(self, Healing, Potion, Life)
        self.Name = Name

    def Mostrar(self):
        print (f'Name: {self.Name}')

Objeto5 = Paladin(75, 'Battle Axe', 'Right', 90, 'Purple Potion', 200, 'Ghost Knight')

Objeto5.Mostrar()
Atacante.Mostrar(Objeto5)
Curador.Mostrar(Objeto5)

print (f'--------------')

class Mascota():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad} años')
        print (f'Peso: {self.Peso}kgs')

class Perro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento, N_Visitas):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        self.N_Visitas = N_Visitas

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        print (f'N_Visitas: {self.N_Visitas}')

Objeto6 = Perro('Chester', 3, 3.2, 'Poodle', 'Hipertension', 3)

Mascota.Mostrar(Objeto6)
Objeto6.Mostrar()

print (f'--------------')

class Gato(Mascota):
    def __init__(self, Nombre, Edad, Peso, Raza, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')

Objeto7 = Gato('Messi', 1.5, 1.9, 'Siames', 'Gris', 'No')

Mascota.Mostrar(Objeto7)
Objeto7.Mostrar()

print (f'--------------')

class Pajaro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto8 = Pajaro('Polly', 31, 0.4, 'Cacatua Amarilla', 'Si')

Mascota.Mostrar(Objeto8)
Objeto8.Mostrar()

print (f'--------------')

class A():
    def Mostrar(self):
        print (f'Hola A')

class E():
    def Mostrar(self):
        print (f'Hola E')

class B(E):
    def Mostrar(self):
        print (f'Hola B')

class C(A):
    def Mostrar(self):
        print (f'Hola C')

class D(B,C):
    def Mostrar(self):
        print (f'Hola D')

Objeto9 = D()

A.Mostrar(Objeto9)
B.Mostrar(Objeto9)
C.Mostrar(Objeto9)
Objeto9.Mostrar()
E.Mostrar(Objeto9)

print (f'--------------')

Lista_Dict = ['Erick', 'Josue', 'Perez', 'Gutierrez']
Key1 = [f'Key{i}' for i in range(Lista_Dict.__len__())]

print (f'{Key1}')

Diccionario1 = dict(zip(Key1, Lista_Dict))

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1["Key0"]}')
print (f'{Diccionario1.get("Key1")}')

print (f'--------------')

Lista_Dict2 = set(Cargar_Csv1['product'])

print (f'{Lista_Dict2}')

Key2 = [f'Key_{i}' for i in range(len(Lista_Dict2))]

print (f'{Key2}')

Diccionario2 = dict(zip(Key2, Lista_Dict2))

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2["Key_1"]}')
print (f'{Diccionario2.get("Key_2")}')

print (f'--------------')

import re

Texto1 = 'este es hola un texto ₡150 pero lo mas interesante! es hala que ₡66 colones no es lo mismo'

Buscar1 = re.findall(r'₡(\d+)', Texto1)
Lista_Buscar1 = list([])

print (f'{Buscar1}')

for elemento in Buscar1:
    Lista_Buscar1.append(int(elemento))

print (f'{Lista_Buscar1}')

Telefono1 = '8888-8888'

Pattern1 = r'[0-9]{4}\-\d{4}'

Buscar2 = bool(re.match(Pattern1, Telefono1))

if (Buscar2 == True):
    print (f'Formato de telefono correcto')
else:
    print (f'Error, el formato del telefono es incorrecto')

Texto2 = 'Tu tarjeta caduca en 03/10/2026, es necesario que visites una sucursal antes de esta fecha'

Pattern2 = r'\d{2}\/[0-9]{2}\/[0-9]{4}'

Replacement = 'XX/XX/XXXX'

New_Texto2 = re.sub(Pattern2, Replacement, Texto2)

print (f'{Texto2}')
print (f'{New_Texto2}')

Email1 = 'sample@sample.com'

Pattern3 = r'^[a-zA-Z0-9/*-+.?_-]+\@[a-zA-Z]+\.[a-z]{2,}$'

Buscar3 = bool(re.match(Pattern3, Email1))

if (Buscar3 == True):
    print (f'Formato de correo electronico correcto')
else:
    print (f'Error, formato de correo incorrecto')

Texto3 = '66 10'

Buscar4 = re.findall(r'^[0-9]{1,2}\s?\d{2,}$', Texto3)

print (f'{Buscar4}')

Texto4 = 'Hola 66'

Buscar5 = re.findall(r'[a-z]*|\d{3}$', Texto4)

print (f'{Buscar5}')

Grupo1 = Cargar_Csv1.groupby('product')['quantity'].mean()
Grupo1_Mayor = Grupo1.idxmax()
Grupo1_Mayor_Prom = Grupo1.max()

print (f'{Grupo1_Mayor}')
print (f'{Grupo1_Mayor_Prom}')

print (f'--------------')

print (f'{Cargar_Csv1}')

print (f'--------------')

Grupo2 = Cargar_Csv1.groupby('product')['quantity'].sum()
Grupo3 = Cargar_Csv1.groupby('product')['quantity'].count()

print (f'{Grupo2}')
print (f'--------------')
print (f'{Grupo3}')

print (f'--------------')

Texto5 = 'esto es hola un ! texto 15 cualquiera para practicar 66 hela mis habilidades con @ expresiones hala 81 regulares'

Buscar6 = re.search(r'(ara)+', Texto5)

print (f'{Buscar6}')

Buscar7 = re.findall(r'l', Texto5)

print (f'{Buscar7}')

Buscar8 = re.fullmatch(r'8888-8888', Telefono1)

print (f'{Buscar8}')

Buscar9 = re.findall(r'h.la', Texto5)

print (f'{Buscar9}')

Buscar10 = re.findall(r'^esto', Texto5)
Buscar11 = re.findall(r'es$', Texto5)

print (f'{Buscar10}')
print (f'{Buscar11}')

def Exception1(Numero):
    try:
        Numerito = int(Numero)
        print (f'Gracias, el numero ingresado es {Numerito}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Exception1("hola")

def Exception2(Num1, Num2):
    try:
        Sumatoria = Num1 + Num2
        print (f'El resultado de la sumatoria es {Sumatoria}')
    except TypeError:
        print (f'Error, ambos elementos deben ser numeros')

Exception2(12, "hola")

def Exception3(Num1, Num2):
    try:
        Div = Num1 / Num2
        print (f'El resultado de la division es {round(Div, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser un cero')

Exception3(12, 0)

Lista_Exception4 = list(['Erick', 'Josue', 'Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento en el indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El elemento con la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception5('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Hiena')
        Docu.close()
except FileNotFoundError:
    print (f'El archivo seleccionado no existe')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nLeon'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSalamandra')
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

print(f'--------------')

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

print(f'--------------')

print (f'{Data_Frame_Concatenate_Age}')

print(f'--------------')

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()} y la mayor de las edades es {Data_Frame_Concatenate_Age.max()}')

Edades = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Edad_Mayor = Edades.idxmax()
Edad_Menor = Edades.idxmin()
Edad_Mayor_Num = Edades.max()
Edad_Menor_Num = Edades.min()

print (f'Del dataframe la persona con la mayor edad es {Edad_Mayor}: {Edad_Mayor_Num}')
print (f'Del dataframe la persona con la menor edad es {Edad_Menor}: {Edad_Menor_Num}')

print(f'--------------')

print (f'{Data_Frame_Concatenate.info()}')

print(f'--------------')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombrecito = elemento['Nombre']

    print (f'Mi nombre es {Nombrecito}')

print(f'--------------')
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print(f'--------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print(f'--------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()'''

print (f'{Data_Frame_Concatenate.head(3)}')

print(f'--------------')

print (f'{Data_Frame_Concatenate.head(1)}')

print(f'--------------')

print (f'{Data_Frame_Concatenate.tail(1)}')

print(f'--------------')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'Filas: {Filas}')
print (f'Columnas: {Columnas}')

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

print(f'--------------')

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

print(f'--------------')

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel)

print (f'{Cargar_Excel.head()}')

print(f'--------------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, index_col="tarifa")
Cargar_Excel5 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols="E:J", index_col="cabina")
Cargar_Excel6 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols="E:J", index_col="cabina", nrows=1)

print (f'{Cargar_Excel1.head()}')

print(f'--------------')

print (f'{Cargar_Excel2.head()}')

print(f'--------------')

print (f'{Cargar_Excel3.head()}')

print(f'--------------')

print (f'{Cargar_Excel4.head()}')

print(f'--------------')

print (f'{Cargar_Excel5.head()}')

print(f'--------------')

print (f'{Cargar_Excel6.head()}')

print(f'--------------')

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print(f'--------------')

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

print(f'--------------')

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt.head()}')

print(f'--------------')

print (f'{Cargar_Txt}')

print(f'--------------')

Ruta_Csv2 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2.head()}')

print(f'--------------')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Leer_Html)

print (f'{Cargar_Html[2].head()}')

print(f'--------------')

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

print(f'--------------')

Array2 = np.array([[5, 8, 0], [3, 2, 1]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[0, 1]}')

print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[0, 1:2]}')
print (f'{Array2[:, 1]}')
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

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

print (f'El resultado de la sumatoria es {Sumita1}')
print (f'El resultado de la sumatoria es {Sumita2}')
print (f'El resultado de la sumatoria es {Sumita3}')
print (f'El resultado de la sumatoria es {Sumita4}')

print(f'--------------')

Array3 = np.array([[['a', 'e', 'p'], ['f', 'x', 's']],       [['o', 'k', 'n'], ['m', 'y', 'w']]])

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
print (f'{Array3[1, :, 0]}')
print (f'{Array3[0, 0, 0:None]}')
print (f'{Array3[0, 0, :]}')
print (f'{Array3[Array3 == "e"]}')

print(f'--------------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],      [[[6, 5, 4], [9, 8, 7]], [[4, 9, 0], [2, 5, 8]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 0]}')

print (f'{Array4[1, 1, 0, :2]}')
print (f'{Array4[1, 1, 0, 2:]}')
print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[0, 1, 1, ::3]}')
print (f'{Array4[1, 0, 1, 1:2]}')
print (f'{Array4[1, 0, :, 0]}')
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
Sumita7 = np.sum(Array4_Sorted[0, 1, 1, 0:None])
Sumita8 = np.sum(Array4_Sorted[0, 1, 1, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print(f'--------------')

Array_Num1 = np.arange(start=1, stop=11, step=1)
Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El numero menor es {Array_Num1_Min} y el mayor es {Array_Num1_Max}')

print (f'{Array_Num1}')

Array_Num2 = np.arange(25)

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

Array_Num2_Reshape_Column_Max = np.max(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Column_Min = np.min(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Row_Max = np.max(Array_Num2_Reshape, axis=1)
Array_Num2_Reshape_Row_Min = np.min(Array_Num2_Reshape, axis=1)

print (f'Los menores de las columnas son {Array_Num2_Reshape_Column_Min}')
print (f'Los mayores de las columnas son {Array_Num2_Reshape_Column_Max}')
print (f'Los menores de las filas son {Array_Num2_Reshape_Row_Min}')
print (f'Los mayores de las filas son {Array_Num2_Reshape_Row_Max}')

print(f'--------------')

Array_Zero = np.zeros(shape=(2, 3))

print (f'{Array_Zero}')
print (f'{Array_Zero.ndim}')
print (f'{Array_Zero.shape}')
print (f'{Array_Zero.size}')
print (f'{Array_Zero.dtype}')
print (f'{Array_Zero[1, 1]}')

print(f'--------------')

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 0]}')

print(f'--------------')

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 2]}')

print(f'--------------')

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

print (f'{Array_Gen2}')

Lista_Gen2 = []

for elemento in enumerate(Array_Gen2):
    Lista_Gen2.append(str(elemento[1]))

print (f'{Lista_Gen2}')
print (f'{type(Lista_Gen2)}')

print(f'--------------')

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[1, 0, 0, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[0, 1]}')

print(f'--------------')

Tupla_Array = ('Rojo', 'Verde')
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3,2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2,1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4,1), fill_value=Diccionario_Array['Nombre'][1])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print(f'--------------')

print (f'{Array_Gen6[2]}')

print(f'--------------')

Array_Num3 = np.arange(start=1, stop=6, step=1)
Array_Num4 = np.arange(start=2, stop=21, step=2)
Array_Num5 = np.arange(start=3, stop=31, step=3)
Array_Num6 = np.arange(start=1, stop=6, step=2)
Array_Num7 = np.arange(10)

print (f'{Array_Num3}')
print (f'{Array_Num4}')
print (f'{Array_Num5}')
print (f'{Array_Num6}')
print (f'{Array_Num7}')

print(f'--------------')

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')

print(f'--------------')

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

print(f'--------------')

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

print(f'--------------')

Array_Num8 = np.arange(start=1, stop=21, step=1)

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print(f'--------------')

Lista_Array = ['Erick', 'Josue', 'Karlita']

Array5 = np.array(Lista_Array)

print (f'{Array5}')
print (f'{type(Array5)}')

print(f'--------------')

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concatenate([Array6, Array7])

print (f'{Array_Concatenate}')

Array_Concatenate_Split = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Split[0]}')
print (f'{Array_Concatenate_Split[1]}')
print (f'{Array_Concatenate_Split[2]}')

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print(f'--------------')

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print(f'--------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print(f'--------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print(f'--------------')

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Sumita9 = np.sum(Array_Random3, axis=0)
Sumita10 = np.sum(Array_Random3, axis=1)
Sumita11 = np.sum(Array_Random3[1, 0, 0:None])
Sumita12 = np.sum(Array_Random3[1, 0, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

print(f'--------------')

Lista_Array2 = list(['Erick', 'Josue', 'Karlita', 'Carmelo', 'Susanita', 'Roxana'])

Ganador1 = np.random.choice(Lista_Array2, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Array2, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Array2, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print(f'--------------')

Array_LinSpace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_LinSpace}')

print(f'--------------')

def Generadora1():
    for elemento in range(5):
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

print(f'--------------')

def Generadora2():
    for elemento in range(0, 5):
        if (elemento % 2 == 0):
            yield f'El numero es par'
        else:
            yield f'El numero es impar'

Gen2 = Generadora2()

try:
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
except StopIteration:
    print (f'Fin del experimento')

print(f'--------------')

def Generadora3():
    for elemento in range(0, 5):
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
            yield f'ERROR DE CODIGO'

Gen3 = Generadora3()

try:
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
except StopIteration:
    print (f'Fin del experimento')

print(f'--------------')

class Una:
    def Mostrar(self):
        print (f'Hola Clase')

class Dos():
    def __init__(self):
        self.Mensaje = Una()

    def Finale(self):
        self.Mensaje.Mostrar()

Objeto10 = Dos()

Objeto10.Finale()

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

    return Usuario_Interno('FEMENINO')

Variable_Usuario = Usuario_Externo()

if (Variable_Usuario == True):
    print (f'YOU ARE A MAN')
else:
    print (f'YOU ARE A WOMAN')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(123)}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

print(f'--------------')

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.6, 200, not False)

print (f'{Funcion_Tupla("Perro", 3.6, 200, not False)}')
print (f'{Funcion_Tupla("Perro", 3.6, 200, not False)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.6, 200, not False))}')

print(f'--------------')

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')

Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])

print(f'--------------')

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

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
def Operacion(Numero):
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
print (f'{Variable_Closure(25)}')
print (f'{Variable_Closure(37)}')

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
        Lista_Impar = [num for num in Lista if num % 2 != 0]

        print (f'Los numeros impares de la lista son {list(Anonima4)} o incluso podrian ser {Lista_Impar}')
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
        return Segunda(*args, **kwargs) - 10

    return Tercera

@Primera
def Sumatoria3(Num1, Num2):
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(4, 7)}')

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

print (f'--------------------')

class Pokemon():
    def __init__(self, Nombre, Tipo, Ataque):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque
        self.Cantidad = Objeto1.Cantidad
        self.Catched = not True

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')

class HijaPoke2(Pokemon):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto11 = HijaPoke2('Snorlax', 'Normal', 'Mega Puño', 'Hada')

Pokemon.Mostrar(Objeto11)
Objeto11.Mostrar()

print (f'--------------------')

class Dancer():
    def Bailar(self):
        print (f'The dancer dances')

class Writer:
    def Escribir(self):
        print (f'The writer writes')

class Speaker(Dancer, Writer):
    def Hablar(self):
        print (f'The Speaker speaks')

Objeto12 = Speaker()

Objeto12.Hablar()
Objeto12.Escribir()
Objeto12.Bailar()

print (f'--------------------')

class Pet():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def Mostrar(self):
        print (f'nombre: {self.nombre}')
        print (f'edad: {self.edad} años')
        print (f'peso: {self.peso}kgs')

class dog(Pet):
    def __init__(self, nombre, edad, peso, Raza, Padecimiento, N_Visitas):
        super().__init__(nombre, edad, peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        self.N_Visitas = N_Visitas

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        print (f'N_Visitas: {self.N_Visitas}')

Objeto13 = dog('Chester', 3, 2.8, 'Poodle', 'Hipertension', 4)

Pet.Mostrar(Objeto13)
Objeto13.Mostrar()

print (f'--------------------')

class cat(Pet):
    def __init__(self, nombre, edad, peso, Raza, Color, Paciente_Activo):
        super().__init__(nombre, edad, peso)
        self.Raza = Raza
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')

Objeto14 = cat('Messi', 1.5, 1.2, 'Siames', 'Gris', 'No')

Pet.Mostrar(Objeto14)
Objeto14.Mostrar()

print (f'--------------------')

class bird(Pet):
    def __init__(self, nombre, edad, peso, Especie, Habla):
        super().__init__(nombre, edad, peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto15 = bird('Polly', 32, 0.4, 'Cacatua Amarilla', 'Si')

Pet.Mostrar(Objeto15)
Objeto15.Mostrar()

print (f'--------------------')

class Atacante():
    def __init__(self, Dano, Arma, Posicion):
        self.Dano = Dano
        self.Arma = Arma
        self.Posicion = Posicion

    def Mostrar(self):
        print (f'Daño: {self.Dano}pts')
        print (f'Arma: {self.Arma}')
        print (f'Posicion: {self.Posicion}')

class Defensor:
    def __init__(self, Curacion, Pocima, Vida):
        self.Curacion = Curacion
        self.Pocima = Pocima
        self.Vida = Vida

    def Mostrar(self):
        print (f'Curacion: {self.Curacion}pts')
        print (f'Pocima: {self.Pocima}')
        print (f'Vida: {self.Vida}pts')

class Personaje(Atacante, Defensor):
    def __init__(self, Dano, Arma, Posicion, Curacion, Pocima, Vida, Nombre):
        Atacante.__init__(self, Dano, Arma, Posicion)
        Defensor.__init__(self, Curacion, Pocima, Vida)
        self.Nombre = Nombre

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')

Objeto16 = Personaje(75, 'Espada De Fuego', 'Centro', 50, 'Pocion De Escudo', 200, 'Ladron De Mentes')

Objeto16.Mostrar()
Atacante.Mostrar(Objeto16)
Defensor.Mostrar(Objeto16)

print (f'--------------------')

Hereda_Padre = issubclass(HijaPoke2, Pokemon)

print (f'{Hereda_Padre}')

Objeto_Clase2 = isinstance(Objeto16, Atacante)

print (f'{Objeto_Clase2}')

print (f'--------------------')

class Efectivo():
    def Pagar(self):
        print (f'Pago realizado en efectivo')

class Tarjeta():
    def Pagar(self):
        print (f'Pago realizado en tarjeta')

class Cripto():
    def Pagar(self):
        print (f'Pago realizado en cripto')

Objeto18 = Cripto()
Objeto19 = Tarjeta()
Objeto20 = Efectivo()

Objeto18.Pagar()
Objeto19.Pagar()
Objeto20.Pagar()

print (f'--------------------')

class Cuenta_Bancaria:
    def __init__(self, Saldo):
        self.__Saldo = Saldo

    def Depositar(self, Dinero):
        self.__Saldo += Dinero

    def Mostrar(self):
        print (f'Gracias! Su saldo actual es de ${self.__Saldo}')

    @property
    def Dinero(self):
        return self.__Saldo

    @Dinero.setter
    def Dinero(self, New_Saldo):
        self.__Saldo = New_Saldo

Objeto21 = Cuenta_Bancaria(100)
Objeto21.Depositar(25)
Objeto21.Mostrar()

print (f'La variable privada es {Objeto21.Dinero}')

Objeto21.Dinero = '20,000'

Objeto21.Mostrar()

print (f'--------------------')

from abc import ABC, abstractclassmethod

class Plantilla(ABC):
    @abstractclassmethod

    def Escribir(self):
        pass

class Escritor(Plantilla):
    def Escribir(self):
        print (f'Estoy escribiendo')

Objeto22 = Escritor()

Objeto22.Escribir()

print (f'--------------------')

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''
Esto
Es
Un
Long
String'''
variable4 = Objeto1.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = not False, Objeto3.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke2"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[2]} tiene {Variable_Sumatoria}, {Sumatoria2(1, 2, 3, 4, 5)} o incluso {Objeto3.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es una declaracion de variables con empaquetado de variables y snake case {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto3.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Un rango de elementos de la lista 2 seria {PEPE.Lista2[2:4]}')

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

Tupla1 = ('Rojo', 'Verde', 'Verde', 'Verde', 'Verde')

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Green', 'Blue'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')

Set_Conjunto1 = {'Roca', Objeto2.Tipo, Objeto2.Tipo, Objeto2.Tipo, Objeto2.Tipo, Objeto2.Tipo}
Set_Conjunto1.add(Objeto1.Tipo)

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Rock', 'Electricity'})

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
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, Objeto3.Nombre})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Diccionario3 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Objeto3.Cantidad,
    'Votante' : variable6
}

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3["Nombre"]}')
print (f'{Diccionario3.get("Edad")}')

Diccionario4 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
}

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4["Nombre"][1]}')
print (f'{Diccionario4.get("Edad")[2]}')

Diccionario5 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5["Ingresos"]}')
print (f'{Diccionario5.get("Gastos")}')

Diccionario3['Nombre'] = variable1

print (f'{Diccionario3}')

del Diccionario3['Nombre']
Diccionario3.pop('Edad')

print (f'{Diccionario3}')

Diccionario3.clear()

print (f'{Diccionario3}')

Diccionario3 = dict({1 : "Karlita", 2 : Sumatoria2(1, 2, 3), 3 : not True})

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3[1]}')
print (f'{Diccionario3.get(2)}')

print (f'{Diccionario4["Nombre"][2]} no puede votar ya que solo tiene {Diccionario3.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'HolaMundo')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = PEPE.Diccionario_Poke["Poke3"]

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')

variable8 = 'este es un texto cualquiera para ver si la mica sirve pero lo mas importante es intentarlo'

Lista_variable8 = variable8.split(' ')

Key3 = [f'Key{i}' for i in range(len(Lista_variable8))]

print (f'{Key3}')

Diccionario6 = dict(zip(Key3, Lista_variable8))

for elemento in Diccionario6.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Lista_Dict4 = set(Cargar_Csv1['product'])

Key4 = [f'Llave({i})' for i in range(len(Lista_Dict4))]

print (f'{Key4}')

print (f'{Lista_Dict4}')

Diccionario7 = dict(zip(Key4, Lista_Dict4))

print (f'{Diccionario7}')
print (f'{Diccionario7.keys()}')
print (f'{Diccionario7["Llave(1)"]}')
print (f'{Diccionario7.get("Llave(3)")}')

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
print (f'{type(Objeto2.Catched)}')
print (f'{type(Lista_Uno_Copia)}')
print (f'{type(Tupla1)}')
print (f'{type(Set_Conjunto_Menu1)}')
print (f'{type(Set_Conjunto_Menu2)}')
print (f'{type(Diccionario6)}')
print (f'{type(Funcion_Diccionario)}')
print (f'{type(Atacante)}')
print (f'{type(Objeto2)}')
print (f'{type(Array5)}')
print (f'{type(Data_Frame_Concatenate)}')
print (f'{type(PEPE)}')

if (Diccionario5['Ingresos'] > 500):
    if (Diccionario5['Gastos'] < 200):
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario5['Gastos'] == 200):
        print (f'Ingresos Altos, Gastos Al Limite')
    elif (Diccionario5['Gastos'] > 200):
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario5['Ingresos'] == 500):
    if (Diccionario5['Gastos'] < 200):
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario5['Gastos'] == 200):
        print (f'Ingresos Minimos, Gastos Al Limite')
    elif (Diccionario5['Gastos'] > 200):
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario5['Ingresos'] < 500):
    if (Diccionario5['Gastos'] < 200):
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario5['Gastos'] == 200):
        print (f'Ingresos Bajos, Gastos Al Limite')
    elif (Diccionario5['Gastos'] > 200):
        print (f'Ingresos Bajos, Gastos Altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')

if (variable1 == 'Erick' and variable4 < 20):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una condicion no se cumple')

if (variable1 == 'Josue' or variable4 < 20):
    print (f'Al menos una condicion se cumple')
else:
    print (f'Ninguna de las condiciones se cumple')

print (f'{variable1.__dir__()}')

print (f'{help(PEPE)}')

class Trainer():
    def __init__(self, Nombre, Ciudad, Favorito):
        self.Nombre = Nombre
        self.Ciudad = Ciudad
        self.Favorito = Favorito
        self.Pokedex = Sumatoria2(1, 2, 3, 4, 5)
        self.Clasificado = True

    def Desplegar(self):
        print (f'{self.Nombre} just catched a {self.Favorito} while visiting {self.Ciudad}')

Objeto23 = Trainer(PEPE.Tupla_Poke[0], 'Kanto', Objeto1.Nombre)
Objeto24 = Trainer(PEPE.Tupla_Poke[1], 'Alolah', Objeto2.Nombre)
Objeto25 = Trainer(PEPE.Tupla_Poke[2], 'Paldea', Objeto3.Nombre)

Objeto24.Desplegar()

Negativo = -5

print (f'{int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima5 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable}')
print (f'{Lista_Iterable}')
print (f'{list(Anonima5)}')

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario5['Vacio']) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, ingrese una cadena de texto')

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'El elemento en la posicion {indice} es {elemento}')

variable9 = 'eSteBAN'
letra9 = variable9[0]

print (f'{variable9}')
print (f'{variable9.lower()}')
print (f'{variable9.upper()}')
print (f'{variable9.capitalize()}')

print (f'{variable9.lower().find("b")}')
print (f'{variable9.lower().index("t")}')

print (f'{variable9.lower().startswith(letra9)}')
print (f'{variable9.lower().endswith("n")}')

print (f'La letra {letra9} aparece un total de {variable9.lower().count(letra9)} veces')

print (f'{variable9.lower().replace("ban", "POPOTAMO")}')

print (f'El elemento {PEPE.Tupla_Poke[2]} aparece en la posicion {PEPE.Tupla_Poke.index("Misty")}')

for elemento in Diccionario3:
    print (f'{Diccionario3[elemento]}')

for elemento in Diccionario4.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1

ListA_Animales = ['Avestruz']
ListA_Animales.append('Gorila')
ListA_Animales.insert(1, 'Leopardo')
ListA_Animales.extend(['Tortuga'])

print (f'{ListA_Animales}')

Contador = 0

while (Contador < len(ListA_Animales)):
    if (ListA_Animales[Contador] == 'Gorila'):
        print (f'Este primate es poderoso')
        break
    else:
        Contador+= 1
        continue

for elemento1, elemento2 in zip(Lista_Uno_Copia, Set_Conjunto_Menu1):
    print (f'{elemento2} -- {elemento1}')

for elemento in range(5):
    print (f'{elemento}')

for elemento in range(995, 1000):
    print (f'{elemento}')

Lista_Numeros_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Mayor = max(Lista_Numeros_Mult)
Menor = min(Lista_Numeros_Mult)
Redondeo = round(14.458795, 2)
Sumatoria4 = sum(Lista_Numeros_Mult)

print (f'{bool(False)}')
print (f'{bool(not True)}')
print (f'{bool(0)}')
print (f'{bool(None)}')
print (f'{bool("")}')

Todo_All = all([Lista_Numeros_Mult, Tupla1, Set_Conjunto_Menu1, ""])

print (f'{Todo_All}')

print (f'Numero Mayor {Mayor}')
print (f'Numero Menor {Menor}')
print (f'Redondeo: {Redondeo}')
print (f'El resultado de la sumatoria es {Sumatoria4}')

Uno = int("500")
Dos = str(500)
Tres = float(Dos)

print (f'{Uno} - {type(Uno)}')
print (f'{Dos} - {type(Dos)}')
print (f'{Tres} - {type(Tres)}')

print (f' - '.join(Set_Conjunto_Menu1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

variable_PEPE3 = PEPE3
'''
def Ejemplo1(Numero:int) -> int:
    return Variable_Sumatoria * Sumatoria2(1, 2, 3, 4) * Numero

print (f'El resultado de la operacion es {Ejemplo1(PEPE.Flotante1)}')

try:
    Resultado = eval(PEPE.Flotante2)
    print (f'El resultado de la operacion es {Resultado}')
except TypeError:
    print (f'Error, ambos elementos deben ser numeros')

def Ejemplo3(Cadena):
    Lista_Cadena = Cadena.split(' ')

    for elemento in Lista_Cadena:
        print (f'{elemento}')

    print (f'La cantidad de palabras digitadas es {Lista_Cadena.__len__()}')

Ejemplo3(PEPE.Flotante3)

Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumnos = input(f'Ingrese el nombre del estudiante {elemento}: ')
        Lista.append(Alumnos)

    return Lista

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nLa lista de estudiantes es {Colegio(Lista_Alumnos)}')
    Docu.close()

with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

Lista_Alumnos2 = list([])

Contador = int(input(f'Ingrese el numero de estudiantes: '))

def Colegio2(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]

        Lista.append(Estudiante)

    Lista.sort(key=lambda Num :  Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]

    print (f'El menor de los estudiantes es {Menore} y el mayor es {Mayore}')

Colegio2(Lista_Alumnos2)

def Ejemplo_Finale():
    while True:
        Num = input(f'Ingrese un numero entero: ')
        try:
            Numerito = int(Num)
            break
        except:
            print (f'Error, necesito que ingreses un numero entero')
    return Numerito

print (f'Gracias, tu numero es {Ejemplo_Finale()}')

print (f'-----------')'''

import pandas as pd
from datetime import datetime

Date = input(f'Ingrese una fecha con formato YY-MM-DD: ')

try:
    Dat_Formateada = pd.to_datetime(Date)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Error, formato incorrecto')

print (f'{Cargar_Csv1}')

Encontrado = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Dat_Formateada.date()]

if (Encontrado.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    Grupo4 = Encontrado.groupby('product')['quantity'].sum()
    Grupo4_Prod = Grupo4.idxmax()
    Grupo4_Prod_Cant = Grupo4.max()

    print (f'En la fecha {Dat_Formateada} se realizaron un total de {Grupo4_Prod_Cant} {Grupo4_Prod}s')

class Mensaje:
    def Saludar(self):
        print (f'Hola Amigos')

class Maura():
    def __init__(self):
        self.Mensaje = Mensaje()

    def Mostrar(self):
        self.Mensaje.Saludar()

Objeto26 = Maura()

Objeto26.Mostrar()