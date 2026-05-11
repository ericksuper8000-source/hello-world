variable0 = '45'
variable1 = 45
variable3 = 500
variable4 = 4.8
variable5 = 'Hola Mundo'

if (isinstance(variable1, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero entero')
    
if (variable0.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero entero')
    
try:
    flotante = float(variable3)
    if (flotante.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error de codigo')
    
if (isinstance(variable4, (int, float))):
    print (f'Lo ingresado puede ser un numero entero o un decimal')
else:
    print (f'Lo ingresado puede ser algo mas')
    
if (isinstance(variable5.replace(' ', ''), (str))):
    print (f'Lo ingresado es texto')
else:
    print (f'Lo ingresado no es texto')
    
variable6 = '600'

if (variable6.isalpha()):
    print (f'Lo ingresado es texto')
elif (variable6.isnumeric()):
    print (f'Lo ingresado es un numero')
    
variable7 = 3.5

try:
    numerito1 = float(variable7)
    if (numerito1.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
Texto1 = '   esto!!! es un texto@ que DEBE    sa?narse? ya que lo que teng....o aQui no esta bien*   '

print (f'{Texto1}')

Texto1_Version1 = Texto1.lower()

print (f'{Texto1_Version1}')

Texto1_Version2 = Texto1_Version1.strip()

print (f'{Texto1_Version2}')

Texto1_Version3 = ' '.join(Texto1_Version2.split())

print (f'{Texto1_Version3}')

import re

Texto1_Version4 = re.sub(r'\!|\@|\?|\.{2,}|\*', '', Texto1_Version3)

print (f'{Texto1_Version4}')

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
    print (f'Formato incorrecto')
    exit()
    
Cargar_Csv1['FINALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrado1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()]

if (Encontrado1.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! encontramos ventas')
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_May = Grupo1.idxmax()
    Grupo1_May_Cant = Grupo1.max()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Min_Cant = Grupo1.min()
    
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_May} vendio {Grupo1_May_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Min} vendio {Grupo1_Min_Cant} unidades')
    
    Grupo2 = Grupo1.count()
    print (f'Durante la fecha {Fech1_Formateada} no compraron {Grupo2} clientes')
    print (f'La cantidad de productos vendidos en esta fecha fue de {Grupo1.sum()} unidades')
    
    print (f'La cantidad de dinero vendida en esta fecha fue de {Encontrado1['FINALITO'].sum()}')
    
print (f'-' * 20)

SetA = {1, 2, 3, 4}
SetB = set({3, 4, 5, 6})

print (f'{SetA.union(SetB)}')
print (f'{SetA | SetB}')

print (f'-' * 20)

print (f'{SetA.intersection(SetB)}')
print (f'{SetA & SetB}')

print (f'-' * 20)

print (f'{SetA.difference(SetB)}')
print (f'{SetA - SetB}')

print (f'-' * 20)

print (f'{SetB.difference(SetA)}')
print (f'{SetB - SetA}')

print (f'-' * 20)

print (f'{SetA.symmetric_difference(SetB)}')
print (f'{SetA ^ SetB}')

print (f'-' * 20)

'''SetA.update(SetB)

print (f'{SetA}')'''

'''SetA.intersection_update(SetB)
print (f'{SetA}')'''

'''SetA.difference_update(SetB)
print (f'{SetA}')'''

'''SetB.difference_update(SetA)
print (f'{SetB}')'''

'''SetA.symmetric_difference_update(SetB)
print (f'{SetA}')'''

SetC = {1, 2, 3, 4, 5}
SetD = {4, 5}
SetE = set({8})

print (f'{SetC.issuperset(SetD)}')
print (f'{SetC >= SetD}')
print (f'-' * 20)
print (f'{SetD.issubset(SetC)}')
print (f'{SetD <= SetC}')
print (f'-' * 20)
print (f'{SetC.isdisjoint(SetE)}')

print (f'-' * 20)

class Caramelo1():
    def Elegir(self):
        return f'Caramelo'
    
class Helado1:
    def __init__(self):
        self.Favorito = Caramelo1()
        
    def Comer(self):
        print (f'Te estas comiendo un helado de {self.Favorito.Elegir()}')
        
Objeto1 = Helado1()
Objeto1.Comer()

print (f'-' * 20)

class Chocolate1():
    def Elegir(self):
        return f'Chocolate'
    
class Fresa1:
    def Elegir(self):
        return f'Fresa'
    
class Vainilla1:
    def Elegir(self):
        return f'Vainilla'
    
class Helado2:
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Comer(self):
        print (f'Te estas comiendo un helado de {self.Favorito.Elegir()}')
        
Eleccion1 = Chocolate1()
Objeto2 = Helado2(Eleccion1)
Objeto2.Comer()

Eleccion2 = Fresa1()
Objeto3 = Helado2(Eleccion2)
Objeto3.Comer()

Eleccion3 = Vainilla1()
Objeto4 = Helado2(Eleccion3)
Objeto4.Comer()

print (f'-' * 20)

import re

Texto2 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Pattern1 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|org|net)'

Buscar1 = re.findall(Pattern1, Texto2)

print (f'{Buscar1}')
print (f'{type(Buscar1)}')

for indice, elemento in enumerate(Buscar1, start=1):
    print (f'{indice} -- {elemento}')
    
import re
    
Texto3 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Buscar2 = re.sub(r'\!|\?|\.{2,}|\-', '', Texto3)

print (f'{Buscar2}')

Buscar3 = re.sub(r'\d+', '', Buscar2)

print (f'{Buscar3}')

print (f'-' * 20)

print (f'{Texto3}')

Pattern2 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|org|net)'

Correo1 = re.findall(Pattern2, Texto3)

print (f'{Correo1}')

Texto3_temp = Texto3

for i, email in enumerate(Correo1, start=1):
    Texto3_temp = Texto3_temp.replace(email, f'CORREO{i}')
    
print (f'{Texto3_temp}')

Texto3_temp_Version2 = re.sub(r'\!|\?|\.{2,}', '', Texto3_temp)

print (f'{Texto3_temp_Version2}')

for i, email in enumerate(Correo1, start=1):
    Texto3_temp_Version2 = Texto3_temp_Version2.replace(f'CORREO{i}', email)
    
print (f'{Texto3_temp_Version2}')

import re

Texto4 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Pattern3 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|org|net)'

Correo2 = re.findall(Pattern3, Texto4)

print (f'{Correo2}')

Texto4_temp = Texto4

for i, email in enumerate(Correo2, start=1):
    Texto4_temp = Texto4_temp.replace(email, f'CORREO_{i}')
    
print (f'{Texto4_temp}')

Texto4_temp2 = re.sub(r'\!|\?', '', Texto4_temp)

print (f'{Texto4_temp2}')

for i, email in enumerate(Correo2, start=1):
    Texto4_temp2 = Texto4_temp2.replace(f'CORREO_{i}', email)
    
print (f'{Texto4_temp2}')

PEPE = None

try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, modulo no ubicado')

for elemento in PEPE.Diccionario_Poke:
    print (f'{PEPE.Diccionario_Poke[elemento]}')
    
print (f'-' * 20)

for elemento in PEPE.Diccionario_Poke.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in PEPE.Diccionario_Poke.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in PEPE.Diccionario_Poke.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

from Module_Own import Pokemon1 as Poke1

Objeto5 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')

Objeto5.Mostrar()

print (f'-' * 20)

print (f'Mi pokedex tiene actualmente {Objeto5.Cantidad} pokemones')

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto6 = Poke_Kid1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Acero')

Poke1.Mostrar(Objeto6)
Objeto6.Mostrar()

print (f'-' * 20)

class Veterinaria1():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso
        
    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad} años')
        print (f'Peso: {self.Peso}kgs')
        
class Perro1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        
    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        
Objeto7 = Perro1('Chester', 5, 2.8, 'Poodle', 'Hiper-tension')

Veterinaria1.Mostrar(Objeto7)
Objeto7.Mostrar()

print (f'-' * 20)

class Gato1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo
        
    def Mostrar(self):
        print (f'Color: {self.Color}')   
        print (f'Paciente_Activo: {self.Paciente_Activo}')
        
Objeto8 = Gato1('Messi', 1.5, 2, 'Gris', 'No')

Veterinaria1.Mostrar(Objeto8)
Objeto8.Mostrar()

print (f'-' * 20)

class Pajaro1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto9 = Pajaro1('Polly', 31, 0.4, 'Cacatua Roja', 'Si')

Veterinaria1.Mostrar(Objeto9)
Objeto9.Mostrar()

print (f'-' * 20)

class Atacante1():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon
        
    def Mostrar(self):
        print (f'Damage: {self.Damage}')
        print (f'Weapon: {self.Damage}')
        
class Defensor1:
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life
        
    def Mostrar(self):
        print (f'Healing: {self.Healing}')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}')
        
class Paladin1(Atacante1, Defensor1):
    def __init__(self, Damage, Weapon, Healing, Potion, Life, Name):
        Atacante1.__init__(self, Damage, Weapon)
        Defensor1.__init__(self, Healing, Potion, Life)
        self.Name = Name
        
    def Mostrar(self):
        print (f'Name: {self.Name}')
        
Objeto10 = Paladin1(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto10.Mostrar()
Atacante1.Mostrar(Objeto10)
Defensor1.Mostrar(Objeto10)

print (f'-' * 20)

class A1():
    def Mostrar(self):
        print (f'Hola A')
        
class E1():
    def Mostrar(self):
        print (f'Hola E')
        
class B1(E1):
    def Mostrar(self):
        print (f'Hola B')
        
class C1(A1):
    def Mostrar(self):
        print (f'Hola C')
        
class D1(B1, C1):
    def Mostrar(self):
        print (f'Hola D')
        
Objeto11 = D1()

A1.Mostrar(Objeto11)
B1.Mostrar(Objeto11)
C1.Mostrar(Objeto11)
Objeto11.Mostrar()
E1.Mostrar(Objeto11)

print (f'-' * 20)

class Efectivo1():
    def Pagar(self):
        print (f'El pago se realizo en efectivo')
        
class Tarjeta1:
    def Pagar(self):
        print (f'El pago se realizo en tarjeta')
        
class Cripto1:
    def Pagar(self):
        print (f'El pago se realizo en cripto')
        
Objeto12 = Cripto1()
Objeto13 = Tarjeta1()
Objeto14 = Efectivo1()

Objeto12.Pagar()
Objeto13.Pagar()
Objeto14.Pagar()

print (f'-' * 20)

class Cuenta_Bancaria1():
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
        print (f'Gracias, tu saldo a la fecha es de ${self.__Saldo}')
        
Objeto15 = Cuenta_Bancaria1(100)
Objeto15.Depositar(25)
Objeto15.Mostrar()

print (f'Tu saldo privado es de {Objeto15.Dinero}')

Objeto15.Dinero = '20,000'

Objeto15.Mostrar()
print (f'Tu saldo privado es de {Objeto15.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla1(ABC):
    @abstractmethod
    def Metodo(self):
        pass

class Primera1(Plantilla1):
    def Mostrar(self):
        print (f'Esta es la Platilla interna')
        
    def Metodo(self):
        print (f'Esta es la plantilla externa')
        
Objeto16 = Primera1()

Objeto16.Mostrar()
Objeto16.Metodo()

print (f'-' * 20)

class Animalito():
    def Seleccionar(self):
        return f'Cocodrilo'
    
class Composicion1:
    def __init__(self):
        self.Aqui = Animalito()
        
    def Mostrar(self):
        print (f'Esto que ves aqui es un {self.Aqui.Seleccionar()}')
        
Objeto17 = Composicion1()

Objeto17.Mostrar()

print (f'-' * 20)

import re

Texto5 = 'esto es un hola texto 123 ! cualq?uiera para hula@ ver si la ieeidadoei mica funciona hela'

Buscar4 = re.search(r'h.la', Texto5)

print (f'{Buscar4}')

Buscar5 = re.findall(r'h.la', Texto5)

print (f'{Buscar5}')

Buscar6 = re.fullmatch('esto es un hola texto 123 cualq\?uiera para hula\@ ver si la mica funciona hela', Texto5)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\d+', Texto5)

print (f'{Buscar7}')

Buscar8 = re.findall(r'^esto', Texto5)

print (f'{Buscar8}')

Buscar9 = re.findall(r'a$', Texto5)

print (f'{Buscar9}')

Pattern4 = r'\d{3}\s\W'

Buscar10 = re.findall(Pattern4, Texto5)

print (f'{Buscar10}')

Buscar11 = re.findall(r'[ie]{2,4}', Texto5)

print (f'{Buscar11}')

Correo3 = 'sample@sample.com'

Pattern5 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.(?:com|org|net)$'

Buscar12 = bool(re.match(Pattern5, Correo3))

if (Buscar12 == True):
    print (f'El correo electronico tiene un formato valido')
else:
    print (f'Error, formato incorrecto')
    
Correo4 = 'ericksuper80@hotmail.com'

Pattern6 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:hotmail|gmail|yahoo)\.(?:com|net|org)$'

Buscar13 = bool(re.match(Pattern6, Correo4))

if (Buscar13 == True):
    print (f'El correo electronico tiene un formato valido')
else:
    print (f'Error, formato incorrecto')
    
numerito2 = '32'

Pattern7 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar14 = bool(re.match(Pattern7, numerito2))

if (Buscar14 == True):
    print (f'El numero se encuentra entre 1 y 31')
else:
    print (f'Error, numero fuera de rango')
    
Texto6 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern8 = r'\d{2}\/[0-9]{2}\/\d{2,4}'

Replacement1 = 'XX/XX/XXXX'

Buscar15 = re.sub(Pattern8, Replacement1, Texto6)

print (f'{Buscar15}')

Pattern9 = r'\+\d{1}\-[0-9]{3}\-\d{3}\-[0-9]{2,4}'

Replacement2 = '+*-***-***-****'

Buscar16 = re.sub(Pattern9, Replacement2, Buscar15)

print (f'{Buscar16}')

print (f'-' * 20)

Texto7 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Correo5 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:hotmail|gmail|yahoo)\.(?:com|net|org)'

Buscar17 = re.findall(Correo5, Texto7)

print (f'{Buscar17}')

for indice, elemento in enumerate(Buscar17, start=1):
    print (f'{indice} -- {elemento}')
    
print (f'-' * 20)

Texto8 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Buscar18 = re.sub(r'\!|\?|\.{3}|\-', '', Texto8)

print (f'{Buscar18}')

Buscar19 = re.sub(r'\d+', '', Buscar18)

print (f'{Buscar19}')

print (f'-' * 20)

print (f'{Texto8}')

Correo6 = re.findall(r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:hotmail|gmail|yahoo)\.(?:com|org|net)', Texto8)

Texto8_temp = Texto8

print (f'{Correo6}')

for i, email in enumerate(Correo6, start=1):
    Texto8_temp = Texto8_temp.replace(email, f'PLACEHOLDER{i}')
    
print (f'{Texto8_temp}')

Texto8_temp2 = re.sub(r'\!|\?|\.{2,}', '', Texto8_temp)

print (f'{Texto8_temp2}')

for i, email in enumerate(Correo6, start=1):
    Texto8_temp2 = Texto8_temp2.replace(f'PLACEHOLDER{i}', email)
    
print (f'{Texto8_temp2}')

numerito3 = '3.5'

try:
    numerito4 = float(numerito3)
    if (numerito4.is_integer()):
        print (f'Lo que ingresaste fue un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
def Exception1(Numero):
    try:
        numerito5 = int(Numero)
    except ValueError:
        return f'Error, lo ingresado no es un numero'
    
    return f'Lo ingresado es el numero {numerito5}'
        
print (f'{Exception1(900)}')

Texto9 = "   Hola!!!   mundo@@   123   "

print (f'{Texto9}')

Texto9_version1 = Texto9.strip()

print (f'{Texto9_version1}')

Texto9_version2 = ' '.join(Texto9_version1.split())

print (f'{Texto9_version2}')

Texto9_version3 = Texto9_version2.lower()

print (f'{Texto9_version3}')

import re

Texto9_version4 = re.sub(r'\!|\@', '', Texto9_version3)

print (f'{Texto9_version4}')

def Exception2(Num1, Num2):
    try:
        Sumita = Num1 + Num2
        return f'El resultado de la sumita es {Sumita}'
    except TypeError:
        return f'Error, ambos elementos deben ser numeros'
    
print (f'{Exception2(4, "hola")}')

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        return f'El resultado de la division es {round(Divi, 2)}'
    except ZeroDivisionError:
        return f'Error, el divisor no puede ser cero'

print (f'{Exception3(7, 0)}')

Lista_Exception4 = list(['Erick', 'Josue', 'Karlita'])

def Exception4(Indice):
    try:
        return f'El elemento en la posicion {Indice} es {Lista_Exception4[Indice]}'
    except IndexError:
        return f'Error, el indice esta fuera de rango'

print (f'{Exception4(3)}')

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        return f'El elemeto en la llave {Llave} es {Diccionario_Exception5[Llave]}'
    except KeyError:
        return f'Error, la llave esta fuera de rango'
    
print (f'{Exception5("Votante")}')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Koala')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el documento seleccionado no existe')
    
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
    Documento_Agregar = Docu.write(f'\nHiena')
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
    Documento_Agregar = Docu.write(f'{' - '.join(PEPE.Set_Conjunto_Poke)}')
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

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()} y la mayor de las edades es {Data_Frame_Concatenate_Age.max()}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    elementito1 = elemento['Nombre']
    elementito2 = elemento['Edad']
    
    print (f'Mi nombre es {elementito1} y mi edad es {elementito2}')
    
print (f'-' * 20)

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()

print (f'{Grupo3}')

print (f'-' * 20)

print (f'La cantidad de personas en el dataframe son {Grupo3.count()}')

print (f'La suma total de todas las edades es {Grupo3.sum()} años')
print (f'La media de las edades es {round(Grupo3.mean(), 2)}%')

Grupo3_May = Grupo3.idxmax()
Grupo3_Min = Grupo3.idxmin()
Grupo3_May_Cant = Grupo3.max()
Grupo3_Min_Cant = Grupo3.min()

print (f'De la lista, la persona mayor es {Grupo3_May} con {Grupo3_May_Cant} años')
print (f'De la lista, la persona menor es {Grupo3_Min} con {Grupo3_Min_Cant} años')

'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x='Nombre', y='Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x='Nombre', y='Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x='Nombre', y='Edad', data=Data_Frame_Concatenate)

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
Elemento4 = Data_Frame1.loc[0, :]
Elemento5 = Data_Frame1.loc[:, 'Votante']

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
Elemento10 = Data_Frame2.iloc[:, 1]

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
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nuevo', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tiquete')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:K", index_col='cabina')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:K", index_col='cabina', nrows=1)

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

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

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

Grupo4 = Cargar_Csv2.groupby('Nombre')['Edad'].sum()

print (f'Tenemos {Grupo4.count()} personas en el csv')

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Leer_Html)

print (f'{Cargar_Html[3].head()}')

print (f'-' * 20)

Array0 = [
    [1, 2, 3], 
    [4, 5, 6]
    ]

print (f'{Array0}')

print (f'{Array0[1][2]}')
print (f'{Array0[0][::2]}')
print (f'{Array0[1][::3]}')
print (f'{Array0[1][:2]}')
print (f'{Array0[1][2:]}')
print (f'{Array0[0][2:3]}')
print (f'{Array0[1][0:None]}')
print (f'{Array0[1][:]}')
print (f'{Array0[:][0]}')

print (f'-' * 20)

for i in range(len(Array0)):
    for j in range(len(Array0[i])):
        print (f'{Array0[i][j]}')
        
print (f'-' * 20)

import numpy as np

Array1 = np.array([1, 2, 3])

print (f'{Array1}')
print (f'{Array1.ndim}') # 1
print (f'{Array1.shape}') # 1x3
print (f'{Array1.size}') # 3
print (f'{Array1.dtype}') # int64
print (f'{Array1[2]}')

print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
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
print (f'{Array2[1, 1]}')

print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[:, 1]}')
print (f'{Array2[1, 2:3]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodados: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[0, 0:None])
Sumita4 = np.sum(Array2_Sorted[0, :])

print (f'{Sumita1}')
print (f'{Sumita2}')
print (f'{Sumita3}')
print (f'{Sumita4}')

print (f'-' * 20)

Array3 = np.array([[['e', 'j', 'm'], ['a', 'c', 'x']],      [['f', 'w', 's'], ['r', 'k', 'n']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 2:3]}')

print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[0, 1, 2:3]}')
print (f'{Array3[1, 0, 0:None]}')
print (f'{Array3[1, 0, :]}')
print (f'{Array3[Array3 == "n"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],     [[[6, 5, 4], [9, 8, 7]], [[1, 4, 7], [9, 6, 3]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 
print (f'{Array4.shape}') # 
print (f'{Array4.size}') # 
print (f'{Array4.dtype}') # 
print (f'{Array4[1, 0, 1, 2]}')

print (f'{Array4[1, 0, 0, ::2]}')
print (f'{Array4[1, 1, 0, ::3]}')
print (f'{Array4[0, 1, 1, :2]}')
print (f'{Array4[0, 1, 1, 2:]}')
print (f'{Array4[1, 0, :, 0]}')
print (f'{Array4[1, 0, 1, 2:3]}')
print (f'{Array4[0, 0, 0, 0:None]}')
print (f'{Array4[0, 0, 0, :]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[0, 1, 0, 0:None])
Sumita8 = np.sum(Array4_Sorted[0, 1, 0, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_Mayor = np.max(Array_Num1)
Array_Menor = np.min(Array_Num1)

print (f'El menor de los numeros es {Array_Menor} y el mayor es {Array_Mayor}')

print (f'-' * 20)

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
print (f'{Array_Ones[0, 2:3]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 0]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value=f'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[3]}')

Lista_Array_Gen2 = list([])

for elemento in Array_Gen2:
    Lista_Array_Gen2.append(str(elemento))
    
print (f'{Array_Gen2}')
print (f'{Lista_Array_Gen2}')
print (f'{type(Lista_Array_Gen2)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[1, 0, 1, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 2]}')

print (f'-' * 20)

Tupla_Array = tuple(('Rojo', 'Verde'))
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value = Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value = Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value = Diccionario_Array['Nombre'][2:3])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'-' * 20)

print (f'{Array_Gen6[2]}')

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
print (f'{Array_Random2[0, 1]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Mean = np.mean(Array_Random2)
Array_Random2_Sum = np.sum(Array_Random2)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sum}')

print (f'-' * 20)

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Sum = Arr1 + Arr2
Rest = Arr1 - Arr2
Mult = Arr1 * Arr2
Div = Arr1 / Arr2

Array_Random1_Cien = Array_Random1 + 100

print (f'Resultado de la operacion es {Sum}')
print (f'Resultado de la operacion es {Rest}')
print (f'Resultado de la operacion es {Mult}')
print (f'Resultado de la operacion es {Div}')
print (f'Resultado de la operacion es {Array_Random1_Cien}')

print (f'-' * 20)

Array_Num8 = np.arange(start=1, stop=21, step=1)

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Lista_Array_Gen3 = ['Erick', 'Josue', 'Karlita']

Array5 = np.array(Lista_Array_Gen3)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-' * 20)

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concat([Array6, Array7])

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

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Sumita9 = np.sum(Array_Random3, axis=0)
Sumita10 = np.sum(Array_Random3, axis=1)
Sumita11 = np.sum(Array_Random3[0, 1, 0:None])
Sumita12 = np.sum(Array_Random3[0, 1, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

print (f'-' * 20)

Lista_Sorteo = []
Lista_Sorteo.append('Erick')
Lista_Sorteo.insert(1, 'Karlita')
Lista_Sorteo.extend(['Roxana', 'Josue'])
Lista_Sorteo.append('Carmelo')
Lista_Sorteo.insert(2, 'Susanita')

Ganador1 = np.random.choice(Lista_Sorteo, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Sorteo, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Sorteo, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-' * 20)

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-' * 20)

def Generadora1():
    for elemento in range(5):
        yield f'{elemento}'
        
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
            yield f'El elemento es par'
        else:
            yield f'El elemento es impar'
            
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
            yield f'El numero es Cero'
        elif (elemento == 1):
            yield f'El numero es Uno'
        elif (elemento == 2):
            yield f'El numero es Dos'
        elif (elemento == 3):
            yield f'El numero es Tres'
        elif (elemento == 4):
            yield f'El numero es Cuatro'
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

def Calculado(Lista):
    import numpy as np
    Array_Menor2 = np.min(Lista)
    Array_Mayor2 = np.max(Lista)
    
    Lista_Resultado1 = [int(Array_Menor2), int(Array_Mayor2)]
    return Lista_Resultado1

print (f'{Calculado(PEPE.Lista_Numeros)}')

print (f'-' * 20)

print (f'{PEPE.Saludar1()}')

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
    
print (f'{PEPE.Usuario(Saludar_Dos(), 'MASCULINO')}')

def Usuario_Externo():
    def Usuario_Interno(Sexo:str) -> str:
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
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nTu contrasena temporal es {PEPE.Contrasena(44)}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe 404')
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
print (f'-' * 20)
    
def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.5, 200, not False)

print (f'{Funcion_Tupla("Perro", 3.5, 200, not False)}')
print (f'{Funcion_Tupla("Perro", 3.5, 200, not False)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.5, 200, not False))}')

def Funcion_Diccionario(**kwargs):
    print (f'-' * 20)
    for elemento in kwargs:
        print (f'{kwargs[elemento]}')
        
    print (f'-' * 20)
    
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')
        
    print (f'-' * 20)
    
    for elemento in kwargs.keys():
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    for elemento in kwargs.values():
        print (f'{elemento}')
        
Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])
        
print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre} tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 2)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

if (PEPE.Any_Par == True):
    print (f'Los numeros pares de la lista son {list(Anonima3)} o incluso podrian ser {PEPE.Lista_Par}')
else:
    print (f'No hay numeros pares en la lista')
    
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

print (f'{Externa('ERICK JOSUE')}')

def Closure_Externo():
    Lista_Closure = []
    def Closure_Interno(x):
        Lista_Closure.append(x)
        return Lista_Closure
    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(23)}')
print (f'{Variable_Closure(37)}')

def Closure_Crear_Multiplicador_Externa(x):
    def Closure_Multiplicador_Interna(y):
        return x * y
    return Closure_Multiplicador_Interna

Variable_Mult1 = Closure_Crear_Multiplicador_Externa(2)
Variable_Mult2 = Closure_Crear_Multiplicador_Externa(3)

print (f'El multiplicador es {Variable_Mult1(10)}')
print (f'El multiplicador es {Variable_Mult2(10)}')

print (f'-' * 20)

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    if (Any_Impar == True):
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impares = [num for num in Lista if num % 2 != 0]
        print (f'Los numeros impares de la lista son {list(Anonima4)} o incluso podria ser {Lista_Impares}')
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
    print (f'Hola mundo')
    
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
    return f'Mi nombre es {Nombre} {Apellido}'

print (f'{Usuario2("Erick", "Perez")}')

print (f'-' * 20)

from Module_Own import Pokemon2 as Poke2

Objeto18 = Poke2(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto19 = Poke2(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto18.Mostrar()

print (f'Yo tengo {Objeto18.Cantidad} {Objeto18.Nombre}s')

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto20 = Poke_Kid2(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto20)
Objeto20.Mostrar()

print (f'-' * 20)

class Camara1():
    def Tomar_Fotografia(self):
        print (f'Fotografia Tomada')
        
class Reproductor_Musica1:
    def Reproducir_Musica(self):
        print (f'Musica Reproducida')
        
class Celular1(Camara1, Reproductor_Musica1):
    def Encender_Celular(self):
        print (f'Celular Encendido')
        
Objeto21 = Celular1()

Objeto21.Encender_Celular()
Objeto21.Reproducir_Musica()
Objeto21.Tomar_Fotografia()

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
        
Objeto22 = Perro2('Chester', 5, 2.5, 'Poodle', 'Asma')

Veterinaria2.Mostrar(Objeto22)
Objeto22.Mostrar()

print (f'-' * 20)

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente:Activo: {self.Paciente_Activo}')
        
Objeto23 = Gato2('Messi', 1.5, 1.9, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto23)
Objeto23.Mostrar()

print (f'-' * 20)

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto24 = Pajaro2('Polly', 31, 0.4, 'Cacatua Amarilla', 'Si')

Veterinaria2.Mostrar(Objeto24)
Objeto24.Mostrar()

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
        
Objeto25 = Paladin2(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto25.Mostrar()
Atacante2.Mostrar(Objeto25)
Defensor2.Mostrar(Objeto25)

print (f'-' * 20)

Objeto_Childre1 = issubclass(Poke_Kid2, Poke2)

print (f'{Objeto_Childre1}')

Objeto_Instancia1 = isinstance(Objeto25, Paladin2)
Objeto_Instancia2 = isinstance(Objeto25, Atacante2)
Objeto_Instancia3 = isinstance(Objeto25, Defensor2)

print (f'{Objeto_Instancia1}')
print (f'{Objeto_Instancia2}')
print (f'{Objeto_Instancia3}')

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
        
Objeto26 = D2()

A2.Mostrar(Objeto26)
B2.Mostrar(Objeto26)
C2.Mostrar(Objeto26)
Objeto26.Mostrar()
E2.Mostrar(Objeto26)

print (f'-' * 20)

class Efectivo2():
    def Pagar(self):
        print (f'El pago se realizo en efectivo')
        
class Tarjeta2():
    def Pagar(self):
        print (f'El pago se realizo en tarjeta')
        
class Cripto2():
    def Pagar(self):
        print (f'El pago se realizo en cripto')
        
Objeto27 = Cripto2()
Objeto28 = Tarjeta2()
Objeto29 = Efectivo2()

Objeto27.Pagar()
Objeto28.Pagar()
Objeto29.Pagar()

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
        
Objeto30 = Cuenta_Bancaria2(100)
Objeto30.Depositar(25)
Objeto30.Mostrar()

print (f'Tu saldo privado es de {Objeto30.Dinero}')

Objeto30.Dinero = '55,000,000'

Objeto30.Mostrar()

print (f'Tu saldo privado es de {Objeto30.Dinero}')

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def Generica(self):
        pass

class Primera2(Plantilla2):
    def Mostrar(self):
        print (f'Hola Amigos')
        
    def Generica(self):
        print (f'Esta es la abstraccion heradada de la clase plantilla 2')
        
Objeto31 = Primera2()

Objeto31.Mostrar()
Objeto31.Generica()

print (f'-' * 20)

class Bulbasaur():
    def Seleccionar2(self):
        return f'Bulbasaur'
    
class Inicial2:
    def __init__(self):
        self.Amigo = Bulbasaur()
        
    def Batallar(self):
        print (f'Yo te elijo {self.Amigo.Seleccionar2()}')
        
Objeto32 = Inicial2()
Objeto32.Batallar()

print (f'-' * 20)

class Bulbasaur3():
    def Seleccionar(self):
        return f'Bulbasaur'
    
class Treecko3():
    def Seleccionar(self):
        return f'Treecko'
    
class Chikorita3():
    def Seleccionar(self):
        return f'Chikorita'
    
class Inicial3:
    def __init__(self, Amigo):
        self.Amigo = Amigo
        
    def Batallar(self):
        print (f'Mi pokemon planta favorito es {self.Amigo.Seleccionar()}')
        
Borrador1 = Bulbasaur3()
Borrador2 = Treecko3()
Borrador3 = Chikorita3()

Objeto33 = Inicial3(Borrador1)
Objeto33.Batallar()

Objeto34 = Inicial3(Borrador2)
Objeto34.Batallar()

Objeto35 = Inicial3(Borrador3)
Objeto35.Batallar()

print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable8 = Lista_Uno[0]
variable9 = 'Perez'
variable10 = '''Esto
Es
Un
Long
String'''

variable11 = Sumatoria2(1, 2, 3, 4, 5, 6)
variable12 = PEPE.Division_Flotante
variable13, variable14 = True, Objeto5.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke3"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable9}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {variable11} o {Variable_Sumatoria} o incluso {Objeto6.Cantidad} pokemones')

del variable12

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable10)

print (f'Brooke' in PEPE.Tupla_Poke)
print (2 in SetA)
print (f'Koala' in PEPE.Lista2)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables con snake case {snake_case3}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto6.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Un rango de elementos de la lista 2 son {PEPE.Lista2[::2]}')
print (f'Un rango de elementos de la lista 2 son {PEPE.Lista2[::3]}')
print (f'Un rango de elementos de la lista 2 son {PEPE.Lista2[:2]}')
print (f'Un rango de elementos de la lista 2 son {PEPE.Lista2[2:]}')
print (f'Un rango de elementos de la lista 2 son {PEPE.Lista2[2:3]}')
print (f'Un rango de elementos de la lista 2 son {PEPE.Lista2[0:None]}')
print (f'Un rango de elementos de la lista 2 son {PEPE.Lista2[:]}')

print (f'{Lista_Uno[1]} eso que esta ahi es un {PEPE.Lista2[PEPE.Lista2.index("Koala")]}?')

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

Tupla1 = tuple(('Red', 'Blue', 'Green'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{Tupla1}')
print (f'{Tupla2}')
print (f'{Tupla3}')
print (f'{Tupla2[2:3]}')

Set_Conjunto1 = {Objeto6.Nombre, 'Graveler', 'Graveler', 'Graveler', 'Graveler'}
Set_Conjunto1.add(PEPE.Diccionario_Poke['Poke1'])

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Uno', 'Dos', 'Tres'})

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

SetA1 = {1, 2, 3, 4}
SetB1 = {3, 4, 5, 6}

print (f'{SetA1.union(SetB1)}')
print (f'{SetA1 | SetB1}')

print (f'-' * 20)

print (f'{SetA1.intersection(SetB1)}')
print (f'{SetA1 & SetB1}')

print (f'-' * 20)

print (f'{SetA1.difference(SetB1)}')
print (f'{SetA1 - SetB1}')

print (f'-' * 20)

print (f'{SetB1.difference(SetA1)}')
print (f'{SetB1 - SetA1}')

print (f'-' * 20)

print (f'{SetA1.symmetric_difference(SetB1)}')
print (f'{SetA1 ^ SetB1}')

print (f'-' * 20)

'''SetA1.update(SetB1)

print (f'{SetA1}')'''

'''SetA1.intersection_update(SetB1)

print (f'{SetA1}')'''

'''SetA1.difference_update(SetB1)

print (f'{SetA1}')'''

'''SetB1.difference_update(SetA1)

print (f'{SetB1}')'''

'''SetA1.symmetric_difference_update(SetB1)

print (f'{SetA1}')'''

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})

Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, 'ChocoFresa'})

print (f'{Set_Conjunto_Menu1.union(Set_Conjunto_Menu2)}')

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : 37,
    'Votante' : not False
}

Diccionario2 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
}

Diccionario3 = dict({'Ingresos' : 500, 'Gastos' : 200, 'Vacio' : "q"})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1["Nombre"]}')
print (f'{Diccionario1.get("Edad")}')

print (f'-' * 20)

Diccionario1['Nombre'] = variable8

print (f'{Diccionario1}')

del Diccionario1['Nombre']
Diccionario1.pop('Edad')

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')

Diccionario1 = dict({
    1 : "Karlita",
    2 : 6,
    3 : False
})

print (f'{Diccionario1[1]} no puede votar ya que solo tiene {Diccionario2['Edad'][2]} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', PEPE.Diccionario_Poke['Poke2'])
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])

Diccionario_Vacio2['Dos'] = PEPE.Lista2[2]

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')

Lista_Dict1 = ['Erick', 'Josue', 'Perez', 'Gutierrez']

Key1 = [f'Key_{i}' for i in range(len(Lista_Dict1))]

print (f'{Key1}')

Diccionario4 = dict(zip(Key1, Lista_Dict1))

print (f'{Diccionario4}')

print (f'-' * 20)

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
    
import pandas as pd
    
Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

print (f'-' * 20)

Set_Conjunto_Dict2 = set(Cargar_Csv3['product'])

print (f'{Set_Conjunto_Dict2}')

Key2 = [f'Key_{i}' for i in range(len(Set_Conjunto_Dict2))]

Diccionario5 = dict(zip(Key2, Set_Conjunto_Dict2))

for elemento in Diccionario5.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20 % 6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'El tipo de dato de la variable es {type(variable8)}')
print (f'El tipo de dato de la variable es {type(Variable_Sumatoria)}')
print (f'El tipo de dato de la variable es {type(Objeto6.Catched)}')
print (f'El tipo de dato de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de dato de la variable es {type(Tupla1)}')
print (f'El tipo de dato de la variable es {type(Funcion_Diccionario)}')
print (f'El tipo de dato de la variable es {type(Objeto7)}')
print (f'El tipo de dato de la variable es {type(Array1)}')
print (f'El tipo de dato de la variable es {type(Data_Frame_Concatenate)}')
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
        
variable15 = 'Josue'
variable16 = 37

if (variable15 == 'Erick' and variable16 >= 30):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una condicion no se cumple')
    
if (variable15 == 'Erick' or variable16 >= 50):
    print (f'Al menos una condicion se cumple')
else:
    print (f'Error, ninguna condicion se cumple')
    
print (f'{dir(variable15)}')
print (f'{help(variable15)}')

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Variable_Sumatoria
        self.Classified = True

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')
        
Objeto36 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto5.Nombre)
Objeto37 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto6.Nombre)
Objeto38 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto7.Nombre)

Objeto36.Desplegar()

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
    print (f'{indice} -- {elemento}')
    
variable17 = 'eSteBAN'
variable17_letra = variable17[0]

print (f'{variable17}')
print (f'{variable17.lower()}')
print (f'{variable17.upper()}')
print (f'{variable17.capitalize()}')

print (f'{variable17.lower().find("t")}')
print (f'{variable17.lower().index("b")}')

print (f'{variable17.lower().startswith(variable17_letra)}')
print (f'{variable17.lower().endswith("n")}')

print (f'La letra {variable17_letra} aparece un total de {variable17.lower().count(variable17_letra)} veces')

print (f'{variable17.lower().replace("ban", "POPOTAMO")}')

variable18 = 'esto es un texto de ejemplo para probar si la mica funciona'

Lista_variable18 = variable18.split(' ')

for elemento in Lista_variable18:
    print (f'{elemento}')
    
print (f'La cantidad de palabras digitadas es de {len(Lista_variable18)} palabras')

variable19 = '36'

if (variable19.isalpha()):
    print (f'Lo ingresado es texto')
else:
    print (f'Error, lo ingresado no es texto')
    
if (isinstance(variable19, (str))):
    print (f'Lo ingresado es texto')
else:
    print (f'Lo ingresado no es texto')
    
variable20 = 3.4

try:
    toto = float(variable20)
    if (toto.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado no es un numero')
    
variable21 = 500
   
print (f'{PEPE.Tupla_Poke[2]} aparece en la posicion {PEPE.Tupla_Poke.index("Misty")}')

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1
    
print (f'-' * 20)

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1
    
print (f'-' * 20)

Lista_Animales = ['Jirafa']
Lista_Animales.append('Cocodrilo')
Lista_Animales.insert(1, PEPE.Lista2[2])
Lista_Animales.extend(['Avestruz'])

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador == 'Cocodrilo']):
        print (f'Esto es un reptil')
        break
    else:
        Contador+= 1
        continue
    
for elemento1, elemento2 in zip(Lista_Animales, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
Lista_Numeros_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Menor = min(Lista_Numeros_Mult)
Mayor = max(Lista_Numeros_Mult)
Redondeado = round(14.458795, 2)

print (f'{Menor}')
print (f'{Mayor}')
print (f'{Redondeado}')

print (f'{bool('')}')
print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool(False)}')
print (f'{bool(not True)}')

Todo_All = all([Lista_Numeros_Mult, Tupla1, Set_Conjunto_Menu1, None])

print (f'{Todo_All}')

Sumatoria4 = sum(Lista_Numeros_Mult)

print (f'El resultado de la sumatoria es {Sumatoria4}')

Uno = str(500)
Dos = int('500')
Tres = float(Uno)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')

print (f'- -'.join(PEPE.Set_Conjunto_Poke))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

print (f'-' * 20)

'''def Floating1(Elemento):
    if (len(Elemento) != 0):
        try:
            numerito = int(Elemento)
            if (numerito.is_integer()):
                Resultado = Variable_Sumatoria * numerito + Objeto6.Cantidad
                print (f'El resultado de la operacion es {Resultado}')
            else:
                print (f'Lo ingresado es un numero decimal')
        except ValueError:
            print (f'Error, lo ingresado no es un numero entero')
    else:
        print (f'Error, ingrese una cadena de texto')

Floating1(PEPE.Flotante1)

Resultado2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado2}')

def Floating3(Cadena):
    if (bool(Cadena) == True):
        if (Cadena.isalpha()):
            Cadenita = Cadena.replace(' ', '')
            if (isinstance(Cadenita, (str))):
                print (f'Lo ingresado es texto')
            else:
                print (f'Error, esto no es texto')
        else:
            print (f'Error, lo ingresado no es una cadena de texto')
    else:
        print (f'Error, ingrese una cadena de texto')

Floating3(PEPE.Flotante3)'''

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento}: ')
        Lista.append(Alumno)
        
    return Lista

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nLa lista de estudiantes es {Colegio(Lista_Alumnos)}: '])
    Docu.close()
    
with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
Lista_Alumnos2 = list([])

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio2(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda Num : Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes es {Menore} ({Lista[0][1]}) y el mayor de los estudiantes es {Mayore} ({Lista[-1][1]})')
    
Colegio2(Lista_Alumnos2)'''

'''def Exception_Finale():
    while True:
        Numerito = input(f'Ingrese un numero entero: ')
        try:
            Finale_Numerito = int(Numerito)
            break
        except:
            print (f'Error, el numero no es entero')
    return Finale_Numerito
            
print (f'Gracias, el numero ingresado es {Exception_Finale()}')'''

import re

Correo7 = 'example@example.com'

Pattern10 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.(?:com|org|net)$'

Buscar20 = bool(re.match(Pattern10, Correo7))

if (Buscar20 == True):
    print (f'El correo electronico tiene un formato valido')
else:
    print (f'Error, formato invalido')
    
import pandas as pd
from datetime import datetime

Ruta_Csv4 = 'C:\\Repo\\Store.csv'

Cargar_Csv4 = pd.read_csv(Ruta_Csv4)

print (f'{Cargar_Csv4}')

print (f'-' * 20)

Fecha2 = '2026-04-01'

try:
    Fech2 = datetime.strptime(Fecha2, '%Y-%m-%d').date()
    Fech2_Formateada = pd.to_datetime(Fech2)
    Cargar_Csv4['date'] = pd.to_datetime(Cargar_Csv4['date'])
except ValueError:
    print (f'Error, formato de fecha incorrecto')
    
Cargar_Csv4['FINALITO'] = Cargar_Csv4['quantity'] * Cargar_Csv4['price']
    
Encontrado2 = Cargar_Csv4[Cargar_Csv4['date'].dt.date == Fech2_Formateada.date()]

if (Encontrado2.empty):
    print (f'No hay ventas en esta fecha')
else:
    print (f'Genial! encontramos ventas')
    Grupo5 = Encontrado2.groupby('product')['quantity'].sum()
    Grupo5_May = Grupo5.idxmax()
    Grupo5_Min = Grupo5.idxmin()
    Grupo5_May_Cant = Grupo5.max()
    Grupo5_Min_Cant = Grupo5.min()
    
    print (f'En la fecha {Fech2_Formateada} el producto {Grupo5_May} vendio {Grupo5_May_Cant} unidades')
    print (f'En la fecha {Fech2_Formateada} el producto {Grupo5_Min} vendio {Grupo5_Min_Cant} unidades')
    
    Grupo6 = Grupo5.count()
    
    print (f'En esta fecha recibimos {Grupo6} clientes')
    print (f'El total de productos vendidos en esta fecha fue de {Grupo5.sum()} productos')
    
    Grupo7 = Encontrado2.groupby('product')['FINALITO'].sum()
    
    print (f'El total de dinero vendido en {Fech2_Formateada} fue de ${Grupo7.sum()}')


class Especiales:
    def __str__(self):
        return f'Esto es un metodo especial'
    
Objeto39 = Especiales()

print (f'{Objeto39}')

class Especiales2():
    def __len__(self):
        return 500
    
Objeto40 = Especiales2()

print (f'{len(Objeto40)}')
