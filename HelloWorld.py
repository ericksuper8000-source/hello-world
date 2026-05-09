Texto1 = "   Hola!!!   mundo@@   123   "

print (f'{Texto1}')

Texto1_Version1 = Texto1.lower()

print (f'{Texto1_Version1}')

Texto1_Version2 = Texto1_Version1.strip()

print (f'{Texto1_Version2}')

Texto1_Version3 = ' '.join(Texto1_Version2.split())

print (f'{Texto1_Version3}')

import re

Texto1_Version4 = re.sub(r'[^a-z0-9\s]', '', Texto1_Version3)

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
    print (f'Error de formato, fecha incorrecta')
    exit()

Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']

Encontrado1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()]

if (Encontrado1.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! encontramos ventas')
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_May = Grupo1.idxmax()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_May_Cant = Grupo1.max()
    Grupo1_Min_Cant = Grupo1.min()

    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_May} vendio {Grupo1_May_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Min} vendio {Grupo1_Min_Cant} unidades')

    Grupo2 = Encontrado1['TOTALITO'].sum()

    Grupo3 = Grupo1.count()

    print (f'El total de dinero que se vendio en {Fech1_Formateada} fue de ${Grupo2}')
    print (f'En {Fech1_Formateada} se realizaron {Grupo3} ventas por cliente, sin embargo el total de productos vendidos fueron: {sum(Encontrado1['quantity'])}')

Set_A = {1, 2, 3, 4}
Set_B = {3, 4, 5, 6}
Set_C = set({1, 2, 3, 4, 5})
Set_D = set({4, 5})
Set_E = set({8})

print (f'{Set_A.union(Set_B)}')
print (f'{Set_A | Set_B}')

print (f'-' * 20)

print (f'{Set_A.intersection(Set_B)}')
print (f'{Set_A & Set_B}')

print (f'-' * 20)

print (f'{Set_A.difference(Set_B)}')
print (f'{Set_A - Set_B}')

print (f'-' * 20)

print (f'{Set_B.difference(Set_A)}')
print (f'{Set_B - Set_A}')

print (f'-' * 20)

print (f'{Set_A.symmetric_difference(Set_B)}')
print (f'{Set_A ^ Set_B}')

print (f'-' * 20)

print (f'{Set_C.issuperset(Set_D)}')
print (f'{Set_C >= Set_D}')
print (f'-' * 20)
print (f'{Set_D.issubset(Set_C)}')
print (f'{Set_D <= Set_C}')
print (f'-' * 20)
print (f'{Set_C.isdisjoint(Set_E)}')

print (f'-' * 20)

'''Set_A.update(Set_B)

print (f'{Set_A}')'''

'''Set_A.intersection_update(Set_B)

print (f'{Set_A}')'''

'''Set_A.difference_update(Set_B)

print (f'{Set_A}')'''

'''Set_B.difference_update(Set_A)

print (f'{Set_B}')'''

Set_A.symmetric_difference_update(Set_B)

print (f'{Set_A}')

print (f'-' * 20)

# Esto es un ejercicio simple de composicion
class Caramelo():
    def Elegir(self):
        return f'Caramelo'

class Pastel:
    def __init__(self):
        self.Favorito = Caramelo()

    def Hornear(self):
        print (f'Acabas de hornear un pastel de {self.Favorito.Elegir()}')

Objeto1 = Pastel()

Objeto1.Hornear()

print (f'-' * 20)

# Esto es un ejemplo de composicion compleja tambien conocida como inyeccion de dependencias

class Fresa():
    def Elegir(self):
        return f'Fresa'

class Chocolate:
    def Elegir(self):
        return f'Chocolate'

class Vainilla:
    def Elegir(self):
        return f'Vainilla'

class Pastel2:
    def __init__(self, Favorito):
        self.Favorito = Favorito

    def Hornear(self):
        print (f'Acabas de hornear un pastel de {self.Favorito.Elegir()}')

Sabore1 = Fresa()
Objeto2 = Pastel2(Sabore1)
Objeto2.Hornear()

print (f'-' * 20)

Sabore2 = Chocolate()
Objeto3 = Pastel2(Sabore2)
Objeto3.Hornear()

print (f'-' * 20)

Sabore3 = Vainilla()
Objeto4 = Pastel2(Sabore3)
Objeto4.Hornear()

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

Pattern1 = r'[a-zA-Z0-9]+[\.\_\+][a-zA-Z0-9]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

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

Buscar2 = re.sub(r'\!|\?|\.{2,}', '', Texto3)

print (f'{Buscar2}')

Buscar3 = re.sub(r'\d+', '', Buscar2)

print (f'{Buscar3}')

print (f'-' * 20)

try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo no existe')

from Module_Own import Pokemon1 as Poke1

Objeto5 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto6 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')
Objeto7 = Poke1(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro')

Objeto5.Mostrar()

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto7 = Poke_Kid1(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto7)
Objeto7.Mostrar()

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

Objeto8 = Perro1('Chester', 2.5, 5, 'Poodle', 'Asma')

Veterinaria1.Mostrar(Objeto8)
Objeto8.Mostrar()

print (f'-' * 20)

class Gato1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')

Objeto9 = Gato1('Messi', 1.5, 1.8, 'Gris', 'No')

Veterinaria1.Mostrar(Objeto9)
Objeto9.Mostrar()

print (f'-' * 20)

class Pajaro1(Veterinaria1):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto10 = Pajaro1('Polly', 31, 0.4, 'Lora Verde', 'Si')

Veterinaria1.Mostrar(Objeto10)
Objeto10.Mostrar()

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

Objeto11 = Paladin(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto11.Mostrar()
Atacante.Mostrar(Objeto11)
Defensor.Mostrar(Objeto11)

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

Objeto12 = D1()

A1.Mostrar(Objeto12)
B1.Mostrar(Objeto12)
C1.Mostrar(Objeto12)
Objeto12.Mostrar()
E1.Mostrar(Objeto12)

print (f'-' * 20)

class Efectivo1():
    def Pagar(self):
        print (f'El pago se a realizado con efectivo')

class Tarjeta1():
    def Pagar(self):
        print (f'El pago se a realizado con tarjeta')

class Cripto1():
    def Pagar(self):
        print (f'El pago se a realizado con cripto')

Objeto13 = Efectivo1()
Objeto14 = Tarjeta1()
Objeto15 = Cripto1()

Objeto13.Pagar()
Objeto14.Pagar()
Objeto15.Pagar()

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

Objeto16 = Cuenta_Bancaria1(100)
Objeto16.Depositar(25)
Objeto16.Mostrar()

print (f'Tu saldo privado es de {Objeto16.Dinero}')

Objeto16.Dinero = '30,000'

Objeto16.Mostrar()

print (f'Tu saldo privado es de {Objeto16.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla1(ABC):
    @abstractmethod
    def Mostrar(self):
        pass

class Plantilla1_under1(Plantilla1):
    def Desplegar(self):
        print (f'Esto es el texto de Plantilla uno under')

    def Mostrar(self):
        print (f'Este es el metodo obligatorio')

Objeto17 = Plantilla1_under1()

Objeto17.Desplegar()
Objeto17.Mostrar()

import re

Texto4 = 'esto hela es 12 un @ texto cualquiera 666 ! que!!! hola puedo usar hula 150 como ejemplo'

Buscar4 = re.search(r'puedo', Texto4)

print (f'{Buscar4}')

Buscar5 = re.findall(r'[ue]', Texto4)

print (f'{Buscar5}')

Buscar6 = re.fullmatch(r'esto hela es 12 un @ texto cualquiera 666 ! que!!! hola puedo usar hula 150 como ejemplo', Texto4)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\d{2}', Texto4)

print (f'{Buscar7}')

Buscar8 = re.findall(r'h.la', Texto4)

print (f'{Buscar8}')

Buscar9 = re.findall(r'^esto', Texto4)
Buscar10 = re.findall(r'o$', Texto4)

print (f'{Buscar9}')
print (f'{Buscar10}')

Buscar11 = re.findall(r'\d{3}\s\W', Texto4)

print (f'{Buscar11}')

Email1 = 'sample@sample.com'

Pattern2 = r'^[a-zA-Z0-9\.\*\/\-\+\_\-]+\@[a-zA-Z]+\.(?:com|org|net)$'

Buscar12 = bool(re.match(Pattern2, Email1))

if (Buscar12):
    print (f'Formato de correo valido')
else:
    print (f'Formato invalido')

Email2 = 'sample@yahoo.com'

Pattern3 = r'^[a-zA-Z0-9\.\/\*\-\+\_\-]+\@(?:gmail|hotmail|yahoo)\.(?:org|com|net)$'

Buscar13 = bool(re.match(Pattern3, Email2))

if (Buscar13 == True):
    print (f'Formato de correo valido')
else:
    print (f'Formato invalido')

Numero1 = '28'

Pattern4 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar14 = bool(re.match(Pattern4, Numero1))

if (Buscar14):
    print (f'Correcto, el numero se encuentra entre 1 y 31')
else:
    print (f'Formato incorrecto')

Texto5 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern5 = r'\d{2}\/[0-9]{2}\/\d{3,4}'

Replacement5 = 'XX/XX/XXXX'

Buscar15 = re.sub(Pattern5, Replacement5, Texto5)

print (f'{Buscar15}')

Pattern6 = r'\+\d{1}\-[0-9]{3}\-[0-9]{3}\-\d{4}'

Replacement6 = "+DATE"

Buscar16 = re.sub(Pattern6, Replacement6, Buscar15)

print (f'{Buscar16}')

print (f'-' * 20)

def Exception1(Texto):
    try:
        Num1 = int(Texto)
        return Num1
    except ValueError:
        return f'Error, necesito que ingreses un numero'

print (f'{Exception1(99)}')

print (f'-' * 20)

def Exception2(Numero):
    try:
        Num2 = float(Numero)
        return Num2
    except ValueError:
        return f'Error, el numero no es decimal'

print (f'{Exception2(2.4)}')

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        Resultado = Num1 + Num2
        return f'El resultado de la operacion es {Resultado}'
    except TypeError:
        return f'Error, ambos elementos deben ser numeros'

print (f'{Exception3(12, 7)}')

def Exception4(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception4(14, 0)

Lista_Exception5 = list(['Erick', 'Josue', 'Karlita'])

def Exception5(Indice):
    try:
        print (f'El elemento en la posicion {Indice} es {Lista_Exception5[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception5(3)

Diccionario_Exception6 = dict({'Nombre' : "Josue", 'Edad' : 37})

def Exception6(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception6[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception6('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Hiena')
        Docu.close()
except FileNotFoundError:
    print (f'Error, El archivo seleccionado no existe')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nSalamandra'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nTortuga')
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

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

print (f'{Data_Frame1}')

print (f'-' * 20)

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame_Concatenate_Age}')

print (f'La suma de todas las edades es {Data_Frame_Concatenate_Age.sum()}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()} y la mayor de las edades es {Data_Frame_Concatenate_Age.max()}')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Aqui1 = elemento['Nombre']
    Aqui2 = elemento['Edad']

    print (f'Mi nombre es {Aqui1} y mi edad es {Aqui2} años')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate}')

Grupo4 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()

Grupo4_May = Grupo4.idxmax()
Grupo4_Min = Grupo4.idxmin()
Grupo4_May_Cant = Grupo4.max()
Grupo4_Min_Cant = Grupo4.min()

print (f'El mayor es {Grupo4_May} -- ({Grupo4_May_Cant} años)')
print (f'El menor es {Grupo4_Min} -- ({Grupo4_Min_Cant} años)')

Grupo5 = Data_Frame_Concatenate['Edad'].count()

print (f'Tenemos actualmente {Grupo5} personas en el dataframe')

'''import pandas as pd
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

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.tail(1)}')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'Filas: {Filas}')
print (f'Columnas: {Columnas}')

print (f'-' * 20)

import re

texto = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Pattern7 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|net|org)'

Emails = re.findall(Pattern7, texto)

print (f'{Emails}')

print (f'-' * 20)

texto_temporal = texto
for i, correo in enumerate(Emails, start=1):
    texto_temporal = texto_temporal.replace(correo, f'Email_{i}')

print (f'{texto_temporal}')

texto_nuevo = re.sub(r'\!|\?|\.{2,}', '', texto_temporal)

print (f'-' * 20)

print (f'{texto_nuevo}')

print (f'-' * 20)

for i, correo in enumerate(Emails, start=1):
    texto_nuevo = texto_nuevo.replace(f'Email_{i}', correo)

print (f'-' * 20)

print (f'{texto_nuevo}')

print (f'-' * 20)

Texto6 = "   Hola!!!   mundo@@   123   "

print (f'{Texto6}')

Texto6_Version1 = Texto6.lower()

print (f'{Texto6_Version1}')

Texto6_Version2 = Texto6_Version1.strip()

print (f'{Texto6_Version2}')

Texto6_Version3 = ' '.join(Texto6_Version2.split())

print (f'{Texto6_Version3}')

import re

Texto6_Version4 = re.sub(r'[^a-zA-Z0-9\s]', '', Texto6_Version3)

print (f'{Texto6_Version4}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv2 = 'C:\\Repo\\Store.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

print (f'-' * 20)

Fecha2 = '2026-04-01'

try:
    Fech2 = datetime.strptime(Fecha2, '%Y-%m-%d').date()
    Fech2_Formateada = pd.to_datetime(Fech2)
    Cargar_Csv2['date'] = pd.to_datetime(Cargar_Csv2['date'])
except ValueError:
    print (f'Error, formato incorrecto')
    exit()

Cargar_Csv2['FINALITO'] = Cargar_Csv2['quantity'] * Cargar_Csv2['price']

Encontrado2 = Cargar_Csv2[Cargar_Csv2['date'].dt.date == Fech2_Formateada.date()]

if (Encontrado2.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! ventas encontradas')
    Grupo6 = Encontrado2.groupby('product')['quantity'].sum()

    Grupo6_May = Grupo6.idxmax()
    Grupo6_Min = Grupo6.idxmin()
    Grupo6_May_Cant = Grupo6.max()
    Grupo6_Min_Cant = Grupo6.min()

    print (f'En {Fech2_Formateada} el producto {Grupo6_May} vendio {Grupo6_May_Cant} unidades')
    print (f'En {Fech2_Formateada} el producto {Grupo6_Min} vendio {Grupo6_Min_Cant} unidades')

    Grupo7 = Grupo6.count()
    Grupo8 = Encontrado2['quantity'].sum()

    print (f'En {Fech2_Formateada} se realizaron {Grupo7} ventas, pero la cantidad de productos vendidos fue {Grupo8}')

    Grupo9 = Encontrado2['FINALITO'].sum()

    print (f'La cantidad de dinero en ventas generado durante {Fech2_Formateada} fue ${Grupo9}')

print (f'-' * 20)

Set_A2 = {1, 2, 3, 4}
Set_B2 = {3, 4, 5, 6}

print (f'{Set_A2.union(Set_B2)}')
print (f'{Set_A2 | Set_B2}')

print (f'-' * 20)

print (f'{Set_A2.intersection(Set_B2)}')
print (f'{Set_A2 & Set_B2}')

print (f'-' * 20)

print (f'{Set_A2.difference(Set_B2)}')
print (f'{Set_A2 - Set_B2}')

print (f'-' * 20)

print (f'{Set_B2.difference(Set_A2)}')
print (f'{Set_B2 - Set_A2}')

print (f'-' * 20)

print (f'{Set_A2.symmetric_difference(Set_B2)}')
print (f'{Set_A2 ^ Set_B2}')

print (f'-' * 20)

Set_C2 = {1, 2, 3, 4, 5}
Set_D2 = {4, 5}
Set_E2 = set({8})

print (f'{Set_C2.issuperset(Set_D2)}')
print (f'{Set_C2 >= Set_D2}')
print (f'-' * 20)
print (f'{Set_D2.issubset(Set_C2)}')
print (f'{Set_D2 <= Set_C2}')
print (f'-' * 20)
print (f'{Set_C2.isdisjoint(Set_E2)}')

print (f'-' * 20)

'''Set_A2.update(Set_B2)

print (f'{Set_A2}')'''

'''Set_A2.intersection_update(Set_B2)

print (f'{Set_A2}')'''

'''Set_A2.difference_update(Set_B2)

print (f'{Set_A2}')'''

'''Set_B2.difference_update(Set_A2)

print (f'{Set_B2}')'''

Set_A2.symmetric_difference_update(Set_B2)

print (f'{Set_A2}')

print (f'-' * 20)

class Caramelo2():
    def Ingrediente(self):
        return f'Caramelo'

class Pastel2:
    def __init__(self):
        self.Elegir = Caramelo2()

    def Hornear(self):
        print (f'Acabas de hornear un pastel de {self.Elegir.Ingrediente()}')

Objeto18 = Pastel2()

Objeto18.Hornear()

print (f'-' * 20)

class Chocolate2():
    def Sabor(self):
        return f'Chocolate'

class Vainilla2:
    def Sabor(self):
        return f'Vainilla'

class Fresa2:
    def Sabor(self):
        return f'Fresa'

class Pastel3:
    def __init__(self, Elegido):
        self.Elegido = Elegido

    def Hornear(self):
        print (f'Acabas de hornear un pastel de {self.Elegido.Sabor()}')

Sabore4 = Chocolate2()
Objeto19 = Pastel3(Sabore4)
Objeto19.Hornear()

Sabore5 = Vainilla2()
Objeto20 = Pastel3(Sabore5)
Objeto20.Hornear()

Sabore6 = Fresa2()
Objeto21 = Pastel3(Sabore6)
Objeto21.Hornear()

print (f'-' * 20)

import re

# usuario@dominio.extension
Texto7 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Pattern8 = r'[a-zA-Z0-9\.\_\+]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar17 = re.findall(Pattern8, Texto7)

print (f'{Buscar17}')

for indice, elemento in enumerate(Buscar17, start=1):
    print (f'{indice} -- {elemento}')


import re

Texto8 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Buscar18 = re.sub(r'\!|\?|\.{2,}', '', Texto8)

print (f'{Buscar18}')

Buscar19 = re.sub(r'\d+', '', Buscar18)

print (f'{Buscar19}')

import re

Texto9 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Correos = re.findall(r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)', Texto9)

print (f'{Correos}')

Texto9_temp = Texto9

for i, email in enumerate(Correos, start=1):
    Texto9_temp = Texto9_temp.replace(email, f'EMAIL_{i}')

print (f'{Texto9_temp}')

Texto9_temp2 = re.sub(r'\!|\?|\.{2,}', '', Texto9_temp)

print (f'{Texto9_temp2}')

for i, email in enumerate(Correos, start=1):
    Texto9_temp2 = Texto9_temp2.replace(f'EMAIL_{i}', email)

print (f'{Texto9_temp2}')

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

for elemento in PEPE.Diccionario_Poke:
    print (f'{PEPE.Diccionario_Poke[elemento]}')

print (f'-' * 20)

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

print (f'-' * 20)

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel)

print (f'{Cargar_Excel.head()}')

Grupo10 = Cargar_Excel.groupby('nombre')['tarifa'].sum()

print (f'La persona que pago mas por su tiquete fue {Grupo10.idxmax()}')

print (f'-' * 20)

Cargar_Excel1 = pd.read_excel(Ruta_Excel, sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, index_col='cabina')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:K')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:K', nrows=1)

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

import pandas as pd

Ruta_Html = 'C:\\Repo\\HolaMundo.txt'

Cargar_Html = pd.read_csv(Ruta_Html)

print (f'{Cargar_Html}')

print (f'-' * 20)

print (f'{Cargar_Html.head()}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv3 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

Grupo11 = Cargar_Csv3.groupby('Nombre')['Edad'].sum()

print (f'El menor de las personas es {Grupo11.idxmin()}')

print (f'-' * 20)

import pandas as pd
import requests
import io

Ruta_Html2 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html2, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Leer_Html)

print (f'{Cargar_Html2[1].head()}')

print (f'-' * 20)

Array0 = [[1, 2, 3], [4, 5, 6]]

print (f'{Array0[1][::2]}')
print (f'{Array0[0][::3]}')
print (f'{Array0[1][:2]}')
print (f'{Array0[0][2:]}')
print (f'{Array0[1][1:2]}')
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
print (f'{Array1[1]}')

print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[2:3]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 <= 2]}')

print (f'-' * 20)

Array2 = np.array([[4, 5, 6], [7, 8, 9]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 0]}')

print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[0, :2]}')
print (f'{Array2[0, 2:]}')
print (f'{Array2[:, 0]}')
print (f'{Array2[1, 2:3]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 <= 6]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodados: {Array2_Sorted}')
print (f'media: {round(Array2_Sorted_Mean, 2)}')
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

Array3 = np.array([[['e', 'i', 'j'], ['d', 'x', 'a']],     [['f', 'v', 'k'], ['r', 'o', 'n']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 2]}')

print (f'{Array3[1, 0, ::2]}')
print (f'{Array3[1, 1, ::3]}')
print (f'{Array3[0, 0, :2]}')
print (f'{Array3[0, 0, 2:]}')
print (f'{Array3[1, :, 0]}')
print (f'{Array3[1, 1, 2:3]}')
print (f'{Array3[1, 0, 0:None]}')
print (f'{Array3[1, 0, :]}')
print (f'{Array3[Array3 == "a"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],       [[[6, 5, 4], [9, 8, 7]], [[4, 5, 6], [9, 5, 1]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[0, 1, 0, 1]}')

print (f'{Array4[1, 0, 1, ::2]}')
print (f'{Array4[1, 0, 1, ::3]}')
print (f'{Array4[1, 1, 0, :2]}')
print (f'{Array4[1, 1, 0, 2:]}')
print (f'{Array4[1, 0, :, 2]}')
print (f'{Array4[0, 0, 1, 2:3]}')
print (f'{Array4[1, 0, 0, 0:None]}')
print (f'{Array4[1, 0, 0, :]}')
print (f'{Array4[Array4 <= 2]}')

print (f'-' * 20)

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

print (f'-' * 20)

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[0, 1, 0, 0:None])
Sumita8 = np.sum(Array4_Sorted[0, 1, 0, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_Mayor = np.max(Array_Num1)
Array_Menor = np.min(Array_Num1)

print (f'El numero menor de la lista es {Array_Menor} y el mayor es {Array_Mayor}')

print (f'-' * 20)

Array_Num2 = np.arange(start=1, stop=26, step=1)

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

Array_Num2_Column_Max = np.max(Array_Num2_Reshape, axis=0)
Array_Num2_Column_Min = np.min(Array_Num2_Reshape, axis=0)
Array_Num2_Row_Max = np.max(Array_Num2_Reshape, axis=1)
Array_Num2_Row_Min = np.min(Array_Num2_Reshape, axis=1)

print (f'Los menores de las columnas son {Array_Num2_Column_Min}')
print (f'Los mayores de las columnas son {Array_Num2_Column_Max}')
print (f'Los menores de las filas son {Array_Num2_Row_Min}')
print (f'Los mayores de las filas son {Array_Num2_Row_Max}')

print (f'-' * 20)

Array_Zero = np.zeros(shape=(2, 3))

print (f'{Array_Zero}')
print (f'{Array_Zero.ndim}') # 2
print (f'{Array_Zero.shape}') # 2x3
print (f'{Array_Zero.size}') # 6
print (f'{Array_Zero.dtype}') # int64
print (f'{Array_Zero[1, 0]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}') # 2
print (f'{Array_Ones.shape}') # 2x3
print (f'{Array_Ones.size}') # 6
print (f'{Array_Ones.dtype}') # int64
print (f'{Array_Ones[1, 1]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}') # 2
print (f'{Array_Gen1.shape}') # 2x3
print (f'{Array_Gen1.size}') # 6
print (f'{Array_Gen1.dtype}') # <U1
print (f'{Array_Gen1[1, 2]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[3]}')

print (f'-' * 20)

Lista_Array_Gen2 = []

for elemento in Array_Gen2:
    Lista_Array_Gen2.append(str(elemento))

print (f'{Lista_Array_Gen2}')
print (f'{type(Lista_Array_Gen2)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4_Sorted[0, 1, 1, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 1]}')

print (f'-' * 20)

Set_Conjunto_Array = set({1, 2, 3})
Tupla_Array = tuple(('Rojo', 'Verde'))

Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value = Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value = Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value = Diccionario_Array['Nombre'][2])

print (f'{Array_Gen4}')
print (f'-' * 20)
print (f'{Array_Gen5}')
print (f'-' * 20)
print (f'{Array_Gen6}')

print (f'-' * 20)

print (f'{Array_Gen6[3]}')

print (f'-' * 20)

Array_Num3 = np.arange(start=1, stop=6, step=1)
Array_Num4 = np.arange(start=2, stop=11, step=2)
Array_Num5 = np.arange(start=3, stop=31, step=3)
Array_Num6 = np.arange(start=10, stop=21, step=2)
Array_Num7 = np.arange(10)

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
print (f'{Array_Random2.ndim}') # 2
print (f'{Array_Random2.shape}') # 2x3
print (f'{Array_Random2.size}') # 6
print (f'{Array_Random2.dtype}') # int64
print (f'{Array_Random2[1, 2]}')

print (f'-' * 20)

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodados : {Array_Random2_Sorted}')
print (f'Media : {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria : {Array_Random2_Sorted_Sum}')

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

Array_Num8 = np.arange(20)

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Lista_Array1 = ['Erick', 'Josue', 'Karlita']

Array5 = np.array(Lista_Array1)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-' * 20)

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concatenate([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'-' * 20)

Array_Concatenate_Splitted = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Splitted[0]}')
print (f'{Array_Concatenate_Splitted[1]}')
print (f'{Array_Concatenate_Splitted[2]}')

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

Array00 = [[1, 2, 3], [4, 5, 6]]

for i in range(len(Array00)):
    for j in range(len(Array00[i])):
        print (f'{Array00[i][j]}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')
print (f'{Array_Random3.ndim}')
print (f'{Array_Random3.shape}')
print (f'{Array_Random3.size}')
print (f'{Array_Random3.dtype}')
print (f'{Array_Random3[1, 0, 1]}')

print (f'{Array_Random3[1, 0, ::2]}')
print (f'{Array_Random3[0, 0, ::3]}')
print (f'{Array_Random3[1, 1, :2]}')
print (f'{Array_Random3[1, 1, 2:]}')
print (f'{Array_Random3[0, :, 0]}')
print (f'{Array_Random3[0, 1, 2:3]}')
print (f'{Array_Random3[1, 1, 0:None]}')
print (f'{Array_Random3[1, 1, :]}')
print (f'{Array_Random3[Array_Random3 <= 2]}')

print (f'-' * 20)

Array_Random3_Sorted = np.sort(Array_Random3)
Array_Random3_Sorted_Mean = np.mean(Array_Random3_Sorted)
Array_Random3_Sorted_Sum = np.sum(Array_Random3_Sorted)

print (f'Acomodado: {Array_Random3_Sorted}')
print (f'Media: {round(Array_Random3_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random3_Sorted_Sum}')

Sumita9 = np.sum(Array_Random3_Sorted, axis=0)
Sumita10 = np.sum(Array_Random3_Sorted, axis=1)
Sumita11 = np.sum(Array_Random3_Sorted[1, 0, 0:None])
Sumita12 = np.sum(Array_Random3_Sorted[1, 0, :])

print (f'{Sumita9}')
print (f'{Sumita10}')
print (f'{Sumita11}')
print (f'{Sumita12}')

print (f'-' * 20)

Lista_Array2 = list([])
Lista_Array2.append('Roberto')
Lista_Array2.insert(1, 'Karlita')
Lista_Array2.extend(['Erick', 'Roxana'])
Lista_Array2.append('Josue')
Lista_Array2.insert(2, 'Carmelo')

Ganador1 = np.random.choice(Lista_Array2, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Array2, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Array2, size=(2, 3), replace=False)

print (f'Ganador del sorteo: {Ganador1}')
print (f'Ganador del sorteo: {Ganador2}')
print (f'Ganador del sorteo: {Ganador3}')

print (f'-' * 20)

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-' * 20)

Texto10 = "   Hola!!!   mundo@@   123   "

print (f'{Texto10}')

Texto10_Version1 = Texto10.strip()

print (f'{Texto10_Version1}')

Texto10_Version2 = ' '.join(Texto10_Version1.split())

print (f'{Texto10_Version2}')

Texto10_Version3 = Texto10_Version2.lower()

import re

Texto10_Version4 = re.sub(r'[^a-z0-9\s]+', '', Texto10_Version3)

print (f'{Texto10_Version4}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv4 = 'C:\\Repo\\Store.csv'

Cargar_Csv4 = pd.read_csv(Ruta_Csv4)

print (f'{Cargar_Csv4}')

print (f'-' * 20)

Fecha3 = '2026-04-01'

try:
    Fech3 = datetime.strptime(Fecha3, '%Y-%m-%d').date()
    Fech3_Formateada = pd.to_datetime(Fech3)
    Cargar_Csv4['date'] = pd.to_datetime(Cargar_Csv4['date'])
except ValueError:
    print (f'Error, formato de fecha incorrecto')
    exit()

Cargar_Csv4['TOTALITO'] = Cargar_Csv4['quantity'] * Cargar_Csv4['price']

Encontrado3 = Cargar_Csv4[Cargar_Csv4['date'].dt.date == Fech3_Formateada.date()]

if (Encontrado3.empty):
    print (f'No se han encontrado ventas en {Fech3_Formateada}')
else:
    print (f'Genial! ventas encontradas')
    Grupo12 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo12_May = Grupo12.idxmax()
    Grupo12_Min = Grupo12.idxmin()
    Grupo12_May_Cant = Grupo12.max()
    Grupo12_Min_Cant = Grupo12.min()

    print (f'En la fecha {Fech3_Formateada} el producto {Grupo12_May} vendio un total de {Grupo12_May_Cant} unidades')
    print (f'En la fecha {Fech3_Formateada} el producto {Grupo12_Min} vendio un total de {Grupo12_Min_Cant} unidades')
    print (f'-' * 20)
    print (f'En {Fech3_Formateada} se realizaron {Grupo12.count()} ventas')
    print (f'La cantidad de ventas individuales en esta fecha fueron {Grupo12.sum()}')
    print (f'-' * 20)

    Grupo13 = Encontrado3.groupby('product')['TOTALITO'].sum()

    print (f'El total en dolares vendido durante {Fech3_Formateada} fue de ${Grupo13.sum()}')

Set_A3 = {1, 2, 3, 4}
Set_B3 = set({3, 4, 5, 6})

print (f'{Set_A3.union(Set_B3)}')
print (f'{Set_A3 | Set_B3}')

print (f'-' * 20)

print (f'{Set_A3.intersection(Set_B3)}')
print (f'{Set_A3 & Set_B3}')

print (f'-' * 20)

print (f'{Set_A3.difference(Set_B3)}')
print (f'{Set_A3 - Set_B3}')

print (f'-' * 20)

print (f'{Set_B3.difference(Set_A3)}')
print (f'{Set_B3 - Set_A3}')

print (f'-' * 20)

print (f'{Set_A3.symmetric_difference(Set_B3)}')
print (f'{Set_A3 ^ Set_B3}')

print (f'-' * 20)

Set_C3 = {1, 2, 3, 4, 5}
Set_D3 = {4, 5}
Set_E3 = set({8})

print (f'{Set_C3.issuperset(Set_D3)}')
print (f'{Set_C3 >= Set_D3}')
print (f'-' * 20)
print (f'{Set_D3.issubset(Set_C3)}')
print (f'{Set_D3 <= Set_C3}')
print (f'-' * 20)
print (f'{Set_C3.isdisjoint(Set_E3)}')

print (f'-' * 20)

'''Set_A3.update(Set_B3)

print (f'{Set_A3}')'''

'''Set_A3.intersection_update(Set_B3)

print (f'{Set_A3}')'''

'''Set_A3.difference_update(Set_B3)

print (f'{Set_A3}')'''

'''Set_B3.difference_update(Set_A3)

print (f'{Set_B3}')'''

Set_A3.symmetric_difference_update(Set_B3)

print (f'{Set_A3}')

print (f'-' * 20)

class Caramelo3():
    def Sabor(self):
        return f'Caramelo'

class Pastel3:
    def __init__(self):
        self.Elegir = Caramelo3()

    def Hornear(self):
        print (f'Horneaste un pastel de {self.Elegir.Sabor()}')

Objeto22 = Pastel3()

Objeto22.Hornear()

print (f'-' * 20)

class Chocolate3():
    def Sabor(self):
        return f'Chocolate'

class Vainilla3:
    def Sabor(self):
        return f'Vainilla'

class Fresa3:
    def Sabor(self):
        return f'Fresa'

class Pastel4:
    def __init__(self, Elegir):
        self.Elegir = Elegir

    def Hornear(self):
        print (f'Acabas de hornear un paste de {self.Elegir.Sabor()}')

Sabore7 = Chocolate3()
Objeto23 = Pastel4(Sabore7)
Objeto23.Hornear()

Sabore8 = Vainilla3()
Objeto24 = Pastel4(Sabore8)
Objeto24.Hornear()

Sabore9 = Fresa3()
Objeto25 = Pastel4(Sabore9)
Objeto25.Hornear()

print (f'-' * 20)

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

Buscar20 = re.findall(Pattern9, Texto11)

print (f'{Buscar20}')

for elemento in enumerate(Buscar20):
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'-' * 20)

import re

Texto12 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Buscar21 = re.sub(r'\!|\?|\.{2,}', '', Texto12)

print (f'{Buscar21}')

Buscar22 = re.sub(r'\d+', '', Buscar21)

print (f'{Buscar22}')

print (f'-' * 20)

import re

Texto13 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Pattern10 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:org|com|net)'

Correos = re.findall(Pattern10, Texto13)

print (f'{Correos}')

Texto13_temp = Texto13

for i, email in enumerate(Correos, start=1):
    Texto13_temp = Texto13_temp.replace(email, f'EMAIL{i}')

print (f'{Texto13_temp}')

Texto13_temp2 = re.sub(r'\!|\?|\.{2,}', '', Texto13_temp)

print (f'{Texto13_temp2}')

print (f'-' * 20)

for i, email in enumerate(Correos, start=1):
    Texto13_temp2 = Texto13_temp2.replace(f'EMAIL{i}', email)

print (f'{Texto13_temp2}')

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
    print (f'El experimento termino')

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
    print (f'El experimento termino')

print (f'-' * 20)

def Generadora3():
    for elemento in range(5):
        if (elemento == 0):
            yield f'Number zero'
        elif (elemento == 1):
            yield f'Number one'
        elif (elemento == 2):
            yield f'Number two'
        elif (elemento == 3):
            yield f'Number three'
        elif (elemento == 4):
            yield f'Number four'
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
    print (f'El experimento termino')

print (f'-' * 20)

def Inicial(Lista):
    Menor = min(Lista)
    Mayor = max(Lista)
    Lista_Resultado = list([Menor, Mayor])
    return Lista_Resultado

Lista0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Lista0.append(10)

print (f'El numero menor y el mayor de la lista son {Inicial(Lista0)}')

PEPE.Saludar1()

from Module_Own import Saludar2 as SaludarDos

print (f'Hola {SaludarDos()}')

print (f'Hola nuevamente {PEPE.Saludar3(SaludarDos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int) -> int:
        return Num1 + Num2

    return Sumatoria_Interna(4)

Variable_Sumatoria = Sumatoria_Externa(3)

print (f'El resultado de la sumatoria es {Variable_Sumatoria}')

if (PEPE.Par(Variable_Sumatoria) == True):
    print (f'El numero elegido es par')
else:
    print (f'El numero elegido es impar')

PEPE.Usuario(SaludarDos(), 'MASCULINO')

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

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(33)}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.5, 500, not True)

print (f'{Funcion_Tupla("Perro", 3.5, 500, not True)}')
print (f'{Funcion_Tupla("Perro", 3.5, 500, not True)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.5, 500, not True))}')

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

    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')

Funcion_Diccionario(Nombre = SaludarDos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def SumatoriaDos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{SumatoriaDos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

print (f'Los numeros pares de la lista son {list(Anonima3)} o incluso podrian ser {PEPE.Lista_Par}')

def Primera(Segunda):
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

def Closure_Externa():
    Lista_Closure = []
    def Closure_Interna(x):
        Lista_Closure.append(x)
        return Lista_Closure

    return Closure_Interna

Variable_Closure = Closure_Externa()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(24)}')
print (f'{Variable_Closure(37)}')

def Closure_Crear_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y

    return Closure_Multiplicador

Variable_Mult1 = Closure_Crear_Multiplicador(2)
Variable_Mult2 = Closure_Crear_Multiplicador(3)

print (f'El multiplicador es {Variable_Mult1(10)}')
print (f'El multiplicador es {Variable_Mult2(10)}')

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    if (Any_Impar == True):
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impar = [num for num in Lista if num % 2 != 0]

        print (f'Los numeros impares de la lista son {list(Anonima4)} o incluso seran {Lista_Impar}')
    else:
        print (f'Error, no hay elementos impares en la lista')

Filtrador(PEPE.Lista_Numeros)

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

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 7

    return Tercera

@Primera
def Sumatoria3(Num1, Num2):
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

Usuario2("Erick", "Perez")

from Module_Own import Pokemon2 as Poke2

Objeto26 = Poke2(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto27 = Poke2(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto27.Mostrar()

print (f'Esto muy feliz porque finalmente tengo {Objeto27.Cantidad} pokemones')

if (Objeto27.Catched == True):
    print (f'El pokemon ha sido capturado')
else:
    print (f'El pokemon no fue capturado')

Lista_Azar = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Generador = np.random.choice(Lista_Azar)

Intentos = list([1, 2, 3])

for elemento in Intentos:
    if (elemento == Generador):
        print (f'CATCHA!!!! Felicidades, atrapaste un {Objeto26.Nombre}')
        break
    else:
        print (f'Oh no, {Objeto26.Nombre} se ha escapado')

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto28 = Poke_Kid2(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto28)
Objeto28.Mostrar()

print (f'-' * 20)

class Camara():
    def Tomar_Fotografia(self):
        print (f'Fotografia Tomada')

class Reproductor_Musica:
    def Reproducir_Musica(self):
        print (f'Musica Reproducida')

class Celular(Camara, Reproductor_Musica):
    def Encender_Celular(self):
        print (f'Celular Encendido')

Objeto29 = Celular()

Objeto29.Encender_Celular()
Objeto29.Reproducir_Musica()
Objeto29.Tomar_Fotografia()

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

Objeto30 = Perro2('Chester', 5, 2.5, 'Poddle', 'Asma')

Veterinaria2.Mostrar(Objeto30)
Objeto30.Mostrar()

print (f'-' * 20)

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo

    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente_Activo: {self.Paciente_Activo}')

Objeto31 = Gato2('Messi', 1.5, 1.8, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto31)
Objeto31.Mostrar()

print (f'-' * 20)

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto32 = Pajaro2('Polly', 31, 0.4, 'Cacatua Blanca', 'Si')

Veterinaria2.Mostrar(Objeto32)
Objeto32.Mostrar()

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

Objeto33 = Paladin1(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto33.Mostrar()
Atacante1.Mostrar(Objeto33)
Defensor1.Mostrar(Objeto33)

print (f'-' * 20)

Heredero1 = issubclass(Poke_Kid2, Poke2)

print (f'{Heredero1}')

print (f'{isinstance(Objeto33, Paladin1)}')
print (f'{isinstance(Objeto33, Defensor1)}')
print (f'{isinstance(Objeto33, Atacante1)}')

print (f'-' * 20)

'''name = input(f'Ingrese su nombre: ')
age = int(input(f'Ingrese su edad: '))

def saludar_usuario(nombre, edad):
    return f'Hola {nombre}, tienes {edad} años'

print (f'{saludar_usuario(name, age)}')'''

'''age = input(f'Ingrese su edad: ')

def verificar_edad(edad):
    try:
        numerito = int(edad)
        if (numerito >= 18):
            if (numerito >= 100):
                return f'Edad poco común 👀'
            else:
                return f'Eres mayor de edad'
        else:
            return f'Eres menor de edad'
    except:
        return f'Error necesito que ingreses un numero entero'

print (f'{verificar_edad(age)}')'''

'''number1 = int(input(f'Ingrese el primer numero: '))
number2 = int(input(f'Ingrese el segundo numero: '))
operator = input(f'Que operacion desea realizar?: ')

def calculadora(num1, num2, operador):
    try:
        numerito1 = int(num1)
        numerito2 = int(num2)

        if (operador == '+'):
            Resultado = numerito1 + numerito2
            return Resultado
        elif (operador == '-'):
            Resultado = numerito1 - numerito2
            return Resultado
        elif (operador == '*'):
            Resultado = numerito1 * numerito2
            return Resultado
        elif (operador == '/'):
            try:
                Resultado = round(numerito1 / numerito2, 2)
                return Resultado
            except ZeroDivisionError:
                return f'Error, el divisor no puede ser cero'
        else:
            return f'Error, el operador no coincide'

    except:
        return f'Error, ambos elementos deben ser numeros enteros'

if (isinstance(calculadora(number1, number2, operator), int)):
    print (f'El resultado de la operacion es {calculadora(number1, number2, operator)}')
else:
    print (f'{calculadora(number1, number2, operator)}')'''

numerito = 8

if (isinstance(numerito, int)):
    print (f'El numero es entero')
else:
    print (f'Error, el numero no es entero')

if (isinstance(numerito, (int, float))):
    print (f'El elemento puede ser un numero entero o flotante')
else:
    print (f'Error, no es ninguno de los dos')

numerito2 = 77

if (isinstance(numerito2, int)):
    print (f'Esto es un numero entero')
else:
    print (f'Esto no es un numero entero')

print (f'-' * 20)

numerito3 = 10

if (isinstance(numerito3, float)):
    print (f'Ok aqui tenemos un flotante')
else:
    print (f'La mica no es un flotante')

print (f'-' * 20)

numerito4 = '2.5'

if (isinstance(numerito4, (int, float))):
    print (f'puede ser un numero entero o un flotante')
else:
    print (f'error, esto es otra cosa')

textico1 = False

if (isinstance(textico1, str)):
    print (f'Lo ingresado es una cadena de texto')
else:
    print (f'ERROR ESTO ES OTRA COSA')

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

Objeto34 = D2()

A2.Mostrar(Objeto34)
B2.Mostrar(Objeto34)
C2.Mostrar(Objeto34)
Objeto34.Mostrar()
E2.Mostrar(Objeto34)

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

Objeto35 = Cripto2()
Objeto36 = Tarjeta2()
Objeto37 = Efectivo2()

Objeto35.Pagar()
Objeto36.Pagar()
Objeto37.Pagar()

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
        print (f'Tu saldo a la fecha es de ${self.__Saldo}')

Objeto38 = Cuenta_Bancaria2(100)
Objeto38.Depositar(25)
Objeto38.Mostrar()

print (f'Tu saldo privado es de {Objeto38.Dinero}')

Objeto38.Dinero = '50,000,000'

Objeto38.Mostrar()

print (f'Tu saldo privado es de {Objeto38.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def Necesaria(self):
        pass

class Nueva2(Plantilla2):
    def Mostrar(self):
        print (f'Hola Nueva Dos')

    def Necesaria(self):
        print (f'Esto es la abstraccion')

Objeto39 = Nueva2()
Objeto39.Mostrar()
Objeto39.Necesaria()

print (f'-' * 20)

class Colores():
    def Seleccion(self):
        return f'Amarillo'

class Camisa1:
    def __init__(self):
        self.Ropita = Colores()

    def Mostrar(self):
        print (f'El color de mi camisa es {self.Ropita.Seleccion()}')

Objeto40 = Camisa1()
Objeto40.Mostrar()

print (f'-' * 20)

class Roja():
    def Seleccion(self):
        return f'Roja'

class Amarilla:
    def Seleccion(self):
        return f'Amarilla'

class Negra:
    def Seleccion(self):
        return f'Negra'

class Gris:
    def Seleccion(self):
        return f'Gris'

class Azul:
    def Seleccion(self):
        return f'Azul'

class Camisa2:
    def __init__(self, Ropita):
        self.Ropita = Ropita

    def Mostrar(self):
        print (f'El dia de hoy voy a vestir una camisa {self.Ropita.Seleccion()}')

Paca1 = Roja()
Objeto41 = Camisa2(Paca1)
Objeto41.Mostrar()
Paca2 = Amarilla()
Objeto42 = Camisa2(Paca2)
Objeto42.Mostrar()
Paca3 = Negra()
Objeto43 = Camisa2(Paca3)
Objeto43.Mostrar()
Paca4 = Gris()
Objeto44 = Camisa2(Paca4)
Objeto44.Mostrar()
Paca5 = Azul()
Objeto45 = Camisa2(Paca5)
Objeto45.Mostrar()

print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un
Long
String'''

variable4 = 400
variable5 = PEPE.Division_Flotante
variable6, variable7 = not True, Objeto6.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke3"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Variable_Sumatoria} o talvez {Sumatoria2(1, 2, 3, 4, 5)} pokemones')

del variable5

print (f'melo' in SaludarDos())

print (f'Long' not in variable3)

print (f'Brooke' in PEPE.Tupla_Poke)
print (f'Koala' not in PEPE.Lista2)
print (PEPE.Diccionario_Poke['Poke1'] in PEPE.Set_Conjunto_Poke)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es una declaracion snake case y desempaquetado de variables {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Sumatoria2(1, 2, 3, 4, 5, 6, 7), Variable_Sumatoria)

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Esto es un rango de elementos de la lista 2 {PEPE.Lista2[:2]}')
print (f'Esto es un rango de elementos de la lista 2 {PEPE.Lista2[2:]}')
print (f'Esto es un rango de elementos de la lista 2 {PEPE.Lista2[::2]}')
print (f'Esto es un rango de elementos de la lista 2 {PEPE.Lista2[::3]}')
print (f'Esto es un rango de elementos de la lista 2 {PEPE.Lista2[2:3]}')
print (f'Esto es un rango de elementos de la lista 2 {PEPE.Lista2[0:None]}')
print (f'Esto es un rango de elementos de la lista 2 {PEPE.Lista2[:]}')

print (f'{Lista_Uno[1]} eso que esta ahi es un {PEPE.Lista2[PEPE.Lista2.index("Koala")]}?')

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
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

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

Tupla1 = tuple(('Red', 'Green'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')

print (f'Un unico elemento de la tupla es {Tupla2[2:3]}')

Set_Conjunto1 = {'Pikachu', PEPE.Diccionario_Poke['Poke1'], PEPE.Diccionario_Poke['Poke1'], PEPE.Diccionario_Poke['Poke1'], PEPE.Diccionario_Poke['Poke1']}
Set_Conjunto1.add(PEPE.Diccionario_Poke['Poke3'])

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({1, 2, 3, 4, 5})

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

Set_A4 = {1, 2, 3, 4}
Set_B4 = set({3, 4, 5, 6})

print (f'{Set_A4.union(Set_B4)}')
print (f'{Set_A4 | Set_B4}')

print (f'-' * 20)

print (f'{Set_A4.intersection(Set_B4)}')
print (f'{Set_A4 & Set_B4}')

print (f'-' * 20)

print (f'{Set_A4.difference(Set_B4)}')
print (f'{Set_A4 - Set_B4}')

print (f'-' * 20)

print (f'{Set_B4.difference(Set_A4)}')
print (f'{Set_B4 - Set_A4}')

print (f'-' * 20)

print (f'{Set_A4.symmetric_difference(Set_B4)}')
print (f'{Set_A4 ^ Set_B4}')

'''Set_A4.update(Set_B4)

print (f'{Set_A4}')'''

print (f'-' * 20)

'''Set_A4.intersection_update(Set_B4)

print (f'{Set_A4}')'''

'''Set_A4.difference_update(Set_B4)
print (f'{Set_A4}')'''

'''Set_B4.difference_update(Set_A4)

print (f'{Set_B4}')'''

Set_A4.symmetric_difference_update(Set_B4)

print (f'{Set_A4}')

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')
Set_Conjunto_Menu2 = frozenset({'Caramelo'})
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, PEPE.Lista2[2]})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : variable1,
    'Edad' : Variable_Sumatoria,
    'Votante' : Variable_Funcion_Tupla[3]
}

Diccionario2 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [18 * 2, 20, 6],
    'Votante' : [True, not False, False]
}

Diccionario3 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1["Nombre"]}')
print (f'{Diccionario1.get("Edad")}')

print (f'-' * 20)

Diccionario1['Nombre'] = PEPE.Lista2[2]

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

print (f'-' * 20)

print (f'{Diccionario1.get(1)} no puede votar, ya que solo tiene {Diccionario2["Edad"][2]} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'Azul')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = PEPE.Tupla_Poke[1]

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')

print (f'-' * 20)

Keys1 = [f'Key_{i}' for i in range(len(Lista_Uno_Copia))]

Diccionario4 = dict(zip(Keys1, Lista_Uno_Copia))

for elemento in Diccionario4.items():
    print (f'{elemento[0]} -- {elemento[1]}')

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

for elemento in Diccionario1:
    print (f'{Diccionario1[elemento]}')

print (f'-' * 20)

print (f'{Cargar_Csv1}')

print (f'-' * 20)

Set_Conjunto_Store1 = set(Cargar_Csv1['product'])

print (f'{Set_Conjunto_Store1}')

Keys2 = [f'Key{i}' for i in range(len(Set_Conjunto_Store1))]

print (f'{Keys2}')

Diccionario5 = dict(zip(Keys2, Set_Conjunto_Store1))

print (f'{Diccionario5}')

print (f'-' * 20)

for elemento in Diccionario5.items():
    print (f'{elemento[0]} -- {elemento[1]}')

print (f'-' * 20)

'''
Lee una lista de numeros y devuelve los que son pares y mayores que diez.

[Elementos]
Tengo una lista de numeros
La recorro
Evaluo de estos numeros cuales son pares
De estos numeros resultantes evaluo cuales son mayores a diez
Si cumple las condiciones lo guardo
Devuelvo lo guardado
'''
Lista_Numeros = []
Array_Random4 = np.random.randint(low=1, high=20, size=(10))

for elemento in Array_Random4:
    Lista_Numeros.append(int(elemento))

print (f'{Lista_Numeros}')
print (f'{type(Lista_Numeros)}')

Lista_Numeros_Updated = []
Lista_Numeros_Updated2 = []

for elemento in Lista_Numeros:
    if (elemento % 2 == 0):
        Lista_Numeros_Updated.append(elemento)
    else:
        continue

for elemento in Lista_Numeros_Updated:
    if (elemento > 10):
        Lista_Numeros_Updated2.append(elemento)
    else:
        continue

print (f'{Lista_Numeros}')
print (f'{Lista_Numeros_Updated}')
print (f'{Lista_Numeros_Updated2}')

Texto_Ejercicio1 = 'Este es un texto de ejemplo murcielago'
Texto_Ejercicio1_NoSpace = Texto_Ejercicio1.replace(' ', '')

import re

Pattern11 = r'[aeiou]'

Buscar23 = re.findall(Pattern11, Texto_Ejercicio1_NoSpace)

print (f'{Buscar23}')

ContadorA = 0
ContadorB = 0
ContadorC = 0
ContadorD = 0
ContadorE = 0

for elemento in Buscar23:
    if (elemento == "a"):
        ContadorA+= 1
    elif (elemento == "e"):
        ContadorB+= 1
    elif (elemento == "i"):
        ContadorC+= 1
    elif (elemento == "o"):
        ContadorD+= 1
    else:
        ContadorE+= 1

print (f'La letra A aparece un total de : {ContadorA} veces')
print (f'La letra E aparece un total de : {ContadorB} veces')
print (f'La letra I aparece un total de : {ContadorC} veces')
print (f'La letra O aparece un total de : {ContadorD} veces')
print (f'La letra U aparece un total de : {ContadorE} veces')

'''class Cuenta_Bancaria3():
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
        return f'{self.__Saldo}'

Objeto46 = Cuenta_Bancaria3(800)
Objeto46.Depositar(200)
print (f'{Objeto46.Mostrar()}')

print (f'Tu saldo privado es de {Objeto46.Dinero}')


def Menu():
    while True:
        Ingresado = input(f'Ingrese un numero entre 1 y 4: ')
        try:
            Numero2 = int(Ingresado)
            if (Numero2 >= 5):
                print (f'Error, necesito que ingreses un numero entre 1 y 4')
                break
            else:
                if (Numero2 == 1):
                    print (f'Gracias por la espera, tu saldo actual es de ${Objeto46.Mostrar()}')
                elif (Numero2 == 2):
                    Nuevo_Saldo = int(input(f'Ingrese la cantidad de dinero a depositar: '))
                    Deposito = Objeto46.Dinero + Nuevo_Saldo
                    Objeto46.Dinero = Deposito
                    print (f'Gracias por el deposito, tu saldo nuevo es de ${Objeto46.Mostrar()}')
                elif (Numero2 == 3):
                    Nuevo_Saldo = 300
                    Retiro = Objeto46.Dinero - Nuevo_Saldo
                    Objeto46.Dinero = Retiro
                    print (f'Gracias por el retiro, tu saldo nuevo es de ${Objeto46.Mostrar()}')
                else:
                    print (f'Gracias por usar nuestros servicios, que tengas un lindo dia')
            break
        except ValueError:
            print (f'Error, necesito que ingreses un numero')

    return Numero2

Menu()'''

Nombrecitos = ["Ana", "Carlos", "Luis", "Eva", "Fernanda", "Noe"]

def Ejemplo(Lista, Limite):
    Nombre_Resultado = []

    for elemento in Lista:
        if (elemento.__len__() <= Limite):
            Nombre_Resultado.append(elemento)
        else:
            continue
    return Nombre_Resultado

Resultado = Ejemplo(Nombrecitos, 7)

for elemento in Resultado:
    print (f'{elemento}')

Lista_Numeros2 = [2, 5, 12, 7, 20, 9, 14]

def Ejemplo2(Lista):
    Acumulador = []
    Anonima6 = filter(lambda Num : Num % 2 == 0, Lista)
    for i in Anonima6:
        if (i > 10):
            Acumulador.append(i)

    return Acumulador

print (f'Los numeros pares mayores a 10 son: {Ejemplo2(Lista_Numeros2)}')

Lista_Palabras = ["avion", "casa", "elefante", "uva", "escuela", "sol"]

def Ejemplo3(Lista):
    import re
    Pattern12 = r'^[aeiou]{1}[a-z]+'

    Acumulador = []
    for elemento1 in Lista:
        if (len(elemento1) > 5):
            Acumulador.append(elemento1)
            for elemento in Acumulador:
                Buscar24 = re.findall(Pattern12, elemento)

    return Buscar24

print (f'{Ejemplo3(Lista_Palabras)}')

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20%7

print (f'El resultado de la operacion es {Division_Baja}')
print (f'El resultado de la operacion es {round(PEPE.Division_Flotante, 2)}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'-' * 20)

print (f'El tipo de dato de la variable es {type(variable1)}')
print (f'El tipo de dato de la variable es {type(variable4)}')
print (f'El tipo de dato de la variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de dato de la variable es {type(variable6)}')
print (f'El tipo de dato de la variable es {type(Array_Concatenate)}')
print (f'El tipo de dato de la variable es {type(Lista_Palabras)}')
print (f'El tipo de dato de la variable es {type(Tupla1)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de dato de la variable es {type(Diccionario1)}')
print (f'El tipo de dato de la variable es {type(Funcion_Tupla)}')
print (f'El tipo de dato de la variable es {type(Data_Frame1)}')
print (f'El tipo de dato de la variable es {type(PEPE)}')

print (f'-' * 20)

if (Diccionario3['Ingresos'] > 500):
    if (Diccionario3['Gastos'] < 200):
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200):
        print (f'Ingresos Altos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200):
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] == 500):
    if (Diccionario3['Gastos'] < 200):
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200):
        print (f'Ingresos Minimos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200):
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] < 500):
    if (Diccionario3['Gastos'] < 200):
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200):
        print (f'Ingresos Bajos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200):
        print (f'Ingresos Bajos, Gastos Altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')

variable8 = 'Erick'
variable9 = 36

if (variable8 == 'Josue' and variable9 >= 30):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Al menos una condicion no se cumple')

if (variable8 == 'Josue' or variable9 >= 50):
    print (f'Al menos una condicion se cumple')
else:
    print (f'Ninguna condicion se cumple')

print (f'{variable1.__dir__()}')

print (f'{help(PEPE)}')

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Variable_Sumatoria
        self.Classified = True

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')

Objeto46 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index('Ash')], 'Kanto', Objeto5.Nombre)
Objeto47 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index('Brooke')], 'Alolah', Objeto6.Nombre)
Objeto48 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index('Misty')], 'Paldea', Objeto7.Nombre)

Objeto46.Desplegar()
Objeto47.Desplegar()
Objeto48.Desplegar()

Negativo = -5

print (f'{int(abs(Negativo))}')

Any_Impar = any(num % 2 != 0 for num in PEPE.Lista_Numeros)
Lista_Impar = [num for num in PEPE.Lista_Numeros if num % 2 != 0]
Anonima7 = filter(lambda Num : Num % 2 != 0, PEPE.Lista_Numeros)

print (f'{Any_Impar}')
print (f'{Lista_Impar}')
print (f'{list(Anonima7)}')

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, ingrese una cadena de texto')

Cociente, Residuo = divmod(Objeto5.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

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

print (f'La letra t aparece en la posicion {variable10.lower().find("t")}')
print (f'La letra b aparece en la posicion {variable10.lower().index("b")}')

print (f'la letra {variable10_letra} aparece un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = 'esto es un texto de ejemplo, quiero ver si soy capaz de reparar el texto'

variable11_Lista = variable11.split(' ')

print (f'La cantidad de palabras digitadas son {len(variable11_Lista)}')

for elemento in enumerate(variable11_Lista):
    print (f'{elemento[0]} -- {elemento[1]}')

variable12 = '39'

if (isinstance(variable12, str)):
    print (f'Lo ingresado es texto')
else:
    print (f'Error, esto no es texto')

if (variable12.isalpha()):
    print (f'Lo ingresado es texto')
else:
    print(f'Error, esto no es texto')

variable13 = 500

if (isinstance(variable13, float)):
    print (f'Lo ingresado es decimal')
else:
    print (f'Lo ingresado no es decimal')

variable14 = '500'

if (isinstance(variable14, int)):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero entero')

if (variable14.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Lo ingresado no es un numero entero')

variable15 = 'erick123'

if (variable15.isalnum()):
    print (f'El texto contiene numeros y texto')
else:
    print (f'El texto es incorrecto')

variable15 = ' '

if (variable15.isspace()):
    print (f'Esto es un espacio nada mas')
else:
    print (f'No hay espacios')

variable16 = 'ESTO'

if (variable16.islower()):
    print (f'Esto es minuscula')
else:
    print (f'Esto no es totalmente minuscula')

if (variable16.isupper()):
    print (f'Esto es mayuscula')
else:
    print (f'Esto no es totalmente mayuscula')

variable17 = 6.9

if (isinstance(variable17, (int, float))):
    print (f'Esto es entero o decimal')
else:
    print (f'Error')

print (f'{PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

print (f'-' * 20)

for elemento in Diccionario5:
    print (f'{Diccionario5[elemento]}')

print (f'-' * 20)

for elemento in Diccionario5.keys():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario5.values():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario5.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1

print (f'-' * 20)

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1

print (f'-' * 20)

Lista_Animales = []
Lista_Animales.append(PEPE.Lista2[2])
Lista_Animales.insert(1, 'Jirafa')
Lista_Animales.extend(['Cocodrilo', 'Pez'])

print (f'{Lista_Animales}')

for elemento in Lista_Animales:
    if (elemento == 'Cocodrilo'):
        print (f'Esto es un reptil')
        break
    else:
        Contador+= 1
        continue

print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Animales, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')

print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')

print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')

Lista_Numeros_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Mayor1 = max(Lista_Numeros_Mult)
Menor1 = min(Lista_Numeros_Mult)

print (f'El menor de los numeros es {Menor1} y el mayor es {Mayor1}')

Redondeado = round(14.458795, 2)

print (f'El redondeado es {Redondeado}')

print (f'{bool("")}')
print (f'{bool(None)}')
print (f'{bool(False)}')
print (f'{bool(0)}')
print (f'{bool(not True)}')

Todo_All = all([Lista_Impar, Set_Conjunto_Menu1, Diccionario1, 0])

print (f'{Todo_All}')

Sumatoria4 = sum(Lista_Numeros_Mult)

print (f'El resultado de la sumatoria es {Sumatoria4}')

Uno = str(500)
Dos = int('500')
Tres = float(Uno)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]
Anonima8 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)

print (f'{Any_Iterable}')
print (f'{Lista_Iterable}')
print (f'{list(Anonima8)}')

print (f' - '.join(PEPE.Set_Conjunto_Poke))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

'''def Floating1(Numero):
    return Numero * Sumatoria2(1, 2, 3, 4) + Variable_Sumatoria

print (f'El resultado de la sumatoria es {Floating1(PEPE.Flotante1)}')

Resultado2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado2}')

def Floating3(Elemento):
    if (Elemento.isalpha()):
        print (f'Lo ingresado es un texto')
    elif (Elemento.isnumeric()):
        print (f'Lo ingresado es un numero')
    elif (isinstance(Elemento, float)):
        print (f'Lo ingresado es un flotante')
    else:
        print (f'Error, no identificamos el tipo de valor')

Floating3(PEPE.Flotante3_Limpio)'''

'''def Floating4(Cadena):
    Lista_Cadena = Cadena.split(' ')
    for elemento in Lista_Cadena:
        print (f'{elemento}')

    print (f'La cantidad de palabras digitadas es {len(Lista_Cadena)}')

Floating4(PEPE.Flotante4)'''

'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento}: ')
        Lista.append(Alumno)

    return Lista

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nLa lista de estudiantes es {Colegio(Lista_Alumnos)}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()'''

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese el numero de estudiantes: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del estudiante {elemento}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)

    Lista.sort(key = lambda Num : Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]

    print (f'El estudiante menor de la lista es {Menore} ({Lista[0][1]}) años')
    print (f'El estudiante mayor de la lista es {Mayore} ({Lista[-1][1]}) años')

Colegio(Lista_Alumnos)'''

'''def Ciclo():
    while True:
        Numero = input(f'Ingrese un numero entero')
        try:
            Numerito = int(Numero)
            break
        except:
            print (f'Error, ingrese un numero entero')

    return Numerito

print (f'Gracias, el numero digitado es {Ciclo()}')'''

import pandas as pd
import requests
import io

Ruta_Html3 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html3, headers=headers)

Leer_Html3 = io.StringIO(Response.text)

Cargar_Html3 = pd.read_html(Leer_Html3)

print (f'{Cargar_Html3[4].head()}')

print (f'-' * 20)

import re

Correo1 = 'erick123_catorce*@yahoo.org'

Pattern12 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|org|net)$'

Buscar24 = bool(re.match(Pattern12, Correo1))

if (Buscar24 == True):
    print (f'El correo electronico tiene un formato correcto')
else:
    print (f'Formato de correo incorrecto')

Numero2 = '32'

Buscar25 = bool(re.match(r'(0[0-9]|[12][0-9]|3[01])', Numero2))

if (Buscar25 == True):
    print (f'El numero esta entre 01 y 31')
else:
    print (f'Error, el numero esta fuera de rango')

import pandas as pd
from datetime import datetime

Ruta_Csv5 = 'C:\\Repo\\Store.csv'

Cargar_Csv5 = pd.read_csv(Ruta_Csv5)

print (f'{Cargar_Csv5}')

print (f'-' * 20)

Fecha4 = '2026-04-01'

try:
    Fech4 = datetime.strptime(Fecha4, '%Y-%m-%d').date()
    Fech4_Formateada = pd.to_datetime(Fech4)
    Cargar_Csv5['date'] = pd.to_datetime(Cargar_Csv5['date'])
except ValueError:
    print (f'Error, formato de fecha incorrecto')
    exit()

Cargar_Csv5['FINALITO'] = Cargar_Csv5['quantity'] * Cargar_Csv5['price']

Encontrado4 = Cargar_Csv5[Cargar_Csv5['date'].dt.date == Fech4_Formateada.date()]

if (Encontrado4.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! encontramos ventas')
    Grupo14 = Encontrado4.groupby('product')['quantity'].sum()
    Grupo14_May = Grupo14.idxmax()
    Grupo14_Min = Grupo14.idxmin()
    Grupo14_May_Cant = Grupo14.max()
    Grupo14_Min_Cant = Grupo14.min()

    print (f'En la fecha {Fech4_Formateada} el producto {Grupo14_May} vendio un total de {Grupo14_May_Cant} unidades')
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo14_Min} vendio un total de {Grupo14_Min_Cant} unidades')

    print (f'En esta fecha {Fech4_Formateada} recibimos {Grupo14.count()} clientes')
    print (f'El total de productos que vendimos en esta fecha fue de {Grupo14.sum()} unidades individuales')

    Grupo15 = Encontrado4['FINALITO'].sum()

    print (f'En esta fecha {Fech4_Formateada} vendimos un total de ${Grupo15}')

import re

Texto14 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern13 = r'\d{2}\/[0-9]{2}\/\d{2,}'

Replacement7 = 'XX/XX/XXXX'

Buscar26 = re.sub(Pattern13, Replacement7, Texto14)

print (f'{Buscar26}')

Pattern14 = r'\+\d{1}\-[0-9]{3}\-[0-9]{3}\-\d{2,4}'

Replacement8 = '*-***-***-****'

Buscar27 = re.sub(Pattern14, Replacement8, Buscar26)

print (f'{Buscar27}')

Texto15 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern15 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|org|net)'

Correos1 = re.findall(Pattern15, Texto15)

Texto15_temp = Texto15

for i, email in enumerate(Correos1, start=1):
    Texto15_temp = Texto15_temp.replace(email, f'SAMPLE{i}')

print (f'{Texto15_temp}')

Texto15_temp_Version1 = Texto15_temp.lower()

print (f'{Texto15_temp_Version1}')

Texto15_temp_Version2 = re.sub(r'\!|\?|\.{2,}', '', Texto15_temp_Version1)

print (f'{Texto15_temp_Version2}')

Texto15_temp_Version3 = re.sub(r'\d+', '', Texto15_temp_Version2)

print (f'{Texto15_temp_Version3}')

for i, email in enumerate(Correos1, start=1):
    Texto15_temp_Version2 = Texto15_temp_Version2.replace(f'SAMPLE{i}', email)

print (f'{Texto15_temp_Version2}')

personas = [
    ["Ana", 17, True],
    ["Carlos", 25, True],
    ["Luis", 19, False],
    ["Elena", 30, True],
    ["Mario", 15, False]
]


def Ejemplo3(elemento):
    
    Lista_resultado = []

    for elemento1 in elemento:
        if (elemento1[1] >= 18 and elemento1[2] == True):
            Lista_resultado.append(elemento1[0])
        else:
            continue

    return Lista_resultado

print (f'Las personas que cumplen ambas condiciones son {Ejemplo3(personas)}')