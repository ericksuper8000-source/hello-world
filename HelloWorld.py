try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado no existe')
    raise

Lista_Elementos = [1, 2]
Lista_Elementos.append(3)
Lista_Elementos.insert(4, 4)
Lista_Elementos.extend([5])

def Ejercicio1(Lista):
    Contador = 0
    for elemento in Lista:
        Contador += 1
        
    return Contador

print (f'La lista tiene {Ejercicio1(Lista_Elementos)} elementos')

print (f'-' * 20)

def Ejercicio2(Lista):
    Contador = 0
    for elemento in Lista:
        if (elemento % 2 == 0):
            Contador += elemento
        else:
            continue
        
    return Contador

print (f'Si sumo solo los elementos pares de la lista me da el numero {Ejercicio2(Lista_Elementos)}')

print (f'-' * 20)

def Ejercicio3(Lista):
    Contador = 0
    for elemento in Lista:
        Contador += elemento
        
    return Contador

print (f'El resultado de sumar todos los elementos de la lista es {Ejercicio3(Lista_Elementos)}')

print (f'-' * 20)

def Ejercicio4(Lista, Numero):
    Founder = False
    for elemento in Lista:
        if (elemento == Numero):
            Founder = True
            break
        else:
            continue
        
    return Founder

if (Ejercicio4(Lista_Elementos, 3) == True):
    print (f'El numero fue encontrado en la lista')
else:
    print (f'Error, el numero no fue encontrado en la lista')
    
print (f'-' * 20)

def Ejercicio5(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    Lista_Resultado = [Menore, Mayore]

    return Lista_Resultado

print (f'La lista resultado es {Ejercicio5(Lista_Elementos)}')
print (f'El menor de los numeros de la lista es {min(Ejercicio5(Lista_Elementos))}')
print (f'El mayor de los numeros de la lista es {max(Ejercicio5(Lista_Elementos))}')

print (f'-' * 20)

def Ejercicio6(Lista, Numero):
    Contador = 0
    for elemento in Lista:
        if (elemento > Numero):
            Contador += 1
        else:
            continue
        
    return Contador

print (f'La cantidad de numeros mayores a 3 en la lista es {Ejercicio6(Lista_Elementos, 3)}')

print (f'-' * 20)

def Ejercicio7(Lista):
    Lista_Pares = list([])
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            continue
        
    return Lista_Pares

print (f'Se creo una lista que contiene solo los elementos pares: {Ejercicio7(Lista_Elementos)}')

print (f'-' * 20)

def Ejercicio8(Lista):
    Lista_ImPares = list([])
    for elemento in Lista:
        if (elemento % 2 != 0):
            Lista_ImPares.append(elemento)
        else:
            continue
        
    return Lista_ImPares

print (f'Se creo una lista que contiene solo los elementos pares: {Ejercicio8(Lista_Elementos)}')

print (f'-' * 20)

def Ejercicio9(Lista):
    Lista_Mult = []
    for elemento in Lista:
        Lista_Mult.extend([elemento * 2])
        
    return Lista_Mult

print (f'La lista original es {Lista_Elementos}')
print (f'La lista multiplicada es {Ejercicio9(Lista_Elementos)}')

print (f'-' * 20)

'''Contador = 0
Lista_Promedios = []

while (Contador < 3):
    while True:
        Numerito1 = input(f'Ingrese la nota {Contador}: ')
        try:
            Numerito2 = float(Numerito1)
            if (Numerito2.is_integer()):
                print (f'Lo ingresado es un numero entero')
                Lista_Promedios.append(Numerito2)
                break
            else:
                print (f'Lo ingresado es un numero decimal')
                Lista_Promedios.append(Numerito2)
                break
        except ValueError:
            print (f'Error, lo ingresado no es un numero')
    Contador += 1
    
Promedio1 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas ingresadas es {round(Promedio1, 2)}')'''

class Persona1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto1 = Persona1('Erick Josue Perez Gutierrez')

print (f'Hola, mi nombre es {Objeto1}')

print (f'-' * 20)

class Colores1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Colores1 = [
    Colores1('Rojo'),
    Colores1('Negro'),
    Colores1('Verde')
]

print (f'La lista de coloares es {Lista_Colores1}')

print (f'-' * 20)

class Inventario1():
    def __init__(self):
        self.Productos = list([])
        
    def __len__(self):
        return len(self.Productos)
        
Objeto2 = Inventario1()

Objeto2.Productos.append('Huevo')
Objeto2.Productos.insert(1, 'Sandia')
Objeto2.Productos.extend(['Jamon'])

print (f'La cantidad de elementos de la lista es {len(Objeto2)}')

print (f'-' * 20)

class Igualdad1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto3 = Igualdad1('Panda Rojo')
Objeto4 = Igualdad1('Panda Rojo')

if (Objeto3 == Objeto4):
    print (f'Ambos elementos son iguales')
else:
    print (f'Error, los elementos no son iguales')
    
print (f'-' * 20)

class Caja1():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto5 = Caja1(5)
Objeto6 = Caja1(3)

print (f'La suma de ambos pesos es {Objeto5 + Objeto6}')

print (f'-' * 20)

'''import requests

Resultado1 = requests.get('http://127.0.0.1:8006/grupo1/elemento1')
Resultado2 = Resultado1.json()

print (f'{Resultado2}')'''

var1 = '3'

if (isinstance(var1, (int))):
    print (f'El elemento es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
if (var1.isnumeric()):
    print (f'El elemento es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
try:
    Numerito1 = float(var1)
    if (Numerito1.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var2 = '3.2'

if (isinstance(var2, (float))):
    print (f'Lo ingresado es un numero decimal')
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

var3 = 'Erick'

if (var3.isalpha()):
    print (f'Lo ingresado es texto')
else:
    print (f'Lo ingresado no es texto')
    
if (isinstance(var3, (str))):
    print (f'Lo ingresado es texto')
else:
    print (f'Lo ingresado no es texto')
    
try:
    Numerito3 = float(var3)
    if (Numerito3.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado es texto')

print (f'-' * 20)

var4 = 'erick123'

if (var4.isalnum()):
    print (f'Esto tiene texto o numeros')
else:
    print (f'Error de formato')
    
var5 = 3

if (isinstance(var5, (int, float))):
    print (f'Esto es numero entero o decimal')
else:
    print (f'Error de formato')
    
var6 = '         e          '
    
if (var6.isspace()):
    print (f'Esto esta compuesto por espacios nada mas')
else:
    print (f'Error, esto tiene algo mas que espacios')
    
var7 = 'eSteBAN'

if (var7.lower().islower()):
    print (f'Esto es todo minuscula')
else:
    print (f'Error, no todo es minuscula')
    
if (var7.upper().isupper()):
    print (f'Esto es todo mayuscula')
else:
    print (f'Error, no todo es mayuscula')
    
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

Texto1_Version4 = re.sub(r'\!|\@|\d+', '', Texto1_Version3)

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
    print (f'Error, formato de fecha incorrecto')
    exit()
    
Cargar_Csv1['Totalito'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrado1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()]

if (Encontrado1.empty):
    print (f'No se ha encontrado ventas en esta fecha')
else:
    print (f'Genial! se han encontrado ventas en esta fecha')
    
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'En la fecha {Fech1_Formateada}, el producto {Grupo1_Min} vendio un total de {Grupo1_Min_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada}, el producto {Grupo1_Max} vendio un total de {Grupo1_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron en esta fecha fue de {Grupo1.count()}')
    print (f'La cantidad de productos vendidos en esta fecha fue de {Grupo1.sum()}')
    
    Grupo2 = Encontrado1.groupby('product')['Totalito'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue de ${Grupo2.sum()}')
    
    Promedio1 = Grupo2.sum() / Grupo1.count()
    
    print (f'El promedio de dinero vendido en esta fecha es de ${round(Promedio1, 2)}')
    print (f'El promedio de dinero vendido en esta fecha es de ${Grupo2.mean()}')
    
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

class Bulbasaur1():
    def Elegir(self):
        return f'Bulbasaur'
    
class Treekoo1():
    def Elegir(self):
        return f'Treekoo'
    
class Chikorita1():
    def Elegir(self):
        return f'Chikorita'
    
class Battle1():
    def __init__(self):
        self.Favorito = Bulbasaur1()
        
    def Batallar(self):
        print (f'El retador ha elegido a {self.Favorito.Elegir()} para la batalla!!!')
        
Objeto7 = Battle1()

Objeto7.Batallar()

print (f'-' * 20)

class Battle2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El retador ha elegido a {self.Favorito.Elegir()} para la batalla!!!')
        
Criatura1 = Bulbasaur1()
Objeto8 = Battle2(Criatura1)
Objeto8.Batallar()

Criatura2 = Treekoo1()
Objeto9 = Battle2(Criatura2)
Objeto9.Batallar()

Criatura3 = Chikorita1()
Objeto10 = Battle2(Criatura3)
Objeto10.Batallar()

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

Pattern2 = r'[^a-zA-Z0-9\s]'

Buscar2 = re.sub(Pattern2, '', Texto3)

print (f'{Buscar2}')

Buscar3 = re.sub(r'\d{5,}', '', Buscar2)

print (f'{Buscar3}')

# Version2

Pattern3 = r'\!|\?|\.{2,}|[0-9]{4}\-\d{3,4}'

Buscar4 = re.sub(Pattern3, '', Texto3)

print (f'{Buscar4}')

# Version3

Pattern4 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.[a-z]{2,}'

Correos1 = re.findall(Pattern4, Texto3)

Texto3_temp1 = Texto3

for i, email in enumerate(Correos1, start=1):
    Texto3_temp1 = Texto3_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto3_temp1}')

Texto3_temp2 = re.sub(r'\!|\?|\.{2,}|[0-9]{4}\-\d{3,}', '', Texto3_temp1)

print (f'{Texto3_temp2}')

for i, email in enumerate(Correos1, start=1):
    Texto3_temp2 = Texto3_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto3_temp2}')

print (f'-' * 20)

import re

Texto4 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Pattern5 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos2 = re.findall(Pattern5, Texto4)

Texto4_temp1 = Texto4

for i, email in enumerate(Correos2, start=1):
    Texto4_temp1 = Texto4_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto4_temp1}')

Pattern6 = r'\!|\?|\.{2,}'

Texto4_temp2 = re.sub(Pattern6, '', Texto4_temp1)

print (f'{Texto4_temp2}')

for i, email in enumerate(Correos2, start=1):
    Texto4_temp2 = Texto4_temp2.replace(f'SAMPLE{i}', email)
    
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
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

'''Contador = 0

Lista_Promedios = list([])

while (Contador < 3):
    while True:
        Numerito4 = input(f'Ingrese la nota {Contador}: ')
        try:
            Numerito5 = float(Numerito4)
            if (Numerito5.is_integer()):
                Lista_Promedios.append(Numerito5)
                break
            else:
                Lista_Promedios.append(Numerito5)
                break
        except ValueError:
            print (f'Error, lo ingresado no es un numero, intente nuevamente')
    Contador+= 1
    
Promedio2 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas elegidas es {round(Promedio2, 2)}')'''

class Primo():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto11 = Primo('Carmelo Vargas')

print (f'El nombre de mi primo es {Objeto11}')

from Module_Own import Pokemon1 as Poke1

Objeto12 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto13 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto12.Mostrar()

print (f'-' * 20)

Objeto13.Mostrar()

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto13 = Poke_Kid1(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto13)
Objeto13.Mostrar()

print (f'-' * 20)

class Veterinaria1():
    def __init__(self, Nombre, Peso, Edad):
        self.Nombre = Nombre
        self.Peso = Peso
        self.Edad = Edad

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Peso: {self.Peso}')
        print (f'Edad: {self.Edad}')
        
class Perro1(Veterinaria1):
    def __init__(self, Nombre, Peso, Edad, Raza, Padecimiento):
        super().__init__(Nombre, Peso, Edad)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        
    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        
Objeto14 = Perro1('Chester', 2.8, 5, 'Poodle', 'Asma De Perro')

Veterinaria1.Mostrar(Objeto14)
Objeto14.Mostrar()

print (f'-' * 20)

class Gato1(Veterinaria1):
    def __init__(self, Nombre, Peso, Edad, Color, Paciente):
        super().__init__(Nombre, Peso, Edad)
        self.Color = Color
        self.Paciente = Paciente

    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto15 = Gato1('Messi', 1.8, 1.5, 'Gris', 'No')

Veterinaria1.Mostrar(Objeto15)
Objeto15.Mostrar()

print (f'-' * 20)

class Pajaro1(Veterinaria1):
    def __init__(self, Nombre, Peso, Edad, Especie, Habla):
        super().__init__(Nombre, Peso, Edad)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto16 = Pajaro1('Polly', 0.4, 31, 'Cacatua', 'Si')

Veterinaria1.Mostrar(Objeto16)
Objeto16.Mostrar()

print (f'-' * 20)

class Atacante1():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon
        
    def Mostrar(self):
        print (f'Damage: {self.Damage}')
        print (f'Weapon: {self.Weapon}')
        
class Defensor1():
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
        
Objeto17 = Paladin1(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto17.Mostrar()
Atacante1.Mostrar(Objeto17)
Defensor1.Mostrar(Objeto17)

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
        
Objeto18 = D1()

A1.Mostrar(Objeto18)
B1.Mostrar(Objeto18)
C1.Mostrar(Objeto18)
Objeto18.Mostrar()
E1.Mostrar(Objeto18)

print (f'-' * 20)

class Tarjeta1():
    def Pagar(self):
        print (f'El pago se realizo con Tarjeta')
        
class Efectivo1():
    def Pagar(self):
        print (f'El pago se realizo con Efectivo')
        
class Cripto1():
    def Pagar(self):
        print (f'El pago se realizo con Cripto')
        
Objeto19 = Cripto1()
Objeto20 = Efectivo1()
Objeto21 = Tarjeta1()

Objeto19.Pagar()
Objeto20.Pagar()
Objeto21.Pagar()

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

print (f'Existe un saldo privado que no deberia ser publico, este es {Objeto21.Dinero}')

Objeto21.Dinero = '50,000,000'

Objeto21.Mostrar()

print (f'Existe un saldo privado que no deberia ser publico, este es {Objeto21.Dinero}')

from abc import ABC, abstractmethod

class Plantilla1(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla1(Plantilla1):
    def Mostrar(self):
        print (f'Este es el metodo interno')
        
    def General(self):
        print (f'Esto es de la plantilla y es obligatorio')
        
Objeto22 = Sub_Plantilla1()

Objeto22.Mostrar()
Objeto22.General()

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
    
class Pastel1():
    def __init__(self):
        self.Favorito = Chocolate1()
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Objeto23 = Pastel1()

Objeto23.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Ingrediente1 = Chocolate1()
Objeto24 = Pastel2(Ingrediente1)
Objeto24.Hornear()

Ingrediente2 = Vainilla1()
Objeto25 = Pastel2(Ingrediente2)
Objeto25.Hornear()

Ingrediente3 = Fresa1()
Objeto26 = Pastel2(Ingrediente3)
Objeto26.Hornear()

print (f'-' * 20)

Texto5 = 'esto hola 15 es un texto @ cualquiera hela 200 @ que deberia! de hula ser parte de lo ma-s 6 importante'

Buscar5 = re.search(r'parte', Texto5)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\d+', Texto5)

print (f'{Buscar6}')

Buscar7 = re.fullmatch(r'esto hola 15 es un texto \@ cualquiera hela 200 que deberia\! de hula ser parte de lo ma\-s 6 importante', Texto5)

print (f'{Buscar7}')

Buscar8 = re.findall(r'\d+', Texto5)

print (f'{Buscar8}')

Buscar9 = re.findall(r'\D+', Texto5)

print (f'{Buscar9}')

Buscar10 = re.findall(r'\s+', Texto5)

print (f'{Buscar10}')

Buscar11 = re.findall(r'\S+', Texto5)

print (f'{Buscar11}')

Buscar12 = re.findall(r'\W+', Texto5)

print (f'{Buscar12}')

Buscar13 = re.findall(r'\w+', Texto5)

print (f'{Buscar13}')

print (f'-' * 20)

'''
+
*
?
{2}
{2,3}
{2,}
'''

Buscar14 = re.findall(r'h.la', Texto5)

print (f'{Buscar14}')

Buscar15 = re.findall(r'^est', Texto5)

print (f'{Buscar15}')

Buscar16 = re.findall(r'tante$', Texto5)

print (f'{Buscar16}')

Buscar17 = re.findall(r'\d{3}\s\W', Texto5)

print (f'{Buscar17}')

Buscar18 = re.findall(r'[ei]{2,}', Texto5)

print (f'{Buscar18}')

print (f'-' * 20)

import re

Texto6 = 'ericksuper80@hotmail.com'

Pattern7 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.[a-z]{2,}'

Buscar19 = bool(re.fullmatch(Pattern7, Texto6))

if (Buscar19 == True):
    print (f'El formato del correo electronico es correcto')
else:
    print (f'Error, el formato del correo es incorrecto')
    
print (f'-' * 20)

Pattern8 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar20 = bool(re.fullmatch(Pattern8, Texto6))

if (Buscar20 == True):
    print (f'El formato del correo electronico es correcto')
else:
    print (f'Error, el formato del correo es incorrecto')
    
print (f'-' * 20)

Texto7 = '32'

Pattern9 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar21 = bool(re.fullmatch(Pattern9, Texto7))

if (Buscar21 == True):
    print (f'El numero se encuentra entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')

print (f'-' * 20)

Texto8 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern10 = r'\d{2}\/[0-9]{2}\/\d{3,}'

Replacement10 = 'XX/XX/XXXX'

Buscar22 = re.sub(Pattern10, Replacement10, Texto8)

print (f'{Buscar22}')

Pattern11 = r'\+\d?\-[0-9]{3}\-\d{3}\-[0-9]{4,5}'

Replacement11 = 'TELEFONO'

Buscar23 = re.sub(Pattern11, Replacement11, Buscar22)

print (f'{Buscar23}')

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

Pattern12 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Buscar23 = re.findall(Pattern12, Texto9)

print (f'{Buscar23}')

for elemento in enumerate(Buscar23):
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

import re

Texto10 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern13 = r'\!|\?|\.{2,}|[0-9]{4}\-\d{3,}'

Buscar24 = re.sub(Pattern13, '', Texto10)

print (f'{Buscar24}')

print (f'-' * 20)

var8 = 3.5

if (isinstance(var8, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Error, lo ingresado no es un numero decimal')
    
try:
    Numerito4 = float(var8)
    if (Numerito4.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado no es un numero')
    
print (f'-' * 20)

var9 = '5'

if (var9.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
if (isinstance(var9, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
try:
    Numerito5 = float(var9)
    if (Numerito5.is_integer()):
        print (f'El numero ingresado es entero')
    else:
        print (f'El numero ingresado es decimal')
       
except ValueError:
    print (f'Lo ingresado no es un numero')
    
print (f'-' * 20)

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
            print (f'Lo ingresado es un numero entero')
        else:
            print (f'Lo ingresado es un numero decimal')
    except ValueError:
        print (f'Error, esto no es un numero')

Exception1('hola')

def Exception2(Num1, Num2):
    try:
        Sumi = Num1 + Num2
        print (f'El resultado de la sumatoria es {Sumi}')
    except (ValueError, TypeError):
        print (f'Error, ambos elementos deben ser numeros enteros')

Exception2(12, 'hola')

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser un numero cero')

Exception3(12, 7)

print (f'-' * 20)

Lista_Exception4 = list([])
Lista_Exception4.append('Erick')
Lista_Exception4.insert(1, 'Josue')
Lista_Exception4.extend(['Karlita'])

print (f'{Lista_Exception4}')

def Exception4(Indice):
    try:
        print (f'El elemento en el indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')
        
Exception4(3)

Diccionario_Exception5 = dict.fromkeys(['Nombre', 'Edad'])
Diccionario_Exception5['Nombre'] = 'Erick'
Diccionario_Exception5['Edad']= 37

print (f'{Diccionario_Exception5}')
print (f'{Diccionario_Exception5.keys()}')
print (f'{Diccionario_Exception5.values()}')
print (f'{Diccionario_Exception5.items()}')
print (f'{Diccionario_Exception5["Nombre"]}')
print (f'{Diccionario_Exception5.get("Edad")}')

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception5("Votante")

print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Hiena')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')
    
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

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame_Concatenate_Age}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

print (f'De las personas en el dataframe, la edad menor es {Data_Frame_Concatenate_Age.min()}')
print (f'De las personas en el dataframe, la edad mayor es {Data_Frame_Concatenate_Age.max()}')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    todito1 = elemento['Nombre']
    todito2 = elemento['Edad']
    
    print (f'Mi nombre es {todito1} y mi edad es {todito2} años')
    
print (f'-' * 20)

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()
Grupo3_Min_Cant = Grupo3.min()
Grupo3_Max_Cant = Grupo3.max()

print (f'El bichillo menor de la lista es {Grupo3_Min} y su edad es {Grupo3_Min_Cant} años')
print (f'El bichillo menor de la lista es {Grupo3_Max} y su edad es {Grupo3_Max_Cant} años')

print (f'La cantidad de personas en la lista es {Grupo3.count()}')
print (f'Si sumo todas las edades el numero que me da es {Grupo3.sum()}')

Promedio2 = Grupo3.sum() / Grupo3.count()

print (f'El promedio de las edades es {round(Promedio2, 2)}')
print (f'El promedio de las edades es {round(Grupo3.mean(), 2)}')

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

print (f'La cantidad de Filas es {Filas}')
print (f'La cantidad de Columnas es {Columnas}')

Elemento1 = Data_Frame1.loc[0, 'Nombre']
Elemento2 = Data_Frame1.loc[1, 'Edad']
Elemento3 = Data_Frame1.loc[2, 'Votante']
Elemento4 = Data_Frame1.loc[0, :]
Elemento5 = Data_Frame1.loc[:, 'Edad']

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

print (f'{Cargar_Excel}')

print (f'-' * 20)

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='cabina')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='cabina', usecols='E:K')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='cabina', usecols='E:K', nrows=1)

print (f'{Cargar_Excel1}')

print (f'-' * 20)

print (f'{Cargar_Excel2}')

print (f'-' * 20)

print (f'{Cargar_Excel3}')

print (f'-' * 20)

print (f'{Cargar_Excel4}')

print (f'-' * 20)

print (f'{Cargar_Excel5}')

print (f'-' * 20)

print (f'{Cargar_Excel6}')

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

import numpy as np

Array0 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print (f'{Array0}')
print (f'{Array0[1]}')
print (f'{Array0[1][::2]}')
print (f'{Array0[2][::3]}')
print (f'{Array0[0][:2]}')
print (f'{Array0[0][2:]}')
print (f'{Array0[1][2:3]}')
print (f'{Array0[2][0:None]}')
print (f'{Array0[2][:]}')

print (f'-' * 20)

for i in range(len(Array0)):
    for j in range(len(Array0[i])):
        print (f'{Array0[i][j]}')
        
print (f'-' * 20)

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
print (f'{Array1[Array1 > 2]}')

print (f'-' * 20)

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 1]}')

print (f'{Array2[1, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[0, :2]}')
print (f'{Array2[0, 2:]}')
print (f'{Array2[1, 2:3]}')
print (f'{Array2[:, 1]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[0, :]}')
print (f'{Array2[Array2 >= 2]}')

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

print (f'El resultado de la sumatoria es {Sumita1}')
print (f'El resultado de la sumatoria es {Sumita2}')
print (f'El resultado de la sumatoria es {Sumita3}')
print (f'El resultado de la sumatoria es {Sumita4}')

print (f'-' * 20)

Array3 = np.array([[['e', 'k', 'n'], ['a', 's', 'r']],      [['o', 'n', 'i'], ['p', 'm', 'x']]])

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
print (f'{Array3[0, 0, 2:3]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "n"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],                [[[6, 5, 4], [9, 8, 7]], [[4, 5, 6], [9, 2, 7]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 2]}')

print (f'{Array4[1, 0, 0, ::2]}')
print (f'{Array4[1, 0, 1, ::3]}')
print (f'{Array4[1, 1, 0, :2]}')
print (f'{Array4[1, 0, 0, 2:]}')
print (f'{Array4[1, 1, 0, 2:3]}')
print (f'{Array4[0, 1, :, 2]}')
print (f'{Array4[0, 1, 0, 0:None]}')
print (f'{Array4[0, 1, 0, :]}')
print (f'{Array4[Array4 >= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodados: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[1, 0, 0, 0:None])
Sumita8 = np.sum(Array4_Sorted[1, 0, 0, :])

print (f'El resultado de las sumatorias es {Sumita5}')
print (f'El resultado de las sumatorias es {Sumita6}')
print (f'El resultado de las sumatorias es {Sumita7}')
print (f'El resultado de las sumatorias es {Sumita8}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1) #type: ignore

print (f'{Array_Num1}')

Array_Num_Min = np.min(Array_Num1)
Array_Num_Max = np.max(Array_Num1)

print (f'El menor de los numeros es {Array_Num_Min} y el mayor es {Array_Num_Max}')

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
print (f'{Array_Zeros[1, 2]}')

print (f'{Array_Zeros[0, ::2]}')
print (f'{Array_Zeros[1, ::3]}')
print (f'{Array_Zeros[0, :2]}')
print (f'{Array_Zeros[0, 2:]}')
print (f'{Array_Zeros[1, 2:3]}')
print (f'{Array_Zeros[:, 2]}')
print (f'{Array_Zeros[1, 0:None]}')
print (f'{Array_Zeros[1, :]}')
print (f'{Array_Zeros[Array_Zeros == 0]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 1]}')

print (f'{Array_Ones[0, ::2]}')
print (f'{Array_Ones[1, ::3]}')
print (f'{Array_Ones[0, :2]}')
print (f'{Array_Ones[0, 2:]}')
print (f'{Array_Ones[1, 2:3]}')
print (f'{Array_Ones[:, 0]}')
print (f'{Array_Ones[1, 0:None]}')
print (f'{Array_Ones[1, :]}')
print (f'{Array_Ones[Array_Ones == 1]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke2"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 1]}')

print (f'{Array_Gen1[0, ::2]}')
print (f'{Array_Gen1[1, ::3]}')
print (f'{Array_Gen1[0, :2]}')
print (f'{Array_Gen1[0, 2:]}')
print (f'{Array_Gen1[1, 2:3]}')
print (f'{Array_Gen1[:, 2]}')
print (f'{Array_Gen1[1, 0:None]}')
print (f'{Array_Gen1[1, :]}')
print (f'{Array_Gen1[Array_Gen1 == "Graveler"]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value=f'Fuecoco')

print (f'{Array_Gen2}')

Lista_Array1 = list([])

for elemento in Array_Gen2:
    Lista_Array1.append(str(elemento))
    
print (f'{type(Array_Gen2)}')
print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[1, 0, 1, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 0]}')

print (f'{Array_Gen3[0, ::2]}')
print (f'{Array_Gen3[1, ::3]}')
print (f'{Array_Gen3[1, :2]}')
print (f'{Array_Gen3[1, 2:]}')
print (f'{Array_Gen3[:, 1]}')
print (f'{Array_Gen3[1, 2:3]}')
print (f'{Array_Gen3[0, 0:None]}')
print (f'{Array_Gen3[0, :]}')
print (f'{Array_Gen3[Array_Gen3 >= 6]}')

print (f'-' * 20)

Tupla_Array = ('Rojo', 'Azul', 'Verde')
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(1, 3), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(3, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array['Nombre'][2])


print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'-' * 20)

print (f'{Array_Gen6[2]}')

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
print (f'{Array_Random2.ndim}')
print (f'{Array_Random2.shape}')
print (f'{Array_Random2.size}')
print (f'{Array_Random2.dtype}')
print (f'{Array_Random2[1, 2]}')

print (f'{Array_Random2[0, ::2]}')
print (f'{Array_Random2[1, ::3]}')
print (f'{Array_Random2[0, :2]}')
print (f'{Array_Random2[0, 2:]}')
print (f'{Array_Random2[:, 2]}')
print (f'{Array_Random2[1, 2:3]}')
print (f'{Array_Random2[0, 0:None]}')
print (f'{Array_Random2[0, :]}')
print (f'{Array_Random2[Array_Random2 >= 5]}')

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

print (f'El resultado de la sumatoria es {Sumita9}')
print (f'El resultado de la sumatoria es {Sumita10}')
print (f'El resultado de la sumatoria es {Sumita11}')
print (f'El resultado de la sumatoria es {Sumita12}')

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

Array_Num8_Reshape_Column_Min = np.min(Array_Num8_Reshape, axis=0)
Array_Num8_Reshape_Column_Max = np.max(Array_Num8_Reshape, axis=0)
Array_Num8_Reshape_Row_Min = np.min(Array_Num8_Reshape, axis=1)
Array_Num8_Reshape_Row_Max = np.max(Array_Num8_Reshape, axis=1)

print (f'Los menores de las columnas {Array_Num8_Reshape_Column_Min}')
print (f'Los mayores de las columnas {Array_Num8_Reshape_Column_Max}')
print (f'Los menores de las filas {Array_Num8_Reshape_Row_Min}')
print (f'Los mayores de las filas {Array_Num8_Reshape_Row_Max}')

print (f'-' * 20)

Lista_Array2 = ['Erick']
Lista_Array2.append('Josue')
Lista_Array2.extend(['Karlita'])

Array_Num9 = np.array([Lista_Array2])

print (f'{Array_Num9}')
print (f'{type(Array_Num9)}')

print (f'-' * 20)

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1) #type: ignore

Array_Concatenate = np.concat([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'-' * 20)

Array_Concatenate_Split1 = np.split(Array_Concatenate, 1)
Array_Concatenate_Split2 = np.split(Array_Concatenate, 2)
Array_Concatenate_Split3 = np.split(Array_Concatenate, 3)
Array_Concatenate_Split4 = np.split(Array_Concatenate, 6)

print (f'{Array_Concatenate_Split1[0]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Split2[0]}')
print (f'{Array_Concatenate_Split2[1]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Split3[0]}')
print (f'{Array_Concatenate_Split3[1]}')
print (f'{Array_Concatenate_Split3[2]}')

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

for Matriz1 in Array3:
    for Fila in Matriz1:
        print (f'{Fila}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Array_Random3_Sorted = np.sort(Array_Random3)
Array_Random3_Sorted_Mean = np.mean(Array_Random3_Sorted)
Array_Random3_Sorted_Sum = np.sum(Array_Random3_Sorted)

print (f'Acomodado: {Array_Random3_Sorted}')
print (f'Media: {round(Array_Random3_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random3_Sorted_Sum}')

Sumita13 = np.sum(Array_Random3_Sorted, axis=0)
Sumita14 = np.sum(Array_Random3_Sorted, axis=1)
Sumita15 = np.sum(Array_Random3_Sorted[0, 0:None])
Sumita16 = np.sum(Array_Random3_Sorted[0, :])

print (f'El resultado de la sumatoria es {Sumita13}')
print (f'El resultado de la sumatoria es {Sumita14}')
print (f'El resultado de la sumatoria es {Sumita15}')
print (f'El resultado de la sumatoria es {Sumita16}')

Array_Random3_Column_Min = np.min(Array_Random3, axis=0)
Array_Random3_Column_Max = np.max(Array_Random3, axis=0)
Array_Random3_Row_Min = np.min(Array_Random3, axis=1)
Array_Random3_Row_Max = np.max(Array_Random3, axis=1)

print (f'Los menores de las columnas son {Array_Random3_Column_Min}')
print (f'Los menores de las columnas son {Array_Random3_Column_Max}')
print (f'Los menores de las columnas son {Array_Random3_Row_Min}')
print (f'Los menores de las columnas son {Array_Random3_Row_Max}')

print (f'-' * 20)

Set_Conjunto_Sorteo1 = set({'Erick', 'Josue', 'Josue', 'Josue', 'Josue', 'Josue', 'Josue'})
Set_Conjunto_Sorteo1.add('Karlita')
Set_Conjunto_Sorteo2 = {'Carmelo', 'Susanita'}
Set_Conjunto_Sorteo2.add('Roxana')

Set_Conjunto_Sorteo1.update(Set_Conjunto_Sorteo2)

Lista_Sorteo1 = list(Set_Conjunto_Sorteo1)

print (f'{Lista_Sorteo1}')

Ganador1 = np.random.choice(Lista_Sorteo1, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Sorteo1, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Sorteo1, size=(2, 3), replace=False)

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
            yield f'El numero es cero'
        elif (elemento == 1):
            yield f'El numero es uno'
        elif (elemento == 2):
            yield f'El numero es dos'
        elif (elemento == 3):
            yield f'El numero es tres'
        elif (elemento == 4):
            yield f'El numero es cuatro'
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
    print (f'Fin del experimento')

print (f'-' * 20)

Lista_Elementos2 = list([1, 2, 3, 4, 5])

def Ejercicio10(Lista):
    Contador = 0
    for elemento in Lista:
        Contador += 1
        
    return Contador

print (f'La cantidad de elementos que tiene la lista es {Ejercicio10(Lista_Elementos2)}')

print (f'-' * 20)

def Ejercicio11(Lista):
    Contador = 0
    for elemento in Lista:
        if (elemento % 2 == 0):
            Contador += elemento
        else:
            continue
        
    return Contador

print (f'Si tomo solo los elementos pares de la lista y los sumo, me da el numero {Ejercicio11(Lista_Elementos2)}')

print (f'-' * 20)

def Ejercicio12(Lista):
    Contador = 0
    for elemento in Lista:
        Contador += elemento
        
    return Contador

print (f'Si sumo todos los elementos de las listas el resultado es {Ejercicio12(Lista_Elementos2)}')

print (f'-' * 20)

def Ejercicio13(Lista, Numero):
    Founder = False
    for elemento in Lista:
        if (elemento == Numero):
            Founder = True
            break
        else:
            continue
        
    return Founder

if (Ejercicio13(Lista_Elementos2, 3) == True):
    print (f'El numero fue encontrado en la lista')
else:
    print (f'Error, el numero no esta en la lista')
    
print (f'-' * 20)

def Ejercicio14(Lista, Numero):
    Contador = 0
    for elemento in Lista:
        if (elemento > Numero):
            Contador += 1
        else:
            continue
        
    return Contador

print (f'La cantidad de numeros que son mayores a 3 es {Ejercicio14(Lista_Elementos2, 3)}')

print (f'-' * 20)

def Ejercicio15(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    Lista_Resultado = [Menore, Mayore]
    
    return Lista_Resultado

print (f'La lista resultado {Ejercicio15(Lista_Elementos2)}')

print (f'El menor de los numeros de la lista es {min(Ejercicio15(Lista_Elementos2))}')
print (f'El mayor de los numeros de la lista es {max(Ejercicio15(Lista_Elementos2))}')

print (f'-' * 20)

def Ejercicio16(Lista): #type: ignore
    Lista_Pares = []
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            continue
        
    return Lista_Pares

print (f'La lista de elementos pares es {Ejercicio16(Lista_Elementos2)}')

print (f'-' * 20)

def Ejercicio16(Lista):
    Lista_ImPares = []
    for elemento in Lista:
        if (elemento % 2 != 0):
            Lista_ImPares.append(elemento)
        else:
            continue
        
    return Lista_ImPares

print (f'La lista de elementos impares es {Ejercicio16(Lista_Elementos2)}')

print (f'-' * 20)

def Ejercicio17(Lista):
    Lista_Mult = list([])
    for elemento in Lista:
        Lista_Mult.extend([elemento * 2])
        
    return Lista_Mult

print (f'Lista Original: {Lista_Elementos2}')
print (f'Lista Actulizada: {Ejercicio17(Lista_Elementos2)}')

print (f'-' * 20)

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
    
PEPE.Usuario1(Saludar_Dos(), 'FEMENINO')

def Usuario_Externo():
    def Usuario_Interno(Sexo):
        Genero = Sexo.lower()
        if (Genero == 'masculino'):
            return True
        else:
            return False

    return Usuario_Interno('FEMENINO')

Variable_Usuario = Usuario_Externo()

if (Variable_Usuario == True):
    print (f'YOU ARE A MAN')
else:
    print (f'YOU ARE A WOMAN')
    
print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(98)}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo es incorrecto')
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

print (f'-' * 20)

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.keys():
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    for elemento in kwargs.values():
            print (f'{elemento}')
            
    print (f'-' * 20)
        
    for elemento in kwargs.items():
            print (f'{elemento[0]} -- {elemento[1]}')
            
    print (f'-' * 20)
    
    for elemento in kwargs:
        print (f'{kwargs[elemento]}')
        
Variable_Funcion_Diccionario = Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = 37, Votante = Variable_Funcion_Tupla[3])

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

def Sumatoria_Dos(Nombre, *args):
    return f'Mi nombre es {Nombre} y mi numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

Any_Par = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Lista_Par = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

if (Any_Par == True):
    print (f'Los numeros pares de la lista son {Lista_Par}')
    print (f'Los numeros pares de la lista son {list(Anonima3)}')
else:
    print (f'Error, no hay numeros pares en la lista')
    
print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda(*args) - 42
        
    return Tercera

@Primera
def Operacion(Numero : int) -> int:
    Local = Numero
    return PEPE.GLOBAL + Local

print (f'El resultado de la operacion es {Operacion(12)}')

def Externa(Nombre):
    def Interna(Apellido:str) -> str:
        return Nombre + Apellido
    
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
print (f'{Variable_Closure(26)}')
print (f'{Variable_Closure(41)}')

print (f'-' * 20)

def Closure_Crear_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y

    return Closure_Multiplicador

Mult1 = Closure_Crear_Multiplicador(2)
Mult2 = Closure_Crear_Multiplicador(3)

print (f'El multiplicador es {Mult1(10)}')
print (f'El multiplicador es {Mult2(10)}')

print (f'-' * 20)

def Filtrador(Lista):
    Any_Impares = any(num % 2 != 0 for num in Lista)
    if (Any_Impares == True):
        Anonimo = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impares = [num for num in Lista if num % 2 != 0]
        
        print (f'Los numeros impares de la lista son {list(Anonimo)}')
        print (f'Los numeros impares de la lista son {Lista_Impares}')
    else:
        print (f'Error, no hay numeros impares en la lista')

Filtrador(PEPE.Lista_Numeros)

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'ANTES')
        Segunda()
        print (f'DESPUES')
        
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
def Sumatoria3(Num1, Num2):
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(12, 7)}')

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

Lista_Elementos3 = [2, 4, 6]

def separar_pares_impares(Lista):
    Lista_Pares = []
    Lista_Impares = list([])
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            Lista_Impares.append(elemento)
            
    Lista_Resultado = [Lista_Pares, Lista_Impares]
    
    return Lista_Resultado

print (f'Pares: {separar_pares_impares(Lista_Elementos3)[0]}')
print (f'Impares: {separar_pares_impares(Lista_Elementos3)[1]}')

print (f'-' * 20)

Lista_Elementos4 = []

def clasificar_numeros(Lista):
    Positivos = 0
    Negativos = 0
    Ceros = 0
    for elemento in Lista:
        if (elemento > 0):
            Positivos += 1
        elif (elemento < 0):
            Negativos += 1
        else:
            Ceros += 1
            
    Lista_Resultado = [Positivos, Negativos, Ceros]
    
    return Lista_Resultado

Total_Positivos = clasificar_numeros(Lista_Elementos4)[0]
Total_Negativos = clasificar_numeros(Lista_Elementos4)[1]
Total_Ceros = clasificar_numeros(Lista_Elementos4)[2]

print (f'Positivos: {Total_Positivos}')
print (f'Negativos: {Total_Negativos}')
print (f'Ceros: {Total_Ceros}')

print (f'-' * 20)

import re

Lista_Cadenas = [
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
]

def filtrar_correos(Cadenas):
    Lista_Validos = []
    Lista_Invalidos = list([])
    
    Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'
    
    for elemento in Cadenas:
        Buscar = bool(re.fullmatch(Pattern, elemento))
        if (Buscar == True):
            Lista_Validos.append(elemento)
        else:
            Lista_Invalidos.extend([elemento])
            
    return Lista_Validos, Lista_Invalidos
        

Correos_Validos, Correos_Invalidos = filtrar_correos(Lista_Cadenas)

print (f'Los correos con formato valido son {Correos_Validos}')
print (f'Los correos con formato invalido son {Correos_Invalidos}')

Lista_Elementos5 = list([1, 2])
Lista_Elementos5.append(3)
Lista_Elementos5.insert(4, 4)
Lista_Elementos5.extend([5])

def Ejercicio18(Lista):
    Contador = 0
    for elemento in Lista:
        Contador += 1
        
    return Contador

print (f'La cantidad de numeros que tenemos en la lista es {Ejercicio18(Lista_Elementos5)}')

print (f'-' * 20)

def Ejercicio19(Lista):
    Contador = 0
    for elemento in Lista:
        if (elemento % 2 == 0):
            Contador += elemento
        else:
            continue
        
    return Contador

print (f'Si tomo los elementos pares de la lista y los sumo, me da el numero {Ejercicio19(Lista_Elementos5)}')

print (f'-' * 20)

def Ejercicio20(Lista):
    Acumulador = 0
    for elemento in Lista:
        Acumulador += elemento
        
    return Acumulador

print (f'Si sumo todos los numeros de la lista me da el numero {Ejercicio20(Lista_Elementos5)}')

print (f'-' * 20)

def Ejercicio21(Lista, Numero):
    Founder = False
    for elemento in Lista:
        if (elemento == Numero):
            Founder = True
            break
        else:
            continue
        
    return Founder

if (Ejercicio21(Lista_Elementos5, 4) == True):
    print (f'El numero fue encontrado en la lista')
else:
    print (f'Error, el numero no existe en la lista')
    
print (f'-' * 20)

def Ejercicio22(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    Lista_Resultado = [Menore, Mayore]
    
    return Lista_Resultado

Menore1 = min(Ejercicio22(Lista_Elementos5))
Mayore1 = max(Ejercicio22(Lista_Elementos5))

print (f'El menor de los numeros de la lista es {Menore1} y el mayor de los numeros de la lista es {Mayore1}')

print (f'-' * 20)

def Ejercicio23(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    return Menore, Mayore

Menore2, Mayore2 = Ejercicio23(Lista_Elementos5)

print (f'El menor de los numeros de la lista es {Menore2} y el mayor de los numeros de la lista es {Mayore2}')

print (f'-' * 20)

def Ejercicio24(Lista, Numero):
    Contador = 0
    for elemento in Lista:
        if (elemento > Numero):
            Contador += 1
        else:
            continue
        
    return Contador

print (f'La cantidad de numeros en la lista que son mayores a 2 son: {Ejercicio24(Lista_Elementos5, 2)}')

print (f'-' * 20)

def Ejercicio25(Lista):
    Lista_Pares = []
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            continue
        
    return Lista_Pares

print (f'De la lista elegida, los pares son {Ejercicio25(Lista_Elementos5)}')

print (f'-' * 20)

def Ejercicio26(Lista):
    Lista_ImPares = []
    for elemento in Lista:
        if (elemento % 2 != 0):
            Lista_ImPares.append(elemento)
        else:
            continue
        
    return Lista_ImPares

print (f'De la lista elegida, los impares son {Ejercicio26(Lista_Elementos5)}')

print (f'-' * 20)

def Ejercicio27(Lista):
    Lista_Mult = list([])
    for elemento in Lista:
        Lista_Mult.append(elemento * 2)
        
    return Lista_Mult

print (f'Lista Original: {Lista_Elementos5}')
print (f'Lista Actualizada: {Ejercicio27(Lista_Elementos5)}')

print (f'-' * 20)

'''Lista_Promedios = []

Contador = 0

while (Contador < 3):
    while True:
        Numerito6 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito7 = float(Numerito6)
            if (Numerito7.is_integer()):
                Lista_Promedios.append(Numerito7)
                break
            else:
                Lista_Promedios.append(Numerito7)
                break
        except ValueError:
            print (f'Error, lo ingresado no es un numero, intente nuevamente')
    Contador+= 1
    
Promedio3 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas seleccionadas es {round(Promedio3, 2)}')'''

def Ejercicio28(Lista):
    Lista_Pares = []
    Lista_Impares = list([])
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            Lista_Impares.extend([elemento])
            
    return Lista_Pares, Lista_Impares

Pares, Impares = Ejercicio28(Lista_Elementos5)

print (f'PARES: {Pares}')
print (f'PARES: {Impares}')

print (f'-' * 20)

Lista_Elementos6 = [-1, -6, 9, 0, -3, 0]

def Ejercicio29(Lista):
    Positivos = 0
    Negativos = 0
    Ceros = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Positivos += 1
        elif (elemento < 0):
            Negativos += 1
        else:
            Ceros += 1
            
    return Positivos, Negativos, Ceros

POSITIVE, NEGATIVE, ZERO = Ejercicio29(Lista_Elementos6)

print (f'Numeros Positivos: {POSITIVE}')
print (f'Numeros Negativos: {NEGATIVE}')
print (f'Numeros Ceros: {ZERO}')

print (f'-' * 20)

import re

Lista_Elementos7 = [
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
]

def Ejercicio30(Lista):
    
    Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'
    
    Lista_Correos_Validos = []
    Lista_Correos_Invalidos = list([])
    
    for elemento in Lista:
        Buscar = bool(re.fullmatch(Pattern, elemento))
        if (Buscar == True):
            Lista_Correos_Validos.append(elemento)
        else:
            Lista_Correos_Invalidos.extend([elemento])
            
    Lista_Resultados = [Lista_Correos_Validos, Lista_Correos_Invalidos]
    
    return Lista_Resultados

Validos, Invalidos = Ejercicio30(Lista_Elementos7)

print (f'La lista de correos validos es {Validos}')
print (f'La lista de correos invalidos es {Invalidos}')

print (f'-' * 20)

'''def Floating1(Numero):
    try:
        Numerito6 = float(Numero)
        if (Numerito6.is_integer()):
            Resultado = Objeto13.Cantidad + Variable_Sumatoria * Numerito6
            print (f'El numero que ingresaste es entero, y el resultado de la operacion es {Resultado}')
        else:
            Resultado = Objeto13.Cantidad + Variable_Sumatoria * Numerito6
            print (f'El numero que ingresaste es entero, y el resultado de la operacion es {round(Resultado, 2)}')
    except ValueError:
        print (f'Error, lo que se ingreso no es un numero')

Floating1(PEPE.Flotante1)'''

'''Resultado1 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado1}')'''

'''def Floating3(Cadena):
    if (isinstance(Cadena, (str))):
        if (Cadena.replace(' ', '').isalpha()):
            print (f'Gracias, lo que ingresaste es un texto - {Cadena.replace(' ', '')} - {Cadena}')
    else:
        print (f'Error, lo ingresado no es texto')

Floating3(PEPE.Flotante3)'''

'''def Floating4(Cadena):
    Lista_Cadena = Cadena.split(' ')
    
    for indice, elemento in enumerate(Lista_Cadena, start=1):
        print (f'{indice} -- {elemento}')
        
    print (f'La cantidad de palabras digitadas por usted fue de {Lista_Cadena.__len__()}')

Floating4(PEPE.Flotante4)'''

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento}: ')
        Lista.append(Alumno)
        
    return Lista

Alumnos = Colegio(Lista_Alumnos)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.writelines([f'\nLa lista de alumnos es {Alumnos}'])
        Docu.close()
except FileNotFoundError:
    print (f'Error, este archivo no existe')
    raise

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()'''
    
'''Lista_Alumnos = []

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
        Lista_Alumnos = [Alumno_Nombre, Alumno_Edad]
        Lista.extend([Lista_Alumnos])
        
    Lista.sort(key = lambda Num : Num[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'De la lista de alumnos, el menor de los alumnos es {Menore} ({Lista[0][1]} años)')
    print (f'De la lista de alumnos, el mayor de los alumnos es {Mayore} ({Lista[-1][1]} años)')

Colegio(Lista_Alumnos)'''

class Persona2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto27 = Persona2('Erick Perez Gutierrez')

print (f'Hola, mi nombre es {Objeto27}')

print (f'-' * 20)

class Colores2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Colores2 = list([
    Colores2('Blue'),
    Colores2('Red'),
    Colores2('Green')
])

print (f'La lista de colores es {Lista_Colores2}')

print (f'-' * 20)

class Inventario2():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto28 = Inventario2()

Objeto28.Productos.append('Coco')
Objeto28.Productos.insert(1, 'Manzana')
Objeto28.Productos.extend(['Pera'])

print (f'La cantidad de elementos de la lista es {len(Objeto28)}')

print (f'-' * 20)

class Igualdad2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
        
Objeto29 = Igualdad2('Panda Rojo')
Objeto30 = Igualdad2('Panda Rojo')

if (Objeto29 == Objeto30):
    print (f'Los objetos son iguales')
else:
    print (f'Error, los objetos no son iguales')
    
print (f'-' * 20)

class Caja2():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto31 = Caja2(5)
Objeto32 = Caja2(4)

print (f'La suma de los elementos es {Objeto31 + Objeto32}')

print (f'-' * 20)

'''import requests

Resultado1 = requests.get('http://127.0.0.1:8009/grupo1/elemento1')
Resultado2 = Resultado1.json()

print (f'{Resultado2}')'''

from Module_Own import Pokemon2 as Poke2

Objeto33 = Poke2(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto34 = Poke2(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto33.Mostrar()

print (f'-' * 20)

Objeto34.Mostrar()

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto35 = Poke_Kid2(PEPE.Diccionario_Poke["Poke3"], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto35)
Objeto35.Mostrar()

print (f'-' * 20)

class Camara1():
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada')
        
class Reproductor_Musica1():
    def Reproducir_Musica(self):
        print (f'La musica fue reproducida')
        
class Smartphone1(Camara1, Reproductor_Musica1):
    def Encender_Smartphone(self):
        print (f'Smartphone encendido')
        
Objeto36 = Smartphone1()

Objeto36.Encender_Smartphone()
Objeto36.Reproducir_Musica()
Objeto36.Tomar_Fotografia()

print (f'-' * 20)

class Veterinaria2():
    def __init__(self, Nombre, Peso, Edad):
        self.Nombre = Nombre
        self.Peso = Peso
        self.Edad = Edad

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Peso: {self.Peso}')
        print (f'Edad: {self.Edad}')
        
class Perro2(Veterinaria2):
    def __init__(self, Nombre, Peso, Edad, Raza, Padecimiento):
        super().__init__(Nombre, Peso, Edad)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        
    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        
Objeto37 = Perro2('Chester', 2.8, 5, 'Poodle', 'Asma De Perro')

Veterinaria2.Mostrar(Objeto37)
Objeto37.Mostrar()

print (f'-' * 20)

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Peso, Edad, Color, Paciente):
        super().__init__(Nombre, Peso, Edad)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto38 = Gato2('Messi', 1.8, 1.5, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto38)
Objeto38.Mostrar()

print (f'-' * 20)

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Peso, Edad, Especie, Habla):
        super().__init__(Nombre, Peso, Edad)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto39 = Pajaro2('Polly', 0.4, 31, 'Perico Verde', 'Si')

Veterinaria2.Mostrar(Objeto39)
Objeto39.Mostrar()

print (f'-' * 20)

class Atacante2():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon
        
    def Mostrar(self):
        print (f'Damage: {self.Damage}')
        print (f'Weapon: {self.Weapon}')
        
class Defensor2():
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life

    def Mostrar(self):
        print (f'Healing: {self.Healing}')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}')
        
class Paladin2(Atacante2, Defensor2):
    def __init__(self, Damage, Weapon, Healing, Potion, Life, Name):
        Atacante2.__init__(self, Damage, Weapon)
        Defensor2.__init__(self, Healing, Potion, Life)
        self.Name = Name
        
    def Mostrar(self):
        print (f'Name: {self.Name}')
        
Objeto40 = Paladin2(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto40.Mostrar()
Atacante2.Mostrar(Objeto40)
Defensor2.Mostrar(Objeto40)

print (f'-' * 20)

Hija_Padre1 = issubclass(Poke_Kid2, Poke2)
Hija_Padre2 = issubclass(Poke_Kid2, Poke1)

print (f'{Hija_Padre1}')
print (f'{Hija_Padre2}')

print (f'-' * 20)

Instancia1 = isinstance(Objeto40, Paladin2)
Instancia2 = isinstance(Objeto40, Defensor2)
Instancia3 = isinstance(Objeto40, Atacante2)
Instancia4 = isinstance(Objeto40, Atacante1)

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
        
Objeto41 = D2()

A2.Mostrar(Objeto41)
B2.Mostrar(Objeto41)
C2.Mostrar(Objeto41)
Objeto41.Mostrar()
E2.Mostrar(Objeto41)

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
        
Objeto42 = Efectivo2()
Objeto43 = Tarjeta2()
Objeto44 = Cripto2()

Objeto42.Pagar()
Objeto43.Pagar()
Objeto44.Pagar()

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
        
Objeto45 = Cuenta_Bancaria2(100)
Objeto45.Depositar(25)
Objeto45.Mostrar()

print (f'Hay un saldo privado que no deberia ser publico, este saldo es {Objeto45.Dinero}')

Objeto45.Dinero = '50,000,000'

Objeto45.Mostrar()

print (f'Hay un saldo privado que no deberia ser publico, este saldo es {Objeto45.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla2(Plantilla2):
    def Mostrar(self):
        print (f'Este metodo pertenece a esta clase')
        
    def General(self):
        print (f'Este metodo pertenece a la plantilla 2')
        
Objeto46 = Sub_Plantilla2()

Objeto46.Mostrar()
Objeto46.General()

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
    
class Battle3():
    def __init__(self):
        self.Favorito = Bulbasaur2()
        
    def Batallar(self):
        print (f'El retador ha elegido a {self.Favorito.Elegir()} para la batalla!!!')
        
Objeto47 = Battle3()

Objeto47.Batallar()

print (f'-' * 20)

class Battle4():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El retador ha elegido a {self.Favorito.Elegir()} para la batalla!!!')
        
Criatura4 = Bulbasaur2()
Objeto48 = Battle4(Criatura4)
Objeto48.Batallar()

Criatura5 = Treekoo2()
Objeto49 = Battle4(Criatura5)
Objeto49.Batallar()

Criatura6 = Chikorita2()
Objeto50 = Battle4(Criatura6)
Objeto50.Batallar()

print (f'-' * 20)

Lista_Elementos8 = [-10, -5, -20]

def encontrar_mayor(Lista):
    if (len(Lista) == 0):
        return f'No se puede evaluar esta lista ya que esta vacia'
    else:
        Temporal = Lista[0]
        for elemento in Lista:
            if (elemento > Temporal):
                Temporal = elemento
                
        return f'De la lista, el numero mayor es {Temporal}'

print (f'{encontrar_mayor(Lista_Elementos8)}')

print (f'-' * 20)

Lista_Elementos9 = []

def encontrar_menor(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Temporal = Lista[0]
        for elemento in Lista:
            if (elemento < Temporal):
                Temporal = elemento
                
        return Temporal

Resultado = encontrar_menor(Lista_Elementos9)

if (Resultado == None):
    print (f'Error, la lista no puede evaluarse ya que esta vacia')
else:
    print (f'El menor de los numeros de la lista es {Resultado}')
    
print (f'-' * 20)

Lista_Elementos10 = [1, 2]
Lista_Elementos10.append(3)
Lista_Elementos10.insert(4, 4)
Lista_Elementos10.extend([5])
    
def Ejercicio31(Lista):
    Contador = 0
    for elemento in Lista:
        Contador += 1
        
    return Contador

print (f'La lista seleccionada tiene {Ejercicio31(Lista_Elementos10)} elementos')

print (f'-' * 20)

def Ejercicio32(Lista):
    Contador_Pares = 0
    for elemento in Lista:
        if (elemento % 2 == 0):
            Contador_Pares += elemento
        else:
            continue
        
    return Contador_Pares

print (f'Si tomo todos los elementos pares y los sumo, me da el numero {Ejercicio32(Lista_Elementos10)}')

print (f'-' * 20)

def Ejercicio33(Lista):
    Contador = 0
    for elemento in Lista:
        Contador += elemento
        
    return Contador

print (f'La suma de todos los elementos de la lista es {Ejercicio33(Lista_Elementos10)}')

print (f'-' * 20)

def Ejercicio34(Lista, Numero):
    Founder = False
    for elemento in Lista:
        if (elemento == Numero):
            Founder = True
            break
        else:
            continue
        
    return Founder

if (Ejercicio34(Lista_Elementos10, 4) == True):
    print (f'El numero fue encontrado')
else:
    print (f'Error, el numero no fue encontrado')
    
print (f'-' * 20)

def Ejercicio35(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    Lista_Resultado = [Menore, Mayore]
    
    return Lista_Resultado

print (f'El menor de los numeros de la lista es {min(Ejercicio35(Lista_Elementos10))}')
print (f'El mayor de los numeros de la lista es {max(Ejercicio35(Lista_Elementos10))}')

print (f'-' * 20)

def Ejercicio36(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    return Menore, Mayore

Menore3, Mayore3 = Ejercicio36(Lista_Elementos10)

print (f'El menor de los numeros de la lista es {Menore3}')
print (f'El mayor de los numeros de la lista es {Mayore3}')

print (f'-' * 20)

def Ejercicio37(Lista, Numero):
    Contador = 0
    for elemento in Lista:
        if (elemento > Numero):
            Contador+= 1
        else:
            continue
        
    return Contador

print (f'La cantidad de numeros mayores a 2 es {Ejercicio37(Lista_Elementos10, 2)}')

print (f'-' * 20)

def Ejercicio38(Lista):
    Lista_Pares = list([])
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            continue
        
    return Lista_Pares

print (f'Pares: {Ejercicio38(Lista_Elementos10)}')

def Ejercicio39(Lista):
    Lista_ImPares = list([])
    for elemento in Lista:
        if (elemento % 2 != 0):
            Lista_ImPares.append(elemento)
        else:
            continue
        
    return Lista_ImPares

print (f'ImPares: {Ejercicio39(Lista_Elementos10)}')

print (f'-' * 20)

def Ejercicio40(Lista):
    Lista_Mult = []
    for elemento in Lista:
        Lista_Mult.append(elemento * 2)
        
    return Lista_Mult

print (f'Lista original: {Lista_Elementos10}')
print (f'Lista Actualizada: {Ejercicio40(Lista_Elementos10)}')

print (f'-' * 20)

'''Lista_Promedios = list([])

Contador = 0

while (Contador < 3):
    while True:
        Numerito6 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito7 = float(Numerito6)
            if (Numerito7.is_integer()):
                Lista_Promedios.append(Numerito7)
                break
            else:
                Lista_Promedios.extend([Numerito7])
                break
        except ValueError:
            print (f'Error, el valor ingresado no es un numero, intente nuevamente')
    Contador+= 1
    
print (f'Notas {Lista_Promedios}')

Promedio3 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas seleccionadas es {round(Promedio3, 2)}')'''

def Ejercicio41(Lista):
    Lista_Pares = []
    Lista_Impares = list([])
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            Lista_Impares.extend([elemento])
            
    return Lista_Pares, Lista_Impares

Pares2, Impares2 = Ejercicio41(Lista_Elementos10)

print (f'PARES: {Pares2}')
print (f'IMPARES: {Impares2}')

print (f'-' * 20)

Lista_Elementos11 = [5, -6, 0, 0, -3, 0]

def Ejercicio42(Lista):
    Positivos = 0
    Negativos = 0
    Ceros = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Positivos += 1
        elif (elemento < 0):
            Negativos += 1
        else:
            Ceros += 1
            
    return Positivos, Negativos, Ceros

POSITIVE2, NEGATIVE2, ZERO2 = Ejercicio42(Lista_Elementos11)

print (f'Numeros Positivos: {POSITIVE2}')
print (f'Numeros Negativos: {NEGATIVE2}')
print (f'Numeros Ceros: {ZERO2}')

print (f'-' * 20)

import re

Lista_Elementos12 = [
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
]

def Ejercicio43(Lista):
    
    Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'
    
    Lista_Validos = []
    Lista_Invalidos = list([])
    
    for elemento in Lista:
        Buscar25 = bool(re.fullmatch(Pattern, elemento))
        
        if (Buscar25 == True):
            Lista_Validos.append(elemento)
        else:
            Lista_Invalidos.extend([elemento])
            
    return Lista_Validos, Lista_Invalidos

Validos2, Invalidos2 = Ejercicio43(Lista_Elementos12)

print (f'Correos validos: {Validos2}')
print (f'Correos invalidos: {Invalidos2}')

print (f'-' * 20)

Lista_Elementos13 = [3, 1, 2]

def Ejercicio44(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Temporal = Lista[0]
        for elemento in Lista:
            if (elemento > Temporal):
                Temporal = elemento
            else:
                continue
            
    return Temporal

if (Ejercicio44(Lista_Elementos13) == None):
    print (f'Error, la lista esta vacia, no se puede evaluar')
else:
    print (f'De la lista, el numero mayor es {Ejercicio44(Lista_Elementos13)}')
    
print (f'-' * 20)

Lista_Elementos13 = [3, 1, 2]

def Ejercicio45(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Temporal = Lista[0]
        for elemento in Lista:
            if (elemento < Temporal):
                Temporal = elemento
            else:
                continue
            
    return Temporal

if (Ejercicio45(Lista_Elementos13) == None):
    print (f'Error, la lista esta vacia, no se puede evaluar')
else:
    print (f'De la lista, el numero menor es {Ejercicio45(Lista_Elementos13)}')
    
print (f'-' * 20)

class Persona3():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto51 = Persona3('Erick Perez')

print (f'Hola, mi nombre es {Objeto51}')

print (f'-' * 20)

class Colores3():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Colores3 = list([
    Colores3('Magenta'),
    Colores3('Sian'),
    Colores3('Morado')
])

print (f'La lista de colores es {Lista_Colores3}')

print (f'-' * 20)

class Inventario3():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto52 = Inventario3()

Objeto52.Productos.append('Erick')
Objeto52.Productos.insert(1, 'Josue')
Objeto52.Productos.extend(['Karlita'])

print (f'La cantidad de elementos en la lista es {len(Objeto52)}')

print (f'-' * 20)

class Igualdad3():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto53 = Igualdad3('Panda Rojo')
Objeto54 = Igualdad3('Panda Rojo')

if (Objeto53 == Objeto54):
    print (f'Ambos objetos son iguales')
else:
    print (f'Error, los objetos no son iguales')
    
print (f'-' * 20)

class Cajas3():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto55 = Cajas3(4)
Objeto56 = Cajas3(3)

print (f'La suma de los numeros es {Objeto55 + Objeto56}')

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
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Objeto57 = Pastel3()

Objeto57.Hornear()

print (f'-' * 20)

class Pastel4():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Ingrediente4 = Chocolate2()
Objeto58 = Pastel4(Ingrediente4)
Objeto58.Hornear()

Ingrediente5 = Vainilla2()
Objeto59 = Pastel4(Ingrediente5)
Objeto59.Hornear()

Ingrediente6 = Fresa2()
Objeto60 = Pastel4(Ingrediente6)
Objeto60.Hornear()

print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un
Long
String'''

variable4 = Objeto13.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = True, Objeto12.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke3"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene un total de {Objeto13.Cantidad} pokemones')

del variable5

print (f'ubana' in Saludar_Dos())
print (f'Long' not in  variable3)

print (f'Koala' in PEPE.Lista2)
print (f'Brooke' in PEPE.Tupla_Poke)
print (f'Raykuasa' not in PEPE.Set_Conjunto_Poke1)

print (f'-' * 20)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables y snake case {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto12.Cantidad, Sumatoria2(1, 2, 2))

print (f'El Cociente de la operacion es {Cociente}')
print (f'El Residuo de la operacion es {Residuo}')

print (f'{PEPE.Lista2[::2]}')
print (f'{PEPE.Lista2[::3]}')
print (f'{PEPE.Lista2[:2]}')
print (f'{PEPE.Lista2[2:]}')
print (f'{PEPE.Lista2[2:3]}')
print (f'{PEPE.Lista2[0:None]}')
print (f'{PEPE.Lista2[:]}')

print (f'{Lista_Uno[0]} eso que estamos viendo ahi es un {PEPE.Lista2[2]}?')

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
print (f'{Lista_Uno_Copia}')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'-' * 20)

print (f'{dir(PEPE)}')

Tupla1 = ('Uno', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos')

print (f'{Tupla1}')

Tupla1 = tuple(('Uno', 'Dos', 'Tres'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{Tupla1}')
print (f'{Tupla2}')
print (f'{Tupla3}')
print (f'{Tupla1[2:3]}')

print (f'-' * 20)

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Variable_Funcion_Tupla)}')

print (f'-' * 20)

Set_Conjunto1 = {'Roca', Objeto13.Tipo, Objeto13.Tipo, Objeto13.Tipo, Objeto13.Tipo, Objeto13.Tipo}
Set_Conjunto1.add('Electrico')

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

SetA2 = {1, 2, 3, 4}
SetB2 = {3, 4,5 , 6}

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

print (f'-' * 20)

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})

Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, 'ChocoBanano'})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Objeto13.Cantidad,
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
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
}

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2.values()}')
print (f'{Diccionario2.items()}')
print (f'{Diccionario2["Nombre"][1]}')
print (f'{Diccionario2.get("Edad")[2]}') #type: ignore

print (f'-' * 20)

Diccionario3 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3.values()}')
print (f'{Diccionario3.items()}')
print (f'{Diccionario3["Ingresos"]}')
print (f'{Diccionario3.get("Gastos")}')

print (f'-' * 20)

Diccionario1_Copia = Diccionario1.copy()

Diccionario1['Nombre'] = variable1

print (f'{Diccionario1}')

del Diccionario1['Nombre']
Diccionario1.pop('Edad')

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')

print (f'-' * 20)

Diccionario1 = dict({1 : "Karlita", 2 : 6, 3 : not True})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'{Diccionario2["Nombre"][2]} no puede votar ya que solo tiene {Diccionario1.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'Huevo')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = 'Egg'

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

Key1 = [f'Key{i}' for i in range(len(Lista_Uno_Copia))]

Diccionario4 = dict(zip(Key1, Lista_Uno_Copia))

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Key1"]}')
print (f'{Diccionario4.get("Key2")}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

print (f'-' * 20)

Fecha3 = '2026-04-01'

try:
    Fech3 = datetime.strptime(Fecha3, '%Y-%m-%d').date()
    Fech3_Formateada = pd.to_datetime(Fech3)
    Cargar_Csv3['date'] = pd.to_datetime(Cargar_Csv3['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato incorrecto')
    exit()
    
Cargar_Csv3['TOTALITO'] = Cargar_Csv3['quantity'] * Cargar_Csv3['price']
    
Encontrado3 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech3_Formateada.date()]

if (Encontrado3.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! se han encontrado ventas en esta fecha')
    
    Grupo4 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo4_Min = Grupo4.idxmin()
    Grupo4_Max = Grupo4.idxmax()
    Grupo4_Min_Cant = Grupo4.min()
    Grupo4_Max_Cant = Grupo4.max()
    
    print (f'En la fecha {Fech3_Formateada}, el producto {Grupo4_Min} vendio un total de {Grupo4_Min_Cant} unidades')
    print (f'En la fecha {Fech3_Formateada}, el producto {Grupo4_Max} vendio un total de {Grupo4_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que nos compraron en esta fecha fue de {Grupo4.count()}')
    print (f'La cantidad de productos que se vendieron en esta fecha fue de {Grupo4.sum()}')
    
    Grupo5 = Encontrado3.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue de ${Grupo5.sum()}')
    
    Promedio3 = Grupo5.sum() / Grupo4.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio3, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${Grupo5.mean()}')
    
print (f'-' * 20)

Lista_Cargar_Csv3 = list(Cargar_Csv3['product'])

print (f'{Lista_Cargar_Csv3}')

Key2 = [f'Key_{i}' for i in range(len(Lista_Cargar_Csv3))]

print (f'{Key2}')

Diccionario5 = dict(zip(Key2, Lista_Cargar_Csv3))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key_4"]}')
print (f'{Diccionario5.get("Key_6")}')

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
print (f'El tipo de dato de la variable es {type(variable6)}')
print (f'El tipo de dato de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato de la variable es {type(PEPE.Tupla_Poke)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu3)}')
print (f'El tipo de dato de la variable es {type(Diccionario1_Copia)}')
print (f'El tipo de dato de la variable es {type(Objeto10)}')
print (f'El tipo de dato de la variable es {type(Funcion_Diccionario)}')
print (f'El tipo de dato de la variable es {type(Array2_Sorted)}')
print (f'El tipo de dato de la variable es {type(Data_Frame2)}')
print (f'El tipo de dato de la variable es {type(PEPE)}')

print (f'-' * 20)

Lista_Elementos14 = []

def sumar_positivos(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador_Positivos = 0
        for elemento in Lista:
            if (elemento > 0):
                Acumulador_Positivos += elemento
                    
        return Acumulador_Positivos

if (sumar_positivos(Lista_Elementos14) == None):
    print (f'Error, no podemos realizar la operacion ya que la lista esta vacia')
else:
    print (f'El resultado de sumar los numeros positivos de la lista es {sumar_positivos(Lista_Elementos14)}')
    
print (f'-' * 20)

Lista_Elementos15 = [-5, -10, -2]

def analizar_positivos(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador_Positivos = 0
        Suma_Positivos = 0
            
        for elemento in Lista:
            if (elemento > 0):
                Contador_Positivos += 1
                Suma_Positivos += elemento
                    
        return Contador_Positivos, Suma_Positivos
    
if (analizar_positivos(Lista_Elementos15) == None):
    print (f'Error, la lista elegida no tiene elementos')
else:
    Positivos, Sumatoria = analizar_positivos(Lista_Elementos15) #type: ignore
    
    print (f'La cantidad de numeros positivos en la lista es {Positivos}')
    print (f'La sumatoria de estos numeros positivos es {Sumatoria}')
    
print (f'-' * 20)

Lista_Elementos16 = [85, 42, 91, 67, 100, 58, 73]

def analizar_notas(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Aprobados = 0
        Reprobados = 0
        Suma_Aprobados = 0
        for elemento in Lista:
            if (elemento >= 70):
                Aprobados += 1
                Suma_Aprobados += elemento
            else:
                Reprobados += 1
                
    return Aprobados, Reprobados, Suma_Aprobados

Resultado = analizar_notas(Lista_Elementos16)

if (Resultado == None):
    print (f'Error, la lista esta vacia')
else:
    Alumnos_Aprobados, Alumnos_Reprobados, Sumatoria_Aprobados = Resultado
    
    print (f'La cantidad de alumnos que aprobaron el curso es {Alumnos_Aprobados}')
    print (f'La cantidad de alumnos que reprobaron el curso es {Alumnos_Reprobados}')
    print (f'La suma de las notas de los estudiantes que aprobaron es {Sumatoria_Aprobados}')
    
print (f'-' * 20)

Lista_Elementos17 = [120, 0, 350, 80, 0, 40, 600]

def analizar_ventas(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador_Ventas_Reales = 0
        Contador_Ventas_No_Reales = 0
        Total_Vendido = 0
            
        for elemento in Lista:
            if (elemento > 0):
                Contador_Ventas_Reales += 1
                Total_Vendido += elemento
            else:
                Contador_Ventas_No_Reales += 1
                
    return Contador_Ventas_Reales, Contador_Ventas_No_Reales, Total_Vendido

Resultado2 = analizar_ventas(Lista_Elementos17)

if Resultado2 is None:
    print (f'Error, la lista esta vacia y no puede evaluarse')
else:
    Ventas, No_Ventas, Total = Resultado2
    
    print (f'La cantidad de ventas registradas en el dia fue de {Ventas}')
    print (f'La cantidad de clientes que no compraron en el dia fue de {No_Ventas}')
    print (f'El monto total vendido en el dia fue de ${Total}')
    
if (Diccionario3['Ingresos'] > 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos altos, Gastos bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos altos, Gastos al limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos altos, Gastos altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] == 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Minimos, Gastos bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos Minimos, Gastos al limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Minimos, Gastos altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] < 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos bajos, Gastos bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos bajos, Gastos al limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos bajos, Gastos altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')
    
print (f'-' * 20)

variable8 = 'Josue'
variable9 = Sumatoria2(1, 2, 1, 3)

if (variable8 == 'Erick' and variable9 > 30):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')
    
print (f'-' * 20)

if (variable8 == 'Erick' or variable9 > 30):
    print (f'Al menos una de las condiciones se cumple')
else:
    print (f'Error, ninguna de las condiciones se cumple')
    
print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = 10
        self.Classified = True

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')
        
Objeto61 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index('Ash')], 'Kanto', Objeto12.Nombre)
Objeto62 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index('Brooke')], 'Alolah', Objeto13.Nombre)

Objeto61.Desplegar()

print (f'-' * 20)

Objeto62.Desplegar()

print (f'-' * 20)

Negativo = -11

print (f'El numero es {int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima4 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable}')
print (f'{list(Anonima4)}')
print (f'{Lista_Iterable}')

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error! Ingrese una cadena de texto')
    
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

print (f'La letra t aparece en la posicion {variable10.lower().find("t")}')
print (f'La letra b aparece en la posicion {variable10.lower().index("b")}')

print (f'La letra e aparece un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}') 

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = 'esto es una cadena de texto cualquiera'

Lista_variable11 = variable11.split(' ')

for elemento in Lista_variable11:
    print (f'{elemento}')
    
print (f'La cantidad de palabras digitadas es {len(Lista_variable11)}')

print (f'-' * 20)

var10 = 'texto'

if (isinstance(var10, (str))):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Error, lo que ingresaste no es texto')
    
if (var10.isalpha()):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Error, lo que ingresaste no es texto')
    
try:
    Numerito6 = float(var10)
    if (Numerito6.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado es texto')
    
print (f'-' * 20)

var11 = '3.5'

if (isinstance(var11, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Error, lo ingresado no es un numero decimal')
    
try:
    Numerito7 = float(var11)
    if (Numerito7.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado es texto')
    
print (f'-' * 20)

var12 = '3'

if (isinstance(var12, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var12.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
try:
    Numerito8 = float(var12)
    if (Numerito8.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado es texto')
    
print (f'-' * 20)

var13 = 'erick123'

if (isinstance(var13, (int, float, str))):
    print (f'Esto puede tener letras o numeros')
else:
    print (f'Error de formato')
    
if (var13.isalnum()):
    print (f'Esto puede tener letras o numeros')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var14 = '    s      '

if (var14.isspace()):
    print (f'Esto esta compuesto por solo espacios')
else:
    print (f'Error, esto tiene mas que solo espacios')
    
var15 = ''

if (bool(var15)):
    print (f'Esto tiene contenido')
else:
    print (f'Esto esta completamente vacio')
    
print (f'-' * 20)

var16 = 'eSteBAN'

if (var16.lower().islower()):
    print (f'Esto esta compuesto nada mas por minusculas')
else:
    print (f'Error, esto tiene mas que solo minusculas')
    
if (var16.upper().isupper()):
    print (f'Esto esta compuesto nada mas por mayusculas')
else:
    print (f'Error, esto tiene mas que solo mayusculas')
    
print (f'-' * 20)

print (f'{PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

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
    
Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador += 1
    
print (f'-' * 20)

Lista_Animales = ['Cocodrilo']
Lista_Animales.append(f'{PEPE.Lista2[2]}')
Lista_Animales.insert(1, 'Leon')
Lista_Animales.extend(['Escarabajo'])

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Koala'):
        print (f'Este bichillo viene de Australia')
        break
    else:
        Contador += 1
        continue
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Animales, Set_Conjunto1):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento1, elemento2, elemento3, elemento4 in zip(Lista_Animales, Set_Conjunto1, Lista_Uno_Copia, PEPE.Tupla_Poke):
    print (f'{elemento1} -- {elemento2} -- {elemento3} -- {elemento4} ')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
print (f'-' * 20)

Lista_Multiplicado = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Multiplicado}')

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1
    
print (f'-' * 20)

Menor = min(Lista_Multiplicado)
Mayor = max(Lista_Multiplicado)

print (f'El menor de los numeros es {Menor} y el mayor de los numeros es {Mayor}')

Redondeado = round(14.458795, 2)

print (f'El numero redondeado es {Redondeado}')

print (f'{bool(False)}')
print (f'{bool(not True)}')
print (f'{bool(0)}')
print (f'{bool(None)}')
print (f'{bool("")}')

print (f'-' * 20)

Todo_All = all([Lista_Animales, PEPE.Tupla_Poke, Set_Conjunto1, ""])

print (f'{Todo_All}')

Sumatoria4 = sum(Lista_Multiplicado)

print (f'El resultado de la sumatoria es {Sumatoria4}')

Uno = str(500)
Dos = int('500')
Tres = float(Uno)
Cuatro = set(Lista_Multiplicado)
Cinco = tuple(Set_Conjunto_Menu1)
Seis = list(PEPE.Tupla_Poke)

print (f'{type(500)} -- {type(Uno)}')
print (f'{type('500')} -- {type(Dos)}')
print (f'{type(Uno)} -- {type(Tres)}')
print (f'{type(Lista_Multiplicado)} -- {type(Cuatro)}')
print (f'{type(Set_Conjunto_Menu1)} -- {type(Cinco)}')
print (f'{type(PEPE.Tupla_Poke)} -- {type(Seis)}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto_Poke1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

print (f'-' * 20)

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

print (f'-' * 20)

'''def Exception_Finale():
    while True:
        Elemento = input(f'Ingrese un numero: ')
        try:
            Numerito9 = float(Elemento)
            if (Numerito9.is_integer()):
                print (f'Lo que ingreso fue un numero entero')
                break
            else:
                print (f'Lo que ingreso fue un numero decimal')
                break
        except ValueError:
            print (f'Error, lo ingresado no es un numero, intente nuevamente')

Exception_Finale()'''

import pandas as pd
import requests
import io

Ruta_Html2 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html2, headers=headers)

Leer_Html2 = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Leer_Html2)

print (f'{Cargar_Html2[3].head()}')

print (f'-' * 20)

import re

Texto12 = 'sample@sample.com'

Pattern14 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.[a-z]{2,}'

Buscar25 = bool(re.fullmatch(Pattern14, Texto12))

if (Buscar25 == True):
    print (f'El correo electronico tiene el formato correcto')
else:
    print (f'Error, el correo electronico tiene un formato invalido')
    
print (f'-' * 20)

import re

Texto13 = 'ericksuper80@hotmail.com'

Pattern15 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)$'

Buscar26 = bool(re.fullmatch(Pattern15, Texto13))

if (Buscar26 == True):
    print (f'El correo electronico tiene el formato correcto')
else:
    print (f'Error, el correo electronico tiene un formato invalido')
    
print (f'-' * 20)

import re

Texto14 = '32'

Pattern16 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar26 = bool(re.match(Pattern16, Texto14))

if (Buscar26 == True):
    print (f'El numero esta entre 1 y 31')
else:
    print (f'Error el numero esta fuera de rango')
    
print (f'-' * 20)

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
    print (f'Error, el formato de la fecha es invalido')
    exit()
    
Cargar_Csv4['TOTALITO'] = Cargar_Csv4['quantity'] * Cargar_Csv4['price']
    
Encontrado4 = Cargar_Csv4[Cargar_Csv4['date'].dt.date == Fech4_Formateada.date()]

if (Encontrado4.empty):
    print (f'No hay ventas registradas en esta fecha')
else:
    print (f'Genial! Encontramos ventas en esta fecha')
    
    Grupo6 = Encontrado4.groupby('product')['quantity'].sum()
    Grupo6_Min = Grupo6.idxmin()
    Grupo6_Max = Grupo6.idxmax()
    Grupo6_Min_Cant = Grupo6.min()
    Grupo6_Max_Cant = Grupo6.max()
    
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo6_Min} vendio un total de {Grupo6_Min_Cant} unidades')
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo6_Max} vendio un total de {Grupo6_Max_Cant} unidades')
    
    print (f'La cantidad de clietnes que nos compraron en esta fecha fue de {Grupo6.count()}')
    print (f'La cantidad de productos vendidos en esta fecha fue de {Grupo6.sum()}')
    
    Grupo7 = Encontrado4.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue de ${Grupo7.sum()}')
    
    Promedio4 = Grupo7.sum() / Grupo6.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio4, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${Grupo7.mean()}')
    
print (f'-' * 20)

Lista_Elementos18 = [1, 2, 3, 4, 5]

def Ejercicio46(Lista):
    Contador = 0
    while (Contador < len(Lista)):
        Contador += 1
        
    return Contador

print (f'La lista tiene {Ejercicio46(Lista_Elementos18)} elementos')

print (f'-' * 20)

def Ejercicio47(Lista):
    Acumulador = 0
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador += elemento
            
    return Acumulador

print (f'Si tomo todos los numeros pares de la lista y los sumo, me da el numero {Ejercicio47(Lista_Elementos18)}')

print (f'-' * 20)

def Ejercicio48(Lista):
    Acumulador = 0
    for elemento in Lista:
        Acumulador += elemento
        
    return Acumulador

print (f'Si sumo todos los elementos de la lista me da el numero {Ejercicio48(Lista_Elementos18)}')

print (f'-' * 20)

def Ejercicio49(Lista, Numero):
    Founder = False
    for elemento in Lista:
        if (elemento == Numero):
            Founder = True
            break
        else:
            continue
        
    return Founder

if (Ejercicio49(Lista_Elementos18, 2) == True):
    print (f'El numero fue encontrado')
else:
    print (f'Error, el numero no fue encontrado')
    
print (f'-' * 20)

def Ejercicio50(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    Lista_Resultado = [Menore, Mayore]
    
    return Lista_Resultado

print (f'El numero menor de la lista es {Ejercicio50(Lista_Elementos18)[0]}')
print (f'El numero mayor de la lista es {Ejercicio50(Lista_Elementos18)[1]}')

print (f'El numero menor de la lista es {min(Ejercicio50(Lista_Elementos18))}')
print (f'El numero mayor de la lista es {max(Ejercicio50(Lista_Elementos18))}')

print (f'-' * 20)

def Ejercicio51(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    return Menore, Mayore

Min, May = Ejercicio51(Lista_Elementos18)

print (f'El numero menor de la lista es {Min}')
print (f'El numero mayor de la lista es {May}')

print (f'-' * 20)

def Ejercicio52(Lista, Numero):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        for elemento in Lista:
            if (elemento > Numero):
                Contador += 1
            else:
                continue
            
    return Contador

Resultado3 = Ejercicio52(Lista_Elementos18, 1)

if (Resultado3 is None):
    print (f'Error, la lista que elegiste esta vacia')
else:
    print (f'La cantidad de numeros que son mayores que 1 en la lista es {Resultado3}')
    
print (f'-' * 20)

def Ejercicio53(Lista):
    Lista_Pares = list([])
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            continue
        
    return Lista_Pares

print (f'La sub lista de numeros pares es {Ejercicio53(Lista_Elementos18)}')

print (f'-' * 20)

def Ejercicio54(Lista):
    Lista_ImPares = list([])
    
    for elemento in Lista:
        if (elemento % 2 != 0):
            Lista_ImPares.append(elemento)
        else:
            continue
        
    return Lista_ImPares

print (f'La sub lista de numeros impares es {Ejercicio54(Lista_Elementos18)}')

print (f'-' * 20)

def Ejercicio55(Lista):
    Lista_Mult = []
    
    for elemento in Lista:
        Lista_Mult.append(elemento * 2)
        
    return Lista_Mult

print (f'Lista Original: {Lista_Elementos18}')
print (f'Lista Actualizada {Ejercicio55(Lista_Elementos18)}')

'''Lista_Promedios = []

Contador = 0

while (Contador < 3):
    while True:
        Numerito9 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito10 = float(Numerito9)
            if (Numerito10.is_integer()):
                print (f'El numero ingresado es entero')
                Lista_Promedios.append(Numerito10)
                break
            else:
                print (f'El numero ingresado es decimal')
                Lista_Promedios.append(Numerito10)
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador += 1
    
print (f'{Lista_Promedios}')

Promedio5 = sum(Lista_Promedios) / Lista_Promedios.__len__()

print (f'El promedio de las notas ingresadas es {round(Promedio5, 2)}')'''

print (f'-' * 20)

def Ejercicio56(Lista):
    Lista_Pares = []
    Lista_Impares = list([])
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            Lista_Impares.extend([elemento])
            
    return Lista_Pares, Lista_Impares

Pares4, Impares4 = Ejercicio56(Lista_Elementos18)

print (f'Lista Pares: {Pares4}')
print (f'Lista ImPares: {Impares4}')

print (f'-' * 20)

Lista_Elementos19 = [5, -6, 0, -1, -3, 0]

def Ejercicio57(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador_Positivo = 0
        Contador_Negativo = 0
        Contador_Cero = 0
        
        for elemento in Lista:
            if (elemento > 0):
                Contador_Positivo += 1
            elif (elemento < 0):
                Contador_Negativo += 1
            else:
                Contador_Cero += 1
                
    return Contador_Positivo, Contador_Negativo, Contador_Cero

Resultado4 = Ejercicio57(Lista_Elementos19)

if (Resultado4 is None):
    print (f'Error, la lista elegida esta vacia')
else:
    POSITIVE3, NEGATIVE3, ZERO3 = Resultado4
    
    print (f'Positivos: {POSITIVE3}')
    print (f'Negativos: {NEGATIVE3}')
    print (f'Ceros: {ZERO3}')
    
print (f'-' * 20)

import re

Lista_Elementos20 = [
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
]

def Ejercicio58(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Validos = []
        Lista_Invalidos = list([])
        
        Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'
        
        for elemento in Lista:
            Buscar = bool(re.fullmatch(Pattern, elemento))
            
            if (Buscar == True):
                Lista_Validos.append(elemento)
            else:
                Lista_Invalidos.append(elemento)
                
    return Lista_Validos, Lista_Invalidos

Resultado5 = Ejercicio58(Lista_Elementos20)

if (Resultado5 is None):
    print (f'Error, la lista de correos esta vacia')
else:
    Validos3, Invalidos3 = Resultado5
    
    print (f'Correos Validos: {Validos3}')
    print (f'Correos Invalidos: {Invalidos3}')
    
print (f'-' * 20)

def Ejercicio59(Lista):
    Temporal = Lista[0]
    
    for elemento in Lista:
        if (elemento > Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

print (f'El numero mayor de toda la lista es {Ejercicio59(Lista_Elementos18)}')

print (f'-' * 20)

def Ejercicio60(Lista):
    Temporal = Lista[0]
    
    for elemento in Lista:
        if (elemento < Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

print (f'El numero menor de toda la lista es {Ejercicio60(Lista_Elementos18)}')

print (f'-' * 20)

def Ejercicio61(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        Acumulador = 0
        
        for elemento in Lista:
            if (elemento > 0):
                Contador += 1
                Acumulador += elemento
            else:
                continue
            
    return Contador, Acumulador

Resultado6 = Ejercicio61([5, -6, 0, -1, -3, 0])

if (Resultado6 is None):
    print (f'Error, la lista seleccionada esta vacia')
else:
    Total_Positivos, Suma_Positivos = Resultado6
    
    print (f'Cantidad total de positivos: {Total_Positivos}')
    print (f'Suma de estos numeros positivos: {Suma_Positivos}')
    
print (f'-' * 20)

Lista_Elementos21 = [65, 70, 54, 80, 69, 66]

def Ejercicio62(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Aprobados = 0
        Reprobados = 0
        Notas_Aprobados = 0
        
        for elemento in Lista:
            if (elemento >= 70):
                Aprobados += 1
                Notas_Aprobados += elemento
            else:
                Reprobados += 1
                
    return Aprobados, Reprobados, Notas_Aprobados

Resultado7 = Ejercicio62(Lista_Elementos21)

if (Resultado7 is None):
    print (f'Error, la lista esta vacia')
else:
    Alumnos_Aprobados2, Alumnos_Reprobados2, Sumatoria_Aprobados2 = Resultado7
    
    print (f'Alumnos Aprobados: {Alumnos_Aprobados2}')
    print (f'Alumnos Reprobados: {Alumnos_Reprobados2}')
    print (f'Suma notas aprobadas: {Sumatoria_Aprobados2}')
    
print (f'-' * 20)

Lista_Elementos22 = [120, 0, 350, 80, 0, 40, 600]

def Ejercicio63(Lista):
    Ventas = 0
    No_Ventas = 0
    Total_Ventas = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Ventas += 1
            Total_Ventas += elemento
        else:
            No_Ventas += 1
            
    return Ventas, No_Ventas, Total_Ventas

Sales, Unsales, Total_Sales = Ejercicio63(Lista_Elementos22)

print (f'La cantidad de ventas del dia es {Sales}')
print (f'Clientes que entraron pero no compraron {Unsales}')
print (f'Total de dinero vendido en el dia ${Total_Sales}')