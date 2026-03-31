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
print (f'-' * 30)
print (f'-' * 30)
print (f'-' * 30)
print (f'-' * 30)
print (f'-' * 30)
print (f'-' * 30)
print (f'-' * 30)
print (f'-' * 30)
print (f'-' * 30)
print (f'-' * 30)
print (f'-' * 30)
print (f'-' * 30)


# Ahora creemos una lista con 10 elementos, luego creemos un arreglo y llenemoslo con los elementos de la lista

# Ahora creemos dos arrays de 1x3 cada uno y concatenemoslos con np.concatenate       -----  np.concatenate([arr1, arr2], axis = 1)
# Tomemos un array de 6 elementos y dividamoslo en 3 arrays  de 2 elementos cada uno con np.split(Array, 3)
# Ahora hagamos un array de 10 elementos, con la instruccion np.where(Array == 3) me creara un array que muestra todas las posiciones donde haya un 3

# con un ciclo for y una matriz de 2x3 recorra cada una de las filas
# Con un ciclo for y una matriz de 2x2x3 recorra cada matriz y luego otro for para recorrer cada fila
# vamos a hacer una matriz de 2x2x3 y con axis, vamos a sumar solo los elementos de la segunda fila np.sum(array1, axis=0)

# Vertical (por columnas)	           axis=0	Baja por las filas ↓
# Horizontal (por filas)	           axis=1	Cruza las columnas →
# Todo	                               Ninguno	Hace todo junto

'''
[Mini programa ganador del sorteo]
Creemos una lista con 6 nombres
Ganador = random.choise(Lista_Nombres)
Ahora elija 3 ganadores  Ganador = random.choise(Lista_Nombres, size=(3))
Finalmente elija una matriz de ganadores de 2x3     random.choise(Lista_Nombres, size=(2, 3))
Con la instruccion replace = False, vamos a asegurarnos que ningun numero del resultado se repita


Busque 3 numeros entre el 1 y el 10 con Array_Linspace = np.linspace(start=1, stop=10, num=3)
'''



Hagamos una funcion Generadora.
Las funciones generadoras me permiten ejecutar un codigo de manera pausada y controlada para ver el comportamiento.

Hagamos una funcion generadora, donde por medio de un range se muestren 10 numeros, pero con los parametros de la funcion generadora, ir de uno en uno para analizar su ejecucion.

def Ejemplo():
    for elemento in range(0, 10):
        yield elemento

Rango = Ejemplo()

print (f'{next(Rango)}')


Ahora hagamos una funcion donde por medio de un range se evalue si el elemento es un numero par o impar, vamos a ir evaluando cada uno con un if % 2 == 0 y yield, quiero que me muestre cada resultado de manera individual. La idea es con el next mostrar par, impar, par, etc….

def Ejemplo2():
    for elemento in range(5):
        if (elemento % 2 == 0):
            yield f'par'
        else:
            yield f'impar'

Rango2 = Ejemplo2()

print (f'{next(Rango2)}')



# Ahora vamos a hacer un ejercicio mas donde por medio de una funcion que recorra un ciclo range, con yield y next se muestre cada uno por separado
# Pero en este caso cuando lleguemos al final mostraremos un mensaje El ejercicio termino. Esto lo manejaremos con una exception StopIteration
def Ejemplo():
    for elemento in range(3):
        yield elemento

Rango = Ejemplo()

try:
    print (f'{next(Rango)}')
    print(f'{next(Rango)}')
    print(f'{next(Rango)}')
    print(f'{next(Rango)}')
except StopIteration:
    print (f'El ejercicio termino')
'''


####### CREANDO MIS PROPIAS FUNCIONES

# Creamos una funcion simple propia que diga hola mundo  en  Modulo_Propio
# Creamos una funcion que tenga un parametro nombre = (argumento) declarado en la misma funcion. En  Modulo_Propio
# Creamos una funcion que tenga un parametro nombre agregado por el usuario en  Modulo_Propio, ojo hagamos la funcion type hint mostrando el tipo de dato
# Creamos una funcion que recibe dos numeros, retorne (return) la suma del num1 y el num2 en  Modulo_Propio
# Ahora haremos la misma sumatoria pero con funciones anidadas
# Crear una función que devuelva True si un número es par
# Creamos ahora una funcion con dos parametros, nombre y sexo, si el sexo es femenimo muestra chica, si el sexo es masculino muestra chico con un condicional.
# Ahora haremos la misma funcion pero con funciones anidadas
# Creamos una funcion que solicite un numero para hacer una contrasena random, se devuelve un valor con return
# *args devuelve una tupla
# Con un subindice, muestre un solo elemento de la tupla resultado
# **kwargs devuelve un diccionario
# Ahora vamos a usar el argumento *args para empaquetar varios argumentos en una unica variable, hacemos una funcion que reciba muchos argumentos, los sume todos y despliegue el resultado
# Ahora vamos a hacer una funcion que diga, variable nombre Erick, la sumatoria de todos tus numeros es xxx, usando dos parametros, nombre y *args
# Ahora vamos a crear una tupla con *args
# Creamos un diccionario con **kwargs
# Creamos una funcion anonima lambda basica
# Crear una lambda que calcule el doble de un número. y lo imprima
# Creamos una lista de numeros y una funcion lambda con un filter que saque solo los pares

'''
Declarar una variable global externa integer
Ahora declaramos una funcion con una variable local interna integer
Hacemos una suma en la funcion de la variable global mas la variable local

Hagamos una funcion anidada
funcion externa con una variable nombre
indentamos una funcion interna con un apellido
imprimimos el nombre completo en la funcion interna

'''

# Esto es una funcion closure anidada que agrega numeros a una lista

def Agregue_Numero_Externa():
    Lista = []
   
    def Agregue_Numero_Interna(x):
        Lista.append(x)
        print (f'{Lista}')
       
    return Agregue_Numero_Interna

variable = Agregue_Numero_Externa()

variable(1)
variable(2)
variable(3)

# Ahora vamos a crear un closure con dos funciones crear_multiplicador y multiplicar que recibe dos parametros x y n, la idea es crear dos variables que multpliquen 10 * 2 y 10 * 3

def crear_Multiplicador(x):
    def Multiplicar(n):
        return x * n
   
    return Multiplicar

num1 = crear_Multiplicador(2)
num2 = crear_Multiplicador(3)

print (f'El primer resultado es {num1(10)}')
print (f'El primer resultado es {num2(10)}')

# Creamos una funcion que reciba un set o tupla de numeros y filtre para mostrar unicamente los numeros pares
Pares = [num for num in Lista if num % 2 == 0]

'''
************************* DECORADORES   *************************

1 - Primero vamos a crear un decorador que afecta a una funcion saludar hola mundo. La idea es agregar el texto "Esto va antes" a la funcion saludar hola mundo original por medio de un decorador

2 - Ahora vamos a crear una funcion que suma dos numeros, por medio de otro decorador, vamos a alterar el resultado de la sumatoria de la funcion y le sumaremos 100 mas

3 - Ahora vamos a crear una funcion que muestre un nombre y un apellido y por medio de un decorador vamos a cambiar el nombre de Erick a Carmelo

'''



# Crea una clase pokemon con tipo, nombre, ataque y una variable capturado en el  Modulo_Propio

# Usemos un unico elemento del modulo saludar con la instruccion "from Saludar import Diccionario_Poke", ya no se necesita usar Saludar

# Creemos una clase hija que herede todas las caracteristicas de la clase pokemon

# Ahora vamos a hacer un ejercicio de herencia multiple con 3 clases, una clase camara, otra reproductor musica y otra clase smartphone, smartphone hereda de las clases padre. Solamente tendra un metodo accion cada una


'''

Tipos de Herencia
Hacer un ejemplo de herencia Simple
Pokemon y poke hija

Hacer un ejemplo de herencia Herarquica (Veterinaria)
clase padre Mascota (nombre, edad, peso)
Clases hijas (Perro, Gato, Pajaro)
Perro (Raza, Padecimiento, N_Visitas)
Gato (Raza, Color, Paciente_Activo)
Pajaro (Especie, Habla)


Hacer un ejemplo de herencia Multiple (Personaje VideoJuego)

Atacante
daño base
método para atacar
energía de ataque

Curador
puntos de curación
método para curar
regeneración de vida

Paladin

Hereda de atacante y curador y tiene un nombre. Mostrar ficha de personaje



Como saber si una clase hija hereda de una clase padre?
Herencia = issubclass(Poke_Hija, Poke) # Esto debe darme true como resultado

Como saber si una variable es un objeto de una clase?
Instancia = isinstance(Objeto1, Poke) # Esto debe darme true como resultado



MRO  (Que pasa si varias clases tienen el mismo metodo?)
Vamos a hacer un ejemplo de herencia con MRO, lo que haremos es crear 5 clases, A,F,B,C,D,F, donde cada una tendra un metodo llamado Mostrar() y un texto hola "letra".
B heredara de A, C heredara de F, D heredara de B y C. Con esto veremos el flujo y como mostraria el mensaje del metodo si tengo un objeto Objeto1.Mostrar() Cual mensaje mostrara primero?
Vamos quitando bloques con pass
Que deberia hacer ahora que entiendo el orden del MRO si quisiera explicitamente llamar el metodo de la clase B desde D?

B.Mostrar(Objeto1)
F.Mostrar(Objeto1)
A.Mostrar(Objeto1)




[Polimorfismo]
Un cliente puede pagar con:
Tarjeta
PayPal
Criptomonedas
Todos comparten el mismo metodo pagar() que cambia dependiendo del metodo de pago


[Encapsulamiento] __privada
Cuenta bancaria encapsulada:
class Cuenta:

    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, dinero):
        self.__saldo += dinero

    def ver_saldo(self):
        print(self.__saldo)

mi_cuenta = Cuenta(100)
mi_cuenta.depositar(50)
mi_cuenta.ver_saldo()

Encapsulamiento: El saldo está protegido, no se puede alterar.

Getter → sirve para LEER un dato
Setter → sirve para CAMBIAR un dato

Muestre el valor de __Saldo con un getter
Cambie el valor de __Saldo con un setter

Hagamos una clase protegida que reciba un
nombre __privado y mostrarlo afuera de la
clase por medio de un @property



class Protegido:
    def __init__(self, Nombre):
        self.__Nombre = Nombre

    def Mostrar(self):
        print (f'Tu nombre es {self.__Nombre}')

    @property
    def nombre(self):
        return self.__Nombre

    @nombre.setter
    def nombre(self, Nuevo_Nombre):
        self.__Nombre = Nuevo_Nombre

Objeto1 = Protegido('Erick')

Objeto1.Mostrar()

Objeto1.nombre = 'Hola'   # setter

print(Objeto1.nombre)     # getter

--------------------------------------------------------------------






Abstraccion

Clases Abstractas

Las clases abstractas son plantillas que generan reglas que se deben seguir a la hora de crear clases en proyectos grandes.
En otras palabras, si hay 100 programadores, todos deben crear las reglas definidas en la plantilla. Normalmente son metodos.
Pero yo puedo crear todos los metodos que quiera en mis clases, la clase abstracta me dice nada mas que a fuerza la clase nueva debe tener ese metodo definido y todo lo demas que quiera.

from abc import ABC, abstractclassmethod

class Comida(ABC):

    @abstractclassmethod
    def Cocinar(self):
        pass

class Pizza(Comida):
        def Cocinar(self):
            print (f'Horneando La Pizza')

        def Mostrar(self):
            print (f'Hola Mundo')

Objeto1 = Pizza()

Objeto1.Cocinar()
Objeto1.Mostrar()

'''




# Como declarar dos variables string?
# Como declarar una variable long string?
# Como declarar una variable integer?
# Como declarar una varible decimal
# Como declarar dos variables booleanas?
# Declare dos variables en la misma linea
# Agrega un comentario simple
# Agregue un comentario compuesto
# Imprime un texto con una variable string
# Imprime dos varibles string concatenadas
# Imprime una concatenacion de una varible texto y un integer
# borra una variable
# Juegue con los operadores de pertenencia in / not in
# Declare una variable con Snake Case

# ***********************  Listas   **********************

# Declara una lista con string

# Usemos un unico elemento del modulo saludar con la instruccion "from Saludar import Lista1" y cambiemosle el nombre con “as”, ya no se necesita usar Saludar

# Declara una lista con diferentes tipos de datos En  Modulo_Propio
# Declara una lista de solo numeros En  Modulo_Propio
# Cree una lista con la funcion list En  Modulo_Propio

# Ahora vamos a sacar del modulo propio varias listas al mismo tiempo 1 y 4 con la instruccion from Modulo_Propio import Lista1, Lista4

# Muestre en consola la cantidad de elementos en una de las listas con la funcion len
# Agrega un elemento aleatorio a la lista con .append()
# Inserta un elemento en una posición específica con .insert(posición, elemento)
# Agreguemos varios elementos a la lista con extend(['Cada elemento se ingresa asi'])
# Haz alguna operacion matematica con los valores de la lista 3
# Despliegue en consola el resultado
# Imprima un rango de elementos de la lista, por ejemplo del valor en la posicion 0 al 2 con [x:y]
# Concatene un elemento de la primer lista y de la segunda lista e imprima en consola
# Imprima todos los elemento de alguna de las tres listas
# Cambie el valor de un elemento de una lista
# Ahora muestre todos los elementos de la lista incluyendo el que cambio
# Borre un valor de una lista usando del
# Borra otro elemento usando .remove(elemento textual) y muestra la lista
# Borre 1 elemento de la lista utilizando el metodo pop('Indice')
# Borre 1 elemento de la lista utilizando el metodo pop('Indice negativo para borrar el ultimo elemento')
# Elimine todos los elementos de una lista con el metodo clear()
# Ordena la lista 3 numerica en orden ascendente con .sort()
# Ordena la lista 3 numerica orden descendente .sort(reverse=True)
# Invierte el orden de la lista con .reverse()

# User la funcion dunder "dir" sobre el Modulo_Propio para ver todas sus caracteristicas incluyendo todos los elementos que creamos a mano

# ********************************************************

# Cree una tupla
# Cree una tupla con la funcion tuple
# Cree una tupla sin parentesis
# Cree una tupla sin parentesis de un solo elemento
# En que se diferencia una lista de una tupla?
# Intente cambiar un elemento de la tupla para obtener un error
# Muestre en consola todos los elementos de la tupla
# Muestre con un print un elemento de la tupla

# Cree un set o conjunto
# Cree un set con la funcion set
# Cual es la diferencia entre una lista, una tupla y un set o conjunto?
# Muestre los elementos totales del conjunto
# Intente agregar un elemento al set con .add()
# Reconstruya el conjunto con nuevos elementos
# Intente agregar un elemento repetido del conjunto para obtener un error

# TEORIA DE CONJUNTOS, CONJUNTOS SETS SIMPLES Y FROZENSETS *****
# Creamos dos conjuntos, uno tiene 3 elementos que salen en un super conjunto mayor conjunto1, conjunto2
# Usemos el metodo .issubset() para saber si el conjunto 2 es un subconjunto de 1, osea que sus elementos salen en el conjunto mayor, devolvera True
# Usemos el metodo .issuperset() para saber si el conjunto 1 es un super conjunto de 2
# Ahora comparemos si en el conjunto 2 hay algun elemento que se repita en conjunto 1 con .isdisjoint()
# El restaurante tiene un menú fijo de jugos. Este menú nunca cambia, entonces hagamos un set con frozenset({}) de 3 sabores que no pueden cambiar
# Intentar agregar un nuevo sabor con el metodo .add() para obtener un error
# Ahora hacemos otro set_conjunto con 3 sabores, pero este es un set normal
# Intentar agregar un nuevo sabor con el metodo .add()

# Crea un diccionario
# Cree un Diccionario con la funcion dict
# Muestre cada una de las llaves de un diccionario con el metodo keys
# Imprima un Elemento del diccionario
# Despliegue otro elemento del diccionario con la funcion get()
# Imprima Todo el diccionario
# Cambie un elemento del diccionario
# Elimine un elemento del diccionario con el metodo pop()
# Muestre el diccionario con los nuevos elementos
# Reconstruya el diccionario con nuevos valores, ojo las llaves ahora seran numeros - Cree un Diccionario con la funcion dict
# Haga un diccionario2 pero con varios elementos por indice, varios nombres, varias edades, etc
# Imprima en consola una concatenacion de dos elementos del diccionario
# Muestre cada una de las llaves de un diccionario con el metodo keys
# Haga una operacion matematica con un elemento de una lista o tupla y uno del diccionario
# Concatene un elemento de una lista con una tupla
# Concatene un elemento de una lista con el diccionario
# Creamos un diccionario vacio, solo con los keys pero sin valores por medio de la funcion dict.fromkeys([])
# Ahora creamos un diccionario en el que todos los keys tengan el mismo valor Diccionario_Vacio = dict.fromkeys('ABCD', "Carmelo")

# Hagamos un diccionario vacio con fromkeys, luego una lista de elementos y agregue los elementos de la lista al diccionario con un ciclo    i=0


# A partir de los elementos del csv file, vamos a crear primero una lista de llaves, luego vamos a tomar los nombres y agregarlos a una lista
# finalmente vamos a crear un diccionario y emparejar las llaves creadas y los nombres y mostramos el nuevo diccionario creado



# Declare una variable y asignele una division flotante
# Declare una variable y asignele una potenciacion o exponente **
# Declare una variable y asignele una division baja //
# Declare una variable y asignele un resto o modulo %
# Muestre en consola el tipo de dato de una variable float, un string, una lista, una tupla, un conjunto y un diccionario
# Despliegue el resultado de la division flotante y de la division baja

# ***********************  Condicionales   **********************

# Crea una llave condicional con if simple - Contar la cantidad de caracteres de una cadena de texto con len, haga un if condition
# Crea una llave condicional con if y else simple
# Ahora crea un condicional con if, elif y else
# Ahora crea un condicional con multiples elif
# Ahora un ejercicio con varios if anidados - declaras dos variables, ingresos y gastos, si los ingresos son mayores a x y los gastos menores a x, entonces estas bien, etc
# Ahora vamos a hacer un if con un and
# Ahora vamos a hacer un if con un or

# ***********************  Metodos / Funciones mas utilizadas   **********************

# Declare una variable string, con un print y dir muestre todos los métodos y atributos disponibles para una variable u objeto
# use help para ver que hace un metodo

#**********

# Declare una clase Persona, cree un objeto y defina un metodo
# Metodos magicos vs metodos normales
# dunder methods porque empiezan y terminan con __)
# x = 'Ejemplo'
# len(x) o tambien
# x.__len__()
# Metodos normales x.upper()

#**********

# abs(x) → Escribe un programa que reciba un número negativo y devuelva su valor absoluto.
# any(iterable) → Comprueba si al menos un número de una lista es par.
# bin(x) → Convierte un número entero dado por el usuario a binario.
# bool(x) → Determina si una cadena ingresada por el usuario está vacía o no.
# divmod(a, b) → Pide dos números y muestra el cociente y el residuo de su división.
# Haz un ciclo for enumerate con un unico elemento, ese unico elemento mostrara el indice con elemento[0] y el valor con elemento[1]
# enumerate(iterable) → Crea una lista de frutas y muestra cada una con su posición en la lista.
# Haga el texto de una variable todo minuscula con el metodo lower
# Haga el texto de una variable todo mayuscula con el metodo upper
# Haga la primera letra de una variable mayuscula con el metodo capitalize
# Busque una letra en especifico en una cadena de texto con el metodo find e index
# Cuantas veces esta la letra a en una cadena con el metodo count
# Verifiquemos si una cadena comienza con x letra con el metodo startswith
# Verifiquemos si una cadena termina con x letra con el metodo endswith
# Reemplace una parte de una cadena con el metodo replace(Este tiene dos parametros, lo que se quiere cambiar y lo nuevo)
# Tome una variable de texto y separe cada elemento de la variable en una lista separada por ',' utilizando el metodo split()

# Busque un elemento en una lista o tupla con index, ojo find no es un metodo para listas
# Declare una variable y asignele una copia de una lista con el metodo copy()
# Borrar todos los elementos de un diccionario con clear()
# Eliminar un elemento del diccinario con pop()
# Recorra todos los elementos de un diccionario con un ciclo for normal
# Recorramos tdos los elementos de un diccionario con la funcio .items()

#### VARIABLES 2.0

# Vamos a usar la tecnica de desempaquetado de variables creando una tupla de 3 elementos y agregando cada elemento de la tupla a 3 variables, ojo, no usar indices

### CICLOS WHILE

# Creamos una lista con los numeros 1, 2, 3, 4, 5, hagamos un ciclo for que multiple cada uno de estos numeros y los muestre en consola
# Creamos ahora una lista con 3 animales, los recorremos con un ciclo for, inmediatamente se evalua con un if si la variable es igual al segundo animal, lo muestra y se detiene el ciclo. Ojo, usar el break y el continue
# Hagamos un for anidado con la funcion zip(), creamos dos listas del mismo tamaño
# Hagamos un ciclo for con la funcion range de 0 a 5 con un unico parametro
# Hagamos un ciclo for con la funcion range de 1 a 10 con dos parametros
# Creamos una lista con 4 numeros, ahora creamos otra listsa Lista_Multiplicado y agregamos cada numero de la primera lista a la segunda x 10

#### Ciclo WHILE
# Creamo un ciclo while simple con un contador que se ejecutara mientras contador sea menor a 10


#### Funciones creadas directamente por python (Funciones Build-In)

# Encontrar el numero mayor de una lista con la funcion max()
# Encontrar el numero menor de una lista con la funcion min()
# Redondear el numero 14.458795 a dos decimales con la funcion round() con dos parametros
# Retornemos False con la funcion bool() usando False, 0, "", None
# Retornemos un False agregando varios elementos a una variable con la funcion all() pero al menos uno debe ser False, 0, "", None
# Cree una variable y sumele todos los elementos de una Tupla, Lista, Set con la funcion sum()

# Imprime en pantalla    print()    
# Solicita datos al usuario     input()
# Devuelve la longitud de una secuencia    len()
# Devuelve el tipo de un objeto    type()
# Convierte un número a texto y viceversa  str(), int(), float()
# Despliegue los numeros de 90 a 100 con range()
# Imprime los elementos de una lista con su posición.     enumerate()
# Combina dos listas y muéstralas juntas    zip()
# Ordena una lista de números con sort, sort(reverse = True) reverse()

# Verifique si un elemento de una tupla es par con any()
# Cree una list(), tuple(), set(), dict()
# Cree una lista de 4 palabras por ejemplo mi nombre completo y unalas con la funcion print ("-".join(Lista))

# Divide un texto por espacios con split()

# ***********************  Data Inputs   **********************

# Input lo que nos devuelve siempre es texto, aunque se ingresen numeros
# Declare una variable y asignele un input, pida que ingrese un numero
# Esa variable debe convertirse en integer con la funcion int
# Haga una operacion matematica con esta variable y muestrela

# eval(expression) → Permite al usuario ingresar una operación matemática como texto y muestra el resultado.

# Haga un input que pida su nombre y valide si lo que se ingreso es un texto o algo mas
# (Nombre.replace(" ", "").isalpha()):

# Vamos a crear un programa en el que por medio de un input le pidamos a un usuario ingresar una cadena de texto
# Esta cadena de texto sera guardada en una variable matriz con la funcion split separando cada palabra por un espacio
# Ahora vamos a usar la funcion dunder len para contar cuantas palabras ingreso el usuario

# Creamos una lista vacia, Ahora creamos un programa que pida la cantidad de alumnos
# Luego con un for range, se recorre el ciclo y se pide el nombre de la cantidad de alumnos
# Por medio de un append agregamos cada nombre a la lista vacia
# Mostramos los elementos del filtro, cada nombre digitado

# Ahora vamos a hacer un programa que pida nombres y edades, vamos a evaluar cual es el mayor y cual es el menor
# Y vamos a desplegar que el mayor es el profesor y el menor es el alumno menor

# Usemos elementos de un modulo por medio de un import
# Renombremos un modulo con la instrucion "as" Saludar as OtroNombre



##############################     ENRUTAMIENTO DE MODULOS     ######################################

''' Hay un modulo llamado Modulo_Propio2 dentro de una carpeta alternativa, importemos esta carpeta alternativa
por medio del nombre de la carpeta Nueva.Modulo_Propio2, y despleguemos algun elemento de Modulo Propio2,
Como el nombre del import se vuelve grandisimo, usemos "as" para renombrarlo y que sea mas facil manejarlo'''


##############################     PAQUETES (Es una carpeta con muchos archivos python)     ######################################

''''''Un paquete es una carpeta con muchos archivos, lo mas importante es que esta carpeta para ser
Considerara un paquete debe tener un archivo llamado __init__.py, esto lo convierte en paquete
Si dentro de esta carpeta paquete agregamos una sub carpeta con __init__.py, esto se vuelve un sub paquete.'''




Alumnos = []

Cantidad = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Cantidad):
        Alumno = input(f'Ingrese el nombre del alumno {elemento}: ')
        Edad = int(input(f'Ingrese la edad del alumno {elemento}: '))
        Estudiante = [Alumno, Edad]
        Lista.append(Estudiante)
        Lista.sort(key = lambda Num : Num[1])

    Estudiante = Lista[0][0]
    Profesor = Lista[-1][0]

    print (f'El profesor es {Profesor} y el estudiante menor es {Estudiante}')


Colegio(Alumnos)


---------------------------




[Excepciones]
Una excepcion es un bloque de codigo que se mostrara en caso de que el codigo se rompa. Por ejemplo digamos que tenemos un codigo que pide un numero pero ingresamos una cadena de texto. Entonces el codigo se detendra y mostrara un mensaje de error hasta que agreguemos el numero.

def Ejemplo():
    while True:
        Numero1 = input(f'Ingrese un numero: ')
        try:
            Numerito = int(Numero1)
            break
        except:
            print (f'Error, eso no es un numero')

    return Numerito

print (f'{Ejemplo()}')



[LEER UNA PAGINA WEB]

import pandas as pd
import requests
import io # Esto viene incluido en Python, no hay que instalar nada

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'
headers = {'User-Agent' : 'Mozilla/5.0'}

# 1. Obtenemos la respuesta
Response = requests.get(Ruta_Html, headers=headers)

# 2. Envolvemos el texto en StringIO (esto suele quitar el 99% de los errores)
texto_html = io.StringIO(Response.text)

# 3. Leemos las tablas
Cargar_Html = pd.read_html(texto_html)

# 4. Mostramos la primera tabla encontrada
print(Cargar_Html[0].head())


# Validar si el correo electronico tiene el formato correcto por medio de expresiones regulares

'''

import re

email = 'example@example.com'

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.match(pattern, email)

if result:
	print (f'Valido')
else:
	print (f'Invalido')

'''

Expresiones regulares en Python
Excepciones
Importar modulos
Escribir en un txt file
DataFrames de Pandas
Graficos con Matplotlit
Trabarjar con archivos excel
Trabajar con archivos csv
Trabajar con informacion de una pagina web
Arreglos con numpy
Funciones Generadoras
Funciones
Funciones anidadas
Funciones Lambda
Decoradores de funciones
Funciones Type hint
Funciones Closure
Clases
Variables
Listas
Tuplas
Conjuntos
Diccionarios
Condicionales
Ciclo For
Ciclo While
Data inputs







Esto es un programa que solicita una fecha y la compara con una entrada de un documento csv. Si no la encuentra mostrara un mensaje de error, si el formato es incorrecto mostrara un mensaje de error, si la encuentra mostrara el mensaje que la fecha se encontro x numero de veces.

Importar pandas
from datetime import datetime
Crear la ruta del csv
Cargar el archivo csv
Pedir la fecha por medio de un input
hacer un try except valueerror
en el try primero vamos a asegurarnos co datetime.strptime que el formato es el correcto
en el try luego hay que asegurarnos que la fecha esta formateda to_datetime
en el try despues hay que asegurarse que la fecha del csv esta formateada to_datetime
si no, el excep muestra un error ojo necesita un exit()
Hacemos una variable encontrado, igualamos == entrada del csv .dt.date contra la fecha ingresada date()
if encontrado.empty
else
exito

'''

# Estudiemos clases y herencia

class Pokemon:
    def __init__(self, Nombre, Tipo, Ataque):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque
        self.Cantidad = 18 * 2
        self.Catched = not True

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')

class Poke2(Pokemon):
    def __init__(self, Nombre, Tipo, Ataque, City, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.City = City
        self.Sub_Tipo = Sub_Tipo

    def Desplegar(self):
        print (f'{self.Nombre} se encuentra en {self.City} y tiene tipos {self.Tipo} / {self.Sub_Tipo}')

Objeto1 = Poke2('Pikachu', 'Electrico', 'Impact Trueno', 'Kanto', 'Acero')

Objeto1.Mostrar()

print (f'-----------')

Objeto1.Desplegar()