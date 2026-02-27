import re

var1 = 'esTo es hula un texto 2 pero tambien! es hela un 150 ejercicio que yo estaree intenntando? hola completaR'

Buscar1 = re.search('ejercicio', var1)

print (f'{Buscar1}')

Buscar2 = re.fullmatch('esTo es hula un texto 2 pero tambien! es hela un 150 ejercicio que yo estaree intenntando? hola completaR', var1)

print (f'{Buscar2}')

Buscar3 = re.findall('e', var1)

print (f'{Buscar3}')

Buscar4 = re.findall(r'\d+', var1)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\D+',var1)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\w+', var1)

print (f'{Buscar6}')

Buscar7 = re.findall(r'\W+', var1)

print (f'{Buscar7}')

Buscar8 = re.findall(r'\w+', var1)

print (f'{Buscar8}')

Buscar9 = re.search(r'\W', var1)

print (f'{Buscar9}')

Buscar10 = re.findall(r'h.la', var1)

print (f'{Buscar10}')

Buscar11 = re.findall(r'[a-z]+', var1)

print (f'{Buscar11}')

Buscar12 = re.findall(r'[a-zA-Z0-9\W]+', var1)

print (f'{Buscar12}')

Buscar13 = re.search(r'^e', var1)

print (f'{Buscar13}')

Buscar14 = re.search(r'R$', var1)

print (f'{Buscar14}')

var2 = '''
esto
es
un
Texto
multilinea'''

var3 = 'otro ejemplo123 ! vamos a ver si caeaemos bapero no solo saeaenz sabia  esto sirv@'

Buscar15 = re.search(r'[A-Z]+', var2, flags=re.M)

print (f'{Buscar15}')

Buscar16 = re.search(r'[a-z]+', var2, flags=re.IGNORECASE)

print (f'{Buscar16}')

Buscar17 = re.search(r'[0-9]{3}\s{1}\W{1}', var3)

print (f'{Buscar17}')

Buscar18 = re.findall(r'(ae){2,4}', var3)

print (f'{Buscar18}')

Buscar19 = re.findall(r'[ab]+', var3)

print (f'{Buscar19}')

Buscar20 = re.findall(r'\d+|\W+', var3)

print (f'{Buscar20}')

Fecha = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Patron1 = r'\d{2}/\d{2}/[0-9]{4}'

Replacement = 'xxxxxxx'

Buscar21 = re.sub(Patron1, Replacement, Fecha)

print (f'{Buscar21}')

Email1 = 'sample123@sample.com'

Patron2 = r'[a-zA-Z0-9%.]+@([a-z]).?.([a-z]){2,}'

Buscar22 = re.match(Patron2, Email1)

if (Buscar22):
    print (f'Formato correcto')
else:
    print (f'Formato incorrecto')

def Exception1(Elemento):
    try:
        Numerito = int(Elemento)
        print (f'Gracias, el numero es {Numerito}')
    except ValueError:
        print (f'Error, necesito que sea un numero')

Exception1("Hola")

def Exception2(Num1, Num2):
    try:
        Resultado = Num2 + Num1
        print (f'El resultado de la operacionn es {Resultado}')
    except TypeError:
        print (f'Error, necesito que ambos elementos sean numeros')

Exception2(12, "Hola Mundo")

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

Diccionario_Exception5 = {
    'Nombre' : "Erick",
    'Edad' : 37
}

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error la llave esta fuera de rango')

Exception5('Votante')

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

try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado no existe')

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nSalamandra'])
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nOso')
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

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'{Data_Frame1}')

print (f'------------')

print (f'El menor de todos es {Data_Frame_Concatenate_Age.min()} y el mayor es {Data_Frame_Concatenate_Age.max()}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'------------')

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Nombrecito = elemento['Nombre']
    Edaccita = elemento['Edad']

    print (f'Mi nombre es {Nombrecito} y mi edad {Edaccita}')

print(f'------------')

Llaves = [f'Llave_{i}' for i in range(len(Data_Frame_Concatenate))]

print (f'{Llaves}')

Lista_Nombres = list(Data_Frame_Concatenate['Nombre'])

print (f'{Lista_Nombres}')

Diccionario_DataFrame = dict(zip(Llaves, Lista_Nombres))

print (f'{Diccionario_DataFrame}')
print (f'{Diccionario_DataFrame.keys()}')
print (f'{Diccionario_DataFrame["Llave_1"]}')
print (f'{Diccionario_DataFrame.get("Llave_4")}')

print(f'------------')

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print(f'------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print(f'------------')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()
'''

print (f'{Data_Frame_Concatenate.head(1)}')

print(f'------------')

print (f'{Data_Frame_Concatenate.head(3)}')

print(f'------------')

print (f'{Data_Frame_Concatenate.tail(1)}')

print(f'------------')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'El numero de filas son {Filas} y el numero de Columnas son {Columnas}')

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

print(f'------------')

Elemento6 = Data_Frame2.iloc[0, 0]
Elemento7 = Data_Frame2.iloc[1, 1]
Elemento8 = Data_Frame2.iloc[2, 2]
Elemento9 = Data_Frame2.iloc[1, :]
Elemento10 = Data_Frame2.iloc[:, 2]

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')
print (f'{Elemento9}')
print (f'{Elemento10}')