import itertools


class Poke1:
    def __init__(self, Nombre, Tipo, Ataque):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque
        self.Cantidad = 18 * 2
        self.Catched = not True

class Poke1_Hijo(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Desplegar(self):
        print (f'{self.Nombre} es de tipo {self.Tipo} / {self.Sub_Tipo}')

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')

Objeto1 = Poke1_Hijo('Pikachu', 'Electrico', 'Impact Trueno', 'Acero')

Objeto1.Mostrar()
print (f'Yo tengo {Objeto1.Cantidad} {Objeto1.Nombre}s')

Objeto1.Desplegar()

class Camara:
    def Tomar_Foto(self):
        print (f'La fotografia se ha tomado')

class Musica:
    def Reproducir_Musica(self):
        print (f'La musica se ha reproducido')

class Smartphone(Camara, Musica):
    def Encender_Smartphone(self):
        print (f'El smartphone ha sido encendido')

Objeto2 = Smartphone()

Objeto2.Tomar_Foto()
Objeto2.Reproducir_Musica()
Objeto2.Encender_Smartphone()

Lista_Dict1 = ['Erick', 'Josue', 'Karlita']

Key1 = [f'Key{i}' for i in range(len(Lista_Dict1))]

print (f'{Key1}')

Diccionario0 = dict(zip(Key1, Lista_Dict1))

print (f'{Diccionario0}')

print (f'{Diccionario0}')
print (f'{Diccionario0.keys}')
print (f'{Diccionario0["Key0"]}')
print (f'{Diccionario0.get("Key1")}')

print (f'----------')

import pandas as pd

Ruta_Csv1 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

Key2 = [f'Key_{i}' for i in range(len(Cargar_Csv1))]

print (f'{Key2}')

Lista_Dict2 = list(Cargar_Csv1['Nombre'])

print (f'{Lista_Dict2}')

Diccionario00 = dict(zip(Key2, Lista_Dict2))

print (f'{Diccionario00}')
print (f'{Diccionario00.keys()}')
print (f'{Diccionario00["Key_1"]}')
print (f'{Diccionario00.get("Key_2")}')

print (f'----------')

import re

Texto1 = 'este es hola un texto ₡150 pero lo mas interesante! es hala que ₡66 colones no es lo mismo que hela tener ₡0 en el bolsillo'

Buscar1 = re.findall(r'₡(\d+)', Texto1)

print (f'{Buscar1}')

Lista_Buscar1 = list([])

for elemento in Buscar1:
    Lista_Buscar1.append(int(elemento))

print (f'{Lista_Buscar1}')

Telefono1 = '8888-8888'

Buscar2 = bool(re.match(r'[0-9]{4}\-\d{4}', Telefono1))

if (Buscar2 == True):
    print (f'El formato del numero de telefono es correcto')
else:
    print (f'Error, formato incorrecto')

Texto2 = 'Tu tarjeta caduca en 03/10/2026, es necesario que visites una sucursal antes de esta fecha'

Pattern1 = r'\d{2}\/[0-9]{2}\/\d{4}'

Hidden_Phone = 'XX/XX/XXXX'

Buscar3 = re.sub(Pattern1, Hidden_Phone, Texto2)

print (f'{Buscar3}')

Email1 = 'sample@sample.com'

Pattern2 = r'^[a-zA-Z0-9./*-+?_-]+\@[a-zA-Z]+\.[a-z]{2,}$'

Buscar4 = bool(re.match(Pattern2, Email1))

if (Buscar4 == True):
    print (f'El formato del correo es correcto')
else:
    print (f'El formato del correo es incorrecto')

print (f'----------')

Texto3 = 'este es hola un texto ₡150 pero lo mas interesante! es hala que ₡66 colones no es lo mismo que hela tener ₡0 en el bolsillo'

Buscar5 = re.search(r'\d+', Texto3)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\d+', Texto3)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\D+', Texto3)

print (f'{Buscar7}')

Buscar8 = re.findall(r'\w+', Texto3)

print (f'{Buscar8}')

Buscar9 = re.findall(r'\W+', Texto3)

print (f'{Buscar9}')

Buscar10 = re.findall(r'\s+', Texto3)

print (f'{Buscar10}')

Buscar11 = re.findall(r'[\S+]', Texto3)

print (f'{Buscar11}')

Buscar12 = re.findall(r'h.la', Texto3)

print (f'{Buscar12}')

Buscar13 = re.findall(r'hol[a]{3}', 'holaaa')

print (f'{Buscar13}')

Buscar14 = re.findall(r'hol[a]{4,}', 'holaaa')

print (f'{Buscar14}')

Buscar15 = re.findall(r'hol[a]{3,6}', 'holaaaa')

print (f'{Buscar15}')

Buscar16 = re.fullmatch(r'hol[a]*', 'hol')

print (f'{Buscar16}')

Buscar17 = re.fullmatch(r'hol[a]+', 'hol')

print (f'{Buscar17}')

Buscar18 = re.fullmatch(r'hol[a]?', 'hol')

print (f'{Buscar18}')

Buscar19 = re.findall(r'[abl]{3}', 'hablablr')

print (f'{Buscar19}')

Texto4 = 'este es hola un texto ₡150 pero lo mas interesante! es hala que ₡66 colones no es lo mismo colonescolones que hela tener ₡0 en el bolsillo'

Buscar20 = re.findall(r'(colones){2,}', Texto4)

print (f'{Buscar20}')

import re

Ruta_Csv2 = 'C:\\python-data-analyzer\\data\\sales.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

Elemento1 = Cargar_Csv2.groupby('product')['quantity'].sum()
Elemento1_Mayor = Elemento1.idxmax()
Elemento1_Menor = Elemento1.idxmin()

Cantidad_Mayor = Elemento1.max()
Cantidad_Menor = Elemento1.min()

print (f'El producto que vendio mas fue {Elemento1_Mayor} y vendio {Cantidad_Mayor} productos')
print (f'El producto que vendio menos fue {Elemento1_Menor} y vendio {Cantidad_Menor} productos')

print (f'{Elemento1}')

import pandas as pd
from datetime import datetime

'''Fecha = input(f'Ingrese una fecha con formato YY-MM-DD: ')

try:
    Fech = datetime.strptime(Fecha, '%Y-%m-%d').date()
    Fech_Formateado = pd.to_datetime(Fech)
    Cargar_Csv2['date'] = pd.to_datetime(Cargar_Csv2['date'])
except ValueError:
    print (f'Error, formato incorrecto')
    exit()

Encontrado = Cargar_Csv2[Cargar_Csv2['date'].dt.date == Fech_Formateado.date()]

if (Encontrado.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    Elemento2 = Cargar_Csv2.groupby('product')['quantity'].sum()
    Elemento2_1 = Elemento2.max()
    Elemento2_1_1 = Elemento2.idxmax()
    print (f'GENIAL! El producto que vendio mas fue {Elemento2_1_1} con {Elemento2_1} unidades')

    Elemento2_2 = Elemento2.min()
    Elemento2_2_1 = Elemento2.idxmin()
    print (f'GENIAL! El producto que vendio menos fue {Elemento2_2_1} con {Elemento2_2} unidades')
    
'''

Cargar_Csv2['TOTALE'] = Cargar_Csv2['quantity'] * Cargar_Csv2['price']

print (f'{Cargar_Csv2}')

def Exception1(Numero):
    try:
        Numerito = int(Numero)
        print (f'Gracias, tu numero es {Numerito}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Exception1(9)

def Exception2(Num1, Num2):
    try:
        Resultado = Num2 + Num1
        print (f'El resutlado de la operacion es {Resultado}')
    except TypeError:
        print (f'Error, ambos elementos deben ser numeros')

Exception2(12, "hola")

def Exception3(Num1, Num2):
    try:
        Div = Num1 / Num2
        print (f'El resultado de la division es {round(Div, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(12, 0)

Lista_Exception4 = ['Erick', 'Josue', 'Karlita']

def Exception5(Indice):
    try:
        print (f'El elemento en la posicion {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, indice fuera de rango')

Exception5(2)

Diccionario_Exception5 = dict({'Nombre' : "Josue", 'Edad' : 20})

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception5('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Leon')
        Docu.close()

except FilenotFoundError:
    print (f'Error, el archivo no fue encontrado')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

