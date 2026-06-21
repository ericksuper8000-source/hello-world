try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo no existe')
    raise

var1 = 'hola'

if (var1.isnumeric()):
    print (f'El numero es entero')
else:
    print (f'Error el numero no es entero')
    
if (isinstance(var1, (int))):
    print (f'El numero es entero')
else:
    print (f'Error el numero no es entero')
    
try:
    Numerito1 = float(var1)
    if (Numerito1.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var2 = 3.5

if (isinstance(var2, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Error, lo ingresado no es un numero decimal')
    
try:
    Numerito2 = float(var2)
    if (Numerito2.is_integer()):
        print (f'El numero ingresado es entero')
    else:
        print (f'El numero ingresado es decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero') 
    
print (f'-' * 20)

var3 = '3'

if (isinstance(var3, (int, float))):
    print (f'Lo ingresado es un numero entero o decimal')
else:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var4 = 'hola'

if (var4.isalpha()):
    print (f'Lo ingresado es un texto')
else:
    print (f'Error, lo ingresado no es un texto')
    
if (isinstance(var4, (str))):
    print (f'Lo ingresado es un texto')
else:
    print (f'Error, lo ingresado no es un texto')
    
try:
    Numerito3 = float(var4)
    if (Numerito3.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado es un texto')
    
print (f'-' * 20)

var5 = 'erick123'

if (var5.isalnum()):
    print (f'Lo ingresao es texto o numero')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var6 = 'eSteBAN'

if (var6.lower().islower()):
    print (f'Lo ingresado esta en minuscula')
else:
    print (f'Error, formato incorrecto')
    
if (var6.upper().isupper()):
    print (f'Lo ingresado esta en mayuscula')
else:
    print (f'Error, formato incorrecto')
    
print (f'-' * 20)

import re

Texto1 = "   Hola!!!   mundo@@   123   "

print (f'{Texto1}')

Texto1_Version1 = Texto1.strip()

print (f'{Texto1_Version1}')

Texto1_Version2 = ' '.join(Texto1_Version1.split())

print (f'{Texto1_Version2}')

Texto1_Version3 = re.sub(r'\!|\@|\d+', '', Texto1_Version2)

print (f'{Texto1_Version3}')

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
    print (f'Error, la fecha tiene el formato incorrecto')
    exit()
    
Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrada1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()]

if (Encontrada1.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! Ventas encontradas')
    
    Grupo1 = Encontrada1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Min} vendio un total de {Grupo1_Min_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Max} vendio un total de {Grupo1_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que nos compraron en esta fecha fue de {Grupo1.count()}')
    
    Grupo2 = Encontrada1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de productos vendidos en esta fecha fue de {Grupo1.sum()}')
    print (f'La cantidad de dinero vendida en esta fecha fue de ${Grupo2.sum()}')
    
    Promedio1 = Grupo2.sum() / Grupo1.count()
    
    print (f'El promedio de ventas en dolares fue de ${Promedio1}')
    print (f'El promedio de ventas en dolares fue de ${Grupo2.mean()}')
    
    Set_Productos = set(Cargar_Csv1['product'])
    
    Key1 = [f'Key{i}' for i in range(len(Set_Productos))]
    
    Diccionario0 = dict(zip(Key1, Set_Productos))
    
    print (f'{Diccionario0}')
    print (f'{Diccionario0.keys()}')
    print (f'{Diccionario0.values()}')
    print (f'{Diccionario0.items()}')
    print (f'{Diccionario0["Key6"]}')
    print (f'{Diccionario0.get("Key0")}')
    
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

SetC1 = {1, 2, 3, 4, 5}
SetD1 = {4, 5}
SetE1 = set({8})

print (f'{SetC1.issuperset(SetD1)}')
print (f'{SetC1 >= SetD1}')

print (f'{SetD1.issubset(SetC1)}')
print (f'{SetD1 <= SetC1}')

print (f'{SetC1.isdisjoint(SetE1)}')

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
        print (f'{self.Favorito.Elegir()} fue elegido para la batalla!!!')
        
Objeto1 = Battle1()
Objeto1.Batallar()

print (f'-' * 20)

class Battle2:
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'{self.Favorito.Elegir()} fue elegido para la batalla!!!')
        
Criatura1 = Bulbasaur1()
Objeto2 = Battle2(Criatura1)
Objeto2.Batallar()

Criatura2 = Treekoo1()
Objeto3 = Battle2(Criatura2)
Objeto3.Batallar()

Criatura3 = Chikorita1()
Objeto4 = Battle2(Criatura3)
Objeto4.Batallar()

print (f'-' * 20)

class Persona1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
        
Objeto5 = Persona1('Erick Josue')

print (f'Hola, mi nombre es {Objeto5}')

print (f'-' * 20)

class Inventario1():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto6 = Inventario1()

Objeto6.Productos.append('Erick')
Objeto6.Productos.insert(1, 'Josue')
Objeto6.Productos.extend(['Karlita'])

print (f'La cantidad de elementos de la lista es de {len(Objeto6)}')

print (f'-' * 20)

class Igualdad1:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
        
Objeto7 = Igualdad1('Erick')
Objeto8 = Igualdad1('Erick')

print (f'{Objeto7 == Objeto8}')

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

#VERSION1

Pattern1 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar1 = re.findall(Pattern1, Texto2)

print (f'{Buscar1}')

for indice, elemento in enumerate(Buscar1, start=1):
    print (f'{indice} -- {elemento}')

print (f'-' * 20)

Pattern2 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos1 = re.findall(Pattern2, Texto2)

Texto2_temp1 = Texto2

for i, email in enumerate(Correos1, start=1):
    Texto2_temp1 = Texto2_temp1.replace(email, f'TEMPLATE{i}')
    
print (f'{Texto2_temp1}')

print (f'-' * 20)

import re

Texto3 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

#VERSION1

Buscar2 = re.sub(r'\!|\@|\?|\.{2,}', '', Texto3)

print (f'{Buscar2}')

Buscar3 = re.sub(r'\d{4}\-[0-9]{3,4}', '', Buscar2)

print (f'{Buscar3}')

#VERSION2

import re

Pattern3 = r'[^a-zA-Z0-9\s]+'

Buscar4 = re.sub(Pattern3, '', Texto3)

print (f'{Buscar4}')

Buscar5 = re.sub(r'\d{4,}', '', Buscar4)

print (f'{Buscar5}')

#VERSION3

import re

Pattern4 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|net|org)'

Correos2 = re.findall(Pattern4, Texto3)

print (f'{Correos2}')

Texto3_temp1 = Texto3

for i, email in enumerate(Correos2, start=1):
    Texto3_temp1 = Texto3_temp1.replace(email, f'Sample{i}')
    
print (f'{Texto3_temp1}')

Pattern5 = r'\!|\?|\.{2,}|\d{4}\-[0-9]{3,4}'

Texto3_temp2 = re.sub(Pattern5, '', Texto3_temp1)

print (f'{Texto3_temp2}')

for i, email in enumerate(Correos2, start=1):
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

Pattern6 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|net|org)'

Correos3 = re.findall(Pattern6, Texto4)

Texto4_temp1 = Texto4

for i, email in enumerate(Correos3, start=1):
    Texto4_temp1 = Texto4_temp1.replace(email, f'Sample{i}')
    
print (f'{Texto4_temp1}')

Texto4_temp2 = re.sub(r'\!|\?', '', Texto4_temp1)

print (f'{Texto4_temp2}')

for i, email in enumerate(Correos3, start=1):
    Texto4_temp2 = Texto4_temp2.replace(f'Sample{i}', email)
    
print (f'{Texto4_temp2}')

print (f'-' * 20)

for elemento in PEPE.Diccionario_Pokemon:
    print (f'{PEPE.Diccionario_Pokemon[elemento]}')
    
print (f'-' * 20)

for elemento in PEPE.Diccionario_Pokemon.keys():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in PEPE.Diccionario_Pokemon.values():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in PEPE.Diccionario_Pokemon.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

'''Lista_Promedio = list([])

Contador = 0

while (Contador < 3):
    while True:
        Numerito4 = input(f'Ingrese el numero {Contador}: ')
        try:
            Numerito5 = float(Numerito4)
            if (Numerito5.is_integer()):
                print (f'El numero {Contador} es entero')
                Lista_Promedio.append(Numerito5)
                break
            else:
                print (f'El numero {Contador} es decimal')
                Lista_Promedio.extend([Numerito5])
                break
        except ValueError:
            print (f'Error, lo ingresado no es un numero')
    Contador+= 1
    
Promedio2 = sum(Lista_Promedio) / Lista_Promedio.__len__()

print (f'El promedio de las notas agregadas es {round(Promedio2, 2)}')'''

from Module_Own import Pokemon1 as Poke1

Objeto9 = Poke1(PEPE.Diccionario_Pokemon["Poke1"], 'Electrico', 'Impact Trueno')
Objeto10 = Poke1(PEPE.Diccionario_Pokemon["Poke2"], 'Roca', 'Sismo')

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
        
Objeto11 = Poke_Kid1(PEPE.Diccionario_Pokemon["Poke3"], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto11)
Objeto11.Mostrar()

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
        
Objeto12 = Perro1('Chester', 5, 2.8, 'Poodle', 'Asma')

Veterinaria1.Mostrar(Objeto12)
Objeto12.Mostrar()

print (f'-' * 20)

class Gato1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto13 = Gato1('Messi', 1.5, 2, 'Gris', 'No')

Veterinaria1.Mostrar(Objeto13)
Objeto13.Mostrar()

print (f'-' * 20)

class Pajaro1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto14 = Pajaro1('Polly', 31, 0.4, 'Cacatua Blanca', 'Si')

Veterinaria1.Mostrar(Objeto14)
Objeto14.Mostrar()

print (f'-' * 20)

class Atacante1():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon
        
    def Mostrar(self):
        print (f'Damage: {self.Damage}pts')
        print (f'Weapon: {self.Weapon}')
        
class Defensor1():
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
        
Objeto15 = Paladin1(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Atacante1.Mostrar(Objeto15)
Defensor1.Mostrar(Objeto15)
Objeto15.Mostrar()

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
        
Objeto16 = D1()

A1.Mostrar(Objeto16)
B1.Mostrar(Objeto16)
C1.Mostrar(Objeto16)
Objeto16.Mostrar()
E1.Mostrar(Objeto16)

print (f'-' * 20)

class Efectivo1():
    def Pagar(self):
        print (f'El pago se realizo en Efectivo')
        
class Tarjeta1():
    def Pagar(self):
        print (f'El pago se realizo en Tarjeta')
        
class Cripto1():
    def Pagar(self):
        print (f'El pago se realizo en Cripto')
        
Objeto17 = Efectivo1()
Objeto18 = Tarjeta1()
Objeto19 = Cripto1()

Objeto17.Pagar()
Objeto18.Pagar()
Objeto19.Pagar()

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
        
Objeto20 = Cuenta_Bancaria1(100)
Objeto20.Depositar(25)
Objeto20.Mostrar()

print (f'Tu saldo privado, que no deberia de mostrarse fuera de la clase es {Objeto20.Dinero}')

Objeto20.Dinero = '50,000,000'

Objeto20.Mostrar()

print (f'Tu saldo privado, que no deberia de mostrarse fuera de la clase es {Objeto20.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla1(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla1(Plantilla1):
    def Mostrar(self):
        print (f'Este es un metodo interno de sub plantilla')
        
    def General(self):
        print (f'Este metodo es parte de plantilla1 y es mandatorio')
        
Objeto21 = Sub_Plantilla1()

Objeto21.Mostrar()
Objeto21.General()

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
        print (f'Tu pastel de {self.Favorito.Elegir()} te quedo delicioso')
        
Objeto22 = Pastel1()

Objeto22.Hornear()

print (f'-' * 20)

class Pastel2:
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Tu pastel de {self.Favorito.Elegir()} te quedo delicioso')
        
Sabor1 = Chocolate1()
Objeto23 = Pastel2(Sabor1)
Objeto23.Hornear()

Sabor2 = Vainilla1()
Objeto24 = Pastel2(Sabor2)
Objeto24.Hornear()

Sabor3 = Fresa1()
Objeto25 = Pastel2(Sabor3)
Objeto25.Hornear()

print (f'-' * 20)

class Persona2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
        
Objeto26 = Persona2('Erick Josue')

print (f'Hola, mi nombre es {Objeto26}')

print (f'-' * 20)

class Inventario2:
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto27 = Inventario2()

Objeto27.Productos.extend([1])
Objeto27.Productos.insert(1, 2)
Objeto27.Productos.append(3)

print (f'La cantidad de elementos en la lista son {len(Objeto27)}')

print (f'-' * 20)

class Igualdad2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
    
Objeto28 = Igualdad2('Erick')
Objeto29 = Igualdad2('Erick')

print (f'{Objeto28 == Objeto29}')

print (f'-' * 20)

import re

Texto5 = 'esto! es un texto hola 12 cualquiera pero 912 @ la idea es hala probar si esto 150 funciona o hula no'

Buscar6 = re.search(r'idea', Texto5)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\d+', Texto5)

print (f'{Buscar7}')

Buscar8 = re.fullmatch(r'esto\! es un texto hola 12 cualquiera pero 912 \@ la idea es hala probar si esto 150 funciona o hula no', Texto5)

print (f'{Buscar8}')

Buscar9 = re.findall(r'h.la', Texto5)

print (f'{Buscar9}')

Buscar10 = re.findall(r'^esto', Texto5)

print (f'{Buscar10}')

Buscar11 = re.findall(r'o$', Texto5)

print (f'{Buscar11}')

'''
{2}
{2,}
{2,4}
+ de 1 o mas
* de 0 o mas
? 0 o 1
'''

'''
\d+ solamente numeros
\D+ todo menos numeros
\s solamente espacios
\S todo menos espacios
\w todo menos simbolos especiales
\W solo characteres especiales
'''

Buscar12 = re.findall(r'\W', Texto5)

print (f'{Buscar12}')

Buscar13 = re.findall(r'\d{3}\s\W', Texto5)

print (f'{Buscar13}')

Buscar14 = re.findall(r'[la]{2,4}', Texto5)

print (f'{Buscar14}')

Buscar15 = re.findall(r'\d{2,4}', Texto5)

print (f'{Buscar15}')

print (f'-' * 20)

import re

Texto6 = 'ericksuper80@hotmail.com'

Pattern7 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-z]+\.[a-z]{2,}$'

Buscar16 = bool(re.fullmatch(Pattern7, Texto6))

if (Buscar16 == True):
    print (f'El coreo electronico tiene un formato correcto')
else:
    print (f'Error, el formato del correo es incorrecto')
    
print (f'-' * 20)

import re

Pattern8 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|org|net)$'

Buscar17 = bool(re.match(Pattern8, Texto6))

if (Buscar17 == True):
    print (f'El coreo 2 electronico tiene un formato correcto')
else:
    print (f'Error, el formato del correo 2 es incorrecto')
    
print (f'-' * 20)

import re

Texto7 = '31'

Pattern9 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar18 = bool(re.fullmatch(Pattern9, Texto7))

if (Buscar18 == True):
    print (f'El numero se encuentra entre 01 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

import re

Texto8 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern10 = r'\d{2}\/[0-9]{2}\/\d{3,}'

Replacement1 = 'XX/XX/XXXX'

Buscar20 = re.sub(Pattern10, Replacement1, Texto8)

print (f'{Buscar20}')

Pattern11 = r'\+\d?\-[0-9]{3}\-\d{3}\-[0-9]{3,4}'

Replacement2 = 'PhoneNumber'

Buscar21 = re.sub(Pattern11, Replacement2, Buscar20)

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

Pattern12 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|net|org)'

Buscar22 = re.findall(Pattern12, Texto9)

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

# VERSION1

Buscar23 = re.sub(r'\!|\?|\.{2,}', '', Texto10)

print (f'{Buscar23}')

Buscar24 = re.sub(r'\d{4}\-[0-9]{3,}', '', Buscar23)

print (f'{Buscar24}')

# VERSION2

print (f'-' * 20)

import re

Buscar25 = re.sub(r'[^a-zA-Z0-9\s]+', '', Texto10)

print (f'{Buscar25}')

Buscar26 = re.sub(r'[0-9]{5,}', '', Buscar25)

print (f'{Buscar26}')

# VERSION3

print (f'-' * 20)

import re

Pattern13 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos4 = re.findall(Pattern13, Texto10)

Texto10_temp1 = Texto10

for i, email in enumerate(Correos4, start=1):
    Texto10_temp1 = Texto10_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto10_temp1}')

Texto10_temp2 = re.sub(r'\!|\?|\.{2,}|\d{4}\-[0-9]{4,}', '', Texto10_temp1)

print (f'{Texto10_temp2}')

for i, email in enumerate(Correos4, start=1):
    Texto10_temp2 = Texto10_temp2.replace(f'SAMPLE{i}', email)

print (f'{Texto10_temp2}')

print (f'-' * 20)

var7 = '3.5'

try:
    Numerito4 = float(var7)
    if (Numerito4.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var8 = '3'

if (var8.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero entero')
    
if (isinstance(var8, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero entero')
    
try:
    Numerito5 = float(var8)
    if (Numerito5.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

import re

Texto11 = "   Hola!!!   mundo@@   123   "

Texto11_Version1 = Texto11.strip()
Texto11_Version2 = ' '.join(Texto11_Version1.split())
Texto11_Version3 = re.sub(r'\!|\@|\d*', '', Texto11_Version2)
Texto11_Version4 = Texto11_Version3.lower()

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
        print (f'Error, lo ingresado no es un numero')

Exception1('hola')

print (f'-' * 20)

def Exception2(Num1, Num2):
    try:
        Opera = Num1 + Num2
        print (f'El resultado de la operacion es {Opera}')
    except (ValueError, TypeError):
        print (f'Error, ambos elementos deben se numeros')

Exception2(12, 'hola')

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(12, 0)

print (f'-' * 20)

Lista_Exception4 = []
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
        print (f'Error, la llave esta fuera de rango')
        
Exception5('Nombre')

print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Papaya')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nUvas'])
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nManzana')
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
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Pokemon["Poke1"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Pokemon["Poke2"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Pokemon["Poke3"]}\n')
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

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'-' * 20)

print (f'{Data_Frame_Concatenate_Age}')

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()}')
print (f'La mayor de las edades es {Data_Frame_Concatenate_Age.max()}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Elemento1 = elemento['Nombre']
    Elemento2 = elemento['Edad']
    
    print (f'Hola, mi nombre es {Elemento1} y mi edad es {Elemento2} años')
    
print (f'-' * 20)

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()
Grupo3_Min_Cant = Grupo3.min()
Grupo3_Max_Cant = Grupo3.max()

print (f'El menor de las personas en el dataframe es {Grupo3_Min} y su edad es {Grupo3_Min_Cant} años')
print (f'El mayor de las personas en el dataframe es {Grupo3_Max} y su edad es {Grupo3_Max_Cant} años')

print (f'La cantidad de personas en el dataframe es {Grupo3.count()}')
print (f'Si sumo todas las edades me da {Grupo3.sum()}')
print (f'La media de las edades es {Grupo3.mean()}')
print (f'La media de las edades es {Grupo3.sum() / Grupo3.count()}')

Data_Frame_Concatenate_TOTALITO = Data_Frame_Concatenate['Edad'] * 500

print (f'{Data_Frame_Concatenate_TOTALITO}')

Grupo4 = Data_Frame_Concatenate_TOTALITO.sum()

print (f'-' * 20)

print (f'El total de la suma de los elementos es {Grupo4.sum()}')

print (f'-' * 20)

'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn

seaborn.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn

seaborn.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn

seaborn.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()'''

print (f'{Data_Frame_Concatenate.head(1)}')
print (f'-' * 20)

print (f'{Data_Frame_Concatenate.head(3)}')
print (f'-' * 20)

print (f'{Data_Frame_Concatenate.tail(1)}')
print (f'-' * 20)

Fila, Columna = Data_Frame_Concatenate.shape

print (f'El numerro de Fila es {Fila}')
print (f'El numerro de Columna es {Columna}')

Elemento3 = Data_Frame1.loc[0, 'Nombre']
Elemento4 = Data_Frame1.loc[1, 'Edad']
Elemento5 = Data_Frame1.loc[2, 'Votante']
Elemento6 = Data_Frame1.loc[1, :]
Elemento7 = Data_Frame1.loc[:, 'Nombre']

print (f'{Elemento3}')
print (f'{Elemento4}')
print (f'{Elemento5}')
print (f'{Elemento6}')
print (f'{Elemento7}')

print (f'-' * 20)

Elemento8 = Data_Frame2.iloc[0, 0]
Elemento9 = Data_Frame2.iloc[1, 1]
Elemento10 = Data_Frame2.iloc[2, 2]
Elemento11 = Data_Frame2.iloc[0, :]
Elemento12 = Data_Frame2.iloc[:, 2]

print (f'{Elemento8}')
print (f'{Elemento9}')
print (f'{Elemento10}')
print (f'{Elemento11}')
print (f'{Elemento12}')

print (f'-' * 20)

import pandas as pd
import openpyxl

Ruta_Excel1 = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel1, engine='openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'-' * 20)

Cargar_Excel1 = pd.read_excel(Ruta_Excel1, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel1, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel1, engine='openpyxl', sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel1, engine='openpyxl', sheet_name=0, header=0, index_col='embarcado')
Cargar_Excel5 = pd.read_excel(Ruta_Excel1, engine='openpyxl', sheet_name=0, header=0, usecols='E:I')
Cargar_Excel6 = pd.read_excel(Ruta_Excel1, engine='openpyxl', sheet_name=0, header=0, usecols='E:I', index_col='tarifa')

print (f'{Cargar_Excel.head()}')

print (f'-' * 20)

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

'''import requests

Resultado = requests.get(
    'http://localhost:8000/saludo'
)

Datos = Resultado.json()

print(f'Aqui estamos consumiendo un API - {Datos["Texto"]}')

import requests

Resultado = requests.get(
    'http://localhost:8000/uno/dos/tres/'
)

Datos = Resultado.json()

print (f'El numero es {Objeto9.Cantidad * Datos["Numerito"]}')
'''
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

'''Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Leer_Html)

print (f'{Cargar_Html[2].head()}')'''

print (f'-' * 20)

'''import requests

Resultado = requests.get('http://localhost:8000/saludo')

Datos = Resultado.json()

print (f'{Datos["Texto"]}')'''

Array0 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print (f'{Array0[0][2]}')
print (f'{Array0[0][::2]}')
print (f'{Array0[1][::3]}')
print (f'{Array0[1][:2]}')
print (f'{Array0[1][2:]}')
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
print (f'{Array1[Array1 >= 2]}')

print (f'-' * 20)

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 1]}')

print (f'{Array2[1, ::2]}')
print (f'{Array2[0, ::3]}')
print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[0, 2:3]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 >= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Elementos acomodados: {Array2_Sorted}')
print (f'Media de los numeros: {round(Array2_Sorted_Mean, 2)}')
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

Array3 = np.array([[['e', 'r', 'x'], ['d', 'a', 'l']],               [['m', 'u', 'o'], ['s', 'k', 'n']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[0, 1, 2]}')

print (f'{Array3[0, 0, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[1, :, 0]}')
print (f'{Array3[1, 1, 2:3]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "x"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],        [[[6, 5, 4], [9, 8, 7]], [[2, 5, 8], [6, 7, 2]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[0, 1, 1, 2]}')

print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[0, 1, 1, ::3]}')
print (f'{Array4[1, 0, 0, :2]}')
print (f'{Array4[1, 0, 0, 2:]}')
print (f'{Array4[0, 0, 0, 2:3]}')
print (f'{Array4[0, 1, :, 2]}')
print (f'{Array4[1, 1, 0, 0:None]}')
print (f'{Array4[1, 1, 0, :]}')
print (f'{Array4[Array4 >= 2]}')

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

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1) #type: ignore

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

print (f'Los menores de las columnas son {Array_Num2_Reshape_Column_Min}')
print (f'Los mayores de las columnas son {Array_Num2_Reshape_Column_Max}')
print (f'Los menores de las filas son {Array_Num2_Reshape_Row_Min}')
print (f'Los mayores de las filas son {Array_Num2_Reshape_Row_Max}')

print (f'-' * 20)

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 0]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}') # 2
print (f'{Array_Ones.shape}') # 2x3
print (f'{Array_Ones.size}') # 6
print (f'{Array_Ones.dtype}') # float64
print (f'{Array_Ones[0, 1]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Pokemon["Poke2"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[0, 2]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value = f'FUECOCO')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[4]}')

Lista_Array1 = list([])

for elemento in Array_Gen2:
    Lista_Array1.extend([str(elemento)])

print (f'{Array_Gen2}')
print (f'{type(Array_Gen2)}')
print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[1, 1, 0, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 2]}')

print (f'-' * 20)

Tupla_Array1 = tuple(('Rojo', 'Verde'))
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array1)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array["Nombre"][2])

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
print (f'{Array_Random1.ndim}')
print (f'{Array_Random1.size}')
print (f'{Array_Random1.shape}')
print (f'{Array_Random1.dtype}')
print (f'{Array_Random1[6]}')

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

print (f'Acomodados {Array_Random2_Sorted}')
print (f'Media {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria {Array_Random2_Sorted_Sum}')

print (f'-' * 20)

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Sum = Arr1 + Arr2
Rest = Arr1 - Arr2
Mult = Arr1 * Arr2
Div = Arr1 / Arr2

Array_Random1_Cien = Array_Random1 * 100

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

Lista_Array2 = ['Erick']
Lista_Array2.append('Josue')
Lista_Array2.insert(2, 'Karlita')
Lista_Array2.extend(['Roberta'])

Array_Num9 = np.array(Lista_Array2)

print (f'{Array_Num9}')
print (f'{type(Array_Num9)}')

print (f'-' * 20)

Array5 = np.array([1, 2, 3])
Array6 = np.arange(start=4, stop=7, step=1) #type: ignore

Array_Concatenated = np.concat([Array5, Array6])

print (f'{Array_Concatenated}')

print (f'-' * 20)

Array_Concatenated_Split = np.split(Array_Concatenated, 3)

print (f'{Array_Concatenated_Split[0]}')
print (f'{Array_Concatenated_Split[1]}')
print (f'{Array_Concatenated_Split[2]}')

print (f'-' * 20)

Array_Concatenated_Split2 = np.split(Array_Concatenated, 2)

print (f'{Array_Concatenated_Split2[0]}')
print (f'{Array_Concatenated_Split2[1]}')

print (f'-' * 20)

Array_Concatenated_Split3 = np.split(Array_Concatenated, 6)

print (f'{Array_Concatenated_Split3[0]}')
print (f'{Array_Concatenated_Split3[1]}')
print (f'{Array_Concatenated_Split3[2]}')
print (f'{Array_Concatenated_Split3[3]}')
print (f'{Array_Concatenated_Split3[4]}')
print (f'{Array_Concatenated_Split3[5]}')

print (f'-' * 20)

Array_Concatenated_Split4 = np.split(Array_Concatenated, 1)

print (f'{Array_Concatenated_Split4[0]}')

print (f'-' * 20)

Array_Concatenated_Where = np.where(Array_Concatenated == 3)

print (f'{Array_Concatenated_Where}')

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
print (f'{Array_Random3.ndim}')
print (f'{Array_Random3.shape}')
print (f'{Array_Random3.size}')
print (f'{Array_Random3.dtype}')
print (f'{Array_Random3[1, 0, 0]}')

Sumita9 = np.sum(Array_Random3, axis=0)
Sumita10 = np.sum(Array_Random3, axis=1)
Sumita11 = np.sum(Array_Random3[0, 0, 0:None])
Sumita12 = np.sum(Array_Random3[0, 0, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

print (f'-' * 20)

Lista_Sorteo = list(['Erick', 'Josue', 'Karlita', 'Carmelo', 'Susanita', 'Roxana'])

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

class Persona3():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
        
Objeto30 = Persona3('Erick Perez Gutierrez')

print (f'Hola, mi nombre es {Objeto30}')

print (f'-' * 20)

class Inventario3:
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto31 = Inventario3()

Objeto31.Productos.append('Lapiceros')
Objeto31.Productos.insert(1, 'Cuadernos')
Objeto31.Productos.extend(['Borradores'])

print (f'El total de elementos en la lista es de {len(Objeto31)}')

print (f'-' * 20)

class Igualdad3():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
        
Objeto32 = Igualdad3('Rojo')
Objeto33 = Igualdad3('Rojo')

print (f'{Objeto32 == Objeto33}')

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
            yield f'ESTO ES PAR'
        else:
            yield f'ESTO ES IMPAR'

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
            yield f'El numero es zero'
        elif (elemento == 1):
            yield f'El numero es one'
        elif (elemento == 2):
            yield f'El numero es two'
        elif (elemento == 3):
            yield f'El numero es three'
        elif (elemento == 4):
            yield f'El numero es four'
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

'''import requests

Resultado = requests.get('http://localhost:8000/saludo')

Datos = Resultado.json()

print (f'{Datos["Texto"]}')

print (f'-' * 20)

import requests

Resultado = requests.get('http://localhost:8000/{Numero}')

Datos = Resultado.json()

print (f'{Datos["Numerito"]}')'''

'''import requests

Resultado = requests.get('http://127.0.0.1:8000/')

Datos = Resultado.json()

print (f'{Datos["Texto"]}')'''

'''import requests

url = 'http://localhost:8000/elemento'

Diccionario = {
    'id': 1,
    'Nombre': "Erick",
    'Edad': 30
}

Respuesta = requests.post(url, json=Diccionario)

Datos2 = Respuesta.json()

print(Datos2)

Resultado = requests.get("http://localhost:8000/elemento")

Datos3 = Resultado.json()

print(f'Hola, tu nombre es {Datos3["Resultado"][0]["Nombre"]}')'''

class Persona4():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
        
Objeto34 = Persona4('Erick Josue')

print (f'Hola, mi nombre es {Objeto34}')

print (f'-' * 20)

class Inventario4():
    def __init__(self):
        self.Productos = list([])
        
    def __len__(self):
        return len(self.Productos)
        
Objeto35 = Inventario4()

Objeto35.Productos.extend(['Primera'])
Objeto35.Productos.insert(1, 'Segunda')
Objeto35.Productos.append('Tercera')

print (f'La cantidad de elementos de la lista es {len(Objeto35)}')

print (f'-' * 20)

class Igualdad4():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
        
Objeto36 = Igualdad4('Perro')
Objeto37 = Igualdad4('Perro')

print (f'{Objeto36 == Objeto37}')

print (f'-' * 20)

Lista_Contable = [1, 2, 3, 4, 5]

def Contable1(Lista):
    Acumulador = 0
    for elemento in Lista:
        Acumulador += elemento
        
    print (f'El resultado de sumar todos los numeros es {Acumulador}')

Contable1(Lista_Contable)

print (f'-' * 20)

def Evaluable(Lista):
    Sum_Par = 0
    for elemento in Lista:
        if (elemento % 2 == 0):
            Sum_Par += elemento
        else:
            continue

    print (f'El resultado de sumar todos los numeros pares nada mas es {Sum_Par}')

Evaluable(Lista_Contable)

print (f'-' * 20)

def Evaluable2(Lista):
    Sum_Par1 = 0
    Sum_Par2 = 0
    Any_Par = any(num % 2 == 0 for num in Lista)
    if (Any_Par == True):
        Anonima0 = filter(lambda Num : Num % 2 == 0, Lista)
        Lista_ImPares = [num for num in Lista if num % 2 != 0]
        Sum_Par1 = sum(list(Anonima0))
        Sum_Par2 = sum(Lista_ImPares)
        
        print (f'La suma de los elementos pares es {Sum_Par1}')
        print (f'La suma de los elementos impares es {Sum_Par2}')
    else:
        exit()

Evaluable2(Lista_Contable)

print (f'-' * 20)

def Evaluable3(Lista, Numerito):
    Switch = False
    for elemento in Lista:
        if (elemento == Numerito):
            Switch = True
        else:
            continue
        
    return Switch

if (Evaluable3(Lista_Contable, 2) == True):
    print (f'El numerito fue encontrado en la lista')
else:
    print (f'Error, el numerito no fue encontrado en la lista')
    
print (f'-' * 20)

def Evaluable4(Lista):
    Menor = min(Lista)
    Mayor = max(Lista)
    Resultado = [Menor, Mayor]
    
    print (f'Los numeros que buscabas son {Resultado}')

Evaluable4(Lista_Contable)

print (f'-' * 20)

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
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
    
print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(22)}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
print (f'-' * 20)
    
def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Erick", 3.6, 200, False)

print (f'{Funcion_Tupla("Erick", 3.6, 200, False)}')
print (f'{Funcion_Tupla("Erick", 3.6, 200, False)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Erick", 3.6, 200, False))}')

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

print (f'-' * 20)

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(250, 3)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

if (PEPE.Any_Par == True):
    print (f'Los numeros pares de la lista son {PEPE.Lista_Par}')
    print (f'Los numeros pares de la lista son {list(Anonima3)}')
else:
    print (f'Error, no hay numeros pares en la lista')

print (f'-' * 20)

def Primera(Segunda):
    def Tercera(*args):
        return Segunda(*args) - 42
        
    return Tercera

@Primera
def Evaluacion(Numero:int) -> int:
    Local = Numero
    return PEPE.GLOBAL + Local

print (f'El resultado de la operacion es {Evaluacion(12)}')

def Externa(Nombre):
    def Interna(Apellido):
        return f'Mi nombre es {Nombre} {Apellido}'
    
    return Interna('PEREZ GUTIERREZ')

print (f'{Externa('ERICK JOSUE')}')

print (f'-' * 20)

def Closure_Externo():
    Lista_Closure = []
    def Closure_Interno(x):
        Lista_Closure.append(x)
        
        return Lista_Closure
        
    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(28)}')
print (f'{Variable_Closure(34)}')

print (f'-' * 20)

def Crear_Closure_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y
    
    return Closure_Multiplicador

Mult1 = Crear_Closure_Multiplicador(2)
Mult2 = Crear_Closure_Multiplicador(3)

print (f'El multiplicador es {Mult1(10)}')
print (f'El multiplicador es {Mult2(10)}')

print (f'-' * 20)

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    if (Any_Impar == True):
        Anonima = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impar = [num for num in Lista if num % 2 != 0]
        
        print (f'Los numeros impares de la lista son {list(Anonima)} o incluso podrian ser {Lista_Impar}')
    else:
        print (f'Error, no hay elementos impares en la lista')

Filtrador(PEPE.Lista_Numeros)

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'ZZZZ')
        Segunda()
        print (f'ZZZZ')
        
    return Tercera

@Primera
def Saludar3():
    print (f'Hola Mundo')
    
Saludar3()

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 6
        
    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(4, 3)}')

print (f'-' * 20)

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonathan'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)
        
    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    print (f'Hola mi nombre es {Nombre} {Apellido}')
    
Usuario2("Erick", "Perez")

'''import requests

Resultado = requests.get('http://127.0.0.1:8000/elemento')

Datos = Resultado.json()

print (f'Mi edad es {Datos["Resultado"][0]["Edad"]}')'''

'''import requests

URL = 'http://127.0.0.1:8000/elemento'

Diccionario = {
    'id' : 15,
    'Nombre' : "Erick",
    'Edad' : 55
}

Agregado = requests.post(URL, json=Diccionario)

Datos = Agregado.json()

print (f'{Datos}')

print (f'-' * 20)

Resultado = requests.get(URL)

Datos1 = Resultado.json()

print (f'Mi id de usuario es {Datos1["Resultado"][0]["id"]}')'''

print (f'-' * 20)

from Module_Own import Pokemon2 as Poke2

Objeto38 = Poke2(PEPE.Diccionario_Pokemon["Poke1"], 'Electrico', 'Impact Trueno')
Objeto39 = Poke2(PEPE.Diccionario_Pokemon["Poke2"], 'Roca', 'Sismo')

Objeto38.Mostrar()

print (f'-' * 20)

Objeto39.Mostrar()

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto40 = Poke_Kid2(PEPE.Diccionario_Pokemon["Poke3"], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto40)
Objeto40.Mostrar()

print (f'-' * 20)

class Camara1():
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada')
        
class Reproductor_Musica1():
    def Reproducir_Musica(self):
        print (f'La musica ha sido reproducida')
        
class Smartphone1(Camara1, Reproductor_Musica1):
    def Encender_Smartphone(self):
        print (f'El smartphone ha sido encendido')
        
Objeto41 = Smartphone1()

Objeto41.Encender_Smartphone()
Objeto41.Reproducir_Musica()
Objeto41.Tomar_Fotografia()

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
        
Objeto42 = Perro2('Chester', 5, 2.8, 'Poodle', 'Asma')

Veterinaria2.Mostrar(Objeto42)
Objeto42.Mostrar()

print (f'-' * 20)

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto43 = Gato2('Messi', 1.5, 2, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto43)
Objeto43.Mostrar()

print (f'-' * 20)

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto44 = Pajaro2('Polly', 31, 0.4, 'Cacatua Amarilla', 'Si')

Veterinaria2.Mostrar(Objeto44)
Objeto44.Mostrar()

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
        
Objeto45 = Paladin2(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto45.Mostrar()
Atacante2.Mostrar(Objeto45)
Defensor2.Mostrar(Objeto45)

print (f'-' * 20)

Padre_Hija = issubclass(Poke_Kid2, Poke2)

print (f'{Padre_Hija}')

print (f'-' * 20)

Instancia1 = isinstance(Objeto45, Paladin2)
Instancia2 = isinstance(Objeto45, Defensor2)
Instancia3 = isinstance(Objeto45, Atacante2)
Instancia4 = isinstance(Objeto45, Atacante1)

print (f'{Instancia1}')
print (f'{Instancia2}')
print (f'{Instancia3}')
print (f'{Instancia4}')

print (f'-' * 20)

'''import requests

URL = 'http://127.0.0.1:8000/elemento'

Diccionario = {
    'id' : 150,
    'Nombre' : 'Tiranosaurio',
    'Era' : 'Era Jurasica'
}

Agregado = requests.post(URL, json=Diccionario)

Agregado2 = Agregado.json()

print (f'{Agregado2}')

print (f'-' * 20)

Resultado = requests.get(URL)

Datos = Resultado.json()

print (f'El dinosaurio {Datos["Resultado"][5]["Nombre"]} viene de la {Datos["Resultado"][5]["Era"]}')'''

'''import requests

URL = 'http://127.0.0.1:8001/elemento'

Diccionario = {
    'Dino_ID' : 1000,
    'Nombre' : 'Estegosaurio'
}

Agregar1 = requests.post(URL, json=(Diccionario))

Agregar2 = Agregar1.json()

print (f'{Agregar2}')

Resultado = requests.get(URL)

Datos = Resultado.json()

print (f'El nombre del bicho es {Datos["Resultado"][1]["Nombre"]}')'''

class Persona5():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto46 = Persona5('Roxana Madriz')

print (f'El nombre de la chica es {Objeto46}')

print (f'-' * 20)

class Inventario5:
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto47 = Inventario5()

Objeto47.Productos.insert(0, 'Uno')
Objeto47.Productos.append('Dos')
Objeto47.Productos.extend(['Tres'])

print (f'El numero de elementos en la lista es {len(Objeto47)}')

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
  
Objeto48 = D2()

A2.Mostrar(Objeto48)
B2.Mostrar(Objeto48)
C2.Mostrar(Objeto48)
Objeto48.Mostrar()
E2.Mostrar(Objeto48)

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
        
Objeto49 = Efectivo2()
Objeto50 = Tarjeta2()
Objeto51 = Cripto2()

Objeto49.Pagar()
Objeto50.Pagar()
Objeto51.Pagar()

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
        print (f'Tu saldo a la fecha es ${self.__Saldo}')
        
Objeto52 = Cuenta_Bancaria2(100)
Objeto52.Depositar(25)
Objeto52.Mostrar()

print (f'Tu saldo privado es {Objeto52.Dinero}')

Objeto52.Dinero = '50,000,000'

Objeto52.Mostrar()

print (f'Tu saldo privado es {Objeto52.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla2(Plantilla2):
    def Mostrar(self):
        print (f'Este es el metodo de esta clase')
        
    def General(self):
        print (f'Este metodo es obligatorio y viene de la plantilla')
        
Objeto53 = Sub_Plantilla2()

Objeto53.Mostrar()
Objeto53.General()

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
        print (f'El retador ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Objeto54 = Battle3()

Objeto54.Batallar()

print (f'-' * 20)

class Battle4:
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El retador ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Criatura4 = Bulbasaur2()
Objeto55 = Battle4(Criatura4)
Objeto55.Batallar()

Criatura5 = Treekoo2()
Objeto56 = Battle4(Criatura5)
Objeto56.Batallar()

Criatura6 = Chikorita2()
Objeto57 = Battle4(Criatura6)
Objeto57.Batallar()

print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un
Long
String'''

variable4 = Objeto10.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = Objeto11.Catched, not False

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Pokemon["Poke1"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene actualmente {Objeto9.Cantidad} pokemones en su pokedex')

del variable5

print (f'-' * 20)

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'-' * 20)

print (f'Erick' in PEPE.Lista1)
print (f'Sam' in PEPE.Tupla_Poke)
print (f'{PEPE.Diccionario_Pokemon["Poke2"]}' in PEPE.Set_Conjunto_Poke)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables y al mismo tiempo un snake case {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

print (f'-' * 20)

print (f'El resultado de la operacion es {PEPE.Lista3[2] * Objeto10.Cantidad}')

print (f'{PEPE.Lista2[::2]}')
print (f'{PEPE.Lista2[::3]}')
print (f'{PEPE.Lista2[:2]}')
print (f'{PEPE.Lista2[2:]}')
print (f'{PEPE.Lista2[2:3]}')
print (f'{PEPE.Lista2[0:None]}')
print (f'{PEPE.Lista2[:]}')

print (f'-' * 20)

print (f'{Lista_Uno[0]} eso que esta ahi es un {PEPE.Lista2[2]}?')

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

print (f'-' * 20)

Tupla1 = ('Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde')

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Green'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Variable_Funcion_Tupla)}')

print (f'-' * 20)

print (f'{Tupla1[1]}')
print (f'{Tupla1[::2]}')
print (f'{Tupla1[::3]}')
print (f'{Tupla1[:2]}')
print (f'{Tupla1[2:]}')
print (f'{Tupla1[0:1]}')
print (f'{Tupla1[0:None]}')
print (f'{Tupla1[:]}')

print (f'-' * 20)

Set_Conjunto1 = {'Electrico', Objeto9.Tipo, Objeto9.Tipo, Objeto9.Tipo, Objeto9.Tipo}
Set_Conjunto1.add('Agua')
Set_Conjunto2 = set({'Roca'})
Set_Conjunto1.update(Set_Conjunto2)

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Electric', 'Water', 'Rock'})

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

Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, 'ChocoFresa'})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Objeto10.Cantidad,
    'Votante' : Variable_Funcion_Tupla[3]
}

Diccionario2 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
}

Diccionario3 = dict({'Ingresos' : 500, 'Gastos' : 200, 'Vacio' : "a"})

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
print (f'{Diccionario2["Nombre"][1]}')
print (f'{Diccionario2.get("Edad")[2]}') #type: ignore

print (f'-' * 20)

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3.values()}')
print (f'{Diccionario3.items()}')
print (f'{Diccionario3["Ingresos"]}')
print (f'{Diccionario3.get("Gastos")}')

print (f'-' * 20)

Diccionario1['Nombre'] = variable1

print (f'{Diccionario1}')

del Diccionario1['Nombre']

Diccionario1.pop('Edad')

print (f'{Diccionario1}')

Diccionario1_Copy = Diccionario1.copy()

Diccionario1.clear()

print (f'{Diccionario1}')
print (f'{Diccionario1_Copy}')

print (f'-' * 20)

Diccionario1 = dict({1 : 'Karlita', 2 : 6, 3 : False})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario2["Nombre"][0]} no puede votar ya que solo tiene {Diccionario1.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'Oro')
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
print (f'{Diccionario_Vacio2["Uno"]}')
print (f'{Diccionario_Vacio2.get("Dos")}')

print (f'-' * 20)

Key2 = [f'Key_{i}' for i in range(len(Lista_Uno_Copia))]

print (f'{Key2}')

Diccionario4 = dict(zip(Key2, Lista_Uno_Copia))

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Key_1"]}')
print (f'{Diccionario4.get("Key_2")}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

print (f'-' * 20)

Set_Conjunto_Csv3 = set(Cargar_Csv3['product'])

print (f'{Set_Conjunto_Csv3}')

Key3 = [f'Key{i}' for i in range(len(Set_Conjunto_Csv3))]

print (f'{Key3}')

Diccionario5 = dict(zip(Key3, Set_Conjunto_Csv3))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key0"]}')
print (f'{Diccionario5.get("Key1")}')

print (f'-' * 20)

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
    
Encontrada2 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech3_Formateada.date()]

if (Encontrada2.empty):
    print (f'Error, no hay ventas en esta fecha')
else:
    print (f'Genial, se encontraron ventas en esta fecha')
    
    Grupo5 = Encontrada2.groupby('product')['quantity'].sum()
    Grupo5_Min = Grupo5.idxmin()
    Grupo5_Max = Grupo5.idxmax()
    Grupo5_Min_Cant = Grupo5.min()
    Grupo5_Max_Cant = Grupo5.max()
    
    print (f'En la fecha {Fech3_Formateada}, el producto {Grupo5_Min} vendio un total de {Grupo5_Min_Cant} unidades')
    print (f'En la fecha {Fech3_Formateada}, el producto {Grupo5_Max} vendio un total de {Grupo5_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron fue de {Grupo5.count()}')
    print (f'La cantidad total de productos vendidos en esta fecha fue de {Grupo5.sum()}')
    
    Grupo6 = Encontrada2.groupby('product')['TOTALITO'].sum()
    
    print (f'El total vendido en dolares es de ${Grupo6.sum()}')
    
    Promedio2 = Grupo6.sum() / Grupo5.count()
    
    print (f'El promedio de dolares vendido en esta fecha fue de ${round(Promedio2, 2)}')
    print (f'El promedio de dolares vendido en esta fecha fue de ${Grupo6.mean()}')
    
print (f'-' * 20)

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la operacion es {round(int(Division_Baja))}')
print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'-' * 20)

print (f'{type(variable1)}')
print (f'{type(variable4)}')
print (f'{type(PEPE.Division_Flotante)}')
print (f'{type(variable6)}')
print (f'{type(Lista_Uno_Copia)}')
print (f'{type(Tupla3)}')
print (f'{type(Set_Conjunto_Menu1)}')
print (f'{type(Set_Conjunto_Menu2)}')
print (f'{type(Diccionario1_Copy)}')
print (f'{type(Objeto12)}')
print (f'{type(Funcion_Tupla)}')

print (f'{type(Data_Frame_Concatenate)}')
print (f'{type(PEPE)}')
print (f'{type(Array2_Sorted)}')

print (f'-' * 20)

if (Diccionario3['Ingresos'] > 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Los ingresos son altos, Gastos bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Los ingresos son altos, Gastos al limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Los ingresos son altos, Gastos altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] == 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Los ingresos son los minimos, Gastos bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Los ingresos son los minimos, Gastos al limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Los ingresos son los minimos, Gastos altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] < 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Los ingresos son bajos, Gastos bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Los ingresos son bajos, Gastos al limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Los ingresos son bajos, Gastos altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')
    
variable8 = 'Josue'
variable9 = 5

if (variable8 == variable1 and variable9 > Variable_Sumatoria):
    print (f'Correcto, ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')
    
if (variable8 == variable1 or variable9 > Variable_Sumatoria):
    print (f'Correcto, al menos una de las condiciones se cumple')
else:
    print (f'Error, ninguna de las dos condiciones se cumple')
    
print (f'-' * 20)

class Persona6():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
        
Objeto58 = Persona6('Karlita Vega')

print (f'Hola {Objeto58}, como estas?')

print (f'-' * 20)

class Inventario6:
    def __init__(self):
        self.Productos = list([])
        
    def __len__(self):
        return len(self.Productos)
        
Objeto59 = Inventario6()

Objeto59.Productos.append('Erick')
Objeto59.Productos.insert(1, 'Josue')
Objeto59.Productos.extend(['Karlita', 'Roxana', 'Susanita'])

print (f'La cantidad de elementos de la lista son {len(Objeto59)}')

print (f'-' * 20)

class Igualdad5():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
        
Objeto60 = Igualdad5('Perro')
Objeto61 = Igualdad5('Perro')

print (f'{Objeto60 == Objeto61}')

print (f'-' * 20)

'''import requests

URL = 'http://localhost:8000/elemento'

Diccionario = {
    'Worker_id' : 58426,
    'Name' : 'Julian Knight',
    'Role' : "DevOps"
}

Agregar1 = requests.post(URL, json=(Diccionario))
Agregar2 = Agregar1.json()

print (f'{Agregar2}')

print (f'-' * 20)

Resultado = requests.get(URL)

Datos = Resultado.json()

print (f'En la base de datos hay un trabajador con identificacion {Datos["Resultado"][0]["Worker_id"]}, cuyo nombre es {Datos["Resultado"][0]["Name"]} y su posicion es {Datos["Resultado"][0]["Role"]}')'''

print (f'{dir(variable1)}')

print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Variable_Sumatoria
        self.Classified = True

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')
        
Objeto62 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Ash")], 'Kanto', Objeto9.Nombre)
Objeto63 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Brooke")], 'Alolah', Objeto10.Nombre)
Objeto64 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")], 'Paldea', Objeto11.Nombre)

Objeto62.Desplegar()
print (f'Mi pokedex tiene {Objeto62.Pokedex} criaturas')

if (Objeto62.Classified == True):
    print (f'Felicidades, has clasificado a la liga')
else:
    print (f'Mas suerte la proxima vez')
    
print (f'-' * 20)

Objeto63.Desplegar()
print (f'Mi pokedex tiene {Objeto63.Pokedex} criaturas')

if (Objeto63.Classified == True):
    print (f'Felicidades, has clasificado a la liga')
else:
    print (f'Mas suerte la proxima vez')
    
print (f'-' * 20)

Objeto64.Desplegar()
print (f'Mi pokedex tiene {Objeto64.Pokedex} criaturas')

if (Objeto64.Classified == True):
    print (f'Felicidades, has clasificado a la liga')
else:
    print (f'Mas suerte la proxima vez')
    
print (f'-' * 20)

Negativo = -5

print (f'El numero ahora es positivo {int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)

if (Any_Iterable == True):
    print (f'Hay numeros pares en la lista')
else:
    print (f'No hay numeros pares en la lista')
    
Anonima4 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)

Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{list(Anonima4)}')
print (f'{Lista_Iterable}')

print (f'-' * 20)

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, ingrese una cadena de texto')
    
Cociente, Residuo = divmod(Objeto9.Cantidad, Sumatoria2(1, 2, 1, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

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
print (f'La letra n esta en la posicion {variable10.lower().index("n")}')

print (f'La letra {variable10_letra} aparece un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = 'este es un texto cualquiera que yo podria usar para practicar o no'
variable11_lista = variable11.split(' ')

for indice, elemento in enumerate(variable11_lista, start=1):
    print (f'{indice} -- {elemento}')
    
print (f'-' * 20)

print (f'La cantidad de palabras en la cadena de texto es {len(variable11_lista)}')

var9 = 'hola'

if (isinstance(var9, (str))):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Error, lo que ingresaste no es texto')
    
if (var9.isalpha()):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Error, lo que ingresaste no es texto')
    
try:
    Numerito6 = float(var9)
    if (Numerito6.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Lo que ingresaste es texto')
    
print (f'-' * 20)

var10 = '3.5'

if (isinstance(var10, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Error, lo ingresado no es un numero decimal')
    
try:
    Numerito7 = float(var10)
    if (Numerito7.is_integer()):
        print (f'El numero ingresado es entero')
    else:
        print (f'El numero ingresado es decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var11 = '20'

if (var11.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
if (isinstance(var11, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
try:
    Numerito8 = float(var11)
    if (Numerito8.is_integer()):
        print (f'El numero ingresado es entero')
    else:
        print (f'El numero ingresado es decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var12 = 2.3

if (isinstance(var12, (float, int))):
    print (f'Lo ingresado es un numero entero o decimal')
else:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var13 = 'erick123'

if (var13.isalnum()):
    print (f'Se permiten letras y numeros')
else:
    print (f'Error de formato invalido')
    
print (f'-' * 20)

var14 = '  e       '

if (var14.isspace()):
    print (f'Este elemento esta compuesto por solo espacios')
else:
    print (f'Error, esto tiene mas que solo espacios')
    
print (f'-' * 20)

var15 = 'eSteBAN'

if (var15.lower().islower() == True):
    print (f'Correcto, el texto esta en minuscula')
else:
    print (f'Error, el texto no esta todo en minuscula')
    
if (var15.upper().isupper() == True):
    print (f'Correcto, el texto esta en mayuscula')
else:
    print (f'Error, el texto no esta todo en mayuscula')
    
print (f'-' * 20)

print (f'Misty, se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")} de la tupla')

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

print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1
    
print (f'-' * 20)

Lista_Animales = []
Lista_Animales.append('Cocodrilo')
Lista_Animales.insert(1, PEPE.Lista2[2])
Lista_Animales.extend(['Tigre', 'Oso'])

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Tigre'):
        print (f'The name of this animal in english is Tiger')
        break
    else:
        Contador+= 1
        continue
    
print (f'-' * 20)

for elemento1, elemento2, elemento3 in zip(Lista_Uno_Copia, Set_Conjunto_Menu1, Lista_Animales):
    print (f'{elemento1} -- {elemento2} -- {elemento3}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
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

print (f'El numero menor de la lista es {Menor}')
print (f'El numero mayor de la lista es {Mayor}')

Redondeado = round(14.458795, 2)

print (f'El redondeado es {Redondeado}')

print (f'{bool(False)}')
print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool("")}')
print (f'{bool(not True)}')

Todo_All = all([Lista_Numeros_Mult, PEPE.Tupla_Poke, PEPE.Set_Conjunto_Poke, ""])

print (f'{Todo_All}')

print (f'-' * 20)

Sumatoria4 = sum(Lista_Numeros_Mult)

print (f'El resultado de la sumatoria es {Sumatoria4}')

Uno = int('500')
Dos = str(500)
Tres = float(Uno)
Cuatro = list(PEPE.Set_Conjunto_Poke)
Cinco = tuple(Lista_Numeros_Mult)
Seis = set(Lista_Animales)

print (f'{type('500')} -- {type(Uno)}')
print (f'{type(500)} -- {type(Dos)}')
print (f'{type(Uno)} -- {type(Tres)}')

print (f'{type(PEPE.Set_Conjunto_Poke)} -- {type(Cuatro)}')
print (f'{type(Lista_Numeros_Mult)} -- {type(Cinco)}')
print (f'{type(Lista_Animales)} -- {type(Seis)}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto_Poke))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

variable_PEPE3 = PEPE3

print (f'-' * 20)

import requests
import pandas as pd
import io

Ruta_Html2 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html2, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Leer_Html)

print (f'{Cargar_Html2[2].head()}')

print (f'-' * 20)

import re

Texto12 = 'ericksuper80@hotmail.com'

Pattern14 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)$'

Buscar27 = bool(re.fullmatch(Pattern14, Texto12))

if (Buscar27 == True):
    print (f'El correo tiene un formato correcto')
else:
    print (f'Error, el formato del correo es invalido')
    
print (f'-' * 20)

import re

Texto13 = '31'

Pattern15 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar28 = bool(re.match(Pattern15, Texto13))

if (Buscar28 == True):
    print (f'El numero esta entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')

print (f'-' * 20)

'''def Floating1(Numero):
    try:
        Numerito9 = float(Numero)
        if (Numerito9.is_integer()):
            print (f'Lo ingresado es un numero entero')
        else:
            print (f'Lo ingresado es un numero decimal')
    except ValueError:
        print (f'Error, lo ingresado no es un numero')

Floating1(PEPE.Flotante1)

Resultado = Objeto10.Cantidad * Variable_Sumatoria + PEPE.Flotante2

print (f'El resultado de la operacion es {Resultado}')'''

'''Resultado = eval(PEPE.Flotante3)

print (f'El resultado de la operacion es {Resultado}')'''

'''def Floating4(Textico):
    Texto = Textico.replace(' ', '')
    if (isinstance(Texto, (str))):
        print (f'Lo ingresado es texto')
    else:
        print (f'Lo ingresado no es un texto')
        
    if (Texto.isalpha()):
        print (f'Lo ingresado es texto')
    else:
        print (f'Lo ingresado no es un texto')
        
    try:
        Numerito9 = float(Textico)
        if (Numerito9.is_integer()):
            print (f'Lo ingresado es un numero entero')
        else:
            print (f'Lo ingresado es un numero decimal')
    except ValueError:
        print (f'Lo ingresado es un texto')

Floating4(PEPE.Flotante4)'''

'''def Floating5(Cadena):
    Lista_Cadena = Cadena.split(' ')
    
    for elemento in Lista_Cadena:
        print (f'{elemento}')
        
    print (f'La cantidad de palabras digitadas es {len(Lista_Cadena)}')

Floating5(PEPE.Flotante5)'''

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de estudiantes de la lista: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento}: ')
        Lista.append(Alumno)
        
    return Lista

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.writelines([f'\nLa lista de estudiantes es {Colegio(Lista_Alumnos)}'])
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()'''
    
'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del estudiante {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del estudiante {elemento}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda Num : Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes es {Menore} -- {Lista[0][1]} años')
    print (f'El mayor de los estudiantes es {Mayore} -- {Lista[-1][1]} años')

Colegio(Lista_Alumnos)'''

'''def Exception_Finale():
    while True:
        Numero = input(f'Ingrese un numero: ')
        try:
            Numerito9 = float(Numero)
            if (Numerito9.is_integer()):
                print (f'Lo ingresado es un numero entero')
                break
            else:
                print (f'Lo ingresado es un numero decimal')
                break
        except ValueError:
            print (f'Error, ingrese un numero')

Exception_Finale()'''

import pandas as pd
from datetime import datetime

Ruta_Csv4 = 'C:\\Repo\\Store.csv'

Cargar_Csv4 = pd.read_csv(Ruta_Csv4)

print (f'{Cargar_Csv4}')

print (f'-' * 20)

Set_Csv4 = set(Cargar_Csv4['product'])

print (f'{Set_Csv4}')

Key4 = [f'Key_{i}' for i in range(len(Set_Csv4))]

Diccionario6 = dict(zip(Key4, Set_Csv4))

print (f'{Diccionario6.keys()}')
print (f'{Diccionario6.values()}')
print (f'{Diccionario6.items()}')
print (f'{Diccionario6["Key_1"]}')
print (f'{Diccionario6.get("Key_2")}')

print (f'-' * 20)

for elemento in Diccionario6:
    print (f'{Diccionario6[elemento]}')
    
print (f'-' * 20)

for elemento in Diccionario6.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario6.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario6.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

print (f'{Cargar_Csv4}')

print (f'-' * 20)

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
    print (f'Genial! Encontramos ventas')
    
    Grupo7 = Encontrada4.groupby('product')['quantity'].sum()
    Grupo7_Min = Grupo7.idxmin()
    Grupo7_Max = Grupo7.idxmax()
    Grupo7_Min_Cant = Grupo7.min()
    Grupo7_Max_Cant = Grupo7.max()
    
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo7_Min} vendio un total de {Grupo7_Min_Cant} unidades')
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo7_Max} vendio un total de {Grupo7_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron en esta fecha fue {Grupo7.count()}')
    print (f'La cantidad de productos comprados en esta fecha fue {Grupo7.sum()}')
    
    Grupo8 = Encontrada4.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue ${Grupo8.sum()}')
    
    Promedio4 = Grupo8.sum() / Grupo7.count()
    
    print (f'El promedio de venta es de ${Promedio4}')
    print (f'El promedio de venta es de ${Grupo8.mean()}')
    
class Persona7():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Objeto65 = Persona7('Carmen')

Lista_Persona7 = [
    Persona7('Julian'),
    Persona7('Roberta'),
    Persona7('Ana')
]

print (f'{Lista_Persona7}')