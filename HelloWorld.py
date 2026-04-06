import Module_Own as PEPE
from Module_Own import Pokemon as Poke

class Poke_Kid(Poke):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto1 = Poke_Kid(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno', 'Acero')
Objeto2 = Poke_Kid(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Fantasma')
Objeto3 = Poke_Kid(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Hada')

Poke.Mostrar(Objeto1)
Objeto1.Mostrar()

print (f'-' * 20)

class Mascota():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad} años')
        print (f'Peso: {self.Peso}kgs')

class Perro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')

Objeto4 = Perro('Chester', 5, 2.6, 'Poodle', 'Asma')

Mascota.Mostrar(Objeto4)
Objeto4.Mostrar()

print (f'-' * 20)

class Gato(Mascota):
    def __init__(self, Nombre, Edad, Peso, Raza, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')

Objeto5 = Gato('Messi', 1.5, 1.8, 'Angora', 'Si')

Mascota.Mostrar(Objeto5)
Objeto5.Mostrar()

print (f'-' * 20)

class Pajaro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto6 = Pajaro('Polly', 31, 0.7, 'Cacatua Amarilla', 'Si')

Mascota.Mostrar(Objeto6)
Objeto6.Mostrar()

print (f'-' * 20)

class Atacante():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon

    def Mostrar(self):
        print (f'Damage: {self.Damage}pts')
        print (f'Weapon: {self.Weapon}')

class Defensor:
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life

    def Mostrar(self):
        print (f'Healing: {self.Healing}pts')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}pts')

class Paladin(Atacante, Defensor):
    def __init__(self, Damage, Weapon, Healing, Potion, Life, Name):
        Atacante.__init__(self, Damage, Weapon)
        Defensor.__init__(self, Healing, Potion, Life)
        self.Name = Name

    def Mostrar(self):
        print (f'Name: {self.Name}')

Objeto7 = Paladin(75, 'Battle Axe', 25, 'Green Liquid', 200, 'Ghost Knight')

Objeto7.Mostrar()
Atacante.Mostrar(Objeto7)
Defensor.Mostrar(Objeto7)

print (f'-' * 20)

class Efectivo():
    def Pagar(self):
        print (f'El pago se realizo en efectivo')

class Tarjeta:
    def Pagar(self):
        print (f'El pago se realizo en tarjeta')

class Cripto:
    def Pagar(self):
        print (f'El pago se realizo en cripto')

Objeto8 = Cripto()
Objeto9 = Tarjeta()
Objeto10 = Efectivo()

Objeto8.Pagar()
Objeto9.Pagar()
Objeto10.Pagar()

print (f'-' * 20)

class Banking_Account():
    def __init__(self, Saldo):
        self.__Saldo = Saldo

    def Depositar(self, Dinero):
        self.__Saldo += Dinero

    @property
    def Dinero(self):
        return self.__Saldo

    @Dinero.setter
    def Dinero(self, New_Saldo):
        self.__Saldo = New_Saldo

    def Mostrar(self):
        print (f'Tu saldo a la fecha es de ${self.__Saldo}')

Objeto11 = Banking_Account(100)
Objeto11.Depositar(25)
Objeto11.Mostrar()

print (f'El valor de la variable privada es {Objeto11.Dinero}')

Objeto11.Dinero = '35,0000'

Objeto11.Mostrar()

print (f'El valor de la variable privada es {Objeto11.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def Borrador(self):
        pass

class Ejemplo(Plantilla):
    def Mostrar(self):
        print (f'Hola Cualquiera')

    def Borrador(self):
        print (f'Esto es un ejemplo de abstraccion')

Objeto12 = Ejemplo()

Objeto12.Mostrar()
Objeto12.Borrador()

print (f'-' * 20)

class Uno():
    def Mostrando(self):
        print (f'Esto es un ejemplo de composicion')

class Dos():
    def __init__(self):
        self.Placeholder = Uno()

    def Mostrando_Finale(self):
        self.Placeholder.Mostrando()

Objeto13 = Dos()

Objeto13.Mostrando_Finale()

print (f'-' * 20)

import re

Texto1 = 'esto es 100 un! hola ejemplo cualquiera@ para baiaiai hela probar. el concepto 8 de haala expresiones 45 regulares'

Buscar1 = re.search('\d+', Texto1)

print (f'{Buscar1}')

Buscar2 = re.findall(r'\d+', Texto1)

print (f'{Buscar2}')

Buscar3 = re.findall(r'\D+', Texto1)

print (f'{Buscar3}')

Buscar4 = re.findall(r'\w+', Texto1)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\W+', Texto1)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\s', Texto1)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\S', Texto1)

print (f'{Buscar7}')

Buscar8 = re.findall(r'h.la', Texto1)

print (f'{Buscar8}')

Buscar9 = re.findall(r'[a,e,i]{2,}', Texto1)

print (f'{Buscar9}')

Buscar10 = re.findall(r'(ai){3,4}', Texto1)

print (f'{Buscar10}')

Buscar11 = re.findall(r'a{2}', Texto1)

print (f'{Buscar11}')

Buscar12 = re.findall(r'^esto', Texto1)
Buscar13 = re.findall(r'es$', Texto1)

print (f'{Buscar12}')
print (f'{Buscar13}')

Buscar14 = re.findall(r'hola', Texto1)

print (f'{Buscar14}')

Buscar15 = re.fullmatch('esto es 100 un! hola ejemplo cualquiera@ para baiaiai hela probar. el 123 @ concepto 8 de haala expresiones 45 regulares', Texto1)

print (f'{Buscar15}')

Buscar16 = re.findall(r'[0-9]*', Texto1)

print (f'{Buscar16}')

Buscar17 = re.findall(r'[0-9]{2,}', Texto1)

print (f'{Buscar17}')

Pattern1 = r'[0-9]{3}\s?\W'

Buscar18 = re.findall((r'[0-9]{3}\s+\W{1}'), Texto1)

print (f'{Buscar18}')

Texto2 = 'hola 125 este es mi nombre y mi numero'

Buscar19 = re.findall(r'[a-z]+|\d+', Texto2)

print (f'{Buscar19}')

Texto3 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern2 = r'[0-9]{2}\/\d{2}\/[0-9]{4}'

Reemplazar = 'XX/XX/XXXX'

Buscar20 = re.sub(Pattern2, Reemplazar, Texto3)

print (f'{Buscar20}')

Correo1 = 'sample@sample.com'

Pattern3 = r'^[a-zA-Z./*-+_-]+\@[a-zA-Z]+\.[a-z]{2,}$'

Buscar21 = bool(re.match(Pattern3, Correo1))

if (Buscar21 == True):
    print (f'El formato del correo es correcto')
else:
    print (f'El formato del correo es incorrecto')

def Exception1(Numero):
    try:
        Numerito = int(Numero)
        print (f'Gracias, el numero digitado es {Numerito}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Exception1("Hola")

def Exception2(Num1, Num2):
    try:
        Opera = Num1 + Num2
        print (f'El resultado de la operacion es {Opera}')
    except TypeError:
        print (f'Error, ambos elementos deben ser numeros')

Exception2(12, "Hola")

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(12, 0)

Lista_Exception4 = list(['Erick', 'Josue'])
Lista_Exception4.extend(['Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento con el indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, El indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = {
    'Nombre' : "Erick",
    'Edad' : 37
}

def Exception5(Llave):
    try:
        print (f'El elemento dentro de la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave seleccionada esta fuera de rango')

Exception5('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Elefante')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()