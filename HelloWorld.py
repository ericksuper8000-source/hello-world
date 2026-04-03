import itertools

try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado es incorrecto')

import pandas as pd
from datetime import datetime

Ruta_Csv1 = 'C:\\python-data-analyzer\\data\\sales.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

Fecha = '2025-01-04'

try:
    Fech = datetime.strptime(Fecha, '%Y-%m-%d').date()
    Fech_Formateada = pd.to_datetime(Fech)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Error, formato incorrecto')
    exit()

Buscador = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech_Formateada.date()]

if (Buscador.empty):
    print (f'No hay ventas registradas en esta fecha')
else:
    Ventica = Buscador.groupby('product')['quantity'].sum()
    Ventica_Total = Ventica.count()
    Ventica_Prod_May = Ventica.idxmax()
    Ventica_Prod_Min = Ventica.idxmin()
    Ventica_Prod_May_Cant = Ventica.max()
    Ventica_Prod_Min_Cant = Ventica.min()
    Total_Vendido = Buscador.groupby('product')['price'].sum()
    Total_Vendido_May_Precio = Total_Vendido.max()
    Total_Vendido_Min_Precio = Total_Vendido.min()
    Totale = Total_Vendido_May_Precio + Total_Vendido_Min_Precio

    print (f'Se registraron un total de {Ventica_Total} ventas individuales durante {Fech_Formateada}')
    print (f'La cantidad de productos ventidos en estas {Ventica_Total} ventas fue de {Ventica_Prod_May_Cant + Ventica_Prod_Min_Cant} unidades')
    print (f'El producto que vendio mas durante esta fecha fue {Ventica_Prod_May} con un total de {Ventica_Prod_May_Cant} unidades')
    print (f'El producto que vendio menos durante esta fecha fue {Ventica_Prod_Min} con un total de {Ventica_Prod_Min_Cant} unidades')
    print (f'En {Fech_Formateada} se vendio un total de ${Totale}')

print (f'-' * 20)

from Module_Own import Pokemon as Poke

Objeto1 = Poke(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto2 = Poke(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto2.Mostrar()

print (f'-' * 20)

class Poke_Hija(Poke):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto3 = Poke_Hija(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke.Mostrar(Objeto3)
Objeto3.Mostrar()

print (f'-' * 20)

class Camara():
    def Tomar_Fotografia(self):
        print (f'Fotografia Tomada')

class Reproductor_Musica():
    def Reproducir_Musica(self):
        print (f'Musica Reproducida')

class SmartPhone(Camara, Reproductor_Musica):
    def Encender_Smartphone(self):
        print (f'Smartphone Encendido')

Objeto4 = SmartPhone()

Objeto4.Encender_Smartphone()
Objeto4.Reproducir_Musica()
Objeto4.Tomar_Fotografia()

print (f'-' * 20)

class Atacante():
    def __init__(self, Damage, Weapon, Position):
        self.Damage = Damage
        self.Weapon = Weapon
        self.Position = Position

    def Mostrar(self):
        print (f'Damage: {self.Damage}pts')
        print (f'Weapon: {self.Weapon}')
        print (f'Position: {self.Position}')


class Defensor:
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life

    def Mostrar(self):
        print(f'Healing: {self.Healing}pts')
        print(f'Potion: {self.Potion}')
        print(f'Life: {self.Life}pts')

class Paladin(Atacante, Defensor):
    def __init__(self, Damage, Weapon, Position, Healing, Potion, Life, Name):
        Atacante.__init__(self, Damage, Weapon, Position)
        Defensor.__init__(self, Healing, Potion, Life)
        self.Name = Name

    def Mostrar(self):
        print (f'Name: {self.Name}')

Objeto5 = Paladin(75, 'Battle Axe', 'Right', 25, 'Black Potion', 200, 'Ghost Knight')

Objeto5.Mostrar()
Atacante.Mostrar(Objeto5)
Defensor.Mostrar(Objeto5)

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
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento, Visitas):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        self.Visitas = Visitas

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        print (f'Visitas: {self.Visitas}')

Objeto6 = Perro('Chester', 4, 2.7, 'Poodle', 'Asma', 2)

Mascota.Mostrar(Objeto6)
Objeto6.Mostrar()

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

Objeto7 = Gato('Messi', 1.5, 1.8, 'Siames', 'Gris', 'Si')

Mascota.Mostrar(Objeto7)
Objeto7.Mostrar()

print (f'-' * 20)

class Pajaro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto8 = Pajaro('Polly', 31, 0.5, 'Lora Verde', 'Si')

Mascota.Mostrar(Objeto8)
Objeto8.Mostrar()

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

Objeto9 = D()

A.Mostrar(Objeto9)
B.Mostrar(Objeto9)
C.Mostrar(Objeto9)
Objeto9.Mostrar()
E.Mostrar(Objeto9)

print (f'-' * 20)

Lista_Dict1 = ['Erick', 'Josue', 'Perez', 'Gutierrez']
Key1 = [f'Key{i}' for i in range(len(Lista_Dict1))]

Diccionario1 = dict(zip(Key1, Lista_Dict1))

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1["Key2"]}')
print (f'{Diccionario1.get("Key3")}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv2 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

Lista_Dict2 = list(Cargar_Csv2['Nombre'])
Key2 = [f'Key_{i}' for i in range(Lista_Dict2.__len__())]

Diccionario2 = dict(zip(Key2, Lista_Dict2))

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2["Key_0"]}')
print (f'{Diccionario2.get("Key_1")}')

print (f'-' * 20)

import re

Texto1 = 'este es hola un texto ₡150 pero lo mas interesante! es hala que ₡66 colones no es lo mismo que hela tener ₡0 en el bolsillo'

Buscar1 = re.findall(r'₡(\d+)', Texto1)
Lista_Buscar1 = list([])

for elemento in Buscar1:
    Lista_Buscar1.append(int(elemento))

print (f'{Lista_Buscar1}')

Telefono1 = '8888-8888'

Pattern1 = r'^[0-9]{4}\-(\d){4}$'

Buscar2 = bool(re.match(Pattern1, Telefono1))

if (Buscar2 == True):
    print (f'Formato de telefono correcto')
else:
    print (f'Formato de telefono incorrecto')

Texto2 = 'Tu tarjeta caduca en 03/10/2026, es necesario que visites una sucursal antes de esta fecha'

Pattern2 = r'\d{2}\/[0-9]{2}\/[0-9]{4}'

Reemplazar = 'XX/XX/XXXX'

Buscar3 = re.sub(Pattern2, Reemplazar, Texto2)

print (f'{Buscar3}')

print (f'-' * 20)

Email1 = 'sample@sample.com'

Pattern3 = r'^[a-zA-Z0-9-+*/-?]+\@[a-z]+\.[a-z]{2,}$'

Buscar4 = bool(re.match(Pattern3, Email1))

if (Buscar4 == True):
    print (f'El correo tiene el formato correcto')
else:
    print (f'Error, formato incorrecto')

Buscar5 = re.search(r'\d+', Texto1)

print (f'{Buscar5}')

Buscar6 = re.findall(r'[0-9]+', Texto1)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\w', Texto1) # Todo lo que no sea caracteres especiales
Buscar8 = re.findall(r'\W', Texto1) # Caracteres especiales nada mas
Buscar9 = re.findall(r'\s', Texto1) # Solo espacios
Buscar10 = re.findall(r'\S', Texto1) # Sin espacios

print (f'{Buscar7}')

print (f'-' * 20)

print (f'{Buscar8}')

print (f'-' * 20)

print (f'{Buscar9}')

print (f'-' * 20)

print (f'{Buscar10}')

print (f'-' * 20)

Buscar11 = re.findall(r'h.la', Texto1)

print (f'{Buscar11}')

Buscar12 = re.search(r'hola', Texto1)

print (f'{Buscar12}')

Buscar13 = re.findall(r'(la)+', Texto1)

print (f'{Buscar13}')

Buscar14 = re.fullmatch('Tu tarjeta caduca en 03/10/2026, es necesario que visites una sucursal antes de esta fecha', Texto2)

print (f'{Buscar14}')

Buscar15 = re.findall(r'^Tu', Texto2)
Buscar16 = re.findall(r'cha$', Texto2)

print (f'{Buscar15}')
print (f'{Buscar16}')

Buscar17 = re.findall(r'hila|\d+', Texto1)

print (f'{Buscar17}')

def Exception1(Elemento):
    try:
        Num = int(Elemento)
        print (f'Gracias, tu numero ingresado es {Num}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero')

Exception1("Hola")

def Exception2(Num1, Num2):
    try:
        Suma = Num1 + Num2
        print (f'El resultado de la suma es {Suma}')
    except TypeError:
        print (f'Error necesito que ambos elementos sean numeros')

Exception2(12, "hola")

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(12, 0)

Lista_Exception4 = list(['Erick', 'Josue', 'Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento en el indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, El indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El elemento con la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception5("Votante")

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Durazno')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')

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
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Set_Conjunto_Poke)])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

import pandas as pd

Data_Frame1 = pd.DataFrame({
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 18, 6],
    'Votante' : [True, not False, False]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [55, 14, 26],
    'Votante' : [True, False, not False]
})

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame1}')

print (f'-' * 30)

print (f'{Data_Frame_Concatenate_Age}')

print (f'-' * 30)

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()} y la mayor de las edades es {Data_Frame_Concatenate_Age.max()}')

print (f'-' * 30)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 30)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombrecito = elemento['Nombre']

    print (f'Mi nombre es {Nombrecito}')

print (f'-' * 30)

Grupo1 = Cargar_Csv2.groupby('Nombre')['Edad'].sum()
Grupo1_Max = Grupo1.idxmax()
Grupo1_Min = Grupo1.idxmin()

print (f'El menor es {Grupo1_Min} y el mayor es {Grupo1_Max}')
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Cargar_Csv2)

plt.show()

print (f'-' * 30)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Cargar_Csv2)

plt.show()

print (f'-' * 30)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Cargar_Csv2)

plt.show()

print (f'-' * 30)'''

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'-' * 30)

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'-' * 30)

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'-' * 30)

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'Filas: {Filas}')
print (f'Columnas: {Columnas}')

Elemento1 = Data_Frame1.loc[0, 'Nombre']
Elemento2 = Data_Frame1.loc[0, 'Edad']
Elemento3 = Data_Frame1.loc[0, 'Votante']
Elemento4 = Data_Frame1.loc[0, :]
Elemento5 = Data_Frame1.loc[:, 'Edad']

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')
print (f'-' * 30)
print (f'{Elemento4}')
print (f'-' * 30)
print (f'{Elemento5}')

print (f'-' * 30)

Elemento6 = Data_Frame2.iloc[0, 0]
Elemento7 = Data_Frame2.iloc[1, 1]
Elemento8 = Data_Frame2.iloc[2, 2]
Elemento9 = Data_Frame2.iloc[0, :]
Elemento10 = Data_Frame2.iloc[:, 2]

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')
print (f'-' * 30)
print (f'{Elemento9}')
print (f'-' * 30)
print (f'{Elemento10}')

print (f'-' * 30)

import pandas as pd

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel)

print (f'{Cargar_Excel.head()}')

print (f'-' * 30)

Cargar_Excel1 = pd.read_excel(Ruta_Excel, sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, index_col='cabina')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:J', index_col='cabina')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, sheet_name=0, header=0, usecols='E:J', index_col='cabina', nrows=1)

print (f'{Cargar_Excel1.head()}')

print (f'-' * 30)

print (f'{Cargar_Excel2.head()}')

print (f'-' * 30)

print (f'{Cargar_Excel3.head()}')

print (f'-' * 30)

print (f'{Cargar_Excel4.head()}')

print (f'-' * 30)

print (f'{Cargar_Excel5.head()}')

print (f'-' * 30)

print (f'{Cargar_Excel6.head()}')

print (f'-' * 30)

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'-' * 30)

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

print (f'-' * 30)

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'-' * 30)

print (f'{Cargar_Txt.head()}')

print (f'-' * 30)

import pandas as pd

Ruta_Csv3 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3.head()}')

print (f'-' * 30)

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Leer_Html)

print (f'{Cargar_Html[2].head()}')

print (f'-' * 30)

import numpy as np

Array1 = np.array([1, 2, 3])

print (f'{Array1}')
print (f'{Array1.ndim}') # 1
print (f'{Array1.shape}') # 1x3
print (f'{Array1.size}') # 3
print (f'{Array1.dtype}') # int64
print (f'{Array1[1]}')

print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[2:3]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 <= 2]}')

print (f'-' * 30)

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 0]}')

print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[0, 2:3]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[1, 0:None])
Sumita4 = np.sum(Array2_Sorted[1, :])

print (f'{Array2_Sorted}')
print (f'{round(Array2_Sorted_Mean, 2)}')
print (f'{Array2_Sorted_Sum}')

print (f'-' * 30)

print (f'Resultado de la sumita {Sumita1}')
print (f'Resultado de la sumita {Sumita2}')
print (f'Resultado de la sumita {Sumita3}')
print (f'Resultado de la sumita {Sumita4}')

print (f'-' * 30)

Array3 = np.array([[['e', 'r', 'n'], ['f', 'a', 'x']],       [['i', 'k', 'j'], ['m', 'l', 'd']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 2]}')

print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[1, :, 0]}')
print (f'{Array3[1, 0, 1:2]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "a"]}')

print (f'-' * 30)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],       [[[6, 5, 4], [9, 8, 7]], [[4, 9, 2], [7, 3, 1]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 2]}')

print (f'{Array4[1, 0, 0, :2]}')
print (f'{Array4[1, 0, 0, 2:]}')
print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[0, 1, 0, ::3]}')
print (f'{Array4[1, 0, :, 1]}')
print (f'{Array4[1, 1, 0, 1:2]}')
print (f'{Array4[0, 0, 1, 0:None]}')
print (f'{Array4[0, 0, 1, :]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'{Array2_Sorted}')
print (f'{round(Array4_Sorted_Mean, 2)}')
print (f'{Array4_Sorted_Sum}')

print (f'-' * 30)

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[0, 1, 1, 0:None])
Sumita8 = np.sum(Array4_Sorted[0, 1, 1, :])

print (f'Resultado de la sumita: {Sumita5}')
print (f'Resultado de la sumita: {Sumita6}')
print (f'Resultado de la sumita: {Sumita7}')
print (f'Resultado de la sumita: {Sumita8}')

print (f'-' * 30)

Array_Num1 = np.arange(start=1, stop=11, step=1)

print (f'{Array_Num1}')

Array_Num1_May = np.max(Array_Num1)
Array_Num1_Min = np.min(Array_Num1)

print (f'El menor de los numeros es {Array_Num1_Min} y el mayor es {Array_Num1_May}')

print (f'-' * 30)

Array_Num2 = np.arange(25)

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

Array_Num2_Reshape_Column_Max = np.max(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Column_Min = np.min(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Row_Max = np.max(Array_Num2_Reshape, axis=1)
Array_Num2_Reshape_Row_Min = np.min(Array_Num2_Reshape, axis=1)

print (f'Los menores de las columnas son {Array_Num2_Reshape_Column_Min}')
print (f'Los mayores de las columnas son {Array_Num2_Reshape_Column_Max}')
print (f'Los menores de las filas son {Array_Num2_Reshape_Row_Min}')
print (f'Los mayores de las filas son {Array_Num2_Reshape_Row_Max}')

print (f'-' * 30)

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 1]}')

print (f'-' * 30)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 0]}')

print (f'-' * 30)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 1]}')

print (f'-' * 30)

Array_Gen2 = np.full(shape=(5), fill_value = 'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[2]}')

Lista_Array1 = list([])

for indice, elemento in enumerate(Array_Gen2):
    Lista_Array1.append(str(elemento))

print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 30)

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[0, 1, 1, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[0, 0]}')

print (f'-' * 30)

Tupla_Array = tuple(('Rojo', 'Verde'))
Set_Conjunto_Array = {1, 2, 3}
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array['Nombre'][1])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'-' * 30)

print (f'{Array_Gen6[2]}')

print (f'-' * 30)

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

print (f'-' * 30)

Array_Random1 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random1}')
print (f'{Array_Random1.ndim}')
print (f'{Array_Random1.shape}')
print (f'{Array_Random1.size}')
print (f'{Array_Random1.dtype}')
print (f'{Array_Random1[1, 2]}')

Array_Random1_Sorted = np.sort(Array_Random1)
Array_Random1_Sorted_Mean = np.mean(Array_Random1_Sorted)
Array_Random1_Sorted_Sum = np.sum(Array_Random1_Sorted)

print (f'{Array_Random1_Sorted}')
print (f'{round(Array_Random1_Sorted_Mean, 2)}')
print (f'{Array_Random1_Sorted_Sum}')

Sumita9 = np.sum(Array_Random1_Sorted, axis=0)
Sumita10 = np.sum(Array_Random1_Sorted, axis=1)
Sumita11 = np.sum(Array_Random1_Sorted[1, 0:None])
Sumita12 = np.sum(Array_Random1_Sorted[1, :])

print (f'{Sumita9}')
print (f'{Sumita10}')
print (f'{Sumita11}')
print (f'{Sumita12}')

print (f'-' * 30)

Arr1 = np.array([8, 9, 41])
Arr2 = np.array([2, 3, 7])

Suma = Arr1 + Arr2
Resta = Arr1 - Arr2
Multiplicacion = Arr1 * Arr2
Division = Arr1 / Arr2
Division2 = Arr1 // Arr2

Array_Random2 = np.random.randint(low=1, high=10, size=(10))

Array_Random2_Cien = Array_Random2 + 100

print (f'Resultado de la operacion {Suma}')
print (f'Resultado de la operacion {Resta}')
print (f'Resultado de la operacion {Multiplicacion}')
print (f'Resultado de la operacion {Division}')
print (f'Resultado de la operacion {Division2}')
print (f'Resultado de la operacion {Array_Random2_Cien}')

print (f'-' * 30)

Array_Random3 = np.random.randint(low=1, high=10, size=(20))

print (f'{Array_Random3}')

Array_Random3_Reshape = np.reshape(Array_Random3, shape=(4, 5))

print (f'{Array_Random3_Reshape}')

Array_Random3_Reshape_Ravel = np.ravel(Array_Random3_Reshape)

print (f'{Array_Random3_Reshape_Ravel}')

print (f'-' * 30)

Lista_Array2 = ['Erick', 'Josue', 'Perez', 'Gutierrez']

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-' * 30)

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concatenate([Array6, Array7])

print (f'{Array_Concatenate}')

Array_Concatenate_Split = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Split[0]}')
print (f'{Array_Concatenate_Split[1]}')
print (f'{Array_Concatenate_Split[2]}')

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'-' * 30)

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-' * 30)

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'-' * 30)

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
                print (f'{Fila}')

print (f'-' * 30)

Array_Random4 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random4}')

Array_Random4_Column_Min = np.min(Array_Random4, axis=0)
Array_Random4_Column_Max = np.max(Array_Random4, axis=0)
Array_Random4_Row_Min = np.min(Array_Random4, axis=1)
Array_Random4_Row_Max = np.max(Array_Random4, axis=1)

print (f'Los menores de las columnas: {Array_Random4_Column_Min}')
print (f'Los mayores de las columnas: {Array_Random4_Column_Max}')
print (f'Los menores de las filas: {Array_Random4_Row_Min}')
print (f'Los mayores de las filas: {Array_Random4_Row_Max}')

print (f'-' * 30)

Sorteo = list(['Erick', 'Josue', 'Karlita', 'Carmelo', 'Susanita', 'Roxana'])

Ganador1 = np.random.choice(Sorteo, size=(1), replace=False)
Ganador2 = np.random.choice(Sorteo, size=(2), replace=False)
Ganador3 = np.random.choice(Sorteo, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-' * 30)

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-' * 30)

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
    print (f'Termina Experimento')

print (f'-' * 30)

def Generadora2():
    for elemento in range(5):
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
    print (f'Termina Experimento')

print (f'-' * 30)
print (f'-' * 30)
print (f'-' * 30)

def Generadora3():
    for elemento in range(0, 5):
        if (elemento == 0):
            yield f'ZERO'
        elif (elemento == 1):
            yield f'ONE'
        elif (elemento == 2):
            yield f'TWO'
        elif (elemento == 3):
            yield f'THREE'
        elif (elemento == 4):
            yield f'FOUR'
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
    print (f'Termina Experimento')

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

PEPE.Usuario(Saludar_Dos(), 'FEMENINO')

def Usuario_Externa():
    def Usuario_Interna(Sexo):
        Genero = Sexo.lower()
        if (Genero == 'masculino'):
            return True
        else:
            return False

    return Usuario_Interna('MASCULINO')

Variable_Usuario = Usuario_Externa()

if (Variable_Usuario == True):
    print (f'YOU ARE A MAN')
else:
    print (f'YOU ARE A WOMAN')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(77)}')
        Docu.close()
except FileNotFoundError:
    print (f'Archivo no encontrado')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

print (f'-' * 20)

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.6, 200, not False)

print (f'{Funcion_Tupla("Perro", 3.6, 200, not False)}')
print (f'{Funcion_Tupla("Perro", 3.6, 200, not False)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.6, 200, not False))}')

print (f'-' * 20)

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')

Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre} tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')
print (f'Los numeros pares de la lista son {PEPE.Lista_Par} o incluso podrian ser {list(Anonima3)}')

def Primera(Segunda):
    def Tercera(*args):
        return Segunda(*args) - 42

    return Tercera

@Primera
def Operacion(Numero:int) -> int:
    Local = Numero
    return PEPE.Global + Local

print (f'El resultado de la operacion es {Operacion(12)}')

def Externa(Nombre):
    def Interna(Apellido):
        print (f'El nombre es {Nombre} {Apellido}')

    return Interna("PEREZ GUTIERREZ")

Externa("ERICK JOSUE")

def Closure_Externo():
    Lista_Closure = []
    def Closure_Interno(x):
        Lista_Closure.append(x)

        return Lista_Closure

    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(25)}')
print (f'{Variable_Closure(37)}')

def Crear_Multiplicador(x):
    def Multiplicador(y):
        return x * y

    return Multiplicador

Mult1 = Crear_Multiplicador(2)
Mult2 = Crear_Multiplicador(3)

print (f'Mult {Mult1(10)}')
print (f'Mult {Mult2(10)}')

print (f'-' * 20)

def Filtrador(Lista):
    any_impar = any(num % 2 != 0 for num in Lista)
    if (any_impar == True):
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impar = [num for num in Lista if num % 2 != 0]

        print (f'Los numeros impares de la lista son {list(Anonima4)} o incluso podrian ser {Lista_Impar}')
    else:
        print (f'No hay numeros impares en la lista')

Filtrador(PEPE.Lista_Numeros)

print (f'-' * 20)

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
        return Segunda(*args, **kwargs) - 11

    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(4, 7)}')

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

print (f'-' * 20)

from Module_Own import Pokemon2 as Poke2

class Poke_Hija2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto10 = Poke_Hija2(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno', 'Acero')

Poke2.Mostrar(Objeto10)
Objeto10.Mostrar()

print (f'-' * 20)

class Camara2():
    def Tomar_Foto(self):
        print (f'Foto Tomada')

class Reproductor2:
    def Repro_Musica(self):
        print (f'Musica Reproducida')

class Phone2(Camara2, Reproductor2):
    def Endender_Phone(self):
        print (f'Telefono Encendido')

Objeto11 = Phone2()

Objeto11.Endender_Phone()
Objeto11.Repro_Musica()
Objeto11.Tomar_Foto()

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
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento, Visitas):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        self.Visitas = Visitas

    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        print (f'Visitas: {self.Visitas}')

Objeto12 = Perro('Chester', 3.5, 5, 'Poodle', 'Asma', 3)

Mascota.Mostrar(Objeto12)
Objeto12.Mostrar()

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

Objeto13 = Gato('Messi', 1.5, 2, 'Siames', 'Gris', 'No')

Mascota.Mostrar(Objeto13)
Objeto13.Mostrar()

print (f'-' * 20)

class Pajaro(Mascota):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')

Objeto14 = Pajaro('Polly', 31, 0.4, 'Cacatua Amarilla', 'Si')

Mascota.Mostrar(Objeto14)
Objeto14.Mostrar()

print (f'-' * 20)

class Atacante():
    def __init__(self, Damage, Weapon, Position):
        self.Damage = Damage
        self.Weapon = Weapon
        self.Position = Position

    def Mostrar(self):
        print (f'Damage: {self.Damage}')
        print (f'Weapon: {self.Weapon}')
        print (f'Position: {self.Position}')

class Defensor:
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life

    def Mostrar(self):
        print (f'Healing: {self.Healing}')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}')

class Paladin(Atacante, Defensor):
    def __init__(self, Damage, Weapon, Position, Healing, Potion, Life, Name):
        Atacante.__init__(self, Damage, Weapon, Position)
        Defensor.__init__(self, Healing, Potion, Life)
        self.Name = Name

    def Mostrar(self):
        print (f'Name: {self.Name}')

Objeto15 = Paladin(75, 'Battle Axe', 'Right', 25, 'Toad Liquid', 200, 'Ghost Knight')

Objeto15.Mostrar()
Atacante.Mostrar(Objeto15)
Defensor.Mostrar(Objeto15)

print (f'-' * 20)

Child_Parent = issubclass(Poke_Hija2, Poke2)

print (f'{Child_Parent}')

Child_Parent2 = issubclass(Poke_Hija2, Poke)

print (f'{Child_Parent2}')

Object_Class = isinstance(Objeto15, Atacante)
Object_Class2 = isinstance(Objeto15, Defensor)
Object_Class3 = isinstance(Objeto15, Paladin)

print (f'{Object_Class}')
print (f'{Object_Class2}')
print (f'{Object_Class3}')

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

Objeto16 = D()

A.Mostrar(Objeto16)
B.Mostrar(Objeto16)
C.Mostrar(Objeto16)
Objeto16.Mostrar()
E.Mostrar(Objeto16)

print (f'-' * 20)

class Tarjeta():
    def Pagar(self):
        print (f'El pago se realizo con tarjeta')

class Efectivo:
    def Pagar(self):
        print (f'El pago se realizo con Efectivo')

class Cripto:
    def Pagar(self):
        print (f'El pago se realizo con Cripto')

Objeto17 = Cripto()
Objeto18 = Efectivo()
Objeto19 = Tarjeta()

Objeto17.Pagar()
Objeto18.Pagar()
Objeto19.Pagar()

print (f'-' * 20)

class Cuenta_Bancaria:
    def __init__(self, Saldo):
        self.__Saldo = Saldo

    def Depositar(self, Dinero):
        self.__Saldo += Dinero

    @property
    def Saldo(self):
        return self.__Saldo

    @Saldo.setter
    def Saldo(self, Nuevo_Saldo):
        self.__Saldo = Nuevo_Saldo

    def Mostrar(self):
        print (f'Su saldo a la fecha es de ${self.__Saldo}')

Objeto20 = Cuenta_Bancaria(100)
Objeto20.Depositar(25)
Objeto20.Mostrar()

print (f'El saldo privado es {Objeto20.Saldo}')

Objeto20.Saldo = '20,000'

Objeto20.Mostrar()

print (f'El saldo privado es {Objeto20.Saldo}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):

    @abstractmethod
    def Mostrar(self):
        pass

class Ejemplo1(Plantilla):
    def Mostrar(self):
        print (f'Hola Abstraccion Example')

Objeto21 = Ejemplo1()

Objeto21.Mostrar()

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''
Esto
Es
Un
Long
String'''

variable4 = Objeto1.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = not False, Objeto3.Catched

# Esto es un comentario simple

'''Esto
Es 
Un 
Comentario 
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')

class Primera():
    def Saludar(self):
        print (f'Hola Composicion')

class Segunda():
    def __init__(self):
        self.Example = Primera()

    def Hi(self):
        self.Example.Saludar()

Objeto22 = Segunda()

Objeto22.Hi()

print (f'-' * 20)

class Tercera():
    def Mostrar(self):
        print (f'Segunda Composicion')

class Cuarta():
    def __init__(self):
        self.Nueva = Tercera()

    def Finale(self):
        self.Nueva.Mostrar()

Objeto23 = Cuarta()
Objeto23.Finale()

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[2]} tiene {Variable_Sumatoria}, {Sumatoria2(1, 2, 3, 4, 5)} o incluso {Objeto2.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un encapsulamiento de variables y snake case {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo  = divmod(Objeto2.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El cociente de la operacion es {Cociente} y el residuo es {Residuo}')

print (f'Un rango de elementos de la lista 2 seria {PEPE.Lista2[2:4]}')
print (f'Un rango de elementos de la lista 2 seria {PEPE.Lista2[:2]}')
print (f'Un rango de elementos de la lista 2 seria {PEPE.Lista2[2:]}')
print (f'Un rango de elementos de la lista 2 seria {PEPE.Lista2[::2]}')
print (f'Un rango de elementos de la lista 2 seria {PEPE.Lista2[::3]}')
print (f'Un rango de elementos de la lista 2 seria {PEPE.Lista2[0:None]}')
print (f'Un rango de elementos de la lista 2 seria {PEPE.Lista2[:]}')

print (f'{Lista_Uno[1]} eso de ahi es un {PEPE.Lista2[2]}?')

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

print (f'{PEPE.__dir__()}')

print (f'{help(PEPE)}')

Tupla1 = ('Electrico', Objeto1.Tipo, Objeto1.Tipo, Objeto1.Tipo, Objeto1.Tipo, Objeto1.Tipo)

print (f'{Tupla1}')

Tupla1 = tuple(('Uno', 'Dos', 'Tres'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{Tupla2[2]}')

print (f'{type(Funcion_Tupla)}')
print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')

Set_Conjunto1 = {'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo', 'Rojo'}
Set_Conjunto1.add('Verde')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Red', 'Blue'})
Set_Conjunto1.add('Black')

print (f'{Set_Conjunto1}')

print (f'El set conjunto tiene {len(Set_Conjunto1)} elementos')

Set_Conjunto2 = {1, 2, 3, 4, 5}
Set_Conjunto3 = {3, 4}
Set_Conjunto4 = set({8})

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')
Set_Conjunto_Menu2 = frozenset({'Caramelo', Objeto3.Tipo})
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, Lista_Uno_Copia[1]})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

print (f'-' * 20)

Diccionario3 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Variable_Sumatoria,
    'Votante' : Variable_Funcion_Tupla[3]
}

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3["Nombre"]}')
print (f'{Diccionario3.get("Edad")}')

print (f'-' * 20)

Diccionario4 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [18 * 2, 20, 6],
    'Votante' : [True, not False, False]
}

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4["Nombre"][1]}')
print (f'{Diccionario4.get("Votante")[2]}')

print (f'-' * 20)

Diccionario5 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5["Ingresos"]}')
print (f'{Diccionario5.get("Gastos")}')

print (f'-' * 20)

Diccionario3['Nombre'] = 'Erick'

print (f'{Diccionario3}')

del Diccionario3['Nombre']
Diccionario3.pop("Edad")

print (f'{Diccionario3}')

Diccionario3.clear()

print (f'{Diccionario3}')

Diccionario3 = dict({1 : "Karlita", 2 : 6, 3 : variable7})

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3[1]}')
print (f'{Diccionario3.get(2)}')

print (f'{Diccionario4["Nombre"][2]} no puede votar todavia ya que solo tiene {Diccionario3.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'HolaMundo')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = PEPE.Diccionario_Poke['Poke3']

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')

Lista_Dict3 = list(['Erick', 'Josue', 'Perez', 'Gutierrez'])

Key3 = [f'Key{i}' for i in range(len(Lista_Dict3))]

print (f'{Key3}')

Diccionario6 = dict(zip(Key3, Lista_Dict3))

print (f'{Diccionario6}')
print (f'{Diccionario6.keys()}')
print (f'{Diccionario6["Key1"]}')
print (f'{Diccionario6.get("Key2")}')

for elemento in Diccionario6.items():
    print (f'{elemento[0]} - {elemento[1]}')

import pandas as pd

Ruta_Csv4 = 'C:\\python-data-analyzer\\data\\sales.csv'

Cargar_Csv4 = pd.read_csv(Ruta_Csv4)

print (f'{Cargar_Csv4}')

Lista_Dict4 = set(Cargar_Csv4['product'])
Key4 = [f'Key{i}' for i in range(len(Lista_Dict4))]

print (f'{Lista_Dict4}')
print (f'{Key4}')

Diccionario7 = dict(zip(Key4, Lista_Dict4))

for elemento in Diccionario7.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'El tipo de variable es {type(variable1)}')
print (f'El tipo de variable es {type(variable4)}')
print (f'El tipo de variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de variable es {type(variable6)}')
print (f'El tipo de variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de variable es {type(Tupla3)}')
print (f'El tipo de variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de variable es {type(Diccionario7)}')
print (f'El tipo de variable es {type(Funcion_Tupla)}')
print (f'El tipo de variable es {type(PEPE)}')
print (f'El tipo de variable es {type(Objeto19)}')
print (f'El tipo de variable es {type(Array6)}')
print (f'El tipo de variable es {type(Data_Frame_Concatenate)}')

if (Diccionario5['Ingresos'] > 500):
    if (Diccionario5['Gastos'] < 200):
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario5['Gastos'] == 200):
        print (f'Ingresos Altos, Gastos Al Limite')
    elif (Diccionario5['Gastos'] > 200):
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario5['Ingresos'] == 500):
    if (Diccionario5['Gastos'] < 200):
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario5['Gastos'] == 200):
        print (f'Ingresos Minimos, Gastos Al Limite')
    elif (Diccionario5['Gastos'] > 200):
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario5['Ingresos'] < 500):
    if (Diccionario5['Gastos'] < 200):
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario5['Gastos'] == 200):
        print (f'Ingresos Bajos, Gastos Al Limite')
    elif (Diccionario5['Gastos'] > 200):
        print (f'Ingresos Bajos, Gastos Altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')

if (variable1 == 'Erick' and variable4 > 50):
    print (f'AMBAS CONDICIONES SE CUMPLEN')
else:
    print (f'Al menos una condicion no se cumple')

if (variable1 == 'Josue' or variable4 > 50):
    print (f'AL MENOS UNA CONDICION SE CUMPLE')
else:
    print (f'Ninguna condicion se cumple')

print (f'{variable1.__dir__()}')
print (f'{help(variable1)}')

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Variable_Sumatoria
        self.Classified = variable6

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')

Objeto24 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto1.Nombre)
Objeto25 = Entrenador(PEPE.Tupla_Poke[1], 'Jotho', Objeto2.Nombre)
Objeto26 = Entrenador(PEPE.Tupla_Poke[2], 'Alolah', Objeto3.Nombre)

Objeto24.Desplegar()
Objeto25.Desplegar()
Objeto26.Desplegar()

Negativo = -5

print (f'{int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima5 = filter(lambda Num :  Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable}')
print (f'{list(Anonima5)}')
print (f'{Lista_Iterable}')

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario5['Vacio']) == True):
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

variable8 = 'eSteBAN'
letra8 = variable8[0]

print (f'{variable8}')
print (f'{variable8.lower()}')
print (f'{variable8.upper()}')
print (f'{variable8.capitalize()}')

print (f'{variable8.lower().find("t")}')
print (f'{variable8.lower().index("b")}')

print (f'La letra {letra8} aparece un total de {variable8.lower().count(letra8)} veces')

print (f'{variable8.lower().startswith(letra8)}')
print (f'{variable8.lower().endswith("n")}')

print (f'{variable8.lower().replace("ban", "POPOTAMO")}')

variable9 = 'esto es un texto cualquiera de practica'

Lista_variable9 = variable9.split(' ')

for elemento in Lista_variable9:
    print (f'{elemento}')

print (f'El numero de palabras digitadas es de {len(Lista_variable9)}')

print (f'{PEPE.Tupla_Poke[2]} aparece en la posicion {PEPE.Tupla_Poke.index("Misty")} nunca usar find, con listas o tuplas solo sirve index()')

Lista_Exception4_Copia = Lista_Exception4.copy()

print (f'{Lista_Exception4_Copia}')

Diccionario7.clear()

print (f'{Diccionario7}')

Diccionario3.pop(1)
Diccionario3.pop(2)
Diccionario3.pop(3)

print (f'{Diccionario3}')

for elemento in Diccionario4:
    print (f'{Diccionario4[elemento]}')

print (f'-' * 20)

for elemento in Diccionario5.items():
    print (f'{elemento[0]} -- {elemento[1]}')

Tupla4 = ('Ponyo', 'Messi', 'Pepe')

variable10, variable11, variable12 = Tupla4

print (f'Esta es la tecnica de desempaquetado de variables {variable11}')

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador+= 1

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1

Lista_Animales = []
Lista_Animales.append('Jirafa')
Lista_Animales.insert(0, PEPE.Lista2[2])
Lista_Animales.extend(['Perro', 'Tortuga'])

print (f'{Lista_Animales}')

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Perro'):
        print (f'El mejor amigo del hombre')
        break
    else:
        Contador+= 1
        continue

for elemento1, elemento2 in zip(Set_Conjunto_Menu1, PEPE.Tupla_Poke):
    print (f'{elemento1} -- {elemento2}')

print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')

for elemento in range(995, 1000):
    print (f'{elemento}')

Lista_Numeros_Mult = [num  * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

Num_Mayor = max(Lista_Numeros_Mult)
Num_Menor = min(Lista_Numeros_Mult)
Redondeado = round(14.458795, 2)
Sumatoria4 = sum(Lista_Numeros_Mult)

print (f'El menor de los numeros es {Num_Menor} y el mayor {Num_Mayor}')
print (f'Redondeado {Redondeado}')
print (f'El resultado de la sumatoria {Sumatoria4}')

print (f'{bool(False)}')
print (f'{bool(not True)}')
print (f'{bool("")}')
print (f'{bool(0)}')
print (f'{bool(None)}')

Todo_All = all([Lista_Uno_Copia, Tupla4, Set_Conjunto_Menu1, ""])

print (f'{Todo_All}')

Uno = int("500")
Dos = str(500)
Tres = float(Dos)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')

Any_Iterable2 = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima6 = filter(lambda Num :  Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable2 = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable2}')
print (f'{list(Anonima6)}')
print (f'{Lista_Iterable2}')

print (f' - '.join(Set_Conjunto_Menu1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

variable_PEPE3 = PEPE3

'''def Floating1(Numero):
    return Variable_Sumatoria * Objeto2.Cantidad + Numero

print (f'El resultado de la operacion es {Floating1(PEPE.Flotante1)}')

Resultado2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado2}')

def Floating3(Textico):
    Lista_Textico = Textico.split(' ')

    for elemento in Lista_Textico:
        print (f'{elemento}')

    print (f'Cantidad de palabras digitadas: {Lista_Textico.__len__()}')

Floating3(PEPE.Flotante3)'''

'''Contador = int(input(f'Ingrese la cantidad de estudiantes -> '))

Lista_Alumnos = []

def Colegio(Lista):
    for elemento in range(Contador):
        Estudiante = input(f'Ingrese el nombre del estudiante {elemento}: ')
        Lista.append(Estudiante)

    return Lista

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nLa lista de estudiantes es {Colegio(Lista_Alumnos)}'])
    Docu.close()

with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

Lista_Alumnos2 = list([])

Contador = int(input(f'Ingrese el numero de estudiantes: '))

def Colegio2(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'El nombre del alumno {elemento} es: ')
        Alumno_Edad = int(input(f'La edad del alumno {elemento} es: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)

    Lista.sort(key = lambda Num : Num[1])
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]

    print (f'El alumno menor de la lista es {Menore} y el mayor es {Mayore}')

Colegio2(Lista_Alumnos2)'''

'''def Exception_Finale():
    while True:
        Numero = input(f'Ingrese un numero: ')
        try:
            Numerito = int(Numero)
            break
        except:
            print(f'Error, necesito que ingreses un numero')

    return Numerito

print (f'Gracias, tu numero ingresado es {Exception_Finale()}')'''

import pandas as pd
import requests
import io

headers = {'User-Agent' : 'Mozilla/5.0'}
Response = requests.get(Ruta_Html, headers=headers)

Leer_Html2 = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Leer_Html2)

print (f'{Cargar_Html2[2].head()}')

import re

Correo = 'sample@sample.com'

Pattern4 = r'^[a-zA-Z0-9./*-+]+\@[a-zA-Z]+\.[a-z]{2,}$'

Buscar18 = bool(re.match(Pattern4, Correo))

if (Buscar18 == True):
    print (f'El formato del correo es correcto')
else:
    print (f'El formato del correo es incorrecto')

from datetime import datetime

Ruta_Csv5 = 'C:\\python-data-analyzer\\data\\sales.csv'

Cargar_Csv5 = pd.read_csv(Ruta_Csv5)

'''Fecha2 = input(f'Ingrese una fecha con formato YY-MM-DD: ')

try:
    Fech2 = datetime.strptime(Fecha2, '%Y-%m-%d').date()
    Fech2_Formateada = pd.to_datetime(Fech2)
    Cargar_Csv5['date'] = pd.to_datetime(Cargar_Csv5['date'])
except ValueError:
    print (f'Error, el formato de la fecha es incorrecto')
    exit()

Encontrado2 = Cargar_Csv5[Cargar_Csv5['date'].dt.date == Fech2_Formateada.date()]

if (Encontrado2.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! ventas encontradas')
    Buscar19 = Encontrado2.groupby('product')['quantity'].sum()
    Buscar19_Prod_Mayor = Buscar19.idxmax()
    Buscar19_Prod_Menor = Buscar19.idxmin()
    Buscar19_Prod_Mayor_Cant = Buscar19.max()
    Buscar19_Prod_Menor_Cant = Buscar19.min()

    print (f'{Buscar19}')
    print (f'En la fecha {Fech2_Formateada} se realizaron {Buscar19_Prod_Mayor_Cant} ventas del producto {Buscar19_Prod_Mayor}')
    print (f'En la fecha {Fech2_Formateada} se realizaron {Buscar19_Prod_Menor_Cant} ventas del producto {Buscar19_Prod_Menor}')
    print (f'Total de ventas {Buscar19_Prod_Mayor_Cant + Buscar19_Prod_Menor_Cant}')'''

Cargar_Csv5['Total'] = Cargar_Csv5['quantity'] * Cargar_Csv5['price']

print (f'{Cargar_Csv5}')

Buscar20 = Cargar_Csv5.groupby('product')['Total'].sum()


print (f'{Buscar20}')

class Pokemon3():
    def __init__(self, Nombre, Tipo, Ataque):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque
        self.Cantidad = 18 * 2
        self.Catched = variable7

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')

class Poke_Hija3(Pokemon3):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo

    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')

Objeto27 = Poke_Hija3(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno', 'Hada')

Pokemon3.Mostrar(Objeto27)
Objeto27.Mostrar()

class Una():
    def Desplegar(self):
        print (f'El mensaje ha sido desplegado')

class Dos():
    def __init__(self):
        self.Mensaje = Una()

    def Mensajear(self):
        self.Mensaje.Desplegar()

Objeto28 = Dos()
Objeto28.Mensajear()

class BankingAccount():
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

Objeto29 = BankingAccount(100)
Objeto29.Depositar(25)
Objeto29.Mostrar()

print (f'El saldo privado es de {Objeto29.Dinero}')

Objeto29.Dinero = '20,000'

Objeto29.Mostrar()

print (f'El saldo privado es de {Objeto29.Dinero}')

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def Generica(self):
        pass

class Primera(Plantilla2):
    def Generica(self):
        print (f'Esto es abstraccion')

    def Otra(self):
        print (f'Este es otro mensaje cualquiera')

Objeto30 = Primera()

Objeto30.Generica()
Objeto30.Otra()
