try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado no existe')

from Module_Own import Pokemon as Poke

class Poke_Kid(Poke):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto1 = Poke_Kid(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno', 'Acero')
Objeto2 = Poke_Kid(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Fantasma')
Objeto3 = Poke_Kid(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Hada')

Poke.Mostrar(Objeto1)
Objeto1.Mostrar()

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

Objeto4 = Perro('Chester', 5, 2.6, 'Poodle', 'Asma')

Mascota.Mostrar(Objeto4)
Objeto4.Mostrar()

print (f'-' * 20)

class Gato(Mascota):
    def __init__(self, Nombre, Edad, Peso, Raza, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')

Objeto5 = Gato('Messi', 1.5, 1.8, 'Angora', 'Si')

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

Objeto6 = Pajaro('Polly', 31, 0.7, 'Cacatua Amarilla', 'Si')

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

Objeto7 = Paladin(75, 'Battle Axe', 25, 'Green Liquid', 200, 'Ghost Knight')

Objeto7.Mostrar()
Atacante.Mostrar(Objeto7)
Defensor.Mostrar(Objeto7)

print (f'-' * 20)

class Efectivo():
    def Pagar(self):
        print (f'El pago se realizo en efectivo')

class Tarjeta:
    def Pagar(self):
        print (f'El pago se realizo en tarjeta')

class Cripto:
    def Pagar(self):
        print (f'El pago se realizo en cripto')

Objeto8 = Cripto()
Objeto9 = Tarjeta()
Objeto10 = Efectivo()

Objeto8.Pagar()
Objeto9.Pagar()
Objeto10.Pagar()

print (f'-' * 20)

class Banking_Account():
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
        print (f'Tu saldo a la fecha es de ${self.__Saldo}')

Objeto11 = Banking_Account(100)
Objeto11.Depositar(25)
Objeto11.Mostrar()

print (f'El valor de la variable privada es {Objeto11.Dinero}')

Objeto11.Dinero = '35,0000'

Objeto11.Mostrar()

print (f'El valor de la variable privada es {Objeto11.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def Borrador(self):
        pass

class Ejemplo(Plantilla):
    def Mostrar(self):
        print (f'Hola Cualquiera')

    def Borrador(self):
        print (f'Esto es un ejemplo de abstraccion')

Objeto12 = Ejemplo()

Objeto12.Mostrar()
Objeto12.Borrador()

print (f'-' * 20)

class Uno():
    def Mostrando(self):
        print (f'Esto es un ejemplo de composicion')

class Dos():
    def __init__(self):
        self.Placeholder = Uno()

    def Mostrando_Finale(self):
        self.Placeholder.Mostrando()

Objeto13 = Dos()

Objeto13.Mostrando_Finale()

print (f'-' * 20)

import re

Texto1 = 'esto es 100 un! hola ejemplo cualquiera@ para baiaiai hela probar. el concepto 8 de haala expresiones 45 regulares'

Buscar1 = re.search('\d+', Texto1)

print (f'{Buscar1}')

Buscar2 = re.findall(r'\d+', Texto1)

print (f'{Buscar2}')

Buscar3 = re.findall(r'\D+', Texto1)

print (f'{Buscar3}')

Buscar4 = re.findall(r'\w+', Texto1)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\W+', Texto1)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\s', Texto1)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\S', Texto1)

print (f'{Buscar7}')

Buscar8 = re.findall(r'h.la', Texto1)

print (f'{Buscar8}')

Buscar9 = re.findall(r'[a,e,i]{2,}', Texto1)

print (f'{Buscar9}')

Buscar10 = re.findall(r'(ai){3,4}', Texto1)

print (f'{Buscar10}')

Buscar11 = re.findall(r'a{2}', Texto1)

print (f'{Buscar11}')

Buscar12 = re.findall(r'^esto', Texto1)
Buscar13 = re.findall(r'es$', Texto1)

print (f'{Buscar12}')
print (f'{Buscar13}')

Buscar14 = re.findall(r'hola', Texto1)

print (f'{Buscar14}')

Buscar15 = re.fullmatch('esto es 100 un! hola ejemplo cualquiera@ para baiaiai hela probar. el 123 @ concepto 8 de haala expresiones 45 regulares', Texto1)

print (f'{Buscar15}')

Buscar16 = re.findall(r'[0-9]*', Texto1)

print (f'{Buscar16}')

Buscar17 = re.findall(r'[0-9]{2,}', Texto1)

print (f'{Buscar17}')

Pattern1 = r'[0-9]{3}\s?\W'

Buscar18 = re.findall((r'[0-9]{3}\s+\W{1}'), Texto1)

print (f'{Buscar18}')

Texto2 = 'hola 125 este es mi nombre y mi numero'

Buscar19 = re.findall(r'[a-z]+|\d+', Texto2)

print (f'{Buscar19}')

Texto3 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern2 = r'[0-9]{2}\/\d{2}\/[0-9]{4}'

Reemplazar = 'XX/XX/XXXX'

Buscar20 = re.sub(Pattern2, Reemplazar, Texto3)

print (f'{Buscar20}')

Correo1 = 'sample@sample.com'

Pattern3 = r'^[a-zA-Z./*-+_-]+\@[a-zA-Z]+\.[a-z]{2,}$'

Buscar21 = bool(re.match(Pattern3, Correo1))

if (Buscar21 == True):
    print (f'El formato del correo es correcto')
else:
    print (f'El formato del correo es incorrecto')

def Exception1(Numero):
    try:
        Numerito = int(Numero)
        print (f'Gracias, el numero digitado es {Numerito}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Exception1("Hola")

def Exception2(Num1, Num2):
    try:
        Opera = Num1 + Num2
        print (f'El resultado de la operacion es {Opera}')
    except TypeError:
        print (f'Error, ambos elementos deben ser numeros')

Exception2(12, "Hola")

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(12, 0)

Lista_Exception4 = list(['Erick', 'Josue'])
Lista_Exception4.extend(['Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento con el indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, El indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = {
    'Nombre' : "Erick",
    'Edad' : 37
}

def Exception5(Llave):
    try:
        print (f'El elemento dentro de la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave seleccionada esta fuera de rango')

Exception5('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Elefante')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nCalamar'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nLeon')
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

print (f'{Data_Frame1}')

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'-' * 20)

print (f'{Data_Frame_Concatenate_Age}')

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()} y la mayor es {Data_Frame_Concatenate_Age.max()}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    nombrecito = elemento['Nombre']

    print (f'Mi nombre es {nombrecito}')

print (f'-' * 20)

Grupo1 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo1_Mayor = Grupo1.idxmax()
Grupo1_Menor = Grupo1.idxmin()
Grupo1_Mayor_Cant = Grupo1.max()
Grupo1_Menor_Cant = Grupo1.min()

print (f'Mayor {Grupo1_Mayor} - {Grupo1_Mayor_Cant}')
print (f'Mayor {Grupo1_Menor} - {Grupo1_Menor_Cant}')

'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'-' * 20)'''

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
Elemento5 = Data_Frame1.loc[1, :]

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')
print (f'{Elemento4}')
print (f'{Elemento5}')

print (f'-' * 20)

Elemento6 = Data_Frame2.iloc[0, 0]
Elemento7 = Data_Frame2.iloc[1, 1]
Elemento8 = Data_Frame2.iloc[2, 2]
Elemento9 = Data_Frame2.iloc[0, :]
Elemento10 = Data_Frame2.iloc[:, 2]

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')
print (f'{Elemento9}')
print (f'{Elemento10}')

print (f'-' * 20)

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'
Cargar_Excel = pd.read_excel(Ruta_Excel, engine='openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'-' * 20)

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve' 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tarifa')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols='E:I', index_col='tarifa')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols='E:I', index_col='tarifa', nrows=1)

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

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted}')

print (f'-' * 20)

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted_Descending}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate_Age}')

print (f'-' * 20)

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'-' * 20)

print (f'{Cargar_Txt.head()}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv1 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

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

Array0 = [[1, 2, 3], [4, 5, 6]]

print (f'Esto es un array con Listas: {Array0}')

print (f'Un elemento de la matriz con listas es {Array0[1][0]}')

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
print (f'{Array1[2:3]}')
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

print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[:, 1]}')
print (f'{Array2[0, 2:3]}')
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
Sumita3 = np.sum(Array2_Sorted[0, 0:None])
Sumita4 = np.sum(Array2_Sorted[0, :])

print (f'El resultado de la sumita es {Sumita1}')
print (f'El resultado de la sumita es {Sumita2}')
print (f'El resultado de la sumita es {Sumita3}')
print (f'El resultado de la sumita es {Sumita4}')

print (f'-' * 20)

Array3 = np.array([[['w', 'r', 'f'], ['a', 'k', 'j']],           [['o', 'u', 'b'], ['d', 'c', 'n']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 2]}')

print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[1, 1, 1:2]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "b"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],      [[[6, 5, 4], [9, 8, 7]], [[7, 5, 3], [2, 4, 9]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 2]}')

print (f'{Array4[1, 1, 0, :2]}')
print (f'{Array4[1, 1, 0, 2:]}')
print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[1, 0, 0, ::3]}')
print (f'{Array4[1, 1, :, 0]}')
print (f'{Array4[0, 0, 0, 2:3]}')
print (f'{Array4[1, 0, 1, 0:None]}')
print (f'{Array4[1, 0, 1, :]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_Num1_Menor = np.min(Array_Num1)
Array_Num1_Mayor = np.max(Array_Num1)

print (f'El menor de los numeros es {Array_Num1_Menor} y el mayor es {Array_Num1_Mayor}')

print (f'-' * 20)

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

print (f'-' * 20)

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 0]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 0]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 1]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

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

Array_Num3 = np.full(shape=(2, 3), fill_value = Array4[1, 0, 1, 2:3])

print (f'{Array_Num3}')
print (f'{Array_Num3.ndim}')
print (f'{Array_Num3.shape}')
print (f'{Array_Num3.size}')
print (f'{Array_Num3.dtype}')
print (f'{Array_Num3[1, 1]}')

print (f'-' * 20)

Tupla_Array1 = ('Rojo', 'Verde')
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen3 = np.full(shape=(3, 2), fill_value = Tupla_Array1)
Array_Gen4 = np.full(shape=(2, 1), fill_value = Set_Conjunto_Array)
Array_Gen5 = np.full(shape=(4, 1), fill_value = Diccionario_Array['Nombre'][2])

print (f'{Array_Gen3}')
print (f'{Array_Gen4}')
print (f'{Array_Gen5}')

print (f'-' * 20)

print (f'{Array_Gen5[3]}')

print (f'-' * 20)

Array_Num4 = np.arange(start=1, stop=6, step=1)
Array_Num5 = np.arange(start=2, stop=11, step=2)
Array_Num6 = np.arange(start=3, stop=31, step=3)
Array_Num7 = np.arange(start=10, stop=21, step=2)
Array_Num8 = np.arange(10)

print (f'{Array_Num4}')
print (f'{Array_Num5}')
print (f'{Array_Num6}')
print (f'{Array_Num7}')
print (f'{Array_Num8}')

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
print (f'{Array_Random2[1, 0]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado: {Array_Random2_Sorted}')
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

Array_Num9 = np.arange(start=1, stop=21, step=1)

print (f'{Array_Num9}')

Array_Num9_Reshape = np.reshape(Array_Num9, shape=(4, 5))

print (f'{Array_Num9_Reshape}')

Array_Num9_Reshape_Ravel = np.ravel(Array_Num9_Reshape)

print (f'{Array_Num9_Reshape_Ravel}')

print (f'-' * 20)

Lista_Array2 = []
Lista_Array2.append('Josue')
Lista_Array2.insert(0, 'Erick')
Lista_Array2.extend(['Karlita'])

Array5 = np.array(Lista_Array2)

print (f'{Lista_Array2}')
print (f'{type(Lista_Array2)}')

print (f'-' * 20)

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

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Array_Random3_Columna_Min = np.min(Array_Random3, axis=0)
Array_Random3_Columna_Max = np.max(Array_Random3, axis=0)

Array_Random3_Row_Min = np.min(Array_Random3, axis=1)
Array_Random3_Row_Max = np.max(Array_Random3, axis=1)

print (f'Los menores de las columnas son {Array_Random3_Columna_Min}')
print (f'Los mayores de las columnas son {Array_Random3_Columna_Max}')
print (f'Los menores de las filas son {Array_Random3_Row_Min}')
print (f'Los mayores de las filas son {Array_Random3_Row_Max}')

print (f'-' * 20)

Tupla_Array2 = tuple(('Ash', 'Brooke', 'Misty', 'Josue', 'Karlita', 'Erick'))

Ganador1 = np.random.choice(Tupla_Array2, size=(1), replace=False)
Ganador2 = np.random.choice(Tupla_Array2, size=(2), replace=False)
Ganador3 = np.random.choice(Tupla_Array2, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-' * 20)

Array_Linspace = np.linspace(start=0, stop=10, num=3)

print (f'{Array_Linspace}')

def Generadora1():
    for elemento in range(1, 5):
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

print (f'-' * 20)

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
    print (f'Fin del experimento')

print (f'-' * 20)

def Generadora3():
    for elemento in range(1, 5):
        if (elemento == 1):
            yield f'NUMBER ONE'
        elif (elemento == 2):
            yield f'NUMBER TWO'
        elif (elemento == 3):
            yield f'NUMBER THREE'
        elif (elemento == 4):
            yield f'NUMBER FOUR'
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
    print (f'Fin del experimento')

print (f'-' * 20)

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int):
        return Num1 + Num2

    return Sumatoria_Interna(4)

Variable_Sumatoria = Sumatoria_Externa(3)

print (f'El resultado de la operacion es {Variable_Sumatoria}')

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






















# Creamos una funcion que solicite un numero para hacer una contrasena random, se devuelve un valor con return
# *args devuelve una tupla
# Con un subindice, muestre un solo elemento de la tupla resultado
# **kwargs devuelve un diccionario
# Ahora vamos a usar el argumento *args para empaquetar varios argumentos en una unica variable, hacemos una funcion que reciba muchos argumentos, los sume todos y despliegue el resultado
# Ahora vamos a hacer una funcion que diga, variable nombre Erick, la sumatoria de todos tus numeros es xxx, usando dos parametros, nombre y *args
# Ahora vamos a crear una tupla con *args
# Creamos un diccionario con **kwargs
# Creamos una funcion anonima lambda basica
# Crear una lambda que calcule el doble de un número. y lo imprima
# Creamos una lista de numeros y una funcion lambda con un filter que saque solo los pares

'''
Declarar una variable global externa integer
Ahora declaramos una funcion con una variable local interna integer
Hacemos una suma en la funcion de la variable global mas la variable local

Hagamos una funcion anidada
funcion externa con una variable nombre
indentamos una funcion interna con un apellido
imprimimos el nombre completo en la funcion interna

'''

# Esto es una funcion closure anidada que agrega numeros a una lista

def Agregue_Numero_Externa():
    Lista = []
   
    def Agregue_Numero_Interna(x):
        Lista.append(x)
        print (f'{Lista}')
       
    return Agregue_Numero_Interna

variable = Agregue_Numero_Externa()

variable(1)
variable(2)
variable(3)

# Ahora vamos a crear un closure con dos funciones crear_multiplicador y multiplicar que recibe dos parametros x y n, la idea es crear dos variables que multpliquen 10 * 2 y 10 * 3

def crear_Multiplicador(x):
    def Multiplicar(n):
        return x * n
   
    return Multiplicar

num1 = crear_Multiplicador(2)
num2 = crear_Multiplicador(3)

print (f'El primer resultado es {num1(10)}')
print (f'El primer resultado es {num2(10)}')

# Creamos una funcion que reciba un set o tupla de numeros y filtre para mostrar unicamente los numeros pares
Pares = [num for num in Lista if num % 2 == 0]

'''
************************* DECORADORES   *************************

1 - Primero vamos a crear un decorador que afecta a una funcion saludar hola mundo. La idea es agregar el texto "Esto va antes" a la funcion saludar hola mundo original por medio de un decorador

2 - Ahora vamos a crear una funcion que suma dos numeros, por medio de otro decorador, vamos a alterar el resultado de la sumatoria de la funcion y le sumaremos 100 mas

3 - Ahora vamos a crear una funcion que muestre un nombre y un apellido y por medio de un decorador vamos a cambiar el nombre de Erick a Carmelo

'''



# Crea una clase pokemon con tipo, nombre, ataque y una variable capturado en el  Modulo_Propio

# Usemos un unico elemento del modulo saludar con la instruccion "from Saludar import Diccionario_Poke", ya no se necesita usar Saludar

# Creemos una clase hija que herede todas las caracteristicas de la clase pokemon

# Ahora vamos a hacer un ejercicio de herencia multiple con 3 clases, una clase camara, otra reproductor musica y otra clase smartphone, smartphone hereda de las clases padre. Solamente tendra un metodo accion cada una


'''

Tipos de Herencia
Hacer un ejemplo de herencia Simple
Pokemon y poke hija

Hacer un ejemplo de herencia Herarquica (Veterinaria)
clase padre Mascota (nombre, edad, peso)
Clases hijas (Perro, Gato, Pajaro)
Perro (Raza, Padecimiento, N_Visitas)
Gato (Raza, Color, Paciente_Activo)
Pajaro (Especie, Habla)


Hacer un ejemplo de herencia Multiple (Personaje VideoJuego)

Atacante
daño base
método para atacar
energía de ataque

Curador
puntos de curación
método para curar
regeneración de vida

Paladin

Hereda de atacante y curador y tiene un nombre. Mostrar ficha de personaje



Como saber si una clase hija hereda de una clase padre?
Herencia = issubclass(Poke_Hija, Poke) # Esto debe darme true como resultado

Como saber si una variable es un objeto de una clase?
Instancia = isinstance(Objeto1, Poke) # Esto debe darme true como resultado



MRO  (Que pasa si varias clases tienen el mismo metodo?)
Vamos a hacer un ejemplo de herencia con MRO, lo que haremos es crear 5 clases, A,F,B,C,D,F, donde cada una tendra un metodo llamado Mostrar() y un texto hola "letra".
B heredara de A, C heredara de F, D heredara de B y C. Con esto veremos el flujo y como mostraria el mensaje del metodo si tengo un objeto Objeto1.Mostrar() Cual mensaje mostrara primero?
Vamos quitando bloques con pass
Que deberia hacer ahora que entiendo el orden del MRO si quisiera explicitamente llamar el metodo de la clase B desde D?

B.Mostrar(Objeto1)
F.Mostrar(Objeto1)
A.Mostrar(Objeto1)




[Polimorfismo]
Un cliente puede pagar con:
Tarjeta
PayPal
Criptomonedas
Todos comparten el mismo metodo pagar() que cambia dependiendo del metodo de pago


[Encapsulamiento] __privada
Cuenta bancaria encapsulada:
class Cuenta:

    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, dinero):
        self.__saldo += dinero

    def ver_saldo(self):
        print(self.__saldo)

mi_cuenta = Cuenta(100)
mi_cuenta.depositar(50)
mi_cuenta.ver_saldo()

Encapsulamiento: El saldo está protegido, no se puede alterar.

Getter → sirve para LEER un dato
Setter → sirve para CAMBIAR un dato

Muestre el valor de __Saldo con un getter
Cambie el valor de __Saldo con un setter

Hagamos una clase protegida que reciba un
nombre __privado y mostrarlo afuera de la
clase por medio de un @property



class Protegido:
    def __init__(self, Nombre):
        self.__Nombre = Nombre

    def Mostrar(self):
        print (f'Tu nombre es {self.__Nombre}')

    @property
    def nombre(self):
        return self.__Nombre

    @nombre.setter
    def nombre(self, Nuevo_Nombre):
        self.__Nombre = Nuevo_Nombre

Objeto1 = Protegido('Erick')

Objeto1.Mostrar()

Objeto1.nombre = 'Hola'   # setter

print(Objeto1.nombre)     # getter

--------------------------------------------------------------------






Abstraccion

Clases Abstractas

Las clases abstractas son plantillas que generan reglas que se deben seguir a la hora de crear clases en proyectos grandes.
En otras palabras, si hay 100 programadores, todos deben crear las reglas definidas en la plantilla. Normalmente son metodos.
Pero yo puedo crear todos los metodos que quiera en mis clases, la clase abstracta me dice nada mas que a fuerza la clase nueva debe tener ese metodo definido y todo lo demas que quiera.

from abc import ABC, abstractclassmethod

class Comida(ABC):

    @abstractclassmethod
    def Cocinar(self):
        pass

class Pizza(Comida):
        def Cocinar(self):
            print (f'Horneando La Pizza')

        def Mostrar(self):
            print (f'Hola Mundo')

Objeto1 = Pizza()

Objeto1.Cocinar()
Objeto1.Mostrar()

'''




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

# Haga un input que pida su nombre y valide si lo que se ingreso es un texto o algo mas
# (Nombre.replace(" ", "").isalpha()):

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



[LEER UNA PAGINA WEB]

import pandas as pd
import requests
import io # Esto viene incluido en Python, no hay que instalar nada

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'
headers = {'User-Agent' : 'Mozilla/5.0'}

# 1. Obtenemos la respuesta
Response = requests.get(Ruta_Html, headers=headers)

# 2. Envolvemos el texto en StringIO (esto suele quitar el 99% de los errores)
texto_html = io.StringIO(Response.text)

# 3. Leemos las tablas
Cargar_Html = pd.read_html(texto_html)

# 4. Mostramos la primera tabla encontrada
print(Cargar_Html[0].head())


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


Quiero crear una columna nueva agregada sobre el mismo csv con el total en precio multiplicando cantidad x price

Cargar_Csv5['Total'] = Cargar_Csv5['quantity'] * Cargar_Csv5['price']

print (f'{Cargar_Csv5}')

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