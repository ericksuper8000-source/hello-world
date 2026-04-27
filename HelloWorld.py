try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo no fue encontrado')

try:
    import Module_Own as PEPE
except ModuleNotFoundError:
    print (f'Error, el modulo no fue encontrado')

from Module_Own import Pokemon1 as Poke1

Objeto1 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto2 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto1.Mostrar()

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto3 = Poke_Kid1(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto3)
Objeto3.Mostrar()

print (f'-' * 20)

class Mascota1():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad} años')
        print (f'Peso: {self.Peso}kgs')

class Perro1(Mascota1):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')

Objeto4 = Perro1('Chester', 5, 2.5, 'Poodle', 'Asma')

Mascota1.Mostrar(Objeto4)
Objeto4.Mostrar()

print (f'-' * 20)

class Gato1(Mascota1):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')

Objeto5 = Gato1('Messi', 1.5, 1.8, 'Gris', 'No')

Mascota1.Mostrar(Objeto5)
Objeto5.Mostrar()

print (f'-' * 20)

class Pajaro1(Mascota1):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto6 = Pajaro1('Polly', 31, 0.4, 'Perico Azul', 'Si')

Mascota1.Mostrar(Objeto6)
Objeto6.Mostrar()

print (f'-' * 20)

class Camara1():
    def Fotografiar(self):
        print (f'La fotografia fue tomada')

class Reproductor1:
    def Reproducir_Musica(self):
        print (f'Musica Reproducida')

class Celular1(Camara1, Reproductor1):
    def Encender_Celular(self):
        print (f'Celular encendido')

Objeto7 = Celular1()

Objeto7.Encender_Celular()
Objeto7.Reproducir_Musica()
Objeto7.Fotografiar()

print (f'-' * 20)

class Atacante1():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon

    def Mostrar(self):
        print (f'Damage: {self.Damage}pts')
        print (f'Weapon: {self.Weapon}')

class Defensor1:
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life

    def Mostrar(self):
        print (f'Healing: {self.Healing}pts')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}')

class Paladin1(Atacante1, Defensor1):
    def __init__(self, Damage, Weapon, Healing, Potion, Life, Name):
        Atacante1.__init__(self, Damage, Weapon)
        Defensor1.__init__(self, Healing, Potion, Life)
        self.Name = Name

    def Mostrar(self):
        print (f'Name: {self.Name}')

Objeto8 = Paladin1(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto8.Mostrar()
Atacante1.Mostrar(Objeto8)
Defensor1.Mostrar(Objeto8)

print (f'-' * 20)

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

print (f'-' * 20)

class Efectivo1():
    def Pagar(self):
        print (f'El pago se realizo con efectivo')

class Tarjeta1:
    def Pagar(self):
        print (f'El pago se realizo con tarjeta')

class Cripto1:
    def Pagar(self):
        print (f'El pago se realizo con cripto')

Objeto10 = Cripto1()
Objeto11 = Tarjeta1()
Objeto12 = Efectivo1()

Objeto10.Pagar()
Objeto11.Pagar()
Objeto12.Pagar()

print (f'-' * 20)

class Cuenta_Bancaria1():
    def __init__(self, Saldo):
        self.__Saldo = Saldo

    def Deposito(self, Dinero):
        self.__Saldo += Dinero

    @property
    def Dinero(self):
        return self.__Saldo

    @Dinero.setter
    def Dinero(self, Nuevo_Saldo):
        self.__Saldo = Nuevo_Saldo

    def Mostrar(self):
        print (f'Tu saldo a la fecha es de ${self.__Saldo}')

Objeto13 = Cuenta_Bancaria1(100)
Objeto13.Deposito(25)
Objeto13.Mostrar()

print (f'Tu saldo privado es de {Objeto13.Dinero}')

Objeto13.Dinero = '50,000'

Objeto13.Mostrar()

print (f'Tu saldo privado es de {Objeto13.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla1(ABC):
    @abstractmethod
    def General(self):
        pass

class Ejemplo_Plantilla1(Plantilla1):
    def Mostrar(self):
        print (f'Hola Muchachos')

    def General(self):
        print (f'Este metodo es obligatorio debido a la abstraccion')

Objeto14 = Ejemplo_Plantilla1()

Objeto14.Mostrar()
Objeto14.General()

print (f'-' * 20)

class Una1():
    def Primera(self):
        print (f'Esto es parte de la clase composicion 1')

class Dos1:
    def __init__(self):
        self.Borradora = Una1()

    def Mostrar(self):
        self.Borradora.Primera()

Objeto15 = Dos1()

Objeto15.Mostrar()

print (f'-' * 20)

import re

Texto1 = 'esto @es 100 # hola un texto de 05 ejemplo para abeceabeceabab hala ver 29 si la$ mi_ca hela funciona'

Buscar1 = re.search(r'para', Texto1)

print (f'{Buscar1}')

Buscar2 = re.findall(r'\d+', Texto1)

print (f'{Buscar2}')

Buscar3 = re.fullmatch(r'esto \@es 100 hola un texto de 5 ejemplo para hala ver 29 si la\$ mi\_ca hela funciona', Texto1)

print (f'{Buscar3}')

Buscar4 = re.findall(r'([0-9]{1})', Texto1)

print (f'{Buscar4}')

Buscar5 = re.findall(r'(0[0-9] | [12][0-9] | [34][0-9])', Texto1)

print (f'{Buscar5}')

Buscar6 = re.findall(r'h.la', Texto1)

print (f'{Buscar6}')

Buscar7 = re.findall(r'[\W\s]', Texto1)

print (f'{Buscar7}')

Buscar8 = re.findall(r'^esto', Texto1)

print (f'{Buscar8}')

Buscar9 = re.findall(r'a$', Texto1)

print (f'{Buscar9}')

Buscar10 = re.findall(r'\d{3}\s\W', Texto1)

print (f'{Buscar10}')

Buscar11 = re.findall(r'[ab]{2,4}', Texto1)

print (f'{Buscar11}')

Buscar11 = re.findall(r'([12][0-9] | hola)', Texto1)

print (f'{Buscar11}')

import re

Correo1 = 'sample@sample.com'

Pattern1 = r'^[a-zA-Z0-9./*-+]+\@[a-zA-Z]+\.[a-z]{3}$'

Buscar12 = bool(re.match(Pattern1, Correo1))

if (Buscar12):
    print (f'Formato de correo electronico correcto')
else:
    print (f'El formato del correo es incorrecto')

print (f'-' * 20)

import re

Correo2 = 'ericksuper80@hotmail.com'

Patter2 = r'^[a-zA-Z0-9./*-+]+\@(gmail|yahoo|hotmail)\.(com|net|org)$'

Buscar13 = bool(re.match(Patter2, Correo2))

if (Buscar13 == True):
    print (f'Formato del segundo correo electronico correcto')
else:
    print (f'El formato del segundo correo es incorrecto')

Texto2 = '30'

Buscar14 = bool(re.match(r'(0[0-9]|[12][0-9]|3[01])', Texto2))

if (Buscar14 == True):
    print (f'El numero esta entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')

Texto3 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Patter3 = r'\d{2}/\d{2}\/[0-9]{4}'

Replacement = 'XX/XX/XXXX'

Buscar15 = re.sub(Patter3, Replacement, Texto3)

print (f'{Buscar15}')

Patter4 = r'\+\d{1}\-[0-9]{3}\-\d{3}\-[0-9]{4}'

Replacement2 = '+X-XXX-XXX-XXXX'

Buscar16 = re.sub(Patter4, Replacement2, Buscar15)

print (f'{Buscar16}')

Numero1 = 'Hola'

try:
    float(Numero1)
    print (f'El numero {Numero1} es decimal')
except ValueError:
    print (f'Error, el numero no es decimal')

Texto4 = "   Hola!!!   mundo@@   123   "

print (f'{Texto4}')

Texto4_Version1 = Texto4.strip()

print (f'{Texto4_Version1}')

Texto4_Version2 = ' '.join(Texto4_Version1.split())

print (f'{Texto4_Version2}')

Texto4_Version3 = Texto4_Version2.lower()

print (f'{Texto4_Version3}')

import re

Texto4_Version4 = re.sub(r'[^a-z0-9\s]', '', Texto4_Version3)

print (f'{Texto4_Version4}')

def Exception1(Numero):
    try:
        Numerito = int(Numero)
        print (f'Esto es un numero')
    except ValueError:
        print (f'Error, lo ingresado no es un numero')

Exception1('Hola')

def Exception2(Num1, Num2):
    try:
        Resultado = Num1 + Num2
        print (f'El resultado de la operacion es {Resultado}')
    except TypeError:
        print (f'Error, ambos elementos deben ser numeros')

Exception2(12, 'hola')

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(12, 0)

Lista_Exception4 = list([])
Lista_Exception4.append('Erick')
Lista_Exception4.extend(['Josue', 'Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento en la posicion {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = dict({'Nombre': "Erick", 'Edad': Objeto2.Cantidad})

def Exception5(Llave):
    try:
        print (f'El elemento en la posicion {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception5("Votante")

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Docu_SobreEscribir = Docu.write(f'Durazno')
        Docu.close()
except FileNotFoundError:
    print (f'Error, El file no fue encontrado')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Docu_Linea = Docu.readline()
    print (f'{Docu_Linea}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nManzana'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Docu_Lineas = Docu.readlines()
    print (f'{Docu_Lineas}')
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
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [55, 14, 26],
    'Votante' : [True, False, not False]
})

Data_Frame_Concatenate = pd.concat([Data_Frame1, Data_Frame2])

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame1}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate_Age}')

print (f'-' * 20)

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()} y la mayor de las edades es {Data_Frame_Concatenate_Age.max()}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombrecito = elemento['Nombre']

    print (f'Mi nombre es {Nombrecito}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv1 = 'C:\\Repo\\Store.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

print (f'-' * 20)

Fecha1 = '2026-04-01'

try:
    Fech1 = datetime.strptime(Fecha1, '%Y-%m-%d').date()
    Fech1_Formateada = pd.to_datetime(Fech1)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Formato de fecha incorrecto')

Buscando1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()]

if (Buscando1.empty):
    print (f'No hay ventas registradas en esta fecha')
else:
    print (f'Genial, ventas encontradas')

    Grupo1 = Buscando1.groupby('product')['quantity'].sum()
    Grupo1_May = Grupo1.idxmax()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_May_Cant = Grupo1.max()
    Grupo1_Min_Cant = Grupo1.min()

    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_May} vendio {Grupo1_May_Cant} elementos')
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Min} vendio {Grupo1_Min_Cant} elementos')

'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()'''

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'-' * 20)

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'Filas: {Filas}')
print (f'Columnas: {Columnas}')

Elemento1 = Data_Frame1.loc[0, 'Nombre']

print (f'{Elemento1}')

print (f'-' * 20)
Elemento2 = Data_Frame1.loc[1, 'Edad']

print (f'{Elemento2}')

print (f'-' * 20)
Elemento3 = Data_Frame1.loc[2, 'Votante']

print (f'{Elemento3}')

print (f'-' * 20)
Elemento4 = Data_Frame1.loc[0, :]

print (f'{Elemento4}')

print (f'-' * 20)
Elemento5 = Data_Frame1.loc[:, 'Votante']

print (f'{Elemento5}')

print (f'-' * 20)

Elemento6 = Data_Frame2.iloc[0, 0]
Elemento7 = Data_Frame2.iloc[1, 1]
Elemento8 = Data_Frame2.iloc[2, 2]
Elemento9 = Data_Frame2.iloc[0, :]
Elemento10 = Data_Frame2.iloc[:, 1]

print (f'{Elemento6}')
print (f'-' * 20)
print (f'{Elemento7}')
print (f'-' * 20)
print (f'{Elemento8}')
print (f'-' * 20)
print (f'{Elemento9}')
print (f'-' * 20)
print (f'{Elemento10}')
print (f'-' * 20)

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel)

print (f'{Cargar_Excel.head()}')

print (f'-' * 20)

Cargar_Excel1 = pd.read_excel(Ruta_Excel, sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, names=['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, index_col='cabina')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:J', index_col='cabina')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:J', index_col='cabina', nrows=1)

print (f'{Cargar_Excel1.head()}')

print (f'-' * 20)

print (f'{Cargar_Excel2.head()}')

print (f'-' * 20)

print (f'{Cargar_Excel3.head()}')

print (f'-' * 20)

print (f'{Cargar_Excel4.head()}')

print (f'-' * 20)

print (f'{Cargar_Excel5.head()}')

print (f'-' * 20)

print (f'{Cargar_Excel6.head()}')

print (f'-' * 20)

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='Cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'-' * 20)

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='Cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

print (f'-' * 20)

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'-' * 20)

print (f'{Cargar_Txt.head()}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv2 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

print (f'-' * 20)

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Leer_Html)

print (f'{Cargar_Html[2].head()}')

print (f'-' * 20)