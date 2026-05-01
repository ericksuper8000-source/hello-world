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

Texto5 = "   Hola!!!   mundo@@   123   "

print (f'{Texto5}')

Texto5_Version1 = Texto5.strip()

print (f'{Texto5_Version1}')

Texto5_Version2 = ' '.join(Texto5_Version1.split())

print (f'{Texto5_Version2}')

Texto5_Version3 = Texto5_Version2.lower()

print (f'{Texto5_Version3}')

import re

Texto5_Version4 = re.sub(r'[^a-z0-9\s]', '', Texto5_Version3)

print (f'{Texto5_Version4}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

print (f'-' * 20)

Fecha2 = '2026-04-01'

try:
    Fech2 = datetime.strptime(Fecha2, '%Y-%m-%d').date()
    Fech2_Formateada = pd.to_datetime(Fech2)
    Cargar_Csv3['date'] = pd.to_datetime(Cargar_Csv3['date'])
except ValueError:
    print (f'Error, formato de fecha incorrecto')

Encontrado2 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech2_Formateada.date()]

if (Encontrado2.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! encontramos ventas')

    Grupo2 = Encontrado2.groupby('product')['quantity'].sum()
    Grupo2_May = Grupo2.idxmax()
    Grupo2_Min = Grupo2.idxmin()
    Grupo2_May_Cant = Grupo2.max()
    Grupo2_Min_Cant = Grupo2.min()

    print (f'En la fecha {Fech2_Formateada} el producto {Grupo2_May} vendio {Grupo2_May_Cant} unidades')
    print (f'En la fecha {Fech2_Formateada} el producto {Grupo2_Min} vendio {Grupo2_Min_Cant} unidades')

print (f'-' * 20)

Array0 = list([
    [1, 2, 3],
    [4, 5, 6]
])

print (f'{Array0}')
print (f'{Array0[1][:2]}')
print (f'{Array0[1][2:]}')
print (f'{Array0[0][::2]}')
print (f'{Array0[0][::3]}')
print (f'{Array0[1][0:None]}')
print (f'{Array0[1][:]}')
print (f'{Array0[:][1]}')

print (f'-' * 20)

for i in range(len(Array0)):
    for j in range(len(Array0[i])):
        print (f'{Array0[i][j]}')

import numpy as np

Array1 = np.array([1, 2, 3])

print (f'{Array1}')
print (f'{Array1.ndim}')
print (f'{Array1.shape}')
print (f'{Array1.size}')
print (f'{Array1.dtype}')
print (f'{Array1[2]}')

print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[2:3]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 <= 2]}')

print (f'-' * 20)

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}')
print (f'{Array2.shape}')
print (f'{Array2.size}')
print (f'{Array2.dtype}')
print (f'{Array2[1, 1]}')

print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[0, ::2]}')
print (f'{Array2[0, ::3]}')
print (f'{Array2[1, 3:4]}')
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

print (f'-' * 20)

Array3 = np.array([[['w', 'u', 'a'], ['f', 'x', 'i']],     [['s', 'v', 'n'], ['k', 'm', 'l']]])

print (f'{Array3}')
print (f'{Array3.ndim}')
print (f'{Array3.shape}')
print (f'{Array3.size}')
print (f'{Array3.dtype}')
print (f'{Array3[1, 0, 2]}')

print (f'{Array3[0, 1, :2]}')
print (f'{Array3[0, 1, 2:]}')
print (f'{Array3[1, 0, ::2]}')
print (f'{Array3[1, 0, ::3]}')
print (f'{Array3[0, 1, 2:3]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[1, 0, 0:None]}')
print (f'{Array3[1, 0, :]}')
print (f'{Array3[Array3 == "u"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],      [[[6, 5, 4], [9, 8, 7]], [[0, 5, 9], [4, 8, 1]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 0, 2]}')

print (f'{Array4[1, 0, 1, :2]}')
print (f'{Array4[1, 0, 1, 2:]}')
print (f'{Array4[1, 1, 0, ::2]}')
print (f'{Array4[0, 1, 0, ::3]}')
print (f'{Array4[1, 0, 1, 2:3]}')
print (f'{Array4[1, 1, :, 2]}')
print (f'{Array4[1, 0, 0, 0:None]}')
print (f'{Array4[1, 0, 0, :]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[1, 0, 1, 0:None])
Sumita8 = np.sum(Array4_Sorted[1, 0, 1, :])

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

print (f'El numero menor de la lista es {Array_Num1.min()} y el numero mayor es {Array_Num1.max()}')

Array_Min = np.min(Array_Num1)
Array_Max = np.max(Array_Num1)

print (f'El numero menor de la lista es {Array_Min} y el numero mayor es {Array_Max}')

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

print (f'-' * 20)

Array_Zero = np.zeros(shape=(2, 3))

print (f'{Array_Zero}')
print (f'{Array_Zero.ndim}')
print (f'{Array_Zero.shape}')
print (f'{Array_Zero.size}')
print (f'{Array_Zero.dtype}')
print (f'{Array_Zero[1, 0]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 2]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 0]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value = f'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[3]}')

Lista_Array1 = list([])

for elemento in Array_Gen2:
    Lista_Array1.append(str(elemento))

print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4_Sorted[1, 0, 1, 2])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[0, 1]}')

print (f'-' * 20)

Tupla_Array = tuple(('Rojo', 'Verde'))
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array['Nombre'][2:3])

print (f'{Array_Gen4}')
print (f'{Array_Gen4.ndim}')
print (f'{Array_Gen4.shape}')
print (f'{Array_Gen4.size}')
print (f'{Array_Gen4.dtype}')
print (f'{Array_Gen4[2, 1]}')

print (f'-' * 20)

print (f'{Array_Gen5}')
print (f'{Array_Gen5.ndim}')
print (f'{Array_Gen5.shape}')
print (f'{Array_Gen5.size}')
print (f'{Array_Gen5.dtype}')
print (f'{Array_Gen5[1, 0]}')

print (f'-' * 20)

print (f'{Array_Gen6}')
print (f'{Array_Gen6.ndim}')
print (f'{Array_Gen6.shape}')
print (f'{Array_Gen6.size}')
print (f'{Array_Gen6.dtype}')
print (f'{Array_Gen6[3, 0]}')

print (f'-' * 20)

print (f'{Array_Gen6[3]}')

print (f'-' * 20)

Array_Num3 = np.arange(start=1, stop=6, step=1)
Array_Num4 = np.arange(start=2, stop=11, step=2)
Array_Num5 = np.arange(start=3, stop=31, step=3)
Array_Num6 = np.arange(start=10, stop=21, step=2)
Array_Num7 = np.arange(10)

print (f'{Array_Num3}')
print (f'{Array_Num4}')
print (f'{Array_Num5}')
print (f'{Array_Num6}')
print (f'{Array_Num7}')

print (f'-' * 20)

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')

print (f'-' * 20)

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')
print (f'{Array_Random2.ndim}')
print (f'{Array_Random2.shape}')
print (f'{Array_Random2.size}')
print (f'{Array_Random2.dtype}')
print (f'{Array_Random2[1, 1]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Mean = np.mean(Array_Random2)
Array_Random2_Sum = np.sum(Array_Random2)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Acomodado: {round(Array_Random2_Mean, 2)}')
print (f'Acomodado: {Array_Random2_Sum}')

Sumita9 = np.sum(Array4_Sorted, axis=0)
Sumita10 = np.sum(Array4_Sorted, axis=1)
Sumita11 = np.sum(Array4_Sorted[0, 0:None])
Sumita12 = np.sum(Array4_Sorted[0, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

print (f'-' * 20)

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

print (f'-' * 20)

Array_Num8 = np.arange(20)

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Lista_Array2 = []
Lista_Array2.append('Uno')
Lista_Array2.extend(['Tres', 'Cuatro'])
Lista_Array2.insert(1, 'Dos')

print (f'{Lista_Array2}')

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-' * 20)

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concatenate([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'-' * 20)

Array_Concatenate_Split = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Split[0]}')
print (f'{Array_Concatenate_Split[1]}')
print (f'{Array_Concatenate_Split[2]}')

print (f'-' * 20)

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'-' * 20)

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'-' * 20)

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'-' * 20)

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')
print (f'{Array_Random3.ndim}')
print (f'{Array_Random3.shape}')
print (f'{Array_Random3.size}')
print (f'{Array_Random3.dtype}')
print (f'{Array_Random3[1, 0, 2]}')

Sumita13 = np.sum(Array_Random3, axis=0)
Sumita14 = np.sum(Array_Random3, axis=1)
Sumita15 = np.sum(Array_Random3[0, 1, 0:None])
Sumita16 = np.sum(Array_Random3[0, 1, :])

print (f'El resultado de la sumita es {Sumita13}')
print (f'El resultado de la sumita es {Sumita14}')
print (f'El resultado de la sumita es {Sumita15}')
print (f'El resultado de la sumita es {Sumita16}')

print (f'-' * 20)

Lista_Array3 = ['Erick', 'Josue', 'Karlita', 'Karlita', 'Carmelo', 'Roxana']

Ganador1 = np.random.choice(Lista_Array3, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Array3, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Array3, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-' * 20)

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-' * 20)

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

print (f'-' * 20)

def Generadora2():
    for elemento in range(1, 5):
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

print (f'-' * 20)

def Generadora3():
    for elemento in range(5):
        if (elemento == 0):
            yield f'The number is zero'
        elif (elemento == 1):
            yield f'The number is one'
        elif (elemento == 2):
            yield f'The number is two'
        elif (elemento == 3):
            yield f'The number is three'
        elif (elemento == 4):
            yield f'The number is four'
        else:
            yield f'Coding Error'

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

print (f'-' * 20)

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(7, 4)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int):
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
    print (f'{Docu_Lineas}')
    Docu.close()

Texto6 = "   Hola!!!   mundo@@   123   "

print (f'{Texto6}')

Texto6_Version1 = Texto6.lower()

print (f'{Texto6_Version1}')

Texto6_Version2 = Texto6_Version1.strip()

print (f'{Texto6_Version2}')

Texto6_Version3 = ' '.join(Texto6_Version2.split())

print (f'{Texto6_Version3}')

import re

Texto6_Version4 = re.sub(r'[^a-z0-9\s]', '', Texto6_Version3)

print (f'{Texto6_Version4}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv4 = 'C:\\Repo\\Store.csv'

Cargar_Csv4 = pd.read_csv(Ruta_Csv4)

print (f'{Cargar_Csv4}')

print (f'-' * 20)

Fecha3 = '2026-04-01'

try:
    Fech3 = datetime.strptime(Fecha3, '%Y-%m-%d').date()
    Fech3_Formateado = pd.to_datetime(Fech3)
    Cargar_Csv4['date'] = pd.to_datetime(Cargar_Csv4['date'])
except ValueError:
    print (f'Error, formato de fecha incorrecto')
    exit()

Encontrado3 = Cargar_Csv4[Cargar_Csv4['date'].dt.date == Fech3_Formateado.date()]

if (Encontrado3.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! hemos encontrado ventas')
    Grupo3 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo3_May = Grupo3.idxmax()
    Grupo3_Min = Grupo3.idxmin()
    Grupo3_May_Cant = Grupo3.max()
    Grupo3_Min_Cant = Grupo3.min()

    print (f'En la fecha {Fech3_Formateado} el producto {Grupo3_May} vendio un total de {Grupo3_May_Cant} unidades')
    print (f'En la fecha {Fech3_Formateado} el producto {Grupo3_Min} vendio un total de {Grupo3_Min_Cant} unidades')

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 36, 3.5, True)

print (f'{Funcion_Tupla("Perro", 36, 3.5, True)}')
print (f'{Funcion_Tupla("Perro", 36, 3.5, True)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 36, 3.5, True))}')

print (f'-' * 20)

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')

Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7 ,8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5 ,6 ,7 ,8, 9, 10)}')

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
    return PEPE.GLOBAL + Local

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
print (f'{Variable_Closure(23)}')
print (f'{Variable_Closure(50)}')

print (f'-' * 20)

def Crear_Multiplicador(x):
    def Multiplicador(y):
        return x * y

    return Multiplicador

Mult1 = Crear_Multiplicador(2)
Mult2 = Crear_Multiplicador(3)

print (f'El resultado del multiplicador es {Mult1(10)}')
print (f'El resultado del multiplicador es {Mult2(10)}')

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    if (Any_Impar == True):
        Lista_Impar = [num for num in Lista if num % 2 != 0]
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)

        print (f'Los elementos impares de la lista son {list(Anonima4)} o incluso podrian ser {Lista_Impar}')
    else:
        print (f'Error, no hay elementos impares en la lista')

Filtrador(PEPE.Lista_Numeros)

def Primera(Segunda):
    def Tercera():
        print (f'XXXXXXXX')
        Segunda()
        print (f'XXXXXXXX')

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

print (f'El resultado de la sumatoria es {Sumatoria3(4, 7)}')

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonatha'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)

    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    print (f'Mi nombre es {Nombre} {Apellido}')

Usuario2('Erick', 'Perez')

print (f'-' * 20)

from Module_Own import Pokemon2 as Poke2

Objeto16 = Poke2(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')

Objeto16.Mostrar()

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto17 = Poke_Kid2(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto17)
Objeto17.Mostrar()

print (f'-' * 20)

class Camara2():
    def Tomar_Fotografia(self):
        print (f'Fotografia tomada')

class Reproductor_Musica2:
    def Reproducir_Musica(self):
        print (f'Musica reproducida')

class Celular2(Camara2, Reproductor_Musica2):
    def Encender_Celular(self):
        print (f'Celular encendido')

Objeto18 = Celular2()

Objeto18.Encender_Celular()
Objeto18.Reproducir_Musica()
Objeto18.Tomar_Fotografia()

print (f'-' * 20)

class Veterinaria2():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad} años')
        print (f'Peso: {self.Peso}kgs')

class Perro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')

Objeto19 = Perro2('Chester', 5, 2.8, 'Poodle', 'Asma')

Veterinaria2.Mostrar(Objeto19)
Objeto19.Mostrar()

print (f'-' * 20)

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')

Objeto20 = Gato2('Messi', 1.5, 1.8, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto20)
Objeto20.Mostrar()

print (f'-' * 20)

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto21 = Pajaro2('Polly', 31, 0.4, 'Papagayo', 'Si')

Veterinaria2.Mostrar(Objeto21)
Objeto21.Mostrar()

print (f'-' * 20)

class Atacante2():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon

    def Mostrar(self):
        print (f'Damage: {self.Damage}pts')
        print (f'Weapon: {self.Weapon}')

class Defensor2:
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life

    def Mostrar(self):
        print (f'Healing: {self.Healing}pts')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}pts')

class Hechicero(Atacante2, Defensor2):
    def __init__(self, Damage, Weapon, Healing, Potion, Life, Name):
        Atacante2.__init__(self, Damage, Weapon)
        Defensor2.__init__(self, Healing, Potion, Life)
        self.Name = Name

    def Mostrar(self):
        print (f'Name: {self.Name}')

Objeto22 = Hechicero(65, 'Baston de luz', 50, 'Dark Crystal', 200, 'Gandalf')

Objeto22.Mostrar()
Atacante2.Mostrar(Objeto22)
Defensor2.Mostrar(Objeto22)

print (f'-' * 20)

Hija_Padre = issubclass(Poke_Kid2, Poke2)
Objeto_Clase1 = isinstance(Objeto22, Atacante2)
Objeto_Clase2 = isinstance(Objeto22, Defensor2)
Objeto_Clase3 = isinstance(Objeto22, Hechicero)

print (f'{Hija_Padre}')
print (f'{Objeto_Clase1}')
print (f'{Objeto_Clase2}')
print (f'{Objeto_Clase3}')

print (f'-' * 20)

class A2():
    def Mostrar(self):
        print (f'Hola A')

class E2():
    def Mostrar(self):
        print (f'Hola E')

class B2(E2):
    def Mostrar(self):
        print (f'Hola B')

class C2(A2):
    def Mostrar(self):
        print (f'Hola C')

class D2(B2, C2):
    def Mostrar(self):
        print (f'Hola D')

Objeto23 = D2()

A2.Mostrar(Objeto23)
B2.Mostrar(Objeto23)
C2.Mostrar(Objeto23)
Objeto23.Mostrar()
E2.Mostrar(Objeto23)

print (f'-' * 20)

class Efectivo2:
    def Depositar(self):
        print (f'El deposito se realizo en efectivo')

class Tarjeta2():
    def Depositar(self):
        print (f'El deposito se realizo en tarjeta')

class Cripto2:
    def Depositar(self):
        print (f'El deposito se realizo en cripto')

Objeto24 = Cripto2()
Objeto25 = Tarjeta2()
Objeto26 = Efectivo2()

Objeto24.Depositar()
Objeto25.Depositar()
Objeto26.Depositar()

print (f'-' * 20)

class Cuenta_Bancaria2():
    def __init__(self, Saldo):
        self.__Saldo = Saldo

    def Depositar(self, Dinero):
        self.__Saldo += Dinero

    @property
    def Dinero(self):
        return self.__Saldo

    @Dinero.setter
    def Dinero(self, Nuevo_Saldo):
        self.__Saldo = Nuevo_Saldo

    def Mostrar(self):
        print (f'Tu saldo a la fecha es de ${self.__Saldo}')

Objeto27 = Cuenta_Bancaria2(100)
Objeto27.Depositar(25)
Objeto27.Mostrar()

print (f'Tu saldo privado es de {Objeto27.Dinero}')

Objeto27.Dinero = '55,000'

Objeto27.Mostrar()

print (f'Tu saldo privado es de {Objeto27.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def Borradora(self):
        pass

class Ejemplo2(Plantilla2):
    def Mostrar(self):
        print (f'HOLA AMIGOS')

    def Borradora(self):
        print (f'Esto es lo que debo agregar a fuera para cumplir la abstraccion')

Objeto28 = Ejemplo2()

Objeto28.Mostrar()
Objeto28.Borradora()

print (f'-' * 20)

class Composicion():
    def Compo1(self):
        print (f'Este mensaje de composicion se mostrara en la otra clase')

class Ejemplo_Composicion:
    def __init__(self):
        self.Textico = Composicion()

    def Mostrar(self):
        self.Textico.Compo1()

Objeto29 = Ejemplo_Composicion()

Objeto29.Mostrar()

print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''
Esto
Es
Un
Long
String'''

variable4 = Variable_Sumatoria
variable5 = PEPE.Division_Flotante
variable6, variable7 = not False, Objeto3.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')

print (f'Mi nombre completo es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Variable_Sumatoria}, {Sumatoria2(1, 2, 3, 4)} o incluso {Objeto2.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Koala' in PEPE.Lista2)

print (f'Graveler' in PEPE.Set_Conjunto_Poke)

print (f'Misty' in PEPE.Tupla_Poke)

print (f'Pikachu' in PEPE.Diccionario_Poke['Poke1'])

print (f'-' * 20)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables y snake case asignation al mismo tiempo {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto2.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'{PEPE.Lista2[2:3]}')
print (f'{PEPE.Lista2[:2]}')
print (f'{PEPE.Lista2[2:]}')
print (f'{PEPE.Lista2[::2]}')
print (f'{PEPE.Lista2[::3]}')
print (f'{PEPE.Lista2[0:None]}')
print (f'{PEPE.Lista2[:]}')

print (f'{Lista_Uno[1]} eso de ahi es un {PEPE.Lista2[2]}?')

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

print (f'-' * 20)

Texto7 = "   Hola!!!   mundo@@   123   "

print (f'{Texto7}')

Texto7_Version1 = Texto7.strip()

print (f'{Texto7_Version1}')

Texto7_Version2 = ' '.join(Texto7_Version1.split())

print (f'{Texto7_Version2}')

Texto7_Version3 = Texto7_Version2.lower()

print (f'{Texto7_Version3}')

import re

Texto7_Version4 = re.sub(r'[^a-z0-9\s]', '', Texto7_Version3)

print (f'{Texto7_Version4}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv5 = 'C:\\Repo\\Store.csv'

Cargar_Csv5 = pd.read_csv(Ruta_Csv5)

print (f'{Cargar_Csv5}')

print (f'-' * 20)

Fecha4 = '2026-04-01'

try:
    Fech4 = datetime.strptime(Fecha4, '%Y-%m-%d').date()
    Fech4_Formateado = pd.to_datetime(Fech4)
    Cargar_Csv5['date'] = pd.to_datetime(Cargar_Csv5['date'])
except ValueError:
    print (f'Error, formato incorrecto')
    exit()

Encontrado4 = Cargar_Csv5[Cargar_Csv5['date'].dt.date == Fech4_Formateado.date()]

if (Encontrado4.empty):
    print (f'No hay ventas en esta fecha')
else:
    print (f'Genial! ventas encontradas')
    Grupo4 = Encontrado4.groupby('product')['quantity'].sum()
    Grupo4_May = Grupo4.idxmax()
    Grupo4_Min = Grupo4.idxmin()
    Grupo4_May_Cant = Grupo4.max()
    Grupo4_Min_Cant = Grupo4.min()

    print (f'En la fecha {Fech4_Formateado} el producto {Grupo4_May} vendio {Grupo3_May_Cant} unidades')
    print (f'En la fecha {Fech4_Formateado} el producto {Grupo4_Min} vendio {Grupo4_Min_Cant} unidades')

print (f'{variable4.__dir__()}')

print (f'{help(Objeto22)}')

Tupla1 = ('Electrico', Objeto1.Tipo, Objeto1.Tipo, Objeto1.Tipo, Objeto1.Tipo)

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

Tupla1 = tuple(('Red', 'Black', 'Blue'))

print (f'{Tupla1}')

Set_Conjunto1 = {'Balon', 'Balon', 'Balon', 'Balon', 'Balon'}
Set_Conjunto1.add('Casa')
Set_Conjunto1.add('Bicicleta')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Ball', 'House', 'Bicycle'})

print (f'{Set_Conjunto1}')

Set_Conjunto2 = {1, 2, 3, 4, 5}
Set_Conjunto3 = {4, 5}
Set_Conjunto4 = set({8})

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto2 >= Set_Conjunto3}')
print (f'-' * 20)
print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto3 <= Set_Conjunto2}')
print (f'-' * 20)
print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')
print (f'-' * 20)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print (f'{A.union(B)}')
print (f'{A | B}')

print (f'-' * 20)

print (f'{A.intersection(B)}')
print (f'{A & B}')

print (f'-' * 20)

print (f'{A.difference(B)}')
print (f'{A - B}')

print (f'-' * 20)

print (f'{B.difference(A)}')
print (f'{B - A}')

print (f'-' * 20)

print (f'{A.symmetric_difference(B)}')
print (f'{A ^ B}')

print (f'-' * 20)

A1 = {1, 2, 3}
B1 = {3, 4}

'''A1.update(B1)

print (f'{A1}')'''

'''A1.intersection_update(B1)

print (f'{A1}')'''

'''A1.difference_update(B)

print (f'{A1}')'''

'''B1.difference_update(A1)

print (f'{B1}')'''

A1.symmetric_difference_update(B1)

print (f'{B1}')

print (f'-' * 20)

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, Objeto3.Nombre})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu4 = Set_Conjunto_Menu1.union(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu4}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Objeto2.Cantidad,
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

Diccionario1['Nombre'] = variable1

print (f'{Diccionario1}')

del Diccionario1['Nombre']
Diccionario1.pop('Edad')

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')

Diccionario1 = dict({1 : "Karlita", 2 : variable4, 3 : not False})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'{Diccionario2["Nombre"][2]} no puede votar ya que solo tiene {Diccionario1.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'Hola')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = Lista_Uno_Copia[0]

print (f'{Diccionario_Vacio1}')

print (f'{Diccionario_Vacio2}')

Key1 = [f'{i}' for i in range(len(Lista_Uno_Copia))]

print (f'{Key1}')

Diccionario4 = dict(zip(Key1, Lista_Uno_Copia))

for elemento in Diccionario4.keys():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario4.values():
    print(f'{elemento}')

print(f'-' * 20)

for elemento in Diccionario4.items():
    print(f'{elemento[0]} -- {elemento[1]}')

print(f'-' * 20)

print (f'{Cargar_Csv5}')

print(f'-' * 20)

Set_Conjunto_Diccionario5 = set(Cargar_Csv5['product'])

print (f'{Set_Conjunto_Diccionario5}')

Key2 = [f'key{i}' for i in range(len(Set_Conjunto_Diccionario5))]

print (f'{Key2}')

Diccionario5 = dict(zip(Key2, Set_Conjunto_Diccionario5))

for elemento in Diccionario5.keys():
    print (f'{elemento}')

print(f'-' * 20)

for elemento in Diccionario5.values():
    print(f'{elemento}')

print(f'-' * 20)

for elemento in Diccionario5.items():
    print(f'{elemento[0]} -- {elemento[1]}')

print(f'-' * 20)

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
print (f'El tipo de dato de la variable es {type(Objeto2.Catched)}')
print (f'El tipo de dato de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato de la variable es {type(Tupla3)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de dato de la variable es {type(Diccionario4)}')
print (f'El tipo de dato de la variable es {type(Funcion_Tupla)}')
print (f'El tipo de dato de la variable es {type(Objeto6)}')
print (f'El tipo de dato de la variable es {type(Poke_Kid1)}')
print (f'El tipo de dato de la variable es {type(Data_Frame_Concatenate)}')
print (f'El tipo de dato de la variable es {type(Array_Gen1)}')
print (f'El tipo de dato de la variable es {type(PEPE)}')

print (f'-' * 20)

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

variable8 = 'erick'
variable9 = 30

if (variable8.upper() == 'ERICK' and variable9 >= 30):
    print (f'Ambas condiciones se cumple')
else:
    print (f'Error, al menos una de las condiciones no se cumplen')

if (variable9 <= 20 or variable8 == 'josue'):
    print (f'Correcto, al menos una condcion se cumple')
else:
    print (f'Error, no se cumple ninguna de las condiciones')

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Sumatoria2(1, 2, 3, 4)
        self.Classified = True

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')

Objeto30 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Ash")], 'Kanto', Objeto1.Nombre)
Objeto31 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Brooke")], 'Alolah', Objeto2.Nombre)
Objeto32 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")], 'Paldea', Objeto3.Nombre)

Objeto31.Desplegar()

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

print (f'-' * 20)

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'El elemento en la posicion {indice} es {elemento}')

variable10 = 'eSteBAN'
letra_variable10 = variable10[0]

print (f'{variable10}')
print (f'{variable10.lower()}')
print (f'{variable10.upper()}')
print (f'{variable10.capitalize()}')

print (f'{variable10.lower().find("t")}')
print (f'{variable10.lower().index("b")}')

print (f'{variable10.lower().startswith(letra_variable10)}')
print (f'{variable10.lower().endswith("n")}')

print (f'En la cadena de texto la letra {letra_variable10} aparece un total de {variable10.lower().count(letra_variable10)} veces')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = 'esto es un texto cualquiera para probar que la mica funciona'

Lista_variable11 = variable11.split(' ')

for elemento in Lista_variable11:
    print (f'{elemento}')

print (f'La lista tiene un total de {len(Lista_variable11)} palabras')

variable12 = '26'

if (variable12.isalpha()):
    print (f'Lo ingresado es texto')
else:
    print (f'Lo ingresado no es texto')

variable13 = 2.4

if (isinstance(variable13, float)):
    print (f'Lo ingresado es un decimal')
else:
    print (f'Error, lo ingresado no es un decimal')

variable14 = '36.4'

if (variable14.isnumeric()):
    print (f'La mica es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')

variable15 = 'texto123'

if (variable15.isalnum()):
    print (f'El texto tiene letras o numeros')
else:
    print (f'Error, formato incorrecto')

variable16 = ' e'

if (variable16.isspace()):
    print (f'Esto es un espacio nada mas')
else:
    print (f'Error, es mas que solo espacios')

variable17 = 'eSteBAN'

if (variable17.lower().islower()):
    print (f'Correcto, la mica esta en minuscula')
else:
    print (f'Error')

if (variable17.upper().isupper()):
    print (f'Correcto, la mica esta en mayuscula')
else:
    print (f'Error')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

for elemento in Diccionario1:
    print (f'{Diccionario1[elemento]}')

print (f'-' * 20)

for elemento in Diccionario1.keys():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario1.values():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario1.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1

print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Animales)):
    if (PEPE.Lista_Animales[Contador] == 'Salamandra'):
        print (f'En China se comen estos bichos')
        break
    else:
        Contador+= 1
        continue

print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1

print (f'-' * 20)

for elemento1, elemento2 in zip(Set_Conjunto_Menu1, PEPE.Tupla_Poke):
    print (f'{elemento1} -- {elemento2}')

for elemento in range(5):
    print (f'{elemento}')

print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')

Lista_Numeros_Mult = [num  * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Numero_Mayor = max(Lista_Numeros_Mult)
Numero_Menor = min(Lista_Numeros_Mult)
Redondeado = round(14.458795, 2)
Sumatoria4 = sum(Lista_Numeros_Mult)

print (f'{bool(not True)}')
print (f'{bool(False)}')
print (f'{bool(0)}')
print (f'{bool("")}')
print (f'{bool(None)}')

Todo_All = all([Lista_Numeros_Mult, Set_Conjunto_Menu1, Tupla2, None])

print (f'{Todo_All}')

Uno = int('500')
Dos = str(500)
Tres = float(Dos)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')

print (f' - '.join(PEPE.Set_Conjunto_Poke))

print (f'-' * 20)

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

print (f'-' * 20)

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

'''def Floating1(Elemento):
    print (f'El resultado de la operacion es {Elemento * Variable_Sumatoria + Sumatoria2(1, 2, 3, 4, 5)}')

Floating1(PEPE.Flotante1())

Resultado2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado2}')

def Floating3(Elemento):
    if (Elemento.replace(' ', '').isalpha()):
        print (f'Gracias {Elemento}, lo que ingresaste es correcto')
    else:
        print (f'Error, necesito que ingreses un texto')

Floating3(PEPE.Flotante3)

def Floating4(Cadena):
    Lista_Cadena = Cadena.split(' ')
    for indice, elemento in enumerate(Lista_Cadena):
        print (f'El elemento en la posicion {indice} es {elemento}')

    print (f'Cantidad de palabras digitadas: {len(Lista_Cadena)}')

Floating4(PEPE.Flotante4)'''

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento}: ')
        Lista.append(Alumno)

    return Lista

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nLa lista de estudiantes es {Colegio(Lista_Alumnos)}'])
    Docu.close()

with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()'''

Texto8 = "   Hola!!!   mundo@@   123   "

print (f'{Texto8}')

Texto8_Version1 = Texto8.lower()

print (f'{Texto8_Version1}')

Texto8_Version2 = Texto8_Version1.strip()

print (f'{Texto8_Version2}')

Texto8_Version3 = ' '.join(Texto8_Version2.split())

print (f'{Texto8_Version3}')

import re

Texto8_Version4 = re.sub(r'[^a-z0-9\s]', '', Texto8_Version3)

print (f'{Texto8_Version4}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv6 = 'C:\\Repo\\Store.csv'

Cargar_Csv6 = pd.read_csv(Ruta_Csv6)

print (f'{Cargar_Csv6}')

print (f'-' * 20)

Fecha5 = '2026-04-01'

try:
    Fech5 = datetime.strptime(Fecha5, '%Y-%m-%d').date()
    Fech5_Formateada = pd.to_datetime(Fech5)
    Cargar_Csv6['date'] = pd.to_datetime(Cargar_Csv6['date'])
except ValueError:
    print (f'Error, formato de fecha incorrecto')
    exit()

Encontrado5 = Cargar_Csv6[Cargar_Csv6['date'].dt.date == Fech5_Formateada.date()]

if (Encontrado5.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! hemos encontrado ventas en esta fecha')
    Grupo5 = Encontrado5.groupby('product')['quantity'].sum()
    Grupo5_May = Grupo5.idxmax()
    Grupo5_Min = Grupo5.idxmax()
    Grupo5_May_Cant = Grupo5.max()
    Grupo5_Min_Cant = Grupo5.min()

    print (f'En la fecha {Fech5_Formateada} el producto {Grupo5_May} vendio un total de {Grupo4_May_Cant} unidades')
    print (f'En la fecha {Fech5_Formateada} el producto {Grupo5_Min} vendio un total de {Grupo5_Min_Cant} unidades')

C = {1, 2, 3, 4}
D = set({3, 4, 5, 6})

print (f'{C.union(D)}')
print (f'{C | D}')

print (f'-' * 20)

print (f'{C.intersection(D)}')
print (f'{C & D}')

print (f'-' * 20)

print (f'{C.difference(D)}')
print (f'{C - D}')

print (f'-' * 20)

print (f'{D.difference(C)}')
print (f'{D - C}')

print (f'-' * 20)

print (f'{A.symmetric_difference(B)}')
print (f'{A ^ B}')

print (f'-' * 20)

E = {1, 2, 3, 4, 5}
F = set({4, 5})
G = set({8})

print (f'{E.issuperset(F)}')
print (f'{E >= F}')

print (f'-' * 20)

print (f'{F.issubset(E)}')
print (f'{F <= E}')

print (f'-' * 20)

print (f'{E.isdisjoint(G)}')

'''C.update(D)

print (f'{C}')'''

'''C.intersection_update(D)

print (f'{C}')'''

'''C.difference_update(D)

print (f'{C}')'''

C.symmetric_difference_update(D)

print (f'{C}')

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio2(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del estudiante {elemento}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)

    Lista.sort(key = lambda Num : Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]

    print (f'El estudiante menor es {Menore} - ({Lista[0][1]})')
    print (f'El estudiante mayor es {Mayore} - ({Lista[-1][1]})')

Colegio2(Lista_Alumnos)'''

'''def Finale():
    while True:
        numero = input(f'Ingrese un numero entero: ')
        try:
            numerito = int(numero)
            return numerito
        except:
            print(f'Error, necesito que ingreses un numero entero')

print (f'Gracias, el numero ingresado es {Finale()}')'''

import pandas as pd
import requests
import io

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html2 = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Leer_Html2)

print (f'{Cargar_Html2[2].head()}')

print (f'-' * 20)

import re

Correo3 = 'example@example.com'

Pattern2 = r'^[a-zA-Z0-9./*-+]+\@[a-zA-Z0-9]+\.(com|org|net)$'

Buscar17 = bool(re.match(Pattern2, Correo3))

if (Buscar17):
    print (f'El formato del correo es correcto')
else:
    print (f'Error, el formato del correo es incorrecto')

Numero2 = '06'

Pattern3 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar18 = bool(re.match(Pattern3, Numero2))

if (Buscar18 == True):
    print (f'El numero esta entre 1 y 31')
else:
    print (f'El numero esta fuera de rango')


print (f'{Cargar_Csv6}')

Cargar_Csv6['PANDITA'] = Cargar_Csv6['quantity'] * Cargar_Csv6['price']

print (f'-' * 20)

print (f'{Cargar_Csv6}')





