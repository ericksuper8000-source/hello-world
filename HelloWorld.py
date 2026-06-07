var1 = '35.3'

if (var1.isnumeric()):
    print (f'El numero es entero')
else:
    print (f'Error, no es un numero entero')
    
if (isinstance(var1, (int))):
    print (f'El numero es entero')
else:
    print (f'Error, no es un numero entero')
    
try:
    Totito1 = float(var1)
    if (Totito1.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
var2 = 3.5

if (isinstance(var2, (float))):
    print (f'Lo ingresado es decimal')
else:
    print (f'Error, lo ingresado no es decimal')
    
try:
    Totito2 = float(var2)
    if (Totito2.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es numero')
    
var3 = 'Hola'

if (isinstance(var3, (int, float))):
    print (f'Lo ingresado es un numero')
else:
    print (f'Error, lo ingresado no es un numero')
    
var4 = 'hola'

if (isinstance(var4, (str))):
    print (f'Lo ingresado es texto')
else:
    print (f'Error, lo ingresado no es un texto')
    
if (var4.isalpha()):
    print (f'Lo ingresado es texto')
else:
    print (f'Error, lo ingresado no es un texto')
    
var5 = ' '

if (var5.isalnum()):
    print (f'Lo ingresado es texto o numero')
else:
    print (f'Error, lo ingresado no es ni texto ni numero')
    
if (var5.isspace()):
    print (f'Lo ingresado es un espacio')
else:
    print (f'Error, lo ingresado tiene mas que solo espacios')
    
var6 = 'texTo'

if (var6.lower().islower()):
    print (f'Lo ingresado es un texto en minuscula')
else:
    print (f'Error, no es minuscula')
    
if (var6.upper().isupper()):
    print (f'Lo ingresado es un texto en mayuscula')
else:
    print (f'Error, no es mayuscula')
    
import re
    
Texto1 = "   Hola!!!   mundo@@   123   "

print (f'{Texto1}')

Texto1_Version1 = Texto1.lower()

print (f'{Texto1_Version1}')

Texto1_Version2 = Texto1_Version1.strip()

print (f'{Texto1_Version2}')

Texto1_Version3 = ' '.join(Texto1_Version2.split())

print (f'{Texto1_Version3}')

Texto1_Version4 = re.sub(r'\!|\@|\d+', '', Texto1_Version3)

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
    Fech1_Formateado = pd.to_datetime(Fech1)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Error, formato de fecha incorrecta')
    exit()
    
Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrado1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateado.date()]

if (Encontrado1.empty):
    print (f'No se encontraron ventas en esta fecha')
else:
    print (f'Genial! Encontramos ventas')
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'En la fecha {Fech1_Formateado} el producto {Grupo1_Min} vendio un total de {Grupo1_Min_Cant} unidades')
    print (f'En la fecha {Fech1_Formateado} el producto {Grupo1_Max} vendio un total de {Grupo1_Max_Cant} unidades')
    
    print (f'En esta fecha nos compraron un total de {Grupo1.count()} clientes')
    print (f'La cantidad de productos vendidos en esta fecha fue {Grupo1.sum()}')
    
    Grupo2 = Encontrado1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue ${Grupo2.sum()}')
    print (f'La media de dinero vendido en esta fecha fue de ${Grupo2.mean()}')
    
    Promedio1 = Grupo2.sum() / Grupo1.count()
    
    print (f'El promedio de ventas en esta fecha fue de ${Promedio1}')
    
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

'''SetA1.symmetric_difference_update(SetB1)
print (f'{SetA1}')'''

class Bulbasaur1():
    def Elegir(self):
        return f'Bulbasaur'
    
class Treekoo1():
    def Elegir(self):
        return f'Treekoo'
    
class Chikorita1():
    def Elegir(self):
        return f'Chikorita'
    
class Battle1:
    def __init__(self):
        self.Favorito = Bulbasaur1()
        
    def Batallar(self):
        print (f'Has elegido a {self.Favorito.Elegir()}!!!')
        
Objeto1 = Battle1()
Objeto1.Batallar()

print (f'-' * 20)

class Battle2:
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'Has elegido a {self.Favorito.Elegir()}')
        
Elegido1 = Bulbasaur1()
Objeto2 = Battle2(Elegido1)
Objeto2.Batallar()

Elegido2 = Treekoo1()
Objeto3 = Battle2(Elegido2)
Objeto3.Batallar()

Elegido3 = Chikorita1()
Objeto4 = Battle2(Elegido3)
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

# Version1

Pattern2 = r'[^a-zA-Z0-9\s]+'

Buscar2 = re.sub(Pattern2, '', Texto3)

print (f'{Buscar2}')

print (f'-' * 20)

# Version2

Pattern3 = r'\!|\?|\.{2,}'

Buscar3 = re.sub(Pattern3, '', Texto3)

print (f'{Buscar3}')

Pattern4 = r'\d{4}\-[0-9]{3,4}'

Buscar4 = re.sub(Pattern4, '', Buscar3)

print (f'{Buscar4}')

print (f'-' * 20)

import re

# Version3

Pattern5 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.(?:com|net|org)'

Correos1 = re.findall(Pattern5, Texto3)

Texto3_temp = Texto3

print (f'{Correos1}')

for i, email in enumerate(Correos1, start=1):
    Texto3_temp = Texto3_temp.replace(email, f'SAMPLE{i}')
    
print (f'{Texto3_temp}')

Pattern6 = r'\!|\?|\.{2,}'

Texto3_temp2 = re.sub(Pattern6, '', Texto3_temp)

print (f'{Texto3_temp2}')

Texto3_temp3 = re.sub(r'\d{4}\-[0-9]{3,4}', '', Texto3_temp2)

print (f'{Texto3_temp3}')

for i, email in enumerate(Correos1, start=1):
    Texto3_temp3 = Texto3_temp3.replace(f'SAMPLE{i}', email)
    
print (f'{Texto3_temp3}')

print (f'-' * 20)

import re

Texto4 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Texto4_temp1 = Texto4

Pattern7 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|net|org)'

Correos2 = re.findall(Pattern7, Texto4)

print (f'{Correos2}')

for i, email in enumerate(Correos2, start=1):
    Texto4_temp1 = Texto4_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto4_temp1}')

Texto4_temp2 = re.sub(r'\!|\?', '', Texto4_temp1)

print (f'{Texto4_temp2}')

for i, email in enumerate(Correos2, start=1):
    Texto4_temp2 = Texto4_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto4_temp2}')

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

'''Lista_Promedio1 = list([])

Contador = 0

while (Contador < 3):
    while True:
        Numerito = input(f'Ingrese el numero {Contador + 1}: ')
        try:
            Numerito2 = float(Numerito)
            if (Numerito2.is_integer()):
                print (f'Lo ingresado es un numero entero')
                Lista_Promedio1.append(Numerito2)
                break
            else:
                print (f'Lo ingresado es un numero decimal')
                Lista_Promedio1.extend([Numerito2])
                break
        except ValueError:
            print (f'Error, lo ingresado no es un numero')
    Contador+= 1
    
Promedio2 = sum(Lista_Promedio1) / len(Lista_Promedio1)

print (f'El promedio de las notas ingresadas es {round(Promedio2, 2)}')'''

class Persona1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
    
Objeto5 = Persona1('Erick Perez Gutierrez')

print (f'Hola, mi nombre es {Objeto5}')

from Module_Own import Pokemon1 as Poke1

Objeto6 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto7 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

print (f'-' * 20)

print (f'Actualmente yo tengo {Objeto7.Cantidad} {Objeto7.Nombre}s en mi pokedex')

Objeto6.Mostrar()

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
        
Objeto9 = Perro1('Chester', 5, 2.9, 'Poodle', 'Asma')

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
        
Objeto11 = Pajaro1('Polly', 31, 0.4, 'Lora Verde', 'Si')

Veterinaria1.Mostrar(Objeto11)
Objeto11.Mostrar()

print (f'-' * 20)

class Camara1:
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada')
        
class Reproductor_Musica1:
    def Reproducir_Musica(self):
        print (f'La musica fue reproducida')
        
class Smartphone1(Camara1, Reproductor_Musica1):
    def Encender_Smartphone(self):
        print (f'El smartphone ha sido encendido')
        
Objeto12 = Smartphone1()

Objeto12.Encender_Smartphone()
Objeto12.Reproducir_Musica()
Objeto12.Tomar_Fotografia()

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
        
Objeto13 = Paladin1(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto13.Mostrar()
Atacante1.Mostrar(Objeto13)
Defensor1.Mostrar(Objeto13)

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
        
Objeto14 = D1()

A1.Mostrar(Objeto14)
B1.Mostrar(Objeto14)
C1.Mostrar(Objeto14)
Objeto14.Mostrar()
E1.Mostrar(Objeto14)

print (f'-' * 20)

class Efectivo1():
    def Pagar(self):
        print (f'El pago se realizo en efectivo')
        
class Tarjeta1():
    def Pagar(self):
        print (f'El pago se realizo en tarjeta')
        
class Cripto1():
    def Pagar(self):
        print (f'El pago se realizo en cripto')
        
Objeto15 = Cripto1()
Objeto16 = Tarjeta1()
Objeto17 = Efectivo1()

Objeto15.Pagar()
Objeto16.Pagar()
Objeto17.Pagar()

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
        print (f'Tu saldo a la fecha es de ${self.__Saldo}')
        
Objeto18 = Cuenta_Bancaria1(100)
Objeto18.Depositar(25)
Objeto18.Mostrar()

print (f'Tu saldo privado es de {Objeto18.Dinero}')

Objeto18.Dinero = '50,000,000'

Objeto18.Mostrar()
print (f'Tu saldo privado es de {Objeto18.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def General(self):
        pass
    
class Sub_Plantilla(Plantilla):
    def Mostrar(self):
        print (f'Este es un metodo cualquiera')
        
    def General(self):
        print (f'Este metodo es obligatorio para la abstraccion')
        
Objeto19 = Sub_Plantilla()

Objeto19.Mostrar()
Objeto19.General()

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
    
class Pastelito1():
    def __init__(self):
        self.Favorito = Chocolate1()
        
    def Hornear(self):
        print (f'Te parece si hago un pastel de {self.Favorito.Elegir()}?')
        
Objeto20 = Pastelito1()
Objeto20.Hornear()

print (f'-' * 20)

class Pastelito2:
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Te parece si hago un pastel de {self.Favorito.Elegir()}')
        
Elegido4 = Chocolate1()
Objeto21 = Pastelito2(Elegido4)
Objeto21.Hornear()

Elegido5 = Vainilla1()
Objeto22 = Pastelito2(Elegido5)
Objeto22.Hornear()

Elegido6 = Fresa1()
Objeto23 = Pastelito2(Elegido6)
Objeto23.Hornear()

print (f'-' * 20)

import re

Texto5 = 'esto es ! un hola 15 texto cualquiera hala 981 @ para probar si 3 funciona hela - o no'

Buscar5 = re.search(r'para', Texto5)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\d+', Texto5)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\W', Texto5)

print (f'{Buscar7}')

Buscar8 = re.findall(r'\w', Texto5)

print (f'{Buscar8}')

Buscar9 = re.findall(r'\s', Texto5)

print (f'{Buscar9}')

Buscar10 = re.findall(r'\S', Texto5)

print (f'{Buscar10}')

Buscar11 = re.findall(r'^esto', Texto5)

print (f'{Buscar11}')

Buscar12 = re.findall(r'o$', Texto5)

print (f'{Buscar12}')

Buscar13 = re.fullmatch(r'esto es \! un 15 texto cualquiera 91 \@ para probxear si 3 funciona \- o no', Texto5)

print (f'{Buscar13}')

Buscar14 = re.findall(r'h.la', Texto5)

print (f'{Buscar14}')

Pattern8 = r'\d{3}\s\W'

Buscar15 = re.findall(Pattern8, Texto5)

print (f'{Buscar15}')

Buscar16 = re.findall(r'[ai]+', Texto5)

print (f'{Buscar16}')

Buscar17 = re.findall(r'(ex)', Texto5)

print (f'{Buscar17}')

import re

Texto6 = 'ericksuper80@hotmail.com'

Pattern9 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar18 = bool(re.fullmatch(Pattern9, Texto6))

if (Buscar18):
    print (f'El correo electronico tiene el formato correcto')
else:
    print (f'Error, el correo no tiene el formato correcto')
    
import re

Texto7 = '31'

Pattern10 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar19 = bool(re.match(Pattern10, Texto7))

if (Buscar19 == True):
    print (f'El numero se encuentra entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
import re
    
Texto8 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern11 = r'\d{2}\/[0-9]{2}\/\d{3,}'

Reemplazo1 = 'XX/XX/XXXX'

Busca20 = re.sub(Pattern11, Reemplazo1, Texto8)

print (f'{Busca20}')

Pattern12 = r'\+\d{1}\-[0-9]{3}\-\d{2,3}\-[0-9]{3,}'

Reemplazo2 = '+*-***-***-****'

Busca21 = re.sub(Pattern12, Reemplazo2, Busca20)

print (f'{Busca21}')

print (f'-' * 20)

import re

Texto9 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

# Version1

Pattern13 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Busca22 = re.findall(Pattern13, Texto9)

print (f'{Busca22}')

for elemento in enumerate(Busca22):
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

# Version2

import re

Pattern14 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos3 = re.findall(Pattern14, Texto9)

print (f'{Correos3}')

Texto9_temp1 = Texto9

for i, email in enumerate(Correos3, start=1):
    Texto9_temp1 = Texto9_temp1.replace(email, f'TEMPLATE{i}')
    
print (f'{Texto9_temp1}')

print (f'-' * 20)

import re

# Version1

Texto10 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Busca23 = re.sub(r'[^a-zA-Z0-9\s]+', '', Texto10)

print (f'{Busca23}')

Busca24 = re.sub(r'\d{5,}', '', Busca23)

print (f'{Busca24}')

print (f'-' * 20)

import re

# Version2

Texto11 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Busca25 = re.sub(r'\!|\?|\.{2,}|\d{4}\-[0-9]{4}', '', Texto11)

print (f'{Busca25}')

print (f'-' * 20)

var7 = '3.5'

def Exception1(Numero):
    try:
        var8 = float(Numero)
        if (var8.is_integer()):
            print (f'El numero es entero')
        else:
            print (f'El numero es decimal')
    except ValueError:
        print (f'Error, lo ingresado no es un numero')

Exception1(var7)

def Exception2(Numero):
    if (isinstance(Numero, (int))):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado no es un numero entero')
        
    if (Numero.isnumeric()): #type: ignore
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado no es un numero entero')
        
    try:
        var8 = float(Numero)
        if (var8.is_integer()):
            print (f'Lo ingresado es un numero entero')
        else:
            print (f'Lo ingresado es un numero decimal')
    except ValueError:
        print (f'Error, lo ingresado no es un numero')

Exception2('hola')

import re

Texto12 = "   Hola!!!   mundo@@   123   "

print (f'{Texto12}')

Texto12_Version1 = Texto12.strip()

print (f'{Texto12_Version1}')

Texto12_Version2 = ' '.join(Texto12_Version1.split())

print (f'{Texto12_Version2}')

Texto12_Version3 = re.sub(r'\!|\@|\d+', '', Texto12_Version2)

print (f'{Texto12_Version3}')

print (f'-' * 20)

def Exception3(Numero):
    try:
        var8 = float(Numero)
        if (var8.is_integer()):
            print (f'Lo ingresado es un numero entero')
        else:
            print (f'Lo ingresado es un numero decimal')
    except ValueError:
        print (f'Error, lo ingresado no es un numero')

Exception3('hola')

def Exception4(Num1, Num2):
    try:
        var8 = float(Num1)
        var9 = float(Num2)
        if (var8.is_integer() and var9.is_integer()):
            Resultado1 = var8 + var9
            print (f'El resultado de la operacion es {Resultado1}')
        else:
            Resultado1 = var8 + var9
            print (f'El resultado de la operacion es {round(Resultado1, 2)}')
    except TypeError, ValueError:
        print (f'Error, ambos elementos deben ser numeros')

Exception4('Hola', '12.8')

def Exception5(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except TypeError, ValueError, ZeroDivisionError:
        print (f'Error, ambos elementos deben ser numeros, pero el divisor no puede ser cero')

Exception5(14, 0)

Lista_Exception6 = list([])
Lista_Exception6.append('Erick')
Lista_Exception6.insert(1, 'Josue')
Lista_Exception6.extend(['Karlita'])

def Exception6(Indice):
    try:
        print (f'El elemento en la posicion {Indice} es {Lista_Exception6[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception6(3)

Diccionario_Exception7 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception7(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception7[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception7('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Durazno')
        Docu.close()
except FileNotFoundError:
    print (f'El archivo elegido no fue encontrado')
    
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
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Set_Conjunto_Poke1)])
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
print (f'-' * 20)
    
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

print (f'El menor de las personas en el dataframe es {Data_Frame_Concatenate_Age.min()}')
print (f'El mayor de las personas en el dataframe es {Data_Frame_Concatenate_Age.max()}')

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()

print (f'La persona menor de todos es {Grupo3.idxmin()} con una edad de {Grupo3.min()} años')
print (f'La persona menor de todos es {Grupo3.idxmax()} con una edad de {Grupo3.max()} años')

print (f'La cantidad de personas en el dataframe es {Grupo3.count()}')

print (f'Si sumo todas las edades me da el numero {Grupo3.sum()}')
print (f'La media de todas las edades es {round(Grupo3.mean(), 2)}')

Promedio2 = Grupo3.sum() / Grupo3.count()

print (f'El promedio es {round(Promedio2, 2)}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    El1 = elemento['Nombre']
    El2 = elemento['Edad']
    
    print (f'Mi nombre es {El1} y tengo {El2} años')
    
'''print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)
plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)
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

print (f'El numero de Filas es {Filas}')
print (f'El numero de Columnas es {Columnas}')

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
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='familiares')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols='E:K')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols='E:K', index_col='familiares', nrows=1)

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

Cargar_Excel3_Sorted_Descending['TOTALITO'] = Cargar_Excel3_Sorted_Descending['cinco'] * 500

Grupo4 = Cargar_Excel3_Sorted_Descending.groupby('tres')['cinco'].sum()

print (f'El mayor de los compas es {Grupo4.idxmax()} con una edad de {Grupo4.max()} años')
print (f'El menor de los compas es {Grupo4.idxmin()} con una edad de {Grupo4.min()} años')

print (f'El total de personas en la lista es {Grupo4.count()}')
print (f'Si sumo todas las edades me da como resultado {Grupo4.sum()} años')

Grupo5 = Cargar_Excel3_Sorted_Descending.groupby('tres')['TOTALITO'].sum()

print (f'Hagamos una sumatoria de las multiplicaciones {Grupo5.sum()}')
print (f'El promedio de este numero es {round(Grupo5.sum() / Grupo5.count(), 2)}')
print (f'El promeido tambien es {Grupo5.mean()}')

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

Grupo6 = Cargar_Csv2.groupby('Nombre')['Edad'].sum()

print (f'El menor es {Grupo6.idxmin()} -- {Grupo6.min()} años')
print (f'El mayor es {Grupo6.idxmax()} -- {Grupo6.max()} años')

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

print (f'{Array0[0][1]}')
print (f'{Array0[1][:2]}')
print (f'{Array0[1][2:]}')
print (f'{Array0[2][::2]}')
print (f'{Array0[1][::3]}')
print (f'{Array0[0][2:3]}')
print (f'{Array0[2][0:None]}')
print (f'{Array0[2][:]}')

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
print (f'{Array2[0, ::3]}')
print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[:, 1]}')
print (f'{Array2[1, 2:3]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[0, :]}')
print (f'{Array2[Array2 >= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {Array2_Sorted_Mean}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[1, 0:None])
Sumita4 = np.sum(Array2_Sorted[1, :])

print (f'El resultado de la sumatoria es {Sumita1}')
print (f'El resultado de la sumatoria es {Sumita2}')
print (f'El resultado de la sumatoria es {Sumita3}')
print (f'El resultado de la sumatoria es {Sumita4}')

print (f'-' * 20)

Array3 = np.array([[['e', 'o', 'j'], ['f', 'x', 'k']],       [['l', 'u', 'n'], ['p', 'a', 'b']]])

print (f'{Array3}')
print (f'{Array3.ndim}')
print (f'{Array3.shape}')
print (f'{Array3.size}')
print (f'{Array3.dtype}')
print (f'{Array3[1, 0, 2]}')

print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 1, ::3]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[0, :, 0]}')
print (f'{Array3[1, 1, 2:3]}')
print (f'{Array3[0, 0, 0:None]}')
print (f'{Array3[0, 0, :]}')
print (f'{Array3[Array3 == "a"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],           [[[6, 5, 4], [9, 8, 7]], [[4, 6, 7], [2, 5, 8]]]])

print (f'{Array4}')
print (f'{Array4.ndim}')
print (f'{Array4.shape}')
print (f'{Array4.size}')
print (f'{Array4.dtype}')
print (f'{Array4[1, 0, 1, 1]}')

print (f'-' * 20)

print (f'{Array4[0, 1, 0, :2]}')
print (f'{Array4[0, 1, 0, 2:]}')
print (f'{Array4[0, 0, ::2]}')
print (f'{Array4[0, 0, ::3]}')
print (f'{Array4[1, 0, :, 0]}')
print (f'{Array4[0, 0, 2:3]}')
print (f'{Array4[1, 0, 0:None]}')
print (f'{Array4[1, 0, :]}')
print (f'{Array4[Array4 >= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[1, 1, 0:None])
Sumita8 = np.sum(Array4_Sorted[1, 1, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'-' * 20)

Array_Num1 = np.arange(start=0, stop=11, step=1) #type: ignore

print (f'{Array_Num1}')

Array_Menor = np.min(Array_Num1)
Array_Mayor = np.max(Array_Num1)

print (f'El numero menor es {Array_Menor} y el numero mayor es {Array_Mayor}')

print (f'-' * 20)

Array_Num2 = np.arange(start=0, stop=25, step=1) #type: ignore

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

print (f'-' * 20)

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
print (f'{Array_Ones[0, 2]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke2"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 0]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value=f'Fuecoco')

print (f'{Array_Gen2}')

for elemento in Array_Gen2:
    print (f'{elemento}')

print (f'-' * 20)

Lista_Array1 = []

for indice, elemento in enumerate(Array_Gen2, start=1):
    Lista_Array1.extend([str(elemento)])
    
print (f'{Array_Gen2}')
print (f'{Lista_Array1}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[0, 1, 1, 2])

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

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array['Nombre'][1])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'-' * 20)

print (f'{Array_Gen6[3]}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=6, step=1) #type: ignore
Array_Num2 = np.arange(start=2, stop=11, step=2) #type: ignore
Array_Num3 = np.arange(start=3, stop=31, step=3) #type: ignore
Array_Num4 = np.arange(start=10, stop=21, step=2) #type: ignore
Array_Num5 = np.arange(10) #type: ignore

print (f'{Array_Num1}')
print (f'{Array_Num2}')
print (f'{Array_Num3}')
print (f'{Array_Num4}')
print (f'{Array_Num5}')

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
print (f'{Array_Random2[1, 1]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

print (f'-' * 20)

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Sum = Arr1 + Arr2
Rest = Arr1 - Arr2
Mult = Arr1 * Arr2
Div = Arr1 / Arr2

Array_Random2_Cien = Array_Random2 + 100

print (f'El resultado de la operacion es {Sum}')
print (f'El resultado de la operacion es {Rest}')
print (f'El resultado de la operacion es {Mult}')
print (f'El resultado de la operacion es {Div}')
print (f'El resultado de la operacion es {Array_Random2_Cien}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(20))

print (f'{Array_Random3}')

print (f'-' * 20)

Array_Random3_Reshape = np.reshape(Array_Random3, shape=(4, 5))

print (f'{Array_Random3_Reshape}')

Array_Random3_Reshape_Ravel = np.ravel(Array_Random3_Reshape)

print (f'{Array_Random3_Reshape_Ravel}')

print (f'-' * 20)

Lista_Array2 = [1, 2, 3]
Lista_Array2.append(4)
Lista_Array2.insert(2, 5)
Lista_Array2.extend([6])

Array5 = np.array([Lista_Array2])

print (f'{Array5}')

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

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'-' * 20)

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'-' * 20)

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-' * 20)

Array_Random4 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random4}')

Array_Random4_Sorted = np.sort(Array_Random4)
Array_Random4_Sorted_Mean = np.mean(Array_Random4_Sorted)
Array_Random4_Sorted_Sum = np.sum(Array_Random4_Sorted)

print (f'Acomodado: {Array_Random4_Sorted}')
print (f'Media: {round(Array_Random4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random4_Sorted_Sum}')

Sumita9 = np.sum(Array_Random4_Sorted, axis=0)
Sumita10 = np.sum(Array_Random4_Sorted, axis=1)
Sumita11 = np.sum(Array_Random4_Sorted[0, 1, 0:None])
Sumita12 = np.sum(Array_Random4_Sorted[0, 1, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

Array_Random4_Column_Min = np.min(Array_Random4, axis=0)
Array_Random4_Column_Max = np.min(Array_Random4, axis=0)
Array_Random4_Row_Min = np.min(Array_Random4, axis=1)
Array_Random4_Row_Max = np.min(Array_Random4, axis=1)

print (f'Los menores de las columnas son {Array_Random4_Column_Min}')
print (f'Los mayores de las columnas son {Array_Random4_Column_Max}')
print (f'Los menores de las filas son {Array_Random4_Row_Min}')
print (f'Los mayores de las filas son {Array_Random4_Row_Max}')

print (f'-' * 20)

Lista_Sorteo = []
Lista_Sorteo.append('Erick')
Lista_Sorteo.insert(1, 'Josue')
Lista_Sorteo.extend(['Karlita', 'Carmelo', 'Susanita', 'Roxana'])

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
    for elemento in range(0, 5):
        if (elemento % 2 == 0):
            yield f'El numero es par'
        else:
            yield f'El numero es impar'

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
    for elemento in range(5):
        if (elemento == 0):
            yield f'The number is zero'
        elif (elemento == 1):
            yield f'The number is one'
        elif (elemento == 2):
            yield f'The number is two'
        elif (elemento == 3):
            yield f'The number is three'
        elif (elemento == 4):
            yield f'The number is four'
        else:
            yield f'Error, el numero no existe'

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

Lista_Funcion = [1, 2, 3, 4, 5]

def Calculo(Lista):
    Lista_Menor = min(Lista)
    Lista_Mayor = max(Lista)
    
    Lista_Resultado = [Lista_Menor, Lista_Mayor]
    return Lista_Resultado

print (f'El menor y el mayor de la lista son {Calculo(Lista_Funcion)}')

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int) ->int:
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
    def Usuario_Interno(Sexo:str) -> str:
        Genero = Sexo.lower()
        if (Genero == 'masculino'):
            return True #type: ignore
        else:
            return False #type: ignore
        
    return Usuario_Interno('MASCULINO')

Variable_Usuario = Usuario_Externo()

if (Variable_Usuario == True):
    print (f'YOU ARE A MAN')
else:
    print (f'YOU ARE A WOMAN')
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nTu contrasena temporal es {PEPE.Contrasena(22)}')
        Docu.close()
except FileNotFoundError:
    print (f'El archivo elegido no existe')
    
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
        
    for elemento in kwargs.keys():
        print (f'{elemento}')
        
    print (f'-' * 20)
        
    for elemento in kwargs:
        print (f'{kwargs[elemento]}')
        
    print (f'-' * 20)
        
Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Objeto7.Cantidad, Votante = Variable_Funcion_Tupla[3])

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos(Saludar_Dos(), 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10)}')

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

if (PEPE.Any_Pares == True):
    print (f'Los numeros pares de la lista son {list(Anonima3)} o incluso podrian ser {PEPE.Lista_Pares}')
else:
    print (f'Error, no hay numeros pares en la lista')
    
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
    def Interna(Apellido:str) -> str: #type: ignore
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
print (f'{Variable_Closure(37)}')

def Closure_Crear_Multiplicador(x):
    def Multiplicador(y):
        return x * y
    
    return Multiplicador

Variable_Multiplicador1 = Closure_Crear_Multiplicador(2)
Variable_Multiplicador2 = Closure_Crear_Multiplicador(3)

print (f'El mult1 es {Variable_Multiplicador1(10)}')
print (f'El mult2 es {Variable_Multiplicador2(10)}')

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    if (Any_Impar == True):
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impar = [num for num in Lista if num % 2 != 0]
        
        print (f'Los numeros impares de la lista son {list(Anonima4)} o incluso podrian ser {Lista_Impar}')
    else:
        print (f'Error, no hay numeros impares en la lista')
        
Filtrador(PEPE.Lista_Numeros)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'ZZZZZZ')
        Segunda()
        print (f'ZZZZZZ')
        
    return Tercera

@Primera
def Saludar4():
    print (f'Hola Mundo')
    
Saludar4()

def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda(*args) - 12
        
    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(7, 6)}')

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

Objeto24 = Poke2(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto25 = Poke2(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto24.Mostrar()

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto25 = Poke_Kid2(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

print (f'-' * 20)

Poke2.Mostrar(Objeto25)
Objeto25.Mostrar()

print (f'-' * 20)

class Camara2():
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada')
        
class Reproductor_Musica2:
    def Reproducir_Musica(self):
        print (f'La musica fue reproducida')
        
class Smartphone2(Camara2, Reproductor_Musica2):
    def Encender_Smartphone(self):
        print (f'El smartphone ha sido encendido')
        
Objeto26 = Smartphone2()

Objeto26.Encender_Smartphone()
Objeto26.Reproducir_Musica()
Objeto26.Tomar_Fotografia()

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
        
Objeto27 = Perro2('Chester', 5, 2.8, 'Poodle', 'Hipertension')

Veterinaria2.Mostrar(Objeto27)
Objeto27.Mostrar()

print (f'-' * 20)

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Color, Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Activo = Activo

    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Activo: {self.Activo}')
        
Objeto28 = Gato2('Messi', 1.5, 1.8, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto28)
Objeto28.Mostrar()

print (f'-' * 20)

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto29 = Pajaro2('Polly', 31, 0.4, 'Papagayo', 'Si')

Veterinaria2.Mostrar(Objeto29)
Objeto29.Mostrar()

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
        
Objeto30 = Paladin2(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto30.Mostrar()
Atacante2.Mostrar(Objeto30)
Defensor2.Mostrar(Objeto30)

print (f'-' * 20)

Clase_Hija1 = issubclass(Poke_Kid2, Poke2)

print (f'{Clase_Hija1}')

Instancia1 = isinstance(Objeto30, Paladin2)
Instancia2 = isinstance(Objeto30, Defensor2)
Instancia3 = isinstance(Objeto30, Atacante2)

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
        
Objeto31 = D2()

A2.Mostrar(Objeto31)
B2.Mostrar(Objeto31)
C2.Mostrar(Objeto31)
Objeto31.Mostrar()
E2.Mostrar(Objeto31)

print (f'-' * 20)

class Efectivo2:
    def Pagar(self):
        print (f'El pago se realizo en efectivo')
        
class Tarjeta2:
    def Pagar(self):
        print (f'El pago se realizo en tarjeta')
        
class Cripto2:
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
        print (f'Su saldo a la fecha es de ${self.__Saldo}')
        
Objeto35 = Cuenta_Bancaria2(100)
Objeto35.Depositar(25)
Objeto35.Mostrar()

print (f'Tu saldo privado que nadie mas deberia ver es de {Objeto35.Dinero}')

Objeto35.Dinero = '50,000,000'

Objeto35.Mostrar()

print (f'Tu saldo privado que nadie mas deberia ver es de {Objeto35.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla2(Plantilla2):
    def Mostrar(self):
        print (f'Este es un metodo regular en una clase')
        
    def General(self):
        print (f'Este es el metodo de la abstraccion que es obligatoria')
        
Objeto36 = Sub_Plantilla2()

Objeto36.Mostrar()
Objeto36.General()

print (f'-' * 20)

class Bulbasaur2():
    def Elegir(self):
        return f'Bulbasaur'
    
class Treekoo2():
    def Elegir(self):
        return f'Treekoo'
    
class Chikorita2():
    def Elegir(self):
        return f'Chikorita'
    
class Battle3:
    def __init__(self):
        self.Favorito = Bulbasaur2()
        
    def Batallar(self):
        print (f'{self.Favorito.Elegir()} yo te elijo!!!')
        
Objeto37 = Battle3()

Objeto37.Batallar()

print (f'-' * 20)

class Battle4():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'{self.Favorito.Elegir()} yo te elijo!!!')
        
Elegido7 = Bulbasaur2()
Objeto38 = Battle4(Elegido7)
Objeto38.Batallar()

Elegido8 = Treekoo2()
Objeto39 = Battle4(Elegido8)
Objeto39.Batallar()

Elegido9 = Chikorita2()
Objeto40 = Battle4(Elegido9)
Objeto40.Batallar()

print (f'-' * 20)

class Persona2:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
    
Objeto41 = Persona2('Erick Josue Perez Gutierrez')

print (f'Hola mi nombre es {Objeto41}')

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un
Long
String'''

variable4 = Objeto7.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = Objeto8.Catched, not False

# Esto es un comentario simple

'''Esto
Es
Un
Comentario 
Compuesto'''

print (f'Esta es una concatenacion simple {PEPE.Diccionario_Poke["Poke3"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene un total de {Objeto8.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Erick' in PEPE.Lista1)
print (f'James' not in PEPE.Tupla_Poke)
print (PEPE.Diccionario_Poke['Poke2'] in PEPE.Set_Conjunto_Poke1)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables y al mismo tiempo es snake case {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'La lista 1 tiene {len(Lista_Uno)}')
print (f'{Lista_Uno}')

Cociente, Residuo = divmod(Objeto8.Cantidad, Sumatoria2(1, 2, 1, 3))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Un rango de elementos de la lista 2 es {PEPE.Lista2[::2]}')
print (f'Un rango de elementos de la lista 2 es {PEPE.Lista2[::3]}')
print (f'Un rango de elementos de la lista 2 es {PEPE.Lista2[:2]}')
print (f'Un rango de elementos de la lista 2 es {PEPE.Lista2[2:]}')
print (f'Un rango de elementos de la lista 2 es {PEPE.Lista2[2:3]}')
print (f'Un rango de elementos de la lista 2 es {PEPE.Lista2[0:None]}')
print (f'Un rango de elementos de la lista 2 es {PEPE.Lista2[:]}')

print (f'{Lista_Uno[1]} eso que esta ahi es un {PEPE.Lista2[PEPE.Lista2.index("Koala")]}?')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, 200, 100)

print (f'{Lista_Cuatro}')

del Lista_Uno[1]

Lista_Uno.remove('Coco Rayado')

Lista_Uno.pop(-2)
Lista_Uno.pop(-1)
Lista_Uno.pop(-1)

print (f'La lista 1 tiene {len(Lista_Uno)}')
print (f'{Lista_Uno}')

Lista_Uno_Copia = Lista_Uno.copy()

Lista_Uno.clear()

print (f'{Lista_Uno}')
print (f'{Lista_Uno_Copia}')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'{dir(PEPE)}')

Tupla1 = ('Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde')

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Green', 'Blue'))

print (f'{Tupla1}')

Tupla2 = 'Uno',

Tupla3 = 'Uno', 'Dos', 'Tres',

print (f'{Tupla1}')
print (f'{Tupla2}')
print (f'{Tupla3}')
print (f'{Tupla3[2:3]}')

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Variable_Funcion_Tupla)}')

Set_Conjunto1 = {'Roca', 'Roca', 'Roca', 'Roca', 'Roca'}
Set_Conjunto1.add(Objeto6.Tipo)

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Rock', 'Electric', 'Water'})

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

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})

Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, 'Chocobanano'})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

Contador = 0

for elemento in enumerate(Set_Conjunto_Menu1):
    print (f'{elemento[0]} - {elemento[1]}')
    
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
print (f'{SetA2}')'''

'''SetA2.intersection_update(SetB2)
print (f'{SetA2}')'''

'''SetA2.difference_update(SetB2)
print (f'{SetA2}')'''

'''SetB2.difference_update(SetA2)
print (f'{SetB2}')'''

'''SetA2.symmetric_difference_update(SetB2)

print (f'{SetA2}')'''

Diccionario1 = {
    'Nombre' : Lista_Uno_Copia[0],
    'Edad' : Variable_Sumatoria,
    'Votante' : Variable_Funcion_Tupla[3]
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

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2.values()}')
print (f'{Diccionario2.items()}')
print (f'{Diccionario2["Nombre"][2]}')
print (f'{Diccionario2.get("Edad")[1]}') #type: ignore

print (f'-' * 20)

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3.values()}')
print (f'{Diccionario3.items()}')
print (f'{Diccionario3["Ingresos"]}')
print (f'{Diccionario3.get("Gastos")}')

print (f'-' * 20)

Diccionario1['Nombre'] = Saludar_Dos()

print (f'{Diccionario1}')

Diccionario1_Copia = Diccionario1.copy()

del Diccionario1['Nombre']
Diccionario1.pop('Edad')

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')
print (f'{Diccionario1_Copia}')

print (f'-' * 20)

Diccionario1 = dict({1 : 'Karlita', 2 : 6, 3 : False})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario1.get(1)} no puede votar ya que solamente tiene {Diccionario2['Edad'][2]} añitos')

print (f'El resultado de la operacion es {Lista_Cuatro[2] * Diccionario1.get(2)}') #type: ignore

print (f'Cuantos {Objeto8.Nombre}s tiene {PEPE.Tupla_Poke[0]}?')

print (f'{Lista_Uno_Copia[1]} es un hombre y {Diccionario2['Nombre'][2]} es una mujer')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'HelloWorld')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = 'Jacqueline'

print (f'-' * 20)

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio1.keys()}')
print (f'{Diccionario_Vacio1.values()}')
print (f'{Diccionario_Vacio1.items()}')
print (f'{Diccionario_Vacio1["B"]}')
print (f'{Diccionario_Vacio1.get("C")}')

print (f'-' * 20)

print (f'{Diccionario_Vacio2}')
print (f'{Diccionario_Vacio2.keys()}')
print (f'{Diccionario_Vacio2.values()}')
print (f'{Diccionario_Vacio2.items()}')
print (f'{Diccionario_Vacio2["Uno"]}')
print (f'{Diccionario_Vacio2.get("Dos")}')

print (f'-' * 20)

Key1 = [f'Elemento{i}' for i in range(len(Lista_Uno_Copia))]

print (f'{Key1}')

print (f'-' * 20)

Diccionario4 = dict(zip(Key1, Lista_Uno_Copia))

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Elemento2"]}')
print (f'{Diccionario4.get("Elemento3")}')

print (f'-' * 20)

for elemento in Diccionario1_Copia:
    print (f'{Diccionario1_Copia[elemento]}')
    
print (f'-' * 20)

for elemento in Diccionario1_Copia.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario1_Copia.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario1_Copia.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

print (f'-' * 20)

Set_Csv3 = set(Cargar_Csv3['product'])

print (f'{Set_Csv3}')

Key2 = [f'Key_{i}' for i in range(len(Set_Csv3))]

print (f'{Key2}')

print (f'-' * 20)

Diccionario5 = dict(zip(Key2, Set_Csv3))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key_3"]}')
print (f'{Diccionario5.get("Key_6")}')

print (f'-' * 20)

Fecha3 = '2026-04-01'

try:
    Fech3 = datetime.strptime(Fecha3, '%Y-%m-%d').date()
    Fech3_Formateado = pd.to_datetime(Fech3)
    Cargar_Csv3['date'] = pd.to_datetime(Cargar_Csv3['date'])
except ValueError, TypeError:
    print (f'Error, el formato de la fecha es incorrecto')
    exit()
    
Cargar_Csv3['TOTALITO'] = Cargar_Csv3['quantity'] * Cargar_Csv3['price']
    
Encontrado3 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech3_Formateado.date()]

if (Encontrado3.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! ventas encontradas')
    
    Grupo7 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo7_Min = Grupo7.idxmin()
    Grupo7_Max = Grupo7.idxmax()
    Grupo7_Min_Cant = Grupo7.min()
    Grupo7_Max_Cant = Grupo7.max()
    
    print (f'En la fecha {Fech3_Formateado} el producto {Grupo7_Min} vendio un total de {Grupo7_Min_Cant} unidades')
    print (f'En la fecha {Fech3_Formateado} el producto {Grupo7_Max} vendio un total de {Grupo7_Max_Cant} unidades')
    
    print (f'El total de clientes que compraron productos en esta fecha fue de {Grupo7.count()}')
    print (f'El total de productos comprados fue de {Grupo7.sum()}')
    
    Grupo8 = Encontrado3.groupby('product')['TOTALITO'].sum()
    
    print (f'El total en dinero vendido en esta fecha fue de ${Grupo8.sum()}')
    
    Promedio3 = Grupo8.sum() / Grupo7.count()
    
    print (f'El promedio de venta en dinero fue de ${round(Promedio3, 2)}')
    print (f'El promedio de venta en dinero fue de ${Grupo8.mean()}')
    
print (f'-' * 20)

Division_Baja = 14 // 7
Exponente = 4**3
Modulo = 20 % 6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'-' * 20)

print (f'{type(variable1)}')
print (f'{type(variable4)}')
print (f'{type(variable6)}')
print (f'{type(Lista_Sorteo)}')
print (f'{type(Tupla3)}')
print (f'{type(Set_Conjunto1)}')
print (f'{type(Set_Conjunto_Menu2)}')
print (f'{type(Diccionario1_Copia)}')
print (f'{type(Objeto13)}')
print (f'{type(Funcion_Diccionario)}')
print (f'{type(Array1)}')
print (f'{type(Data_Frame_Concatenate)}')

if (Diccionario3['Ingresos'] > 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos Altos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] == 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] < 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')
    
variable8 = 'Josue'
variable9 = 20

if (variable8 == 'Erick' and variable9 > 30):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')
    
if (variable8 == 'Erick' or variable9 > 30):
    print (f'Al menos una condicion se cumple')
else:
    print (f'Error, ninguna condicion se cumple')
    
print (f'{dir(variable1)}')

'''print (f'{help(Objeto11)}')'''

print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Sumatoria2(1, 2, 3, 4)
        self.Clasificado = True

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')
        
Objeto42 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Ash")], 'Kanto', Objeto6.Nombre)
Objeto43 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Brooke")], 'Paldea', Objeto7.Nombre)
Objeto46 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")], 'Alolah', Objeto8.Nombre)

Objeto42.Desplegar()
Objeto43.Desplegar()
Objeto46.Desplegar()

print (f'-' * 20)

class Pokemon3():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        
Objeto44 = Pokemon3(PEPE.Diccionario_Poke["Poke1"])

Objeto44.Mostrar()

class Poke_Kid3(Pokemon3):
    def __init__(self, Nombre, Tipo):
        super().__init__(Nombre)
        self.Tipo = Tipo

    def Mostrar(self):
        print (f'Tipo: {self.Tipo}')
        
Objeto45 = Poke_Kid3(PEPE.Diccionario_Poke["Poke1"], 'Electrico')

Pokemon3.Mostrar(Objeto45)
Objeto45.Mostrar()

print (f'{Objeto45.Nombre}')

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
    
for elemento in Lista_Uno_Copia:
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'El elemento en la posicion {indice} es {elemento}')
    
print (f'-' * 20)

variable10 = 'eSTEban'
variable10_letra = variable10[0]

print (f'{variable10}')
print (f'{variable10.lower()}')
print (f'{variable10.upper()}')
print (f'{variable10.capitalize()}')

print (f'{variable10.lower().find("t")}')
print (f'{variable10.lower().index("b")}')

print (f'La letra {variable10_letra} aparece un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = 'este es un texto cualquiera para ver si esto sirve o no'

Lista_variable11 = variable11.split(' ')

for elemento in Lista_variable11:
    print (f'{elemento}')
    
print (f'La cantidad de palabras escritas es {len(Lista_variable11)}')

print (f'-' * 20)

variable12 = 'hola'

if (isinstance(variable12, (str))):
    print (f'Lo ingresado es texto')
else:
    print (f'Lo ingresado no es texto')
    
if (variable12.isalpha()):
    print (f'Lo ingresado es texto')
else:
    print (f'Lo ingresado no es texto')
    
try:
    Numerito1 = float(variable12)
    if (Numerito1.is_integer()):
        print (f'Esto es un numero entero')
    else:
        print (f'Esto es un numero decimal')
except ValueError:
    print (f'Lo ingresado, no es numero, es texto')
    
print (f'-' * 20)
    
variable13 = '3.6'

if (isinstance(variable13, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Error, lo ingresado no es un numero decimal')
    
try:
    Numerito2 = float(variable13)
    if (Numerito2.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado, no es numero, es texto')
    
print (f'-' * 20)

variable14 = '4'

if (variable14.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
if (isinstance(variable14, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
try:
    Numerito3 = float(variable14)
    if (Numerito3.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado, no es numero, es texto')
    
print (f'-' * 20)

variable15 = 'erick123'

if (variable15.isalnum()):
    print (f'Lo ingresado tiene letras o tiene numeros')
else:
    print (f'Error')
    
print (f'-' * 20)

variable16 = '  s    '

if (variable16.isspace()):
    print (f'Esto esta compuesto solo de espacios')
else:
    print (f'Error, esto tiene mas que espacios')
    
variable17 = 'eSteBAN'

if (variable17.lower().islower()):
    print (f'TODO ESTO ES MINUSCULA')
else:
    print (f'Error, no todo esto es minuscula')
    
if (variable17.upper().isupper()):
    print (f'TODO ESTO ES MAYUSCULA')
else:
    print (f'Error, no todo esto es mayuscula')
    
print (f'-' * 20)

print (f'{PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

print (f'-' * 20)

for elemento in Diccionario2:
    print (f'{Diccionario2[elemento]}')
    
print (f'-' * 20)

for elemento in Diccionario2.keys():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario2.values():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario2.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'El numero es {PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1
    
print (f'-' * 20)

Lista_Animales = []
Lista_Animales.append('Jirafa')
Lista_Animales.insert(1, PEPE.Lista2[2])
Lista_Animales.extend(['Cocodrilo', 'Avestruz'])

print (f'{Lista_Animales}')

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Cocodrilo'):
        print (f'El animal seleccionado es un reptil asombroso')
        break
    else:
        Contador+= 1
        continue
    
for elemento1, elemento2 in zip(Lista_Animales, Lista_Uno_Copia):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
print (f'-' * 20)

Lista_Num_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Num_Mult}')

print (f'-' * 20)

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1
    
print (f'-' * 20)

Mayor = max(Lista_Num_Mult)
Menor = min(Lista_Num_Mult)
Redondeado = round(14.458795, 2)

print (f'El menor de los numeros es {Menor} y el mayor es {Mayor}')

print (f'El redondeado es {Redondeado}')

print (f'{bool(False)}')
print (f'{bool(not True)}')
print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool("")}')

Todo_All = all([Lista_Uno_Copia, Set_Conjunto_Menu1, Tupla1, None])

print (f'{Todo_All}')

print (f'-' * 20)

Sumatoria4 = sum(Lista_Num_Mult)

print (f'El resultado de la sumatoria es {Sumatoria4}')

Uno = int('500')
Dos = str(500)
Tres = float(Uno)
Cuatro = list(Set_Conjunto_Menu1)
Cinco = set(PEPE.Tupla_Poke)
Seis = tuple(Lista_Animales)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')
print (f'{type(Cuatro)}')
print (f'{type(Cinco)}')
print (f'{type(Seis)}')

print (f'-' * 20)

print (f' - '.join(Lista_Animales))
print (f' - '.join(Set_Conjunto_Menu1))
print (f' - '.join(PEPE.Tupla_Poke))

print (f'-' * 20)

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

print (f'-' * 20)

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

print (f'-' * 20)

'''def Floating1(Numero):
    try:
        Numerito4 = float(Numero)
        if (Numerito4.is_integer()):
            Resultado = Sumatoria2(1, 2, 3, 4) * Objeto7.Cantidad + Numerito4
            return round(Resultado, 2)
        else:
            Resultado = Sumatoria2(1, 2, 3, 4) * Objeto7.Cantidad + Numerito4
            return round(Resultado, 2)
    except (ValueError, TypeError):
        print (f'Error, lo ingresado no es un numero')

print (f'El resultado de la operacion es {Floating1(PEPE.Flotante1)}')

Resultado1 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado1}')

def Floating3(Cadena):
    Cadena_Limpia = Cadena.replace(' ', '')
    if (Cadena_Limpia.isalpha() and isinstance(Cadena_Limpia, (str))):
        print (f'Correcto, lo que ingreso es un texto')
    else:
        print (f'Error, lo ingresado no es un texto')

Floating3(PEPE.Flotante3)

def Floating4(Cadena):
    Lista_Cadena = Cadena.split(' ')
    for elemento in Lista_Cadena:
        print (f'{elemento}')
        
    print (f'La cantidad de palabras digitadas es {len(Lista_Cadena)}')
    
Floating4(PEPE.Flotante4)'''

'''Lista_Alumnos = []

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
    
'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.extend([Estudiante])
        
    Lista.sort(key = lambda Num : Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de la lista es {Menore}, su edad es {Lista[0][1]}')
    print (f'El mayor de la lista es {Mayore}, su edad es {Lista[-1][1]}')
    
Colegio(Lista_Alumnos)'''

'''def Exception_Finale():
    while True:
        Numerito4 = input(f'Ingrese un numero: ')
        try:
            Numerito5 = float(Numerito4)
            if (Numerito5.is_integer()):
                print (f'Lo ingresado es un numero entero')
                break
            else:
                print (f'Lo ingresado es un numero decimal')
                break
        except:
            print (f'Error, necesito que ingreses un numero')

Exception_Finale()'''

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

Texto13 = 'ericksuper80@hotmail.com'

Pattern15 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar20 = bool(re.fullmatch(Pattern15, Texto13))

if (Buscar20 == True):
    print (f'El formato del correo electronico es correcto')
else:
    print (f'Error, formato de correo invalido')
    
import re

Texto14 = '31'

Pattern16 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar21 = bool(re.fullmatch(Pattern16, Texto14))

if (Buscar21 == True):
    print (f'El numero esta entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
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
    print (f'Error, la fecha tiene un formato incorrecto')
    exit()
    
Cargar_Csv4['TOTALITO'] = Cargar_Csv4['quantity'] * Cargar_Csv4['price']
    
Encontrado4 = Cargar_Csv4[Cargar_Csv4['date'].dt.date == Fech4_Formateada.date()]

if (Encontrado4.empty):
    print (f'No se encontraron ventas en esta fecha')
else:
    print (f'Genial! Encontramos ventas')
    
    Grupo8 = Encontrado4.groupby('product')['quantity'].sum()
    Grupo8_Min = Grupo8.idxmin()
    Grupo8_Max = Grupo8.idxmax()
    Grupo8_Min_Cant = Grupo8.min()
    Grupo8_Max_Cant = Grupo8.max()
    
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo8_Min} vendio un total de {Grupo8_Min_Cant} unidades')
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo8_Max} vendio un total de {Grupo8_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron en esta fecha fue {Grupo8.count()}')
    print (f'La cantidad de productos vendidos en esta fecha fue {Grupo8.sum()}')
    
    Grupo9 = Encontrado4.groupby('product')['TOTALITO'].sum()
    
    print (f'El total en dinero que vendimos en esta fecha fue de ${Grupo9.sum()}')
    print (f'El promedio de venta en esta fecha fue de {Grupo9.sum() / Grupo8.count()}')
    print (f'El promedio de venta en esta fecha fue de {Grupo9.mean()}')
    
print (f'-' * 20)