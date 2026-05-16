Elemento1 = 'hola'

if (isinstance(Elemento1, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero entero')
    
try:
    Numero1 = float(Elemento1)
    if (Numero1.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado nisiquiera es un numero')
    
Elemento2 = '600'

if (isinstance(Elemento2, (int, float))):
    print (f'Lo ingresado es un numero entero o decimal')
else:
    print (f'Lo ingresado no es un numero')
    
'''Lista_Numeros = []

Contador = 0

while (Contador < 3):
    Numero2 = input(f'Ingrese el numero {Contador + 1}: ')
    try:
        Numerito2 = float(Numero2)
        if (Numerito2.is_integer()):
            Lista_Numeros.append(Numerito2)
            Contador += 1
        else:
            Lista_Numeros.append(Numerito2)
            Contador += 1
    except ValueError:
        print (f'Error, lo ingresado no es un numero')
        
Promedio = sum(Lista_Numeros) / len(Lista_Numeros)

print (f'El resultado del promedio es {round(Promedio, 2)}')'''

Texto1 = "   Hola!!!   mundo@@   123   "

print (f'{Texto1}')

Texto1_Version1 = Texto1.strip()

print (f'{Texto1_Version1}')

Texto1_Version2 = ' '.join(Texto1_Version1.split())

print (f'{Texto1_Version2}')

Texto1_Version3 = Texto1_Version2.lower()

print (f'{Texto1_Version3}')

import re

Texto1_Version4 = re.sub(r'[^a-zA-Z0-9\s]', '', Texto1_Version3)

print (f'{Texto1_Version4}')

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
    print (f'Error, la fecha tiene un formato incorrecto')
    exit()
    
Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrada1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()]

if (Encontrada1.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    Grupo1 = Encontrada1.groupby('product')['quantity'].sum()
    Grupo1_May = Grupo1.idxmax()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_May_Cant = Grupo1.max()
    Grupo1_Min_Cant = Grupo1.min()
    
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_May} vendio {Grupo1_May_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Min} vendio {Grupo1_Min_Cant} unidades')
    
    print (f'En la fecha {Fech1_Formateada} {Grupo1.count()} clientes realizaron compras')
    print (f'De estos clientes, la cantidad de productos inndividuales vendidos fue de {Grupo1.sum()}')
    
    Grupo2 = Encontrada1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendida en {Fech1_Formateada} fue de {Grupo2.sum()} y la media de estas ventas es de {Grupo2.mean()}')
    
print (f'-' * 20)

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


print (f'{SetB1.difference(SetA1)}')
print (f'{SetB1 - SetA1}')

print (f'-' * 20)

print (f'{SetA1.symmetric_difference(SetB1)}')
print (f'{SetA1 ^ SetB1}')

print (f'-' * 20)

SetC1 = {1, 2, 3, 4, 5}
SetD1 = {4, 5}
SetE1  = set({8}) #type : ignore

print (f'{SetC1.issuperset(SetD1)}')
print (f'{SetC1 >= SetD1}')
print (f'-' * 20)
print (f'{SetD1.issubset(SetC1)}')
print (f'{SetD1 <= SetC1}')
print (f'-' * 20)
print (f'{SetC1.isdisjoint(SetE1)}')

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

class Bulbasaur1():
    def Elegir(self):
        return f'Bulbasaur'
    
class Batalla1:
    def __init__(self):
        self.Favorito = Bulbasaur1()
        
    def Batallar(self):
        print (f'{self.Favorito.Elegir()} yo te elijo!!!')
        
Objeto1 = Batalla1()
Objeto1.Batallar()

print (f'-' * 20)

class Bulbasaur2():
    def Elegir(self):
        return f'Bulbasaur'
    
class Treecko2:
    def Elegir(self):
        return f'Treecko'
    
class Chikorita2:
    def Elegir(self):
        return f'Chikorita'
    
class Batalla2: #type: ignore
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'{self.Favorito.Elegir()}, yo te elijo!!!')
        
Sample1 = Bulbasaur2()
Objeto2 = Batalla2(Sample1)
Objeto2.Batallar()

Sample2 = Treecko2()
Objeto3 = Batalla2(Sample2)
Objeto3.Batallar()

Sample3 = Chikorita2()
Objeto4 = Batalla2(Sample3)
Objeto4.Batallar()

print (f'-' * 20)

import re

# usuario@dominio.extension

Texto2 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Pattern1 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:hotmail|yahoo|gmail)\.(?:com|net|org)'

Buscar1 = re.findall(Pattern1, Texto2)

print (f'{Buscar1}')

for elemento in enumerate(Buscar1):
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

import re

Texto3 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Buscar2 = re.sub(r'\!|\?|\.{2,}', '', Texto3)

print (f'{Buscar2}')

Buscar3 = re.sub(r'\d{3,}\-[0-9]{2,4}', '', Buscar2)

print (f'{Buscar3}')

print (f'-' * 20)

import re

Texto4 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Correos1 = re.findall(r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)', Texto4)

print (f'{Correos1}')

Texto4_temp1 = Texto4

for i, email in enumerate(Correos1, start=1):
    Texto4_temp1 = Texto4_temp1.replace(email, f'DRAFT{i}')
    
print (f'{Texto4_temp1}')

Texto4_temp2 = re.sub(r'\!|\?|\.{2,}|\-', '', Texto4_temp1)

print (f'{Texto4_temp2}')

Texto4_temp3 = re.sub(r'\d{3,}', '', Texto4_temp2)

print (f'{Texto4_temp3}')

for i, email, in enumerate(Correos1, start=1):
    Texto4_temp3 = Texto4_temp3.replace(f'DRAFT{i}', email)
    
print (f'{Texto4_temp3}')

print (f'-' * 20)

import re

Texto5 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Correos2 = re.findall(r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)', Texto5)

print (f'{Correos2}')

Texto5_temp1 = Texto5

for i, email in enumerate(Correos2, start=1):
    Texto5_temp1 = Texto5_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto5_temp1}')

Texto5_temp2 = re.sub(r'\!|\?|\.{2,}', '', Texto5_temp1)

print (f'{Texto5_temp2}')

for i, email in enumerate(Correos2, start=1):
    Texto5_temp2 = Texto5_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto5_temp2}')

print (f'-' * 20)

try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo elegido no existe')
    raise
    
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
Objeto6 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto5.Mostrar()

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto7 = Poke_Kid1(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto7)
Objeto7.Mostrar()

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
        
Objeto8 = Perro1('Chester', 5, 2.8, 'Poodle', 'Asma')

Veterinaria1.Mostrar(Objeto8)
Objeto8.Mostrar()

print (f'-' * 20)

class Gato1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')
        
Objeto9 = Gato1('Messi', 1.5, 2.1, 'Gris', 'No')

Veterinaria1.Mostrar(Objeto9)
Objeto9.Mostrar()

print (f'-' * 20)

class Pajaro1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
    
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto10 = Pajaro1('Polly', 31, 0.4, 'Guacamaya', 'Si')

Veterinaria1.Mostrar(Objeto10)
Objeto10.Mostrar()

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
        print (f'Life: {self.Life}pts')
        
class Paladin1(Atacante1, Defensor1):
    def __init__(self, Damage, Weapon, Healing, Potion, Life, Name):
        Atacante1.__init__(self, Damage, Weapon)
        Defensor1.__init__(self, Healing, Potion, Life)
        self.Name = Name
        
    def Mostrar(self):
        print (f'Name: {self.Name}')
        
Objeto11 = Paladin1(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto11.Mostrar()
Atacante1.Mostrar(Objeto11)
Defensor1.Mostrar(Objeto11)

print (f'-' * 20)

class A1():
    def Mostrar(self):
        print (f'Hola A1')
        
class E1():
    def Mostrar(self):
        print (f'Hola E1')
        
class B1(E1):
    def Mostrar(self):
        print (f'Hola B1')
        
class C1(A1):
    def Mostrar(self):
        print (f'Hola C1')
        
class D1(B1, C1):
    def Mostrar(self):
        print (f'Hola D1')
        
Objeto12 = D1()

A1.Mostrar(Objeto12)
B1.Mostrar(Objeto12)
C1.Mostrar(Objeto12)
Objeto12.Mostrar()
E1.Mostrar(Objeto12)

print (f'-' * 20)

class Efectivo1():
    def Pagar(self):
        print (f'El pago se realizo en efectivo')
        
class Tarjeta1:
    def Pagar(self):
        print (f'El pago se realizo en tarjeta')
        
class Paypal1:
    def Pagar(self):
        print (f'El pago se realizo en paypal')
        
Objeto13 = Paypal1()
Objeto14 = Tarjeta1()
Objeto15 = Efectivo1()

Objeto13.Pagar()
Objeto14.Pagar()
Objeto15.Pagar()

print (f'-' * 20)

class Cuenta_Bancaria:
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
        
Objeto16 = Cuenta_Bancaria(100)
Objeto16.Depositar(25)
Objeto16.Mostrar()

print (f'Tu saldo privado es de {Objeto16.Dinero}')

Objeto16.Dinero = '50,000,000'

Objeto16.Mostrar()

print (f'Tu saldo privado es de {Objeto16.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla1(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla1(Plantilla1):
    def Mostrar(self):
        print (f'Aqui se muestra el mensaje de la SUB PLANTILLA')
        
    def General(self):
        print (f'Este metodo es obligatorio')
        
Objeto17 = Sub_Plantilla1()

Objeto17.Mostrar()
Objeto17.General()

print (f'-' * 20)

class Chocolate1:
    def Elegir(self):
        return f'Chocolate'
    
class Helado1:
    def __init__(self):
        self.Favorito = Chocolate1()
        
    def Mostrar(self):
        print (f'Haz elegido un helado de {self.Favorito.Elegir()}')
        
Objeto18 = Helado1()
Objeto18.Mostrar()

import re

Texto6 = 'Esto @ es 89 un texto hola cualquiera con!! el hala que voy 1 a practica mis habi_lidades hela 321 * de python'

Buscar4 = re.search(r'h.la', Texto6)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\d+', Texto6)

print (f'{Buscar5}')

Buscar6 = re.fullmatch(r'Esto @ es 89 un texto hola cualquiera con!! el hala que voy 1 a practica mis habi_lidades hela 321 _ de python', Texto6)

print (f'{Buscar6}')

Buscar7 = re.findall(r'h.la', Texto6)

print (f'{Buscar7}')

Buscar8 = re.findall(r'\d{3}\s{1}\W{1}', Texto6)

print (f'{Buscar8}')

Buscar9 = re.findall(r'(?:[ai]|[be])', Texto6)

print (f'{Buscar9}')

import re

Correos3 = 'sample@sample.com'

Pattern2 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.(?:com|net|org)$'

Buscar10 = bool(re.fullmatch(Pattern2, Correos3))

if (Buscar10 == True):
    print (f'El correo electronico tiene un formato valido')
else:
    print (f'Error, formato invalido')
    
print (f'-' * 20)

'''Lista_Numeros = []

Contador = 0

while (Contador < 3):
    Numerito = input(f'Ingrese el numero {Contador + 1}: ')
    try:
        Numerito2 = float(Numerito)
        if (Numerito2.is_integer()):
            Lista_Numeros.append(Numerito2)
            Contador += 1
        else:
            Lista_Numeros.extend([Numerito2])
            Contador += 1
    except ValueError:
        print (f'Error, lo ingresado no es un numero')
        
Promedio = sum(Lista_Numeros) / Lista_Numeros.__len__()

print (f'El promedio del estudiante es {round(Promedio, 2)}')'''

'''Lista_Texto = []

Contador = 0

while (Contador < 3):
    Textico1 = input(f'Ingrese el textico {Contador + 1}: ')
    try:
        Textico2 = str(Textico1)
        if (Textico2.isalpha()):
            Lista_Texto.append(Textico2)
            Contador += 1
        else:
            print (f'Error, lo ingresado no es texto')
    except ValueError:
        print (f'Fatal Error, I need you to enter text!')
        
for elemento in Lista_Texto:
    print (f'{elemento}')'''
    
import re

Correos4 = 'ericksuper80@hotmail.com'

Pattern3 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:hotmail|gmail|yahoo)\.(?:com|net|org)$'

Buscar11 = bool(re.match(Pattern3, Correos4))

if (Buscar11 == True):
    print (f'El correo tiene formato valido')
else:
    print (f'Error, formato invalido')
    
import re
    
Numero2 = '01'

Pattern4 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar12 = bool(re.match(Pattern4, Numero2))

if (Buscar12 == True):
    print (f'El numero se encuentra entre 01 y 31')
else:
    print (f'Error, numero fuera de rango')
    
import re
    
Texto7 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern5 = r'\d{2}\/[0-9]{2}\/\d{3,4}'

Replacement1 = 'XX/XX/XXXX'

Buscar13 = re.sub(Pattern5, Replacement1, Texto7)

print (f'{Buscar13}')

Pattern6 = r'\+[0-9]{1}\-\d{3}\-[0-9]{3}\-\d{2,4}'

Replacement2 = '+*-***-***-****'

Buscar14 = re.sub(Pattern6, Replacement2, Buscar13)

print (f'{Buscar14}')

import re

Texto8 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Pattern7 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|org|net)'

Buscar15 = re.findall(Pattern7, Texto8)

for indice, elemento in enumerate(Buscar15, start=1):
    print (f'{indice} -- {elemento}')
    
import re

Texto9 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Buscar16 = re.sub(r'\!|\?|\.{2,}', '', Texto9)

print (f'{Buscar16}')

Buscar17 = re.sub(r'\d{4}\-[0-9]{2,4}', '', Buscar16)

print (f'{Buscar17}')

Numero3 = '70'

try:
    Num1 = float(Numero3)
    if (Num1.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

Texto10 = "   Hola!!!   mundo@@   123   "

Texto10_Version1 = Texto10.strip()
Texto10_Version2 = ' '.join(Texto10_Version1.split())
Texto10_Version3 = Texto10_Version2.lower()

import re

Texto10_Version4 = re.sub(r'\!|\@', '', Texto10_Version3)

print (f'{Texto10_Version4}')

def Exception1(Elemento):
    try:
        Num2 = float(Elemento)
        if (Num2.is_integer()):
            print (f'Lo ingresado es un numero entero')
        else:
            print (f'Lo ingresado es un numero decimal')
    except ValueError:
        print (f'Error, lo ingresado no es un numero')

Exception1('hola')

def Exception2(Num1, Num2):
    try:
        Num3 = float(Num1)
        Num4 = float(Num2)
        if (Num3.is_integer() and (Num4.is_integer())):
            Sumita = Num3 + Num4
            print (f'El resultado de la sumita es {Sumita}')
        else:
            Sumita = Num3 + Num4
            print (f'El resultado de la sumita es {round(Sumita, 2)}')
    except TypeError:
        print (f'Error, necesito que ambos elementos sean numeros')
        
Exception2('12', 9)

def Exception3(Num1, Num2):
    try:
        Sumita = Num1 + Num2
        print (f'El resultado de la sumita es {Sumita}')
    except TypeError:
        print (f'Error, necesito que ambos elementos sean numeros')
        
Exception3(12, "Hola")

def Exception4(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, El divisor no puede ser cero')
        
Exception4(14, 0)

Lista_Exception5 = list([])
Lista_Exception5.append('Erick')
Lista_Exception5.insert(1, 'Josue')
Lista_Exception5.extend(['Karlita'])

def Exception5(Indice):
    try:
        print (f'El elemento en el indice {Indice} es {Lista_Exception5[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')
        
Exception5(3)

Diccionario_Exception6 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception6(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception6[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')
        
Exception6('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Hiena')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado 404')
    
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
    Documento_Agregar = Docu.write(f'\n{PEPE.Lista2[PEPE.Lista2.index("Koala")]}')
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

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame1}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate_Age}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_May = Grupo3.idxmax()
Grupo3_Min = Grupo3.idxmin()

print (f'La persona menor de la lista es {Grupo3_Min} y su edad es {Data_Frame_Concatenate_Age.min()}')
print (f'La persona mayor de la lista es {Grupo3_May} y su edad es {Data_Frame_Concatenate_Age.max()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    uno = elemento['Nombre']
    dos = elemento['Edad']
    
    print (f'Mi nombre es {uno} y mi edad es {dos} años')
    
print (f'-' * 20)

print (f'La cantidad de personas en la lista son {Grupo3.count()}')
print (f'Digamos que queremos sumar todas las edades, te imaginas? el numero seria algo como {Grupo3.sum()}')
print (f'La media de las edades es {round(Grupo3.mean(), 2)}%')

'''import pandas as pd
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

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'-' * 20)

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'El numero de Filas es {Filas}')
print (f'El numero de Columnas es {Columnas}')

Elemento3 = Data_Frame1.loc[0, 'Nombre']
Elemento4 = Data_Frame1.loc[1, 'Edad']
Elemento5 = Data_Frame1.loc[2, 'Votante']
Elemento6 = Data_Frame1.loc[0, :]
Elemento7 = Data_Frame1.loc[:, "Votante"]

print (f'{Elemento3}')
print (f'{Elemento4}')
print (f'{Elemento5}')
print (f'{Elemento6}')
print (f'{Elemento7}')

print (f'-' * 20)

Elemento8 = Data_Frame2.iloc[0, 0]
Elemento9 = Data_Frame2.iloc[1, 1]
Elemento10 = Data_Frame2.iloc[2, 2]
Elemento11 = Data_Frame2.iloc[1, :]
Elemento12 = Data_Frame2.iloc[:, 2]

print (f'{Elemento7}')
print (f'{Elemento9}')
print (f'{Elemento10}')
print (f'{Elemento11}')
print (f'{Elemento12}')

print (f'-' * 20)

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine='openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'-' * 20)

Cargar_Excel1 = pd.read_excel(Ruta_Excel, sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, index_col='tarifa')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:J', index_col='tarifa')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:J', index_col='tarifa', nrows=1)

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

Array0 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print (f'{Array0}')
print (f'{Array0[2][1]}')
print (f'{Array0[0][:2]}')
print (f'{Array0[0][2:]}')
print (f'{Array0[1][::2]}')
print (f'{Array0[0][::3]}')
print (f'{Array0[1][0:None]}')
print (f'{Array0[1][:]}')
print (f'{Array0[0][2:3]}')

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
print (f'{Array1[1]}')

print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[2:3]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 <= 2]}')

print (f'-' * 20)

Array2 = np.array([[1, 2, 3],   [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 2]}')

print (f'{Array2[1, ::2]}')
print (f'{Array2[0, ::3]}')
print (f'{Array2[0, :2]}')
print (f'{Array2[0, 2:]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[1, 2:3]}')
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
Sumita3 = np.sum(Array2_Sorted[0, 0:None])
Sumita4 = np.sum(Array2_Sorted[0, :])

print (f'El resultado de la sumita es {Sumita1}')
print (f'El resultado de la sumita es {Sumita2}')
print (f'El resultado de la sumita es {Sumita3}')
print (f'El resultado de la sumita es {Sumita4}')

print (f'-' * 20)

Array3 = np.array([[['a', 'b', 'c'], ['f', 'x', 'e']],    [['w', 'o', 'm'], ['k', 'j', 'i']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 2]}')

print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[1, :, 0]}')
print (f'{Array3[0, 0, 2:3]}')
print (f'{Array3[1, 1, 0:None]}')
print (f'{Array3[1, 1, :]}')
print (f'{Array3[Array3 == "b"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],      [[[6, 5, 4], [9, 8, 7]], [[1, 5, 9], [8, 6, 7]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[0, 1, 0, 2]}')

print (f'{Array4[1, 0, 1, ::2]}')
print (f'{Array4[1, 0, 0, ::3]}')
print (f'{Array4[0, 1, 0, :2]}')
print (f'{Array4[0, 1, 0, 2:]}')
print (f'{Array4[1, 0, :, 1]}')
print (f'{Array4[1, 0, 1, 2:3]}')
print (f'{Array4[1, 1, 1, 0:None]}')
print (f'{Array4[1, 1, 1, :]}')
print (f'{Array4[Array4 <= 2]}')

print (f'-' * 20)

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

Array_Num1 = np.arange(start=1, stop=11, step=1) # type: ignore

print (f'{Array_Num1}')

Array_Mayor = np.max(Array_Num1)
Array_Menor = np.min(Array_Num1)

print (f'El menor de los numeros es {Array_Menor} y el mayor es {Array_Mayor}')

print (f'-' * 20)

Array_Num2 = np.arange(start=1, stop=26, step=1) #type: ignore

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
print (f'{Array_Gen1[1, 2]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value=f'Fuecoco')

print (f'{Array_Gen2}')

Lista_Gen2 = []

for elemento in enumerate(Array_Gen2):
    Lista_Gen2.extend([str(elemento[1])])
    
print (f'{Lista_Gen2}')
print (f'{type(Lista_Gen2)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value = f'{Array4[0, 1, 0, 2:3]}')

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 1]}')

print (f'-' * 20)

Tupla_Array = tuple(('Uno', 'Dos'))
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value = Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value = Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value = Diccionario_Array["Nombre"][1])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'-' * 20)

print (f'{Array_Gen6[3]}')

print (f'-' * 20)

Array_Num3 = np.arange(start=1, stop=6, step=1) #type: ignore
Array_Num4 = np.arange(start=2, stop=11, step=2) #type: ignore
Array_Num5 = np.arange(start=3, stop=31, step=3) #type: ignore
Array_Num6 = np.arange(start=2, stop=21, step=2) #type: ignore
Array_Num7 = np.arange(10) #type: ignore

print (f'{Array_Num3}')
print (f'{Array_Num4}')
print (f'{Array_Num5}')
print (f'{Array_Num6}')
print (f'{Array_Num7}')

print (f'-' * 20)

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')
print (f'{Array_Random1.ndim}')
print (f'{Array_Random1.size}')
print (f'{Array_Random1.shape}')
print (f'{Array_Random1.dtype}')
print (f'{Array_Random1[8]}')

print (f'-' * 20)

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')
print (f'{Array_Random2.ndim}')
print (f'{Array_Random2.shape}')
print (f'{Array_Random2.size}')
print (f'{Array_Random2.dtype}')
print (f'{Array_Random2[1, 2]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

print (f'-' * 20)

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Suma = Arr1 + Arr2
Resta = Arr1 - Arr2
Multiplicacion = Arr1 * Arr2
Division = Arr1 / Arr2
Array_Random1_Cien = Array_Random1 + 100

print (f'El resultado de la operacion es {Suma}')
print (f'El resultado de la operacion es {Resta}')
print (f'El resultado de la operacion es {Multiplicacion}')
print (f'El resultado de la operacion es {Division}')
print (f'El resultado de la operacion es {Array_Random1_Cien}')

print (f'-' * 20)

Array_Num8 = np.arange(start=1, stop=21, step=1) #type: ignore

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Lista_Array = list(['Erick', 'Josue', 'Karlita'])

Array5 = np.array(Lista_Array)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-' * 20)

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1) #type: ignore

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

for Matriz1 in Array3:
    for Fila in Matriz1:
        print (f'{Fila}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Array_Random3_Column_Min = np.min(Array_Random3, axis=0)
Array_Random3_Column_Max = np.max(Array_Random3, axis=0)
Array_Random3_Row_Min = np.min(Array_Random3, axis=1)
Array_Random3_Row_Max = np.max(Array_Random3, axis=1)

print (f'Los menore de las columnas son {Array_Random3_Column_Min}')
print (f'Los mayore de las columnas son {Array_Random3_Column_Max}')
print (f'Los menore de las filas son {Array_Random3_Row_Min}')
print (f'Los mayore de las filas son {Array_Random3_Row_Max}')

print (f'-' * 20)

Lista_Array2 = ['Erick']
Lista_Array2.append('Josue')
Lista_Array2.insert(2, 'Karlita')
Lista_Array2.extend(['Roxana', 'Carmelo'])
Lista_Array2.insert(3, 'Susanita')

Ganador1 = np.random.choice(Lista_Array2, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Array2, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Array2, size=(2, 3), replace=False)

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
            yield f'EVEN'
        else:
            yield f'ODD'
            
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
            yield f'Cero'
        elif (elemento == 1):
            yield f'One'
        elif (elemento == 2):
            yield f'Two'
        elif (elemento == 3):
            yield f'Three'
        elif (elemento == 4):
            yield f'Four'
        else:
            yield f'Error de codigo'
            
Gen3 = Generadora3()

try:
    print (f'{next(Gen3)}')
except StopIteration:
    print (f'El experimento termina aqui')
    
print (f'-' * 20)

Lista0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Evaluadora(Elementos):
    Menor = min(Elementos)
    import numpy as np
    Mayor = np.max(Elementos)
    
    Lista_Resultado = [Menor, int(Mayor)]
    return Lista_Resultado

print (f'La lista resultado es {Evaluadora(Lista0)}')

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
    print (f'You are a man')
else:
    print (f'You are a woman')
    
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

Variable_Funcion_Tupla = Funcion_Tupla(PEPE.Division_Flotante, 25, PEPE.Lista2[2], not True)

print (f'{Funcion_Tupla(PEPE.Division_Flotante, 25, PEPE.Lista2[2], not True)}')
print (f'{Funcion_Tupla(PEPE.Division_Flotante, 25, PEPE.Lista2[2], not True)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla(PEPE.Division_Flotante, 25, PEPE.Lista2[2], not True))}')

print (f'-' * 20)

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')
        
    print (f'-' * 20)
        
    for elemento in kwargs.keys():
        print (f'{elemento}')
        
    print (f'-' * 20)
        
    for elemento in kwargs.values():
        print (f'{elemento}')
        
Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Funcion_Tupla[1], Votante = not True)

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

print (f'Los numeros pares de la lista son {list(Anonima3)} o incluso podrian ser {PEPE.Lista_Par}')

def Primera(Segunda): #type: ignore
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
        print (f'Tu nombre es {Nombre} {Apellido}')
        
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
print (f'{Variable_Closure(26)}')
print (f'{Variable_Closure(34)}')

def Closure_Crear_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y
    
    return Closure_Multiplicador

Variable_Mult1 = Closure_Crear_Multiplicador(2)
Variable_Mult2 = Closure_Crear_Multiplicador(3)

print (f'El multiplicador es {Variable_Mult1(10)}')
print (f'El multiplicador es {Variable_Mult2(10)}')

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'ZZZZZZZZZZZZZ')
        Segunda()
        print (f'XXXXXXXXXXXXX')
        
    return Tercera

@Primera
def Saludar4():
    print (f'Hola Mundo')
    
Saludar4()

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 10
        
    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(4, 7)}')

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        Nombre = 'Jonathan'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)
        
    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    print (f'Mi nombre es {Nombre} {Apellido}')
    
Usuario2('Erick', 'Perez')

print (f'-' * 20)

from Module_Own import Pokemon2 as Poke2

Objeto19 = Poke2(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto20 = Poke2(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto19.Mostrar()

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto21 = Poke_Kid2(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto21)
Objeto21.Mostrar()

print (f'-' * 20)

class Camara():
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada')
        
class Reproductor_Musica:
    def Reproducir_Musica(self):
        print (f'Musica Reproducida')
        
class Smartphone(Camara, Reproductor_Musica):
    def Encender_Smartphone(self):
        print (f'Smartphone Encendido')
        
Objeto22 = Smartphone()

Objeto22.Encender_Smartphone()
Objeto22.Reproducir_Musica()
Objeto22.Tomar_Fotografia()

print (f'-' * 20)

class Veterinaria2:
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
        
Objeto23 = Perro2('Chester', 5, 2.8, 'Poodle', 'Hipertension')

Veterinaria2.Mostrar(Objeto23)
Objeto23.Mostrar()

print (f'-' * 20)

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')
        
Objeto24 = Gato2('Messi', 1.5, 1.8, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto24)
Objeto24.Mostrar()

print (f'-' * 20)

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto25 = Pajaro2('Polly', 31, 0.4, 'Guacamaya Roja', 'Si')

Veterinaria2.Mostrar(Objeto25)
Objeto25.Mostrar()

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
        
Objeto26 = Paladin2(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto26.Mostrar()
Atacante2.Mostrar(Objeto26)
Defensor2.Mostrar(Objeto26)

print (f'-' * 20)

Hija_Padre = issubclass(Poke_Kid2, Poke2)

print (f'{Hija_Padre}')

Instancia2 = isinstance(Objeto26, Paladin2)
Instancia3 = isinstance(Objeto26, Defensor2)
Instancia4 = isinstance(Objeto26, Atacante2)

print (f'{Instancia2}')
print (f'{Instancia3}')
print (f'{Instancia4}')

print (f'-' * 20)

class A2():
    def Mostrar(self):
        print (f'Hola A2')
        
class E2():
    def Mostrar(self):
        print (f'Hola E2')
        
class B2(E2):
    def Mostrar(self):
        print (f'Hola B2')
        
class C2(A2):
    def Mostrar(self):
        print (f'Hola C2')
        
class D2(B2, C2):
    def Mostrar(self):
        print (f'Hola D2')
        
Objeto27 = D2()

A2.Mostrar(Objeto27)
B2.Mostrar(Objeto27)
C2.Mostrar(Objeto27)
Objeto27.Mostrar()
E2.Mostrar(Objeto27)

print (f'-' * 20)

'''Lista_Numeros = []

Contador = 0

while (Contador < 3):
    Num2 = input(f'Ingrese el numero {Contador + 1}: ')
    try:
        Num3 = float(Num2)
        Lista_Numeros.append(Num3)
        Contador+= 1
    except ValueError:
        print (f'Error, esto no es un numero')
        
Promedio = sum(Lista_Numeros) / len(Lista_Numeros)

print (f'El promedio es {round(Promedio, 2)}')'''

class Efectivo2():
    def Pagar(self):
        print (f'El pago se realizo en efectivo')
        
class Tarjeta2:
    def Pagar(self):
        print (f'El pago se realizo en tarjeta')
        
class Cripto2:
    def Pagar(self):
        print (f'El pago se realizo en cripto')
        
Objeto28 = Cripto2()
Objeto29 = Tarjeta2()
Objeto30 = Efectivo2()

Objeto28.Pagar()
Objeto29.Pagar()
Objeto30.Pagar()

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
        
Objeto31 = Cuenta_Bancaria2(100)
Objeto31.Depositar(25)
Objeto31.Mostrar()

print (f'Tu saldo privado es {Objeto31.Dinero}')

Objeto31.Dinero = '50,000,000'

Objeto31.Mostrar()

print (f'Tu saldo privado es {Objeto31.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla2(Plantilla2):
    def Mostrar(self):
        print (f'Esto es un metodo cualquiera')
        
    def General(self):
        print (f'Estamos obligados a usar este metodo')
        
Objeto32 = Sub_Plantilla2()

Objeto32.Mostrar()
Objeto32.General()

print (f'-' * 20)

class Bulbasaur3():
    def Elegir(self):
        return f'Bulbasaur'
    
class Batalla2:
    def __init__(self):
        self.Favorito = Bulbasaur3()
        
    def Batallar(self):
        print (f'{self.Favorito.Elegir()} yo te elijo!')
        
Objeto33 = Batalla2()

Objeto33.Batallar()

print (f'-' * 20)

class Bulbasaur4():
    def Elegir(self):
        return f'Bulbasaur'
    
class Treecko4:
    def Elegir(self):
        return f'Treeko'
    
class Chikorita4:
    def Elegir(self):
        return f'Chikorita'
    
class Batalla4:
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'{self.Favorito.Elegir()} yo te elijo!')
        
Sample4 = Bulbasaur4()
Objeto34 = Batalla4(Sample4)
Objeto34.Batallar()

Sample5 = Treecko4()
Objeto35 = Batalla4(Sample5)
Objeto35.Batallar()

Sample6 = Chikorita4()
Objeto36 = Batalla4(Sample6)
Objeto36.Batallar()

print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un 
Long String'''

variable4 = Variable_Sumatoria
variable5 = PEPE.Division_Flotante
variable6, variable7 = False, not False

print (f'{variable6}')
print (f'{variable7}')

# Esto es un comentario simple

'''Esto
Es
Un 
Comentario
Simple'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke2"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Sumatoria2(1, 2, 3, 4)}, {Variable_Sumatoria} o incluso {Anonima2(14)} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Koala' in PEPE.Lista2)
print (f'James' not in PEPE.Tupla_Poke)
print (f'Graveler' in PEPE.Set_Conjunto_Poke)

print (f'-' * 20)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es una combinacion de dos conceptos, snake case y desempaquetado de variables')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Anonima2(100), Variable_Sumatoria)

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'{PEPE.Lista2[:2]}')
print (f'{PEPE.Lista2[2:]}')
print (f'{PEPE.Lista2[::2]}')
print (f'{PEPE.Lista2[::3]}')
print (f'{PEPE.Lista2[2:3]}')
print (f'{PEPE.Lista2[0:None]}')
print (f'{PEPE.Lista2[:]}')

print (f'{Lista_Uno[1]} eso de ahi es un {PEPE.Lista2[PEPE.Lista2.index("Koala")]}?')

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

print (f'{dir(PEPE)}')

print (f'-' * 20)

Tupla1 = ('Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde')

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Blue', 'Green'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Variable_Funcion_Tupla)}')

print (f'{Tupla2[2]}')

print (f'-' * 20)

Set_Conjunto1 = {'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo'}

print (f'{Set_Conjunto1}')
Set_Conjunto1.add('Verde')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Red', 'Green'})

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

SetA2 = {1, 2, 3, 4}
SetB2 = set({3, 4, 5, 6})

print (f'{SetA2.union(SetB2)}')
print (f'{SetA2 | SetB2}')

print (f'-' * 20)

print (f'{SetA2.intersection(SetB2)}')
print (f'{SetA2 & SetB2}')

print (f'-' * 20)

print (f'{SetA2.difference(SetB2)}')
print (f'{SetA2 - SetB2}')

print (f'-' * 20)

print (f'{SetB2.difference(SetA2)}')
print (f'{SetB2 - SetA2}')

print (f'-' * 20)

print (f'{SetA2.symmetric_difference(SetB2)}')
print (f'{SetA2 ^ SetB2}')

print (f'-' * 20)

'''SetA2.update(SetB2)

print (f'{SetA2}')'''

'''SetA2.intersection_update(SetB2)

print (f'{SetA2}')'''

'''SetA2.difference_update(SetB2)

print (f'{SetA2}')'''

'''SetB2.difference_update(SetA2)

print (f'{SetB2}')'''

SetA2.symmetric_difference_update(SetB2)

print (f'{SetA2}')

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')
Set_Conjunto_Menu2 = frozenset({'Caramelo'})
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, Lista_Uno_Copia[2]})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Variable_Sumatoria,
    'Votante' : variable6
}

Diccionario2 = {
    'Nombre' : ["Josue", "Eric", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
}

Diccionario3 = dict({'Ingresos' : 500, 'Gastos' : 200, 'Vacio' : "q"})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1['Nombre']}')
print (f'{Diccionario1.get('Edad')}')

print (f'-' * 20)

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2.values()}')
print (f'{Diccionario2.items()}')
print (f'{Diccionario2["Nombre"][2:3]}')
print (f'{Diccionario2.get("Edad")[0:None]}') #type: ignore

print (f'-' * 20)

Diccionario1['Nombre'] = 'Erick'

print (f'{Diccionario1}')

del Diccionario1['Nombre']
Diccionario1.pop('Edad')

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')

Diccionario1 = dict({1 : "Karlita", 2 : 6, 3 : not True})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario2['Nombre'][2]} no puede votar ya que solo tiene {Diccionario1.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'HolaMundo')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = 'Pepe'

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio1.keys()}')
print (f'{Diccionario_Vacio1.values()}')
print (f'{Diccionario_Vacio1.items()}')
print (f'{Diccionario_Vacio1['B']}')
print (f'{Diccionario_Vacio1.get('C')}')

print (f'-' * 20)

print (f'{Diccionario_Vacio2}')
print (f'{Diccionario_Vacio2.keys()}')
print (f'{Diccionario_Vacio2.values()}')
print (f'{Diccionario_Vacio2.items()}')
print (f'{Diccionario_Vacio2['Uno']}')
print (f'{Diccionario_Vacio2.get('Dos')}')

print (f'-' * 20)

Keys1 = [f'Key{i}' for i in range(len(Lista_Uno_Copia))]

print (f'{Keys1}')

Diccionario4 = dict(zip(Keys1, Lista_Uno_Copia))

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Key1"]}')
print (f'{Diccionario4.get("Key3")}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

Set_Conjunto5 = set(Cargar_Csv3['product'])

print (f'{Set_Conjunto5}')

Keys2 = [f'Key_{i}' for i in range(len(Set_Conjunto5))]

print (f'{Keys2}')

Diccionario5 = dict(zip(Keys2, Set_Conjunto5))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key_6"]}')
print (f'{Diccionario5.get("Key_4")}')

print (f'-' * 20)

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

print (f'{type(variable1)}')
print (f'{type(variable4)}')
print (f'{type(PEPE.Division_Flotante)}')
print (f'{type(variable7)}')
print (f'{type(Lista_Uno_Copia)}')
print (f'{type(Tupla3)}')
print (f'{type(Set_Conjunto_Menu1)}')
print (f'{type(Set_Conjunto_Menu2)}')
print (f'{type(Diccionario1)}')
print (f'{type(Funcion_Diccionario)}')
print (f'{type(Data_Frame_Concatenate)}')
print (f'{type(Array4_Sorted)}')
print (f'{type(PEPE)}')
print (f'{type(Objeto14)}')

if (Diccionario3['Ingresos'] > 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200):
        print (f'Ingresos Altos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] == 500):
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200):
        print (f'Ingresos Minimos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] < 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200):
        print (f'Ingresos Bajos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')
    
variable8 = 'Erick'
variable9 = 27

if (variable8 == 'Erick' and variable9 > 30):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una condicion no se cumple')
    
if (variable8 == 'Josue' or variable9 > 30):
    print (f'Al menos una de las condiciones se cumple')
else:
    print (f'Error, ninguna de las condiciones se cumplen')
    
print (f'{dir(variable1)}')

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = 6
        self.Classified = True

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')
        
Objeto37 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto5.Nombre)
Objeto38 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto6.Nombre)
Objeto39 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto7.Nombre)

Objeto37.Desplegar()
Objeto38.Desplegar()
Objeto39.Desplegar()

print (f'-' * 20)

Negativo = -5

print (f'{int(abs(Negativo))}')

Any_Impar = any(num % 2 != 0 for num in PEPE.Lista_Numeros)
Lista_Impar = [num for num in PEPE.Lista_Numeros if num % 2 != 0]
Anonima4 = filter(lambda Num : Num % 2 != 0, PEPE.Lista_Numeros)

print (f'{Any_Impar}')
print (f'{Lista_Impar}')
print (f'{list(Anonima4)}')

print (f'-' * 20)

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
    
print (f'-' * 20)

variable10 = 'eSteBAN'
variable10_letra = variable10[0]

print (f'{variable10}')
print (f'{variable10.lower()}')
print (f'{variable10.upper()}')
print (f'{variable10.capitalize()}')

print (f'{variable10.lower().find("t")}')
print (f'{variable10.lower().index("b")}')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'La letra {variable10_letra} aparece un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = 'este es un texto cualquiera para ver si la cosa sirve o no'

variable11_list = variable11.split(' ')

for elemento in variable11_list:
    print (f'{elemento}')
    
print (f'La lista tiene un total de {len(variable11_list)} palabras')

variable12 = '39'

if (isinstance(variable12, (str))):
    print (f'Lo ingresado es texto')
else:
    print (f'Lo ingresado no es texto')
    
if (variable12.isalpha()):
    print (f'Lo ingresado es texto')
else:
    print (f'Lo ingresado no es texto')
    
print (f'-' * 20)
    
variable13 = '3.4'

try:
    variable14 = float(variable13)
    if (variable14.is_integer()):
        print (f'El numero ingresado es entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
variable15 = 'hola'

try:
    variable16 = float(variable15)
    if (variable16.is_integer()):
        print (f'Numero entero')
    else:
        print (f'Numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
variable17 = 3.6

if (isinstance(variable17, (int, float))):
    print (f'Lo ingresado es un numero entero o decimal')
else:
    print (f'Error, lo ingresado no es un numero')
    
variable18 = 'erick123'

if (variable18.isalpha()):
    print (f'Esto tiene solo letras')
else:
    print (f'Error, esto tiene numeros')
    
if (variable18.isalnum()):
    print (f'Esto tiene letras o numeros')
else:
    print (f'Error')
    
variable19 = ''

if (variable19.isspace()):
    print (f'Solo espacios')
else:
    print (f'Error, esto tiene mas que espacios')
    
variable20 = 'TEXTO'.lower()
variable21 = 'teXto'.upper()

if (variable20.islower()):
    print (f'Lo ingresado esta todo en minuscula')
else:
    print (f'Lo ingresado no esta todo en minuscula')
    
if (variable21.isupper() == True):
    print (f'Lo ingresado esta todo en mayuscula')
else:
    print (f'Lo ingresado no esta todo en mayuscula')
    
print (f'{PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

for elemento in Diccionario5.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario5.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario5.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

for elemento in Diccionario5:
    print (f'{Diccionario5[elemento]}')
    
print (f'-' * 20)

'''Lista_Numeros = list([])

Contador = 0

while (Contador < 3):
    Num2 = input(f'Ingrese el numero {Contador + 1}')
    try:
        Num3 = float(Num2)
        if (Num3.is_integer()):
            Lista_Numeros.append(Num3)
            Contador += 1
        else:
            Lista_Numeros.append(Num3)
            Contador += 1
    except ValueError:
        print (f'Error, lo ingresado no es un numero')
        
Promedio = sum(Lista_Numeros) / len(Lista_Numeros)

print (f'El promedio del estudiante es {round(Promedio, 2)}')'''

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1
    
print (f'-' * 20)

Contador = 0

Lista_Animales = []
Lista_Animales.append('Jirafa')
Lista_Animales.insert(1, PEPE.Lista2[PEPE.Lista2.index("Koala")])
Lista_Animales.extend(['Camello', 'Gorila'])

print (f'{Lista_Animales}')

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Camello'):
        print (f'This Camel animal lives in the desert')
        break
    else:
        Contador+= 1
        continue
    
print (f'-' * 20)

for elemento in range(5):
    print (f'El elemento es {elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'El elemento es {elemento}')
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Animales, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)
    
for elemento1, elemento2, elemento3, elemento4 in zip(Lista_Animales, Set_Conjunto_Menu1, Set_Conjunto1, Lista_Uno_Copia):
    print (f'{elemento1} -- {elemento2} -- {elemento3} -- {elemento4}')
    
print (f'-' * 20)

Lista_Numeros_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1
    
print (f'-' * 20)

Menor = min(Lista_Numeros_Mult)
Mayor = max(Lista_Numeros_Mult)
Redondeo = round(14.458795, 2)
Sumatoria4 = sum(Lista_Numeros_Mult)

print (f'{bool("")}')
print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool(False)}')
print (f'{bool(not True)}')

print (f'-' * 20)

Todo_All = all([Lista_Uno_Copia, Set_Conjunto_Menu1, Tupla1, None])

print (f'{Todo_All}')

print (f'El menor es {Menor} y el mayor es {Mayor}')
print (f'El numero 14.458795 redondeado es {Redondeo}')
print (f'El resultado de la sumatoria es {Sumatoria4}')

Uno = int('500')
Dos = str(500)
Tres = float(Dos)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')

print (f'-' * 20)

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]
Anonima5 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)

print (f'{Any_Iterable}')
print (f'{Lista_Iterable}')
print (f'{list(Anonima5)}')

print (f' - '.join(PEPE.Set_Conjunto_Poke))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

'''def Floating1(Elemento):
    try:
        Elementico = float(Elemento)
        if (Elementico.is_integer()):
            Resultado1 = Variable_Sumatoria * Elementico + Sumatoria2(1, 2, 3, 4)
            return f'El resultado de la operacion es {Resultado1}'
        else:
            Resultado1 = Variable_Sumatoria * Elementico + Sumatoria2(1, 2, 3, 4)
            return f'El resultado de la operacion es {round(Resultado1, 2)}'
    except ValueError:
        return f'Lo ingresado no es un numero'

print (f'{Floating1(PEPE.Flotante1)}')

Resultado2 = eval(PEPE.Flotante2)

print (f'El resultado de la segunda operacion es {Resultado2}')

def Floating3(Elemento):
    if (Elemento.replace(' ', '').isalpha()):
        return f'Gracias, el texto ingresado es {Elemento}'
    elif (Elemento.isspace()):
        return f'Error, no ingresaste nada'
    else:
        return f'Error, lo ingresado no es un texto'
    
print (f'{Floating3(PEPE.Flotante3)}')

def Floating4(Cadena):
    Lista_Cadena = Cadena.split(' ')
    print (f'La cantidad de palabras digitadas son {len(Lista_Cadena)}')
    
    for elemento in enumerate(Lista_Cadena):
        print (f'{elemento[0]} -- {elemento[1]}')
        
Floating4(PEPE.Flotante4)'''

'''Lista_Alumnos = list([])

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
    
'''Lista_Alumnos = []

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda Num : Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El estudiante menor de la lista es {Menore} y su edad es {Lista[0][1]} años')
    print (f'El estudiante menor de la lista es {Mayore} y su edad es {Lista[-1][1]} años')
    
Colegio(Lista_Alumnos)'''

'''Lista_Numeros = []

Contador = 0

while (Contador < 3):
    Numerito = input(f'Ingrese el numero {Contador + 1} ')
    try:
        Numerito2 = float(Numerito)
        if (Numerito2.is_integer()):
            Lista_Numeros.append(Numerito2)
            Contador+= 1
        else:
            Lista_Numeros.append(Numerito2)
            Contador+= 1
    except ValueError:
        print (f'Error, lo ingresado no es un numero')
        
print (f'La lista de numeros es {Lista_Numeros}')'''

'''def Ciclonazo():
    while True:
        Numerito = input(f'Ingrese un numero entero: ')
        try:
            Numerito2 = int(Numerito)
            break
        except:
            print (f'Error, lo ingresado no es un numero entero')
    return Numerito2
    
print (f'Gracias, el numero ingresado es {Ciclonazo()}')'''

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

Texto10 = 'example@example.com'

Pattern8 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.(?:com|net|org)$'

Buscar18 = bool(re.fullmatch(Pattern8, Texto10))

if (Buscar18):
    print (f'Formato de correo valido')
else:
    print (f'Error, formato de correo invalido')
    
Numero4 = '32'

Buscar19 = bool(re.match(r'(0[0-9]|[12][0-9]|3[01])', Numero4))

if (Buscar19 == True):
    print (f'El numero esta entre 01 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)
    
import pandas as pd
from datetime import datetime

Ruta_Csv4 = 'C:\\Repo\\Store.csv'

Cargar_Csv4 = pd.read_csv(Ruta_Csv4)

print (f'{Cargar_Csv4}')

print (f'-' * 20)

Fecha4 = '2026-04-05'

try:
    Fech4 = datetime.strptime(Fecha4, '%Y-%m-%d').date()
    Fech4_Formateada = pd.to_datetime(Fech4)
    Cargar_Csv4['date'] = pd.to_datetime(Cargar_Csv4['date'])
except ValueError:
    print (f'Error, formato de fecha invalido')
    exit()
    
Cargar_Csv4['TOTALITO'] = Cargar_Csv4['quantity'] * Cargar_Csv4['price']
    
Encontrada4 = Cargar_Csv4[Cargar_Csv4['date'].dt.date == Fech4_Formateada.date()]

if (Encontrada4.empty):
    print (f'No hay ventas en esta fecha')
else:
    print (f'Genial! hemos encontrado ventas')
    
    Grupo4 = Encontrada4.groupby('product')['quantity'].sum()
    Grupo4_Min = Grupo4.idxmin()
    Grupo4_Max = Grupo4.idxmax()
    Grupo4_Min_Cant = Grupo4.min()
    Grupo4_May_Cant = Grupo4.max()
    
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo4_Min} vendio un total de {Grupo4_Min_Cant} unidades')
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo4_Max} vendio un total de {Grupo4_May_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron en esta fecha fue de {Grupo4.count()}')
    print (f'La cantidad de productos individuales que se compraron fue {Grupo4.sum()} unidades')
    
    Grupo5 = Encontrada4.groupby('product')['TOTALITO'].sum()
    
    print (f'El total de dinero vendido en esta fecha fue de {Grupo5.sum()}')