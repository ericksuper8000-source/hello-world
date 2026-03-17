try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado no funciona')

from Module_Own import Pokemon as Poke

class Poke_Hija(Poke):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto1 = Poke_Hija(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno', 'Acero')
Objeto2 = Poke_Hija(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Hada')
Objeto3 = Poke_Hija(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Electrico')

Poke.Mostrar(Objeto1)
Objeto1.Mostrar()

print (f'------------')

Poke.Mostrar(Objeto2)
Objeto2.Mostrar()

print (f'------------')

Poke.Mostrar(Objeto3)
Objeto3.Mostrar()

print (f'------------')

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

print (f'------------')

class Mascota:
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

Objeto5 = Perro('Chester', 3, 1.9, 'Poodle', 'Hipertension', 3)

Mascota.Mostrar(Objeto5)
Objeto5.Mostrar()

print (f'------------')

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

Objeto6 = Gato('Messi', 1.5, 1.40, 'Angora', 'Gris', 'Si')

Mascota.Mostrar(Objeto6)
Objeto6.Mostrar()

print (f'------------')

class Pajaro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto7 = Pajaro('Polly', 32, 0.60, 'Lora Verde', 'Si')

Mascota.Mostrar(Objeto7)
Objeto7.Mostrar()

print (f'------------')

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

Objeto8 = Paladin(125, 'Hacha de fuego', 75, 20, 'Posion De Veneno', 500, 'Ghost Knight')

Objeto8.Mostrar()
Atacante.Mostrar(Objeto8)
Curador.Mostrar(Objeto8)

print (f'------------')

Clase_Hija = issubclass(Poke_Hija, Poke)

print (f'{Clase_Hija}')

Objeto_Clase = isinstance(Objeto8, Atacante)

print (f'{Objeto_Clase}')

print (f'------------')

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

print (f'------------')

class Efectivo:
    def Pagar(self):
        print (f'Pago en efectivo')

class Tarjeta:
    def Pagar(self):
        print (f'Pago en Tarjeta')

class Criptomoneda:
    def Pagar(self):
        print (f'Pago en Criptomoneda')

Objeto10 = Criptomoneda()
Objeto11 = Tarjeta()
Objeto12 = Efectivo()

Objeto10.Pagar()
Objeto11.Pagar()
Objeto12.Pagar()

print (f'------------')

class Cuenta_Bancaria:
    def __init__(self, Saldo):
        self.__Saldo = Saldo

    def Depositar(self, Dinero):
        self.__Saldo += Dinero

    def Mostrar(self):
        print (f'Hola, tu saldo actual es ${self.__Saldo}')

    @property
    def dinero(self):
        return self.__Saldo

    @dinero.setter
    def dinero(self, New_Saldo):
        self.__Saldo = New_Saldo

Objeto13 = Cuenta_Bancaria(100)
Objeto13.Depositar(25)
Objeto13.Mostrar()

print (f'La variable privada con getter es {Objeto13.dinero}')

Objeto13.dinero = '20,000'

Objeto13.Mostrar()

print (f'------------')

from abc import ABC, abstractclassmethod

class Plantilla(ABC):

    @abstractclassmethod
    def Mostrar(self):
        pass

class Nombre(Plantilla):
    def Mostrar(self):
        print (f'Hola Muchachos')

Objeto14 = Nombre()

Objeto14.Mostrar()

import re

Texto1 = 'este es hola un te@xto cualquieraa 125 que hala yo voy a 90 ve-r por hela muchoba bueno o buenisimo  2 tiempo'

Buscar1 = re.search(r'\d+', Texto1)
Buscar2 = re.findall(r'\d+', Texto1)

print (f'{Buscar1}')

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

Buscar9 = re.findall(r'[a]{2}', Texto1)

print (f'{Buscar9}')

Buscar10 = re.findall(r'[a]{2,}', Texto1)

print (f'{Buscar10}')

Buscar11 = re.findall(r'[a]{2,4}', Texto1)

print (f'{Buscar11}')

Buscar12 = re.findall(r'[a]+', Texto1)

print (f'{Buscar12}')

Buscar13 = re.findall(r'[a]*', Texto1)

print (f'{Buscar13}')

Buscar14 = re.findall(r'[a]?', Texto1)

print (f'{Buscar14}')

Buscar15 = re.findall(r'(?=hala)+', Texto1)

print (f'{Buscar15}')

Buscar16 = re.fullmatch('este es hola un te@xto cualquieraa 125 que hala yo voy a 90 ve-r por hela mucho  2 tiempo', Texto1)

print (f'{Buscar16}')

Texto2 = '123 @'

Buscar17 = re.findall(r'^\d{3}\s?\W{1}$', Texto2)

print (f'{Buscar17}')

Buscar18 = re.findall(r'[ab]{2,4}', Texto1)

print (f'{Buscar18}')

Buscar19 = re.findall(r'[ab]+', Texto1)

print (f'{Buscar19}')

Buscar20 = re.findall(r'[0-9]{2,4}|hola', Texto1)

print (f'{Buscar20}')

Texto3 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern1 = r'[0-9]{2}/[0-9]{2}/[0-9]{4}'

Replacement = 'XX/XX/XXXX'

Nuevo_Texto = re.sub(Pattern1, Replacement, Texto3)

print (f'{Nuevo_Texto}')

print (f'------------')

def Exception1(Numero):
    try:
        Numerito = int(Numero)
        print (f'Gracias, tu numero es {Numerito}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Exception1("Hola")

def Exception2(Num1, Num2):
    try:
        Resultado = Num1 + Num2
        print (f'Gracias, el resultado de la operacion es {Resultado}')
    except TypeError:
        print (f'Error, necesito que ambos elementos sean numeros')

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
        print (f'El elemento en el indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'El indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'La llave seleccionada esta fuera de rango')

Exception5("Votante")

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Ardilla')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo seleccionado no existe')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nHiena'])
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

import pandas as pd

Data_Frame1 = pd.DataFrame({
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [18 * 2, 20, 6],
    'Votante' : [True, not False, False]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [55, 14, 26],
    'Votante' : [True, False, not False]
})

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

Data_Frame1_Age = Data_Frame1['Edad']

print (f'{Data_Frame1}')

print (f'------------')

print (f'{Data_Frame1_Age}')

print (f'La menor de las edades es {Data_Frame1_Age.min()} y la mayor de las edades es {Data_Frame1_Age.max()}')

print (f'{Data_Frame2.info()}')

print (f'------------')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombrecito = elemento['Nombre']

    print (f'Mi nombre es {Nombrecito}')

Buscar21 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Buscar21_Mayor = Buscar21.idxmax()
Buscar21_Menor = Buscar21.idxmin()
Buscar21_Mayor_Edad = Buscar21.max()
Buscar21_Menor_Edad = Buscar21.min()

print (f'{Buscar21}')

print (f'Del dataframe, la persona mayor del grupo es {Buscar21_Mayor} ({Buscar21_Mayor_Edad})')
print (f'Del dataframe, la persona menor del grupo es {Buscar21_Menor} ({Buscar21_Menor_Edad})')

print (f'------------')

import pandas as pd

Ruta_Csv1 = 'C:\\python-data-analyzer\\data\\sales.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

print (f'------------')

Grupo1 = Cargar_Csv1.groupby('product')['quantity'].sum()
Grupo1_May = Grupo1.idxmax()
Grupo1_Min = Grupo1.idxmin()
Grupo1_May_Cant = Grupo1.max()
Grupo1_Min_Cant = Grupo1.min()

print (f'{Grupo1}')

print (f'Producto con mayor numero de ventas: {Grupo1_May} - ({Grupo1_May_Cant})')
print (f'Producto con menor numero de ventas: {Grupo1_Min} - ({Grupo1_Min_Cant})')

print (f'------------')

Grupo2 = Cargar_Csv1.groupby('date')['quantity'].sum()
Grupo2_May = Grupo2.idxmax()
Grupo2_Min = Grupo2.idxmin()
Grupo2_May_Cant = Grupo2.max()
Grupo2_Min_Cant = Grupo2.min()

print (f'{Grupo2}')

print (f'La fecha con mayor numero de ventas fue {Grupo2_May} con un total de {Grupo2_May_Cant} ventas')
print (f'La fecha con menor numero de ventas fue {Grupo2_Min} con un total de {Grupo2_Min_Cant} ventas')

print (f'------------')

Grupo3 = Cargar_Csv1.groupby('product')['quantity'].sum()
Grupo3_Promedio = Grupo3.mean()

print (f'El promedio de ventas de los productos es {Grupo3_Promedio}')

print (f'------------')
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()'''

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'------------')

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'------------')

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'------------')

Fila, Columna = Data_Frame_Concatenate.shape

print (f'Filas: {Fila}')
print (f'Columnas: {Columna}')

Elemento1 = Data_Frame1.loc[0, 'Nombre']
Elemento2 = Data_Frame1.loc[1, 'Edad']
Elemento3 = Data_Frame1.loc[2, 'Votante']
Elemento4 = Data_Frame1.loc[1, :]
Elemento5 = Data_Frame1.loc[:, 'Nombre']

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')

print (f'------------')

print (f'{Elemento4}')
print (f'------------')
print (f'{Elemento5}')

print (f'------------')

Elemento6 = Data_Frame2.iloc[0, 0]
Elemento7 = Data_Frame2.iloc[1, 1]
Elemento8 = Data_Frame2.iloc[2, 2]
Elemento9 = Data_Frame2.iloc[0, :]
Elemento10 = Data_Frame2.iloc[2, :]

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')

print (f'------------')

print (f'{Elemento9}')
print (f'------------')
print (f'{Elemento10}')

print (f'------------')

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine='openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'------------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col="tarifa")
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:K", index_col="tarifa")
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:K", index_col="tarifa", nrows=1)

print (f'{Cargar_Excel1.head()}')

print (f'------------')

print (f'{Cargar_Excel2.head()}')

print (f'------------')

print (f'{Cargar_Excel3.head()}')

print (f'------------')

print (f'{Cargar_Excel4.head()}')

print (f'------------')

print (f'{Cargar_Excel5.head()}')

print (f'------------')

print (f'{Cargar_Excel6.head()}')

print (f'------------')

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='Cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'------------')

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='Cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

print (f'------------')

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt.head()}')

print (f'------------')

print (f'{Cargar_Txt}')

print (f'------------')

import pandas as pd

Ruta_Csv2 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Leer_Html)

print (f'{Cargar_Html[2].head()}')

print (f'------------')

********************************************** [NUMPY]

Importemos la libreria numpy
Con as llamenos a la libreria np


Cree un arreglo basico de 1 dimension con la funcion np.array([])
Con un print muestre un elemento del array de una dimension
Muestre la cantidad de dimensiones del array con la funcion .ndim
Ahora muestre la forma del array con .shape
Ahora veamos la cantidad de elementos del array con .size
Ahora muestre el tipo de dato con .dtype
# array[:3] // Imprimiremos todos los elemenstos desde el inicio hasta chocar con 3
# array[3:] // Imprimiremos desde el 3 hasta el final
# Array5[::2] se vuela todos los multiplos de 2 y muestra solo los que no lo son
# Array5[::3] se vuela todos los multiplos de 3 y muestra solo los que no lo son
# Array5[0, None] esto me va a mostrar en un array bi dimensional, solamente el row 0
# Ejemplo[Ejemplo < 12] esto imprime los elementos de la matriz que sean menores a 12


Cree un arreglo basico de 2 dimensiones con la funcion np.array([])
Con un print muestre un elemento del array
Muestre la cantidad de dimensiones del array con la funcion .ndim
Ahora muestre la forma del array con .shape
Ahora veamos la cantidad de elementos del array con .size
# array[:3] // Imprimiremos todos los elemenstos desde el inicio hasta chocar con 3
# array[3:] // Imprimiremos desde el 3 hasta el final
# Array5[::2] se vuela todos los multiplos de 2 y muestra solo los que no lo son
# Array5[::3] se vuela todos los multiplos de 3 y muestra solo los que no lo son
# Array5[0, None] esto me va a mostrar en un array bi dimensional, solamente el row 0
# [1, :, 2] = 500  de un array de 3 dimensiones, seleccione la segunda matriz, de todo ese row, tome todos los elementos de la columna 2 y cambielos por 500
# Ejemplo[Ejemplo < 12] esto imprime los elementos de la matriz que sean menores a 12
Acomodome los numeros con sort()
Saque la media con mean
Sume los elementos con sum
Sume los elementos con axis Sumita

# Haga una lista de 10 numeros consecutivos y con np.min() nuestre el mas pequeno
# Haga una lista de 10 numeros consecutivos y con np.max() nuestre el mas grande
# Hagamos una tabla de 5x5 y por medio de np.min(axis = 0) buscar el minimo de cada columna
# Por medio de np.max(axis = 1) buscar el maximo de cada fila
# axis = 0 son columnas
# axis = 1 son filas
# Ejemplo[Ejemplo < 12] esto imprime los elementos de la matriz que sean menores a 12

Cree un arreglo basico de 3 dimensiones pero con letras con la funcion np.array([])
Con un print muestre un elemento del array
Muestre la cantidad de dimensiones del array con la funcion .ndim
Ahora muestre la forma del array con .shape
Ahora veamos la cantidad de elementos del array con .size
Ahora muestre el tipo de dato con .dtype
# array[:3] // Imprimiremos todos los elemenstos desde el inicio hasta chocar con 3
# array[3:] // Imprimiremos desde el 3 hasta el final
# Array5[::2] se vuela todos los multiplos de 2 y muestra solo los que no lo son
# Array5[::3] se vuela todos los multiplos de 3 y muestra solo los que no lo son
# Array5[0, None] esto me va a mostrar en un array bi dimensional, solamente el row 0
# [1, :, 2] = 500  de un array de 3 dimensiones, seleccione la segunda matriz, de todo ese row, tome todos los elementos de la columna 2 y cambielos por 500
# Ejemplo[Ejemplo < 12] esto imprime los elementos de la matriz que sean menores a 12

Cree un arreglo basico de 4 dimensiones con la funcion np.array([])
Con un print muestre un elemento del array
Muestre la cantidad de dimensiones del array con la funcion .ndim
Ahora muestre la forma del array con .shape
Ahora veamos la cantidad de elementos del array con .size
# array[:3] // Imprimiremos todos los elemenstos desde el inicio hasta chocar con 3
# array[3:] // Imprimiremos desde el 3 hasta el final
# Array5[::2] se vuela todos los multiplos de 2 y muestra solo los que no lo son
# Array5[::3] se vuela todos los multiplos de 3 y muestra solo los que no lo son
# Array5[0, None] esto me va a mostrar en un array bi dimensional, solamente el row 0
# [1, :, 2] = 500  de un array de 3 dimensiones, seleccione la segunda matriz, de todo ese row, tome todos los elementos de la columna 2 y cambielos por 500
# Ejemplo[Ejemplo < 12] esto imprime los elementos de la matriz que sean menores a 12
Acomodome los numeros con sort()
Saque la media con mean
Sume los elementos con sum
Sume los elementos con axis Sumita


# Vamos a hacer un arreglo vacio de zeros de 2 x 3 con .zeros
Con un print muestre un elemento del array
Muestre la cantidad de dimensiones del array con la funcion .ndim
Ahora muestre la forma del array con .shape
Ahora veamos la cantidad de elementos del array con .size
Ahora muestre el tipo de dato con .dtype


# Vamos a hacer un arreglo vacio de unos de 2 x 3 con .ones
Con un print muestre un elemento del array
Muestre la cantidad de dimensiones del array con la funcion .ndim
Ahora muestre la forma del array con .shape
Ahora veamos la cantidad de elementos del array con .size
Ahora muestre el tipo de dato con .dtype


# Ahora vamos a crear un arreglo de 3,5 en donde cada posicion tenga el mismo texto .full
Con un print muestre un elemento del array
Muestre la cantidad de dimensiones del array con la funcion .ndim
Ahora muestre la forma del array con .shape
Ahora veamos la cantidad de elementos del array con .size


# Creamos un Array Generico de una dimension con 10 elementos aleatorios. Por medio de un ciclo for vamos a agregarlos a una Tupla_Array



# Array_Generico = np.full(shape=(3, 5), fill_value='Fuecoco')
# Crear una tabla de 2x3 con el número 7 en cada espacio
# Usar una tupla como fill_value, ojo el tamaño de la tupla debe ser mismo tamano de las columnas  mi_tupla = (1, 2)
# Diccionario como fill_value   ---   mi_diccionario = {"a": 1, "b": 2}
# Con un print muestre un elemento del array
# Muestre la cantidad de dimensiones del array con la funcion .ndim
# Ahora muestre la forma del array con .shape
# Ahora veamos la cantidad de elementos del array con .size

# Haz un arreglo 4x1 lleno de la palabra "hola".
# Haz un arreglo 2x2 lleno de un set como {10, 20, 30}




# Ahora vamos a crear un arreglo que contenga numeros del 1 al 5 con np.arange(start=1, stop=6, step=1)
# Solo números pares del 2 al 10   pares = np.arange(2, 11, 2)
# Crea un arreglo con los números del 10 al 20 de 2 en 2
# Crea un arreglo con los múltiplos de 3 desde 3 hasta 30


# Ahora creamos un arreglo que vaya de 1 a 10 con np.arrange(10)

# Creamos un array con random.randint() de una unica dimensional
# # Creamos un array con random.randint() de 2 x 3
# Crea un arreglo de números aleatorios y ordénalo con np.sort()
# Ahora a ese mismo arreglo saquele la media con .mean()
# Ahora haga la sumatoria de todos los elementos del arreglo con .sum()

# array[:3] // Imprimiremos todos los elemenstos desde el inicio hasta chocar con 3
# array[3:] // Imprimiremos desde el 3 hasta el final
# Array5[::2] se vuela todos los multiplos de 2 y muestra solo los que no lo son
# Array5[::3] se vuela todos los multiplos de 3 y muestra solo los que no lo son
# Array5[0, None] esto me va a mostrar en un array bi dimensional, solamente el row 0
# [1, :, 2] = 500  de un array de 3 dimensiones, seleccione la segunda matriz, de todo ese row, tome todos los elementos de la columna 2 y cambielos por 500

# Sume dos matrices de 2, 3 igual tamano
# Reste dos matrices de 2, 3 igual tamano
# Multiplique dos matrices de 2, 3 igual tamano
# Divida dos matrices de 2, 3 igual tamano
# Sumele 5 a cada numero de un arreglo de una unica vez

# Ahora tome un arreglo de un unico axis o dimension de 20 numeros y haga un reshape con una matriz de 4 x 5  np.reshape(array, shape=(2, 3))
# Ahora creemos una lista con 10 elementos, luego creemos un arreglo y llenemoslo con los elementos de la lista
# Ahora el array que fue reshape vamos a desenvolverlo con .ravel()
# Ahora creemos dos arrays de 1x3 cada uno y concatenemoslos con np.concatenate       -----  np.concatenate([arr1, arr2], axis = 1)
# Tomemos un array de 6 elementos y dividamoslo en 3 arrays  de 2 elementos cada uno con np.split(Array, 3)
# Ahora hagamos un array de 10 elementos, con la instruccion np.where(Array == 3) me creara un array que muestra todas las posiciones donde haya un 3

# con un ciclo for y una matriz de 2x3 recorra cada una de las filas
# Con un ciclo for y una matriz de 2x2x3 recorra cada matriz y luego otro for para recorrer cada fila
# vamos a hacer una matriz de 2x2x3 y con axis, vamos a sumar solo los elementos de la segunda fila np.sum(array1, axis=0)

# Vertical (por columnas)	           axis=0	Baja por las filas ↓
# Horizontal (por filas)	           axis=1	Cruza las columnas →
# Todo	                               Ninguno	Hace todo junto

'''
[Mini programa ganador del sorteo]
Creemos una lista con 6 nombres
Ganador = random.choise(Lista_Nombres)
Ahora elija 3 ganadores  Ganador = random.choise(Lista_Nombres, size=(3))
Finalmente elija una matriz de ganadores de 2x3     random.choise(Lista_Nombres, size=(2, 3))
Con la instruccion replace = False, vamos a asegurarnos que ningun numero del resultado se repita


Busque 3 numeros entre el 1 y el 10 con Array_Linspace = np.linspace(start=1, stop=10, num=3)
'''



Hagamos una funcion Generadora.
Las funciones generadoras me permiten ejecutar un codigo de manera pausada y controlada para ver el comportamiento.

Hagamos una funcion generadora, donde por medio de un range se muestren 10 numeros, pero con los parametros de la funcion generadora, ir de uno en uno para analizar su ejecucion.

def Ejemplo():
    for elemento in range(0, 10):
        yield elemento

Rango = Ejemplo()

print (f'{next(Rango)}')


Ahora hagamos una funcion donde por medio de un range se evalue si el elemento es un numero par o impar, vamos a ir evaluando cada uno con un if % 2 == 0 y yield, quiero que me muestre cada resultado de manera individual. La idea es con el next mostrar par, impar, par, etc….

def Ejemplo2():
    for elemento in range(5):
        if (elemento % 2 == 0):
            yield f'par'
        else:
            yield f'impar'

Rango2 = Ejemplo2()

print (f'{next(Rango2)}')



# Ahora vamos a hacer un ejercicio mas donde por medio de una funcion que recorra un ciclo range, con yield y next se muestre cada uno por separado
# Pero en este caso cuando lleguemos al final mostraremos un mensaje El ejercicio termino. Esto lo manejaremos con una exception StopIteration
def Ejemplo():
    for elemento in range(3):
        yield elemento

Rango = Ejemplo()

try:
    print (f'{next(Rango)}')
    print(f'{next(Rango)}')
    print(f'{next(Rango)}')
    print(f'{next(Rango)}')
except StopIteration:
    print (f'El ejercicio termino')
'''


####### CREANDO MIS PROPIAS FUNCIONES

# Creamos una funcion simple propia que diga hola mundo  en  Modulo_Propio
# Creamos una funcion que tenga un parametro nombre = (argumento) declarado en la misma funcion. En  Modulo_Propio
# Creamos una funcion que tenga un parametro nombre agregado por el usuario en  Modulo_Propio, ojo hagamos la funcion type hint mostrando el tipo de dato
# Creamos una funcion que recibe dos numeros, retorne (return) la suma del num1 y el num2 en  Modulo_Propio
# Ahora haremos la misma sumatoria pero con funciones anidadas
# Crear una función que devuelva True si un número es par
# Creamos ahora una funcion con dos parametros, nombre y sexo, si el sexo es femenimo muestra chica, si el sexo es masculino muestra chico con un condicional.
# Ahora haremos la misma funcion pero con funciones anidadas
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