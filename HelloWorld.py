import fontTools.tfmLib
import numpy as np

try:
    import Module_Own as PEPE
except ImportError:
    print (f'El modulo elegido es incorrecto')

from Module_Own import Pokemon1 as Poke

class Poke_Kid1(Poke):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto1 = Poke(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto2 = Poke_Kid1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Acero')
Objeto3 = Poke(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro')

Objeto2.Mostrar()

print (f'-' * 20)

Poke.Mostrar(Objeto2)
Objeto2.Mostrar()

print (f'-' * 20)

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
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')

Objeto4 = Perro('Chester', 5, 2.5, 'Poodle', 'Asma')

Mascota.Mostrar(Objeto4)
Objeto4.Mostrar()

print (f'-' * 20)

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

Objeto5 = Gato('Messi', 1.5, 1.2, 'Angora', 'Gris', 'No')

Mascota.Mostrar(Objeto5)
Objeto5.Mostrar()

print (f'-' * 20)

class Pajaro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto6 = Pajaro('Polly', 31, 0.4, 'Cacatua Amarilla', 'Si')

Mascota.Mostrar(Objeto6)
Objeto6.Mostrar()

print (f'-' * 20)

class Atacante():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon

    def Mostrar(self):
        print (f'Damage: {self.Damage}pts')
        print (f'Weapon: {self.Weapon}')

class Defensor:
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life

    def Mostrar(self):
        print (f'Healing: {self.Healing}pts')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}pts')

class Paladin(Atacante, Defensor):
    def __init__(self, Damage, Weapon, Healing, Potion, Life, Name):
        Atacante.__init__(self, Damage, Weapon)
        Defensor.__init__(self, Healing, Potion, Life)
        self.Name = Name

    def Mostrar(self):
        print (f'Name: {self.Name}')

Objeto7 = Paladin(75, 'Battle Axe', 25, 'Black Lagoon', 200, 'Ghost Knight')

Objeto7.Mostrar()
Atacante.Mostrar(Objeto7)
Defensor.Mostrar(Objeto7)

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

Objeto8 = D()

A.Mostrar(Objeto8)
B.Mostrar(Objeto8)
C.Mostrar(Objeto8)
Objeto8.Mostrar()
E.Mostrar(Objeto8)

print (f'-' * 20)

class Efectivo():
    def Pagar(self):
        print (f'El pago se realizo con Efectivo')

class Tarjeta:
    def Pagar(self):
        print (f'El pago se realizo con Tarjeta')

class Cripto:
    def Pagar(self):
        print (f'El pago se realizo con Cripto')

Objeto9 = Cripto()
Objeto10 = Tarjeta()
Objeto11 = Efectivo()

Objeto9.Pagar()
Objeto10.Pagar()
Objeto11.Pagar()

print (f'-' * 20)

class CuentaBancaria:
    def __init__(self, Saldo):
        self.__Saldo = Saldo

    def Depositar(self, Dinero):
        self.__Saldo += Dinero

    @property
    def Dinero(self):
        return self.__Saldo

    @Dinero.setter
    def Dinero(self, New_Saldo):
        self.__Saldo = New_Saldo

    def Mostrar(self):
        print (f'Su saldo a la fecha es de ${self.__Saldo}')

Objeto11 = CuentaBancaria(100)
Objeto11.Depositar(25)
Objeto11.Mostrar()

print (f'El saldo privado es de {Objeto11.Dinero}')

Objeto11.Dinero = '20,000'

Objeto11.Mostrar()

print (f'El saldo privado es de {Objeto11.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def Obligatoria(self):
        pass

class Ejemplo1(Plantilla):
    def Mostrar(self):
        print (f'Hola Mundo')

    def Obligatoria(self):
        print (f'Hola Ejemplo Abstraccion')

Objeto12 = Ejemplo1()

Objeto12.Mostrar()
Objeto12.Obligatoria()

class Uno:
    def Mensajear(self):
        print (f'El mensaje de Uno aparece en Dos')

class Dos():
    def __init__(self):
        self.Mensaje = Uno()

    def Mostrar(self):
        self.Mensaje.Mensajear()

Objeto13 = Dos()

Objeto13.Mostrar()

print (f'-' * 20)

import re

Texto1 = 'este es hola un 15 texto de ejemplo hela 250 @ para probar que la hala 1000 mica sirve'

Buscar1 = re.search('para', Texto1)

print (f'{Buscar1}')

Buscar2 = re.findall('e', Texto1)

print (f'{Buscar2}')

Buscar3 = re.fullmatch('este es hola un 15 texto de ejemplo hela 250 para probar que la hala 1000 mica sirve', Texto1)

print (f'{Buscar3}')

Buscar4 = re.findall(r'\d{1}', Texto1)

print (f'{Buscar4}')

Buscar5 = re.findall('h.la', Texto1)

print (f'{Buscar5}')

Buscar6 = re.findall(r'(texto|250)', Texto1)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\d{3}\s{1}\W{1}', Texto1)

print (f'{Buscar7}')

Buscar8 = re.findall(r'[ar]{2,4}', Texto1)

print (f'{Buscar8}')

Buscar9 = re.findall(r'[0-9]{2,4}', Texto1)

print (f'{Buscar9}')

Telefono1 = 'sample@hotmail.org'

Pattern1 = r'^[a-zA-Z0-9./*-+=_-]+\@(hotmail|gmail|yahoo)\.(com|net|org)$'

Buscar10 = bool(re.fullmatch(Pattern1, Telefono1))

if (Buscar10 == True):
    print (f'El formato del correo es correcto')
else:
    print (f'El formato del correo es incorrecto')

Fecha = 'Necesito confirmar que la siguiente fecha 12/29/2026 tiene el formato correcto'

Pattern2 = r'[0-9]{2}\/[0-9]{2}\/[0-9]{4}'

Replacement = 'xx/xx/xxxx'

Buscar11 = re.sub(Pattern2, Replacement, Fecha)

print (f'{Buscar11}')

print (f'-' * 20)

Buscar12 = re.findall(r'(0[1-9]|[12][0-9]|3[01])', '32')

print (f'{Buscar12}')

Buscar13 = bool(re.match(r'(0[0-9]|[12][0-9]|3[01])', '32'))

if (Buscar13 == True):
    print (f'El numero se encuentra entre 00 y 31')
else:
    print (f'Error, no se encuentra en el rango definido')

def Exception1(Elemento):
    try:
        Numerito = int(Elemento)
        print (f'El elemento es un numero {Numerito}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Exception1("Hola")

def Exception2(Num1, Num2):
    try:
        Resultado = Num1 + Num2
        print (f'El resultado de la operacion es {Resultado}')
    except TypeError:
        print (f'Error, ambos elementos deben ser numeros')

Exception2(12, "Hola")

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser un numero')

Exception3(12, 0)

Lista_Exception4 = list(['Erick', 'Josue', 'Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento en la posicion {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, El indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = {
    'Nombre' : "Erick",
    'Edad' : 37
}

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave seleccionada esta fuera de rango')

Exception5('Votante')

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

try:
    with open('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Durazno')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')

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
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [55, 14, 26],
    'Votante' : [True, False, not False]
})

Data_Frame_Concatenate = pd.concat([Data_Frame1, Data_Frame2])

print (f'{Data_Frame_Concatenate}')

print (f'-' * 20)

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame_Concatenate_Age}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

print (f'El numero menor del dataframe es {Data_Frame_Concatenate_Age.min()} y el mayor de los numeros es {Data_Frame_Concatenate_Age.max()}')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombrecito = elemento['Nombre']

    print (f'Mi nombre es {Nombrecito}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv1 = 'C:\\Repo\\Store.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

Group1 = Cargar_Csv1.groupby('product')['quantity'].sum()

Group1_May = Group1.idxmax()
Group1_Min = Group1.idxmin()
Group1_May_Cant = Group1.max()
Group1_Min_Cant = Group1.min()

print (f'El producto menos vendido fue ({Group1_Min}) con un total de {Group1_Min_Cant} unidades y el producto mas vendido fue ({Group1_May}) con un total de {Group1_May_Cant} unidades')

'''import pandas as pd
import matplotlib.pyplot as plt

x = list([1, 2, 3, 4])
y = [45, 77, 20, 95]

plt.figure(figsize=(4,3))
plt.plot(x, y)

plt.title("Ventas")
plt.xlabel("Día")
plt.ylabel("Cantidad")

plt.show()

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

print (f'-' * 20)

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
Elemento2 = Data_Frame1.loc[1, 'Edad']
Elemento3 = Data_Frame1.loc[2, 'Votante']
Elemento4 = Data_Frame1.loc[:, 'Nombre']
Elemento5 = Data_Frame1.loc[2, :]

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')
print (f'{Elemento4}')
print (f'{Elemento5}')

print (f'-' * 20)

Elemento6 = Data_Frame2.iloc[0, 0]
Elemento7 = Data_Frame2.iloc[1, 1]
Elemento8 = Data_Frame2.iloc[2, 2]
Elemento9 = Data_Frame2.iloc[1, :]
Elemento10 = Data_Frame2.iloc[:, 0]

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')
print (f'{Elemento9}')
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
Cargar_Excel3 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, index_col='tiquete')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:K', index_col='tiquete')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:K', index_col='tiquete', nrows=1)

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

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'-' * 20)

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

import pandas as pd

Ruta_Txt2 = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt2 = pd.read_csv(Ruta_Txt2)

print (f'{Cargar_Txt2.head()}')

print (f'-' * 20)

print (f'{Cargar_Txt2}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv2 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2.head()}')

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

Lista_Array1 = [[1, 2, 3], [4, 5, 6]]

print (f'{Lista_Array1[1][2]}')
print (f'{Lista_Array1[1][:2]}')
print (f'{Lista_Array1[1][2:]}')
print (f'{Lista_Array1[0][::2]}')
print (f'{Lista_Array1[1][::3]}')
print (f'{Lista_Array1[1][2:3]}')
print (f'{Lista_Array1[0][0:None]}')
print (f'{Lista_Array1[0][:]}')

print (f'-' * 20)

Lista_Array2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(Lista_Array2)):
    for j in range(len(Lista_Array2[i])):
        print (f'{Lista_Array2[i][j]}')

print (f'-' * 20)

for Fila in Lista_Array2:
    for Elemento in Fila:
        print (f'{Elemento}')

print (f'-' * 20)

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

print (f'-' * 20)

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 0]}')

print (f'{Array2[0, :2]}')
print (f'{Array2[0, 2:]}')
print (f'{Array2[1, ::2]}')
print (f'{Array2[0, ::3]}')
print (f'{Array2[1, 1:2]}')
print (f'{Array2[:, 1]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[0, :]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[0, 0:None])
Sumita4 = np.sum(Array2_Sorted[0, :])

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

print (f'El resultado de la sumita es {Sumita1}')
print (f'El resultado de la sumita es {Sumita2}')
print (f'El resultado de la sumita es {Sumita3}')
print (f'El resultado de la sumita es {Sumita4}')

print (f'-' * 20)

Array3 = np.array([[['e', 's', 'u'], ['d', 'a', 'i']],              [['j', 'l', 'm'], ['n', 'o', 'r']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 2]}')

print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[1, 1, ::2]}')
print (f'{Array3[0, 1, ::3]}')
print (f'{Array3[1, 0, 1:2]}')
print (f'{Array3[0, :, 0]}')
print (f'{Array3[1, 0, 0:None]}')
print (f'{Array3[1, 0, :]}')
print (f'{Array3[Array3 == "a"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],          [[[6, 5, 4], [9, 8, 7]], [[4, 6, 7], [3, 1, 9]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') #  4
print (f'{Array4.shape}') #2x2x2x3
print (f'{Array4.size}') #24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 2]}')

print (f'{Array4[1, 0, 1, :2]}')
print (f'{Array4[1, 0, 1, 2:]}')
print (f'{Array4[1, 1, 0, ::2]}')
print (f'{Array4[0, 0, 1, ::3]}')
print (f'{Array4[0, 1, 0, 1:2]}')
print (f'{Array4[1, 0, :, 2]}')
print (f'{Array4[1, 0, 0, 0:None]}')
print (f'{Array4[1, 0, 0, :]}')
print (f'{Array4[Array4 <= 2]}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_May = np.max(Array_Num1)
Array_Min = np.min(Array_Num1)

print (f'El menor de los numeros es {Array_Min} y el mayor es {Array_May}')

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

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 2]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 1]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[0, 0]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[3]}')

Lista_Array3 = list([])

for elemento in Array_Gen2:
    Lista_Array3.append(str(elemento))

print (f'{Lista_Array3}')
print (f'{type(Lista_Array3)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value=Array4[1, 0, 1, 2])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 1]}')

print (f'-' * 20)

Tupla_Array = ('Rojo', 'Verde')
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value = Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value = Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value = Diccionario_Array['Nombre'][1])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

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

Array_Random1 = np.random.randint(low=1, high=10, size=(5))

print (f'{Array_Random1}')

print (f'-' * 20)

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

print (f'Ordenado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

Sumita5 = np.sum(Array_Random2_Sorted, axis=0)
Sumita6 = np.sum(Array_Random2_Sorted, axis=1)
Sumita7 = np.sum(Array_Random2_Sorted[1, 0:None])
Sumita8 = np.sum(Array_Random2_Sorted[1, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

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

Array_Num8 = np.arange(start=1, stop=21, step=1)

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Lista_Array4 = list(['Erick', 'Josue', 'Karlita'])

Array5 = np.array(Lista_Array4)

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

Lista_Array5 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print (f'{Lista_Array5[2][0:None]}')

for i in range(len(Lista_Array5)):
    for j in range(len(Lista_Array5[i])):
        print (f'{Lista_Array5[i][j]}')

print (f'-' * 20)

for Fila in Lista_Array5:
    for Elemento in Fila:
        print (f'{Elemento}')

print (f'-' * 20)

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'-' * 20)

for Matriz1 in Array3:
    for Fila in Matriz1:
        print (f'{Fila}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Sumita9 = np.sum(Array_Random3, axis=0)
Sumita10 = np.sum(Array_Random3, axis=1)
Sumita11 = np.sum(Array_Random3[1, 0, 0:None])
Sumita12 = np.sum(Array_Random3[1, 0, :])

print (f'{Sumita9}')
print (f'{Sumita10}')
print (f'{Sumita11}')
print (f'{Sumita12}')

print (f'-' * 20)

Lista_Ganador = ['Erick', 'Josue']
Lista_Ganador.append('Karlita')
Lista_Ganador.insert(0, 'Carmelo')
Lista_Ganador.extend(['Roxana', 'Susanita'])

Ganador1 = np.random.choice(Lista_Ganador, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Ganador, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Ganador, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-' * 20)

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-' * 20)

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
    print (f'El experimento termina aqui')

print (f'-' * 20)

def Generadora2():
    for elemento in range(0, 5):
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
    print (f'El experimento termina aqui')

print (f'-' * 20)

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
    print (f'El experimento termina aqui')

print (f'-' * 20)

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
    Documento_Agregar = Docu.writelines([f'\nSu contrasena temporal es {PEPE.Contrasena(44)}'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.5, 200, True)

print (f'{Funcion_Tupla("Perro", 3.5, 200, True)}')
print (f'{Funcion_Tupla("Perro", 3.5, 200, True)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.5, 200, True))}')

print (f'-' * 20)

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')

Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

print (f'Los numeros pares de la lista son {PEPE.Lista_Par} o incluso podrian ser {list(Anonima3)}')

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
print (f'{Variable_Closure(28)}')
print (f'{Variable_Closure(34)}')

def Crear_Multiplicador(x):
    def Multiplicador(y):
        return x * y

    return Multiplicador

Mult1 = Crear_Multiplicador(2)
Mult2 = Crear_Multiplicador(3)

print (f'El multiplicador es {Mult1(10)}')
print (f'El multiplicador es {Mult2(10)}')

def Filtrador(Lista):
    Any_Impar = any(num % 2 == 0 for num in Lista)
    if (Any_Impar == True):
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impar = [num for num in Lista if num % 2 != 0]

        print (f'Los numeros impares de la lista son {Lista_Impar} o incluso podrian ser {list(Anonima4)}')
    else:
        print (f'Error, no hay elementos impares en la lista')

Filtrador(PEPE.Lista_Numeros)

def Primera(Segunda):
    def Tercera():
        print (f'COMIENZA AQUI')
        Segunda()
        print (f'TERMINA AQUI')

    return Tercera

@Primera
def Saludar4():
    print (f'Hola Mundo')

Saludar4()

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 1

    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
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

print (f'-' * 20)

from Module_Own import Pokemon2 as Poke2

Objeto14 = Poke2(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')

Objeto14.Mostrar()

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto15 = Poke_Kid2(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Acero')

Poke2.Mostrar(Objeto15)
Objeto15.Mostrar()

print (f'-' * 20)

class Camara():
    def Tomar_Fotografia(self):
        print (f'Fotografia Tomada')

class Reproductor:
    def Reproducir_Musica(self):
        print (f'Musica Reproducida')

class SmartPhone(Camara, Reproductor):
    def Encender_Smartphone(self):
        print (f'Smartphone Encendido')

Objeto16 = SmartPhone()

Objeto16.Encender_Smartphone()
Objeto16.Reproducir_Musica()
Objeto16.Tomar_Fotografia()

print (f'-' * 20)

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
        print (f'Visitas: {self.Visitas}')

Objeto17 = Perro('Chester', 5, 2.8, 'Poodle', 'Asma', 3)

Mascota.Mostrar(Objeto17)
Objeto17.Mostrar()

print (f'-' * 20)

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

Objeto18 = Gato('Messi', 1.5, 1.8, 'Angora', 'Gris', 'No')

Mascota.Mostrar(Objeto18)
Objeto18.Mostrar()

print (f'-' * 20)

class Pajaro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto19 = Pajaro('Polly', 31, 0.4, 'Cacatua Amarilla', 'Si')

Mascota.Mostrar(Objeto19)
Objeto19.Mostrar()

print (f'-' * 20)

class Atacante():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon

    def Mostrar(self):
        print (f'Damage: {self.Damage}pts')
        print (f'Weapon: {self.Weapon}')

class Defensor:
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life

    def Mostrar(self):
        print (f'Healing: {self.Healing}pts')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}pts')

class Paladin(Atacante, Defensor):
    def __init__(self, Damage, Weapon, Healing, Potion, Life, Name):
        Atacante.__init__(self, Damage, Weapon)
        Defensor.__init__(self, Healing, Potion, Life)
        self.Name = Name

    def Mostrar(self):
        print (f'Name: {self.Name}')

Objeto20 = Paladin(75, 'Battle Axe', 25, 'Red Velvet', 200, 'Ghost Knight')

Objeto20.Mostrar()
Atacante.Mostrar(Objeto20)
Defensor.Mostrar(Objeto20)

print (f'-' * 20)

Children_Parent = issubclass(Poke_Kid2, Poke2)

print (f'{Children_Parent}')

Clase_Objeto1 = isinstance(Objeto20, Atacante)
Clase_Objeto2 = isinstance(Objeto20, Defensor)
Clase_Objeto3 = isinstance(Objeto20, Paladin)

print (f'{Clase_Objeto1}')
print (f'{Clase_Objeto2}')
print (f'{Clase_Objeto3}')

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

Objeto21 = D()

A.Mostrar(Objeto21)
B.Mostrar(Objeto21)
C.Mostrar(Objeto21)
Objeto21.Mostrar()
E.Mostrar(Objeto21)

print (f'-' * 20)

class Efectivo():
    def Pagar(self):
        print (f'El pago se realizo en efectivo')

class Tarjeta:
    def Pagar(self):
        print (f'El pago se realizo en tarjeta')

class Cripto:
    def Pagar(self):
        print (f'El pago se realizo en crito')

Objeto22 = Cripto()
Objeto23 = Tarjeta()
Objeto24 = Efectivo()

Objeto22.Pagar()
Objeto23.Pagar()
Objeto24.Pagar()

print (f'-' * 20)

class Cuenta_Bancaria():
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
        print (f'Su saldo a la fecha es de ${self.__Saldo}')

Objeto25 = Cuenta_Bancaria(100)
Objeto25.Depositar(25)
Objeto25.Mostrar()

print (f'Tu saldo privado es de {Objeto25.Dinero}')

Objeto25.Dinero = '20,000'

Objeto25.Mostrar()

print (f'Tu saldo privado es de {Objeto25.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def Borrador(self):
        pass

class Ejemplo1(Plantilla):
    def Mostrar(self):
        print (f'Este es un segundo metodo de la abstraccion')

    def Borrador(self):
        print (f'Aqui se muestra la abstraccion')

Objeto26 = Ejemplo1()

Objeto26.Mostrar()
Objeto26.Borrador()

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un
Long
String'''

variable4 = Variable_Sumatoria
variable5 = PEPE.Division_Flotante
variable6, variable7 = not False, Objeto1.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')

print (f'Mi nombre completo es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Variable_Sumatoria}, {Sumatoria2(1, 2, 3, 4, 5)} o incluso {Objeto3.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Josue' in Lista_Uno)
print (f'Misty' in PEPE.Tupla_Poke)
print (f'Pikachu' in PEPE.Set_Conjunto_Poke)
print (f'Poke3' in PEPE.Diccionario_Poke)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un snake case y al mismo tiempo un desempaquetado de variables: {snake_case3}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto2.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Rango de elementos {PEPE.Lista2[1:2]}')
print (f'Rango de elementos {PEPE.Lista2[:2]}')
print (f'Rango de elementos {PEPE.Lista2[2:]}')
print (f'Rango de elementos {PEPE.Lista2[::2]}')
print (f'Rango de elementos {PEPE.Lista2[::3]}')
print (f'Rango de elementos {PEPE.Lista2[0:None]}')
print (f'Rango de elementos {PEPE.Lista2[:]}')

print (f'{Lista_Uno[0]} eso que esta ahi es un {PEPE.Lista2[2]}?')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, Anonima1(150, 2))

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

Tupla1 = ('Rojo', 'Verde', 'Verde', 'Verde', 'Verde')

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Green'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'Un elemento de la tupla es {Tupla1[1]}')

Set_Conjunto1 = {'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo'}
Set_Conjunto1.add('Black')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Red', 'Black'})
Set_Conjunto1.add('Blue')

print (f'{Set_Conjunto1}')

Set_Conjunto2 = {1, 2, 3, 4, 5}
Set_Conjunto3 = {4, 5}
Set_Conjunto4 = set({8})

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')

A = {1, 2, 3, 4}
B = set({3, 4, 5, 6})

print (f'{A.union(B)}')

print (f'{A|B}')

print (f'{A.intersection(B)}')

print (f'{A&B}')

print (f'{A.difference(B)}')
print (f'{B.difference(A)}')

print (f'{A - B}')
print (f'{B - A}')

print (f'{A.issuperset(B)}')
print (f'{B.issubset(B)}')
print (f'{A.isdisjoint(B)}')

print (f'{A.symmetric_difference(B)}')
print (f'{A ^ B}')

print (f'-' * 20)

C = {1, 2, 3}
D = {3, 4}

C.difference_update(D)

print (f'{C}')

C.update(D)

print (f'{C}')

C.intersection_update(D)

print (f'{C}')

C.symmetric_difference_update(D)

print (f'{C}')

print (f'-' * 20)

Set_Conjunto5 = {1, 2, 3, 4}
Set_Conjunto6 = set({3, 4, 5, 6})

print (f'La union de ambos sets es {Set_Conjunto5.union(Set_Conjunto6)}')
print (f'La union de ambos sets es {Set_Conjunto5 | Set_Conjunto6}')

print (f'Mostrando solo lo que tienen en comun ambos sets {Set_Conjunto5.intersection(Set_Conjunto6)}')
print (f'Mostrando solo lo que tienen en comun ambos sets {Set_Conjunto5 & Set_Conjunto6}')

print (f'Los elementos que no tienen en comun los sets son {Set_Conjunto5.difference(Set_Conjunto6)}')
print (f'Los elementos que no tienen en comun los sets son {Set_Conjunto6.difference(Set_Conjunto5)}')

print (f'Los elementos que no tienen en comun los sets son {Set_Conjunto5 - Set_Conjunto6}')
print (f'Los elementos que no tienen en comun los sets son {Set_Conjunto6 - Set_Conjunto5}')

print (f'Los elementos que son diferentes son {Set_Conjunto5.symmetric_difference(Set_Conjunto6)}')
print (f'Los elementos que son diferentes son {Set_Conjunto5 ^ Set_Conjunto6}')

Set_Conjunto7 = {1, 2, 3, 4, 5}
Set_Conjunto8 = {4, 5}
Set_Conjunto9 = set({8})

print (f'{Set_Conjunto7.issuperset(Set_Conjunto8)}')
print (f'{Set_Conjunto7 >= Set_Conjunto8}')
print (f'-' * 20)
print (f'{Set_Conjunto8.issubset(Set_Conjunto7)}')
print (f'{Set_Conjunto8 <= Set_Conjunto7}')
print (f'-' * 20)
print (f'{Set_Conjunto7.isdisjoint(Set_Conjunto9)}')
print (f'-' * 20)

'''Set_Conjunto6.update(Set_Conjunto7)

print (f'Set actualizado {Set_Conjunto6}')'''

'''Set_Conjunto6.intersection_update(Set_Conjunto7)

print (f'Set actualizado {Set_Conjunto6}')'''

Set_Conjunto6.difference_update(Set_Conjunto7)
Set_Conjunto7.difference_update(Set_Conjunto6)

print (f'Set actualizado {Set_Conjunto6}')
print (f'Set actualizado {Set_Conjunto7}')

Set_Conjunto_Menu1 = {'Chocolate', 'Fresa'}
Set_Conjunto_Menu1.add('Vainilla')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})

print (f'{Set_Conjunto_Menu1.union(Set_Conjunto_Menu2)}')

Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, Objeto1.Nombre})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Nuevo_Set_Menu = list(Set_Conjunto_Menu1.union(Set_Conjunto_Menu2))

print (f'{Nuevo_Set_Menu}')
print (f'{type(Nuevo_Set_Menu)}')

for indice, elemento in enumerate(Nuevo_Set_Menu, start=1):
    print (f'El elemento en la posicion {indice} es {elemento}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Variable_Sumatoria,
    'Votante' : Variable_Funcion_Tupla[3]
}

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1["Nombre"]}')
print (f'{Diccionario1.get("Edad")}')

print (f'-' * 20)

Diccionario2 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [18 * 2, 20, 6],
    'Votante' : [True, not False, False]
}

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2["Nombre"][1]}')
print (f'{Diccionario2.get("Edad")[2]}')

print (f'-' * 20)

Diccionario3 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3["Ingresos"]}')
print (f'{Diccionario3.get("Gastos")}')

print (f'-' * 20)

print (f'Un elemento del diccionario 2 es {Diccionario2["Nombre"][2:3]}')

Diccionario1['Nombre'] = variable1

print (f'{Diccionario1}')

del Diccionario1['Nombre']
Diccionario1.pop("Edad")

print (f'{Diccionario1}')

print (f'-' * 20)

Diccionario1.clear()

print (f'{Diccionario1}')

Diccionario1 = dict({1 : "Karlita", 2 : 6, 3 : not True})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario2.get("Nombre")[2]} no puede votar ya que solo tiene {Diccionario1[2]} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', "HolaMundo")
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')

Key1 = [f'Key{i}' for i in range(len(Lista_Uno_Copia))]

Diccionario4 = dict(zip(Key1, Lista_Uno_Copia))

for elemento in Diccionario4.items():
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'-' * 20)

for elemento in Diccionario3.keys():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario3.values():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario3.items():
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

print (f'-' * 20)

Lista_Csv3 = set(Cargar_Csv3['product'])

print (f'{Lista_Csv3}')

Key2 = [f'Key{i}' for i in range(len(Lista_Csv3))]

print (f'{Key2}')

Diccionario5 = dict(zip(Key2, Lista_Csv3))

print (f'-' * 20)

for elemento in Diccionario5.keys():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario5.values():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario5.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Division_Flotante = PEPE.Division_Flotante
Division_Baja = 14//7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la operacion es {Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'El tipo de dato de la variable es {type(variable1)}')
print (f'El tipo de dato de la variable es {type(variable4)}')
print (f'El tipo de dato de la variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de dato de la variable es {type(Objeto3.Catched)}')

print (f'El tipo de dato de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato de la variable es {type(Tupla_Array)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu3)}')
print (f'El tipo de dato de la variable es {type(Diccionario_Vacio1)}')
print (f'El tipo de dato de la variable es {type(Funcion_Tupla)}')
print (f'El tipo de dato de la variable es {type(Array_Concatenate)}')
print (f'El tipo de dato de la variable es {type(Data_Frame_Concatenate)}')
print (f'El tipo de dato de la variable es {type(Objeto1)}')
print (f'El tipo de dato de la variable es {type(Poke_Kid1)}')
print (f'El tipo de dato de la variable es {type(PEPE)}')

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

if (variable8 == 'erick' and variable9 > 50):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una condicion no se cumple')

if (variable8 == 'josue' or variable9 > 50):
    print (f'Al menos una condicion se cumplen')
else:
    print (f'Error, ninguna de las condiciones se cumplen')

print (f'{dir(PEPE)}')

print (f'{help(PEPE)}')

print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Variable_Sumatoria
        self.Classified = not False

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')

Objeto27 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index('Ash')], 'Kanto', Objeto1.Nombre)
Objeto28 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index('Brooke')], 'Alolah', Objeto2.Nombre)
Objeto29 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index('Misty')], 'Paldea', Objeto3.Nombre)

Objeto28.Desplegar()

Negativo = -5

print (f'El numero positivo es {int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]
Anonima5 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)

print (f'{Any_Iterable}')
print (f'{Lista_Iterable}')
print (f'{list(Anonima5)}')

print (f'La version binaria del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, necesito que ingreses una cadena de texto')

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')

print (f'-' * 20)

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'El elemento en la posicion {indice} es {elemento}')

variable10 = 'eSteBAN'
variable10_letra = variable10[0]

print (f'{variable10}')
print (f'{variable10.lower()}')
print (f'{variable10.capitalize()}')
print (f'{variable10.upper()}')

print (f'{variable10.lower().find("t")}')
print (f'{variable10.lower().index("b")}')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'La letra {variable10_letra} aparece un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = 'esto es un texto cualquiera que quiero probar'

Lista_variable11 = variable11.split(' ')

for elemento in Lista_variable11:
    print (f'{elemento}')

print (f'la variable 11 tiene un total de {Lista_variable11.__len__()} palabras')

variable12 = '89'

if (variable12.replace(' ', '').isalpha() == True):
    print (f'Lo ingresado es un texto')
else:
    print (f'Error, lo ingresado no es un texto')

variable13 = '3.5'

try:
    float(variable13)
    print('Correcto')
except ValueError:
    print('Incorrecto')

variable14 = 35

try:
    int(variable14)
    print (f'Correcto, es un numero entero')
except ValueError:
    print (f'Incorrecto, necesito que ingreses un numero entero')

print (f'{PEPE.Tupla_Poke[2]} aparece en la posicion {PEPE.Tupla_Poke.index("Misty")}')

for elemento in Diccionario5.keys():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario5.values():
    print(f'{elemento}')

print(f'-' * 20)

for elemento in Diccionario5.items():
    print(f'{elemento[0]} -- {elemento[1]}')

print(f'-' * 20)

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1

Lista_Animales = []
Lista_Animales.append('Cocodrilo')
Lista_Animales.insert(1, PEPE.Lista2[2])
Lista_Animales.extend(['Avestruz', 'Escarabajo'])

print (f'{Lista_Animales}')

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Koala'):
        print (f'Este animal es australiano')
        break
    else:
        Contador+= 1
        continue

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1

for elemento1, elemento2 in zip(Lista_Animales, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')

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

print (f'El menor de los resultados es {Menor} y el mayor es {Mayor}')

print (f'El redondeo es {Redondeo}')

print (f'El resultado de la sumatoria es {Sumatoria4}')

print (f'{bool(False)}')
print (f'{bool("")}')
print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool(not True)}')

Todo_All = all([Lista_Uno_Copia, Tupla3, Set_Conjunto_Menu1, ""])

print (f'{Todo_All}')

Entero = int('500')
String = str(500)
Flotante = float(Entero)

print (f'{type(Entero)}')
print (f'{type(String)}')
print (f'{type(Flotante)}')

print (f'La llave es {" - ".join(Lista_Uno_Copia)}')

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

'''def Finale1(Numero):
    return Variable_Sumatoria * Objeto3.Cantidad + Numero

print (f'El resultado de la operacion es {Finale1(PEPE.Flotante1)}')

Resultado2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado2}')

def Finale3(Cadena):
    Lista_Cadena = Cadena.split(' ')
    for elemento in enumerate(Lista_Cadena):
        print (f'{elemento[0]} - {elemento[1]}')

    print (f'La cantidad de palabras digitadas es {len(Lista_Cadena)}')

Finale3(PEPE.Flotante3)

def Finale4(Textico):
    if (Textico.isalpha() == True):
        print (f'Exito, ingresaste un texto')
    else:
        print (f'Error, lo ingresado no es un texto')

Finale4(PEPE.Flotante4)

def Finale5(Decimal):
    try:
        float(Decimal)
        print (f'Genial, lo ingresado es un numero decimal')
    except ValueError:
        print (f'Error, lo ingresado no es un numero decimal')

Finale5(PEPE.Flotante5)

def Finale6(Numero):
    try:
        int(Numero)
        print (f'Genial, lo ingresado es un numero entero')
    except ValueError:
        print (f'Error, lo ingresado no es un numero entero')

Finale6(PEPE.Flotante6)'''

'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Estudiante = input(f'Ingrese el nombre del estudiante {elemento}: ')
        Lista.append(Estudiante)

    return Lista

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nLa lista de estudiantes es {Colegio(Lista_Alumnos)}'])
    Docu.close()

with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

Lista_Alumnos2 = []

Contador = int(input(f'Ingrese el numero de estudiantes: '))

def Colegio2(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del estudiante {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del estudiante {elemento}: '))

        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)

    Lista.sort(key=lambda Num :  Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]

    print (f'El menor de los estudiantes es {Menore} ({Lista[0][1]} años)')
    print (f'El mayor de los estudiantes es {Menore} ({Lista[-1][1]} años)')

Colegio2(Lista_Alumnos2)'''

'''def Exception_Finale():
    while True:
        Numero = input(f'Ingrese un numero entero: ')
        try:
            Numerito = int(Numero)
            break
        except:
            print (f'Error, el valor ingresado no es un numero entero, intente nuevamente')
    return Numerito

print (f'Gracias, tu numero digitado es {Exception_Finale()}')'''

import pandas as pd
import requests
import io

Ruta_Html2 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html2, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Leer_Html)

print (f'{Cargar_Html2[1].head()}')

import re

Correo1 = 'sample@hotmail.org'

Pattern3 = r'^[a-zA-Z0-9./*-+=_-]+\@(gmail|hotmail|yahoo)\.(com|net|org)$'

Buscar14 = bool(re.match(Pattern3, Correo1))

if (Buscar14 == True):
    print (f'Formato de correo electronico corecto')
else:
    print (f'El formato del correo electronico es incorrecto')

Numero = '32'

Pattern4 = r'0[0-9]|[12][0-9]|3[01]'

Buscar15 = bool(re.fullmatch(Pattern4, Numero))

if (Buscar15):
    print (f'El numero se encuentra entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')

from datetime import datetime

print (f'{Cargar_Csv3}')

Fecha = input(f'Ingrese una fecha con formato YY-MM-DD: ')

try:
    Fech = datetime.strptime(Fecha, '%Y-%m-%d').date()
    Fech_Formateada = pd.to_datetime(Fech)
    Cargar_Csv3['date'] = pd.to_datetime(Cargar_Csv3['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato incorrecto')
    exit()

Buscador = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech_Formateada.date()]

if (Buscador.empty):
    print (f'No hay ventas registradas en esta fecha')
else:
    print (f'Genial, ventas registradas')
    Grupo1 = Buscador.groupby('product')['quantity'].sum()
    Grupo1_Prod_Max = Grupo1.idxmax()
    Grupo1_Prod_Min = Grupo1.idxmin()
    Grupo1_Prod_Max_Cant = Grupo1.max()
    Grupo1_Prod_Min_Cant = Grupo1.min()

    print (f'Durante {Fech_Formateada} el producto que mas vendio fue {Grupo1_Prod_Max} con un total de {Grupo1_Prod_Max_Cant} unidades')
    print (f'Durante {Fech_Formateada} el producto que menos vendio fue {Grupo1_Prod_Min} con un total de {Grupo1_Prod_Min_Cant} unidades')

print (f'-' * 20)

Cargar_Csv3['Totales'] = Cargar_Csv3['quantity'] * Cargar_Csv3['price']

print (f'{Cargar_Csv3}')