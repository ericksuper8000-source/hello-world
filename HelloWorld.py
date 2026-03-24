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

print(f'--------------')

Array3 = np.array([[['a', 'e', 'p'], ['f', 'x', 's']],       [['o', 'k', 'n'], ['m', 'y', 'w']]])

print(f'--------------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],      [[[6, 5, 4], [9, 8, 7]], [[4, 9, 0], [2, 5, 8]]]])

print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')
print(f'--------------')