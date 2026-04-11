import fontTools.tfmLib

try:
    import Module_Own as PEPE
except ImportError:
    print (f'El modulo elegido es incorrecto')

from Module_Own import Pokemon1 as Poke

class Poke_Kid1(Poke):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto1 = Poke(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto2 = Poke_Kid1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Acero')
Objeto3 = Poke(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro')

Objeto2.Mostrar()

print (f'-' * 20)

Poke.Mostrar(Objeto2)
Objeto2.Mostrar()

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

Objeto4 = Perro('Chester', 5, 2.5, 'Poodle', 'Asma')

Mascota.Mostrar(Objeto4)
Objeto4.Mostrar()

print (f'-' * 20)

class Gato(Mascota):
    def __init__(self, Nombre, Edad, Peso, Raza, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')

Objeto5 = Gato('Messi', 1.5, 1.2, 'Angora', 'Gris', 'No')

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

Objeto6 = Pajaro('Polly', 31, 0.4, 'Cacatua Amarilla', 'Si')

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

Objeto7 = Paladin(75, 'Battle Axe', 25, 'Black Lagoon', 200, 'Ghost Knight')

Objeto7.Mostrar()
Atacante.Mostrar(Objeto7)
Defensor.Mostrar(Objeto7)

print (f'-' * 20)

class A():
    def Mostrar(self):
        print (f'Hola A')

class E():
    def Mostrar(self):
        print (f'Hola E')

class B(E):
    def Mostrar(self):
        print (f'Hola B')

class C(A):
    def Mostrar(self):
        print (f'Hola C')

class D(B,C):
    def Mostrar(self):
        print (f'Hola D')

Objeto8 = D()

A.Mostrar(Objeto8)
B.Mostrar(Objeto8)
C.Mostrar(Objeto8)
Objeto8.Mostrar()
E.Mostrar(Objeto8)

print (f'-' * 20)

class Efectivo():
    def Pagar(self):
        print (f'El pago se realizo con Efectivo')

class Tarjeta:
    def Pagar(self):
        print (f'El pago se realizo con Tarjeta')

class Cripto:
    def Pagar(self):
        print (f'El pago se realizo con Cripto')

Objeto9 = Cripto()
Objeto10 = Tarjeta()
Objeto11 = Efectivo()

Objeto9.Pagar()
Objeto10.Pagar()
Objeto11.Pagar()

print (f'-' * 20)

class CuentaBancaria:
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
        print (f'Su saldo a la fecha es de ${self.__Saldo}')

Objeto11 = CuentaBancaria(100)
Objeto11.Depositar(25)
Objeto11.Mostrar()

print (f'El saldo privado es de {Objeto11.Dinero}')

Objeto11.Dinero = '20,000'

Objeto11.Mostrar()

print (f'El saldo privado es de {Objeto11.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def Obligatoria(self):
        pass

class Ejemplo1(Plantilla):
    def Mostrar(self):
        print (f'Hola Mundo')

    def Obligatoria(self):
        print (f'Hola Ejemplo Abstraccion')

Objeto12 = Ejemplo1()

Objeto12.Mostrar()
Objeto12.Obligatoria()

class Uno:
    def Mensajear(self):
        print (f'El mensaje de Uno aparece en Dos')

class Dos():
    def __init__(self):
        self.Mensaje = Uno()

    def Mostrar(self):
        self.Mensaje.Mensajear()

Objeto13 = Dos()

Objeto13.Mostrar()

print (f'-' * 20)

import re

Texto1 = 'este es hola un 15 texto de ejemplo hela 250 @ para probar que la hala 1000 mica sirve'

Buscar1 = re.search('para', Texto1)

print (f'{Buscar1}')

Buscar2 = re.findall('e', Texto1)

print (f'{Buscar2}')

Buscar3 = re.fullmatch('este es hola un 15 texto de ejemplo hela 250 para probar que la hala 1000 mica sirve', Texto1)

print (f'{Buscar3}')

Buscar4 = re.findall(r'\d{1}', Texto1)

print (f'{Buscar4}')

Buscar5 = re.findall('h.la', Texto1)

print (f'{Buscar5}')

Buscar6 = re.findall(r'(texto|250)', Texto1)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\d{3}\s{1}\W{1}', Texto1)

print (f'{Buscar7}')

Buscar8 = re.findall(r'[ar]{2,4}', Texto1)

print (f'{Buscar8}')

Buscar9 = re.findall(r'[0-9]{2,4}', Texto1)

print (f'{Buscar9}')

Telefono1 = 'sample@hotmail.org'

Pattern1 = r'^[a-zA-Z0-9./*-+=_-]+\@(hotmail|gmail|yahoo)\.(com|net|org)$'

Buscar10 = bool(re.fullmatch(Pattern1, Telefono1))

if (Buscar10 == True):
    print (f'El formato del correo es correcto')
else:
    print (f'El formato del correo es incorrecto')

Fecha = 'Necesito confirmar que la siguiente fecha 12/29/2026 tiene el formato correcto'

Pattern2 = r'[0-9]{2}\/[0-9]{2}\/[0-9]{4}'

Replacement = 'xx/xx/xxxx'

Buscar11 = re.sub(Pattern2, Replacement, Fecha)

print (f'{Buscar11}')

print (f'-' * 20)

Buscar12 = re.findall(r'(0[1-9]|[12][0-9]|3[01])', '32')

print (f'{Buscar12}')