import itertools
import nt
import turtledemo.penrose

try:
    import Module_Own as PEPE
except ImportError:
    print (f'El paquete es incorrecto')

from Module_Own import Pokemon as Poke

class Poke_Hija(Poke):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

    def Desplegar(self):
        print (f'{self.Nombre} es de tipos {self.Tipo}/{self.Sub_Tipo}')

Objeto1 = Poke_Hija(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno', 'Acero')
Objeto2 = Poke_Hija(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Hada')
Objeto3 = Poke_Hija(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Psiquico')

Poke.Mostrar(Objeto3)
Objeto3.Mostrar()
Objeto3.Desplegar()

print (f'----------------')

Poke.Mostrar(Objeto1)
Objeto1.Mostrar()
Objeto1.Desplegar()

print (f'----------------')

Poke.Mostrar(Objeto2)
Objeto2.Mostrar()
Objeto2.Desplegar()

print (f'----------------')

class Camara():
    def Tomar_Fotografia(self):
        print (f'FOTOGRAFIA TOMADA')

class Reproductor_Musica:
    def Reproducir_Musica(self):
        print (f'MUSICA REPRODUCIDA')

class Smartphone(Camara, Reproductor_Musica):
    def Encender_Smartphone(self):
        print (f'SMARTPHONE ENCENDIDO')

Objeto4 = Smartphone()

Objeto4.Encender_Smartphone()
Objeto4.Reproducir_Musica()
Objeto4.Tomar_Fotografia()

print (f'----------------')

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
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento, Visitas):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        self.Visitas = Visitas

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        print (f'Visitas: {self.Visitas} visitas en el mes')

Objeto5 = Perro('Chester', 3, 1.8, 'Poodle', 'Hipertension', 3)

Mascota.Mostrar(Objeto5)
Objeto5.Mostrar()

print (f'----------------')

class Gato(Mascota):
    def __init__(self, Nombre, Edad, Peso, Raza, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo} esta activo')

Objeto6 = Gato('Messi', 2, 1.2, 'Angora', 'Gris', 'Si')

Mascota.Mostrar(Objeto6)
Objeto6.Mostrar()

print (f'----------------')

class Pajaro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla} habla')

Objeto7 = Pajaro('Polly', 31, 0.4, 'Lora Verde', 'Si')

Mascota.Mostrar(Objeto7)
Objeto7.Mostrar()

print (f'----------------')

class Atacante():
    def __init__(self, Damage, Weapon, Attack_Energy):
        self.Damage = Damage
        self.Weapon = Weapon
        self.Attack_Energy = Attack_Energy

    def Mostrar(self):
        print (f'Damage: {self.Damage}')
        print (f'Weapon: {self.Weapon}')
        print (f'Attack_Energy: {self.Attack_Energy}')

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
    def __init__(self, Damage, Weapon, Attack_Energy, Healing, Potion, Life, Name):
        Atacante.__init__(self, Damage, Weapon, Attack_Energy)
        Curador.__init__(self, Healing, Potion, Life)
        self.Name = Name

    def Mostrar(self):
        print (f'Name: {self.Name}')

Objeto8 = Paladin(125, 'Espada Diamante', 30, 25, 'Pocion de esmeralda', 500, 'Ghost Knight')

Objeto8.Mostrar()
Atacante.Mostrar(Objeto8)
Curador.Mostrar(Objeto8)

print (f'----------------')

Clase_Hija = issubclass(Poke_Hija, Poke)

print (f'{Clase_Hija}')

Objeto_Clase = isinstance(Objeto8, Atacante)

print (f'{Objeto_Clase}')

print (f'----------------')

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

print (f'----------------')

class Efectivo():
    def Pagar(self):
        print (f'Pago realizado en efectivo')

class Tarjeta():
    def Pagar(self):
        print (f'Pago realizado con tarjeta')

class Cripto():
    def Pagar(self):
        print (f'Pago realizado en cripto')

Objeto10 = Cripto()
Objeto11 = Tarjeta()
Objeto12 = Efectivo()

Objeto10.Pagar()
Objeto11.Pagar()
Objeto12.Pagar()

print (f'----------------')

class Cuenta_Bancaria:
    def __init__(self, Saldo):
        self.__Saldo = Saldo

    def Depositar(self, Dinero):
        self.__Saldo += Dinero

    def Mostrar(self):
        return self.__Saldo

    @property
    def dinero(self):
        return self.__Saldo

    @dinero.setter
    def dinero(self, New_Saldo):
        self.__Saldo = New_Saldo

Objeto13 = Cuenta_Bancaria(100)
Objeto13.Depositar(25)

print (f'Gracias por elegirnos, tu saldo a la fecha es ${Objeto13.Mostrar()}')

print (f'La variable privada es {Objeto13.dinero}')

Objeto13.dinero = '20,000'

print (f'Gracias por elegirnos, tu saldo a la fecha es ${Objeto13.Mostrar()}')

print (f'----------------')

from abc import ABC, abstractclassmethod

class Plantilla(ABC):

    @abstractclassmethod
    def Mostrar(self):
        pass

class Ejemplo(Plantilla):
    def Mostrar(self):
        print (f'Ejemplo de Abstraccion')

Objeto14 = Ejemplo()

Objeto14.Mostrar()

print (f'----------------')

import re

Texto1 = 'este es 10 un aula hola texto de ejemplo 23, vamos! a helaver como ausente aullido 254 nos va con hala e-ste @topico autentico'

Buscar1 = re.search(r'e', Texto1)

print (f'{Buscar1}')

Buscar2 = re.findall(r'\d+', Texto1)

print (f'{Buscar2}')

Buscar3 = re.findall(r'\D+', Texto1)

print (f'{Buscar3}')

Buscar4 = re.findall(r'\w+', Texto1)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\W+', Texto1)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\s+', Texto1)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\S+', Texto1)

print (f'{Buscar7}')

Buscar8 = re.findall(r'h.la', Texto1)

print (f'{Buscar8}')

Buscar9 = bool(re.fullmatch(r'este es 10 un hola texto de ejemplo 23, vamos! a helaver como 254 nos va con hala e-ste @topico', Texto1))

print (f'{Buscar9}')

'''{2}
{2,}
{2,4}
+
*
?'''

Buscar10 = re.search(r'(au){1}', Texto1)

print (f'{Buscar10}')

Buscar11 = re.findall(r'(au){1,3}', Texto1)

print (f'{Buscar11}')

texto = "au auau auauau auauauau"
print(re.findall(r'(au){1,3}', texto))

Texto2 = 'este es hola un texto ₡150 pero lo mas interesante! es hala que ₡66 colones no es lo mismo que hela tener ₡0 en el bolsillo'

Buscar12 = re.findall(r'₡(\d+)', Texto2)

print (f'{Buscar12}')

Lista_Buscar12 = []

for elemento in Buscar12:
    Lista_Buscar12.append(int(elemento))

print (f'{Lista_Buscar12}')

Telefono1 = '8888-8888'

Pattern1 = r'[0-9]{4}\-\d{4}'

Buscar13 = bool(re.match(Pattern1, Telefono1))

if (Buscar13 == True):
    print (f'El telefono tiene el formato correcto')
else:
    print (f'Formato de telefono incorrecto')

Texto3 = 'Tu tarjeta caduca en 03/10/2026, es necesario que visites una sucursal antes de esta fecha'

Pattern2 = r'[0-9]{2}\/\d{2}\/[0-9]{4}'

Replacement = 'XX/XX/XXXX'

New_Texto3 = re.sub(Pattern2, Replacement, Texto3)

print (f'{New_Texto3}')

Email1 = 'sample@sample.com'

Pattern3 = r'^[a-zA-Z0-9./*-+_-]+\@[a-z]+\.[a-z]{2,}$'

Buscar14 = bool(re.match(Pattern3, Email1))

if (Buscar14 == True):
    print (f'Genial, Formato de correo correcto')
else:
    print (f'Error, formato incorrecto')

Buscar15 = re.findall(r'^este', Texto2)
Buscar16 = re.findall(r'bolsillo$', Texto2)

print (f'{Buscar15}')
print (f'{Buscar16}')

Texto4 = '123 123'

Buscar17 = re.findall(r'^[a-zA-Z]+|\d+$', Texto4)

print (f'{Buscar17}')

Texto5 = '123 @'

Buscar18 = bool(re.match(r'^\d{3}\s?\W$', Texto5))

if (Buscar18 == True):
    print (f'FORMATO CORRECTO')
else:
    print (f'FORMATO INCORRECTO')

Buscar19 = re.findall(r'[au]{1,}', Texto1)

print (f'{Buscar19}')

Texto6 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern4 = r'\d{2}\/[0-9]{2}\/\d{4}'

Replacement2 = '??/??/????'

New_Texto6 = re.sub(Pattern4, Replacement2, Texto6)

print (f'{New_Texto6}')

Lista_Dict1 = ['Erick', 'Josue', 'Karlita']

Key1 = [f'key{i}' for i in range(len(Lista_Dict1))]

print (f'{Key1}')

Diccionario_Dict1 = dict(zip(Key1, Lista_Dict1))

print (f'{Diccionario_Dict1}')
print (f'{Diccionario_Dict1.keys()}')
print (f'{Diccionario_Dict1["key1"]}')
print (f'{Diccionario_Dict1.get("key2")}')

import pandas as pd

Ruta_Csv1 = 'C:\\python-data-analyzer\\data\\sales.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

Lista_CSV1 = set(Cargar_Csv1['product'])
Key2 = [f'key_{i}' for i in range(len(Lista_CSV1))]

print (f'{Lista_CSV1}')
print (f'{Key2}')

Diccionario_Dict2 = dict(zip(Key2, Lista_CSV1))

print (f'{Diccionario_Dict2}')
print (f'{Diccionario_Dict2.keys()}')
print (f'{Diccionario_Dict2["key_0"]}')
print (f'{Diccionario_Dict2.get("key_1")}')

def Exception1(Num):
    try:
        Numerito = int(Num)
        print (f'Gracias, tu numero es {Numerito}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Exception1("hola")

def Exception2(Num1, Num2):
    try:
        Sum = Num1 + Num2
        print (f'El resultado de la sumatoria es {Sum}')
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

Lista_Exception4 = list(['Erick', 'Josue', 'Karlita'])

def Exception4(Indice):
    try:
        print (f'El indice {Indice} tiene como elemento {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception6(Llave):
    try:
        print (f'La llave {Llave} tiene como elemento {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception6("Votante")

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Durazno')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')

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
    'Edad' : [18*2, 20, 6],
    'Votante' : [True, not False, False]
})

print (f'{Data_Frame1}')

Data_Frame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [50, 14, 26],
    'Votante' : [True, False, not False]
})

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame_Concatenate_Age}')

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()} y la mayor es {Data_Frame_Concatenate_Age.max()}')

print (f'-------------')

print (f'{Data_Frame_Concatenate.info()}')

print (f'-------------')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombrecito = elemento['Nombre']

    print (f'Mi nombre es {Nombrecito}')

print (f'-------------')

Grupo1 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo1_Mayor = Grupo1.idxmax()
Grupo1_Menor = Grupo1.idxmin()
Grupo1_Mayor_Edad = Grupo1.max()
Grupo1_Menor_Edad = Grupo1.min()

print (f'{Grupo1}')

print (f'La menor de las personas es {Grupo1_Menor} ({Grupo1_Menor_Edad}) y la mayor es {Grupo1_Mayor} ({Grupo1_Mayor_Edad})')

print (f'-------------')

'''import pandas as pd
from datetime import datetime

Ruta_Csv2 = 'C:\\python-data-analyzer\\data\\sales.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2.head()}')

Fecha = input(f'Ingrese una fecha con formato YY-MM-DD: ')

try:
    Fech = datetime.strptime(Fecha, '%Y-%m-%d').date()
    Fech_Formateada = pd.to_datetime(Fech)
    Cargar_Csv2['date'] = pd.to_datetime(Cargar_Csv2['date'])
except ValueError:
    print (f'Error, formato incorrecto')
    exit()

Encontrado = Cargar_Csv2[Cargar_Csv2['date'].dt.date == Fech_Formateada.date()]

if (Encontrado.empty):
    print (f'No hay ventas en esta fecha')
else:
    Ventas = Cargar_Csv2.groupby('product')['quantity'].sum()
    Venta_Mayor = Ventas.idxmax()
    Venta_Menor = Ventas.idxmin()
    Venta_Mayor_Cant = Ventas.max()
    Venta_Menor_Cant = Ventas.min()

    print (f'El producto que vendio mas fue {Venta_Mayor} con un total de {Venta_Mayor_Cant} ventas')
    print (f'El producto que vendio menos fue {Venta_Menor} con un total de {Venta_Menor_Cant} ventas')

import pandas as pd
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
print (f'-------------')
print (f'{Data_Frame_Concatenate.head(1)}')
print (f'-------------')
print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'-------------')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'Filas {Filas}')
print (f'Columnas {Columnas}')

print (f'-------------')

Buscar21 = Data_Frame1.loc[0, 'Nombre']
Buscar22 = Data_Frame1.loc[1, 'Edad']
Buscar23 = Data_Frame1.loc[2, 'Votante']
Buscar24 = Data_Frame1.loc[0, :]
Buscar25 = Data_Frame1.loc[:, 'Edad']

print (f'{Buscar21}')
print (f'{Buscar22}')
print (f'{Buscar23}')
print (f'-------------')
print (f'{Buscar24}')
print (f'-------------')
print (f'{Buscar25}')
print (f'-------------')

Buscar26 = Data_Frame2.iloc[0, 0]
Buscar27 = Data_Frame2.iloc[1, 1]
Buscar28 = Data_Frame2.iloc[2, 2]
Buscar29 = Data_Frame2.iloc[0, :]
Buscar30 = Data_Frame2.iloc[:, 2]

print (f'{Buscar26}')
print (f'{Buscar27}')
print (f'{Buscar28}')
print (f'-------------')
print (f'{Buscar29}')
print (f'-------------')
print (f'{Buscar30}')
print (f'-------------')

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine='openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'-------------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tarifa')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:K", index_col='tarifa')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:K", index_col='tarifa', nrows=1)

print (f'{Cargar_Excel1.head()}')

print (f'-------------')

print (f'{Cargar_Excel2.head()}')

print (f'-------------')

print (f'{Cargar_Excel3.head()}')

print (f'-------------')

print (f'{Cargar_Excel4.head()}')

print (f'-------------')

print (f'{Cargar_Excel5.head()}')

print (f'-------------')

print (f'{Cargar_Excel6.head()}')

print (f'-------------')

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='Cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'-------------')

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='Cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')
print (f'-------------')

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'-------------')

print (f'{Cargar_Txt.head()}')

print (f'-------------')

Ruta_Csv3 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3.head()}')

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

Array1 = np.array([6, 9, 0])

print (f'{Array1}')
print (f'{Array1.ndim}') # 1
print (f'{Array1.shape}') # 1x3
print (f'{Array1.size}') # 3
print (f'{Array1.dtype}') # int64
print (f'{Array1[2]}')

print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[1:2]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 >= 2]}')

print (f'-------------')

Array2 = np.array([[7,3,9], [4,5,1]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 0]}')

print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[0, 2:3]}')
print (f'{Array2[:, 1]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[1, 0:None])
Sumita4 = np.sum(Array2_Sorted[1, :])

print (f'El resultado de la sumita es {Sumita1}')
print (f'El resultado de la sumita es {Sumita2}')
print (f'El resultado de la sumita es {Sumita3}')
print (f'El resultado de la sumita es {Sumita4}')

print (f'-------------')

Array3 = np.array([[['e', 'u', 'p'], ['x', 'v', 'm']],        [['n', 'a', 's'], ['r', 'w', 'i']]])

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
print (f'{Array3[1, 1, 2:3]}')
print (f'{Array3[1, :, 0]}')
print (f'{Array3[1, 0, 0:None]}')
print (f'{Array3[1, 0, :]}')
print (f'{Array3[Array3 == "u"]}')

print (f'-------------')

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],      [[[6, 5, 4], [9, 8, 7]], [[0, 5, 8], [9, 1, 7]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[0, 1, 0, 2]}')

print (f'{Array4[1, 1, 0, :2]}')
print (f'{Array4[1, 1, 0, 2:]}')
print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[0, 1, 1, ::3]}')
print (f'{Array4[0, 0, 1, 1:2]}')
print (f'{Array4[1, 1, :, 0]}')
print (f'{Array4[1, 0, 0, 0:None]}')
print (f'{Array4[1, 0, 0, :]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)
print (f'-------------')
print (f'Ordenado \n{Array4_Sorted}')
print (f'-------------')
print (f'Media {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria {Array4_Sorted_Sum}')

print (f'-------------')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[0, 1, 1, 0:None])
Sumita8 = np.sum(Array4_Sorted[0, 1, 1, :])

print (f'{Sumita5}')
print (f'{Sumita6}')
print (f'{Sumita7}')
print (f'{Sumita8}')

print (f'-------------')

Array_Num1 = np.arange(10)

print (f'{Array_Num1}')

Array_Num1_Max = np.max(Array_Num1)
Array_Num1_Min = np.min(Array_Num1)

print (f'El menor de los numeros es {Array_Num1_Min} y el mayor es {Array_Num1_Max}')

print (f'-------------')

Array_Num2 = np.arange(start=1, stop=26, step=(1))

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

Array_Num2_Reshape_Column_Max = np.max(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Column_Min = np.min(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Row_Max = np.max(Array_Num2_Reshape, axis=1)
Array_Num2_Reshape_Row_Min = np.min(Array_Num2_Reshape, axis=1)

print (f'Los mayores de las columnas son {Array_Num2_Reshape_Column_Max}')
print (f'Los menores de las columnas son {Array_Num2_Reshape_Column_Min}')
print (f'Los mayores de las filas son {Array_Num2_Reshape_Row_Max}')
print (f'Los menores de las filas son {Array_Num2_Reshape_Row_Min}')

print (f'-------------')

Array_Zero = np.zeros(shape=(2, 3))

print (f'{Array_Zero}')
print (f'{Array_Zero.ndim}')
print (f'{Array_Zero.shape}')
print (f'{Array_Zero.size}')
print (f'{Array_Zero.dtype}')
print (f'{Array_Zero[1, 1]}')

print (f'-------------')

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 0]}')

print (f'-------------')

Array_Gen1 = np.full(shape=(2, 3), fill_value=PEPE.Diccionario_Poke['Poke1'])

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 0]}')

print (f'-------------')

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

print (f'{Array_Gen2}')

Lista_Array1 = list([])

for elemento in Array_Gen2:
    Lista_Array1.append(str(elemento))

print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-------------')

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[1, 0, 1, 2:3])

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

Array_Gen4 = np.full(shape=(3, 2), fill_value = Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value = Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value = Diccionario_Array['Nombre'][2])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'-------------')

print (f'{Array_Gen6[3]}')

print (f'-------------')

Array_Num3 = np.arange(start=1, stop=6, step=1)
Array_Num4 = np.arange(start=2, stop=11, step=2)
Array_Num5 = np.arange(start=3, stop=31, step=3)
Array_Num6 = np.arange(start=2, stop=21, step=2)
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
Array_Random2_Mean = np.mean(Array_Random2)
Array_Random2_Sum = np.sum(Array_Random2)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sum}')

print (f'-------------')

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Sum = Arr1 + Arr2
Rest = Arr1 - Arr2
Div = Arr1 / Arr2
Mult = Arr1 * Arr2

Array_Random1_Cien = Array_Random1 + 100

print (f'El resultado de la operacion es {Sum}')
print (f'El resultado de la operacion es {Rest}')
print (f'El resultado de la operacion es {Div}')
print (f'El resultado de la operacion es {Mult}')
print (f'El resultado de la operacion es {Array_Random1_Cien}')

print (f'-------------')

Array_Random3 = np.random.randint(low=1, high=10, size=(20))

print (f'{Array_Random3}')

Array_Random3_Reshape = np.reshape(Array_Random3, shape=(4, 5))

print (f'{Array_Random3_Reshape}')

Array_Random3_Reshape_Ravel = np.ravel(Array_Random3_Reshape)

print (f'{Array_Random3_Reshape_Ravel}')

print (f'-------------')

Lista_Array2 = ['Erick', 'Josue', 'Karlita']

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-------------')

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concatenate([Array6, Array7])

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

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-------------')

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

print (f'-------------')

Lista_Sorteo = ['Erick', 'Josue', 'Karlita', 'Carmelo', 'Susanita', 'Roxana']

Ganador1 = np.random.choice(Lista_Sorteo, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Sorteo, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Sorteo, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-------------')

Array_Linspace = np.linspace(start=0, stop=10, num=3)

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
    for elemento in range(0,5):
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
    print (f'Fin del experimento')

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

    return Usuario_Interno('FEMENINO')

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

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.5, 20, True)

print (f'{Funcion_Tupla("Perro", 3.5, 20, True)}')
print (f'{Funcion_Tupla("Perro", 3.5, 20, True)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.5, 20, True))}')

print (f'------------')

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')

Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])

print (f'------------')

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

print (f'Los numeros pares de la lista son {list(Anonima3)} o podrian ser {PEPE.Lista_Par}')

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
print (f'{Variable_Closure(23)}')
print (f'{Variable_Closure(37)}')

def Crear_Multiplicador(x):
    def Multiplicador(y):
        return x * y

    return Multiplicador

Variable_Mult1 = Crear_Multiplicador(2)
Variable_Mult2 = Crear_Multiplicador(3)

print (f'El multiplicador es {Variable_Mult1(10)}')
print (f'El multiplicador es {Variable_Mult2(10)}')

def Filtrador(Lista):
    any_impar = any(num % 2 != 0 for num in Lista)
    if (any_impar == True):
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impares = [num for num in Lista if num % 2 != 0]

        print (f'Los numeros impares de la lista son {list(Anonima4)} o incluso podrian ser {Lista_Impares}')
    else:
        print (f'Error, no hay numeros impares en la lista')

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
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la operacion es {Sumatoria3(4, 7)}')

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