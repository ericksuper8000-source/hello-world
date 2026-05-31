try:
    import Module_Own as PEPE1
except ImportError:
    print (f'Error, el modulo seleccionado no existe')
    raise

variable1 = '33'

try:
    variable2 = float(variable1)
    if (variable2.is_integer()):
        print (f'El numero ingresado es entero')
    else:
        print (f'El numero ingresado es decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
if (isinstance(variable1, (int))):
    print (f'Lo ingresado es un numero entero')
elif (isinstance(variable1, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Error, lo ingresado no es un numero')
    
if (variable1.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero entero')
    
print (f'-' * 20)

variable3 = 3.5

try:
    variable4 = float(variable3)
    if (variable4.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
if (isinstance(variable3, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Lo ingresado no es un numero decimal')
    
print (f'-' * 20)

variable5 = 5.9

try:
    variable6 = float(variable5)
    if (variable6.is_integer()):
        print (f'Esto es un numero entero, lo cual es valido')
    else:
        print (f'Esto es un numero decimal, lo cual es valido')
except ValueError:
    print (f'Lo ingresado no es numero')
    
if (isinstance(variable5, (int, float))):
    print (f'Esta mica es numero entero o decimal, lo cual es valido')
else:
    print (f'Lo ingresado no es un numero')
    
print (f'-' * 20)

import re

Texto1 = "   Hola!!!   mundo@@   123   "

print (f'{Texto1}')

Texto1_Version1 = Texto1.strip()

print (f'{Texto1_Version1}')

Texto1_Version2 = ' '.join(Texto1_Version1.split())

print (f'{Texto1_Version2}')

Texto1_Version3 = Texto1_Version2.lower()

print (f'{Texto1_Version3}')

Buscar1 = re.sub(r'\!|\@|\d+', '', Texto1_Version3)

print (f'{Buscar1}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Fecha1 = '2026-04-01'

Ruta_Csv1 = 'C:\\Repo\\Store.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

print (f'-' * 20)

try:
    Fech1 = datetime.strptime(Fecha1, '%Y-%m-%d').date()
    Fech1_Formateada = pd.to_datetime(Fech1)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato incorrecto')
    exit()
    
Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrado1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()]

if (Encontrado1.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! Encontramos ventas')
    
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_May = Grupo1.idxmax()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_May_Cant = Grupo1.max()
    Grupo1_Min_Cant = Grupo1.min()
    
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_May} vendio un total de {Grupo1_May_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Min} vendio un total de {Grupo1_Min_Cant} unidades')
    
    print (f'En esta fecha, nos compraron {Grupo1.count()} clientes')
    print (f'La cantidad de productos individuales vendidos en esta fecha fue de {Grupo1.sum()}')
    
    Grupo2 = Encontrado1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendida en esta fecha fue de ${Grupo2.sum()}')
    print (f'La media vendida fue de ${Grupo2.mean()}')
    
print (f'-' * 20)

SetA1 = {1, 2, 3, 4}
SetB1 = set({3, 4, 5, 6})

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

SetC1 = {1, 2, 3, 4, 5}
SetD1 = {4, 5}
SetE1 = set({8})

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

SetA1.symmetric_difference_update(SetB1)

print (f'{SetA1}')

print (f'-' * 20)

class Persona1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
    
Objeto1 = Persona1('Erick Perez')

print (f'Hola, mi nombre es {Objeto1}')

print (f'-' * 20)

class Bulbasaur1():
    def Elegir(self):
        return f'Bulbasaur'
    
class Batallar:
    def __init__(self):
        self.Favorito = Bulbasaur1()
        
    def Batalla(self):
        print (f'{self.Favorito.Elegir()} entra a la batalla!')
        
Objeto2 = Batallar()

Objeto2.Batalla()

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
    
class Batallar2:
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'{self.Favorito.Elegir()} entra a la batalla!')
        
Rotator1 = Spirigatito1()
Objeto3 = Batallar2(Rotator1)
Objeto3.Batallar()

Rotator2 = Treekoo1()
Objeto4 = Batallar2(Rotator2)
Objeto4.Batallar()

Rotator3 = Chikorita1()
Objeto5 = Batallar2(Rotator3)
Objeto5.Batallar()

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

Pattern1 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|org|net)'

Buscar2 = re.findall(Pattern1, Texto2)

print (f'{Buscar2}')

print (f'-' * 20)

for indice, elemento in enumerate(Buscar2, start=1):
    print (f'{indice} -- {elemento}')
    
print (f'-' * 20)

Texto3 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???"""

# WAY NUMBER #1

import re

Pattern2 = r'\!|\?|\.{2,}'

Buscar3 = re.sub(Pattern2, '', Texto3)

print (f'{Buscar3}')

Pattern3 = r'\d{4}\-[0-9]{2,4}'

Buscar4 = re.sub(Pattern3, '', Buscar3)

print (f'{Buscar4}')

# WAY NUMBER #2

import re

Texto4 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???"""

Correos1 = re.findall(r'[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.(?:com|net|org)', Texto4)

print (f'{Correos1}')

Texto4_temp1 = Texto4

for i, email in enumerate(Correos1, start=1):
    Texto4_temp1 = Texto4_temp1.replace(email, f'RANDOM{i}')
    
print (f'{Texto4_temp1}')

Pattern4 = r'\!|\?|\.{2,}'

Texto4_temp2 = re.sub(Pattern4, '', Texto4_temp1)

print (f'{Texto4_temp2}')

Pattern5 = r'\d{4}\-[0-9]{3,4}'

Texto4_temp3 = re.sub(Pattern5, '', Texto4_temp2)

print (f'{Texto4_temp3}')

for i, email in enumerate(Correos1, start=1):
    Texto4_temp3 = Texto4_temp3.replace(f'RANDOM{i}', email)
    
print (f'{Texto4_temp3}')

print (f'-' * 20)

import re

Texto5 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!"""

Correos2 = re.findall(r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)', Texto5)

print (f'{Correos2}')

Texto5_temp1 = Texto5

for i, email in enumerate(Correos2, start=1):
    Texto5_temp1 = Texto5_temp1.replace(email, f'TOKEN{i}')
    
print (f'{Texto5_temp1}')

Pattern6 = r'\!|\?'

Texto5_temp2 = re.sub(Pattern6, '', Texto5_temp1)

print (f'{Texto5_temp2}')

for i, email in enumerate(Correos2, start=1):
    Texto5_temp2 = Texto5_temp2.replace(f'TOKEN{i}', email)
    
print (f'{Texto5_temp2}')

print (f'-' * 20)

for elemento in PEPE1.Diccionario_Poke:
    print (f'{PEPE1.Diccionario_Poke[elemento]}')
    
print (f'-' * 20)

for elemento in PEPE1.Diccionario_Poke.keys():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in PEPE1.Diccionario_Poke.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in PEPE1.Diccionario_Poke.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

'''Contador = 0

Lista_Promedio = list([])

while (Contador < 3):
    while True:
        Numerito1 = input(f'Ingrese el numero {Contador + 1}: ')
        try:
            Numerito2 = float(Numerito1)
            if (Numerito2.is_integer()):
                Lista_Promedio.append(Numerito2)
                break
            else:
                Lista_Promedio.append(Numerito2)
                break
        except ValueError:
            print (f'Error, lo ingresado no es un numero')
    Contador+= 1
    
Promedio1 = sum(Lista_Promedio) / len(Lista_Promedio)

print (f'El promedio de las notas es de {round(Promedio1, 2)}')'''

from Module_Own import Pokemon1 as Poke1

Objeto6 = Poke1(PEPE1.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto7 = Poke1(PEPE1.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto6.Mostrar()

print (f'Actualmente tengo {Objeto7.Cantidad} Pokemones')

if (Objeto6.Catched == True):
    print (f'El pokemon fue capturado')
else:
    print (f'El pokemon no fue capturado')
    
print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto8 = Poke_Kid1(PEPE1.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto8)
Objeto8.Mostrar()

print (f'-' * 20)

class Veterinaria1():
    def __init__(self, Nombre, Peso, Edad):
        self.Nombre = Nombre
        self.Peso = Peso
        self.Edad = Edad
        
    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Peso: {self.Peso}kgs')
        print (f'Edad: {self.Edad} años')
        
class Perro1(Veterinaria1):
    def __init__(self, Nombre, Peso, Edad, Raza, Padecimiento):
        super().__init__(Nombre, Peso, Edad)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        
    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        
Objeto9 = Perro1('Chester', 2.8, 5, 'Poodle', 'Hiper-Tension')

Veterinaria1.Mostrar(Objeto9)
Objeto9.Mostrar()

print (f'-' * 20)

class Gato1(Veterinaria1):
    def __init__(self, Nombre, Peso, Edad, Color, Activo):
        super().__init__(Nombre, Peso, Edad)
        self.Color =Color
        self.Activo = Activo
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente Activo: {self.Activo}')
        
Objeto10 = Gato1('Messi', 1.8, 1.5, 'Gris', 'No')

Veterinaria1.Mostrar(Objeto10)
Objeto10.Mostrar()

print (f'-' * 20)

class Pajaro1(Veterinaria1):
    def __init__(self, Nombre, Peso, Edad, Especie, Habla):
        super().__init__(Nombre, Peso, Edad)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto11 = Pajaro1('Polly', 0.4, 31, 'Lora Verde', 'Si')

Veterinaria1.Mostrar(Objeto11)
Objeto11.Mostrar()

print (f'-' * 20)

class Atacante1():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon

    def Mostrar(self):
        print (f'Damamge: {self.Damage}pts')
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
Objeto14.Pagar()

Objeto15 = Tarjeta1()
Objeto15.Pagar()

Objeto16 = Efectivo1()
Objeto16.Pagar()

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
        
Objeto17 = Cuenta_Bancaria(100)
Objeto17.Depositar(25)
Objeto17.Mostrar()

print (f'Su saldo privado es de {Objeto17.Dinero}')

Objeto17.Dinero = '50,000,000'

Objeto17.Mostrar()

print (f'Su saldo privado es de {Objeto17.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla1(ABC):
    def Reciclada(self):
        pass

class Sub_Plantilla1(Plantilla1):
    def Mostrar(self):
        print (f'Este metodo no es obligatorio')
        
    def Reciclada(self):
        print (f'Este metodo si es obligatorio')
        
Objeto18 = Sub_Plantilla1()

Objeto18.Mostrar()
Objeto18.Reciclada()

print (f'-' * 20)

class Chocolate1():
    def Elegir(self):
        return f'Chocolate'
    
class Vainilla1():
    def Elegir(self):
        return f'Vainilla'
    
class Fresa1():
    def Elegir(self):
        return f'Fresa'
    
class Pastel1:
    def __init__(self):
        self.Favorito = Chocolate1()
        
    def Hornear(self):
        print (f'Hoy horneamos un pastel de {self.Favorito.Elegir()}')
        
Objeto19 = Pastel1()
Objeto19.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy horneamos un pastel de {self.Favorito.Elegir()}')
        
Rotator4 = Chocolate1()
Objeto19 = Pastel2(Rotator4)
Objeto19.Hornear()

Rotator5 = Vainilla1()
Objeto20 = Pastel2(Rotator5)
Objeto20.Hornear()

Rotator6 = Fresa1()
Objeto21 = Pastel2(Rotator6)
Objeto21.Hornear()

print (f'-' * 20)

import re

Texto6 = 'esto es 12 un texto cualquiera! para ver si la 9 hola mica funciona correctamente, lo mas 450 @ hela importante @ es ver si al final esto hala es util o no'

Buscar5 = re.search(r'ver', Texto6)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\d+', Texto6)
Buscar7 = re.findall(r'\s+', Texto6)
Buscar8 = re.findall(r'\S+', Texto6)
Buscar9 = re.findall(r'\w+', Texto6)
Buscar10 = re.findall(r'\W+', Texto6)
Buscar11 = re.findall(r'\D+', Texto6)

print (f'{Buscar6}')

print (f'-' * 20)

print (f'{Buscar7}')

print (f'-' * 20)

print (f'{Buscar8}')

print (f'-' * 20)

print (f'{Buscar9}')

print (f'-' * 20)

print (f'{Buscar10}')

print (f'-' * 20)

print (f'{Buscar11}')

print (f'-' * 20)

Buscar12 = re.fullmatch(r'esto es 12 un texto cualquiera! para ver si la 9 hola mica funciona correctamente, lo mas 450 hela importante @ es ver si al final esto hala es util o no', Texto6)

print (f'{Buscar12}')

Buscar13 = re.findall(r'h.la', Texto6)

print (f'{Buscar13}')

Buscar14 = re.findall(r'^esto', Texto6)

Buscar15 = re.findall(r'o$', Texto6)

print (f'{Buscar14}')

print (f'{Buscar15}')

Pattern7 = r'\d{3}\s?\W{1}'

Buscar16 = re.findall(Pattern7, Texto6)

print (f'{Buscar16}')

Buscar17 = re.findall(r'[ei]{2,}', Texto6)

print (f'{Buscar17}')

Texto7 = 'ericksuper80@gmail.com'

Pattern8 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|org|net)$'

Buscar18 = bool(re.fullmatch(Pattern8, Texto7))

if (Buscar18 == True):
    print (f'El correo tiene el formato correcto')
else:
    print (f'El correo no tiene el formato correcto')
    
print (f'-' * 20)

Pattern9 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.[a-z]{2,}$'

Buscar19 = bool(re.match(Pattern9, Texto7))

if (Buscar19 == True):
    print (f'El correo tiene el formato correcto')
else:
    print (f'El correo no tiene el formato correcto')
    
print (f'-' * 20)

import re

Texto8 = '32'

Pattern10 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar20 = bool(re.fullmatch(Pattern10, Texto8))

if (Buscar20):
    print (f'El numero esta entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
import re
    
Texto9 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern11 = r'\d{2}\/[0-9]{2}\/\d{3,4}'

Replacement1 = 'XX/XX/XXXX'

Buscar21 = re.sub(Pattern11, Replacement1, Texto9)

print (f'{Buscar21}')

Pattern12 = r'\+\d{1}\-[0-9]{3}\-\d{3}\-[0-9]{3,4}'

Replacement2 = '+*-***-***-****'

Buscar22 = re.sub(Pattern12, Replacement2, Buscar21)

print (f'{Buscar22}')

print (f'-' * 20)

import re

# usuario@dominio.extension

Texto10 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Pattern13 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|net|org)'

Buscar23 = re.findall(Pattern13, Texto10)

print (f'{Buscar23}')

print (f'-' * 20)

for indice, elemento in enumerate(Buscar23, start=1):
    print (f'{indice} -- {elemento}')
    
print (f'-' * 20)

import re

# Way #1

Texto11 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern14 = r'\!|\?|\.{2,}'

Buscar24 = re.sub(Pattern14, '', Texto11)

print (f'{Buscar24}')

Pattern15 = r'\d{4}\-[0-9]{3,4}'

Replacement3 = ''

Buscar25 = re.sub(Pattern15, Replacement3, Buscar24)

print (f'{Buscar25}')

import re

# Way #1

print (f'{Texto11}')

Correos3 = re.findall(r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)', Texto11)

print (f'{Correos3}')

Texto11_temp = Texto11

for i, email in enumerate(Correos3, start=1):
    Texto11_temp = Texto11_temp.replace(email, f'Borrador_{i}')
    
print (f'{Texto11_temp}')

Pattern16 = r'\!|\?|\.{2,}'

Texto11_temp2 = re.sub(Pattern16, '', Texto11_temp)

print (f'{Texto11_temp2}')

Texto11_temp3 = re.sub(r'\d{4}\-[0-9]{4}', '', Texto11_temp2)

print (f'{Texto11_temp3}')

for i, email in enumerate(Correos3, start=1):
    Texto11_temp3 = Texto11_temp3.replace(f'Borrador_{i}', email)
    
print (f'{Texto11_temp3}')

print (f'-' * 20)

Texto12 = '3.5'

try:
    Numerito1 = float(Texto12)
    if (Numerito1.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
if (isinstance(Texto12, (float))):
    print (f'Lo ingresado es un numero decimal')
elif (isinstance(Texto12, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero')
    
print (f'-' * 20)

Texto13 = '2'

try:
    Numerito2 = float(Texto13)
    if (Numerito2.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado no es un numero')
    
if (Texto13.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
if (isinstance(Texto13, (int))):
    print (f'Lo ingresado es un numero entero')
elif (isinstance(Texto13, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Lo ingresado no es un numero')
    
print (f'-' * 20)

import re

Texto14 = "   Hola!!!   mundo@@   123   "

Texto14_Version1 = Texto14.strip()
Texto14_Version2 = ' '.join(Texto1_Version1.split())
Texto14_Version3 = Texto14_Version2.lower()

Texto14_Version4 = re.sub(r'\!|\@|\d+', '', Texto14_Version3)

print (f'{Texto14_Version4}')

print (f'-' * 20)

def Exception1(Elemento):
    try:
        Numerito3 = float(Elemento)
        if (Numerito3.is_integer()):
            return f'Lo ingresado es un numero entero'
        else:
            return f'Lo ingresado es un numero decimal'
    except ValueError:
        return f'Error, lo ingresado no es un numero'

print (f'{Exception1("Hola")}')

def Exception2(Num1, Num2):
    try:
        Numerito4 = float(Num1)
        Numerito5 = float(Num2)
        if (Numerito4.is_integer() and Numerito5.is_integer()):
            Resultado1 = Numerito4 + Numerito5
            print (f'El resultado de la operacion es {Resultado1}')
        elif (Numerito4.is_integer() or Numerito5.is_integer()):
            Resultado1 = Numerito4 + Numerito5
            print (f'El resultado de la operacion es {round(Resultado1, 2)}')
    except TypeError:
        print (f'Error, ambos elementos deben ser numeros')
        
Exception2("6", 3.5)

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')
        
Exception3(12, 0)

Lista_Exception4 = list([])
Lista_Exception4.append('Erick')
Lista_Exception4.insert(1, 'Josue')
Lista_Exception4.extend(['Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento en la posicion {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')
        
Exception4(3)

Lista_Exception5 = ['Erick', 37]

Key1 = [f'Key_{i}' for i in range(len(Lista_Exception5))]

print (f'{Key1}')

Diccionario_Exception5 = dict(zip(Key1, Lista_Exception5))

print (f'{Diccionario_Exception5}')

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')
        
Exception5('Key_2')

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv('C:\\Repo\\HolaMundo.txt')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Hiena')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo seleccionado no existe')
    
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
    Documento_Agregar = Docu.write(f'\n{PEPE1.Diccionario_Poke["Poke1"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE1.Diccionario_Poke["Poke2"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE1.Diccionario_Poke["Poke3"]}\n')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE1.Set_Conjunto_Poke1)])
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
import pandas as pd

DataFrame1 = pd.DataFrame({
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
})

DataFrame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [55, 14, 26],
    'Votante' : [True, False, not False]
})

DataFrame_Concatenate = pd.concat([DataFrame1, DataFrame2])

DataFrame_Concatenate_Age = DataFrame_Concatenate['Edad']

print (f'{DataFrame_Concatenate}')

print (f'-' * 20)

Grupo3 = DataFrame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_May = Grupo3.idxmax()
Grupo3_Min = Grupo3.idxmin()

print (f'La persona mayor es {Grupo3_May} con una edad de {DataFrame_Concatenate_Age.max()} años y la persona con menor edad es {Grupo3_Min} con una edad de {DataFrame_Concatenate_Age.min()} años')

print (f'{DataFrame_Concatenate.info()}')

print (f'-' * 20)

for indice, elemento in DataFrame_Concatenate.iterrows():
    elementito1 = elemento['Nombre']
    elementito2 = elemento['Edad']
    
    print (f'Mi nombre es {elementito1} y mi edad es {elementito2} años')
    
print (f'-' * 20)

print (f'La cantidad de elementos del dataframe son {Grupo3.count()} elementos')
print (f'Si sumamos todas las edades, el numero resultante es {Grupo3.sum()}')
print (f'La media de las edades es {round(Grupo3.mean(), 2)}')

'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=DataFrame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=DataFrame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=DataFrame_Concatenate)

plt.show()

print (f'-' * 20)'''

print (f'{DataFrame_Concatenate.head(1)}')

print (f'-' * 20)

print (f'{DataFrame_Concatenate.head(2)}')

print (f'-' * 20)

print (f'{DataFrame_Concatenate.tail(1)}')

print (f'-' * 20)

Filas, Columnas = DataFrame_Concatenate.shape

print (f'La cantidad de Filas es {Filas}')
print (f'La cantidad de Columnas es {Columnas}')

Elemento1 = DataFrame1.loc[0, 'Nombre']
Elemento2 = DataFrame1.loc[1, 'Nombre']
Elemento3 = DataFrame1.loc[2, 'Nombre']
Elemento4 = DataFrame1.loc[1, :]
Elemento5 = DataFrame1.loc[:, 'Edad']

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')
print (f'{Elemento4}')
print (f'{Elemento5}')

print (f'-' * 20)

Elemento6 = DataFrame2.iloc[0, 0]
Elemento7 = DataFrame2.iloc[1, 1]
Elemento8 = DataFrame2.iloc[2, 2]
Elemento9 = DataFrame2.iloc[1, :]
Elemento10 = DataFrame2.iloc[:, 2]

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
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='familiares')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:J")
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols="E:J", nrows=1)

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

Cargar_Excel3_Sorted_Descending_Edad = Cargar_Excel3_Sorted_Descending['cinco']

print (f'{Cargar_Excel3_Sorted_Descending_Edad}')

Cargar_Excel3_Sorted_Descending['TOTALITO'] = Cargar_Excel3_Sorted_Descending['cinco'] * Cargar_Excel3_Sorted_Descending['ocho']

Grupo4 = Cargar_Excel3_Sorted_Descending.groupby('tres')['cinco'].sum()
Grupo4_May = Grupo4.idxmax()
Grupo4_Min = Grupo4.idxmin()

print (f'El menor de los compas es {Grupo4_Min} y su edad es {Cargar_Excel3_Sorted_Descending_Edad.min()} años, y el compa mayor es {Grupo4_May} y su edad es {Cargar_Excel3_Sorted_Descending_Edad.max()} años')

Grupo5 = Cargar_Excel3_Sorted_Descending.groupby('tres')['TOTALITO'].sum()

print (f'{Grupo5}')

print (f'La cantidad de registros en el excel son {Grupo5.count()}')
print (f'La media de los precios es {round(Grupo5.mean(), 2)}')
print (f'Si sumamos todos los valores me da {Grupo5.sum()}')

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

Array0 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print (f'{Array0}')
print (f'{Array0[0][:2]}')
print (f'{Array0[0][2:]}')
print (f'{Array0[1][::2]}')
print (f'{Array0[2][::3]}')
print (f'{Array0[:][1]}')
print (f'{Array0[2][2:3]}')
print (f'{Array0[0][0:None]}')
print (f'{Array0[0][:]}')

print (f'-' * 20)

for i in range(len(Array0)):
    for j in range(len(Array0[i])):
        print (f'{Array0[i][j]}')
        
print (f'-' * 20)

import numpy as np

Array1 = np.array([1, 2, 3])

print (f'{Array1}')
print (f'{Array1.ndim}')
print (f'{Array1.shape}')
print (f'{Array1.size}')
print (f'{Array1.dtype}')
print (f'{Array1[1]}')

print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[2:3]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 >= 2]}')

print (f'-' * 20)

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}')
print (f'{Array2.shape}')
print (f'{Array2.size}')
print (f'{Array2.dtype}')
print (f'{Array2[1, 2]}')

print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[1, 2:3]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')

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

Array3 = np.array([[['e', 'c', 'i'], ['s', 'f', 'x']],    [['w', 'r', 'o'], ['n', 'm', 'k']]])

print (f'{Array3}')
print (f'{Array3.ndim}')
print (f'{Array3.shape}')
print (f'{Array3.size}')
print (f'{Array3.dtype}')
print (f'{Array3[1, 0, 2:3]}')

print (f'{Array3[1, 1, :2]}')
print (f'{Array3[1, 1, 2:]}')
print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[1, :, 0]}')
print (f'{Array3[0, 0, 2:3]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "x"]}')

print (f'-' * 20)

Array4 = np.array([[[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]], [[[6, 5, 4], [8, 7, 6]], [[4, 9, 8], [7, 6, 3]]]],           [[[[4, 1, 0], [6, 9, 8]],   [[1, 2 ,3], [6, 7, 8]]],     [[[3, 9, 0], [4, 6, 1]], [[2, 5, 8], [3, 6, 9]]]]])

print (f'{Array4}')
print (f'{Array4.ndim}')
print (f'{Array4.shape}')
print (f'{Array4.size}')
print (f'{Array4.dtype}')
print (f'{Array4[1, 0, 0, 1, 2:3]}')

print (f'{Array4[0, 1, 0, 0, ::2]}')
print (f'{Array4[0, 1, 0, 0, ::3]}')
print (f'{Array4[1, 0, 1, 0, :2]}')
print (f'{Array4[1, 0, 1, 0, 2:]}')
print (f'{Array4[1, 1, 0, :, 2]}')
print (f'{Array4[0, 1, 0, 1, 2:3]}')
print (f'{Array4[0, 0, 0, 0, 0:None]}')
print (f'{Array4[0, 0, 0, 0, :]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sort = np.sort(Array4)
Array4_Sort_Mean = np.mean(Array4_Sort)
Array4_Sort_Sum = np.sum(Array4_Sort)

print (f'Acomodados: {Array4_Sort}')
print (f'Media: {round(Array4_Sort_Mean, 2)}')
print (f'Sumatoria: {Array4_Sort_Sum}')

Sumita5 = np.sum(Array4, axis=0)
Sumita6 = np.sum(Array4, axis=1)
Sumita7 = np.sum(Array4[1, 0, 1, 1, 0:None])
Sumita8 = np.sum(Array4[1, 0, 1, 1, :])

print (f'{Sumita5}')
print (f'{Sumita6}')
print (f'{Sumita7}')
print (f'{Sumita8}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1) #type: ignore

print (f'{Array_Num1}')

Array_Menor = np.min(Array_Num1)
Array_Mayor = np.max(Array_Num1)

print (f'El numero menor de la lista es {Array_Menor} y el mayor es {Array_Mayor}')

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

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 0]}')

print (f'{Array_Zeros[0, :2]}')
print (f'{Array_Zeros[0, 2:]}')
print (f'{Array_Zeros[1, ::2]}')
print (f'{Array_Zeros[0, ::3]}')
print (f'{Array_Zeros[:, 1]}')
print (f'{Array_Zeros[1, 2:3]}')
print (f'{Array_Zeros[0, 0:None]}')
print (f'{Array_Zeros[0, :]}')
print (f'{Array_Zeros[Array_Zeros == 0.0]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 2:3]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE1.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[0, 2]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value = f'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[3]}')

print (f'-' * 20)

Lista_Array1 = []

for elemento in enumerate(Array_Gen2):
    Lista_Array1.extend([str(elemento[1])])
    
print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value=Array4[0, 1, 1, 0, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[0, 1]}')

print (f'-' * 20)

Tupla_Array1 = ('Rojo', 'Negro')
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array1)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array['Nombre'][2:3])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'-' * 20)

print (f'{Array_Gen6[3]}')

print (f'-' * 20)

Array_Num3 = np.arange(start=1, stop=6, step=1) #type: ignore
Array_Num4 = np.arange(start=2, stop=11, step=2) #type: ignore
Array_Num5 = np.arange(start=3, stop=31, step=3) #type: ignore
Array_Num6 = np.arange(start=10, stop=21, step=2) #type: ignore
Array_Num7 = np.arange(10) #type: ignore

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

Array_Random2_Sort = np.sort(Array_Random2)
Array_Random2_Sort_Mean = np.mean(Array_Random2_Sort)
Array_Random2_Sort_Sum = np.sum(Array_Random2_Sort)

print (f'Acomodado: {Array_Random2_Sort}')
print (f'Media: {round(Array_Random2_Sort_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sort_Sum}')

Sumita9 = np.sum(Array_Random2, axis=0)
Sumita10 = np.sum(Array_Random2, axis=1)
Sumita11 = np.sum(Array_Random2[0, 0:None])
Sumita12 = np.sum(Array_Random2[0, :])

print (f'Sumita: {Sumita9}')
print (f'Sumita: {Sumita10}')
print (f'Sumita: {Sumita11}')
print (f'Sumita: {Sumita12}')

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

Expo = Arr2 ** 2
Mod = Arr1 % 6

print (f'El resultado de la operacion es {Expo}')
print (f'El resultado de la operacion es {Mod}')

print (f'-' * 20)

Array_Num8 = np.arange(start=1, stop=21, step=1) #type: ignore

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Lista_Array2 = list([])
Lista_Array2.append('Erick')
Lista_Array2.insert(1, 'Josue')
Lista_Array2.extend(['Karlita'])

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-' * 20)

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1) #type: ignore

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

for Matriz3 in Array4:
    for Matriz2 in Matriz3:
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

print (f'Los menores de las columnas son {Array_Random3_Column_Min}')
print (f'Los mayores de las columnas son {Array_Random3_Column_Max}')
print (f'Los menores de las filas son {Array_Random3_Row_Min}')
print (f'Los mayores de las filas son {Array_Random3_Row_Max}')

print (f'-' * 20)

Set_Conjunto_Array2 = set({'Erick'})
Set_Conjunto_Array3 = set({'Carmelo', 'Susanita'})
Set_Conjunto_Array3.add('Roxana')
Set_Conjunto_Array2.add('Josue')
Set_Conjunto_Array4 = {'Karlita'}

Set_Conjunto_Array2.update(Set_Conjunto_Array4)
Set_Conjunto_Array2.update(Set_Conjunto_Array3)

print (f'{Set_Conjunto_Array2}')

Lista_Array3 = list(Set_Conjunto_Array2)

Ganador1 = np.random.choice(Lista_Array3, size=(1), replace=False) #type: ignore
Ganador2 = np.random.choice(Lista_Array3, size=(2), replace=False) #type: ignore
Ganador3 = np.random.choice(Lista_Array3, size=(2, 3), replace=False) #type: ignore

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
    print (f'Experimento termina aqui')
    
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
    print (f'Experimento termina aqui')
    
print (f'-' * 20)

def Generadora3():
    for elemento in range(5):
        if (elemento == 0):
            yield f'Number Zero'
        elif (elemento == 1):
            yield f'Number One'
        elif (elemento == 2):
            yield f'Number Two'
        elif (elemento == 3):
            yield f'Number Three'
        elif (elemento == 4):
            yield f'Number Four'
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
   print (f'Experimento termina aqui')
   
print (f'-' * 20)

Lista_Numeros1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Calculo(Lista):
    Min = min(Lista)
    Max = max(Lista)
    Lista_Resultado = list([Min, Max])
    return Lista_Resultado

print (f'La lista resultado es {Calculo(Lista_Numeros1)}')

PEPE1.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE1.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE1.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int) -> int:
        return Num1 + Num2
    
    return Sumatoria_Interna(4)

Variable_Sumatoria = Sumatoria_Externa(3)

print (f'El resultado de la sumatoria es {Variable_Sumatoria}')

if (PEPE1.Par(Variable_Sumatoria) == True):
    print (f'El numero es par')
else:
    print (f'El numero es impar')
    
PEPE1.Usuario1(Saludar_Dos(), 'masculino')

def Usuario_Externa():
    def Usuario_Interno(Sexo):
        Genero = Sexo.lower()
        if (Genero == 'masculino'):
            return True
        else:
            return False
        
    return Usuario_Interno('masculino')

Variable_Usuario = Usuario_Externa()

if (Variable_Usuario == True):
    print (f'YOU ARE A MAN')
else:
    print (f'YOU ARE A WOMAN')
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE1.Contrasena(42)}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')
    raise

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

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')
        
    print (f'-' * 20)
        
    for elemento in kwargs:
        print (f'{kwargs[elemento]}')
        
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
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

Any_Par = any(num % 2 == 0 for num in PEPE1.Lista_Numeros)
Lista_Par = [num for num in PEPE1.Lista_Numeros if num % 2 == 0]

print (f'{Any_Par}')
print (f'{Lista_Par}')
print (f'{list(Anonima3)}')

def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda(*args) - 42
        
    return Tercera

@Primera
def Operacion(Numero:int) -> int:
    Local = Numero
    return PEPE1.GLOBAL + Local

print (f'El resultado de la operacion es {Operacion(12)}')

def Externa(Nombre):
    def Interna(Apellido:str) -> str: #type: ignore
        print (f'Mi nombre es {Nombre} es {Apellido}')
        
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
print (f'{Variable_Closure(27)}')
print (f'{Variable_Closure(33)}')

def Crear_Closure_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y
    
    return Closure_Multiplicador

Mult1 = Crear_Closure_Multiplicador(2)
Mult2 = Crear_Closure_Multiplicador(3)

print (f'El multiplicador es {Mult1(10)}')
print (f'El multiplicador es {Mult2(10)}')

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    Lista_Impar = [num for num in Lista if num % 2 != 0]
    Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
    
    if (Any_Impar == True):
        print (f'Los elementos impares de la lista son {Lista_Impar} o tambien podrian ser {list(Anonima4)}')
    else:
        print (f'Error, no hay elementos impares')
        
Filtrador(PEPE1.Lista_Numeros)

def Primera(Segunda):
    def Tercera():
        print (f'ANTES')
        Segunda()
        print (f'DESPUES')
        
    return Tercera

@Primera
def Saludar4():
    print (f'Hola Mundo')
    
Saludar4()

print (f'El resultado de la sumatoria es {PEPE1.Sumatoria3(4, 3)}')

PEPE1.Usuario2('Erick', 'Perez')

print (f'-' * 20)

from Module_Own import Pokemon2 as Poke2

Objeto22 = Poke2(PEPE1.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto23 = Poke2(PEPE1.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto22.Mostrar()

print (f'-' * 20)

print (f'Yo tengo {Objeto23.Cantidad} {Objeto23.Nombre}s')

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto24 = Poke_Kid2(PEPE1.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto24)
Objeto24.Mostrar()

print (f'-' * 20)

class Camara():
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada')
        
class Reproductor_Musica():
    def Reproducir_Musica(self):
        print (f'La musica fue reproducida')
        
class SmartPhone(Camara, Reproductor_Musica):
    def Encender_Smartphone(self):
        print (f'El smartphone fue encendido')
        
Objeto25 = SmartPhone()

Objeto25.Encender_Smartphone()
Objeto25.Reproducir_Musica()
Objeto25.Tomar_Fotografia()

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
        
Objeto26 = Perro2('Chester', 5, 2.8, 'Poodle', 'Hiper-Tension')

Veterinaria2.Mostrar(Objeto26)
Objeto26.Mostrar()

print (f'-' * 20)

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Color, Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Activo = Activo
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Activo: {self.Activo}')
        
Objeto27 = Gato2('Chester', 1.5, 1.8, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto27)
Objeto27.Mostrar()

print (f'-' * 20)

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto28 = Pajaro2('Polly', 31, 0.4, 'Cacatua', 'Si')

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
        
class Paladin2(Atacante2, Defensor2):
    def __init__(self, Damage, Weapon, Healing, Potion, Life, Name):
        Atacante2.__init__(self, Damage, Weapon)
        Defensor2.__init__(self,  Healing, Potion, Life)
        self.Name = Name
    
    def Mostrar(self):
        print (f'Name: {self.Name}')
        
Objeto29 = Paladin2(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto29.Mostrar()
Atacante2.Mostrar(Objeto29)
Defensor2.Mostrar(Objeto29)

print (f'-' * 20)

Hija_Padre = issubclass(Poke_Kid2, Poke2)

print (f'{Hija_Padre}')

Instancia1 = isinstance(Objeto29, Paladin2)
Instancia2 = isinstance(Objeto29, Atacante2)
Instancia3 = isinstance(Objeto29, Defensor2)

print (f'{Instancia1}')
print (f'{Instancia2}')
print (f'{Instancia3}')

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

class Persona2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
    
Objeto31 = Persona2('Jonathan Smith')

print (f'Hola mi nombre es {Objeto31}')

class Efectivo2():
    def Pagar(self):
        print (f'El pago se realizo en efectivo')
        
class Tarjeta2():
    def Pagar(self):
        print (f'El pago se realizo en tarjeta')
        
class Cripto2():
    def Pagar(self):
        print (f'El pago se realizo en cripto')
        
Objeto32 = Cripto2()
Objeto33 = Tarjeta2()
Objeto34 = Efectivo2()

Objeto32.Pagar()
Objeto33.Pagar()
Objeto34.Pagar()

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
        print (f'Su saldo actual es ${self.__Saldo}')
        
Objeto35 = Cuenta_Bancaria2(100)
Objeto35.Depositar(25)
Objeto35.Mostrar()

print (f'Tu saldo privado es de {Objeto35.Dinero}')

Objeto35.Dinero = '50,000,000'

Objeto35.Mostrar()
print (f'Tu saldo privado es de {Objeto35.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla2(Plantilla2):
    def Mostrar(self):
        print (f'Este es el metodo de la sub plantila')
        
    def General(self):
        print (f'Este es el metodo de la abstraccion')
        
Objeto36 = Sub_Plantilla2()

Objeto36.Mostrar()
Objeto36.General()

class Chocolate2():
    def Elegir(self):
        return f'Chocolate'
    
class Vainilla2():
    def Elegir(self):
        return f'Vainilla'
    
class Fresa2():
    def Elegir(self):
        return f'Fresa'
    
class Helado2:
    def __init__(self):
        self.Favorito = Chocolate1()
        
    def Comer(self):
        print (f'Hoy te vas a comer un helado de {self.Favorito.Elegir()}')
        
Objeto37 = Helado2()
Objeto37.Comer()

print (f'-' * 20)

class Helado3:
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Comer(self):
        print (f'Hoy te vas a comer un helado de {self.Favorito.Elegir()}')
        
Sample1 = Chocolate1()
Objeto37 = Helado3(Sample1)
Objeto37.Comer()

Sample2 = Vainilla2()
Objeto38 = Helado3(Sample2)
Objeto38.Comer()

Sample3 = Fresa2()
Objeto39 = Helado3(Sample3)
Objeto39.Comer()

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
variable5 = PEPE1.Division_Flotante
variable6, variable7 = True, Objeto23.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esta es una concatenacion simple {PEPE1.Diccionario_Poke["Poke3"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE1.Tupla_Poke[PEPE1.Tupla_Poke.index("Misty")]} tiene {Variable_Sumatoria} o {Sumatoria2(1, 2, 3, 4, 5)} o incluso {Objeto23.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Erick' in Lista_Uno)
print (f'Brooke' in PEPE1.Tupla_Poke)
print (f'Pikachu' in PEPE1.Set_Conjunto_Poke1)

print (f'-' * 20)

snake_case1, snake_case2, snake_case3 = PEPE1.Tupla_Poke

print (f'Esto es desempaquetado de variables con snake case {snake_case3}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto22.Cantidad, Sumatoria2(1, 2, 3, 4, 5))

print (f'El cociente es {Cociente} y el residuo es {Residuo}')

print (f'{PEPE1.Lista2[::2]}')
print (f'{PEPE1.Lista2[::3]}')
print (f'{PEPE1.Lista2[:2]}')
print (f'{PEPE1.Lista2[2:]}')
print (f'{PEPE1.Lista2[0:None]}')
print (f'{PEPE1.Lista2[:]}')
print (f'{PEPE1.Lista2[2:4]}')

print (f'{Lista_Uno[1]} eso que esta ahi es un {PEPE1.Lista2[PEPE1.Lista2.index("Koala")]}?')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, 200, 100)

print (f'{Lista_Cuatro}')

del Lista_Uno[1]

print (f'{Lista_Uno}')

Lista_Uno.remove('Coco Rayado')
Lista_Uno.pop(-2)
Lista_Uno.pop(-1)
Lista_Uno.pop(-1)

print (f'{Lista_Uno}')

Lista_Uno_Copia = Lista_Uno.copy()

Lista_Uno.clear()

print (f'{Lista_Uno}')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'{dir(PEPE1)}')

Tupla1 = ('Rojo', 'Azul', 'Azul', 'Azul', 'Azul', 'Azul')

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Blue'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Variable_Funcion_Tupla)}')

print (f'{Tupla1}')
print (f'{Tupla1[1:2]}')

Set_Conjunto1 = {'Electrico', Objeto22.Tipo, Objeto22.Tipo, Objeto22.Tipo, Objeto22.Tipo, Objeto22.Tipo}
Set_Conjunto1.add('Agua')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Electric', 'Water', 'Rock'})

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

'''SetA2.symmetric_difference_update(SetB2)

print (f'{SetA2}')'''

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})

Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, 'ChocoMenta'})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : Lista_Uno_Copia[0],
    'Edad' : Objeto23.Cantidad,
    'Votante' : Variable_Funcion_Tupla[3]
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
    'Edad' : [37, 20 ,6],
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

Diccionario1_Copia = Diccionario1.copy()

print (f'{Diccionario1}')

del Diccionario1['Nombre']
Diccionario1.pop('Edad')

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')

print (f'-' * 20)

print (f'{Diccionario1_Copia}')

Diccionario1 = dict({1 : 'Karlita', 2 : 6, 3 : 'False'})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario2.get("Nombre")[2]} no puede votar ya que solo tiene {Diccionario1[2]} añitos') #type: ignore

Diccionario_Vacio1 = dict.fromkeys('ABC', 'Dragon')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = Objeto23.Tipo

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')

print (f'-' * 20)

Key2 = [f'Key_{i}' for i in range(len(Lista_Uno_Copia))]

print (f'{Key2}')

Diccionario4 = dict(zip(Key2, Lista_Uno_Copia))

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Key_2"]}')
print (f'{Diccionario4.get("Key_3")}')

print (f'-' * 20)

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

import pandas as pd
from datetime import datetime

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

print (f'-' * 20)

Set_Conjunto_Csv = set(Cargar_Csv3['product'])

print (f'{Set_Conjunto_Csv}')

Key3 = [f'Key{i}' for i in range(len(Set_Conjunto_Csv))]

print (f'{Key3}')

print (f'-' * 20)

Diccionario5 = dict(zip(Key3, Set_Conjunto_Csv))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key3"]}')
print (f'{Diccionario5.get("Key6")}')

print (f'-' * 20)

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la operacion es {PEPE1.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'{type(variable1)}')
print (f'{type(variable4)}')
print (f'{type(PEPE1.Division_Flotante)}')
print (f'{type(Objeto23.Catched)}')
print (f'{type(Lista_Uno_Copia)}')
print (f'{type(Variable_Funcion_Tupla)}')
print (f'{type(Set_Conjunto_Menu1)}')
print (f'{type(Set_Conjunto_Menu2)}')
print (f'{type(Diccionario1_Copia)}')
print (f'{type(Funcion_Diccionario)}')
print (f'{type(Array2)}')
print (f'{type(DataFrame2)}')
print (f'{type(Objeto12)}')

if Diccionario3['Ingresos'] > 500: #type: ignore
    if Diccionario3['Gastos'] < 200: #type: ignore
        print('Ingresos Altos, Gastos Bajos')
    elif Diccionario3['Gastos'] == 200:
        print('Ingresos Altos, Gastos Al Limite')
    elif Diccionario3['Gastos'] > 200: #type: ignore
        print('Ingresos Altos, Gastos Altos')
    else:
        print('Error de código')

elif Diccionario3['Ingresos'] == 500:
    if Diccionario3['Gastos'] < 200: #type: ignore
        print('Ingresos Mínimos, Gastos Bajos')
    elif Diccionario3['Gastos'] == 200:
        print('Ingresos Mínimos, Gastos Al Limite')
    elif Diccionario3['Gastos'] > 200: #type: ignore
        print('Ingresos Mínimos, Gastos Altos')
    else:
        print('Error de código')

elif Diccionario3['Ingresos'] < 500: #type: ignore
    if Diccionario3['Gastos'] < 200: #type: ignore
        print('Ingresos Bajos, Gastos Bajos')
    elif Diccionario3['Gastos'] == 200:
        print('Ingresos Bajos, Gastos Al Limite')
    elif Diccionario3['Gastos'] > 200: #type: ignore
        print('Ingresos Bajos, Gastos Altos')
    else:
        print('Error de código')

else:
    print('Error de código')
    
variable8 = 'Josue'
variable9 = 20

if (variable8 == 'Erick' and variable9 > 30):
    print (f'Ambas condiciones se cumplieron')
else:
    print (f'Error, al menos una condicion no se cumple')
    
if (variable8 == 'Erick' or variable9 > 30):
    print (f'Al menos una condicion se cumple')
else:
    print (f'Error, ninguna condicion se cumple')
    
Objeto40 = PEPE1.Entrenador(PEPE1.Tupla_Poke[0], 'Kanto', Objeto22.Nombre)
Objeto41 = PEPE1.Entrenador(PEPE1.Tupla_Poke[1], 'Paldea', Objeto23.Nombre)
Objeto42 = PEPE1.Entrenador(PEPE1.Tupla_Poke[2], 'Alolah', Objeto24.Nombre)

Objeto40.Desplegar()
print (f'-' * 20)
Objeto41.Desplegar()
print (f'-' * 20)
Objeto42.Desplegar()
print (f'-' * 20)

Negativo = -5

print (f'{int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE1.Lista_Numeros)
Lista_Iterable = [num for num in PEPE1.Lista_Numeros if num % 2 == 0]
Anonima5 = filter(lambda Num :  Num % 2 == 0, PEPE1.Lista_Numeros)

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
variable10_letra = variable10[0]

print (f'{variable10}')
print (f'{variable10.lower()}')
print (f'{variable10.upper()}')
print (f'{variable10.capitalize()}')

print (f'{variable10.lower().index("t")}')
print (f'{variable10.lower().find("b")}')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'La cantidad de letras {variable10_letra} en la cadena es de {variable10.lower().count(variable10_letra)}')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

print (f'-' * 20)

variable11 = 'esto es un texto cualquiera para ver si al final sirve o no'

Lista_variable11 = variable11.split(' ')

print (f'La cantidad de palabras digitadas es {len(Lista_variable11)}')

Contador = 0

while (Contador < len(Lista_variable11)):
    print (f'{Lista_variable11[Contador]}')
    Contador+= 1
    
print (f'-' * 20)

variable12 = '3'

if (variable12.isalpha()):
    print (f'Lo que ingresaste es un texto')
else:
    print (f'Error, lo que ingresaste no es un numero')

if (isinstance(variable12, (str))):
    print (f'Lo que ingresaste es un texto')
else:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

variable13 = 3.5

try:
    Numerito3 = float(variable13)
    if (Numerito3.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
if (isinstance(variable13, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, lo que ingresaste no es un numero decimal')
    
print (f'-' * 20)

variable14 = '30'

try:
    Numerito4 = float(variable14)
    if (Numerito4.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
if (isinstance(variable14, (int, float))):
    print (f'Lo que ingresaste es un numero entero o decimal')
else:
    print (f'Error, lo que ingresaste no es un numero')
    
if (variable14.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')
    
print (f'-' * 20)

variable15 = 'gatito123'

if (variable15.isalnum()):
    print (f'Esto es letras o numeros')
else:
    print (f'Error, esto no funciono')
    
print (f'-' * 20)

variable16 = '    e     '

if (variable16.isspace()):
    print (f'Esto son solo espacios')
else:
    print (f'Error, esto tiene mas que solo espacios')
    
print (f'-' * 20)

variable17 = 'texto'

if (variable17.lower().islower() == True):
    print (f'Esto es totalmente minuscula')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

if (variable17.upper().isupper() == True):
    print (f'Esto es totalmente mayuscula')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

print (f'{PEPE1.Tupla_Poke[2]} aparece en la posicion {PEPE1.Tupla_Poke.index("Misty")}')

'''Lista_Numeros2 = []

Contador = 0

while Contador < 3:
    while True:
        Numerito5 = input(f'Ingrese el numero {Contador + 1}: ')
        try:
            Numerito6 = float(Numerito5)
            if (Numerito6.is_integer()):
                print (f'El numero es entero')
                Lista_Numeros2.extend([Numerito6])
                break
            else:
                print (f'El numero es decimal')
                Lista_Numeros2.append(Numerito6)
                break
        except ValueError:
            print (f'Error, necesito que ingreses un numero')
    Contador+= 1
    
Promedio = sum(Lista_Numeros2) / len(Lista_Numeros2)

print (f'Gracias por agregar los numeros, tu promedio es de {round(Promedio, 2)}')'''

Contador = 0

while (Contador < len(PEPE1.Lista_Numeros)):
    print (f'{PEPE1.Lista_Numeros[Contador] * 100}')
    Contador+= 1
    
print (f'-' * 20)

Lista_Animales = list([])
Lista_Animales.append('Jirafa')
Lista_Animales.insert(1, f'{PEPE1.Lista2[2]}')
Lista_Animales.extend(['Cocodrilo', 'Avestruz'])

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Koala'):
        print (f'Este bichillo es de Australia')
        break
    else:
        Contador+= 1
        
print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Uno_Copia, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
print (f'-' * 20)

Lista_Numeros_Mult = [num * 100 for num in PEPE1.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1
    
print (f'-' * 20)

Menor = min(Lista_Numeros_Mult)
Mayor = max(Lista_Numeros_Mult)

print (f'El numero menor de la lista es {Menor} y el mayor es {Mayor}')

Redondeado = round(14.458795, 2)

print (f'El numero redondeado es {Redondeado}')

print (f'{bool("")}')
print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool(False)}')
print (f'{bool(not True)}')

Todo_All = all([Lista_Uno_Copia, "", Set_Conjunto_Array2, Diccionario3])

print (f'{Todo_All}')

Sumatoria3 = sum(Lista_Numeros_Mult)

print (f'El resultado de la sumatoria es {Sumatoria3}')

Uno = int('500')
Dos = str(500)
Tres = float(500)
Cuatro = list(Set_Conjunto1)
Cinco = tuple(Set_Conjunto_Menu1)
Seis = set(Lista_Numeros_Mult)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')
print (f'{type(Cuatro)}')
print (f'{type(Cinco)}')
print (f'{type(Seis)}')

print (f'-'.join(PEPE1.Set_Conjunto_Poke1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

variable_PEPE3 = PEPE3

import pandas as pd
import requests
import io

Ruta_Html2 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html2, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Leer_Html)

print (f'{Cargar_Html2[2].head()}')

print (f'-' * 20)

import re

Texto15 = 'ericksuper80@hotmail.com'

Pattern17 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(com|org|net)$'

Buscar26 = bool(re.fullmatch(Pattern17, Texto15))

if (Buscar26 == True):
    print (f'El formato del correo es correcto')
else:
    print (f'Error, formato de correo incorrecto')
    
'''def Floating1(Elemento):
    try:
        Numerito5 = float(Elemento)
        if (Numerito5.is_integer()):
            Resultado = Sumatoria2(1, 2, 3, 4, 5) * Variable_Sumatoria + Numerito5
            print (f'El resultado de la operacion es {Resultado}')
        else:
            Resultado = Sumatoria2(1, 2, 3, 4, 5) * Variable_Sumatoria + Numerito5
            print (f'El resultado de la operacion es {round(Resultado, 2)}')
    except ValueError:
        print (f'Error, necesito que ingrese un numero')
        
Floating1(PEPE1.Flotante1)

Resultado2 = eval(PEPE1.Flotante2)

print (f'El resultado de la operacion es {Resultado2}')

def Floating3(Elemento):
    if (Elemento.isalpha()):
        print (f'Lo ingresado es texto')
    elif (Elemento.isspace()):
        print (f'Lo ingresado son solo espacios')
    else:
        print (f'Error, lo ingresado no es texto')

Floating3(PEPE1.Flotante3)

def Floating4(Elemento):
    Cadena = Elemento.split(' ')
    for elemento in Cadena:
        print (f'{elemento}')
        
    print (f'La cantidad de palabras digitadas es de {len(Cadena)}')
    
Floating4(PEPE1.Flotante4)'''

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el alumno {elemento}: ')
        Lista.append(Alumno)
        
    return Lista

try:
    with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nLa lista de estudiantes es {Colegio(Lista_Alumnos)}')
        Docu.close()
except FileNotFoundError:
    print (f'Error el archivo no existe')
    raise

with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()  '''  
    
'''Lista_Alumnos = []

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del estudiante {elemento}: '))
        
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda Num : Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'De la lista el estudiante menor es {Menore} con una edad de {Lista[0][1]} años')
    print (f'De la lista el estudiante mayor es {Mayore} con una edad de {Lista[-1][1]} años')
    
Colegio(Lista_Alumnos)'''

'''def Exception_Finale():
    while True:
        Numerito7 = input(f'Ingrese un numero entero: ')
        try:
            Numerito8 = float(Numerito7)
            if (Numerito8.is_integer()):
                print (f'Lo ingresado fue un numero entero')
                break
        except ValueError:
            print (f'Error, necesito que ingreses un numero entero')
        
Exception_Finale()'''

import pandas as pd
from datetime import datetime

Ruta_Csv4 = 'C:\\Repo\\Store.csv'

Cargar_Csv4 = pd.read_csv(Ruta_Csv4)

print (f'{Cargar_Csv4}')

print (f'-' * 20)

Fecha4 = '2026-04-01'

try:
    Fech4 = datetime.strptime(Fecha4, '%Y-%m-%d').date()
    Fech4_Formateada = pd.to_datetime(Fech4)
    Cargar_Csv4['date'] = pd.to_datetime(Cargar_Csv4['date'])
except ValueError:
    print (f'Formato de fecha incorrecto')
    exit()
    
Cargar_Csv4['TOTALITO'] = Cargar_Csv4['quantity'] * Cargar_Csv4['price']
    
Encontrado4 = Cargar_Csv4[Cargar_Csv4['date'].dt.date == Fech4_Formateada.date()]

if (Encontrado4.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! Encontramos ventas')
    Grupo6 = Encontrado4.groupby('product')['quantity'].sum()
    Grupo6_Min = Grupo6.idxmin()
    Grupo6_Max = Grupo6.idxmax()
    Grupo6_Min_Cant = Grupo6.min()
    Grupo6_Max_Cant = Grupo6.max()
    
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo6_Min} vendio un total de {Grupo6_Min_Cant} unidades')
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo6_Max} vendio un total de {Grupo6_Max_Cant} unidades')
    
    print (f'El total de clientes que nos compraron hoy fue de {Grupo6.count()}')
    print (f'El total de productos vendidos en esta fecha fue de {Grupo6.sum()}')
    
    Grupo7 = Encontrado4.groupby('product')['TOTALITO'].sum()
    
    print (f'El total de dinero vendido en esta fecha fue de ${Grupo7.sum()}')
    print (f'La media del dinero vendido fue de {Grupo7.mean()}')
    
    Promedio = Grupo7.sum() / Grupo7.count()
    
    print (f'El promedio vendido el dia de hoy fue de {round(Promedio, 2)}')