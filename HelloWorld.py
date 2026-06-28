try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo no existe')
    raise

class Persona1():
    def __init__(self, Nombre):
        self.Nombre = Nombre

Objeto1 = Persona1('Erick Josue')

print (f'Hola, mi nombre es {Objeto1}')

class Inventario1:
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto2 = Inventario1()

Objeto2.Productos.extend(['Azul'])
Objeto2.Productos.append('Verde')
Objeto2.Productos.insert(1, 'Rojo')

print (f'La cantidad de elementos de la lista es {len(Objeto2)}')

class Igualdad1:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto3 = Igualdad1('Erick')
Objeto4 = Igualdad1('Erick')

if (Objeto3 == Objeto4):
    print (f'Ambos objetos son iguales')
else:
    print (f'Error, los objetos no son iguales')
    
class Interno1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Interno1 = list([
    Interno1('Carlos'),
    Interno1('Ramiro'),
    Interno1('Susanita')
])

print (f'{Lista_Interno1}')

print (f'-' * 20)

'''import requests

URL = 'http://localhost:8000/elemento'

Diccionario = {
    'ID' : 595852,
    'Nombre' : "Pikachu"
}

Agregado1 = requests.post(URL, json=(Diccionario))
Agregado2 = Agregado1.json()

print (f'{Agregado2}')

print (f'-' * 20)

Resultado = requests.get(URL)

Datos = Resultado.json()

print (f'Mi pokemon favorito de todos es {Datos["Resultado"][0]["Nombre"]}')'''

var1 = '3'

if (isinstance(var1, (int))):
    print (f'El numero es entero')
else:
    print (f'Error, el numero no es entero')
    
if (var1.isnumeric()):
    print (f'El numero es entero')
else:
    print (f'Error, el numero no es entero')
    
try:
    Numerito1 = float(var1)
    if (Numerito1.is_integer()):
        print (f'El numero es entero')
    else:
        print (f'El numero es decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var2 = 3.5

if (isinstance(var2, (float))):
    print (f'Esto es un numero decimal')
else:
    print (f'Error, lo ingresado no es un numero decimal')
    
try:
    Numerito2 = float(var2)
    if (Numerito2.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var3 = 3.6

if (isinstance(var3, (int, float))):
    print (f'Lo ingresado es un numero decimal o entero')
else:
    print (f'Error, no es un numero')
    
print (f'-' * 20)

var4 = 'erick123'

if (var4.isalnum()):
    print (f'Lo ingresado puede ser numero o texto')
else:
    print (f'Error de contexto')
    
print (f'-' * 20)

var5 = 'hola'

if (isinstance(var5, (str))):
    print (f'Lo ingresado es texto')
else:
    print (f'Error, lo ingresado no es texto')
    
if (var5.isalpha()):
    print (f'Lo ingresado es texto')
else:
    print (f'Error, lo ingresado no es texto')
    
try:
    Numerito3 = float(var5)
    if (Numerito3.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado es texto')
    
print (f'-' * 20)

import re

Texto1 = "   Hola!!!   mundo@@   123   "

Texto1_Version1 = Texto1.strip()
Texto1_Version2 = ' '.join(Texto1_Version1.split())
Texto1_Version3 = Texto1_Version2.lower()
Texto1_Version4 = re.sub(r'[^a-zA-Z\s]', '', Texto1_Version3)

print (f'{Texto1_Version4}')

print (f'-' * 20)

import pandas as pd
import re
from datetime import datetime

Ruta_Csv1 = 'C:\\Repo\\Store.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

print (f'-' * 20)

Set_Conjunto_Csv1 = set(Cargar_Csv1['product'])

Key1 = [f'Key_{i}' for i in range(len(Set_Conjunto_Csv1))]

Diccionario1 = dict(zip(Key1, Set_Conjunto_Csv1))

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1["Key_3"]}')
print (f'{Diccionario1.get("Key_4")}')

print (f'-' * 20)

Fecha1 = '2026-04-01'

try:
    Fech1 = datetime.strptime(Fecha1, '%Y-%m-%d').date()
    Fech1_Formateada = pd.to_datetime(Fech1)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Error, el formato de la fecha es invalido')
    exit()
    
Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrada1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()]

if (Encontrada1.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! Encontramos ventas en esta fecha')
    
    Grupo1 = Encontrada1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'En la fecha {Fech1_Formateada}, el producto {Grupo1_Min} vendio un total de {Grupo1_Min_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada}, el producto {Grupo1_Max} vendio un total de {Grupo1_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que nos compraron en esta fecha fue {Grupo1.count()}')
    print (f'La cantidad de productos vendidos en esta fecha fue {Grupo1.sum()}')
    
    Grupo2 = Encontrada1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido fue ${Grupo2.sum()}')
    
    Promedio1 = Grupo2.sum() / Grupo1.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue ${Promedio1}')
    print (f'El promedio de dinero vendido en esta fecha fue ${Grupo2.mean()}')
    
print (f'-' * 20)

Set_Conjunto_A1 = {1, 2, 3, 4}
Set_Conjunto_B1 = {3, 4, 5, 6}

print (f'{Set_Conjunto_A1.union(Set_Conjunto_B1)}')
print (f'{Set_Conjunto_A1 | Set_Conjunto_B1}')

print (f'-' * 20)

print (f'{Set_Conjunto_A1.intersection(Set_Conjunto_B1)}')
print (f'{Set_Conjunto_A1 & Set_Conjunto_B1}')

print (f'-' * 20)

print (f'{Set_Conjunto_A1.difference(Set_Conjunto_B1)}')
print (f'{Set_Conjunto_A1 - Set_Conjunto_B1}')

print (f'-' * 20)

print (f'{Set_Conjunto_B1.difference(Set_Conjunto_A1)}')
print (f'{Set_Conjunto_B1 - Set_Conjunto_A1}')

print (f'-' * 20)

print (f'{Set_Conjunto_A1.symmetric_difference(Set_Conjunto_B1)}')
print (f'{Set_Conjunto_A1 ^ Set_Conjunto_B1}')

print (f'-' * 20)

Set_Conjunto_C1 = {1, 2, 3, 4, 5}
Set_Conjunto_D1 = {4, 5}
Set_Conjunto_E1 = set({8})

print (f'{Set_Conjunto_C1.issuperset(Set_Conjunto_D1)}')
print (f'{Set_Conjunto_C1 >= Set_Conjunto_D1}')
print (f'-' * 20)

print (f'{Set_Conjunto_D1.issubset(Set_Conjunto_C1)}')
print (f'{Set_Conjunto_D1 <= Set_Conjunto_C1}')
print (f'-' * 20)

print (f'{Set_Conjunto_C1.isdisjoint(Set_Conjunto_E1)}')

print (f'-' * 20)

'''Set_Conjunto_A1.update(Set_Conjunto_B1)

print (f'{Set_Conjunto_A1}')'''

'''Set_Conjunto_A1.intersection_update(Set_Conjunto_B1)

print (f'{Set_Conjunto_A1}')'''

'''Set_Conjunto_A1.difference_update(Set_Conjunto_B1)

print (f'{Set_Conjunto_A1}')'''

'''Set_Conjunto_B1.difference_update(Set_Conjunto_A1)

print (f'{Set_Conjunto_B1}')'''

'''Set_Conjunto_A1.symmetric_difference_update(Set_Conjunto_B1)

print (f'{Set_Conjunto_A1}')'''

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
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Objeto5 = Pastel1()
Objeto5.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Sabor1 = Chocolate1()
Objeto6 = Pastel2(Sabor1)
Objeto6.Hornear()

Sabor2 = Vainilla1()
Objeto7 = Pastel2(Sabor2)
Objeto7.Hornear()

Sabor3 = Fresa1()
Objeto8 = Pastel2(Sabor3)
Objeto8.Hornear()

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

Pattern1 = r'[a-zA-Z0-9\.\/\*\\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|net|org)'

Buscar1 = re.findall(Pattern1, Texto2)

print (f'{Buscar1}')

for indice, elemento in enumerate(Buscar1, start=1):
    print (f'{indice} -- {elemento}')
    
print (f'-' * 20)

Texto3 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Version1

import re

Pattern2 = r'\!|\?|\.{2,}'

Buscar2 = re.sub(Pattern2, '', Texto3)

print (f'{Buscar2}')

print (f'-' * 20)

# Version2

import re

Buscar3 = re.sub(r'[^a-zA-Z0-9\s]+', '', Texto3)

print (f'{Buscar2}')

# Version3

import re

Pattern3 = r'[a-zA-Z0-9\.\/\*\-\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos1 = re.findall(Pattern3, Texto3)

Texto3_temp1 = Texto3

for i, email in enumerate(Correos1, start=1):
    Texto3_temp1 = Texto3_temp1.replace(email, f'Sample{i}')
    
print (f'{Texto3_temp1}')

Texto3_temp2 = re.sub(r'\!|\?|\.{2,}', '', Texto3_temp1)

print (f'{Texto3_temp2}')

for i, email in enumerate(Correos1, start=1):
    Texto3_temp2 = Texto3_temp2.replace(f'Sample{i}', email)
    
print (f'{Texto3_temp2}')

print (f'-' * 20)

import re

Texto4 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Pattern4 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)'

Correos2 = re.findall(Pattern4, Texto4)

print (f'{Correos2}')

Texto4_temp1 = Texto4

for i, email in enumerate(Correos2, start=1):
    Texto4_temp1 = Texto4_temp1.replace(email, f'Sample{i}')
    
print (f'{Texto4_temp1}')

Texto4_temp2 = re.sub(r'\!|\?|\.{2,}', '', Texto4_temp1)

print (f'{Texto4_temp2}')

for i, email in enumerate(Correos2, start=1):
    Texto4_temp2 = Texto4_temp2.replace(f'Sample{i}', email)
    
print (f'{Texto4_temp2}')

print (f'-' * 20)

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
    print (f'{elemento}')
    
print (f'-' * 20)

'''Contador = 0

Lista_Promedio = list([])

while Contador < 3:
    while True:
        Elemento = input(f'Ingrese el numero {Contador}: ')
        try:
            Numerito4 = float(Elemento)
            if (Numerito4.is_integer()):
                Lista_Promedio.extend([Numerito4])
                break
            else:
                Lista_Promedio.extend([Numerito4])
                break
        except ValueError:
            print (f'Error, lo ingresado no es un numero')
    Contador+= 1
    
print (f'{Lista_Promedio}')

Promedio2 = sum(Lista_Promedio) / len(Lista_Promedio)

print (f'El promedio de las notas es {round(Promedio2, 2)}')'''

from Module_Own import Pokemon1 as Poke1

Objeto9 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto10 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto9.Mostrar()

print (f'-' * 20)

Objeto10.Mostrar()

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto11 = Poke_Kid1(PEPE.Diccionario_Poke['Poke2'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto11)
Objeto11.Mostrar()

print (f'-' * 20)

class Camara1():
    def Tomar_Fotografia(self):
        print (f'La fotografia se tomo correctamente')
        
class Reproductor_Musica1():
    def Reproducir_Musica(self):
        print (f'La musica fue reproducida correctamente')
        
class SmartPhone1(Camara1, Reproductor_Musica1):
    def Encender_Smartphone(self):
        print (f'El smartphone fue encendido correctamente')
        
Objeto12 = SmartPhone1()

Objeto12.Encender_Smartphone()
Objeto12.Reproducir_Musica()
Objeto12.Tomar_Fotografia()

print (f'-' * 20)

class Veterinaria1():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad}')
        print (f'Peso: {self.Peso}')
        
class Perro1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        
    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        
Objeto13 = Perro1('Chester', 5, 2.8, 'Poodle', 'Asma')

Veterinaria1.Mostrar(Objeto13)
Objeto13.Mostrar()

print (f'-' * 20)
        
class Gato1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto14 = Gato1('Messi', 1.5, 2, 'Gris', 'No')

Veterinaria1.Mostrar(Objeto14)
Objeto14.Mostrar()

print (f'-' * 20)
        
class Pajaro1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto15 = Pajaro1('Polly', 31, 0.4, 'Cacatua Blanca', 'Si')

Veterinaria1.Mostrar(Objeto15)
Objeto15.Mostrar()

print (f'-' * 20)

class Atacante1():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon
        
    def Mostrar(self):
        print (f'Damage: {self.Damage}')
        print (f'Weapon: {self.Weapon}')
        
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
        
Objeto16 = Paladin1(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto16.Mostrar()
Atacante1.Mostrar(Objeto16)
Defensor1.Mostrar(Objeto16)

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
        
Objeto17 = D1()

A1.Mostrar(Objeto17)
B1.Mostrar(Objeto17)
C1.Mostrar(Objeto17)
Objeto17.Mostrar()
E1.Mostrar(Objeto17)

print (f'-' * 20)

class Efectivo1:
    def Pagar(self):
        print (f'El pago se realizo en Efectivo')
        
class Tarjeta1:
    def Pagar(self):
        print (f'El pago se realizo en Tarjeta')
        
class Cripto1:
    def Pagar(self):
        print (f'El pago se realizo en Cripto')
        
Objeto18 = Cripto1()
Objeto19 = Tarjeta1()
Objeto20 = Efectivo1()

Objeto18.Pagar()
Objeto19.Pagar()
Objeto20.Pagar()

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
        print (f'Su saldo a la fecha es de ${self.__Saldo}')
        
Objeto21 = Cuenta_Bancaria1(100)
Objeto21.Depositar(25)
Objeto21.Mostrar()

print (f'Su saldo privado es de {Objeto21.Dinero}')

Objeto21.Dinero = '50,000,000'

Objeto21.Mostrar()

print (f'Su saldo privado es de {Objeto21.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla1(ABC):
    @abstractmethod
    def General(self):
        pass
    
class Sub_Plantilla1(Plantilla1):
    def Mostrar(self):
        print (f'Este metodo pertenece a esta clase')
        
    def General(self):
        print (f'Esto es parte de la plantilla y siempre debe incluirse en la abstraccion')
        
Objeto22 = Sub_Plantilla1()

Objeto22.Mostrar()
Objeto22.General()

print (f'-' * 20)

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
        print (f'El retador ha elegido a {self.Favorito.Elegir()} para la batalla!!!')
        
Objeto23 = Battle1()
Objeto23.Batallar()

print (f'-' * 20)

class Battle2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El retador ha elegido a {self.Favorito.Elegir()} para la batalla')
        
Criatura1 = Bulbasaur1()
Objeto24 = Battle2(Criatura1)
Objeto24.Batallar()

Criatura2 = Treekoo1()
Objeto25 = Battle2(Criatura2)
Objeto25.Batallar()

Criatura3 = Chikorita1()
Objeto26 = Battle2(Criatura3)
Objeto26.Batallar()

print (f'-' * 20)

import re

Texto5 = 'esto 20 es un! texto hola cualquiera, lo que deseamos es 8  que hela - lo escrito realmente hala 588 @ sea de utilidad'

Buscar4 = re.search(r'escrito', Texto5)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\d+', Texto5)

print (f'{Buscar5}')

Buscar6 = re.findall(r'h.la', Texto5)

print (f'{Buscar6}')

Buscar7 = re.fullmatch(r'esto 20 es un\! texto hola cualquiera, lo que deseamos es 8  que hela \- lo escrito realmente hala 588 \@ sea de utilidad', Texto5)

print (f'{Buscar7}')

Buscar8 = re.findall(r'\d+', Texto5)

print (f'{Buscar8}')

Buscar9 = re.findall(r'\D+', Texto5)

print (f'{Buscar9}')

Buscar10 = re.findall(r'\w+', Texto5)

print (f'{Buscar10}')

Buscar11 = re.findall(r'\W+', Texto5)

print (f'{Buscar11}')

Buscar12 = re.findall(r'\s+', Texto5)

print (f'{Buscar12}')

Buscar13 = re.findall(r'\S+', Texto5)

print (f'{Buscar13}')

'''
+
*
?
{1}
{1,6}
{2,}
'''

Buscar14 = re.findall(r'^esto', Texto5)

print (f'{Buscar14}')

Buscar15 = re.findall(r'ad$', Texto5)

print (f'{Buscar15}')

Buscar16 = re.findall(r'\d{3}\s\W', Texto5)

print (f'{Buscar16}')

Buscar17 = re.findall(r'[ea]{2,}', Texto5)

print (f'{Buscar17}')

print (f'-' * 20)

import re

Texto6 = 'ericksuper80@hotmail.com'

Pattern5 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'
Pattern5 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.[a-z]{2,}$'

Buscar18 = bool(re.fullmatch(Pattern5, Texto6))

if (Buscar18 == True):
    print (f'El correo tiene el formato correcto')
else:
    print (f'Error, formato de correo invalido')
    
import re

Texto7 = '32'

Pattern6 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar19 = bool(re.match(Pattern6, Texto7))

if (Buscar19):
    print (f'El numero esta entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

Texto8 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern7 = r'\d{2}\/[0-9]{2}\/\d{3,4}'

Replacement7 = 'XX/XX/XXXX'

Buscar20 = re.sub(Pattern7, Replacement7, Texto8)

print (f'{Buscar20}')

Pattern8 = r'\+\d{1}\-[0-9]{3}\-\d{3}\-[0-9]{4}'

Replacement8 = '+Uno-CincoX3-CincoX3-CincoX4'

Buscar21 = re.sub(Pattern8, Replacement8, Buscar20)

print (f'{Buscar21}')

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

Pattern9 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar22 = re.findall(Pattern9, Texto9)

print (f'{Buscar22}')

for elemento in Buscar22:
    print (f'{elemento}')
    
print (f'-' * 20)

import re

Texto10 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Version1

import re

Pattern10 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos3 = re.findall(Pattern10, Texto10)

print (f'{Correos3}')

Texto10_temp1 = Texto10

for i, email in enumerate(Correos3, start=1):
    Texto10_temp1 = Texto10_temp1.replace(email, f'Sample{i}')
    
print (f'{Texto10_temp1}')

Texto10_temp2 = re.sub(r'\!|\?|\.{2,}', '', Texto10_temp1)

print (f'{Texto10_temp2}')

for i, email in enumerate(Correos3, start=1):
    Texto10_temp2 = Texto10_temp2.replace(f'Sample{i}', email)
    
print (f'{Texto10_temp2}')

print (f'-' * 20)

# Version2

Buscar23 = re.sub(r'\!|\?|\.{2,}', '', Texto10)

print (f'{Buscar23}')

print (f'-' * 20)

# Version3

Buscar24 = re.sub(r'[^a-zA-Z0-9\s]', '', Texto10)

print (f'{Buscar24}')

print (f'-' * 20)

var6 = 3.5

if (isinstance(var6, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Error, lo ingresado no es un numero decimal')
    
try:
    Numerito4 = float(var6)
    if (Numerito4.is_integer()):
        print (f'Se ingreso un numero entero')
    else:
        print (f'Se ingreso un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var7 = '3'

if (var7.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
if (isinstance(var7, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
try:
    Numerito5 = float(var7)
    if (Numerito5.is_integer()):
        print (f'Se ingreso un numero entero')
    else:
        print (f'Se ingreso un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
var8 = 'erick123'

if (var8.isalnum()):
    print (f'Lo ingresado puede ser texto o numero')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var9 = 'hola'

if (var9.isalpha()):
    print (f'Lo ingresado es un texto')
else:
    print (f'Error, lo ingresado no es un texto')
    
if (isinstance(var9, (str))):
    print (f'Lo ingresado es un texto')
else:
    print (f'Error, lo ingresado no es un texto')
    
try:
    Textico = str(var9)
    if (Textico.isalpha()):
        print (f'Lo ingresado es un texto')
except ValueError:
    print (f'Error, lo ingresado no es un texto')
    
print (f'-' * 20)

var10 = 3.5

if (isinstance(var10, (int, float))):
    print (f'Esto es un numero entero o decimal')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var11 = '   s  '

if (var11.isspace()):
    print (f'Esto esta compuesto por espacios nada mas')
else:
    print (f'Error, esto tiene mas que espacios')
    
print (f'-' * 20)

var12 = 'eSteBAN'

if (var12.lower().islower()):
    print (f'MINUSCULAS')
else:
    print (f'Error, esto no es totalmente minusculo')
    
if (var12.upper().isupper()):
    print (f'MAYUSCULA')
else:
    print (f'Error, esto no es totalmente mayuscula')
    
print (f'-' * 20)

class Persona2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto27 = Persona2('Erick Perez')

print (f'Hola, mi nombre es {Objeto27}')

print (f'-' * 20)

class Codigo2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Codigo2 = [
    Codigo2('Rojo'),
    Codigo2('Verde'),
    Codigo2('Negro')
]

print (f'La lista de elementos es {Lista_Codigo2}')

print (f'-' * 20)

class Inventario2():
    def __init__(self):
        self.Productos = list([])
        
    def __len__(self):
        return len(self.Productos)
        
Objeto28 = Inventario2()

Objeto28.Productos.append('Durazno')
Objeto28.Productos.insert(1, 'Manzana')
Objeto28.Productos.extend(['Pera', 'Uvas'])

print (f'La cantidad de elementos de la lista son {len(Objeto28)}')

print (f'-' * 20)

class Igualdad2:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto29 = Igualdad2('Erick Perez')
Objeto30 = Igualdad2('Erick Perez')

print (f'{Objeto29 == Objeto30}')

print (f'-' * 20)

'''import requests

Resultado = requests.get('http://127.0.0.1:8000')

Datos = Resultado.json()

print (f'{Datos["Texto"]}')'''

'''import requests

url = 'http://localhost:8000/elemento'

diccionario = {
    'id': 1,
    'Nombre': "Erick",
    'Edad': 30
}

respuesta = requests.post(url, json=diccionario)
print(respuesta.json())

print (f'-' * 20)

resultado = requests.get(url)
datos = resultado.json()

print(datos["Resultado"][0]["Nombre"])'''

import re

Texto11 = "   Hola!!!   mundo@@   123   "

print (f'{Texto11}')

Texto11_Version1 = Texto11.strip()

print (f'{Texto11_Version1}')

Texto11_Version2 = ' '.join(Texto11_Version1.split())

print (f'{Texto11_Version2}')

Texto11_Version3 = Texto11_Version2.lower()

print (f'{Texto11_Version3}')

Texto11_Version4 = re.sub(r'\!|\@|\d+', '', Texto11_Version3)

print (f'{Texto11_Version4}')

print (f'-' * 20)

def Exception1(Numero):
    try:
        Numerito6 = float(Numero)
        if (Numerito6.is_integer()):
            print (f'El numero es entero')
        else:
            print (f'El numero es decimal')
    except ValueError:
        print (f'Error, lo ingresado no es un numero')

Exception1('3')

print (f'-' * 20)

def Exception2(Num1, Num2):
    try:
        Sumita = Num1 + Num2
        print (f'El resultado de la operacion es {Sumita}')
    except (ValueError, TypeError):
        print (f'Error, ambos elementos deben ser numeros')

Exception2(12, 'hola')

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(7, 0)

print (f'-' * 20)

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

print (f'-' * 20)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El elemento con llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, llave fuera de rango')

Exception5('Votante')

print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Hiena')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nLeon'])
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nCocodrilo')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nElefante Grande', '\nElefante Grande', '\nElefante Grande'])
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding = 'UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke1"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke2"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke3"]}\n')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Set_Conjunto1)])
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.read()
    print (f'{Documento_Lineas}')
    Docu.close()
    
'''import requests

URL = 'http://127.0.0.1:8001/ejemplo'

Diccionario_API = {
    'id' : 456789,
    'Nombre' : "Carmen Lira",
    'Profesion' : "Escritora"
}

Agregado1 = requests.post(URL, json=(Diccionario_API))
Agregado2 = Agregado1.json()

print (f'{Agregado2}')

print (f'-' * 20)

Resultado = requests.get(URL)

Datos = Resultado.json()

print (f'Mi {Datos["Resultado"][0]["Profesion"]} favorita es {Datos["Resultado"][0]["Nombre"]}')

class Persona3():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto31 = Persona3('Erick Perez')

print (f'Hola, mi nombre es {Objeto31}')'''

print (f'-' * 20)

class Colores3:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre
        
Lista_Colores3 = [
    Colores3('Azul'),
    Colores3('Verde'),
    Colores3('Rojo')
]

print (f'Los elementos de la lista son {Lista_Colores3}')

print (f'-' * 20)

class Inventario3():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto32 = Inventario3()

Objeto32.Productos.extend(['Durazno', 'Pera'])
Objeto32.Productos.append('Manzana')
Objeto32.Productos.insert(1, 'Uvas')

print (f'La cantidad de elementos de la lista son {len(Objeto32)}')

print (f'-' * 20)

class Igualdad3:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
        
Objeto33 = Igualdad3('Coconut')
Objeto34 = Igualdad3('Coconut')

print (f'{Objeto33 == Objeto34}')

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

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame1}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate_Age}')

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()} y la mayor de las edades es {Data_Frame_Concatenate_Age.max()}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    unitario1 = elemento['Nombre']
    unitario2 = elemento['Edad']
    
    print (f'Mi nombre es {unitario1} y mi edad es {unitario2} años')
    
print (f'-' * 20)

print (f'{Data_Frame_Concatenate}')

Lista_Data_Frame = list(Data_Frame_Concatenate['Nombre'])
Key2 = [f'Key_{i}' for i in range(len(Lista_Data_Frame))]

Diccionario2 = dict(zip(Key2, Lista_Data_Frame))

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2.values()}')
print (f'{Diccionario2.items()}')
print (f'{Diccionario2["Key_2"]}')
print (f'{Diccionario2.get("Key_3")}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate}')

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()
Grupo3_Min_Cant = Grupo3.min()
Grupo3_Max_Cant = Grupo3.max()

print (f'Del dataframe la persona menor es {Grupo3_Min} y su edad es {Grupo3_Min_Cant} años')
print (f'Del dataframe la persona mayor es {Grupo3_Max} y su edad es {Grupo3_Max_Cant} años')

print (f'La cantidad de personas en el dataframe son {Grupo3.count()}')
print (f'Si sumara todas las edades, me daria el numero {Grupo3.sum()}')

Data_Frame_Concatenate['TOTALITO'] = Data_Frame_Concatenate['Edad'] * 100

Grupo4 = Data_Frame_Concatenate.groupby('Nombre')['TOTALITO'].sum()

print (f'Si sumo todos los resulatdo de las operaciones me da el numero {Grupo4.sum()}')

Promedio2 = Grupo4.sum() / Grupo3.count()

print (f'El promedio de esta operacion es {round(Promedio2, 2)}')
print (f'El promedio de esta operacion es {round(Grupo4.mean(), 2)}')

print (f'-' * 20)

'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data = Data_Frame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data = Data_Frame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data = Data_Frame_Concatenate)

plt.show()'''

print (f'La primera fila del dataframe es {Data_Frame_Concatenate.head(1)}')

print (f'-' * 20)

print (f'Las 3 primeras filas del dataframe son {Data_Frame_Concatenate.head(3)}')

print (f'-' * 20)

print (f'La ultima fila del dataframe es {Data_Frame_Concatenate.tail(1)}')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'La cantidad de Filas del dataframe son {Filas}')
print (f'La cantidad de Columnas del dataframe son {Columnas}')

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
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='familiares')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols='E:J', index_col='familiares')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, usecols='E:J', index_col='familiares', nrows=1)

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

Grupo5 = Cargar_Excel3_Sorted.groupby('tres')['cinco'].sum()

Grupo5_min = Grupo5.idxmin()
Grupo5_max = Grupo5.idxmax()
Grupo5_min_cant = Grupo5.min()
Grupo5_max_cant = Grupo5.max()

print (f'El menor de la lista es {Grupo5_min} con una edad de {Grupo5_min_cant} años')
print (f'El mayor de la lista es {Grupo5_max} con una edad de {Grupo5_max_cant} años')

print (f'La cantidad de registros en el excel es {Grupo5.count()}')

print (f'Si sumo todas las edades del excel me da el numero {Grupo5.sum()}')

Promedio3 = Grupo5.sum() / Grupo5.count()

print (f'El promedio de las edades es {round(Promedio3, 2)}')
print (f'El promedio de las edades es {round(Grupo5.mean(), 2)}')

print (f'-' * 20)

import pandas as pd

Ruta_txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_txt = pd.read_csv(Ruta_txt)

print (f'{Cargar_txt.head()}')

print (f'-' * 20)

print (f'{Cargar_txt}')

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
print (f'{Array0[1][::2]}')
print (f'{Array0[0][::3]}')
print (f'{Array0[0][:2]}')
print (f'{Array0[0][2:]}')
print (f'{Array0[2][2:3]}')
print (f'{Array0[1][0:None]}')
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
print (f'{Array1[2]}')

print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[2:3]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 > 2]}')

print (f'-' * 20)

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}')
print (f'{Array2.shape}')
print (f'{Array2.size}')
print (f'{Array2.dtype}')
print (f'{Array2[1, 1]}')

print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[:, 0]}')
print (f'{Array2[0, 2:3]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 >= 2]}')

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

Array3 = np.array([[['a', 'o', 'k'], ['f', 'l', 'w']],     [['r', 'x', 'b'], ['m', 'e', 'p']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 1]}')

print (f'{Array3[1, 0, ::2]}')
print (f'{Array3[1, 1, ::3]}')
print (f'{Array3[0, 1, :2]}')
print (f'{Array3[0, 1, 2:]}')
print (f'{Array3[0, :, 2]}')
print (f'{Array3[1, 1, 2:3]}')
print (f'{Array3[0, 0, 0:None]}')
print (f'{Array3[0, 0, :]}')
print (f'{Array3[Array3 == "b"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],      [[[6, 5, 4], [9, 8, 7]], [[0, 5, 9], [7, 3, 1]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 0]}')

print (f'{Array4[0, 1, 1, ::2]}')
print (f'{Array4[0, 1, 1, ::3]}')
print (f'{Array4[0, 0, 1, 2:]}')
print (f'{Array4[0, 0, 1, :2]}')
print (f'{Array4[1, 0, :, 2]}')
print (f'{Array4[1, 1, 0, 2:3]}')
print (f'{Array4[0, 1, 0, 0:None]}')
print (f'{Array4[0, 1, 0, :]}')
print (f'{Array4[Array4 >= 2]}')

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

Array_Num1 = np.arange(start=1, stop=6, step=1) #type: ignore

print (f'{Array_Num1}')

Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El menor de los numeros es {Array_Num1_Min}')
print (f'El mayor de los numeros es {Array_Num1_Max}')

print (f'-' * 20)

Array_Num2 = np.arange(start=1, stop=26, step=1) #type: ignore

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

Array_Num2_Reshape_Column_Min = np.min(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Column_Max = np.max(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Row_Min = np.min(Array_Num2_Reshape, axis=1)
Array_Num2_Reshape_Row_Max = np.max(Array_Num2_Reshape, axis=1)

print (f'Los menores de la columna son {Array_Num2_Reshape_Column_Min}')
print (f'Los mayores de la columna son {Array_Num2_Reshape_Column_Max}')
print (f'Los menores de la filas son {Array_Num2_Reshape_Row_Min}')
print (f'Los mayores de la filas son {Array_Num2_Reshape_Row_Max}')

print (f'-' * 20)

Array_Zero = np.zeros(shape=(2, 3))

print (f'{Array_Zero}')
print (f'{Array_Zero.ndim}')
print (f'{Array_Zero.shape}')
print (f'{Array_Zero.size}')
print (f'{Array_Zero.dtype}')
print (f'{Array_Zero[0, 2]}')

print (f'-' * 20)

Array_One = np.ones(shape=(2, 3))

print (f'{Array_One}')
print (f'{Array_One.ndim}')
print (f'{Array_One.shape}')
print (f'{Array_One.size}')
print (f'{Array_One.dtype}')
print (f'{Array_One[0, 2:3]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value=f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 2]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value='FUECOCO')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[3]}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value=Array4[1, 0, 0, 2])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[0, 2]}')

print (f'-' * 20)

Tupla_Array = tuple(('Rojo', 'Verde'))
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value = Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value = Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value = Diccionario_Array['Nombre'][2])

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
Sumita11 = np.sum(Array_Random2_Sorted)
Sumita12 = np.sum(Array_Random2_Sorted)

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

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

Array_Num8 = np.arange(start=1, stop=21, step=1) #type: ignore

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Array_Num9 = np.arange(start=1, stop=11, step=1) #type: ignore

print (f'{Array_Num9}')

Lista_Array1 = []

for elemento in Array_Num9:
    Lista_Array1.append(int(elemento))
    
print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array5 = np.array([1, 2, 3])
Array6 = np.arange(start=4, stop=7, step=1) #type: ignore

Array_Concatenate = np.concat([Array5, Array6])

print (f'{Array_Concatenate}')

Array_Concatenate_Split1 = np.split(Array_Concatenate, 3)
Array_Concatenate_Split2 = np.split(Array_Concatenate, 2)
Array_Concatenate_Split3 = np.split(Array_Concatenate, 1)
Array_Concatenate_Split4 = np.split(Array_Concatenate, 6)

print (f'{Array_Concatenate_Split1[0]}')
print (f'{Array_Concatenate_Split1[1]}')
print (f'{Array_Concatenate_Split1[2]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Split2[0]}')
print (f'{Array_Concatenate_Split2[1]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Split3[0]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Split4[0]}')
print (f'{Array_Concatenate_Split4[1]}')
print (f'{Array_Concatenate_Split4[2]}')
print (f'{Array_Concatenate_Split4[3]}')
print (f'{Array_Concatenate_Split4[4]}')
print (f'{Array_Concatenate_Split4[5]}')

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

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

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

Array_Random3_Sorted = np.sort(Array_Random3)
Array_Random3_Sorted_Mean = np.mean(Array_Random3_Sorted)
Array_Random3_Sorted_Sum = np.sum(Array_Random3_Sorted)

print (f'Acomodado: {Array_Random3_Sorted}')
print (f'Media: {round(Array_Random3_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random3_Sorted_Sum}')

Sumita13 = np.sum(Array_Random3_Sorted, axis=0)
Sumita14 = np.sum(Array_Random3_Sorted, axis=1)
Sumita15 = np.sum(Array_Random3_Sorted[1, 0, 0:None])
Sumita16 = np.sum(Array_Random3_Sorted[1, 0, :])

print (f'El resultado de la sumita es {Sumita13}')
print (f'El resultado de la sumita es {Sumita14}')
print (f'El resultado de la sumita es {Sumita15}')
print (f'El resultado de la sumita es {Sumita16}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

Set_Conjunto_Csv3 = set(Cargar_Csv3['product'])

print (f'{Set_Conjunto_Csv3}')

Lista_Csv3 = list(Set_Conjunto_Csv3)

Ganador1 = np.random.choice(Lista_Csv3, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Csv3, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Csv3, size=(2, 3), replace=False)

print (f'El producto ganador es {Ganador1}')
print (f'El producto ganador es {Ganador2}')
print (f'El producto ganador es {Ganador3}')

print (f'-' * 20)

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-' * 20)

'''import requests

URL1 = 'http://127.0.0.1:8001/elemento2'

Diccionario = {
    'Dragon_Id' : 658952,
    'Dragon_Name' : "Jourin"
}

Agregado1 = requests.post(URL1, json=(Diccionario))
Agregado2 = Agregado1.json()

print (f'{Agregado2}')

print (f'-' * 20)

import requests

URL2 = 'http://127.0.0.1:8001/elemento'

Resultado = requests.get(URL2)

Datos = Resultado.json()

print (f'El nombre del dragon es {Datos["Resultado"][0]["Dragon_Name"]}')

print (f'-' * 20)

import requests

var13 = 7

Resultado2 = requests.get(f'http://127.0.0.1:8001/elemento3/{var13}')

Datos2 = Resultado2.json()

print (f'Vamos a hacer una operacion con los elementos {Objeto9.Cantidad + Datos2["Numerito"]}')'''

class Persona4():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto35 = Persona4('Erick Perez')

print (f'Hola, mi nombre es {Objeto35}')

print (f'-' * 20)


class Colores4():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre
        
Lista_Colores4 = list([
    Colores4('Azul'),
    Colores4('Magenta'),
    Colores4('Cian'),
    Colores4('Morado'),
    Colores4('Negro'),
    Colores4('Celeste')
])

print (f'Los elementos de la lista son {Lista_Colores4}')

print (f'-' * 20)

class Inventario4():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto36 = Inventario4()

Objeto36.Productos.append('Chocolate')
Objeto36.Productos.insert(1, 'Fresa')
Objeto36.Productos.extend(['Caramelo'])

print (f'La cantidad de elementos de la lista son {len(Objeto36)}')

print (f'-' * 20)

class Igualdad4:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto37 = Igualdad4('Panda')
Objeto38 = Igualdad4('Panda')

print (f'{Objeto37 == Objeto38}')

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
            yield f'El numero {elemento} es par'
        else:
            yield f'El numero {elemento} es impar'

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

Lista_Contador = [1, 2, 3, 4, 5]

def Counter(Lista):
    Counter = 0
    for elemento in Lista:
        Counter += elemento
        
    print (f'La suma de los elementos de la lista es {Counter}')

Counter(Lista_Contador)

print (f'-' * 20)

Lista_Contador2 = list([1, 2, 3, 4, 5])

def Counter2(Lista):
    Pare = 0
    for elemento in Lista:
        if (elemento % 2 == 0):
            Pare += elemento
        else:
            continue
        
    print (f'La suma de los elementos pares es {Pare}')

Counter2(Lista_Contador2)

print (f'-' * 20)

def Counter3(Lista):
    Impare = 0
    Any_Impar = any(num % 2 != 0 for num in Lista)
    Anonima0 = filter(lambda Num : Num % 2 != 0, Lista)
    Lista_Impar = [num for num in Lista if num % 2 != 0]
    
    if (Any_Impar == True):
        print (f'Impares: {list(Anonima0)}')
        print (f'Impares: {Lista_Impar}')
        
        for elemento in Lista_Impar:
            Impare += elemento
            
        print (f'La suma de los elementos impares de la lista es {Impare}')
    else:
        print (f'Error, no hay elementos impares en la lista')

Counter3(Lista_Contador2)

def Ubicado(Lista, Numero):
    Found = False

    for elemento in Lista:
        if (elemento == Numero):
            Found = True
            break
        else:
            continue
        
    return Found

if (Ubicado(Lista_Contador, 5) == True):
    print (f'EL NUMERO FUE ENCONTRADO')
else:
    print (f'EL NUMERO NO FUE ENCONTRADO')
    
print (f'-' * 20)

def Evaluado(Lista):
    Min = min(Lista)
    Max = max(Lista)
    
    Resultado = [Min, Max]
    return Resultado

print (f'Los numeros resultado son {Evaluado(Lista_Contador)}')

print (f'-' * 20)

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1:int) -> int:
    def Sumatoria_Interna(Num2):
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
    
print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(22)}')
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.5, 200, False)

print (f'{Funcion_Tupla("Perro", 3.5, 200, False)}')
print (f'{Variable_Funcion_Tupla[2]}')
print (f'{Funcion_Tupla("Perro", 3.5, 200, False)[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.5, 200, False))}')

print (f'-' * 20)

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs:
        print (f'{kwargs[elemento]}')
        
    print (f'-' * 20)
    
    for elemento in kwargs.keys():
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    for elemento in kwargs.values():
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')
        
Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Objeto9.Cantidad, Votante = Variable_Funcion_Tupla[3])

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos(Saludar_Dos(), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 2)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')
print (f'Los numeros pares de la lista son {list(Anonima3)}')
print (f'Los numeros pares de la lista son {PEPE.Lista_Numeros}')
print (f'{PEPE.Any_Par}')
print (f'Los numeros pares de la lista son {list(PEPE.Anonima4)}')

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
        return f'{Nombre} {Apellido}'
    
    return Interna('PEREZ GUTIERREZ')

print (f'{Externa('ERICK JOSUE')}')

def Closure_Externo():
    Lista_Closure = []
    def Closure_Interno(x):
        Lista_Closure.extend([x])
        return Lista_Closure
    
    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(26)}')
print (f'{Variable_Closure(39)}')

print (f'-' * 20)

def Closure_Crear_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y

    return Closure_Multiplicador

Var_Mult1 = Closure_Crear_Multiplicador(3)
Var_Mult2 = Closure_Crear_Multiplicador(4)

print (f'El multiplicador es {Var_Mult1(10)}')
print (f'El multiplicador es {Var_Mult2(10)}')

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'ZZZZ')
        Segunda()
        print (f'XXXX')
        
    return Tercera

@Primera
def Saludar3():
    print (f'Hola Mundo')
    
Saludar3()

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 19
        
    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(12, 7)}')

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonatha'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)
        
    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    print (f'Mi nombre es {Nombre} {Apellido}')
    
Usuario2('Erick', 'Perez')

class Persona5():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto39 = Persona5('Erick Josue')

print (f'Hola, mi nombre es {Objeto39}')

print (f'-' * 20)

class Colores5:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Colores5 = list([
    Colores5('Rojo'),
    Colores5('Negro'),
    Colores5('Naranja'),
    Colores5('Rosado'),
    Colores5('Gris')
])

print (f'La lista de colores es {Lista_Colores5}')

print (f'-' * 20)

class Inventario5:
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto40 = Inventario5()

Objeto40.Productos.append('Perro')
Objeto40.Productos.insert(1, 'Gato')
Objeto40.Productos.extend(['Raton'])

print (f'La cantidad de elementos en la lista es {len(Objeto40)}')

print (f'-' * 20)

class Igualdad5():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto41 = Igualdad5('Azul')
Objeto42 = Igualdad5('Azul')

print (f'{Objeto41 == Objeto42}')

print (f'-' * 20)

'''import requests

Resultado1 = requests.get('http://127.0.0.1:8004/')

Datos1 = Resultado1.json()

print (f'{Datos1["Texto"]}')

print (f'-' * 20)

import requests

var13 = 7

Resultado2 = requests.get(f'http://127.0.0.1:8004/elemento1/{var13}')

Datos2 = Resultado2.json()

print (f'Hola, mi numero favorito es {Datos2["Numerito"]} y el doble de este numero es {Anonima2(Datos2["Numerito"])}')

print (f'-' * 20)

import requests

URL1 = 'http://127.0.0.1:8004/elemento2'
URL2 = 'http://127.0.0.1:8004/elemento3'

Diccionario_Api = {
    'Dino_Id' : 519,
    'Dino_Name' : "Tiranosaurius Rex",
    'Country' : "United States"
}

Agregado1 = requests.post(URL1, json=(Diccionario_Api))
Agregado2 = Agregado1.json()

print (f'{Agregado2}')

Resultado3 = requests.get(URL2)

Datos3 = Resultado3.json()

print (f'Mi dino favorito es {Datos3["Elementos"][0]["Dino_Name"]}')'''

from Module_Own import Pokemon2 as Poke2

Objeto43 = Poke2(PEPE.Diccionario_Poke["Poke1"], 'Electrico', 'Impact Trueno')
Objeto44 = Poke2(PEPE.Diccionario_Poke["Poke2"], 'Roca', 'Sismo')

Objeto43.Mostrar()

print (f'-' * 20)

Objeto44.Mostrar()

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto45 = Poke_Kid2(PEPE.Diccionario_Poke["Poke3"], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto45)
Objeto45.Mostrar()

print (f'-' * 20)

class Camara2():
    def Tomar_Fotografia(self):
        print (f'La Fotografia fue tomada')
        
class Reproductor_Musica2():
    def Reproducir_Musica(self):
        print (f'La Musica fue reproducida')
        
class Smartphone2(Camara2, Reproductor_Musica2):
    def Encender_Smartphone(self):
        print (f'El Smartphone fue encendido')
        
Objeto46 = Smartphone2()

Objeto46.Encender_Smartphone()
Objeto46.Reproducir_Musica()
Objeto46.Tomar_Fotografia()

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

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto47 = Perro2('Chester', 5, 2.8, 'Poodle', 'Asma De Perro')
Objeto48 = Perro2('Messi', 1.5, 2, 'Gris', 'No')
Objeto49 = Perro2('Polly', 35, 0.4, 'Cacatua Amarilla', 'Si')

Veterinaria2.Mostrar(Objeto47)
Objeto47.Mostrar()

print (f'-' * 20)

Veterinaria2.Mostrar(Objeto48)
Objeto48.Mostrar()

print (f'-' * 20)

Veterinaria2.Mostrar(Objeto49)
Objeto49.Mostrar()

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
        
Objeto50 = Paladin2(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto50.Mostrar()
Atacante2.Mostrar(Objeto50)
Defensor2.Mostrar(Objeto50)

print (f'-' * 20)

Hija_Padre1 = issubclass(Poke_Kid2, Poke2)
Hija_Padre2 = issubclass(Poke_Kid2, Poke1)

print (f'{Hija_Padre1}')
print (f'{Hija_Padre2}')

print (f'-' * 20)

Instancia1 = isinstance(Objeto50, Paladin2)
Instancia2 = isinstance(Objeto50, Atacante2)
Instancia3 = isinstance(Objeto50, Defensor2)
Instancia4 = isinstance(Objeto50, Defensor1)

print (f'{Instancia1}')
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
        
Objeto51 = D2()

A2.Mostrar(Objeto51)
B2.Mostrar(Objeto51)
C2.Mostrar(Objeto51)
Objeto51.Mostrar()
E2.Mostrar(Objeto51)

print (f'-' * 20)

class Efectivo2():
    def Pagar(self):
        print (f'El pago se realizo en Efectivo')
        
class Tarjeta2():
    def Pagar(self):
        print (f'El pago se realizo en Tarjeta')
        
class Cripto2():
    def Pagar(self):
        print (f'El pago se realizo en Cripto')
        
Objeto52 = Cripto2()
Objeto53 = Tarjeta2()
Objeto54 = Efectivo2()

Objeto52.Pagar()
Objeto53.Pagar()
Objeto54.Pagar()

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
        
Objeto54 = Cuenta_Bancaria2(100)
Objeto54.Depositar(25)
Objeto54.Mostrar()

print (f'Este es el dinero que actualmente se encuentra privado en una variable encriptada {Objeto54.Dinero}')

Objeto54.Dinero = '50,000,000'

Objeto54.Mostrar()

print (f'Este es el dinero que actualmente se encuentra privado en una variable encriptada {Objeto54.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla2(Plantilla2):
    def Mostrar(self):
        print (f'Esto es un mensaje directo de la clase sub_plantilla')
        
    def General(self):
        print (f'Este metodo es obligatorio y pertenece a la plantilla2')
        
Objeto55 = Sub_Plantilla2()

Objeto55.Mostrar()
Objeto55.General()

print (f'-' * 20)

class Chocolate2():
    def Elegir(self):
        return f'Chocolate'
    
class Vainilla2():
    def Elegir(self):
        return f'Vainilla'
    
class Fresa2():
    def Elegir(self):
        return f'Fresa'
    
class Pastel3():
    def __init__(self):
        self.Favorito = Chocolate2()
        
    def Hornear(self):
        print (f'Que te parece si horneamos un pastel de {self.Favorito.Elegir()}?')
        
Objeto56 = Pastel3()

Objeto56.Hornear()

print (f'-' * 20)

class Pastel4:
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Que te parece si horneamos un pastel de {self.Favorito.Elegir()}')
        
Sabor4 = Chocolate2()
Objeto57 = Pastel4(Sabor4)
Objeto57.Hornear()

Sabor5 = Vainilla2()
Objeto58 = Pastel4(Sabor5)
Objeto58.Hornear()

Sabor6 = Fresa2()
Objeto59 = Pastel4(Sabor6)
Objeto59.Hornear()

print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Una
Variable
Long
String'''

variable4 = Objeto10.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = Objeto11.Catched, True

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke3"]}')

print (f'Mi nombres es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene actualmente {Variable_Sumatoria}, {Sumatoria2(1, 2, 3, 2)} o incluso {Objeto11.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'-' * 20)

print (f'Erick' in Lista_Uno)
print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Ash")]}' not in PEPE.Tupla_Poke)
print (f'{Objeto11.Nombre}' in PEPE.Set_Conjunto1)

print (f'-' * 20)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables y al mismo tiempo es una declaracion snake case {snake_case3}')

print (f'La lista 1 tiene actualmente {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene actualmente {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto9.Cantidad, Sumatoria2(1, 2, 2, 2))

print (f'El Cociente de la operacion es {Cociente}')
print (f'El Residuo de la operacion es {Residuo}')

print (f'{PEPE.Lista2[::2]}')
print (f'{PEPE.Lista2[::3]}')
print (f'{PEPE.Lista2[:2]}')
print (f'{PEPE.Lista2[2:]}')
print (f'{PEPE.Lista2[2:3]}')
print (f'{PEPE.Lista2[0:None]}')
print (f'{PEPE.Lista2[:]}')

print (f'{Lista_Uno[1]}, eso que ves ahi es un {PEPE.Lista2[2]}?')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, 200, 100)

print (f'{Lista_Cuatro}')

del Lista_Uno[1]
Lista_Uno.remove('Coco Rayado')
Lista_Uno.pop(-2)
Lista_Uno.pop(-1)
Lista_Uno.pop(-1)

print (f'{Lista_Uno}')
print (f'La lista 1 tiene actualmente {len(Lista_Uno)} elementos')

Lista_Uno_Copia = Lista_Uno.copy()

Lista_Uno.clear()

print (f'{Lista_Uno}')
print (f'{Lista_Uno_Copia}')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')

print (f'{dir(PEPE)}')

Tupla1 = ('Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde')

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Green', 'Blue'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Variable_Funcion_Tupla)}')

print (f'{Tupla1[2]}')

Set_Conjunto1 = {'Casa', 'Pared', 'Puerta'}
Set_Conjunto1.add('Patio')
Set_Conjunto2 = set({'Triciclo'})

Set_Conjunto1.update(Set_Conjunto2)

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'House', 'Wall', 'Door', 'Yard'})

print (f'{Set_Conjunto1}')

Set_Conjunto1 = {1, 2, 3, 4, 5}
Set_Conjunto2 = {4, 5}
Set_Conjunto3 = set({8})

print (f'{Set_Conjunto1.issuperset(Set_Conjunto2)}')
print (f'{Set_Conjunto1 >= Set_Conjunto2}')
print (f'-' * 20)

print (f'{Set_Conjunto2.issubset(Set_Conjunto1)}')
print (f'{Set_Conjunto2 <= Set_Conjunto1}')
print (f'-' * 20)

print (f'{Set_Conjunto1.isdisjoint(Set_Conjunto3)}')

print (f'-' * 20)

Set_Conjunto_A2 = {1, 2, 3, 4}
Set_Conjunto_B2 = {3, 4, 5, 6}

print (f'{Set_Conjunto_A2.union(Set_Conjunto_B2)}')
print (f'{Set_Conjunto_A2 | Set_Conjunto_B2}')

print (f'-' * 20)

print (f'{Set_Conjunto_A2.intersection(Set_Conjunto_B2)}')
print (f'{Set_Conjunto_A2 & Set_Conjunto_B2}')

print (f'-' * 20)

print (f'{Set_Conjunto_A2.difference(Set_Conjunto_B2)}')
print (f'{Set_Conjunto_A2 - Set_Conjunto_B2}')

print (f'-' * 20)

print (f'{Set_Conjunto_B2.difference(Set_Conjunto_A2)}')
print (f'{Set_Conjunto_B2 - Set_Conjunto_A2}')

print (f'-' * 20)

print (f'{Set_Conjunto_A2.symmetric_difference(Set_Conjunto_B2)}')
print (f'{Set_Conjunto_A2 ^ Set_Conjunto_B2}')

print (f'-' * 20)

'''Set_Conjunto_A2.update(Set_Conjunto_B2)

print (f'{Set_Conjunto_A2}')'''

'''Set_Conjunto_A2.intersection_update(Set_Conjunto_B2)

print (f'{Set_Conjunto_A2}')'''

'''Set_Conjunto_A2.difference_update(Set_Conjunto_B2)

print (f'{Set_Conjunto_A2}')'''

'''Set_Conjunto_B2.difference_update(Set_Conjunto_A2)

print (f'{Set_Conjunto_B2}')'''

'''Set_Conjunto_A2.symmetric_difference_update(Set_Conjunto_B2)

print (f'{Set_Conjunto_A2}')'''

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})

Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, 'ChocoFresa'})

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

print (f'-' * 20)

Diccionario3 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Objeto9.Cantidad,
    'Votante' : Variable_Funcion_Tupla[3]
}

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3.values()}')
print (f'{Diccionario3.items()}')
print (f'{Diccionario3["Nombre"]}')
print (f'{Diccionario3.get("Edad")}')

print (f'-' * 20)

Diccionario4 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, Anonima2(10), 6],
    'Votante' : [True, not False, False]
}

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Nombre"][2]}')
print (f'{Diccionario4.get("Edad")[1]}') #type: ignore

print (f'-' * 20)

Diccionario5 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Ingresos"]}')
print (f'{Diccionario5.get("Gastos")}')

print (f'-' * 20)

Diccionario3['Nombre'] = Lista_Uno_Copia[2]

print (f'{Diccionario3}')

del Diccionario3['Nombre']
Diccionario3.pop('Edad')

print (f'{Diccionario3}')

Diccionario3_Copia = Diccionario3.copy()

Diccionario3.clear()

print (f'{Diccionario3}')
print (f'{Diccionario3_Copia}')

print (f'-' * 20)

Diccionario3 = dict({1 : "Karlita", 2 : 6, 3 : not True})

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3.values()}')
print (f'{Diccionario3.items()}')
print (f'{Diccionario3[1]}')
print (f'{Diccionario3.get(2)}')

print (f'-' * 20)

print (f'{Diccionario3.get(1)} no puede votar ya que solo tiene {Diccionario4["Edad"][2]} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', "Hola")
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = Objeto11.Nombre

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio1.keys()}')
print (f'{Diccionario_Vacio1.values()}')
print (f'{Diccionario_Vacio1.items()}')
print (f'{Diccionario_Vacio1["A"]}')
print (f'{Diccionario_Vacio1.get("B")}')

print (f'-' * 20)

print (f'{Diccionario_Vacio2}')
print (f'{Diccionario_Vacio2.keys()}')
print (f'{Diccionario_Vacio2.values()}')
print (f'{Diccionario_Vacio2.items()}')
print (f'{Diccionario_Vacio2["Dos"]}')
print (f'{Diccionario_Vacio2.get("Uno")}')

print (f'-' * 20)

Lista_Contador3 = list([1, 2, 3, 4, 5])

def Contador3(Lista):
    Cuenta1 = 0
    for elemento in Lista:
        Cuenta1 += elemento
        
    return Cuenta1

print (f'Si sumo todos los elementos de la lista me da el numero {Contador3(Lista_Contador3)}')

print (f'-' * 20)

def Contador4(Lista):
    Even = 0
    for elemento in Lista:
        if (elemento % 2 == 0):
            Even += elemento
        else:
            continue
        
    return Even

print (f'Si sumo todos los elementos pares de la lista {Contador4(Lista_Contador3)}')

print (f'-' * 20)

def Contador5(Lista):
    Cuenta2 = 0
    for elemento in Lista:
        Cuenta2 += 1
        
    return Cuenta2

print (f'La cantidad de elementos de la lista es {Contador5(Lista_Contador3)}')

print (f'-' * 20)

def Contador6(Lista, Numero):
    Encontrado = False
    for elemento in Lista:
        if (elemento == Numero):
            Encontrado = True
            break
        else:
            continue
        
    return Encontrado

if (Contador6(Lista_Contador3, 2) == True):
    print (f'El numero fue encontrado')
else:
    print (f'Error, el numero no fue encontrado')

print (f'-' * 20)

def contar_mayores(lista, numero):
    mayore = 0
    for elemento in lista:
        if (elemento > numero):
            mayore += 1
        else:
            continue
        
    return mayore

print (f'La cantidad de numeros en la lista que son mayores a 20 son: {contar_mayores([], 30)}')

def obtener_pares(Lista):
    Nueva_Lista = []
    for elemento in Lista:
        if (elemento % 2 == 0):
            Nueva_Lista.append(elemento)
            
    return Nueva_Lista

print (f'La lista de numeros pares es {obtener_pares([])}')

print (f'-' * 20)

def duplicar_numeros(Lista):
    Lista_Mult = []
    for elemento in Lista:
        Lista_Mult.append(elemento * 2)
        
    return Lista_Mult

print (f'La lista resultado es {duplicar_numeros([3, 7, 10])}')

Lista_Contador4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Contable(Lista):
    Contador = 0
    for elemento in Lista:
        Contador += 1
        
    return Contador

print (f'Recorrimos toda la lista y al final encontramos {Contable(Lista_Contador4)} elementos')

print (f'-' * 20)

def Evaluador(Lista):
    Any_Par = any(num % 2 == 0 for num in Lista)
    Anonima4 = filter(lambda Num : Num % 2 == 0, Lista)
    Lista_Pares = [num for num in Lista if num % 2 == 0]
    if (Any_Par == True):
        Conta_Par = 0
        
        print (f'{list(Anonima4)}')
        print (f'{Lista_Pares}')
        
        for elemento in Lista_Pares:
            Conta_Par += elemento
            
        print (f'La suma de los numeros pares de la lista es {Conta_Par}')
    else:
        print (f'Error, no hay elementos pares en la lista')

Evaluador(Lista_Contador4)

print (f'-' * 20)

def Evaluador2(Lista):
    Conta_Par = 0
    
    for elemento in Lista:
        if (elemento % 2 != 0):
            Conta_Par += elemento
        else:
            continue
        
    return Conta_Par

print (f'La suma de todos los numeros impares es {Evaluador2(Lista_Contador4)}')

print (f'-' * 20)

def Sumatoria4(Lista):
    Contador = 0
    for elemento in Lista:
        Contador += elemento
        
    return Contador

print (f'El resultado de sumar todos los numeros de la lista es {Sumatoria4(Lista_Contador4)}')

print (f'-' * 20)

def Buscador1(Lista, Numero):
    Ubicado = False
    for elemento in Lista:
        if (elemento == Numero):
            Ubicado = True
            break
        else:
            continue
        
    return Ubicado

if (Buscador1(Lista_Contador4, 19) == True):
    print (f'El numero fue encontrado')
else:
    print (f'Error, el numero no fue encontrado')
    
print (f'-' * 20)

def Buscador2(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    Lista_Resultado = [Menore, Mayore]
    
    return Lista_Resultado

print (f'{Buscador2(Lista_Contador4)}')

print (f'El menor de los numeros de la lista es {min(Buscador2(Lista_Contador4))}')
print (f'El mayor de los numeros de la lista es {max(Buscador2(Lista_Contador4))}')

print (f'-' * 20)

def Buscador3(Lista, Numero):
    Contador = 0
    for elemento in Lista:
        if (elemento > Numero):
            Contador += 1
        else:
            continue
        
    return Contador

print (f'La cantidad de numeros que son mayores a 8 en la lista es {Buscador3(Lista_Contador4, 8)}')

def Buscador4(Lista):
    Nueva_Lista = []
    for elemento in Lista:
        if (elemento % 2 == 0):
            Nueva_Lista.append(elemento)
        else:
            continue
        
    return Nueva_Lista

print (f'Sacamos solo los elementos pares de la lista original: {Buscador4(Lista_Contador4)}')

print (f'-' * 20)

def Buscador5(Lista):
    Lista_Mult = list([])
    for elemento in Lista:
        Lista_Mult.append(elemento * 2)
        
    return Lista_Mult

print (f'Lista Original {Lista_Contador4}')
print (f'Lista Actualizada: {Buscador5(Lista_Contador4)}')

print (f'-' * 20)

'''def Evaluacion1():
    Lista_Notas = list([])
    Contador = 0
    while (Contador < 3):
        while True:
            Numerito6 = input(f'Ingrese el numero {Contador}: ')
            try:
                Numerito7 = float(Numerito6)
                if (Numerito7.is_integer()):
                    Lista_Notas.append(Numerito7)
                    break
                else:
                    Lista_Notas.append(Numerito7)
                    break
            except ValueError:
                print (f'Error, lo ingresado no es un numero, intente nuevamente!')
        Contador += 1
    
    Promedio4 = sum(Lista_Notas) / len(Lista_Notas)
    print (f'El promedio de las notas es {round(Promedio4, 2)}')

Notas = Evaluacion1()'''

class Persona6():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto60 = Persona6('Erick Perez')

print (f'Mi nombre es {Objeto60}')

print (f'-' * 20)

class Colores6():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Colores6 = list([
    Colores6('Blue'),
    Colores6('Green'),
    Colores6('Gray'),
    Colores6('White'),
    Colores6('Yellow')
])

print (f'Los elementos de la lista son {Lista_Colores6}')

print (f'-' * 20)

class Inventario6():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto61 = Inventario6()

Objeto61.Productos.append('Pastel')
Objeto61.Productos.insert(1, 'Helado')
Objeto61.Productos.extend(['Hamburguesa'])

print (f'La cuenta de elementos de la lista es {len(Objeto61)}')

print (f'-' * 20)

class Igualdad6():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto62 = Igualdad6('Perro')
Objeto63 = Igualdad6('Perro')

print (f'{Objeto62 == Objeto63}')

print (f'-' * 20)

'''import requests

Resultado1 = requests.get('http://127.0.0.1:8005/')

Datos1 = Resultado1.json()

print (f'{Datos1["Resultado"]}')

print (f'-' * 20)

import requests

Resultado2 = requests.get('http://127.0.0.1:8005/grupo1/elemento1/')

Datos2 = Resultado2.json()

print (f'La lista de elementos es {Datos2["Elementos"]}')

print (f'-' * 20)

import requests

var13 = 'ChocoCoco'

URL1 = f'http://127.0.0.1:8005/grupo1/elemento1/{var13}'

Agregado1 = requests.post(URL1, json=(var13))
Agregado2 = Agregado1.json()

print (f'{Agregado2}')

import requests

sabores = [
    "Chocolate",
    "Fresa"
]

respuesta = requests.post("http://127.0.0.1:8005/grupo1/elementos", json=(sabores)) #type: ignore

print(respuesta.json())

var14 = 0
var15 = 'Cas Con Siracha'

Reemplazado1 = requests.put(f'http://127.0.0.1:8005/grupo1/elemento1/?Indice={var14}&Nuevo_Sabor={var15}')
Reemplazado2 = Reemplazado1.json()

print (f'{Reemplazado2}')

var16 = 0

Eliminado1 = requests.delete('http://127.0.0.1:8005/grupo1/elemento1')
Eliminado2 = Eliminado1.json()

print (f'{Eliminado2}')

Resultado3 = requests.get('http://127.0.0.1:8005/grupo1/elemento1/')

Datos3 = Resultado3.json()

print (f'Mi sabor favorito es {Datos3["Elementos"]}')'''

'''import requests

Lista_Elementos = [
    'Caramelo',
    'Fresa',
    'CocoMenta'
]

Agregado1 = requests.post('http://127.0.0.1:8005/grupo2/elemento1', json=(Lista_Elementos)) #type: ignore
Agregado2 = Agregado1.json()

print (f'{Agregado2}')

Resultado1 = requests.get('http://127.0.0.1:8005/grupo2/elemento1')
Resultado2 = Resultado1.json()

print (f'{Resultado2["Elementos"]}')'''

Key3 = [f'Key{i}' for i in range(len(Lista_Uno_Copia))]

Diccionario6 = dict(zip(Key3, Lista_Uno_Copia))

print (f'{Diccionario6}')
print (f'{Diccionario6.keys()}')
print (f'{Diccionario6.values()}')
print (f'{Diccionario6.items()}')
print (f'{Diccionario6["Key2"]}')
print (f'{Diccionario6.get("Key3")}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv4 = 'C:\\Repo\\Store.csv'

Cargar_Csv4 = pd.read_csv(Ruta_Csv4)

print (f'{Cargar_Csv4}')

Set_Conjunto_Csv4 = set(Cargar_Csv4['product'])

print (f'{Set_Conjunto_Csv4}')

Key4 = [f'Key_{i}' for i in range(len(Set_Conjunto_Csv4))]

Diccionario7 = dict(zip(Key4, Set_Conjunto_Csv4))

print (f'{Diccionario7}')
print (f'{Diccionario7.keys()}')
print (f'{Diccionario7.values()}')
print (f'{Diccionario7.items()}')
print (f'{Diccionario7["Key_3"]}')
print (f'{Diccionario7.get("Key_5")}')

print (f'-' * 20)

print (f'{Cargar_Csv4}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Fecha4 = '2026-04-01'

try:
    Fech4 = datetime.strptime(Fecha4, '%Y-%m-%d').date()
    Fech4_Formateada = pd.to_datetime(Fech4)
    Cargar_Csv4['date'] = pd.to_datetime(Cargar_Csv4['date'])
except ValueError:
    print (f'Error, el formato de la fecha es incorrecto')
    exit()
    
Cargar_Csv4['TOTALITO'] = Cargar_Csv4['quantity'] * Cargar_Csv4['price']
    
Encontrada4 = Cargar_Csv4[Cargar_Csv4['date'].dt.date == Fech4_Formateada.date()]

if (Encontrada4.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! hemos encontrado ventas en esta fecha')
    
    Grupo6 = Encontrada4.groupby('product')['quantity'].sum()
    Grupo6_Min = Grupo6.idxmin()
    Grupo6_Max = Grupo6.idxmax()
    Grupo6_Min_Cant = Grupo6.min()
    Grupo6_Max_Cant = Grupo6.max()
    
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo6_Min} vendio un total de {Grupo6_Min_Cant} unidades')
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo6_Max} vendio un total de {Grupo6_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron en esta fecha fue de {Grupo6.count()}')
    print (f'La cantidad de productos vendidos en esta fecha fue de {Grupo6.sum()}')
    
    Grupo7 = Encontrada4.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero que se vendio en esta fecha fue ${Grupo7.sum()}')
    
    Promedio4 = Grupo7.sum() / Grupo6.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio4, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${Grupo7.mean()}')
    
print (f'-' * 20)

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'El tipo de dato de la variable es {type(variable1)}')
print (f'El tipo de dato de la variable es {type(variable4)}')
print (f'El tipo de dato de la variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de dato de la variable es {type(variable7)}')
print (f'El tipo de dato de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato de la variable es {type(Tupla1)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto2)}')
print (f'El tipo de dato de la variable es {type(Diccionario3_Copia)}')
print (f'El tipo de dato de la variable es {type(Funcion_Diccionario)}')
print (f'El tipo de dato de la variable es {type(Objeto15)}')
print (f'El tipo de dato de la variable es {type(Data_Frame_Concatenate)}')
print (f'El tipo de dato de la variable es {type(Array2_Sorted_Mean)}')
print (f'El tipo de dato de la variable es {type(PEPE)}')

if (Diccionario5['Ingresos'] > 500): #type: ignore
    if (Diccionario5['Gastos'] < 200): #type: ignore
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario5['Gastos'] == 200): #type: ignore
        print (f'Ingresos Altos, Gastos Al Limite')
    elif (Diccionario5['Gastos'] > 200): #type: ignore
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario5['Ingresos'] == 500): #type: ignore
    if (Diccionario5['Gastos'] < 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario5['Gastos'] == 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Al Limite')
    elif (Diccionario5['Gastos'] > 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario5['Ingresos'] < 500): #type: ignore
    if (Diccionario5['Gastos'] < 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario5['Gastos'] == 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Al Limite')
    elif (Diccionario5['Gastos'] > 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')
    
Lista_Contador5 = [1, 2, 3, 4, 5]

def Ejecutable1(Lista):
    Contador = 0
    for elemento in Lista:
        Contador += 1
        
    return Contador

print (f'La lista elegida tiene {Ejecutable1(Lista_Contador5)} elementos')

def Ejecutable2(Lista):
    Contador = 0
    for elemento in Lista:
        if (elemento % 2 == 0):
            Contador += elemento
        else:
            continue
        
    return Contador

print (f'Si tomo todos los elementos pares de la lista y los sumo, me da el numero {Ejecutable2(Lista_Contador5)}')

def Ejecutable3(Lista):
    Contador = 0
    for elemento in Lista:
        Contador += elemento
        
    return Contador

print (f'Si tomo todos los elementos de la lista y los sumo, me da el numero {Ejecutable3(Lista_Contador5)}')

'''def Ejecutable4(Lista, Numero):
    Validador = False
    for elemento in Lista:
        if (elemento == Numero):
            Validador = True
            break
        else:
            continue
        
    return Validador

while True:
    Numerito6 = input(f'Ingrese un numero: ')
    try:
        Numerito7 = float(Numerito6)
        if (Numerito7.is_integer()):
            if (Ejecutable4(Lista_Contador5, Numerito7) == True):
                print (f'Felicidades el numero fue encontrado')
            else:
                print (f'Error, el numero que elegiste no existe en la lista')
            break
        else:
            print (f'Error, necesito que el numero que ingreses, sea entero')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')'''
        
def Ejecutable4(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    Lista_Resultado = [Menore, Mayore]
    
    return Lista_Resultado

print (f'La lista que contiene el menor y el mayor de los elementos es {Ejecutable4(Lista_Contador5)}')

def Ejecutable5(Lista, Numero):
    Contador = 0
    for elemento in Lista:
        if (elemento > Numero):
            Contador += 1
        else:
            continue
        
    return Contador

print (f'La cantidad de numeros mayores a 3 en la lista son {Ejecutable5(Lista_Contador5, 3)}')

def Ejecutable6(Lista):
    Nueva_Lista = list([])
    for elemento in Lista:
        if (elemento % 2 == 0):
            Nueva_Lista.append(elemento)
        else:
            continue
        
    return Nueva_Lista

print (f'Hice una lista nueva a partir de la original solo con los numeros pares {Ejecutable6(Lista_Contador5)}')

def Ejecutable7(Lista):
    Lista_Mult = []
    for elemento in Lista:
        Lista_Mult.append(elemento * 2)
        
    return Lista_Mult

print (f'{Lista_Contador5}')
print (f'{Ejecutable7(Lista_Contador5)}')

'''Lista_Promedios = []

Contador = 0

while (Contador < 3):
    while True:
        Elemento11 = input(f'Ingrese el numero {Contador}: ')
        try:
            Numerito6 = float(Elemento11)
            if (Numerito6.is_integer()):
                Lista_Promedios.append(Numerito6)
                break
            else:
                Lista_Promedios.append(Numerito6)
                break
        except ValueError:
            print (f'Error, necesito que ingreses un numero')
    Contador+= 1
    
Promedio5 = sum(Lista_Promedios) / Lista_Promedios.__len__()

print (f'El promedio de las notas elegidas es {round(Promedio5, 2)}')'''


class Persona7():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto64 = Persona7('Erick Perez Gutierrez')

print (f'Mi nombre es {Objeto64}')

class Colores7():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Colores7 = list([
    Colores7('Azul'),
    Colores7('Rojo'),
    Colores7('Verde'),
    Colores7('Amarillo')
])

print (f'Los elementos de la lista son {Lista_Colores7}')

class Inventario7:
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto65 = Inventario7()

Objeto65.Productos.append('Lapiz')
Objeto65.Productos.insert(1, 'Cuaderno')
Objeto65.Productos.extend(['Tajador'])

print (f'El total de elementos de la lista son {len(Objeto65)}')

class Igualdad7:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto66 = Igualdad7('Panda')
Objeto67 = Igualdad7('Panda')

print (f'{Objeto66 == Objeto67}')

'''print (f'-' * 20)

import requests

Resultado1 = requests.get('http://127.0.0.1:8005/grupo1/elemento1')
Resultado2 = Resultado1.json()

print (f'{Resultado2}')

print (f'-' * 20)

Lista_Api = [
    'Perro',
    'Gato',
    'Raton'
]

Agregar1 = requests.post('http://127.0.0.1:8005/grupo1/elemento1', json=(Lista_Api)) #type: ignore
Agregar2 = Agregar1.json()

print (f'{Agregar2}')

Resultado1 = requests.get('http://127.0.0.1:8005/grupo1/elemento1')
Resultado2 = Resultado1.json()

print (f'Mi animal favorito es el {Resultado2["Elementos"][0]}')

print (f'-' * 20)

import requests

var13 = 2

Agregar1 = requests.post(f'http://127.0.0.1:8005/grupo1/elemento1/{var13}')
Agregar2 = Agregar1.json()

print (f'{Agregar2}')

print (f'-' * 20)

import requests

var14 = 1
var15 = f'{Objeto9.Nombre}'

Reemplazar1 = requests.put(f'http://127.0.0.1:8005/grupo1/elemento1?Indice={var14}&Nuevo_Elemento={var15}')
Reemplazar2 = Reemplazar1.json()

print (f'{Reemplazar2}')

print (f'-' * 20)

import requests

Elimninar1 = requests.delete('http://127.0.0.1:8005/grupo1/elemento1', json=(0))
Elimninar2 = Elimninar1.json()

print (f'{Elimninar2}')'''

variable8 = 'Josue'
variable9 = 15

if (variable8 == variable1 and variable9 > Sumatoria2(1, 2, 3, 4, 5, 6)):
    print (f'Correcto, ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')
    
print (f'-' * 20)

if (variable8 == variable1 or variable9 > Sumatoria2(1, 2, 3, 4, 5, 6)):
    print (f'Correcto, al menos una de las condiciones se cumplen')
else:
    print (f'Error, ninguna condicion se cumple')
    
print (f'-' * 20)

print (f'{dir(Objeto11)}')

'''print (f'{help(Funcion_Diccionario)}')'''

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        
    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')
        
Objeto67 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Ash")], 'Kanto', Objeto9.Nombre)
Objeto68 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Brooke")], 'Alolah', Objeto10.Nombre)
Objeto69 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")], 'Paldea', Objeto11.Nombre)

Objeto67.Desplegar()

print (f'-' * 20)

Objeto68.Desplegar()

print (f'-' * 20)

Objeto69.Desplegar()

Negativo = -5

print (f'{int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima4 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable}')
print (f'{list(Anonima4)}')
print (f'{Lista_Iterable}')

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario5['Vacio']) == True):
    print (f'Gracias, informacion recibida')
else:
    print (f'Error, ingrese una cadena de texto')
    
Cociente, Residuo = divmod(Objeto10.Cantidad, Sumatoria2(1, 2, 1, 1, 2))

print (f'El cociente de la operacion es {Cociente}')
print (f'El Residuo de la operacion es {Residuo}')

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'{indice} ----- {elemento}')

print (f'-' * 20)

variable10 = 'eSteBAN'
variable10_letra = variable10[0]

print (f'{variable10}')
print (f'{variable10.lower()}')
print (f'{variable10.upper()}')
print (f'{variable10.capitalize()}')

print (f'{variable10.lower().find("t")}')
print (f'{variable10.lower().index("b")}')

print (f'La letra {variable10_letra} fue encontrada un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = 'este es un texto cualquiera para que podamos probar este proceso'
variable11_lista = variable11.split(' ')

for elemento in variable11_lista:
    print (f'{elemento}')
    
print (f'La cantidad de elementos del parrafor es {len(variable11_lista)}')

var13 = 'erick perez'

if (isinstance(var13.replace(' ', ''), (str))):
    print (f'Lo ingresado es un texto')
else:
    print (f'Lo ingresado no es un texto')
    
if (var13.replace(' ', '').isalpha()):
    print (f'Lo ingresado es un texto')
else:
    print (f'Lo ingresado no es un texto')
    
try:
    Numerito6 = float(var13)
    if (Numerito6.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado es un texto')
    
print (f'-' * 20)

var14 = 'hola'

if (isinstance(var14, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Lo ingresado no es un numero decimal')
    
try:
    Numerito7 = float(var14)
    if (Numerito7.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var15 = '5'

if (isinstance(var15, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero entero')
    
if (var15.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero entero')
    
try:
    Numerito8 = float(var15)
    if (Numerito8.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var16 = 'erick123'

if (var16.isalnum):
    print (f'Esto tiene letras, numeros o ambos')
else:
    print (f'Error de formato')
    
var17 = '      e       '

if (var17.isspace()):
    print (f'Esto solo esta compuesto por espacios')
else:
    print (f'Error, esto no son solo espacios')
    
var18 = 'eSteBAN'

if (var18.lower().islower()):
    print (f'Esto es puro minuscula')
else:
    print (f'Error, esto tiene mas que solo minusculas')
    
if (var18.upper().isupper()):
    print (f'Esto es puro mayuscula')
else:
    print (f'Error, esto tiene mas que solo mayuscula')
    
print (f'{PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

print (f'-' * 20)

for elemento in Diccionario7:
    print (f'{Diccionario7[elemento]}')
    
print (f'-' * 20)

for elemento in Diccionario7.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario7.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario7.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1
    
print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador += 1
    
print (f'-' * 20)

Lista_Animales = set({'Cebra', 'Serpiente'})
Set_Conjunto_Animal2 = {'Oso'}
Lista_Animales.update(Set_Conjunto_Animal2)

print (f'{Lista_Animales}')

Lista_Animales = list(Lista_Animales)

print (f'{Lista_Animales}')
print (f'{type(Lista_Animales)}')

Lista_Animales.append('Cocodrilo')
Lista_Animales.insert(1, 'Castor')
Lista_Animales.extend(['Avestruz'])

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Serpiente'):
        print (f'The name of this bicho in english is Snake or Serpent')
        break
    else:
        Contador+= 1
        continue
    
print (f'-' * 20)
    
for elemento1, elemento2 in zip(Lista_Animales, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)
    
for elemento1, elemento2, elemento3, elemento4 in zip(Lista_Animales, Set_Conjunto_Menu1, PEPE.Tupla_Poke, Lista_Uno_Copia):
    print (f'{elemento1} -- {elemento2} -- {elemento3} -- {elemento4}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
print (f'-' * 20)

Lista_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Mult}')

Num_Menor = min(Lista_Mult)
Num_Mayor = max(Lista_Mult)
Redondeado = round(14.458795, 2)

print (f'El numero menor de la lista es {Num_Menor}')
print (f'El numero mayor de la lista es {Num_Mayor}')

print (f'El numero redondeado 14.458795 es {Redondeado}')

print (f'{bool(False)}')
print (f'{bool(not True)}')
print (f'{bool("")}')
print (f'{bool(0)}')
print (f'{bool(None)}')

Todo_All = all([Lista_Uno_Copia, Diccionario5, Set_Conjunto3, None])

print (f'{Todo_All}')

print (f'-' * 20)

Sumatoria5 = sum(Lista_Mult)

print (f'El resultado de la sumatoria es {Sumatoria5}')

Uno = int('500')
Dos = str(500)
Tres = float(Uno)
Cuatro = list(Set_Conjunto_Menu1)
Cinco = set(Lista_Uno_Copia)
Seis = tuple(Set_Conjunto_Animal2)

print (f'El tipo de dato de la variable es {type(Uno)}')
print (f'El tipo de dato de la variable es {type(Dos)}')
print (f'El tipo de dato de la variable es {type(Tres)}')
print (f'El tipo de dato de la variable es {type(Cuatro)}')
print (f'El tipo de dato de la variable es {type(Cinco)}')
print (f'El tipo de dato de la variable es {type(Seis)}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

print (f'-' * 20)

'''def Floating1(Numero):
    try:
        Numerito9 = float(Numero)
        if (Numerito9.is_integer()):
            print (f'Lo ingresado fue un numero entero')
            Resultado = Numerito9 * Objeto11.Cantidad + Sumatoria2(1, 2, 2, 1)
            print (f'El resultado de la operacion es {Resultado}')
        else:
            print (f'Lo ingresado fue un numero decimal')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Floating1(PEPE.Flotante1)

print (f'-' * 20)

Resultado2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado2}')

def Floating3(Cadena):
    if (Cadena.lower().replace(' ', '').isalpha()):
        print (f'Lo ingresado es texto')
    else:
        print (f'Lo ingresado no es texto')

Floating3(PEPE.Flotante3)

print (f'-' * 20)

def Floating4(Cadena):
    Lista_Cadena = Cadena.split(' ')
    
    for indice, elemento in enumerate(Lista_Cadena, start=1):
        print (f'El indice {indice} tiene el elemento {elemento}')
        
    print (f'La cantidad de palabras digitadas es {len(Lista_Cadena)}')

Floating4(PEPE.Flotante4)'''

'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento}: ')
        Lista.append(Alumno)
        
    return Lista

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nLa lista de estudiantes es {Colegio(Lista_Alumnos)}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()'''
    
'''Lista_Alumnos = []

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Name = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Edad = input(f'Ingrese la edad del alumno {elemento}: ')
        Estudiante = [Alumno_Name, Alumno_Edad]
        Lista.append(Estudiante)
        
    print (f'{Lista}')
        
    Lista.sort(key = lambda Num : Num[1])
    
    Mayore = Lista[0][0]
    Menore = Lista[-1][0]
    
    print (f'El mayor de los estudiantes es {Menore} - {Lista[-1][1]}')
    print (f'El menor de los estudiantes es {Mayore} - {Lista[0][1]}')

Colegio(Lista_Alumnos)'''

def Exception_Finale(Numero):
    try:
        Numerito9 = float(Numero)
        if (Numerito9.is_integer()):
            print (f'Lo ingresado es un numero entero')
        else:
            print (f'Lo ingresado es un numero decimal')
    except ValueError:
        print (f'Error, lo ingresado no es un numero')

Exception_Finale('Hola')

import pandas as pd
import requests
import io

Ruta_Html2 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html2, headers=headers)

Leer_Html2 = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Leer_Html2)

print (f'{Cargar_Html2[2].head()}')

print (f'-' * 20)

import re

Texto12 = 'ericksuper80@hotmail.com'

Pattern11 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)$'

Buscar25 = bool(re.fullmatch(Pattern11, Texto12))

if (Buscar25 == True):
    print (f'El correo electronico tiene el formato correcto')
else:
    print (f'Error, formato de correo incorrecto')

print (f'-' * 20)

Texto13 = '32'

Pattern12 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar26 = bool(re.match(Pattern12, Texto13))

if (Buscar26):
    print (f'El numero se encuentra entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
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
    Fech5_Formateada = pd.to_datetime(Fech5)
    Cargar_Csv5['date'] = pd.to_datetime(Cargar_Csv5['date'])
except ValueError:
    print (f'Error, el formato de la fecha es incorrecto')
    exit()
    
Cargar_Csv5['TOTALITO'] = Cargar_Csv5['quantity'] * Cargar_Csv5['price']
    
Encontrada5 = Cargar_Csv5[Cargar_Csv5['date'].dt.date == Fech5_Formateada.date()]

if (Encontrada5.empty):
    print (f'No se han encontado ventas en esta fecha')
else:
    print (f'Genial! Hemos encontrado ventas en esta fecha')
    
    Grupo8 = Encontrada5.groupby('product')['quantity'].sum()
    Grupo8_Min = Grupo8.idxmin()
    Grupo8_Max = Grupo8.idxmax()
    Grupo8_Min_Cant = Grupo8.min()
    Grupo8_Max_Cant = Grupo8.max()
    
    print (f'En la fecha {Fech5_Formateada} el producto {Grupo8_Min} vendido un total de {Grupo8_Min_Cant} unidades')
    print (f'En la fecha {Fech5_Formateada} el producto {Grupo8_Max} vendido un total de {Grupo8_Max_Cant} unidades')
    
    print (f'En esta fecha un total de {Grupo8.count()} clientes compraron')
    print (f'La cantidad de productos vendidos en esta fecha fue de {Grupo8.sum()}')
    
    Grupo9 = Encontrada5.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue de ${Grupo9.sum()}')
    
    Promedio5 = Grupo9.sum() / Grupo8.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio5, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${Grupo9.mean()}')
    
class Caja():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto70 = Caja(5)
Objeto71 = Caja(4)

print (f'El resultado de la suma es {Objeto70 + Objeto71}')
    