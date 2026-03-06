List1 = list(['Erick', 'Josue', 'Karlita'])

Key1 = [f'Key{i}' for i in range(len(List1))]

print (f'{Key1}')

Dict1 = dict(zip(Key1, List1))

print (f'{Dict1}')

import pandas as pd

Ruta_Csv1 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

Key2 = [f'Key_{i}' for i in range(len(Cargar_Csv1))]

List2 = list(Cargar_Csv1['Nombre'])

print (f'{Key2}')
print (f'{List2}')

Dict2 = dict(zip(Key2, List2))

print (f'{Dict2}')

class Persona:
    def __init__(self, Nombre, Genero, Edad):
        self.Nombre = Nombre
        self.Genero = Genero
        self.Edad = Edad

    def Mostrar(self):
        print (f'{self.Nombre} es de genero {self.Genero} y su edad son {self.Edad} años')

class Trabajador(Persona):
    def __init__(self, Nombre, Genero, Edad, Profesion, Ciudad):
        super().__init__(Nombre, Genero, Edad)
        self.Profesion = Profesion
        self.Cuidad = Ciudad

    def Desplegar(self):
        print (f'{self.Nombre}, tu profesion es {self.Profesion} y vives en {self.Cuidad}')

Objeto1 = Trabajador(Dict2['Key_2'], 'Femenino', 6, 'Estudiante', 'San Jose')

Objeto1.Mostrar()
Objeto1.Desplegar()

print (f'--------------------')

class Camara:
    def tomar_fotos(self):
        print (f'Has tomado una fotografia')

class Reproductor:
    def reproducir_musica(self):
        print (f'Has reproducido la musica')

class SmartPhone(Camara, Reproductor):
    def encender_smartphone(self):
        print (f'El smartphone ha sido encendido')

Objeto2 = SmartPhone()

Objeto2.tomar_fotos()
Objeto2.reproducir_musica()
Objeto2.encender_smartphone()

print (f'--------------------')
'''
import pandas as pd
from datetime import datetime

Ruta_Csv2 = 'C:\\python-data-analyzer\\data\\sales.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

Fecha = input(f'Ingrese una fecha con formato YY-MM-DD: ')

try:
    Formato = datetime.strptime(Fecha, '%Y-%m-%d').date()
    Formato_Correcto = pd.to_datetime(Formato)
    Cargar_Csv2['date'] = pd.to_datetime(Cargar_Csv2['date'])
except ValueError:
    print (f'Formato incorrecto')
    exit()

Encontrado = Cargar_Csv2[Cargar_Csv2['date'].dt.date == Formato_Correcto.date()]

if (Encontrado.empty):
    print (f'No se han encontrado ventas en {Formato_Correcto}')
else:
    print (f'Genial! se han encontado {len(Encontrado)} ventas en esta fecha: {Formato_Correcto}')

'''

import re

Email1 = 'usuario123@empresa.cr'

Pattern1 = r'^[a-zA-Z0-9_+-.#]+@[a-zA-Z0-9]+\.\D{2,}$'

Buscar1 = bool(re.match(Pattern1, Email1))

print (f'{Buscar1}')

Texto1 = "El cliente compró 3 camisas por 25000 colones y 2 pantalones por 40000 colones."

Buscar2 = re.findall(r'\d+', Texto1)

Lista_Buscar2 = []

print (f'{Buscar2}')

for indice, elemento in enumerate(Buscar2, start=1):
    Lista_Buscar2.append(int(elemento))

print (f'{Lista_Buscar2}')
print (f'{type(Lista_Buscar2)}')

print (f'------------')

Texto2 = "Se pagaron ₡25000 por materiales, ₡7800 por transporte y ₡150000 por maquinaria."

Buscar3 = re.findall(r'₡(\d+)', Texto2)
Lista_Buscar3 = list([])

print (f'{Buscar3}')

for elemento in enumerate(Buscar3):
    Lista_Buscar3.append(int(elemento[1]))

print (f'{Lista_Buscar3}')
print (f'{type(Lista_Buscar3)}')

print (f'------------')

phone_number = '8888-8888'

Pattern2 = r'^[0-9]{4}\-\d{4}$'

Buscar4 = bool(re.match(Pattern2, phone_number))

if (Buscar4 == True):
    print (f'Formato correcto')
else:
    print (f'Formato incorrecto')

def Funcion_Correo(Correo):
    Email2 = Correo
    Pattern3 = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.com$'
    Buscar5 = bool(re.match(Pattern3, Email2))

    return Buscar5

if (Funcion_Correo('juan123@gmail.com') == True):
    print (f'Formato de correo electronico correcto')
else:
    print (f'Formato de correo electronico incorrecto')

print (f'------------')

def Funcion_Correo2(Correo):
    Email3 = Correo
    Pattern4 = r'^[a-zA-Z0-9]{1}(\.[a-zA-Z0-9]+)?@[a-zA-Z]+\.com$'
    Buscar6 = bool(re.match(Pattern4, Email3))

    return Buscar6

print (f'{Funcion_Correo2("samp.le@sample.com")}')

import re

Texto3 = 'ESTO ES un eje45mplo cualquiera, $10.00000 pero hola lo que  hela deseo es ver 9 si la mica funciona @14 orrectamente hala'

Buscar7 = re.search(r'\d+', Texto3)
Buscar8 = re.findall(r'\d+', Texto3)
Buscar9 = re.findall(r'\$(\d+)', Texto3)

print (f'{Buscar7}')
print (f'{Buscar8}')
print (f'{Buscar9}')

Buscar10 = re.findall(r'(\.[0-9]+)?', Texto3)

print (f'{Buscar10}')

Buscar11 = re.findall(r'\D+', Texto3)

print (f'{Buscar11}')

Buscar12 = re.findall(r'\w+', Texto3)
Buscar13 = re.findall(r'\W+', Texto3)

print (f'{Buscar12}')

print (f'------------')

print (f'{Buscar13}')

Buscar14 = re.search(r'\s+', Texto3)
Buscar15 = re.findall(r'\S+', Texto3)

print (f'{Buscar14}')
print (f'{Buscar15}')

Buscar16 = re.findall(r'h.la', Texto3)

print (f'{Buscar16}')

Buscar17 = re.findall(r'\d+', Texto3)
Buscar18 = re.findall(r'\d?', Texto3)
Buscar19 = re.findall(r'\d*', Texto3)
Buscar20 = re.findall(r'\d{2}', Texto3)
Buscar21 = re.findall(r'\d{1,}', Texto3)
Buscar22 = re.findall(r'\d{1,2}', Texto3)

print (f'{Buscar17}')
print (f'{Buscar18}')
print (f'{Buscar19}')
print (f'{Buscar20}')
print (f'{Buscar21}')
print (f'{Buscar22}')





