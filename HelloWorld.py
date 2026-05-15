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
    
class Batalla2:
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