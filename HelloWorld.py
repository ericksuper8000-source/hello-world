try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado no funciona')

from Module_Own import Pokemon1 as Poke1

Objeto1 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')

Objeto1.Mostrar()

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto2 = Poke_Kid1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Hada')
Objeto3 = Poke1(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro')

Poke1.Mostrar(Objeto2)
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
    def __init__(self, Nombre, Edad, Peso, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')

Objeto5 = Gato('Messi', 1.5, 1.8, 'Gris', 'No')

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

class Camara():
    def Tomar_Fotografia(self):
        print (f'Fotografia Tomada')

class Reproductor_Musica:
    def Reproducir_Musica(self):
        print (f'Musica Reproducida')

class Smartphone(Camara, Reproductor_Musica):
    def Encender_Smartphone(self):
        print (f'Smartphone Encendido')

Objeto7 = Smartphone()

Objeto7.Encender_Smartphone()
Objeto7.Reproducir_Musica()
Objeto7.Tomar_Fotografia()

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

Objeto8 = Paladin(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto8.Mostrar()
Atacante.Mostrar(Objeto8)
Defensor.Mostrar(Objeto8)

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

class Efectivo():
    def Pagar(self):
        print (f'El pago se realizo en efectivo')

class Tarjeta:
    def Pagar(self):
        print (f'El pago se realizo en tarjeta')

class Cripto:
    def Pagar(self):
        print (f'El pago se realizo en cripto')

Objeto10 = Cripto()
Objeto11 = Tarjeta()
Objeto12 = Efectivo()

Objeto10.Pagar()
Objeto11.Pagar()
Objeto12.Pagar()

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

Objeto13 = Cuenta_Bancaria(100)
Objeto13.Depositar(25)
Objeto13.Mostrar()

print (f'Su saldo privado es {Objeto13.Dinero}')

Objeto13.Dinero = '20,000'

Objeto13.Mostrar()
print (f'Su saldo privado es {Objeto13.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Platilla(ABC):
    @abstractmethod
    def Vacio(self):
        pass

class Abstraccion(Platilla):
    def Vacio(self):
        print (f'Esto es un ejemplo de abstraccion')

    def Mostrar(self):
        print (f'Hola Mundo')

Objeto14 = Abstraccion()

Objeto14.Mostrar()
Objeto14.Vacio()

print (f'-' * 20)

class Composicion():
    def Primera(self):
        print (f'Esto se encuentra en la primera clase')

class Ejemplo2:
    def __init__(self):
        self.Heredado = Composicion()

    def Mostrar(self):
        self.Heredado.Primera()

Objeto15 = Ejemplo2()

Objeto15.Mostrar()

print (f'-' * 20)

import re

Texto1 = 'esto es hela un 15 ejemplo cualquiera 314 @ con el que 0 quiero abbaaa hola practicar un hala poco'

Buscar1 = re.search('h.la', Texto1)

print (f'{Buscar1}')

Buscar2 = re.findall(r'(hola|hela)', Texto1)

print (f'{Buscar2}')

Buscar3 = bool(re.fullmatch('esto es hela un 15 ejemplo cualquiera 31 con el que 7 quiero hola practicar un hala poco', Texto1))

if (Buscar3):
    print (f'El texto es exactamente igual')
else:
    print (f'Error, al menos una parte del texto no es igual')

Buscar4 = re.findall('r\d?', Texto1)

print (f'{Buscar4}')

Buscar5 = re.findall('(0[0-9]|[1][0-5])', Texto1)

print (f'{Buscar5}')

Buscar6 = re.findall(r'^esto', Texto1)

print (f'{Buscar6}')

Buscar7 = re.findall(r'o$', Texto1)

print (f'{Buscar7}')

Buscar8 = re.findall(r'[0-9]{3}\s{1}\W{1}', Texto1)

print (f'{Buscar8}')

Buscar9 = re.findall(r'[ab]{2,4}', Texto1)

print (f'{Buscar9}')

Correo1 = 'sample@gmail.com'

Pattern1 = r'^[a-zA-Z0-9./*-+=-_]+\@(yahoo|gmail|hotmail)\.(com|org|net)$'

Buscar10 = bool(re.match(Pattern1, Correo1))

if (Buscar10 == True):
    print (f'Formato correo corecto')
else:
    print (f'El formato del correo es incorrecto')

Numero = '23'

Pattern2 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar11 = bool(re.match(Pattern2, Numero))

if (Buscar11 == True):
    print (f'El numero se encuentra entre 1 y 31')
else:
    print (f'Error, numero fuera de rango')

Texto2 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern3 = r'\d{2}\/[0-9]{2}/\d{4}'

Replacement = 'XX/XX/XXXX'

Buscar12 = re.sub(Pattern3, Replacement, Texto2)

print (f'{Buscar12}')

Numero_Decimal = 5.8

try:
    float(Numero_Decimal)
    print (f'El numero ingresado es decimal {Numero_Decimal}')
except ValueError:
    print (f'Error, el contenido no es decimal')

Numero_Entero = 3.5

try:
    int(Numero_Entero)
    print (f'El numero ingresado es entero {Numero_Entero}')
except ValueError:
    print(f'Error, el contenido no es entero')

Texto3 = "   Hola!!!   mundo@@   123   "

print (f'{Texto3}')

Version1 = Texto3.strip()
Version2 = Version1.lower()

Buscar13 = re.sub(r'[^a-z0-9\s]', '', Version2)

print (f'{Buscar13}')

Buscar14 = ' '.join(Buscar13.split())

print (f'{Buscar14}')

from datetime import datetime
import pandas as pd

Ruta_Csv1 = 'C:\\Repo\\Store.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

Fecha = '2026-04-01'

try:
    Fech = datetime.strptime(Fecha, '%Y-%m-%d').date()
    Fech_Formateada = pd.to_datetime(Fech)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Error, formato fecha incorrecto')
    exit()

Encontrado = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech_Formateada.date()]

if (Encontrado.empty):
    print (f'No se encontraron ventas en esta fecha')
else:
    print (f'Genial! Encontramos ventas')
    Grupo1 = Encontrado.groupby('product')['quantity'].sum()

    Grupo1_Prod_May = Grupo1.idxmax()
    Grupo1_Prod_Min = Grupo1.idxmin()

    Grupo1_Prod_May_Cant = Grupo1.max()
    Grupo1_Prod_Min_Cant = Grupo1.min()

    print (f'En la compra realizada en {Fech_Formateada} el producto que mas vendio fue {Grupo1_Prod_May} ({Grupo1_Prod_May_Cant})')
    print (f'En la compra realizada en {Fech_Formateada} el producto que menos vendio fue {Grupo1_Prod_Min} ({Grupo1_Prod_Min_Cant})')

Cargar_Csv1['MisResultadosxxx'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']

print (f'-' * 20)

print (f'{Cargar_Csv1}')

print (f'-' * 20)

def Exception1(Valor):
    try:
        Valore = int(Valor)
        print (f'El numero ingresado es {Valore}')
    except ValueError:
        print (f'Error, el valor ingresado no es un numero')

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
        print (f'Error, el divisor no puede ser un cero')

Exception3(12, 0)

Lista_Exception4 = list(['Erick', 'Josue', 'Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento con indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El elemento con llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception5('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Hiena')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue ubicado')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nCocodrilo'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nAvestruz')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

Texto4 = "   Hola!!!   mundo@@   123$   "

Version3 = Texto4.strip()
print (f'{Version3}')

Version4 = ' '.join(Version3.split())

print (f'{Version4}')

Version5 = Version4.lower()
print (f'{Version5}')

Version6 = re.sub(r'[^a-z0-9\s]', '', Version5)

print (f'{Version6}')

print (f'-' * 20)

from datetime import datetime
import pandas as pd

Ruta_Csv2 = 'C:\\Repo\\Store.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

print (f'-' * 20)

Fecha2 = '2026-04-01'

try:
    Fech2 = datetime.strptime(Fecha2, '%Y-%m-%d').date()
    Fech2_Formateada = pd.to_datetime(Fech2)
    Cargar_Csv2['date'] = pd.to_datetime(Cargar_Csv2['date'])
except ValueError:
    print (f'Error, formato de fecha incorrecto')
    exit()

Ubicada2 = Cargar_Csv2[Cargar_Csv2['date'].dt.date == Fech2_Formateada.date()]

if (Ubicada2.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial, encontramos ventas')

    Grupo2 = Ubicada2.groupby('product')['quantity'].sum()
    Grupo2_Prod_May = Grupo2.idxmax()
    Grupo2_Prod_May_Cant = Grupo2.max()
    Grupo2_Prod_Min = Grupo2.idxmin()
    Grupo2_Prod_Min_Cant = Grupo2.min()

    print (f'Durante {Fech2_Formateada} el producto que mas vendio fue {Grupo2_Prod_May} con un total de {Grupo2_Prod_May_Cant} unidades')
    print (f'Durante {Fech2_Formateada} el producto que menos vendio fue {Grupo2_Prod_Min} con un total de {Grupo2_Prod_Min_Cant} unidades')

Cargar_Csv2['MUCHACHIS'] = Cargar_Csv2['quantity'] * Cargar_Csv2['price']

print (f'-' * 20)
print (f'-' * 20)

print (f'{Cargar_Csv2}')

print (f'-' * 20)

Texto5 = "   Hola!!!   mundo@@   123$   "

Version7 = Texto5.strip()

print (f'{Version7}')

Version8 = ' '.join(Version7.split())

print (f'{Version8}')

Version9 = Version8.lower()

print (f'{Version9}')

import re

Version10 = re.sub(r'[^a-z0-9\s]', '', Version9)

print (f'{Version10}')

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
    Documento_Agregar = Docu.write(f' - '.join(PEPE.Set_Conjunto_Poke))
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

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

print (f'{Data_Frame1}')

print (f'-' * 20)

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame_Concatenate_Age}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()} y la mayor de las edades es {Data_Frame_Concatenate_Age.max()}')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombrecito = elemento['Nombre']
    Edacita = elemento['Edad']
    print (f'Mi nombre es {Nombrecito} y mi edad es {Edacita} años')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate}')

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()

print (f'El menor de los compas es {Grupo3.idxmin()} ({Grupo3.min()}) y el mayor es {Grupo3.idxmax()} ({Grupo3.max()})')

print (f'El total de nombres es {Grupo3.count()}')

print (f'La media de las edades es {round(Grupo3.mean(), 2)}')

print (f'-' * 20)

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

plt.show()'''

print (f'{Data_Frame_Concatenate.head(1)}')
print (f'-' * 20)

print (f'{Data_Frame_Concatenate.head(3)}')
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

Cargar_Excel = pd.read_excel(Ruta_Excel)

print (f'{Cargar_Excel.head()}')

print (f'-' * 20)

Cargar_Excel1 = pd.read_excel(Ruta_Excel, sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, index_col='cabina')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:K', index_col='cabina')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:K', index_col='cabina', nrows=1)

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

print (f'-' * 20)

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'-' * 20)

print (f'{Cargar_Txt.head()}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv3 = 'Base_Datos.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3.head()}')

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

print (f'{Lista_Array1[1][:]}')
print (f'{Lista_Array1[1][1:2]}')
print (f'{Lista_Array1[1][0:None]}')
print (f'{Lista_Array1[0][:2]}')
print (f'{Lista_Array1[0][2:]}')
print (f'{Lista_Array1[1][::2]}')
print (f'{Lista_Array1[1][::3]}')

print (f'-' * 20)

for i in range(len(Lista_Array1)):
    for j in range(len(Lista_Array1[i])):
        print (f'{Lista_Array1[i][j]}')

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
print (f'{Array1[2:4]}')
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
print (f'{Array2[1, 1:2]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[0, :]}')
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

print (f'-' * 20)

Array3 = np.array([[['a', 'i', 'k'], ['c', 'u', 'm']],     [['x', 'f', 's'], ['r', 'o', 'n']]])

print (f'{Array3}')
print (f'{Array3.ndim}')
print (f'{Array3.shape}')
print (f'{Array3.size}')
print (f'{Array3.dtype}')
print (f'{Array3[0, 1, 2]}')

print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[0, 0, ::2]}')
print (f'{Array3[0, 1, ::3]}')
print (f'{Array3[1, :, 0]}')
print (f'{Array3[0, 1, 2:3]}')
print (f'{Array3[1, 0, 0:None]}')
print (f'{Array3[1, 0, :]}')
print (f'{Array3[Array3 == "e"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],         [[[6, 5, 4], [9, 8, 7]], [[8, 1, 6], [5, 9, 7]]]])

print (f'{Array4}')
print (f'{Array4.ndim}')
print (f'{Array4.shape}')
print (f'{Array4.size}')
print (f'{Array4.dtype}')
print (f'{Array4[1, 0, 1, 2]}')

print (f'{Array4[1, 0, 1, :2]}')
print (f'{Array4[1, 0, 1, 2:]}')
print (f'{Array4[1, 0, 0, ::2]}')
print (f'{Array4[1, 1, 0, ::3]}')
print (f'{Array4[1, 0, :, 2]}')
print (f'{Array4[0, 0, 1, 2:3]}')
print (f'{Array4[0, 1, 0, 0:None]}')
print (f'{Array4[0, 1, 0, :]}')
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

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Menor_Array = np.min(Array_Num1)
Mayor_Array = np.max(Array_Num1)

print (f'El menor de los numeros del array es {Menor_Array}')
print (f'El mayor de los numeros del array es {Mayor_Array}')

print (f'-' * 20)

Array_Num2 = np.arange(start=1, stop=26, step=1)

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

Array_Num2_Reshape_Ravel = np.ravel(Array_Num2_Reshape)

print (f'{Array_Num2_Reshape_Ravel}')

Array_Num2_Reshape2 = np.reshape(Array_Num2_Reshape_Ravel, shape=(5, 5))

print (f'{Array_Num2_Reshape2}')

Array_Num2_Reshape2_Column_Min = np.min(Array_Num2_Reshape2, axis=0)
Array_Num2_Reshape2_Column_Max = np.max(Array_Num2_Reshape2, axis=0)
Array_Num2_Reshape2_Row_Min = np.min(Array_Num2_Reshape2, axis=1)
Array_Num2_Reshape2_Row_Max = np.max(Array_Num2_Reshape2, axis=1)

print (f'Los menores de las columnas son {Array_Num2_Reshape2_Column_Min}')
print (f'Los mayores de las columnas son {Array_Num2_Reshape2_Column_Max}')
print (f'Los menores de las filas son {Array_Num2_Reshape2_Row_Min}')
print (f'Los mayores de las filas son {Array_Num2_Reshape2_Row_Max}')

print (f'-' * 20)

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 2:3]}')

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

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

print (f'{Array_Gen2}')

Lista_Array2 = list([])

for indice, elemento in enumerate(Array_Gen2):
    Lista_Array2.append(str(elemento))

print (f'{Lista_Array2}')
print (f'{type(Lista_Array2)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[0, 1, 0, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[0, 2]}')

print (f'-' * 20)

Tupla_Array = tuple(('Rojo', 'Verde'))
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array['Nombre'][2:3])

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

print (f'-' * 20)

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

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Mean = np.mean(Array_Random2)
Array_Random2_Sum = np.sum(Array_Random2)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sum}')

print (f'-' * 20)

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Suma = Arr1 + Arr2
Rest = Arr1 - Arr2
Mult = Arr1 * Arr2
Div = Arr1 / Arr2

Array_Random1_Cien = Array_Random1 + 100

print (f'El resultado de la operacion es {Suma}')
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

Lista_Array3 = list([1, 2, 3, 4, 5])

Array5 = np.array(Lista_Array3)

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

Sumita9 = np.sum(Array_Random3, axis=0)
Sumita10 = np.sum(Array_Random3, axis=1)
Sumita11 = np.sum(Array_Random3[1, 0, 0:None])
Sumita12 = np.sum(Array_Random3[1, 0, :])

Sumita13 = np.sum(Array_Random3[1, :, 1])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')
print (f'El resultado de la sumita es {Sumita13}')

print (f'-' * 20)

Lista_Array4 = list(['Erick'])
Lista_Array4.append('Josue')
Lista_Array4.insert(1, 'Karlita')
Lista_Array4.append('Carmelo')
Lista_Array4.insert(2, 'Roxana')
Lista_Array4.extend(['Susanita'])

Ganador1 = np.random.choice(Lista_Array4, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Array4, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Array4, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-' * 20)

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-' * 20)

Texto6 = "   Hola!!!   mundo@@   123   "

print (f'{Texto6}')

Version11 = Texto6.strip()

print (f'{Version11}')

Version12 = ' '.join(Version11.split())

print (f'{Version12}')

Version13 = Version12.lower()

print (f'{Version13}')

import re

Version14 = re.sub(r'[^a-z0-9\s]', '', Version13)

print (f'{Version14}')

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
    Fech3_Formateada = pd.to_datetime(Fech3)
    Cargar_Csv4['date'] = pd.to_datetime(Cargar_Csv4['date'])
except ValueError:
    print (f'Error, formato incorrecto')
    exit()

Encontrado4 = Cargar_Csv4[Cargar_Csv4['date'].dt.date == Fech3_Formateada.date()]

if (Encontrado4.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial, encontramos ventas')

    Grupo4 = Encontrado4.groupby('product')['quantity'].sum()
    Grupo4_May = Grupo4.idxmax()
    Grupo4_Min = Grupo4.idxmin()

    Grupo4_May_Cant = Grupo4.max()
    Grupo4_Min_Cant = Grupo4.min()

    print (f'El producto que mas vendio durante {Fech3_Formateada} fue {Grupo4_May} ({Grupo4_May_Cant})')
    print (f'El producto que menos vendio durante {Fech3_Formateada} fue {Grupo4_Min} ({Grupo4_Min_Cant})')

print (f'-' * 20)

Cargar_Csv4['BEBES'] = Cargar_Csv4['quantity'] * Cargar_Csv4['price']

print (f'{Cargar_Csv4}')

print (f'-' * 20)

def Generadora1():
    for elemento in range(5):
        yield elemento

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
            yield 'PAR'
        else:
            yield 'IMPAR'

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
    for elemento in range(5):
        if (elemento == 0):
            yield 'ZERO'
        elif (elemento == 1):
            yield 'ONE'
        elif (elemento == 2):
            yield 'TWO'
        elif (elemento == 3):
            yield 'THREE'
        elif (elemento == 4):
            yield 'FOUR'
        else:
            yield 'Error de codigo'

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

def Primera(Segunda):
    def Tercera(*args):
        Lista_Externa = [20, 21, 22, 23, 24]
        return Segunda(Lista_Externa)

    return Tercera

@Primera
def Dobles(Lista):
    Num1 = min(Lista)
    Num2 = max(Lista)

    Lista_Funcion = [Num1, Num2]

    return Lista_Funcion

Lista0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print (f'{Dobles(Lista0)}')

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int) -> int:
        return Num1 + Num2

    return Sumatoria_Interna(3)

Variable_Sumatoria = Sumatoria_Externa(4)

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

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(44)}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

print (f'-' * 20)

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.5, 500, True)

print (f'{Funcion_Tupla("Perro", 3.5, 500, True)}')
print (f'{Funcion_Tupla("Perro", 3.5, 500, True)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.5, 500, True))}')

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

print (f'Los numeros pares de la lista son {list(Anonima3)} o incluso podrian ser {PEPE.Lista_Par}')

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
        return f'Mi nombre es {Nombre} {Apellido}'

    return Interna('PEREZ GUTIERREZ')

Variable_Finale = Externa('ERICK JOSUE')

print (f'{Variable_Finale}')

def Closure_Externa():
    Lista_Closure = []
    def Closure_Interna(x):
        Lista_Closure.append(x)

        return Lista_Closure

    return Closure_Interna

Variable_Closure = Closure_Externa()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(25)}')
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
    Any_Impar = any(num % 2 != 0 for num in Lista)
    if (Any_Impar == True):
        Anonima4 = filter(lambda Num :  Num % 2 != 0, Lista)
        Lista_Impar = [num for num in Lista if num % 2 != 0]

        print (f'Los elementos impares de la lista son {list(Anonima4)} o incluso podrian ser {Lista_Impar}')
    else:
        print (f'Error, no hay elementos impares en la lista')

Filtrador(PEPE.Lista_Numeros)

def Primera(Segunda):
    def Tercera():
        print (f'****************')
        Segunda()
        print (f'****************')

    return Tercera

@Primera
def Saludar4():
    print (f'Hola Erick')

Saludar4()

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 7

    return Tercera

@Primera
def Sumatoria3(Num1, Num2):
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(4, 3)}')

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'JONATHAN'
        Apellido = 'SMITHY'
        return Segunda(Nombre, Apellido)

    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    print (f'Mi nombre es {Nombre} {Apellido}')

Usuario2('Erick', 'Josue')

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

Objeto17 = Poke_Kid2(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Acero')

Poke2.Mostrar(Objeto17)
Objeto17.Mostrar()

print (f'-' * 20)

class Camara2():
    def Tomar_Fotografia(self):
        print (f'La fotografia ha sido tomada')

class Reproductor2():
    def Reproducir_Musica(self):
        print (f'La musica ha sido reproducida')

class Celular2(Camara2, Reproductor2):
    def Encender_Celular(self):
        print (f'El smartphone ha sido encendido')

Objeto18 = Celular2()

Objeto18.Encender_Celular()
Objeto18.Reproducir_Musica()
Objeto18.Tomar_Fotografia()

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def Borradora(self):
        pass

class Abstraccion2(Plantilla2):
    def Mostrar(self):
        print (f'Este es un mensaje secundario')

    def Borradora(self):
        print (f'Este es el ejemplo de abstraccion')

Objeto19 = Abstraccion2()

Objeto19.Mostrar()
Objeto19.Borradora()

Texto7 = "   Hola!!!   mundo@@   123   "

print (f'{Texto7}')

Version15 = Texto7.strip()

print (f'{Version15}')

Version16 = ' '.join(Version15.split())

print (f'{Version16}')

Version17 = Version16.lower()

print (f'{Version17}')

import re

Version18 = re.sub(r'[^a-z0-9\s]', '', Version17)

print (f'{Version18}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv5 = 'C:\\Repo\\Store.csv'

Cargar_Csv5 = pd.read_csv(Ruta_Csv5)

print (f'{Cargar_Csv5}')

print (f'-' * 20)

Fecha5 = '2026-04-01'

try:
    Fech5 = datetime.strptime(Fecha5, '%Y-%m-%d').date()
    Fecha5_Formateada = pd.to_datetime(Fech5)
    Cargar_Csv5['date'] = pd.to_datetime(Cargar_Csv5['date'])
except ValueError:
    print (f'Error, formato incorrecto')
    exit()

Encontrado5 = Cargar_Csv5[Cargar_Csv5['date'].dt.date == Fecha5_Formateada.date()]

if (Encontrado5.empty):
    print (f'No hay ventas en esta fecha')
else:
    print (f'Genial! encontramos ventas')
    Grupo5 = Encontrado5.groupby('product')['quantity'].sum()
    Grupo5_May = Grupo5.idxmax()
    Grupo5_Min = Grupo5.idxmin()
    Grupo5_May_Cant = Grupo5.max()
    Grupo5_Min_Cant = Grupo5.min()

    print (f'En la fecha {Fecha5_Formateada} el prod que mas vendio fue {Grupo5_May} con un total de unidades de {Grupo5_May_Cant}')
    print (f'En la fecha {Fecha5_Formateada} el prod que mas vendio fue {Grupo5_Min} con un total de unidades de {Grupo5_Min_Cant}')

import re

Correo2 = 'sample@sample.com'

Pattern4 = r'^[a-z-A-Z0-9./*-+-_]+\@[a-zA-Z]+\.[a-z]{3}$'

Buscar15 = bool(re.fullmatch(Pattern4, Correo2))

if (Buscar15 == True):
    print (f'El formato es correcto')
else:
    print (f'Formato de correo electronico incorrecto')

print (f'-' * 20)

import re

Correo2 = 'sample@gmail.com'

Pattern5 = r'^[a-zA-Z0-9*-+./]+\@(gmail|yahoo|hotmail)\.(com|org|net)$'

Buscar16 = bool(re.match(Pattern5, Correo2))

if (Buscar16):
    print (f'El formato de mi correo electronico es correcto')
else:
    print (f'Error, formato de correo incorrecto')

Numero2 = '31'

Pattern6 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar17 = bool(re.match(Pattern6, Numero2))

if (Buscar17 == True):
    print (f'Correcto, el numero se encuentra entre 1 y 31')
else:
    print (f'Error, numero fuera de rango')

print (f'-' * 20)

import re

Texto8 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern7 = r'\d{2}\/[0-9]{2}\/\d{2,4}'

Replacemen7 = 'XX/XX/XXXX'

Buscar18 = re.sub(Pattern7, Replacemen7, Texto8)

print (f'{Buscar18}')

Pattern8 = r'\+[0-9]{1}\-\d{3}\-\d{3}\-[0-9]{2,4}'

Replacemen8 = '+x-xxx-xxx-xxxx'

Buscar19 = re.sub(Pattern8, Replacemen8, Buscar18)

print (f'{Buscar19}')

print (f'-' * 20)

class Mascota2():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad} años')
        print (f'Peso: {self.Peso}kgs')

class Perro2(Mascota2):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimientos):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimientos

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')

Objeto20 = Perro2('Chester', 5, 2.8, 'Bulldog', 'Anemia')

Mascota2.Mostrar(Objeto20)
Objeto20.Mostrar()

print (f'-' * 20)

class Gato2(Mascota2):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')

Objeto21 = Gato2('Messi', 1.5, 1.8, 'Gris', 'No')

Mascota2.Mostrar(Objeto21)
Objeto21.Mostrar()

print (f'-' * 20)

class Pajaro2(Mascota2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto22 = Pajaro2('Polly', 31, 0.4, 'Cacatua Amarilla', 'Si')

Mascota2.Mostrar(Objeto22)
Objeto22.Mostrar()

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

class Paladin2(Atacante2, Defensor2):
    def __init__(self, Damage, Weapon, Healing, Potion, Life, Name):
        Atacante2.__init__(self, Damage, Weapon)
        Defensor2.__init__(self, Healing, Potion, Life)
        self.Name = Name

    def Mostrar(self):
        print (f'Name: {self.Name}')

Objeto23 = Paladin2(75, 'Battle Axe', 25, 'Black Lagoon', 200, 'Ghost Knight')

Objeto23.Mostrar()
Atacante2.Mostrar(Objeto23)
Defensor2.Mostrar(Objeto23)

print (f'-' * 20)

Children_Class = issubclass(Poke_Kid2, Poke2)

print (f'{Children_Class}')

Objeto_Clase1 = isinstance(Objeto23, Atacante2)
Objeto_Clase2 = isinstance(Objeto23, Defensor2)
Objeto_Clase3 = isinstance(Objeto23, Paladin2)

print (f'{Objeto_Clase1}')
print (f'{Objeto_Clase2}')
print (f'{Objeto_Clase3}')

print (f'-' * 20)

class F():
    def Mostrar(self):
        print (f'Hola F')

class J():
    def Mostrar(self):
        print (f'Hola J')

class G(J):
    def Mostrar(self):
        print (f'Hola G')

class H(F):
    def Mostrar(self):
        print (f'Hola H')

class I(G,H):
    def Mostrar(self):
        print (f'Hola I')

Objeto24 = I()

F.Mostrar(Objeto24)
G.Mostrar(Objeto24)
H.Mostrar(Objeto24)
Objeto24.Mostrar()
J.Mostrar(Objeto24)

print (f'-' * 20)

class Banking_Account():
    def __init__(self, Saldo):
        self.__Saldo = Saldo

    def Deposit(self, Money):
        self.__Saldo += Money

    @property
    def Money(self):
        return self.__Saldo

    @Money.setter
    def Money(self, New_Money):
        self.__Saldo = New_Money

    def Show(self):
        print (f'Your current balance is ${self.__Saldo}')

Objeto25 = Banking_Account(200)
Objeto25.Deposit(40)
Objeto25.Show()

print (f'Tu saldo privado es {Objeto25.Money}')

Objeto25.Money = '30,000'

Objeto25.Show()
print (f'Tu saldo privado es {Objeto25.Money}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla3(ABC):
    @abstractmethod
    def Metodo_Default(self):
        pass

class Ejemplo3(Plantilla3):
    def Mostrar(self):
        print (f'Hola Mundo Plantilla3')

    def Metodo_Default(self):
        print (f'Hola Abstraccion 3')

Objeto26 = Ejemplo3()

Objeto26.Mostrar()

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''
Esto
Es
Un
Long
String'''

variable4 = Objeto3.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = not False, Objeto2.Catched

# Esto es un comentario simple

'''
Esto 
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Variable_Sumatoria} o {Sumatoria2(1, 2, 3, 4, 5)} o incluso {Objeto2.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Josue' in PEPE.Lista1)

print (f'Misty' in PEPE.Tupla_Poke)
print (f'Vaporeon' in PEPE.Set_Conjunto_Poke)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto1.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente es {Cociente} y residuo es {Residuo}')

print (f'{Lista_Uno[:2]}')
print (f'{Lista_Uno[2:]}')
print (f'{Lista_Uno[::2]}')
print (f'{Lista_Uno[::3]}')
print (f'{Lista_Uno[2:3]}')
print (f'{Lista_Uno[0:None]}')
print (f'{Lista_Uno[:]}')

print (f'{Lista_Uno[1]} eso de ahi es un {PEPE.Lista2[2]}?')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, 100, 200)

print (f'{Lista_Cuatro}')

del Lista_Uno[0]
Lista_Uno.remove('Juana La Cubana')
Lista_Uno.pop(-2)
Lista_Uno.pop(-1)
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

Tupla1 = tuple(('Red', 'Green'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Tupla_Array)}')

Set_Conjunto1 = {'Erick'}
Set_Conjunto1.add('Josue')
Set_Conjunto1.add('Karlita')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Tortuga'})

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

print (f'Union - {A.union(B)}')
print (f'Union - {A | B}')

print (f'Interseccion - {A.intersection(B)}')
print (f'Interseccion - {A & B}')

print (f'Diferencia1 - {A.difference(B)}')
print (f'Diferencia1 - {A - B}')
print (f'Diferencia2 - {B.difference(A)}')
print (f'Diferencia2 - {B - A}')

print (f'Symmetric Difference - {A.symmetric_difference(B)}')
print (f'Symmetric Difference - {A ^ B}')

print (f'-' * 20)

'''A.update(B)

print (f'{A}')'''

'''A.intersection_update(B)

print (f'{A}')'''

A.symmetric_difference_update(B)

print (f'{A}')

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

'''Hagamos un diccionario nuevo y saquemos diferentes elementos con
.keys()
.values()
.items()
'''


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


'''
| Método        | Descripción                            |
| ------------- | -------------------------------------- |
| `isalpha()`   | Solo letras                            |
| `isdigit()`   | Dígitos y algunos caracteres numéricos |
| `isdecimal()` | Solo dígitos decimales                 |
| `isnumeric()` | Cualquier carácter numérico            |
| `isalnum()`   | Letras y números                       |
| `isspace()`   | Solo espacios                          |
| `islower()`   | Letras en minúsculas                   |
| `isupper()`   | Letras en mayúsculas                   |
| `istitle()`   | Formato de título                      |

'''


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
# Ojo hagamos un ejemplo de validacion de correo electronico que pida explicitamente hotmail, gmail, yahoo o .com, .net .org  pattern1 = r'^[a-zA-Z0-9./*-+=_/?]+\@(hotmail|gmail|yahoo)\.(com|net|org)$'

# Busque un numero que debe estar explicitamente entre 01 y 31. pattern1 = r'(0[0-9]|[12][0-9]|3[01])'

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

