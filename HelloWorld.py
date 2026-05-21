var1 = '40'
var2 = 40

if (var1.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero entero')
    
print (f'-' * 20)

if (isinstance(var2, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero entero')
    
var3 = 'hola'

try:
    var4 = float(var3)
    if (var4.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado no es un numero')
    
var5 = 'hola'

if (isinstance(var5, (int, float))):
    print (f'Lo ingresado es un numero entero o decimal')
else:
    print (f'Lo ingresado no es un numero')
    
print (f'-' * 20)

import re

Texto1 = "   Hola!!!   mundo@@   123   "

Texto1_Version1 = Texto1.strip()
Texto1_Version2 = ' '.join(Texto1_Version1.split())
Texto1_Version3 = Texto1_Version2.lower()
Texto1_Version4 = re.sub(r'\!|\@', '', Texto1_Version3)

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
    print (f'Error, formato incorrecto')
    
Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrada1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()] #type: ignore

if (Encontrada1.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! Encontramos ventas')
    Grupo1 = Encontrada1.groupby('product')['quantity'].sum()
    Grupo1_May = Grupo1.idxmax()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_May_Cant = Grupo1.max()
    Grupo1_Min_Cant = Grupo1.min()
    
print(f'En la fecha {Fech1_Formateada} el producto {Grupo1_May} vendio un total de {Grupo1_May_Cant} unidades') #type: ignore
print(f'En la fecha {Fech1_Formateada} el producto {Grupo1_Min} vendio un total de {Grupo1_Min_Cant} unidades') #type: ignore

print(f'La cantidad de clientes que compraron en esta fecha fue de {Grupo1.count()}') #type: ignore
print(f'La cantidad de productos vendidos en esta fecha fue de {Grupo1.sum()}') #type: ignore
print(f'La media de productos vendidos en esta fecha fue de {Grupo1.sum().mean()}') #type: ignore

Grupo2 = Encontrada1.groupby('product')['TOTALITO'].sum()

print(f'El total en dolares vendido en {Fech1_Formateada} fue de {Grupo2.sum()}') #type: ignore

SetA1 = {1, 2, 3, 4}
SetB1 = {3, 4, 5, 6}

print(f'{SetA1.union(SetB1)}')
print(f'{SetA1 | SetB1}')

print(f'-' * 20)

print(f'{SetA1.intersection(SetB1)}')
print(f'{SetA1 & SetB1}')

print(f'-' * 20)

print(f'{SetA1.difference(SetB1)}')
print(f'{SetA1 - SetB1}')

print(f'-' * 20)

print(f'{SetB1.difference(SetA1)}')
print(f'{SetB1 - SetA1}')

print(f'-' * 20)

print(f'{SetA1.symmetric_difference(SetB1)}')
print(f'{SetA1 ^ SetB1}')

print(f'-' * 20)

SetC1 = {1, 2, 3, 4, 5}
SetD1 = {4, 5}
SetE1 = set({8})

print(f'{SetC1.issuperset(SetD1)}')
print (f'{SetC1 >= SetD1}')
print(f'-' * 20)
print(f'{SetD1.issubset(SetC1)}')
print (f'{SetD1 <= SetC1}')
print(f'-' * 20)
print(f'{SetC1.isdisjoint(SetE1)}')

print(f'-' * 20)

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
        print (f'El entrenador ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Objeto1 = Batalla1()

Objeto1.Batallar()

print (f'-' * 20)

class Spirigatito1():
    def Elegir(self):
        return f'Spirigatito'
    
class Treekoo1:
    def Elegir(self):
        return f'Treekoo'
    
class Chikorita1:
    def Elegir(self):
        return f'Chikorita'
    
class Batalla2:
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El entrenador ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Obj1 = Spirigatito1()
Objeto2 = Batalla2(Obj1)
Objeto2.Batallar()

Obj2 = Treekoo1()
Objeto3 = Batalla2(Obj2)
Objeto3.Batallar()


Obj3 = Chikorita1()
Objeto4 = Batalla2(Obj3)
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

Pattern1 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar1 = re.findall(Pattern1, Texto2)

print (f'{Buscar1}')

for indice, elemento in enumerate(Buscar1, start=1):
    print (f'{indice} -- {elemento}')
    
print (f'-' * 20)

import re

Texto3 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Buscar2 = re.sub(r'\!|\?|\-|\.{2,}', '', Texto3)

print (f'{Buscar2}')

Buscar3 = re.sub(r'\d{4,}', '', Buscar2)

print (f'{Buscar3}')

print (f'-' * 20)

import re

Texto4 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern2 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.(?:com|net|org)'

Correos1 = re.findall(Pattern2, Texto4)

Texto4_temp = Texto4

print (f'{Correos1}')

for i, email in enumerate(Correos1, start=1):
    Texto4_temp = Texto4_temp.replace(email, f'SAMPLE{i}')
    
print (f'{Texto4_temp}')

Texto4_temp2 = re.sub(r'\!|\?|\-|\.{2,}', '', Texto4_temp)

print (f'{Texto4_temp2}')

Texto4_temp3 = re.sub(r'\d{4,}', '', Texto4_temp2)

print (f'{Texto4_temp3}')

for i, email in enumerate(Correos1, start=1):
    Texto4_temp3 = Texto4_temp3.replace(f'SAMPLE{i}', email)
    
print (f'{Texto4_temp3}')

print (f'-' * 20)

import re

Texto5 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Pattern3 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos2 = re.findall(Pattern3, Texto5)

print (f'{Correos2}')

Texto5_temp = Texto5

for i, email in enumerate(Correos2, start=1):
    Texto5_temp = Texto5_temp.replace(email, f'SAMPLE{i}')
    
print (f'{Texto5_temp}')

Texto5_temp2 = re.sub(r'\!|\?', '', Texto5_temp)

print (f'{Texto5_temp2}')

for i, email in enumerate(Correos2, start=1):
    Texto5_temp2 = Texto5_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto5_temp2}')

print (f'-' * 20)

try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado no existe')
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

'''Lista_Numeros = []

Contador = 0

while (Contador < 3):
    while True:
        Numero = input(f'Ingrese el numero {Contador + 1}: ')
        try:
            Numerito = float(Numero)
            if (Numerito.is_integer()):
                Lista_Numeros.append(Numerito)
                break
            else:
                Lista_Numeros.append(Numerito)
                break
        except ValueError:
            print (f'Error, necesito que ingreses un numero')
            
    Contador+= 1
    
Promedio = sum(Lista_Numeros) / len(Lista_Numeros)

print (f'El promedio de las notas es {round(Promedio, 2)}')'''

class Persona:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
    
Objeto5 = Persona('Erick Josue')

print (f'{Objeto5}')

from Module_Own import Pokemon1 as Poke1

Objeto6 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto7 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto7.Mostrar()

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto8 = Poke_Kid1(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto8)
Objeto8.Mostrar()

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
        
Objeto9 = Perro1('Chester', 5, 2.8, 'Poodle', 'Hiper-tension')

Veterinaria1.Mostrar(Objeto9)
Objeto9.Mostrar()

print (f'-' * 20)
        
class Gato1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Color, Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Activo = Activo
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Activo: {self.Activo}')
        
Objeto10 = Gato1('Messi', 1.5, 1.8, 'Gris', 'No')

Veterinaria1.Mostrar(Objeto10)
Objeto10.Mostrar()

print (f'-' * 20)
        
class Pajaro1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto11 = Pajaro1('Polly', 31, 0.4, 'Cacatua Amarilla', 'Si')

Veterinaria1.Mostrar(Objeto11)
Objeto11.Mostrar()

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
        
Objeto12 = Paladin1(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto12.Mostrar()
Atacante1.Mostrar(Objeto12)
Defensor1.Mostrar(Objeto12)

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
        
Objeto13 = D1()

A1.Mostrar(Objeto13)
B1.Mostrar(Objeto13)
C1.Mostrar(Objeto13)
Objeto13.Mostrar()
E1.Mostrar(Objeto13)

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
        
Objeto14 = Cripto1()
Objeto15 = Tarjeta1()
Objeto16 = Efectivo1()

Objeto14.Pagar()
Objeto15.Pagar()
Objeto16.Pagar()

print (f'-' * 20)

class Cuenta_Bancaria1:
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
        
Objeto17 = Cuenta_Bancaria1(100)
Objeto17.Depositar(25)
Objeto17.Mostrar()

print (f'Tu saldo privado es {Objeto17.Dinero}')

Objeto17.Dinero = '50,000,000'

Objeto17.Mostrar()

print (f'Tu saldo privado es {Objeto17.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla1(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla1(Plantilla1):
    def Mostrar(self):
        print (f'Este es un metodo cualquiera')
        
    def General(self):
        print (f'Este metodo Plantilla1 es obligatorio')
        
Objeto18 = Sub_Plantilla1()

Objeto18.Mostrar()
Objeto18.General()

print (f'-' * 20)

class Portugal1():
    def Elegir(self):
        return f'Portugal'
    
class Partido1:
    def __init__(self):
        self.Rival = Portugal1()
        
    def Jugar(self):
        print (f'La sele va a jugar contra {self.Rival.Elegir()} en {Fech1_Formateada}')
        
Objeto19 = Partido1()

Objeto19.Jugar()

print (f'-' * 20)

import re

Texto6 = 'esto hola es un 25 texto @ cualquiera para hula ver si puedo!! practicar estas 945 * hela habili-dades tan 3 complicadas'

Buscar4 = re.search(r'ver', Texto6)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\d+', Texto6)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\W', Texto6)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\!|\?|\-|\@', Texto6)

print (f'{Buscar7}')

Buscar8 = re.findall(r'h.la', Texto6)

print (f'{Buscar8}')

Buscar9 = re.fullmatch(r'esto hola es un 25 texto @ cualquiera para hula ver si puedo!! practicar estas 94 hela habili-dades tan 3 complicadas', Texto6)

print (f'{Buscar9}')

Buscar10 = re.findall(r'\d{3,}\s\W', Texto6)

print (f'{Buscar10}')

Buscar11 = re.findall(r'[ue]{2,4}', Texto6)

print (f'{Buscar11}')

Texto7 = 'sample@sample.com'

Pattern4 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.(?:com|org|net)$'

Buscar12 = bool(re.match(Pattern4, Texto7))

if (Buscar12 == True):
    print (f'El formato del correo electronico es correcto')
else:
    print (f'Formato incorrecto')
    
print (f'-' * 20)

import re

Texto8 = 'ericksuper80@hotmail.com'

Pattern5 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:hotmail|gmail|yahoo)\.(?:com|net|org)$'

Buscar13 = bool(re.fullmatch(Pattern5, Texto8))

if (Buscar13 == True):
    print (f'El formato del segundo correo electronico es correcto')
else:
    print (f'Formato incorrecto')
    
import re
    
Texto9 = '32'

Pattern6 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar14 = bool(re.match(Pattern6, Texto9))

if (Buscar14):
    print (f'El numero se encuentra entre 01 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
import re
    
Texto10 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern7 = r'\d{2}\/[0-9]{2}\/\d{2,4}'

Replacement1 = 'XX/XX/XXXX'

Buscar15 = re.sub(Pattern7, Replacement1, Texto10)

print (f'{Buscar15}')

Pattern8 = r'\+\d{1}\-[0-9]{3}\-\d{3}\-[0-9]{3,4}'

Replacement2 = '+*-***-***-****'

Buscar16 = re.sub(Pattern8, Replacement2, Buscar15)

print (f'{Buscar16}')

import re

# usuario@dominio.extension

Texto11 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Pattern9 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|org|net)'

Buscar17 = re.findall(Pattern9, Texto11)

print (f'{Buscar17}')

print (f'-' * 20)

Contador = 0

while (Contador < len(Buscar17)):
    print (f'{Buscar17[Contador]}')
    Contador+= 1
    
print (f'-' * 20)

import re

Texto12 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Buscar18 = re.sub(r'\!|\?|\.{2,}', '', Texto12)

print (f'{Buscar18}')

Pattern10 = r'[0-9]{4}\-\d{3,4}'

Buscar19 = re.sub(Pattern10, '', Buscar18)

print (f'{Buscar19}')

print (f'-' * 20)

import re

Texto13 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Correos3 = re.findall(r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|org|net)', Texto13)

print (f'{Correos3}')

Texto13_temp = Texto13

for i, email in enumerate(Correos3, start=1):
    Texto13_temp = Texto13_temp.replace(email, f'TEMPLATE{i}')
    
print (f'{Texto13_temp}')

Texto13_temp2 = re.sub(r'\!|\?|\.{2,}', '', Texto13_temp)

print (f'{Texto13_temp2}')

Texto13_temp3 = re.sub(r'\d{4}\-[0-9]{4}', '', Texto13_temp2)

print (f'{Texto13_temp3}')

for i, email in enumerate(Correos3, start=1):
    Texto13_temp3 =  Texto13_temp3.replace(f'TEMPLATE{i}', email)
    
print (f'{Texto13_temp3}')

print (f'-' * 20)

Texto14 = 'hola'

try:
    Numerito1 = float(Texto14)
    if (Numerito1.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
Texto15 = '80'

if (isinstance(Texto15, (int, float))):
    print (f'Lo ingresado es un numero entero o decimal')
else:
    print (f'Error lo ingresado no es un numero')
    
Texto16 = '3.6'

try:
    Numerito2 = float(Texto16)
    if (Numerito2.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado no es un numero')
    
import re
    
Texto17 = "   Hola!!!   mundo@@   123   "

print (f'{Texto17}')

Texto17_Version1 = Texto17.strip()

print (f'{Texto17_Version1}')

Texto17_Version2 = ' '.join(Texto17_Version1.split())

print (f'{Texto17_Version2}')

Texto17_Version3 = Texto17_Version2.lower()

print (f'{Texto17_Version3}')

Texto17_Version4 = re.sub(r'\!|\@', '', Texto17_Version3)

print (f'{Texto17_Version4}')

def Exception1(Elemento):
    try:
        Numerito3 = float(Elemento)
        if (Numerito3.is_integer()):
            return f'El numero ingresado es un entero'
        else:
            return f'El numero ingresado es un decimal'
    except ValueError:
        return f'Error, lo ingresado no es un numero'

print (f'{Exception1("hola")}')

def Exception2(Num1, Num2):
    try:
        Sum1 = Num1 + Num2
        return f'El resultado de la sumatoria es {Sum1}'
    except TypeError:
        return f'Error, necesito que ambos elementos sean numeros'
    
print (f'{Exception2(12, "hola")}')

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        return f'El resultado de la division es {round(Divi, 2)}'
    except ZeroDivisionError:
        return f'Error, el divisor no puede ser cero'
    
print (f'{Exception3(12, 0)}')

Lista_Exception4 = []
Lista_Exception4.append('Erick')
Lista_Exception4.insert(1, 'Josue')
Lista_Exception4.extend(['Karlita'])

def Exception4(Indice):
    try:
        return f'El elemento en la posicion {Indice} es {Lista_Exception4[Indice]}'
    except IndexError:
        return f'Error, el indice esta fuera de rango'
    
print (f'{Exception4(2)}')

Diccionario_Exception5 = {
    'Nombre' : "Erick",
    'Edad' : 37
}

def Exception5(Llalve):
    try:
        return f'El elemento en la llave {Llalve} es {Diccionario_Exception5[Llalve]}'
    except KeyError:
        return f'Error, la llave esta fuera de rango'
    
print (f'{Exception5("Votante")}')

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
    Documento_Leer = Docu.readline()
    print (f'{Documento_Leer}')
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
    'Votante' : [True, True, not True]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [55, 14, 26],
    'Votante' : [True, not True, True]
})

print (f'-' * 20)

Data_Frame_Concatenate = pd.concat([Data_Frame1, Data_Frame2])

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame1}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate_Age}')

print (f'-' * 20)

print (f'La sumatoria total de edad es es {Data_Frame_Concatenate_Age.sum()}')
print (f'Tambien la cantidad de usuarios en el dataframe es {Data_Frame_Concatenate_Age.count()}')

print (f'Finalmente la media del numero de edades es {Data_Frame_Concatenate_Age.sum().mean()}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_May = Grupo3.idxmax()
Grupo3_Min = Grupo3.idxmin()
Grupo3_May_Cant = Grupo3.max()
Grupo3_Min_Cant = Grupo3.min()

print (f'El menor del dataframe es {Grupo3_Min} y su edad es {Grupo3_Min_Cant} años')
print (f'El mayor del dataframe es {Grupo3_May} y su edad es {Grupo3_May_Cant} años')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    volador = elemento['Nombre']
    volador2 = elemento['Edad']
    
    print (f'Mi nombre es {volador} y mi edad es {volador2} años')
    
'''print (f'-' * 20) # LINEPLOT

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'-' * 20) # BARPLOT

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'-' * 20) # SCATTERPLOT

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

print (f'El numero de Filas es de {Filas}')
print (f'El numero de Columnas es de {Columnas}')

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
Elemento9 = Data_Frame2.iloc[0, :]
Elemento10 = Data_Frame2.iloc[:, 1]

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')
print (f'{Elemento9}')
print (f'{Elemento10}')

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine='openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'-' * 20)

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='sexo')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols='E:J')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols='E:J', nrows=1)

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

Grupo4 = Cargar_Excel3_Sorted.groupby('tres')['cinco'].sum()

print (f'La cantidad de bichillos en este excel es {Grupo4.count()}')
print (f'La suma de las edades es de {Grupo4.sum()}')
print (f'La suma media de las edades es de {Grupo4.sum().mean()}')

print (f'-' * 20)

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Csv2 = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Csv2}')

print (f'-' * 20)

print (f'{Cargar_Csv2.head()}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv3 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

print (f'-' * 20)

Grupo5 = Cargar_Csv3.groupby('Nombre')['Edad'].sum()

print (f'La menor de las edades del csv es {Grupo5.min()} y la edad mayor es {Grupo5.max()}')

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
print (f'{Array0[2][:2]}')
print (f'{Array0[2][2:]}')
print (f'{Array0[0][::2]}')
print (f'{Array0[1][::3]}')
print (f'{Array0[2][2:3]}')
print (f'{Array0[0][0:None]}')
print (f'{Array0[1][:]}')

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
print (f'{Array1}')

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
print (f'{Array2}')

print (f'{Array2[1, ::2]}')
print (f'{Array2[0, ::3]}')
print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[:, 1]}')
print (f'{Array2[1, 2:3]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[0, :]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodados: {Array2_Sorted}')
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

Array3 = np.array([[['e', 'r', 'p'], ['a', 'b', 'c']],     [['w', 'x', 'f'], ['s', 'k', 'l']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 2]}')

print (f'{Array3[1, 0, ::2]}')
print (f'{Array3[1, 0, ::3]}')
print (f'{Array3[0, 1, :2]}')
print (f'{Array3[0, 1, 2:]}')
print (f'{Array3[0, :, 0]}')
print (f'{Array3[1, 0, 2:3]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "f"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 5, 7]]],     [[[3, 2, 1], [6, 5, 4]], [[9, 8, 7], [3, 0, 1]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 2]}')

print (f'{Array4[1, 1, 0, ::2]}')
print (f'{Array4[1, 1, 0, ::3]}')
print (f'{Array4[0, 1, 0, :2]}')
print (f'{Array4[0, 1, 0, 2:]}')
print (f'{Array4[1, 1, :, 1]}')
print (f'{Array4[1, 0, 0, 2:3]}')
print (f'{Array4[0, 0, 1, 0:None]}')
print (f'{Array4[0, 0, 1, :]}')
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

print (f'{Sumita5}')
print (f'{Sumita6}')
print (f'{Sumita7}')
print (f'{Sumita8}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1) #type: ignore

print (f'{Array_Num1}')

Array_Num1_May = np.max(Array_Num1)
Array_Num1_Min = np.min(Array_Num1)

print (f'El menor de los numeros es {Array_Num1_Min} y el mayor es {Array_Num1_May}')

print (f'-' * 20)

Array_Num2 = np.arange(start=1, stop=26, step=1) #type: ignore

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
print (f'{Array_Zero[1, 2:3]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 2]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke2"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 1]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value = f'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[3]}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[1, 0, 0, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 1]}')

print (f'-' * 20)

Tupla_Array = tuple(('Rojo', 'Verde'))
Set_Conjunto_Array1 = {1, 2, 3, 4}
Set_Conjunto_Array2 = set({5})
Set_Conjunto_Array1.update(Set_Conjunto_Array2)

Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array1)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array['Nombre'][1])

print (f'-' * 20)

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'-' * 20)

print (f'{Array_Gen6[3]}')

print (f'-' * 20)

Array_Num3 = np.arange(start=1, stop=6, step=1) #type: ignore

print (f'{Array_Num3}')

Lista_Array1 = list([])

for elemento in Array_Num3:
    Lista_Array1.extend([str(elemento)])

print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Num4 = np.arange(start=1, stop=6, step=1) #type: ignore
Array_Num5 = np.arange(start=2, stop=11, step=2) #type: ignore
Array_Num6 = np.arange(start=3, stop=31, step=3) #type: ignore
Array_Num7 = np.arange(start=2, stop=21, step=2) #type: ignore
Array_Num8 = np.arange(10) #type: ignore

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

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

Sumita9 = np.sum(Array_Random2_Sorted, axis=0)
Sumita10 = np.sum(Array_Random2_Sorted, axis=1)
Sumita11 = np.sum(Array_Random2_Sorted[1, 0:None])
Sumita12 = np.sum(Array_Random2_Sorted[1, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

print (f'-' * 20)

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 4, 7])

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

Array_Random3 = np.random.randint(low=1, high=10, size=(20))

print (f'{Array_Random3}')

Array_Random3_Shape = np.reshape(Array_Random3, shape=(4, 5))

print (f'{Array_Random3_Shape}')

Array_Random3_Shape_Ravel = np.ravel(Array_Random3_Shape)

print (f'{Array_Random3_Shape_Ravel}')

print (f'-' * 20)

Lista_Array2 = []
Lista_Array2.append('Erick')
Lista_Array2.insert(1, 'Josue')
Lista_Array2.extend(['Karlita'])

Array5 = np.array(Lista_Array2)

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
            print (f'{Fila}')

print (f'-' * 20)

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-' * 20)

Array_Random4 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random4}')

print (f'-' * 20)

Array_Random4_Column_May = np.max(Array_Random4, axis=0)
Array_Random4_Column_Min = np.min(Array_Random4, axis=0)
Array_Random4_Row_May = np.max(Array_Random4, axis=1)
Array_Random4_Row_Min = np.min(Array_Random4, axis=1)

print (f'Los menores de las columnas son {Array_Random4_Column_Min}')
print (f'Los mayores de las columnas son {Array_Random4_Column_May}')
print (f'Los menores de las filas son {Array_Random4_Row_Min}')
print (f'Los mayores de las filas son {Array_Random4_Row_May}')

print (f'-' * 20)

Lista_Array3 = ['Erick', 'Josue', 'Karlita']
Lista_Array3.append('Carmelo')
Lista_Array3.insert(2, 'Susanita')
Lista_Array3.extend(['Roxana'])

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
    for elemento in range(1, 5):
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
            yield f'NUMBER ZERO'
        elif (elemento == 1):
            yield f'NUMBER ONE'
        elif (elemento == 2):
            yield f'NUMBER TWO'
        elif (elemento == 3):
            yield f'NUMBER THREE'
        elif (elemento == 4):
            yield f'NUMBER FOUR'
        else:
            yield f'CODING ERROR'
            
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

Lista_Numbers = [1, 2, 3, 4, 5]

print (f'El resultado es {PEPE.Calculo(Lista_Numbers)}')

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

def Usuario_Externa():
    def Usuario_Interna(Sexo):
        Genero = Sexo.lower()
        if (Genero == 'masculino'):
            return True
        else:
            return False
        
    return Usuario_Interna('MASCULINO')

Variable_Usuario = Usuario_Externa()

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

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.5, 200, True)

print (f'{Funcion_Tupla("Perro", 3.5, 200, True)}')
print (f'{Funcion_Tupla("Perro", 3.5, 200, True)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.5, 200, True))}')
    
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
        
    print (f'-' * 20)
        
    for elemento in kwargs:
        print (f'{kwargs[elemento]}')
        
Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = 37, Votante = not True)

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
print (f'Los numeros pares de la lista son {list(Anonima3)} o incluso puede ser {PEPE.Lista_Par}')

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
print (f'{Variable_Closure(36)}')

def Closure_Crear_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y
    
    return Closure_Multiplicador

Mult1 = Closure_Crear_Multiplicador(2)
Mult2 = Closure_Crear_Multiplicador(3)

print (f'El multiplicador es {Mult1(10)}')
print (f'El multiplicador es {Mult2(10)}')

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    if (Any_Impar == True):
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impares = [num for num in Lista if num % 2 != 0]
        
        print (f'Los numeros impares de la lista son {list(Anonima4)} o incluso podrian ser {Lista_Impares}')
    else:
        print (f'Error, no hay elementos impares en la lista')
        
Filtrador(PEPE.Lista_Numeros)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'ZZZZZZ')
        Segunda()
        print (f'XXXXXX')
        
    return Tercera

@Primera
def Saludar4():
    print (f'Hola Mundo')
    
Saludar4()

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 7
        
    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(4, 3)}')

def Primera(Segunda):
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

Objeto20 = Poke2(PEPE.Diccionario_Poke["Poke1"], 'Electrico', 'Impact Trueno')
Objeto21 = Poke2(PEPE.Diccionario_Poke["Poke2"], 'Roca', 'Sismo')

Objeto21.Mostrar()

print (f'-' * 20)

class Persona2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
    
Objeto22 = Persona2('Erick')

print (f'Hola {Objeto22}')

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto23 = Poke_Kid2(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto23)
Objeto23.Mostrar()

print (f'-' * 20)

Subclase1 = issubclass(Poke_Kid2, Poke2)

print (f'{Subclase1}')

Instancia1 = isinstance(Objeto23, Poke_Kid2)

print (f'{Instancia1}')

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




Ahora vamos a hacer un ejercicio de Composicion, el metod de la primera clase se debe mostrar en la segunda sin usar herencia

'''




[COMPOSICION VS INYECCION DE DEPENDENCIAS]  

QUE ES DUCK TYPING? - Es una filosofia
"No me importa qué eres.
Me importa si puedes hacer lo que necesito."



Ejercicio horneando un paste. En el caso de la composicion, el pastel "nace" condenado a ser de chocolate porque él mismo crea el ingrediente.

class Ingredientes():
    def Sabor(self):
        return f'Chocolate'

class Pastel:
    def __init__(self):
        self.Agregado = Ingredientes()

    def Hornear(self):
        print (f'Horneaste un pastel de {self.Agregado.Sabor()}')

Objeto33 = Pastel()

Objeto33.Hornear()

[Inyeccion de dependencias]

# 1. Definimos los posibles sabores por separado
class Chocolate:
    def sabor(self):
        return "Chocolate suizo 🍫"

class Fresa:
    def sabor(self):
        return "Fresas naturales 🍓"

# 2. La clase Pastel ahora es "Abierta"
class Pastel:
    def __init__(self, ingrediente):
        # INYECCIÓN: El pastel recibe el ingrediente por el constructor.
        # Ya no hace: self.Agregado = Chocolate()
        self.ingrediente = ingrediente

    def hornear(self):
        # El pastel simplemente usa el sabor del objeto que le pasaron
        print(f"Horneaste un pastel de {self.ingrediente.sabor()}")

# --- MOMENTO DE LA INYECCIÓN (Fuera de las clases) ---

# Queremos un pastel de Chocolate:
ingrediente1 = Chocolate()
mi_pastel_choc = Pastel(ingrediente1) # Inyectamos chocolate
mi_pastel_choc.hornear()

# Queremos un pastel de Fresa:
ingrediente2 = Fresa()
mi_pastel_fresa = Pastel(ingrediente2) # Inyectamos fresa
mi_pastel_fresa.hornear()
mi_pastel_fresa.hornear()



---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------


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
# Juegue con los operadores de pertenencia in / not in en variables simples
# Busque un elemento en una Lista o Tupla o Set_Conjunto con los operadores de pertenencia in/ not in
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


'''

✅ Operaciones principales de conjuntos en Python
Supongamos los siguientes conjuntos para los ejemplos:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

1. 🔹 Unión (union)
Devuelve todos los elementos de ambos conjuntos sin repetir.
A.union(B)
# o también
A | B
Resultado:
{1, 2, 3, 4, 5, 6}

2. 🔹 Intersección (intersection)
Devuelve los elementos comunes entre los conjuntos.
A.intersection(B)
# o también
A & B
Resultado:
{3, 4}

3. 🔹 Diferencia (difference)
Devuelve los elementos que están en un conjunto pero no en el otro.
A.difference(B)
# o también
A - B
Resultado:
{1, 2}
También puedes obtener la diferencia inversa:
B - A  # {5, 6}

4. 🔹 Diferencia simétrica (symmetric_difference)
Devuelve los elementos que están en uno u otro conjunto, pero no en ambos.
A.symmetric_difference(B)
# o también
A ^ B
Resultado:
{1, 2, 5, 6}

5. 🔹 Subconjunto (issubset)
Verifica si todos los elementos de un conjunto están contenidos en otro.
A.issubset(B)
# o también
A <= B
Ejemplo:
C = {1, 2}
C.issubset(A)  # True

6. 🔹 Superconjunto (issuperset)
Verifica si un conjunto contiene todos los elementos de otro.
A.issuperset(C)
# o también
A >= C

7. 🔹 Conjuntos disjuntos (isdisjoint)
Determina si dos conjuntos no tienen elementos en común.
A.isdisjoint(B)
Ejemplo:
D = {7, 8}
A.isdisjoint(D)  # True

8. 🔹 Operaciones con actualización (modifican el conjunto original)

Unión   update()    -----  Conserva los elementos no comunes
Intersección    intersection_update()    --- Conserva solo los elementos comunes
Diferencia      difference_update()    ---  Elimina los elementos presentes en el otro conjunto
Diferencia simétrica     symmetric_difference_update()      --- Conserva los elementos no comunes

Conserva los elementos no comunes
Ejemplo:
A = {1, 2, 3}
B = {3, 4}
A.update(B)
print(A)  # {1, 2, 3, 4}


'''



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
| `isinstance()`| Solo dígitos decimales                 |  mas util
| `isnumeric()` | Cualquier carácter numérico            |
| `isalnum()`   | Letras y números                       |
| `isspace()`   | Solo espacios                          |
| `islower()`   | Letras en minúsculas                   |
| `isupper()`   | Letras en mayúsculas                   |
'''

variable13 = 4.3

if (isinstance(variable13, float)):
    print (f'El numero es decimal')
else:
    print (f'Error, no es decimal')


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