import Module_Own as PEPE

with open (f'C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
    Documento_SobreEscribir = Docu.write(f'Rosa')
    Docu.close()

with open ('C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

with open ('C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nGirasol'])
    Docu.close()

with open ('C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nMargarita')
    Docu.close()

with open ('C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

with open ('C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nFresa Sabrosa', '\nFresa Sabrosa', '\nFresa Sabrosa'])
    Docu.close()

with open ('C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

with open ('C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke1"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke2"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke3"]}\n')
    Docu.close()

with open ('C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

with open ('C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Set_Conjunto_Poke)])
    Docu.close()

with open ('C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()

import pandas as pd

Data_Frame1 = pd.DataFrame({
    'Nombre' : ['Erick', 'Josue', 'Karlita'],
    'Edad' : [36, 20, 6],
    'Votante' : [True, True, False]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ['Roberto', 'Camilo', 'Susana'],
    'Edad' : [55, 24, 7],
    'Votante' : [True, True, False]
})

Data_Frame1_Age = Data_Frame1['Edad']

print (f'{Data_Frame1}')

print (f'-----------------')

print (f'{Data_Frame1.info()}')

print (f'-----------------')

print (f'{Data_Frame1["Votante"]}')

print (f'-----------------')

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

print (f'{Data_Frame_Concatenate}')

print (f'La menor de las edades es {Data_Frame1_Age.min()} y la edad mayor es {Data_Frame1_Age.max()}')

print (f'-----------------')

import openpyxl

Ruta_Excel = 'C:\\Users\\XPC\\Desktop\\Hola Git\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine = 'openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'-----------------')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, names=['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, index_col='nombre')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, usecols="E:H", index_col='edad')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine = 'openpyxl', sheet_name=0, header=0, usecols="E:H", index_col='edad', nrows=1)

print (f'{Cargar_Excel1.head()}')

print (f'-----------------')

print (f'{Cargar_Excel2.head()}')

print (f'-----------------')

print (f'{Cargar_Excel3.head()}')

print (f'-----------------')

print (f'{Cargar_Excel4.head()}')

print (f'-----------------')

print (f'{Cargar_Excel5.head()}')

print (f'-----------------')

print (f'{Cargar_Excel6.head()}')

print (f'-----------------')

Cargar_Excel2_Sorted = Cargar_Excel2.sort_values(by = ['clase'])

print (f'{Cargar_Excel2_Sorted}')

print (f'-----------------')

Cargar_Excel2_Sorted_Ascending = Cargar_Excel2_Sorted.sort_values(by=['clase'], ascending=False)

print (f'{Cargar_Excel2_Sorted_Ascending}')

print (f'-----------------')

Ruta_Txt = 'C:\\Users\\XPC\\Desktop\\Hola Git\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'-----------------')

print (f'{Cargar_Txt.head()}')

print (f'-----------------')

Ruta_Csv = 'C:\\Users\\XPC\\Desktop\\Hola Git\\Base_Datos.csv'

Cargar_Csv = pd.read_csv(Ruta_Csv)

print (f'{Cargar_Csv}')

print (f'-----------------')

import pandas as pd

import requests

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Cargar_HTML = pd.read_html(Response.text)

print (f'{Cargar_HTML[2].head()}')

print (f'-----------------')

import numpy as np

Array1 = np.array([1, 2, 3])

print (f'{Array1}')
print (f'{Array1.ndim}') # 1
print (f'{Array1.shape}') # 1x3
print (f'{Array1.size}') # 3
print (f'{Array1.dtype}') # int64
print (f'{Array1[0]}')
print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 <= 2]}')

print (f'-----------------')

Array2 = np.array([[6, 1, 0], [3, 6, 9]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 1]}')
print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[Array2 <= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

Sumita1 = np.sum(Array2, axis=0)
Sumita2 = np.sum(Array2, axis=1)
Sumita3 = np.sum(Array2[1, 0:None])
Sumita4 = np.sum(Array2[1, :])

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

print (f'El resultado de la sumatoria es {Sumita1}')
print (f'El resultado de la sumatoria es {Sumita2}')
print (f'El resultado de la sumatoria es {Sumita3}')
print (f'El resultado de la sumatoria es {Sumita4}')

print (f'-----------------')

Array3 = np.array([[['e', 'f', 'l'], ['d', 'x', 'j']],       [['n', 'a', 'v'], ['u', 'o', 's']]])

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
print (f'{Array3[1, 1, 0:None]}')
print (f'{Array3[1, 1, :]}')
print (f'{Array3[1, :, 1]}')
print (f'{Array3[Array3 == "a"]}')

print (f'-----------------')

Array4 = np.array([[[[3, 2, 1], [6, 5, 4]], [[9, 8, 7], [0, 1, 2]]],        [[[4, 5, 6], [7, 8, 9]], [[6, 2, 8], [7, 5, 3]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[0, 1, 0, 0]}')
print (f'{Array4[1, 1, 0, :2]}')
print (f'{Array4[1, 1, 0, 2:]}')
print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[1, 0, 1, ::3]}')
print (f'{Array4[1, 1, 0, 0:None]}')
print (f'{Array4[1, 1, 0, :]}')
print (f'{Array4[0, 1, :, 1]}')
print (f'{Array4[Array4 <= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodados: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[0, 1, 0, 0:None])
Sumita8 = np.sum(Array4_Sorted[1, 0, 0, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'-----------------')

Array_Num1 = np.arange(start=1, stop=11, step=1)
Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El minimo de los numeros es {Array_Num1_Min} y el mayor es {Array_Num1_Max}')

print (f'-----------------')

Array_Num2 = np.arange(25)

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

Array_Num2_Reshape_Column_Min = np.min(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Column_Max = np.max(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Row_Min = np.min(Array_Num2_Reshape, axis=1)
Array_Num2_Reshape_Row_Max = np.max(Array_Num2_Reshape, axis=1)

print (f'Los minimos de las columnas son {Array_Num2_Reshape_Column_Min}')
print (f'Los maximos de las columnas son {Array_Num2_Reshape_Column_Max}')
print (f'Los minimos de las filas son {Array_Num2_Reshape_Row_Min}')
print (f'Los maximos de las filas son {Array_Num2_Reshape_Row_Max}')

print (f'-----------------')

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 1]}')

print (f'-----------------')

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 2]}')

print (f'-----------------')

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 0]}')

print (f'-----------------')

Array_Gen2 = np.full(shape=(5), fill_value = "Fuecoco")

print (f'{Array_Gen2}')

Lista_Array1 = list([])

for elemento in enumerate(Array_Gen2):
    Lista_Array1.append(str(elemento[1]))

print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-----------------')

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[1, 1, 0, 0])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[0, 2]}')

print (f'-----------------')

Tupla_Array = tuple(('Rojo', 'Verde'))
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre' : ['Erick', 'Josue', 'Karlita']})

Array_Gen4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array["Nombre"][0])

print (f'-----------------')

print (f'{Array_Gen4}')

print (f'-----------------')

print (f'{Array_Gen5}')

print (f'-----------------')

print (f'{Array_Gen6}')

print (f'-----------------')

print (f'{Array_Gen6[2]}')

print (f'-----------------')

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

print (f'-----------------')

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')

print (f'-----------------')

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')
print (f'{Array_Random2.ndim}')
print (f'{Array_Random2.shape}')
print (f'{Array_Random2.size}')
print (f'{Array_Random2.dtype}')
print (f'{Array_Random2[0, 1]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

print (f'-----------------')

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

print (f'-----------------')

Array_Num8 = np.arange(20)

print (f'{Array_Num8}')

print (f'-----------------')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

print (f'-----------------')

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-----------------')

Lista_Array2 = list(['Erick', 'Josue', 'Karlita'])

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-----------------')

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1)

Array_Concatenate = np.concatenate([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'-----------------')

Array_Concatenate_Split = np.split(Array_Concatenate, 3)

print (f'{Array_Concatenate_Split[0]}')
print (f'{Array_Concatenate_Split[1]}')
print (f'{Array_Concatenate_Split[2]}')

print (f'-----------------')

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'-----------------')

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-----------------')

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'-----------------')

Array_Num9 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Num9}')

Sumita9 = np.sum(Array_Num9, axis=0)
Sumita10 = np.sum(Array_Num9, axis=1)
Sumita11 = np.sum(Array_Num9[1, 0, 0:None])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')

print (f'-----------------')

Lista_Array3 = ['Erick', 'Josue', 'Karlita', 'Susana', 'Antoniella', 'Roberto']

Ganador1 = np.random.choice(Lista_Array3, size=(1))
Ganador2 = np.random.choice(Lista_Array3, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Array3, size=(2, 3), replace=False)

print (f'El ganador del sorte es {Ganador1}')
print (f'El ganador del sorte es {Ganador2}')
print (f'El ganador del sorte es {Ganador3}')

print (f'-----------------')

Array_Linspace = np.linspace(start=0, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-----------------')
print (f'-----------------')
print (f'-----------------')

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2):
        return Num1 + Num2

    return Sumatoria_Interna(3)

Variable_Sumatoria = Sumatoria_Externa(4)

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

with open (Ruta_Txt, 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(37)}')
    Docu.close()

with open (Ruta_Txt, encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla('Perro', 36, 3.5, False)

print (f'{Funcion_Tupla("Perro", 36, 3.5, False)}')
print (f'{Funcion_Tupla("Perro", 36, 3.5, False)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla("Perro", 36, 3.5, False))}')

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')

Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Variable_Sumatoria, Votante = Variable_Funcion_Tupla[3])

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

print (f'Los numeros pares de la lista son {list(Anonima3)}')

Any_Impar = any(num % 2 != 0 for num in PEPE.Lista_Numeros)

Lista_Impares = [num for num in PEPE.Lista_Numeros if num % 2 != 0]

print (f'{Any_Impar}')
print (f'{Lista_Impares}')

def Primera(Segunda):
    def Tercera(*args):
        return Segunda(*args) - 42

    return Tercera

@Primera
def Operacion(Numero):
    Local = Numero
    return PEPE.Global + Local

print (f'El resultado de la operacion es {Operacion(12)}')

def Externa(Nombre):
    def Interna(Apellido):
        print (f'Mi nombre es {Nombre} {Apellido}')

    return Interna('PEREZ GUTIERREZ')

Externa('ERICK JOSUE')

def Closure_Externa():
    Lista_Closure = list([])
    def Closure_Interna(x):
        Lista_Closure.append(x)

        return Lista_Closure

    return Closure_Interna

Variable_Closure = Closure_Externa()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(24)}')
print (f'{Variable_Closure(37)}')

def Crear_Multiplicador(x):
    def Multiplicador(y):
        return x * y

    return Multiplicador

Variable_Multiplicador1 = Crear_Multiplicador(2)
Variable_Multiplicador2 = Crear_Multiplicador(3)

print (f'El multiplicador 1 es {Variable_Multiplicador1(10)}')
print (f'El multiplicador 2 es {Variable_Multiplicador2(10)}')

def Filtrador(Lista):
    Any_Iterable = any(num % 2 == 0 for num in Lista)
    if (Any_Iterable == True):
        Anonima4 = filter(lambda Num : Num % 2 == 0, Lista)
        Lista_Iterable = [num for num in Lista if num % 2 == 0]

        print (f'Los numeros pares de la lista son {list(Anonima4)} o talvez {Lista_Iterable}')
    else:
        print (f'No hay elementos pares en la lista')


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
        return Segunda(*args, **kwargs) + 1

    return Tercera

@Primera
def Sumatoria3(Num1, Num2):
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(7, 2)}')

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonathan'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)

    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    print (f'Mi nombre es {Nombre} {Apellido}')

Usuario2('Erick', 'Perez')

from Module_Own import Pokemon as Poke

Objeto1 = Poke(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto2 = Poke(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')
Objeto3 = Poke(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro Chorro')

Objeto1.Mostrar()