try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado no funciona')

from Module_Own import Pokemon as Poke

class Poke_Hija(Poke):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto1 = Poke_Hija(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno', 'Acero')
Objeto2 = Poke_Hija(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo', 'Hada')
Objeto3 = Poke_Hija(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Electrico')

Poke.Mostrar(Objeto1)
Objeto1.Mostrar()

print (f'------------')

Poke.Mostrar(Objeto2)
Objeto2.Mostrar()

print (f'------------')

Poke.Mostrar(Objeto3)
Objeto3.Mostrar()

print (f'------------')

class Camara():
    def Tomar_Fotografia(self):
        print (f'Fotografia Tomada')

class Reproductor_Musica:
    def Reproducir_Musica(self):
        print (f'Musica Reproducida')

class Smartphone(Camara, Reproductor_Musica):
    def Encender_Smartphone(self):
        print (f'Smartphone Encendido')

Objeto4 = Smartphone()

Objeto4.Encender_Smartphone()
Objeto4.Reproducir_Musica()
Objeto4.Tomar_Fotografia()

print (f'------------')

class Mascota:
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad} años')
        print (f'Peso: {self.Peso}kgs')

class Perro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento, Visitas):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        self.Visitas = Visitas

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        print (f'Visitas: {self.Visitas}')

Objeto5 = Perro('Chester', 3, 1.9, 'Poodle', 'Hipertension', 3)

Mascota.Mostrar(Objeto5)
Objeto5.Mostrar()

print (f'------------')

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

Objeto6 = Gato('Messi', 1.5, 1.40, 'Angora', 'Gris', 'Si')

Mascota.Mostrar(Objeto6)
Objeto6.Mostrar()

print (f'------------')

class Pajaro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto7 = Pajaro('Polly', 32, 0.60, 'Lora Verde', 'Si')

Mascota.Mostrar(Objeto7)
Objeto7.Mostrar()

print (f'------------')

class Atacante():
    def __init__(self, Damage, Weapon, Attack_Energy):
        self.Damage = Damage
        self.Weapon = Weapon
        self.Attack_Energy = Attack_Energy

    def Mostrar(self):
        print (f'Damage: {self.Damage}')
        print (f'Weapon: {self.Weapon}')
        print (f'Attack_Energy: {self.Attack_Energy}')

class Curador:
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life

    def Mostrar(self):
        print (f'Healing: {self.Healing}')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}')

class Paladin(Atacante, Curador):
    def __init__(self, Damage, Weapon, Attack_Energy, Healing, Potion, Life, Name):
        Atacante.__init__(self, Damage, Weapon, Attack_Energy)
        Curador.__init__(self, Healing, Potion, Life)
        self.Name = Name

    def Mostrar(self):
        print (f'Name: {self.Name}')

Objeto8 = Paladin(125, 'Hacha de fuego', 75, 20, 'Posion De Veneno', 500, 'Ghost Knight')

Objeto8.Mostrar()
Atacante.Mostrar(Objeto8)
Curador.Mostrar(Objeto8)

print (f'------------')

Clase_Hija = issubclass(Poke_Hija, Poke)

print (f'{Clase_Hija}')

Objeto_Clase = isinstance(Objeto8, Atacante)

print (f'{Objeto_Clase}')

print (f'------------')

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

Objeto9 = D()

A.Mostrar(Objeto9)
B.Mostrar(Objeto9)
C.Mostrar(Objeto9)
Objeto9.Mostrar()
E.Mostrar(Objeto9)

print (f'------------')

class Efectivo:
    def Pagar(self):
        print (f'Pago en efectivo')

class Tarjeta:
    def Pagar(self):
        print (f'Pago en Tarjeta')

class Criptomoneda:
    def Pagar(self):
        print (f'Pago en Criptomoneda')

Objeto10 = Criptomoneda()
Objeto11 = Tarjeta()
Objeto12 = Efectivo()

Objeto10.Pagar()
Objeto11.Pagar()
Objeto12.Pagar()

print (f'------------')

class Cuenta_Bancaria:
    def __init__(self, Saldo):
        self.__Saldo = Saldo

    def Depositar(self, Dinero):
        self.__Saldo += Dinero

    def Mostrar(self):
        print (f'Hola, tu saldo actual es ${self.__Saldo}')

    @property
    def dinero(self):
        return self.__Saldo

    @dinero.setter
    def dinero(self, New_Saldo):
        self.__Saldo = New_Saldo

Objeto13 = Cuenta_Bancaria(100)
Objeto13.Depositar(25)
Objeto13.Mostrar()

print (f'La variable privada con getter es {Objeto13.dinero}')

Objeto13.dinero = '20,000'

Objeto13.Mostrar()

print (f'------------')

from abc import ABC, abstractclassmethod

class Plantilla(ABC):

    @abstractclassmethod
    def Mostrar(self):
        pass

class Nombre(Plantilla):
    def Mostrar(self):
        print (f'Hola Muchachos')

Objeto14 = Nombre()

Objeto14.Mostrar()

import re

Texto1 = 'este es hola un te@xto cualquieraa 125 que hala yo voy a 90 ve-r por hela muchoba bueno o buenisimo  2 tiempo'

Buscar1 = re.search(r'\d+', Texto1)
Buscar2 = re.findall(r'\d+', Texto1)

print (f'{Buscar1}')

print (f'{Buscar2}')

Buscar3 = re.findall(r'\D+', Texto1)

print (f'{Buscar3}')

Buscar4 = re.findall(r'\w+', Texto1)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\W+', Texto1)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\s+', Texto1)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\S+', Texto1)

print (f'{Buscar7}')

Buscar8 = re.findall(r'h.la', Texto1)

print (f'{Buscar8}')

Buscar9 = re.findall(r'[a]{2}', Texto1)

print (f'{Buscar9}')

Buscar10 = re.findall(r'[a]{2,}', Texto1)

print (f'{Buscar10}')

Buscar11 = re.findall(r'[a]{2,4}', Texto1)

print (f'{Buscar11}')

Buscar12 = re.findall(r'[a]+', Texto1)

print (f'{Buscar12}')

Buscar13 = re.findall(r'[a]*', Texto1)

print (f'{Buscar13}')

Buscar14 = re.findall(r'[a]?', Texto1)

print (f'{Buscar14}')

Buscar15 = re.findall(r'(?=hala)+', Texto1)

print (f'{Buscar15}')

Buscar16 = re.fullmatch('este es hola un te@xto cualquieraa 125 que hala yo voy a 90 ve-r por hela mucho  2 tiempo', Texto1)

print (f'{Buscar16}')

Texto2 = '123 @'

Buscar17 = re.findall(r'^\d{3}\s?\W{1}$', Texto2)

print (f'{Buscar17}')

Buscar18 = re.findall(r'[ab]{2,4}', Texto1)

print (f'{Buscar18}')

Buscar19 = re.findall(r'[ab]+', Texto1)

print (f'{Buscar19}')

Buscar20 = re.findall(r'[0-9]{2,4}|hola', Texto1)

print (f'{Buscar20}')

Texto3 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern1 = r'[0-9]{2}/[0-9]{2}/[0-9]{4}'

Replacement = 'XX/XX/XXXX'

Nuevo_Texto = re.sub(Pattern1, Replacement, Texto3)

print (f'{Nuevo_Texto}')

print (f'------------')

def Exception1(Numero):
    try:
        Numerito = int(Numero)
        print (f'Gracias, tu numero es {Numerito}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Exception1("Hola")

def Exception2(Num1, Num2):
    try:
        Resultado = Num1 + Num2
        print (f'Gracias, el resultado de la operacion es {Resultado}')
    except TypeError:
        print (f'Error, necesito que ambos elementos sean numeros')

Exception2(12, "hola")

def Exception3(Num1, Num2):
    try:
        Div = Num1 / Num2
        print (f'El resultado de la division es {round(Div, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(12, 0)

Lista_Exception4 = list(['Erick', 'Josue', 'Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento en el indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'El indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'La llave seleccionada esta fuera de rango')

Exception5("Votante")

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Ardilla')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo seleccionado no existe')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nHiena'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()