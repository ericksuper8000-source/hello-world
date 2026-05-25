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

print (f'-' * 20)

class Camara1():
    def Tomar_Fotografia(self):
        print (f'Fotografia Tomada')
        
class Reproductor_Musica1:
    def Reproducir_Musica(self):
        print (f'Musica Reproducida')
        
class Smartphone1(Camara1, Reproductor_Musica1):
    def Encender_Smartphone(self):
        print (f'Smartphone Encendido')
        
Objeto24 = Smartphone1()

Objeto24.Encender_Smartphone()
Objeto24.Reproducir_Musica()
Objeto24.Tomar_Fotografia()

print (f'-' * 20)

class Persona3:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
    
Objeto25 = Persona3('Erick Josue')

print (f'Hola {Objeto25}')

print (f'-' * 20)

class Veterinaria2():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso
        
    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad}')
        print (f'Peso: {self.Peso}')
        
class Perro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        
    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        
class Gato2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Color, Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Activo = Activo
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Activo: {self.Activo}')
        
class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto26 = Perro2('Chester', 5, 2.8, 'Poodle', 'Asma')

Veterinaria2.Mostrar(Objeto26)
Objeto26.Mostrar()

print (f'-' * 20)

Objeto27 = Gato2('Messi', 1.5, 2, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto27)
Objeto27.Mostrar()

print (f'-' * 20)

Objeto28 = Pajaro2('Polly', 31, 0.4, 'Cacatua Amarilla', 'Si')

Veterinaria2.Mostrar(Objeto28)
Objeto28.Mostrar()

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
        
Objeto29 = Hechicero(75, 'Magic Wand', 40, 'Green Lighting', 500, 'Magistar')

Objeto29.Mostrar()
Atacante2.Mostrar(Objeto29)
Defensor2.Mostrar(Objeto29)

print (f'-' * 20)

Herencia1 = issubclass(Poke_Kid1, Poke1)

print (f'{Herencia1}')

Instancia2 = isinstance(Objeto29, Hechicero)
Instancia3 = isinstance(Objeto29, Atacante2)
Instancia4 = isinstance(Objeto29, Defensor2)

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
        
Objeto30 = D2()

A2.Mostrar(Objeto30)
B2.Mostrar(Objeto30)
C2.Mostrar(Objeto30)
Objeto30.Mostrar()
E2.Mostrar(Objeto30)

print (f'-' * 20)

class Efectivo2():
    def Pagar(self):
        print (f'El pago se realizo en efectivo')
        
class Tarjeta2:
    def Pagar(self):
        print (f'El pago se realizo en tarjeta')
        
class Cripto2:
    def Pagar(self):
        print (f'El pago se realizo en cripto')
        
Objeto31 = Cripto2()
Objeto32 = Tarjeta2()
Objeto33 = Efectivo2()

Objeto31.Pagar()
Objeto32.Pagar()
Objeto33.Pagar()

print (f'-' * 20)

class Cuenta_Bancaria2:
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
        print (f'Su saldo a la fecha es de {self.__Saldo}')
        
Objeto34 = Cuenta_Bancaria2(100)
Objeto34.Depositar(25)
Objeto34.Mostrar()

print (f'Su saldo privado es de {Objeto34.Dinero}')

print (f'-' * 20)

Objeto34.Dinero = '50,000,000'

Objeto34.Mostrar()

print (f'Su saldo privado es de {Objeto34.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla2(Plantilla2):
    def Mostrar(self):
        print (f'Este es un metodo regular')
        
    def General(self):
        print (f'Este metodo es obligatorio debido a la abstraccion')
        
Objeto35 = Sub_Plantilla2()

Objeto35.Mostrar()
Objeto35.General()

print (f'-' * 20)

class Bulbasaur2():
    def Elegir(self):
        return f'Bulbasaur'
    
class Batalla3:
    def __init__(self):
        self.Favorito = Bulbasaur2()
        
    def Batallar(self):
        print (f'Increible, el retador ha elegido un {self.Favorito.Elegir()}!!!')
        
Objeto36 = Batalla3()

Objeto36.Batallar()

print (f'-' * 20)

class Spirigatito2():
    def Elegir(self):
        return f'Spirigatito'
    
class Treekoo2:
    def Elegir(self):
        return f'Treekoo'
    
class Chikorita2:
    def Elegir(self):
        return f'Chikorita'
    
class Batalla4:
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'Increible, el retador ha elegido un {self.Favorito.Elegir()}')
        
Container1 = Spirigatito2()
Objeto37 = Batalla4(Container1)
Objeto37.Batallar()

Container2 = Treekoo2()
Objeto38 = Batalla4(Container2)
Objeto38.Batallar()

Container3 = Chikorita2()
Objeto39 = Batalla4(Container3)
Objeto39.Batallar()

print (f'-' * 20)

class Chocolate1:
    def Elegir(self):
        return f'Chocolate'
    
class Vainilla1:
    def Elegir(self):
        return f'Vainilla'
    
class Fresa1:
    def Elegir(self):
        return f'Fresa'
    
class Pastel1:
    def __init__(self):
        self.Sabor = Chocolate1()
        
    def Hornear(self):
        print (f'Listo, su pastel de {self.Sabor.Elegir()} esta listo')
        
Objeto40 = Pastel1()
Objeto40.Hornear()

print (f'-' * 20)

class Pastel2:
    def __init__(self, Sabor):
        self.Sabor = Sabor
        
    def Hornear(self):
        print (f'Listo, su pastel de {self.Sabor.Elegir()} esta listo')
        
Container4 = Chocolate1()
Objeto41 = Pastel2(Container4)
Objeto41.Hornear()

Container5 = Vainilla1()
Objeto42 = Pastel2(Container5)
Objeto42.Hornear()

Container6 = Fresa1()
Objeto43 = Pastel2(Container6)
Objeto43.Hornear()

print (f'-' * 20)

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

variable6, variable7 = True, not True

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke2"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Variable_Sumatoria}, {Anonima2(14)} o incluso {Objeto20.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Erick' in Lista_Uno)
print (f'Vaporeon' not in PEPE.Set_Conjunto_Poke)
print (PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")] in PEPE.Tupla_Poke)

print (f'-' * 20)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es una declaracion con snake case y al mismo tiempo tenemos un desempaquetado de variables {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

'''Contador = 0
Lista_Cuenta = []

while (Contador < 3):
    while True:
        Numerito3 = input(f'Ingrese el numero {Contador + 1}: ')
        try:
            Numerito4 = float(Numerito3)
            if (Numerito4.is_integer()):
                print (f'Lo que ingresaste fue un numero entero')
                Lista_Cuenta.append(Numerito4)
                break
            else:
                print (f'Lo que ingresaste fue un numero decimal')
                Lista_Cuenta.append(Numerito4)
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador+= 1

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nGracias por lo ingresado, aqui tienes la lista de numeros agregados: {Lista_Cuenta}'])
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()'''
    
Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto21.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'{PEPE.Lista2[::2]}')
print (f'{PEPE.Lista2[::3]}')
print (f'{PEPE.Lista2[:2]}')
print (f'{PEPE.Lista2[2:]}')
print (f'{PEPE.Lista2[2:3]}')
print (f'{PEPE.Lista2[0:None]}')
print (f'{PEPE.Lista2[:]}')

print (f'{Lista_Uno[1]}, eso que esta ahi es un {PEPE.Lista2[2]}?')

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

print (f'{Lista_Uno_Copia}')

Lista_Uno.clear()

print (f'{Lista_Uno}')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'-' * 20)

print (f'{PEPE.__dir__()}') #type: ignore

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
print (f'{Tupla1[2:3]}')

Set_Conjunto1 = {'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo'}
Set_Conjunto1.add('Verde')
Set_Conjunto2 = set({'Amarillo'})
Set_Conjunto1.update(Set_Conjunto2)

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Red', 'Blue', 'Yellow'})

print (f'{Set_Conjunto1}')

Set_Conjunto3 = {1, 2, 3, 4, 5}
Set_Conjunto4 = {4, 5}
Set_Conjunto5 = set({8})

print (f'{Set_Conjunto3.issuperset(Set_Conjunto4)}')
print (f'{Set_Conjunto3 >= Set_Conjunto4}')
print (f'-' * 20)
print (f'{Set_Conjunto4.issubset(Set_Conjunto3)}')
print (f'{Set_Conjunto4 <= Set_Conjunto3}')
print (f'-' * 20)
print (f'{Set_Conjunto3.isdisjoint(Set_Conjunto5)}')
print (f'-' * 20)

SetA2 = {1, 2, 3, 4}
SetB2 = {3, 4, 5, 6}

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

print (f'{SetA2}')

print (f'-' * 20)'''

'''SetA2.intersection_update(SetB2)

print (f'{SetA2}')

print (f'-' * 20)'''

'''SetA2.difference_update(SetB2)

print (f'{SetA2}')

print (f'-' * 20)'''

'''SetB2.difference_update(SetA2)

print (f'{SetB2}')

print (f'-' * 20)'''

'''SetA2.symmetric_difference_update(SetB2)

print (f'{SetA2}')

print (f'-' * 20)'''

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')
Set_Conjunto_Menu2 = frozenset({'Caramelo'})
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, variable1})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

Lista_Set1 = list(Set_Conjunto_Menu1)

print (f'{Lista_Set1}')
print (f'{type(Lista_Set1)}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : variable1,
    'Edad' : Variable_Sumatoria,
    'Votante' : Objeto21.Catched
}

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1["Nombre"]}')
print (f'{Diccionario1.get("Edad")}')

print (f'-' * 20)

Diccionario2 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
}

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2.values()}')
print (f'{Diccionario2.items()}')
print (f'{Diccionario2["Nombre"][2]}')
print (f'{Diccionario2.get("Edad")[0]}') #type: ignore

print (f'-' * 20)

Diccionario3 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3.values()}')
print (f'{Diccionario3.items()}')
print (f'{Diccionario3["Ingresos"]}')
print (f'{Diccionario3.get("Gastos")}')

print (f'-' * 20)

Diccionario1['Nombre'] = Saludar_Dos()

print (f'{Diccionario1}')

del Diccionario1['Nombre']
Diccionario1.pop('Edad')

print (f'{Diccionario1}')

Diccionario_Copia = Diccionario1.copy()

Diccionario1.clear()

print (f'{Diccionario1}')
print (f'{Diccionario_Copia}')

print (f'-' * 20)

Diccionario1 = dict({1 : 'Karlita', 2 : 6, 3 : False})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario1[1]} no puede votar todavia porque apenas tiene {Diccionario2.get("Edad")[2]} añitos') #type: ignore

Diccionario_Vacio1 = dict.fromkeys('ABC', "Hola")
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = Objeto20.Nombre

print (f'{Diccionario_Vacio1}')

print (f'{Diccionario_Vacio2}')

Key1 = [f'Key{i}' for i in range(len(Lista_Uno_Copia))]

print (f'{Key1}')

Diccionario4 = dict(zip(Key1, Lista_Uno_Copia))

for elemento in Diccionario4:
    print (f'{Diccionario4[elemento]}')
    
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
    print (f'{elemento[0]}  -- {elemento[1]}')
    
print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv4 = 'C:\\Repo\\Store.csv'

Cargar_Csv4 = pd.read_csv(Ruta_Csv4)

print (f'{Cargar_Csv4}')

print (f'-' * 20)

Ruta_Csv1 = 'C:\\Repo\\Store.csv'

Fecha4 = '2026-04-01'

try:
    Fech4 = datetime.strptime(Fecha4, '%Y-%m-%d').date()
    Fech4_Formateado = pd.to_datetime(Fech4)
    Cargar_Csv4['date'] = pd.to_datetime(Cargar_Csv4['date'])
except ValueError:
    print (f'Error, el formato de la fecha es incorrecto')
    exit()
    
Cargar_Csv4['TOTALITO'] = Cargar_Csv4['quantity'] * Cargar_Csv4['price']
    
Encontrada4 = Cargar_Csv4[Cargar_Csv4['date'].dt.date == Fech4_Formateado.date()]

if (Encontrada4.empty):
    print (f'No se encontraron ventas en esta fecha')
else:
    print (f'Genial! Ventas encontradas')
    
    Grupo6 = Encontrada4.groupby('product')['quantity'].sum()
    Grupo6_May = Grupo6.idxmax()
    Grupo6_Min = Grupo6.idxmin()
    Grupo6_May_Cant = Grupo6.max()
    Grupo6_Min_Cant = Grupo6.min()
    
    print (f'El la fecha {Fech4_Formateado}, el producto {Grupo6_May} vendio un total de {Grupo6_May_Cant} unidades')
    print (f'El la fecha {Fech4_Formateado}, el producto {Grupo6_Min} vendio un total de {Grupo6_Min_Cant} unidades')
    
    print (f'La cantidad de clientes que nos visitaron en esta fecha fue de {Grupo6.count()}')
    print (f'La cantidad de productos individuales que se compraron en esta fecha fue de {Grupo6.sum()}')

    Grupo7 = Encontrada4.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero que se vendio en {Fech4_Formateado} fue de {Grupo7.sum()}')
    print (f'La media vendida en {Fech4_Formateado} fue de {round(Grupo7.mean(), 2)}')
    
Set_Csv = set(Cargar_Csv4['product'])

Key2 = [f'Key({i})' for i in range(len(Set_Csv))]

print (f'{Key2}')

Diccionario5 = dict(zip(Key2, Set_Csv))

print (f'-' * 20)

for elemento in Diccionario5.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {Division_Baja}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'{type(variable1)}')
print (f'{type(variable4)}')
print (f'{type(PEPE.Division_Flotante)}')
print (f'{type(Lista_Uno_Copia)}')
print (f'{type(Tupla1)}')
print (f'{type(Set_Conjunto_Menu1)}')
print (f'{type(Set_Conjunto_Menu2)}')
print (f'{type(Diccionario1)}')
print (f'{type(Objeto1)}')
print (f'{type(Funcion_Diccionario)}')
print (f'{type(PEPE)}')
print (f'{type(Array2)}')
print (f'{type(Data_Frame1)}')

print (f'-' * 20)

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
    
variable8 = 'Josue'
variable9 = 27

if (variable8 == 'Erick' and variable9 > 30):
    print (f'Ambos condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')
    
print (f'-' * 20)

if (variable8 == 'Erick' or variable9 > 30):
    print (f'Al menos una condicion se cumplen')
else:
    print (f'Error, ninguna de las condiciones se cumple')
    
print (f'{dir(variable1)}')

print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        
    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')
        
Objeto44 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Ash")], 'Kanto', Objeto6.Nombre)

Objeto44.Desplegar()

print (f'-' * 20)

class Persona4():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
    
Objeto45 = Persona4('Josue Gutierrez')

print (f'Hola, funcion magina dunder method {Objeto45}')

Negativo = -5

print (f'{int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima5 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable}')
print (f'{list(Anonima5)}')
print (f'{Lista_Iterable}')

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, ingrese una cadena de texto')
    
'''Contador = 0

while (Contador < 3):
    while True:
        Numerito3 = input(f'Ingrese un numero entero o decimal {Contador + 1}: ')
        try:
            Numerito4 = float(Numerito3)
            if (Numerito4.is_integer()):
                print (f'Lo ingresado es un numero entero, gracias')
                break
            else:
                print (f'Lo ingresado es un numero decimal, gracias')
                break
        except ValueError:
            if (bool(Numerito3) == False):
                print (f'Error, no puede ser una cadena vacia')
            elif (Numerito3.isspace()):
                print (f'Error, no puedes solo meter espacios')
            else:
                print (f'Error, lo que ingresaste no es un numero')
    Contador+= 1'''
    
print (f'-' * 20)

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')
    
print (f'-' * 20)
    
for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'El elemento en la posicion {indice} es {elemento}')
    
print (f'-' * 20)

variable10 = 'eSteBAN'
variable10_letra = variable10[0]

print (f'{variable10}')
print (f'{variable10.lower()}')
print (f'{variable10.upper()}')
print (f'{variable10.capitalize()}')

print (f'La letra t esta en la posicion {variable10.lower().find("t")}')
print (f'La letra b estsa en la posicion {variable10.lower().index("b")}')

print (f'La letra {variable10_letra} aparece un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = 'este es un texto cualquiera pero lo mas importante es que deseo ver si la mica sirve o no'
variable11_Lista = variable11.split(' ')

print (f'La cantidad de palabras digitadas es {len(variable11_Lista)}')

def Generadora4():
    Contador = 0
    while (Contador < len(variable11_Lista)):
        yield f'{variable11_Lista[Contador]}'
        Contador+= 1
        
Gen4 = Generadora4()

try:
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
    print (f'{next(Gen4)}')
except StopIteration:
    print (f'Fin del Esperimento')
    
print (f'-' * 20)
    
variable12 = '21'

if (variable12.replace(' ', '').isalpha()):
    print (f'Lo ingresado es un texto')
else:
    print (f'Lo ingresado no es un texto')
    
if (isinstance(variable12, (str))):
    print (f'Lo ingresado es un texto')
else:
    print (f'Lo ingresado no es un texto')
    
variable13 = '3.4'

try:
    Numerito3 = float(variable13)
    if (Numerito3.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
if (isinstance(variable13, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Lo ingresado no es un numero decimal')
    
print (f'-' * 20)
    
variable14 = '200'

if (variable14.isnumeric()):
    print (f'Lo ingresado es un numero')
else:
    print (f'Lo ingresado no es un numero')

if (isinstance(variable14, (int))):
    print (f'Lo ingresado es un numero')
else:
    print (f'Lo ingresado no es un numero')
    
try:
    Numerito4 = float(variable14)
    if (Numerito4.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

variable15 = '3.4'

if (variable15.isalnum()):
    print (f'Puede tener letras o numeros enteros nada mas')
else:
    print (f'Error, ni letras ni numeros enteros')
    
print (f'-' * 20)

variable16 = '                         '

if (variable16.isspace()):
    print (f'Esto solo lleva espacios')
else:
    print (f'Aqui hay mas que solo espacios')
    
variable17 = 'hOlA MUNdo'

if (variable17.lower().islower()):
    print (f'Correcto, todo es minuscula')
else:
    print (f'Error, el formato es incorrecto')
    
if (variable17.upper().isupper()):
    print (f'Correcto, todo es mayuscula')
else:
    print (f'Error, el formato es incorrecto')
    
print (f'-' * 20)

print (f'El elemento {PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

Lista_Uno_Copia2 = Lista_Uno_Copia.copy()

print (f'{Lista_Uno_Copia2}')

print (f'{Diccionario2}')

Diccionario2.clear()

print (f'{Diccionario2}')

print (f'{Diccionario3}')

Diccionario3.pop("Ingresos")


print (f'{Diccionario3}')

del Diccionario3['Gastos']

print (f'{Diccionario3}')

for elemento in Diccionario4:
    print (f'{Diccionario4[elemento]}')
    
print (f'-' * 20)

for elemento in Diccionario4.keys():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario4.values():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario4.items():
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'-' * 20)

snake_case4, snake_case5, snake_case6, snake_case7 = Lista_Uno_Copia2

print (f'Esto es una declaracion de snake case y al mismo tiempo es un desempaquetado de variables {snake_case5}')

print (f'-' * 20)

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1
    
print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1
    
print (f'-' * 20)

Contador = 0

Lista_Animales = []
Lista_Animales.append('Cocodrilo')
Lista_Animales.insert(1, 'Camello')
Lista_Animales.extend(['Leon'])

print (f'{Lista_Animales}')

for elemento in enumerate(Lista_Animales):
    if (elemento[1] == 'Camello'):
        print (f'Este es un bicho del desierto')
        break
    else:
        Contador+= 1
        continue
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Uno_Copia2, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
print (f'-' * 20)

Lista_Numeros_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Mayor = max(Lista_Numeros_Mult)
Menor = min(Lista_Numeros_Mult)
Redondeado = round(14.458795, 2)

print (f'El menor de la lista es {Menor}')
print (f'El mayor de la lista es {Mayor}')
print (f'El redondeo del numero 14.458795 es {Redondeado}')

print (f'{bool(None)}')
print (f'{bool("")}')
print (f'{bool(False)}')
print (f'{bool(not True)}')
print (f'{bool(0)}')

Todo_All = all([Lista_Uno_Copia2, Tupla1, Set_Conjunto_Menu1, ""])

print (f'{Todo_All}')

print (f'-' * 20)

Sumatoria4 = sum(Lista_Numeros_Mult)

print (f'El resultado de la sumatoria es {Sumatoria4}')

print (f'-' * 20)

Uno = int('500')
Dos = str(500)
Tres = float(Uno)
Lista = list(Set_Conjunto_Menu1)
Set = set(Lista_Uno_Copia2)
Tupla = tuple(Set_Conjunto4)

print (f'{Uno} - {type(Uno)}')
print (f'{Dos} - {type(Dos)}')
print (f'{Tres} - {type(Tres)}')
print (f'{Lista} - {type(Lista)}')
print (f'{Set} - {type(Set)}')
print (f'{Tupla} - {type(Tupla)}')

print (f'-' * 20)

Any_Iterable2 = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima6 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable2 = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable2}')
print (f'{list(Anonima6)}')
print (f'{Lista_Iterable2}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto_Poke))
print (f' - '.join(Lista))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

'''def Floating1():
    while True:
        Flotante1 = input(f'Ingrese un numero: ')
        try:
            Numerito5 = float(Flotante1)
            if (Numerito5.is_integer()):
                Resultado = Variable_Sumatoria + Objeto6.Cantidad * Numerito5
                return f'El resultado de la operacion es {Resultado}'
                break
            else:
                Resultado = Variable_Sumatoria + Objeto6.Cantidad * Numerito5
                return f'El resultado de la operacion es {round(Resultado, 2)}'
                break
        except ValueError:
            print (f'Error, necesito que ingrese un numero')

print (f'{Floating1()}')'''

'''Resultado = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado}')'''

'''def Validador_Nombre(Nombre):
    Full_Name = Nombre.replace(' ', '')
    if (Full_Name.isalpha()):
        return f'Gracias, lo ingresado - {Nombre} es un texto'
    else:
        return f'Error, lo ingresado no es un texto'

print (f'{Validador_Nombre(PEPE.Flotante3)}')'''

'''def Floating4(Textito):
    Lista_Textito = Textito.split(' ')
    for elemento in Lista_Textito:
        print (f'{elemento}')
        
    print (f'La cantidad de palabras digitadas es {len(Lista_Textito)}')
        
Floating4(PEPE.Flotante4)'''

'''Lista_Alumno = []

Contador = 3

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el estudiante {elemento}: ')
        Lista.append(Alumno)
        
    return Lista

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nLa lista de alumnos es {Colegio(Lista_Alumno)}')
    Docu.close()
    
with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()'''
    
'''Lista_Alumnos = []

Contador = int(input(f'Ingrese el numero de estudiantes: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del estudiante {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del estudiante {elemento}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.extend([Estudiante])
        
    Lista.sort(key = lambda Num : Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El estudiante con menor edad es {Menore} con una edad es {Lista[0][1]} años')
    print (f'El estudiante con mayor edad es {Mayore} con una edad es {Lista[-1][1]} años')
    
Colegio(Lista_Alumnos)'''

import pandas as pd
import requests
import io

Ruta_Html2 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html2, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Leer_Html)

print (f'{Cargar_Html2[2].head()}')

import re

Texto18 = 'example@gmail.com'

Pattern11 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)$'

Buscar20 = bool(re.match(Pattern11, Texto18))

if (Buscar20 == True):
    print (f'Formato de correo valido')
else:
    print (f'Error, formato de correo invalido')
    
import re

Texto19 = '32'

Buscar21 = bool(re.match(r'(0[0-9]|[12][0-9]|3[01])', Texto19))

if (Buscar21 == True):
    print (f'El numero se encuentra entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
import pandas as pd
from datetime import datetime
    
Ruta_Csv5 = 'C:\\Repo\\Store.csv'

Cargar_Csv5 = pd.read_csv(Ruta_Csv5)

print (f'{Cargar_Csv5}')

print (f'-' * 20)

Fecha5 = '2026-04-01'

try:
    Fech5 = datetime.strptime(Fecha5, '%Y-%m-%d').date()
    Fech5_Formateada = pd.to_datetime(Fech5)
    Cargar_Csv5['date'] = pd.to_datetime(Cargar_Csv5['date'])
except ValueError:
    print (f'Error, el formato de la fecha es incorrecta')
    exit()
    
Cargar_Csv5['TOTALITO'] = Cargar_Csv5['quantity'] * Cargar_Csv5['price']
    
Encontrada5 = Cargar_Csv5[Cargar_Csv5['date'].dt.date == Fech5_Formateada.date()]

if (Encontrada5.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print ('Genial!, se encontraron ventas')
    Grupo8 = Encontrada5.groupby('product')['quantity'].sum()
    Grupo8_May = Grupo8.idxmax()
    Grupo8_Min = Grupo8.idxmin()
    Grupo8_May_Cant = Grupo8.max()
    Grupo8_Min_Cant = Grupo8.min()
    
    print (f'En la fecha {Fech5_Formateada} el producto {Grupo8_May} vendio un total de {Grupo8_May_Cant} unidades')
    print (f'En la fecha {Fech5_Formateada} el producto {Grupo8_Min} vendio un total de {Grupo8_Min_Cant} unidades')
    
    print (f'La cantidad de clientes que nos visitaron en esta fecha fue de {Grupo8.count()}')
    print (f'La cantidad de productos vendidos en esta fecha fue de {Grupo8.sum()}')
    
    Grupo9 = Encontrada5.groupby('product')['TOTALITO'].sum()
    
    print (f'El total de ventas en dinero en esta fecha es de {Grupo9.sum()}')
    print (f'El promedio de ventas en esta fecha es de {Grupo9.mean()}')
    
