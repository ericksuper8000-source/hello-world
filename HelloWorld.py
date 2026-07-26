try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado no existe')
    raise

Lista_Elemento1 = [1, 2]
Lista_Elemento1.append(3)
Lista_Elemento1.insert(4, 4)
Lista_Elemento1.extend([5])

def Ejercicio1(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        while (Contador < len(Lista)):
            Contador+= 1
            
    return Contador

Resultado1 = Ejercicio1(Lista_Elemento1)

if (Resultado1 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista tiene un total de {Resultado1} elementos')
    
print (f'-' * 20)

def Ejercicio2(Lista):
    Acumulador_Par = 0
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador_Par += elemento
        else:
            continue
        
    return Acumulador_Par

if (len(Lista_Elemento1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de los elementos pares de la lista es {Ejercicio2(Lista_Elemento1)}')
    
print (f'-' * 20)

def Ejercicio3(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        
        for elemento in Lista:
            Acumulador += elemento
            
    return Acumulador

Resultado3 = Ejercicio3(Lista_Elemento1)

if (Resultado3 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La sumatoria de todos los elementos de la lista es {Resultado3}')
    
print (f'-' * 20)

Lista_Elemento2 = [1, 2, 3, 4, 5]

def Ejercicio4(Lista, Numero):
    Founder = False

    for elemento in Lista:
        if (elemento == Numero):
            Founder = True
            break
        else:
            continue
        
    return Founder

Resultado4 = Ejercicio4(Lista_Elemento2, 2)

if (len(Lista_Elemento2) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado4 == True):
        print (f'El numero 2 fue encontrado')
    else:
        print (f'El numero no fue encontrado')
        
print (f'-' * 20)

def Ejercicio5(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Menore = min(Lista)
        Mayore = max(Lista)
        
    Lista_Resultado = [Menore, Mayore]
    return Lista_Resultado

Resultado5 = Ejercicio5(Lista_Elemento2)

if (Resultado5 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista de numeros es {Resultado5}')
    print (f'El menor de los numeros es {min(Resultado5)}')
    print (f'El mayor de los numeros es {max(Resultado5)}')
    
print (f'-' * 20)

def Ejercicio6(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    return Menore, Mayore

Resultado6 = Ejercicio6(Lista_Elemento2)

if (len(Lista_Elemento2) == 0):
    print (f'Error, la lista esta vacia')
else:
    Menor1, Mayor1 = Resultado6
    print (f'El menor de los numeros es {Menor1}')
    print (f'El mayor de los numeros es {Mayor1}')
    
print (f'-' * 20)

def Ejercicio7(Lista, Numero):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        
        for elemento in Lista:
            if (elemento > Numero):
                Contador += 1
            else:
                continue
            
    return Contador

Resultado7 = Ejercicio7(Lista_Elemento2, 1)

if (Resultado7 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La cantidad de numeros mayores a 1 de la lista es {Resultado7}')
    
print (f'-' * 20)

def Ejercicio8(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Pares = []
        
        for elemento in Lista:
            if (elemento % 2 == 0):
                Lista_Pares.append(elemento)
            else:
                continue

    return Lista_Pares

Resultado8 = Ejercicio8(Lista_Elemento2)

if (Resultado8 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista de elementos pares es {Resultado8}')
    
print (f'-' * 20)

def Ejercicio9(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_ImPares = []
        
        for elemento in Lista:
            if (elemento % 2 != 0):
                Lista_ImPares.append(elemento)
            else:
                continue

    return Lista_ImPares

Resultado8 = Ejercicio9(Lista_Elemento2)

if (Resultado8 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista de elementos impares es {Resultado8}')
    
print (f'-' * 20)

def Ejercicio10(Lista):
    Lista_Mult = []
    
    for elemento in Lista:
        Lista_Mult.append(elemento * 2)
        
    return Lista_Mult

Ejercicio10(Lista_Elemento2)

if (len(Lista_Elemento2) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Elemento2}')
    print (f'Lista Actualizada: {Ejercicio10(Lista_Elemento2)}')
    
print (f'-' * 20)

'''Contador = 0

Lista_Promedios = []

while (Contador < 3):
    while True:
        Numerito1 = input(f'Ingrese el promedio {Contador +1}: ')
        try:
            Numerito2 = float(Numerito1)
            if (Numerito2.is_integer()):
                Lista_Promedios.append(Numerito2)
                break
            else:
                Lista_Promedios.extend([Numerito2])
                break
        except ValueError:
            print (f'Error, ingrese un valor numerico')
    Contador += 1
    
Promedio1 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas elegidas es {round(Promedio1, 2)}')'''

def Ejercicio11(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Impares = []
        Lista_Pares = list([])
        
        for elemento in Lista:
            if (elemento % 2 == 0):
                Lista_Pares.append(elemento)
            else:
                Lista_Impares.extend([elemento])
                
    return Lista_Pares, Lista_Impares

Resultado11 = Ejercicio11(Lista_Elemento2)

if (Resultado11 is None):
    print (f'Error, la lista esta vacia')
else:
    Pares1, Impares1 = Resultado11
    
    print (f'Lista de numeros pares {Pares1}')
    print (f'Lista de numeros impares {Impares1}')
    
print (f'-' * 20)

Lista_Elemento3 = list([5, -6, 0, -1, -3, 0])

def Ejercicio12(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador_Negativo = 0
        Contador_Positivo = 0
        Contador_Ceros = 0
        for elemento in Lista:
            if (elemento > 0):
                Contador_Positivo += 1
            elif (elemento < 0):
                Contador_Negativo += 1
            else:
                Contador_Ceros += 1
                
    return Contador_Positivo, Contador_Negativo, Contador_Ceros

Resultado12 = Ejercicio12(Lista_Elemento3)

if (Resultado12 is None):
    print (f'Error la lista esta vacia')
else:
    Positivos1, Negativos1, Ceros1 = Resultado12
    
    print (f'Positivos: {Positivos1}')
    print (f'Positivos: {Negativos1}')
    print (f'Positivos: {Ceros1}')
    
print (f'-' * 20)

import re

Lista_Elemento4 = [
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
]

def Ejercicio13(Lista):
    Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'
    
    Lista_Correos_Validos = []
    Lista_Correos_Invalidos = list([])
    
    for elemento in Lista:
        Buscar = bool(re.fullmatch(Pattern, elemento))
        if (Buscar == True):
            Lista_Correos_Validos.append(elemento)
        else:
            Lista_Correos_Invalidos.append(elemento)
            
    return Lista_Correos_Validos, Lista_Correos_Invalidos

Ejercicio13(Lista_Elemento4)

if (len(Lista_Elemento4) == 0):
    print (f'Error, la lista esta vacia')
else:
    Validos, Invalidos = Ejercicio13(Lista_Elemento4)
    
    print (f'Correos Validos: {Validos}')
    print (f'Correos InValidos: {Invalidos}')
    
print (f'-' * 20)

def Ejercicio14(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Mayor = Lista[0]
        
        for elemento in Lista:
            if (elemento > Mayor):
                Mayor = elemento
            else:
                continue
            
    return Mayor

Resultado14 = Ejercicio14(Lista_Elemento3)

if (Resultado14 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El mayor de los numeros de la lista es {Resultado14}')
    
print (f'-' * 20)

Lista_Elemento3 = list([5, -6, 0, -1, -3, 0])

def Ejercicio15(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Menor = Lista[0]
        
        for elemento in Lista:
            if (elemento < Menor):
                Menor = elemento
            else:
                continue
            
    return Menor

Resultado15 = Ejercicio15(Lista_Elemento3)

if (Resultado15 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de los numeros de la lista es {Resultado15}')
    
print (f'-' * 20)

Lista_Elemento5 = [-15.5, -8, -3.2, -1, 0, 4, 7.5, 12, 19.1, 25]

def Ejercicio16(Lista):
    Contador_Positivos = 0
    Acumulador_Positivos = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Contador_Positivos += 1
            Acumulador_Positivos += elemento
        else:
            continue
        
    return Contador_Positivos, Acumulador_Positivos

Resultado16 = Ejercicio16(Lista_Elemento5)

if (len(Lista_Elemento5) == 0):
    print (f'Error, la lista esta vacia')
else:
    Total_Positivo, Suma_Positivo = Resultado16
    
    print (f'Total de numeros positivos: {Total_Positivo}')
    print (f'El resultado de sumar los numeros positivos: {Suma_Positivo}')
    
print (f'-' * 20)

Lista_Elemento6 = [65, 70, 54, 80, 69, 66]

def EJercicio17(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador_Aprobados = 0
        Contador_Reprobados = 0
        Acumulador_Aprobados = 0
        
        for elemento in Lista:
            if (elemento >= 70):
                Contador_Aprobados += 1
                Acumulador_Aprobados += elemento
            elif (elemento < 70):
                Contador_Reprobados += 1
                
    return Acumulador_Aprobados, Contador_Aprobados, Contador_Reprobados

Resultado17 = EJercicio17(Lista_Elemento6)

if (Resultado17 is None):
    print (f'Error, la lista esta vacia')
else:
    Suma_Aprobados, Aprobados, Reprobados = Resultado17
    
    print (f'Estudiantes Aprobados: {Aprobados}')
    print (f'Estudiantes Reprobados: {Reprobados}')
    print (f'Suma Notas Aprobadas: {Suma_Aprobados}')
    
print (f'-' * 20)

Lista_Elemento7 = [120, 0, 350, 80, 0, 40, 600]

def Ejercicio18(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Ventas_Reales = 0
        Ventas_No_Reales = 0
        Ventas_Reales_Sum = 0
        
        for elemento in Lista:
            if (elemento > 0):
                Ventas_Reales += 1
                Ventas_Reales_Sum += elemento
            else:
                Ventas_No_Reales += 1
                
    return Ventas_Reales_Sum, Ventas_Reales, Ventas_No_Reales

Resultado18 = Ejercicio18(Lista_Elemento7)

if (Resultado18 is None):
    print (f'Error, la lista esta vacia')
else:
    Sumatoria_Ventas, Total_Ventas, Total_No_Ventas = Resultado18
    
    print (f'Ventas reales que hubo: {Total_Ventas}')
    print (f'Ventas que no se completaron: {Total_No_Ventas}')
    print (f'Total vendido en el dia ${Sumatoria_Ventas}')
    
print (f'-' * 20)

Lista_Elemento8 = [28, 31, 26, 35, 14, 29, 33]

def Ejercicio19(Lista):
    Contador_Mayor_Treinta = 0
    Suma_Mayor_Treinta = 0
    
    for elemento in Lista:
        if (elemento >= 30):
            Contador_Mayor_Treinta += 1
            Suma_Mayor_Treinta += elemento
        else:
            continue
        
    return Contador_Mayor_Treinta, Suma_Mayor_Treinta
    

Resultado19 = Ejercicio19(Lista_Elemento8)

if (len(Lista_Elemento8) == 0):
    print (f'Error, la lista esta vacia')
else:
    Temp_Mayor_Igual_Treinta, Temp_Mayor_Igual_Treinta_Sum = Resultado19
    
    if (Temp_Mayor_Igual_Treinta >= 4):
        print (f'Semana calurosa, tuvimos {Temp_Mayor_Igual_Treinta} dias con temperatura mayor o igual a 30°C')
        print (f'Días calurosos: {Temp_Mayor_Igual_Treinta}')
        print (f'Suma temperaturas: {Temp_Mayor_Igual_Treinta_Sum}')
        print (f'Estado: Semana Calurosa')
    else:
        print (f'La semana no fue calurosa, tuvimos {Temp_Mayor_Igual_Treinta} dias con temperatura mayor o igual a 30°C')
        print (f'Días normales: {Temp_Mayor_Igual_Treinta}')
        print (f'Suma temperaturas: {Temp_Mayor_Igual_Treinta_Sum}')
        print (f'Estado: Semana Regular')
        
print (f'-' * 20)

Lista_Elemento9 = [15, 0, 8, 2, 0, 25, 4]

def Ejercicio20(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador_Agotados = 0
        Contador_Stock_Bajo = 0
        Contador_Stock_Alto = 0
        Stock_Bajo_Sum = 0
        Stock_Alto_Sum = 0
        
        for elemento in Lista:
            if (elemento <= 0):
                Contador_Agotados += 1
            elif (elemento >= 1 and elemento <= 5):
                Contador_Stock_Bajo += 1
                Stock_Bajo_Sum += elemento
            else:
                Contador_Stock_Alto += 1
                Stock_Alto_Sum += elemento
            
    return Contador_Agotados, Contador_Stock_Bajo, Contador_Stock_Alto, Stock_Bajo_Sum, Stock_Alto_Sum

Resultado20 = Ejercicio20(Lista_Elemento9)

if (Resultado20 is None):
    print (f'Error, la lista esta vacia')
else:
    Agotado, Low_Stock, High_Stock, Sum_Low_Stock, Sum_High_Stock = Resultado20
    
    print (f'Productos agotados: {Agotado}')
    print (f'Productos stock bajo: {Low_Stock}')
    print (f'Productos stock alto: {High_Stock}')
    print (f'Sumatoria Productos stock bajo: {Sum_Low_Stock}')
    print (f'Sumatoria Productos stock alto: {Sum_High_Stock}')
    print (f'Sumatoria todos los productos no agotados: {Sum_Low_Stock + Sum_High_Stock}')
    
print (f'-' * 20)

Lista_Elemento10 = [1200, 800, 600, 950, 2000, 700]

def Ejercicio21(Lista):
    Mil_O_Mas = 0
    Mil_O_Menos = 0
    Mil_O_Mas_Sum = 0
    
    for elemento in Lista:
        if (elemento >= 1000):
            Mil_O_Mas += 1
            Mil_O_Mas_Sum += elemento
        else:
            Mil_O_Menos += 1
            
    return Mil_O_Mas, Mil_O_Menos, Mil_O_Mas_Sum

Resultado21 = Ejercicio21(Lista_Elemento10)

if (len(Lista_Elemento10) == 0):
    print (f'Error, la lista esta vacia')
else:
    Result1, Result2, Result3 = Resultado21
    
    print (f'Empleados salario $1000 o mas: {Result1}')
    print (f'Empleados salario menos de $1000: {Result2}')
    print (f'Suma salarios mayores a $1000: ${Result3}')
    
print (f'-' * 20)

Lista_Elemento11 = [12, 8, 5, 0, 7, 0, 10]

def Ejercicio22(Lista):
    Indice1 = 0
    
    for indice, elemento in enumerate(Lista, start=0):
        if (elemento == 0):
            Indice1 = indice
            break
        else:
            continue
        
    if (Indice1 == 0):
        return None
    else:   
        return Indice1

Indice = Ejercicio22(Lista_Elemento11)

if (len(Lista_Elemento11) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Indice is None):
        print (f'No hay ningun producto que actualmente este agotado')
    else:
        print (f'El producto {Lista_Elemento11[Indice]} se encuentra en la posicion {Indice}')
        
print (f'-' * 20)

'''def Ejercicio23(Elemento):
    try:
        Numerito = float(Elemento)
        if (Numerito.is_integer()):
            print (f'Lo que ingresaste fue un numero entero')
            Resultado = 14 * 10 + Numerito
            print (f'El resultado de la operacion es {Resultado}')
        else:
            print (f'Lo que ingresaste fue un numero decimal')
    except ValueError:
        print (f'Error, lo ingresado es texto')

Ejercicio23(PEPE.Flotante1)'''

'''Resultado22 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado22}')'''

'''def Ejercicio23(Texto):
    Consolidado = Texto.replace(' ', '')
    
    if (isinstance(Consolidado, (str))):
        print (f'Lo que ingresaste es un texto')
    else:
        print (f'Error, lo que ingresaste no es texto')
        
    print (f'-' * 20)
    
    if (Consolidado.isalpha()):
        print (f'Lo que ingresaste es un texto')
    else:
        print (f'Error, lo que ingresaste no es texto')
        
    print (f'-' * 20)
    
    try:
        Numerito = float(Consolidado)
        if (Numerito.is_integer()):
            print (f'Lo que ingresaste es un numero entero')
        else:
            print (f'Lo que ingresaste es un numero decimal')
    except ValueError:
        print (f'Lo que ingresaste es texto')

Ejercicio23(PEPE.Flotante3)'''

'''def Ejercicio23(Cadena):
    Lista_Cadena = Cadena.split(' ')
    
    for indice, elemento in enumerate(Lista_Cadena, start=1):
        print (f'{indice} -- {elemento}')
        
    print (f'La cantidad de palabras de la cadena es {Lista_Cadena.__len__()}')

Ejercicio23(PEPE.Flotante4)'''

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Lista.append(Alumno)
        
    return Lista

Listilla = Colegio(Lista_Alumnos)

with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
    Documento_SobreEscribir = Docu.write(f'La lista de alumnos es {Listilla}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()'''
    
print (f'-' * 20)

'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda Num : Num[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes es {Menore}, su edad es {Lista[0][1]} años')
    print (f'El mayor de los estudiantes es {Mayore}, su edad es {Lista[-1][1]} años')

Colegio(Lista_Alumnos)'''

class Persona():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto1 = Persona('Erick Perez')

print (f'Hola, mi nombre es {Objeto1}')

print (f'-' * 20)

class Colores():
    def __init__(self, Colores):
        self.Colores = Colores
        
    def __repr__(self):
        return self.Colores
        
Lista_Colores = [
    Colores('Rojo'),
    Colores('Verde'),
    Colores('Azul')
]

print (f'La lista de colores es {Lista_Colores}')

print (f'-' * 20)

class Inventario1():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto2 = Inventario1()

Objeto2.Productos.extend(['Casa'])
Objeto2.Productos.insert(1, 'Bola')
Objeto2.Productos.append('Piña')

print (f'La cantidad de elementos de la lista es {len(Objeto2)}')

print (f'-' * 20)

class Igualdad():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto3 = Igualdad('Erick Perez')
Objeto4 = Igualdad('Erick Perez')

if (Objeto3 == Objeto4):
    print (f'Ambos objetos son iguales')
else:
    print (f'Error, los objetos no son iguales')
    
print (f'-' * 20)

class Caja():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto5 = Caja(5)
Objeto6 = Caja(3)

print (f'El resultado de la suma es {Objeto5 + Objeto6}')

print (f'-' * 20)

class Inventario2():
    def __init__(self):
        self.Productos = ['Lapicero', 'Tajador', 'Borrador', 'Cuaderno']
        
    def __getitem__(self, Indice):
        return self.Productos[Indice]
        
Objeto7 = Inventario2()

print (f'Producto 1 es {Objeto7[0]}')
print (f'Producto 2 es {Objeto7[1]}')
print (f'Producto 3 es {Objeto7[2]}')
print (f'Producto 4 es {Objeto7[3]}')

print (f'-' * 20)

'''import requests

Primera1 = requests.get('http://127.0.0.1:8006/grupo1/')
Primera2 = Primera1.json()

print (f'{Primera2}')

print (f'-' * 20)

Diccionario_API = {
    'Nombre' : "Erick",
    'Edad' : 37
}

Segunda1 = requests.post('http://127.0.0.1:8006/grupo1/', json=Diccionario_API)
Segunda2 = Segunda1.json()

print (f'{Segunda2}')'''

var1 = '3'

if (var1.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (isinstance(var1, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
try:
    Numerito1 = float(var1)
    if (Numerito1.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var2 = '3.5'

if (isinstance(var2, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Lo ingresado no es un numero decimal')
    
try:
    Numerito2 = float(var2)
    if (Numerito2.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var3 = 3.5

if (isinstance(var3, (int, float))):
    print (f'Lo ingresado es un numero entero o decimal')
else:
    print (f'Error de formato')
    
try:
    Numerito3 = float(var3)
    if (Numerito3.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

import re

Texto1 = "   Hola!!!   mundo@@   123   "

print (f'{Texto1}')

Texto1_Version1 = Texto1.strip()

print (f'{Texto1_Version1}')

Texto1_Version2 = ' '.join(Texto1_Version1.split())

print (f'{Texto1_Version2}')

Texto1_Version3 = Texto1_Version2.lower()

print (f'{Texto1_Version3}')

Texto1_Version4 = re.sub(r'\!|\@|\d+', '', Texto1_Version3)

print (f'{Texto1_Version4}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Fecha1 = '2026-04-01'

Ruta_Csv1 = 'C:\\Repo\\Store.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1}')

print (f'-' * 20)

try:
    Fech1 = datetime.strptime(Fecha1, '%Y-%m-%d').date()
    Fech1_Formateada = pd.to_datetime(Fech1)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato incorrecto')
    
Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrado1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()] #type: ignore

if (Encontrado1.empty):
    print (f'No hay ventas en esta fecha')
else:
    print (f'Genial! Se encontraron ventas en esta fecha')
    
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'En la fecha {Fech1_Formateada}, el producto {Grupo1_Min} vendio {Grupo1_Min_Cant} unidades') #type: ignore
    print (f'En la fecha {Fech1_Formateada}, el producto {Grupo1_Max} vendio {Grupo1_Max_Cant} unidades') #type: ignore
    
    print (f'{Grupo1.count()} clientes compraron en esta fecha')
    
    print (f'La cantidad de productos vendidos en esta fecha fue {Grupo1.sum()}')
    
    Grupo2 = Encontrado1.groupby('product')['TOTALITO'].sum()
    
    print (f'El total de dinero vendido en esta fecha fue de ${Grupo2.sum()}')
    
    Promedio1 = Grupo2.sum() / Grupo1.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de {round(Promedio1, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de {Grupo2.mean()}')
    
print (f'-' * 20)

import re

Texto2 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Texto2_temp = Texto2

Pattern1 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos1 = re.findall(Pattern1, Texto2)

print (f'{Correos1}')

for i, email in enumerate(Correos1, start=1):
    Texto2_temp = Texto2_temp.replace(email, f'SAMPLE{i}')
    
print (f'{Texto2_temp}')

Pattern2 = r'\!|\?|\.{2,}'

Texto2_temp2 = re.sub(Pattern2, '', Texto2_temp)

print (f'{Texto2_temp2}')

for i, email in enumerate(Correos1, start=1):
    Texto2_temp2 = Texto2_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto2_temp2}')

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

'''Contador = 0

Lista_Promedios = []

while (Contador < 3):
    while True:
        Numerito4 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito5 = float(Numerito4)
            if (Numerito5.is_integer()):
                print (f'La nota es un numero entero')
                Lista_Promedios.append(Numerito5)
                break
            else:
                print (f'La nota es un numero decimal')
                Lista_Promedios.extend([Numerito5])
                break
        except ValueError:
            print (f'Error, ingrese un numero')
    Contador += 1
    
Promedio2 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas es {round(Promedio2, 2)}')'''

from Module_Own import Pokemon1 as Poke1

Objeto8 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto9 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto8.Mostrar()

print (f'-' * 20)

Objeto9.Mostrar()

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto10 = Poke_Kid1(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto10)
Objeto10.Mostrar()

print (f'-' * 20)

class Veterinaria():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad} años')
        print (f'Peso: {self.Peso}kgs')
        
class Perro(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        
    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        
Objeto11 = Perro('Chester', 5, 2.8, 'Poodle', 'Hiper-tension')

Veterinaria.Mostrar(Objeto11)
Objeto11.Mostrar()

print (f'-' * 20)

class Gato(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente = Paciente

    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto12 = Gato('Messi', 1.5, 2, 'Gris', 'No')

Veterinaria.Mostrar(Objeto12)
Objeto12.Mostrar()

print (f'-' * 20)

class Pajaro(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto13 = Pajaro('Polly', 31, 0.4, 'Guacamayo', 'Si')

Veterinaria.Mostrar(Objeto13)
Objeto13.Mostrar()

print (f'-' * 20)

class Atacante():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon
        
    def Mostrar(self):
        print (f'Damage: {self.Damage}pts')
        print (f'Weapon: {self.Weapon}')
        
class Defensor():
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
        
Objeto14 = Paladin(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto14.Mostrar()
Atacante.Mostrar(Objeto14)
Defensor.Mostrar(Objeto14)

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
        
Objeto15 = D1()

A1.Mostrar(Objeto15)
B1.Mostrar(Objeto15)
C1.Mostrar(Objeto15)
Objeto15.Mostrar()
E1.Mostrar(Objeto15)

print (f'-' * 20)

class Tarjeta():
    def Pagar(self):
        print (f'El pago se realizo con Tarjeta')
        
class Efectivo():
    def Pagar(self):
        print (f'El pago se realizo con Efectivo')
        
class Cripto():
    def Pagar(self):
        print (f'El pago se realizo con Cripto')
        
Objeto16 = Cripto()
Objeto17 = Efectivo()
Objeto18 = Tarjeta()

Objeto16.Pagar()
Objeto17.Pagar()
Objeto18.Pagar()

print (f'-' * 20)

class Cuenta_Bancaria():
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
        print (f'Tu saldo a la fecha es ${self.__Saldo}')
        
Objeto17 = Cuenta_Bancaria(100)
Objeto17.Depositar(25)
Objeto17.Mostrar()

print (f'Hay una variable privada que contiene tu saldo actual y esta es {Objeto17.Dinero}')

Objeto17.Dinero = '50,000,000'

Objeto17.Mostrar()

print (f'Hay una variable privada que contiene tu saldo actual y esta es {Objeto17.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def General(self):
        pass
    
class Sub_Plantilla(Plantilla):
    def Mostrar(self):
        print (f'Este es el metodo interno')
        
    def General(self):
        print (f'Este es el metodo obligatorio de la plantilla')
        
Objeto19 = Sub_Plantilla()

Objeto19.Mostrar()
Objeto19.General()

print (f'-' * 20)

class Bulbasaur():
    def Elegir(self):
        return f'Bulbasaur'
    
class Treekoo():
    def Elegir(self):
        return f'Treekoo'
    
class Chikorita():
    def Elegir(self):
        return f'Chikorita'
    
class Battle1():
    def __init__(self):
        self.Favorito = Bulbasaur()
        
    def Batallar(self):
        print (f'El retador elegio a {self.Favorito.Elegir()} para la batalla')
        
Objeto20 = Battle1()

Objeto20.Batallar()

print (f'-' * 20)

class Battle2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El retador eligio a {self.Favorito.Elegir()} para la batalla!!!')
        
Criatura1 = Bulbasaur()
Objeto21 = Battle2(Criatura1)
Objeto21.Batallar()

Criatura2 = Treekoo()
Objeto22 = Battle2(Criatura2)
Objeto22.Batallar()

Criatura3 = Chikorita()
Objeto23 = Battle2(Criatura3)
Objeto23.Batallar()

print (f'-' * 20)

import re

Texto3 = 'esto 78 es un hola texto cualquieraa 1, pero hala lo mas importante es 124 @ que querebbbbbbbmos hela saber si esto funciona o no'

Buscar1 = re.search(r'pero', Texto3)

print (f'{Buscar1}')

Buscar2 = re.findall(r'\d+', Texto3)

print (f'{Buscar2}')

Buscar3 = re.fullmatch(r'esto 78 es un hola texto cualquieraa 1, pero hala lo mas importante es 124 \@ que querebbbbbbbmos hela saber si esto funciona o no', Texto3)

if (Buscar3):
    print (f'Los texto son identicos')
else:
    print (f'Error, los textos son diferentes')
    
Buscar4 = re.findall(r'h.la', Texto3)

print (f'{Buscar4}')

Buscar5 = re.findall(r'[a-z]+', Texto3)

print (f'{Buscar5}')

Buscar6 = re.findall(r'^esto', Texto3)
Buscar7 = re.findall(r'o$', Texto3)

print (f'{Buscar6}')
print (f'{Buscar7}')

Buscar8 = re.findall(r'\d{3}\s\W', Texto3)

print (f'{Buscar8}')

Buscar9 = re.findall(r'[ab]{2,4}', Texto3)

print (f'{Buscar9}')

Buscar10 = re.findall(r'[ab]*', Texto3)

print (f'{Buscar10}')

Buscar11 = re.findall(r'(\d{2,4}|h.la)', Texto3)

print (f'{Buscar11}')

'''
{2}
{2,}
{2,4}
+
*
?
'''

Texto4 = 'ericksuper80@hotmail.com'

Pattern3 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.[a-z]{2,}$'

Buscar12 = bool(re.match(Pattern3, Texto4))
if (Buscar12 == True):
    print (f'El correo electronico tiene el formato correcto')
else:
    print (f'Error, formato de correo invalido')
    
print (f'-' * 20)

import re

Texto5 = 'ericksuper80@hotmail.com'

Pattern4 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar13 = bool(re.fullmatch(Pattern4, Texto5))

if (Buscar13 == True):
    print (f'El correo 2 tiene el formato correcto')
else:
    print (f'Error, formato de correo 2 invalido')
    
print (f'-' * 20)

import re

Texto6 = '32'

Pattern5 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar14 = bool(re.fullmatch(Pattern5, Texto6))

if (Buscar14 == True):
    print (f'El numero esta entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

import re

Texto7 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern6 = r'\d{2}\/[0-9]{2,}\/\d{3,4}'

Replacement6 = 'XX/XX/XXXX'

Buscar15 = re.sub(Pattern6, Replacement6, Texto7)

print (f'{Buscar15}')

Pattern7 = r'\+\d{1}\-[0-9]{3,}\-\d{1,3}\-[0-9]{4,}'

Replacement7 = '**TELEFONO**'

Buscar16 = re.sub(Pattern7, Replacement7, Buscar15)

print (f'{Buscar16}')

print (f'-' * 20)

import re

Texto8 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Pattern8 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar17 = re.findall(Pattern8, Texto8)

print (f'{Buscar17}')

print (f'-' * 20)

for elemento in enumerate(Buscar17):
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

import re

Texto9 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Version1
Pattern9 = r'\!|\?|\.{2,}'

Buscar18 = re.sub(Pattern9, '', Texto9)

print (f'{Buscar18}')

print (f'-' * 20)

# Version2

import re

Texto10 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern10 = r'[^a-zA-Z0-9\s]+'

Buscar19 = re.sub(Pattern10, '', Texto10)

print (f'{Buscar19}')

print (f'-' * 20)

# Version3

import re

Texto11 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Texto11_temp1 = Texto11

Pattern11 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Correos2 = re.findall(Pattern11, Texto11)

print (f'{Correos2}')

for i, email in enumerate(Correos2, start=1):
    Texto11_temp1 = Texto11_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto11_temp1}')

Pattern12 = r'\!|\?|\.{2,}|[0-9]{4}\-\d{2,4}'

Texto11_temp2 = re.sub(Pattern12, '', Texto11_temp1)

print (f'{Texto11_temp2}')

for i, email in enumerate(Correos2, start=1):
    Texto11_temp2 = Texto11_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto11_temp2}')

print (f'-' * 20)

var4 = 3.5

if (isinstance(var4, (float))):
    print (f'Numero decimal')
else:
    print (f'Error, lo ingresado no es un numero decimal')
    
try:
    Numerito4 = float(var4)
    if (Numerito4.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var5 = '3'

if (isinstance(var5, (int))):
    print (f'Numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
if (var5.isnumeric()):
    print (f'Numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
try:
    Numerito5 = float(var5)
    if (Numerito5.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

import re

Texto12 = "   Hola!!!   mundo@@   123   "

print (f'{Texto12}')

Texto12_Version1 = Texto12.strip()

print (f'{Texto12_Version1}')

Texto12_Version2 = ' '.join(Texto12_Version1.split())

print (f'{Texto12_Version2}')

Texto12_Version3 = Texto12_Version2.lower()

print (f'{Texto12_Version3}')

Texto12_Version4 = re.sub(r'\!|\@|\d+', '', Texto12_Version3)

print (f'{Texto12_Version4}')

print (f'-' * 20)

def Exception1(Elemento):
    try:
        Numerito = float(Elemento)
        if (Numerito.is_integer()):
            print (f'Lo ingresado es un numero entero')
        else:
            print (f'Lo ingresado es un numero decimal')
    except ValueError:
        print (f'Error, lo que ingresaste no es un numero')

Exception1('hola')

print (f'-' * 20)

def Exception2(Num1, Num2):
    try:
        Sumi = Num1 + Num2
        print (f'El resultado de la sumatoria es {Sumi}')
    except (ValueError, TypeError):
        print (f'Error, ambos elementos deben ser numeritos')

Exception2(12, 'hola')

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor nunca podra ser cero')

Exception3(12, 0)

print (f'-' * 20)

Lista_Exception4 = list(['Erick'])
Lista_Exception4.append('Josue')
Lista_Exception4.insert(2, 'Karlita')

def Exception4(Indice):
    try:
        print (f'El elemento con indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(4)

print (f'-' * 20)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El elemento con llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception5("Votante")

print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nHiena')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo elegido no existe')
    
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
    Documento_Agregar = Docu.write(f'\nOso')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nJirafa Pequeña', '\nJirafa Mediana', '\nJirafa Grande'])
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
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Set_Conjunto_Poke1)])
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

Data_Frame_Concatenate = pd.concat([Data_Frame1, Data_Frame2])

print (f'{Data_Frame1}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'La menor de las edades del dataframe es {Data_Frame_Concatenate_Age.min()}')
print (f'La mayor de las edades del dataframe es {Data_Frame_Concatenate_Age.max()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Inicial1 = elemento["Nombre"]
    Inicial2 = elemento["Edad"]
    
    print (f'Mi nombre es {Inicial1} y mi edad es {Inicial2} años')
    
print (f'-' * 20)

print (f'{Data_Frame_Concatenate}')

Grupo2 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo2_Min = Grupo2.idxmin()
Grupo2_Max = Grupo2.idxmax()
Grupo2_Min_Cant = Grupo2.min()
Grupo2_Max_Cant = Grupo2.max()

print (f'El menor de los miembros del dataframe es {Grupo2_Min} y su edad es {Grupo2_Min_Cant} años')
print (f'El mayor de los miembros del dataframe es {Grupo2_Max} y su edad es {Grupo2_Max_Cant} años')

print (f'La cantidad de personas en el dataframe es {Grupo2.count()}')

print (f'La suma de todas las edades del dataframe es {Grupo2.sum()}')

Data_Frame_Concatenate['TOTALITO'] = Data_Frame_Concatenate['Edad'] * 100

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['TOTALITO'].sum()

print (f'El resultado de las nuevas edades sumadas es {Grupo3.sum()}')

Promedio2 = Grupo3.sum() / Grupo2.count()

print (f'El promedio de la nueva operacion es {round(Promedio2, 2)}')
print (f'El promedio de la nueva operacion es {round(Grupo3.mean(), 2)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate}')

Lista_DataFrame = list(Data_Frame_Concatenate['Nombre'])

Key1 = [f'Key{i}' for i in range(len(Lista_DataFrame))]

print (f'{Lista_DataFrame}')
print (f'{Key1}')

print (f'-' * 20)

Diccionario_DataFrame = dict(zip(Key1, Lista_DataFrame))

print (f'{Diccionario_DataFrame}')
print (f'{Diccionario_DataFrame.keys()}')
print (f'{Diccionario_DataFrame.values()}')
print (f'{Diccionario_DataFrame.items()}')
print (f'{Diccionario_DataFrame["Key1"]}')
print (f'{Diccionario_DataFrame.get("Key2")}')

print (f'-' * 20)

'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = "Nombre", y = "Edad", data=Data_Frame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = "Nombre", y = "Edad", data=Data_Frame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = "Nombre", y = "Edad", data=Data_Frame_Concatenate)

plt.show()'''

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.tail(1)}')

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'La cantidad de Filas son {Filas}')
print (f'La cantidad de Columnas son {Columnas}')

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
Elemento9 = Data_Frame2.iloc[1, :]
Elemento10 = Data_Frame2.iloc[:, 2]

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')
print (f'{Elemento9}')
print (f'{Elemento10}')

print (f'-' * 20)

import pandas as pd
import openpyxl

Ruta_Excel = 'C:\\Repo\\Book.xlsx'

Cargar_Excel = pd.read_excel(Ruta_Excel, engine='openpyxl')

print (f'{Cargar_Excel.head()}')

print (f'-' * 20)

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='cabina')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tarifa', usecols='E:I')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tarifa', usecols='E:I', nrows=1)

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

Grupo4 = Cargar_Excel3_Sorted_Descending.groupby('tres')['cinco'].sum()
Grupo4_Min = Grupo4.idxmin()
Grupo4_Max = Grupo4.idxmax()
Grupo4_Min_Cant = Grupo4.min()
Grupo4_Max_Cant = Grupo4.max()

print (f'El menor de los compas del excel es {Grupo4_Min} y su edad es {Grupo4_Min_Cant} años')
print (f'El mayor de los compas del excel es {Grupo4_Max} y su edad es {Grupo4_Max_Cant} años')

print (f'La cantidad de personas en el excel es {Grupo4.count()}')

print (f'Si sumo todas las edades me da el numero {Grupo4.sum()}')

Promedio3 = Grupo4.sum() / Grupo4.count()

print (f'El promedio de las edades del excel es {round(Promedio3, 2)}')
print (f'El promedio de las edades del excel es {round(Grupo4.mean(), 2)}')

print (f'-' * 20)

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'-' * 20)

print (f'{Cargar_Txt.head()}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv2 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

print (f'-' * 20)

print (f'{Cargar_Csv2.head()}')

print (f'-' * 20)

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Leer_Html)

print (f'{Cargar_Html[2].head()}')

print (f'-' * 20)

Array0 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print (f'{Array0}')
print (f'{Array0[0][::2]}')
print (f'{Array0[1][::3]}')
print (f'{Array0[2][:2]}')
print (f'{Array0[2][2:]}')
print (f'{Array0[0][2:3]}')
print (f'{Array0[:][2]}')
print (f'{Array0[1][0:None]}')
print (f'{Array0[2][:]}')

print (f'-' * 20)

for i in range(len(Array0)):
    for j in range(len(Array0[i])):
        print (f'{Array0[i][j]}')
        
print (f'-' * 20)

import numpy as np

Array1 = np.array([1, 2, 3])

print (f'{Array1}')
print (f'{Array1.ndim}')
print (f'{Array1.shape}')
print (f'{Array1.size}')
print (f'{Array1.dtype}')
print (f'{Array1[2]}')

print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[2:3]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 >= 2]}')

print (f'-' * 20)

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}')
print (f'{Array2.shape}')
print (f'{Array2.size}')
print (f'{Array2.dtype}')
print (f'{Array2[1, 2]}')

print (f'{Array2[1, ::2]}')
print (f'{Array2[0, ::3]}')
print (f'{Array2[0, :2]}')
print (f'{Array2[0, 2:]}')
print (f'{Array2[:, 1]}')
print (f'{Array2[1, 2:3]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[0, :]}')
print (f'{Array2[Array2 >= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[0, 0:None])
Sumita4 = np.sum(Array2_Sorted[0, :])

print (f'El resultado de la sumita es {Sumita1}')
print (f'El resultado de la sumita es {Sumita2}')
print (f'El resultado de la sumita es {Sumita3}')
print (f'El resultado de la sumita es {Sumita4}')

print (f'-' * 20)

Array3 = np.array([[['a', 'b', 'c'], ['d', 'e', 'f']],        [['g', 'h', 'i'], ['j', 'k', 'l']]])

print (f'{Array3}')
print (f'{Array3.ndim}')
print (f'{Array3.shape}')
print (f'{Array3.size}')
print (f'{Array3.dtype}')
print (f'{Array3[0, 1, 1]}')

print (f'{Array3[1, 0, ::2]}')
print (f'{Array3[1, 1, ::3]}')
print (f'{Array3[0, 1, :2]}')
print (f'{Array3[0, 1, 2:]}')
print (f'{Array3[1, :, 1]}')
print (f'{Array3[1, 0, 2:3]}')
print (f'{Array3[1, 1, 0:None]}')
print (f'{Array3[1, 1, :]}')
print (f'{Array3[Array3 == "b"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],                 [[[6, 5, 4], [9, 8, 7]], [[0, 1, 4], [9, 6, 3]]]])

print ((f'{Array4}'))
print ((f'{Array4.ndim}'))
print ((f'{Array4.shape}'))
print ((f'{Array4.size}'))
print ((f'{Array4.dtype}'))
print ((f'{Array4[0, 1, 0, 2]}'))

print ((f'{Array4[1, 0, 0, ::2]}'))
print ((f'{Array4[1, 0, 0, ::3]}'))
print ((f'{Array4[0, 1, 0, :2]}'))
print ((f'{Array4[0, 1, 0, 2:]}'))
print ((f'{Array4[1, 0, :, 1]}'))
print ((f'{Array4[0, 1, 1, 2:3]}'))
print ((f'{Array4[1, 0, 1, 0:None]}'))
print ((f'{Array4[1, 0, 1, :]}'))
print ((f'{Array4[Array4 >= 2]}'))

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita6 = np.sum(Array4_Sorted, axis=0)
Sumita7 = np.sum(Array4_Sorted, axis=1)
Sumita8 = np.sum(Array4_Sorted[0, 1, 1, 0:None])
Sumita9 = np.sum(Array4_Sorted[0, 1, 1, :])

print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')
print (f'El resultado de la sumita es {Sumita9}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=6, step=1) #type: ignore

print (f'{Array_Num1}')

Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El menor de los numeritos es {Array_Num1_Min}')
print (f'El mayor de los numeritos es {Array_Num1_Max}')

print (f'-' * 20)

Array_Num2 = np.arange(start=1, stop=26, step=1) #type: ignore

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

Array_Num2_Reshape_Column_Min = np.min(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Column_Max = np.max(Array_Num2_Reshape, axis=0)
Array_Num2_Reshape_Row_Min = np.min(Array_Num2_Reshape, axis=1)
Array_Num2_Reshape_Row_Max = np.max(Array_Num2_Reshape, axis=1)

print (f'Los menores de las columnas son {Array_Num2_Reshape_Column_Min}')
print (f'Los mayores de las columnas son {Array_Num2_Reshape_Column_Max}')
print (f'Los menores de las filas son {Array_Num2_Reshape_Row_Min}')
print (f'Los mayores de las filas son {Array_Num2_Reshape_Row_Max}')

print (f'-' * 20)

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 2]}')

print (f'{Array_Zeros[0, ::2]}')
print (f'{Array_Zeros[1, ::3]}')
print (f'{Array_Zeros[1, :2]}')
print (f'{Array_Zeros[1, 2:]}')
print (f'{Array_Zeros[:, 2]}')
print (f'{Array_Zeros[1, 2:3]}')
print (f'{Array_Zeros[0, 0:None]}')
print (f'{Array_Zeros[0, :]}')
print (f'{Array_Zeros[Array_Zeros >= 0]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 1]}')

print (f'{Array_Ones[1, ::2]}')
print (f'{Array_Ones[0, ::3]}')
print (f'{Array_Ones[1, :2]}')
print (f'{Array_Ones[1, 2:]}')
print (f'{Array_Ones[:, 0]}')
print (f'{Array_Ones[0, 2:3]}')
print (f'{Array_Ones[1, 0:None]}')
print (f'{Array_Ones[1, :]}')
print (f'{Array_Ones[Array_Ones >= 1]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 1]}')

print (f'{Array_Gen1[1, ::2]}')
print (f'{Array_Gen1[0, ::3]}')
print (f'{Array_Gen1[1, :2]}')
print (f'{Array_Gen1[1, 2:]}')
print (f'{Array_Gen1[:, 1]}')
print (f'{Array_Gen1[0, 2:3]}')
print (f'{Array_Gen1[1, 0:None]}')
print (f'{Array_Gen1[1, :]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value=f'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[3]}')

print (f'{Array_Gen2[::2]}')
print (f'{Array_Gen2[::3]}')
print (f'{Array_Gen2[:2]}')
print (f'{Array_Gen2[2:]}')
print (f'{Array_Gen2[2:4]}')
print (f'{Array_Gen2[0:None]}')
print (f'{Array_Gen2[:]}')

print (f'-' * 20)

Lista_Array1 = []

for elemento in Array_Gen2:
    Lista_Array1.extend([str(elemento)])
    
print (f'{Array_Gen2}')
print (f'{type(Array_Gen2)}')
print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value=Array4[0, 1, 1, 2])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 0]}')

print (f'{Array_Gen3[0, ::2]}')
print (f'{Array_Gen3[1, ::3]}')
print (f'{Array_Gen3[1, :2]}')
print (f'{Array_Gen3[1, 2:]}')
print (f'{Array_Gen3[:, 2]}')
print (f'{Array_Gen3[1, 2:3]}')
print (f'{Array_Gen3[0, 0:None]}')
print (f'{Array_Gen3[0, :]}')

print (f'-' * 20)

Tupla_Array = ('Rojo', 'Verde', 'Negro')
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(2, 3), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(1, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array["Nombre"][1])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'-' * 20)

print (f'{Array_Gen6[3]}')

print (f'-' * 20)

Array_Num3 = np.arange(start=1, stop=10, step=1) #type: ignore
Array_Num4 = np.arange(start=2, stop=11, step=2) #type: ignore
Array_Num5 = np.arange(start=3, stop=31, step=3) #type: ignore
Array_Num6 = np.arange(start=10, stop=21, step=2) #type: ignore
Array_Num7 = np.arange(10) #type: ignore

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
print (f'{Array_Random2.ndim}')
print (f'{Array_Random2.shape}')
print (f'{Array_Random2.size}')
print (f'{Array_Random2.dtype}')
print (f'{Array_Random2[1, 1]}')

print (f'{Array_Random2[0, ::2]}')
print (f'{Array_Random2[1, ::3]}')
print (f'{Array_Random2[1, :2]}')
print (f'{Array_Random2[1, 2:]}')
print (f'{Array_Random2[:, 2]}')
print (f'{Array_Random2[1, 2:3]}')
print (f'{Array_Random2[0, 0:None]}')
print (f'{Array_Random2[0, :]}')
print (f'{Array_Random2[Array_Random2 >= 2]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodados: {Array_Random2_Sorted}')
print (f'Medias: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

Sumita10 = np.sum(Array_Random2_Sorted, axis=0)
Sumita11 = np.sum(Array_Random2_Sorted, axis=1)
Sumita12 = np.sum(Array_Random2_Sorted[1, 0:None])
Sumita13 = np.sum(Array_Random2_Sorted[1, :])

print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')
print (f'El resultado de la sumita es {Sumita13}')

print (f'-' * 20)

Matriz1 = np.array([8, 9, 14])
Matriz2 = np.array([2, 3, 7])

Sum = Matriz1 + Matriz2
Rest = Matriz1 - Matriz2
Mult = Matriz1 * Matriz2
Div = Matriz1 / Matriz2

Array_Random1_Cien = Array_Random1 * 100

print (f'El resultado de la operacion es {Sum}')
print (f'El resultado de la operacion es {Rest}')
print (f'El resultado de la operacion es {Mult}')
print (f'El resultado de la operacion es {Div}')
print (f'El resultado de la operacion es {Array_Random1_Cien}')

print (f'-' * 20)

Array_Num8 = np.arange(start=1, stop=21, step=1) #type: ignore

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Column_Min = np.min(Array_Num8_Reshape, axis=0)
Array_Num8_Reshape_Column_Max = np.max(Array_Num8_Reshape, axis=0)
Array_Num8_Reshape_Row_Min = np.min(Array_Num8_Reshape, axis=1)
Array_Num8_Reshape_Row_Max = np.max(Array_Num8_Reshape, axis=1)

print (f'Los menores de las columnas son {Array_Num8_Reshape_Column_Min}')
print (f'Los mayores de las columnas son {Array_Num8_Reshape_Column_Max}')
print (f'Los menores de las filas son {Array_Num8_Reshape_Row_Min}')
print (f'Los mayores de las filas son {Array_Num8_Reshape_Row_Max}')

print (f'-' * 20)

Lista_Array2 = ["Erick"]
Lista_Array2.append("Josue")
Lista_Array2.insert(1, "Karlita")
Lista_Array2.extend(["Roxana"])

Array5 = np.array(Lista_Array2)

print (f'{Array5}')
print (f'{type(Array5)}')
print (f'{Lista_Array2}')
print (f'{type(Lista_Array2)}')

print (f'-' * 20)

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1) #type: ignore

Array_Concatenate = np.concat([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'-' * 20)

Array_Concatenate_Split1 = np.split(Array_Concatenate, 1)
Array_Concatenate_Split2 = np.split(Array_Concatenate, 2)
Array_Concatenate_Split3 = np.split(Array_Concatenate, 3)
Array_Concatenate_Split4 = np.split(Array_Concatenate, 6)

print (f'{Array_Concatenate_Split1[0]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Split2[0]}')
print (f'{Array_Concatenate_Split2[1]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Split3[0]}')
print (f'{Array_Concatenate_Split3[1]}')
print (f'{Array_Concatenate_Split3[2]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Split4[0]}')
print (f'{Array_Concatenate_Split4[1]}')
print (f'{Array_Concatenate_Split4[2]}')
print (f'{Array_Concatenate_Split4[3]}')
print (f'{Array_Concatenate_Split4[4]}')
print (f'{Array_Concatenate_Split4[5]}')

print (f'-' * 20)

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'-' * 20)

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-' * 20)

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')
print (f'{Array_Random3.ndim}')
print (f'{Array_Random3.shape}')
print (f'{Array_Random3.size}')
print (f'{Array_Random3.dtype}')
print (f'{Array_Random3[1, 0, 2]}')

print (f'{Array_Random3[0, 1, ::2]}')
print (f'{Array_Random3[0, 0, ::3]}')
print (f'{Array_Random3[1, 0, :2]}')
print (f'{Array_Random3[1, 0, 2:]}')
print (f'{Array_Random3[0, :, 0]}')
print (f'{Array_Random3[1, 1, 2:3]}')
print (f'{Array_Random3[0, 0, 0:None]}')
print (f'{Array_Random3[0, 0, :]}')
print (f'{Array_Random3[Array_Random3 >= 2]}')

Array_Random3_Sorted = np.sort(Array_Random3)
Array_Random3_Sorted_Mean = np.mean(Array_Random3_Sorted)
Array_Random3_Sorted_Sum = np.sum(Array_Random3_Sorted)

print (f'Acomodado: {Array_Random3_Sorted}')
print (f'Media: {round(Array_Random3_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random3_Sorted_Sum}')

Sumita14 = np.sum(Array_Random3_Sorted, axis=0)
Sumita15 = np.sum(Array_Random3_Sorted, axis=1)
Sumita16 = np.sum(Array_Random3_Sorted[0, 1, 0:None])
Sumita17 = np.sum(Array_Random3_Sorted[0, 1, :])

print (f'El resultado de la sumita es {Sumita14}')
print (f'El resultado de la sumita es {Sumita15}')
print (f'El resultado de la sumita es {Sumita16}')
print (f'El resultado de la sumita es {Sumita17}')

print (f'-' * 20)

Lista_Sorteo1 = []
Lista_Sorteo1.append("Erick")
Lista_Sorteo1.insert(1, "Josue")
Lista_Sorteo1.extend(["Karlita"])
Set_Conjunto_Sorteo1 = {'Carmelo'}
Set_Conjunto_Sorteo1.add('Susanita')
Set_Conjunto_Sorteo2 = set({'Roxana'})

Set_Conjunto_Sorteo1.update(Set_Conjunto_Sorteo2)

Lista_Sorteo2 = list(Set_Conjunto_Sorteo1)

Lista_Sorteo1.extend([Lista_Sorteo2[0], Lista_Sorteo2[1], Lista_Sorteo2[2]])

print (f'{Lista_Sorteo1}')

Ganador1 = np.random.choice(Lista_Sorteo1, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Sorteo1, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Sorteo1, size=(3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-' * 20)

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

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
    print (f'Fin del experimento')
    
print (f'-' * 20)

def Generadora2():
    for elemento in range(0, 5):
        if (elemento % 2 == 0):
            yield f'The number is Even'
        else:
            yield f'The number is Odd'

Gen2 = Generadora2()

try:
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
except StopIteration:
    print (f'Fin del experimento')

print (f'-' * 20)

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
            continue

Gen3 = Generadora3()

try:
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
except StopIteration:
    print (f'Fin del experimento')

print (f'-' * 20)

Lista_Elemento12 = [1, 2, 3, 4, 5]

def Ejercicio23(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        while (Contador < len(Lista)):
            Contador += 1
            
    return Contador

Resultado22 = Ejercicio23(Lista_Elemento12)

if (Resultado22 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista tiene exactamente {Resultado22} elementos')
    
print (f'-' * 20)

def Ejercicio24(Lista):
    Acumulador = 0
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador += elemento
        else:
            continue
        
    return Acumulador

Resultado23 = Ejercicio24(Lista_Elemento12)

if (len(Lista_Elemento12) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de los numeros pares de la lista es {Resultado23}')
    
print (f'-' * 20)

def Ejercicio25(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        for elemento in Lista:
            Acumulador += elemento
            
    return Acumulador

Resultado24 = Ejercicio25(Lista_Elemento12)

if (Resultado24 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El resultado de sumar todos los elementos de la lista es {Resultado24}')
    
print (f'-' * 20)

def Ejercicio26(Lista, Numero):
    Founder = False

    for elemento in Lista:
        if (elemento == Numero):
            Founder = True
            break
        else:
            continue
        
    return Founder

Resultado25 = Ejercicio26(Lista_Elemento12, 3)

if (len(Lista_Elemento12) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado25 == True):
        print (f'El numero buscado fue encontrado')
    else:
        print (f'Error, el numero no fue encontrado')
        
print (f'-' * 20)

def Ejercicio27(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Min = min(Lista)
        Max = max(Lista)
        
    Lista_Resultado = [Min, Max]
    
    return Lista_Resultado

Resultado26 = Ejercicio27(Lista_Elemento12)

if (Resultado26 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista de numeros es {Resultado26}')
    print (f'El menor de los numeros de la lista es {min(Resultado26)}')
    print (f'El mayor de los numeros de la lista es {max(Resultado26)}')
    
print (f'-' * 20)

def Ejercicio28(Lista):
    Min = min(Lista)
    Max = max(Lista)
    
    return Min, Max

Resultado27 = Ejercicio28(Lista_Elemento12)

if (len(Lista_Elemento12) == 0):
    print (f'Erorr, la lista esta vacia')
else:
    Menor2, Mayor2 = Resultado27
    
    print (f'El menor de los numeros de la lista es {Menor2}')
    print (f'El mayor de los numeros de la lista es {Mayor2}')
    
print (f'-' * 20)

def Ejercicio29(Lista, Numero):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        
        for elemento in Lista:
            if (elemento > Numero):
                Contador += 1
            else:
                continue
            
    return Contador

Resultado28 = Ejercicio29(Lista_Elemento12, 4)

if (Resultado28 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La cantidad de numeros en la lista mayores a 4 es {Resultado28}')
    
print (f'-' * 20)

def Ejercicio30(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Pares = list([])
        
        for elemento in Lista:
            if (elemento % 2 == 0):
                Lista_Pares.extend([elemento])
            else:
                continue
            
    return Lista_Pares

Resultado29 = Ejercicio30(Lista_Elemento12)

if (Resultado29 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Elemento12}')
    print (f'Lista De Pares: {Resultado29}')
    
print (f'-' * 20)

def Ejercicio31(Lista): #type: ignore
    if (len(Lista) == 0):
        return None
    else:
        Lista_ImPares = list([])
        
        for elemento in Lista:
            if (elemento % 2 != 0):
                Lista_ImPares.extend([elemento])
            else:
                continue
            
    return Lista_ImPares

Resultado30 = Ejercicio31(Lista_Elemento12)

if (Resultado30 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Elemento12}')
    print (f'Lista De ImPares: {Resultado30}')
    
print (f'-' * 20)

def Ejercicio31(Lista):
    Lista_Mult = []
    
    for elemento in Lista:
        Lista_Mult.append(elemento * 2)
        
    return Lista_Mult

Resultado30 = Ejercicio31(Lista_Elemento12)

if (len(Lista_Elemento12) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Elemento12}')
    print (f'Lista Actualizada: {Resultado30}')
    
print (f'-' * 20)

Lista_Elemento13 = [65, 70, 54, 80, 69, 66]

def Ejercicio32(Lista): #type: ignore
    if (len(Lista) == 0):
        return None
    else:
        Aprobados = 0
        Reprobados = 0
        Aprobados_Sum = 0
        
        for elemento in Lista:
            if (elemento >= 70):
                Aprobados += 1
                Aprobados_Sum += elemento
            else:
                Reprobados += 1
            
    return Aprobados_Sum, Aprobados, Reprobados

Resultado31 = Ejercicio32(Lista_Elemento13)

if (Resultado31 is None):
    print (f'Error, la lista esta vacia')
else:
    Sumatoria_Aprobados, Aprobados, Reprobados = Resultado31
    
    print (f'Cantidad de aprobados: {Aprobados}')
    print (f'Cantidad de reprobados: {Reprobados}')
    print (f'Sumatoria de aprobados: {Sumatoria_Aprobados}')
    
print (f'-' * 20)

Lista_Elemento14 = [120, 0, 350, 80, 0, 40, 600]

def Ejercicio32(Lista):
    Ventas_Reales = 0
    Ventas_Falsas = 0
    Total_Vendido = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Ventas_Reales += 1
            Total_Vendido += elemento
        else:
            Ventas_Falsas += 1
            
    return Total_Vendido, Ventas_Reales, Ventas_Falsas

Resultado32 = Ejercicio32(Lista_Elemento14)

if (len(Lista_Elemento14) == 0):
    print (f'Error, la lista esta vacia')
else:
    Ventas_Totales, Completadas, No_Completadas = Resultado32
    
    print (f'Cantidad de compras completadas: {Completadas}')
    print (f'Cantidad de compras no completadas: {No_Completadas}')
    print (f'Total de dinero vendido: ${Ventas_Totales}')
    
print (f'-' * 20)

Lista_Elemento15 = [28, 31, 26, 29, 30, 29, 33]

def Ejercicio33(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Temperatura30 = 0
        Temperatura_Menor_30 = 0
        Temperatura30_Sum = 0
        
        for elemento in Lista:
            if (elemento >= 30):
                Temperatura30 += 1
                Temperatura30_Sum += elemento
            else:
                Temperatura_Menor_30 += 1
                
    return Temperatura30_Sum, Temperatura30, Temperatura_Menor_30

Resultado33 = Ejercicio33(Lista_Elemento15)

if (Resultado33 is None):
    print (f'Error, la lista esta vacia')
else:
    Suma30, Mayor30, Menor30 = Resultado33
    if (Mayor30 >= 4):
        print (f'Dias Colurosos: {Mayor30}')
        print (f'Suma de las temperaturas: {Suma30}')
        print (f'Estado: Semana Calurosa')
    else:
        print (f'Dias Colurosos: {Mayor30}')
        print (f'Suma de las temperaturas: {Suma30}')
        print (f'Estado: Semana Regular')
        
print (f'-' * 20)

Lista_Elemento16 = [15, 0, 8, 2, 0, 25, 4]

def Ejercicio34(Lista):
    Agotados = 0
    Stock_Bajo = 0
    Stock_Alto = 0
    Stock_Bajo_Sum = 0
    Stock_Alto_Sum = 0
    for elemento in Lista:
        if (elemento < 0):
            Agotados += 1
        elif (elemento >= 1 and elemento <= 5):
            Stock_Bajo += 1
            Stock_Bajo_Sum += elemento
        elif (elemento > 5):
            Stock_Alto += 1
            Stock_Alto_Sum += elemento
        else:
            continue
        
    return Stock_Alto_Sum, Stock_Alto, Stock_Bajo_Sum, Stock_Bajo, Agotado

Resultado34 = Ejercicio34(Lista_Elemento16)

if (len(Lista_Elemento16) == 0):
    print (f'Error, la lista esta vacia')
else:
    Suma_Stock_Alto2, High_Stock2, Suma_Stock_Bajo2, Low_Stock2, Agotado2 = Resultado34
    
    print (f'Productos con stock alto: {High_Stock2}')
    print (f'Sumatoria de los productos con stock alto: {Suma_Stock_Alto2}')
    print (f'Productos con stock bajo: {Low_Stock2}')
    print (f'Sumatoria de los productos con stock alto: {Suma_Stock_Bajo2}')
    print (f'Productos con stock agotado: {Agotado2}')
    print (f'Productos con stock alto: {Suma_Stock_Alto2 + Suma_Stock_Bajo2}')
    
print (f'-' * 20)

Lista_Elemento17 = [1200, 800, 1500, 1001, 2000, 700]

def Ejercicio35(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Buen_Salario = 0
        Mal_Salario = 0
        Buen_Salario_Sum = 0
        
        for elemento in Lista:
            if (elemento >= 1000):
                Buen_Salario += 1
                Buen_Salario_Sum += elemento
            else:
                Mal_Salario += 1
                
    return Buen_Salario_Sum, Buen_Salario, Mal_Salario

Resultado35 = Ejercicio35(Lista_Elemento17)

if (Resultado35 is None):
    print (f'Error, la lista esta vacia')
else:
    Sumatoria_Salario, Buen_Salario, Mal_Salario = Resultado35
    
    print (f'Sumatoria de todos los buenos salarios: {Sumatoria_Salario}')
    print (f'Trabajadores con buen salario: {Buen_Salario}')
    print (f'Trabajadores con mal salario: {Mal_Salario}')
    
print (f'-' * 20)

Lista_Elemento18 = [12, 8, 5, 3, 7, 0, 10]

def Ejercicio36(Lista):
    Posicion = 0
    for indice, elemento in enumerate(Lista, start=0):
        if (elemento == 0):
            Posicion = indice
            break
        else:
            continue
        
    if (Posicion > 0):
        return Posicion
    else:
        return None

Resultado36 = Ejercicio36(Lista_Elemento18)

if (len(Lista_Elemento18) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado36 is None):
        print (f'No existen productos agotados')
    else:
        print (f'La posicion donde aparece el producto agotado es {Resultado36} y el producto es {Lista_Elemento18[Resultado36]}')
        
print (f'-' * 20)

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola, tu nombre es {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int) -> int:
        return Num1 + Num2
    
    return Sumatoria_Interna(4)

Variable_Sumatoria = Sumatoria_Externa(3)

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
        
    return Usuario_Interno('FEMENINO')

Variable_Usuario = Usuario_Externo()

if (Variable_Usuario == True):
    print (f'YOU ARE A MALE')
else:
    print (f'YOU ARE A FEMALE')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(97)}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 200, 3.5, True)

print (f'{Variable_Funcion_Tupla}')
print (f'{Variable_Funcion_Tupla[2]}')
print (f'{Funcion_Tupla("Perro", 200, 3.5, True)[3]}')
print (f'{type(Funcion_Tupla("Perro", 200, 3.5, True))}')

print (f'-' * 20)

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs:
        print (f'{kwargs[elemento]}')
        
    print (f'-' * 20)
    
    for elemento in kwargs.keys():
        print (f'{elemento}')
    
    print (f'-' * 20)
    
    for elemento in kwargs.values():
        print (f'{elemento}')
    
    print (f'-' * 20)
    
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')
    
Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Objeto10.Cantidad, Votante = Variable_Funcion_Tupla[3])

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos(Saludar_Dos(), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

if (PEPE.Any_Par == True):
    print (f'Hay numeros pares en la lista')
    print (f'Los numeros pares de la lista son {PEPE.Lista_Par}')
    print (f'Los numeros pares de la lista son {list(Anonima3)}')
else:
    print (f'No hay numeros pares en la lista')
    
def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda(*args) - 42
        
    return Tercera
    
@Primera
def Operacion(Num:int) -> int:
    Local = Num
    Resultado = PEPE.GLOBAL + Local
    return Resultado

print (f'El resultado de la operacion es {Operacion(12)}')

def Externa(Nombre):
    def Interna(Apellido:str) -> str:
        return f'{Nombre} {Apellido}'
    
    return Interna("Perez Gutierrez")

print (f'{Externa("Erick Josue")}')

def Closure_Externa():
    Lista_Closure = []
    def Closure_Interna(x):
        Lista_Closure.append(x)
        return Lista_Closure
    
    return Closure_Interna

Variable_Closure = Closure_Externa()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(23)}')
print (f'{Variable_Closure(39)}')

def Closure_Crear_Multiplicador(x):
    def Closure_Mutiplicador(y):
        return x * y
    
    return Closure_Mutiplicador

Mult1 = Closure_Crear_Multiplicador(2)
Mult2 = Closure_Crear_Multiplicador(3)

print (f'El multiplicador es {Mult1(10)}')
print (f'El multiplicador es {Mult2(10)}')

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    if (Any_Impar == True):
        print (f'Si hay numeros impares en la lista')
        Anonima = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impar = [num for num in Lista if num % 2 != 0]
        
        print (f'Los numeros impares de la lista son {list(Anonima)}')
        print (f'Los numeros impares de la lista son {Lista_Impar}')
    else:
        print (f'No hay numeros impares en la lista')

Filtrador(PEPE.Lista_Numeros)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'ANTES')
        Segunda()
        print (f'DESPUES')
        
    return Tercera

@Primera
def Saludar4():
    print (f'Hola Mundo')
    
Saludar4()

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 19
        
    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(12, 7)}')

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonathan'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)
        
    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    return f'{Nombre} {Apellido}'

print (f'-' * 20)

Lista_Elemento19 = [120, 350, 80, 600, 150, 700]

def buscar_primera_venta_mayor(Lista, Monto):
    Posicion = 0
    Contador = 0
    Encontrador = False
    
    while (Contador < len(Lista)):
        if (Lista[Contador] > Monto):
            Posicion = Contador
            Encontrador = True
            break
        Contador+= 1
        
    if (Encontrador == True):
        return Posicion
    else:
        return None
        
Indice = buscar_primera_venta_mayor(Lista_Elemento19, 500)

if (len(Lista_Elemento19) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Indice is None):
        print (f'No se ha encontrado una venta mayor al monto ingresado')
    else:
        print (f'La posicion en la que se encuentra la venta mayor al monton ingresado es {Indice} y el monto encontrado es {Lista_Elemento19[Indice]}')

print (f'-' * 20)

Lista_Elemento20 = [5, 4, 8, 3, 10, 5]

def buscar_primer_repetido(Lista):
    Set_Conjunto1 = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto1):
            return elemento
        else:
            Set_Conjunto1.add(elemento)
        
    return None

Resultado37 = buscar_primer_repetido(Lista_Elemento20)

if (len(Lista_Elemento20) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado37 is None):
        print (f'No se encontro ningun valor repetido')
    else:
        print (f'El primer valor repetido encontrado fue {Resultado37}')
        
print (f'-' * 20)

Lista_Elemento20 = [1, 2, 0]

def buscar_primer_repetido2(Lista):
        Encontrado = False
        for i in range(len(Lista)):
            for j in range(i + 1, len(Lista)):
                if (Lista[i] == Lista[j]):
                    Encontrado = True
                    return Lista[i]

        if (Encontrado == False):
            return None
        
Resultado38 = buscar_primer_repetido2(Lista_Elemento20)

if (len(Lista_Elemento20) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado38 is None):
        print (f'No se encontraron dos numeros iguales')
    else:
        print (f'El primer numero que se repitio fue {Resultado38}')
        
print (f'Mi nombre es {Usuario2("Erick", "Perez")}')

print (f'-' * 20)

Lista_Elemento21 = [120, 350, 80, 600, 150, 700]

def Ejercicio36(Lista, Monto):
    Posicion = 0
    Encontrado = False
    Contador = 0
    while (Contador < len(Lista)):
        if (Lista[Contador] > Monto):
            Posicion = Contador
            Encontrado = True
            break
        else:
            Contador += 1
            continue
        
    if (Encontrado == True):
        return Posicion
    else:
        return None

Resultado39 = Ejercicio36(Lista_Elemento21, 300)

if (len(Lista_Elemento21) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado39 is None):
        print (f'No hay ninguna venta mayor al monto evaluado')
    else:
        print (f'La venta mayor que el monto ingresado esta en la posicion {Resultado39} y la venta fue de {Lista_Elemento21[Resultado39]}')
        
print (f'-' * 20)

Lista_Elemento22 = [10, 1, 3, 4, 2, 1, 6]

def Ejercicio37(Lista):
    Set_Conjunto1 = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto1):
            return elemento
        else:
            Set_Conjunto1.add(elemento)
            
    return None

Resultado40 = Ejercicio37(Lista_Elemento22)

if (len(Lista_Elemento22) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado40 is None):
        print (f'No hay dos numeros iguales en la lista')
    else:
        print (f'El primer numero repetido fue {Resultado40}')
        
print (f'-' * 20)

def Ejercicio38(Lista):
    for i in range(0, len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                return Lista[i]
            else:
                continue
        
    return None

Resultado41 = Ejercicio38(Lista_Elemento22)

if (len(Lista_Elemento22) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado41 is None):
        print (f'No hay dos numeros iguales en la lista')
    else:
        print (f'El primer numero repetido fue {Resultado41}')
        
print (f'-' * 20)

class Inventario3():
    def __init__(self):
        self.Productos = ['Lapiz', 'Cuaderno', 'Borrador']
        
    def __getitem__(self, Indice):
        return self.Productos[Indice]
        
Objeto24 = Inventario3()

print (f'El elemento es {Objeto24[0]}')
print (f'El elemento es {Objeto24[1]}')
print (f'El elemento es {Objeto24[2]}')

print (f'-' * 20)

Lista_Elemento23 = list([1, 2, 3, 4, 5])

def Ejercicio39(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        
        while (Contador < len(Lista)):
            Contador += 1
            
    return Contador

Resultado42 = Ejercicio39(Lista_Elemento23)

if (Resultado42 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero de elementos en la lista es {Resultado42}')
    
print (f'-' * 20)

def Ejercicio40(Lista):
    Acumulador = 0
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador += elemento
        else:
            continue
        
    return Acumulador

Resultado43 = Ejercicio40(Lista_Elemento23)

if (len(Lista_Elemento23) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de los numeros pares de la lista es {Resultado43}')
    
print (f'-' * 20)

def Ejercicio41(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        
        for elemento in Lista:
            Acumulador += elemento
            
    return Acumulador

Resultado44 = Ejercicio41(Lista_Elemento23)

if (Resultado44 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El resultado de sumar todos los elementos de la lista es {Resultado44}')
    
print (f'-' * 20)

def Ejercicio42(Lista, Numero):
    for elemento in Lista:
        if (elemento == Numero):
            return elemento
        else:
            continue
        
    return None

Resultado45 = Ejercicio42(Lista_Elemento23, 3)

if (len(Lista_Elemento23) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado45 is None):
        print (f'El numero buscado no fue encontrado')
    else:
        print (f'El numero 3 fue encontrado en la lista')
        
print (f'-' * 20)

def Ejercicio43(Lista, Numero):
    if (len(Lista) == 0):
        return None
    else:
        Founder = False

        for elemento in Lista:
            if (elemento == Numero):
                Founder = True
                break
            else:
                continue
            
    return Founder

Resultado46 = Ejercicio43(Lista_Elemento23, 3)

if (Resultado46 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado46 == True):
        print (f'El numero buscado fue encontrado')
    else:
        print (f'Error, el numero buscado no aparecio en la lista')
        
print (f'-' * 20)

def Ejercicio44(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    Lista_Resultado = [Menore, Mayore]
    
    return Lista_Resultado

Resultado47 = Ejercicio44(Lista_Elemento23)

if (len(Lista_Elemento23) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista de numeros es {Resultado47}')
    print (f'El menor de los numeros es {min(Resultado47)}')
    print (f'El mayor de los numeros es {max(Resultado47)}')
    
print (f'-' * 20)

def Ejercicio45(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Menore = min(Lista)
        Mayore = max(Lista)
        
    return Mayore, Menore

Resultado47 = Ejercicio45(Lista_Elemento23)

if (Resultado47 is None):
    print (f'Error, la lista esta vacia')
else:
    Mayor3, Menor3 = Resultado47
    print (f'El menor de los numeros es {Menor3}')
    print (f'El mayor de los numeros es {Mayor3}')
    
print (f'-' * 20)

def Ejercicio46(Lista, Numero):
    Contador = 0
    
    for elemento in Lista:
        if (elemento > Numero):
            Contador += 1
        else:
            continue
        
    return Contador

Resultado48 = Ejercicio46(Lista_Elemento23, 2)

if (len(Lista_Elemento23) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La cantidad de numeros mayores que 2 es {Resultado48}')
    
print (f'-' * 20)

def Ejercicio47(Lista, Numero):
    Contador = 0
    
    for elemento in Lista:
        if (elemento < Numero):
            Contador += 1
        else:
            continue
        
    return Contador

Resultado49 = Ejercicio47(Lista_Elemento23, 1)

if (len(Lista_Elemento23) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La cantidad de numeros menores que 1 es {Resultado49}')
    
print (f'-' * 20)

def Ejercicio48(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Pares = list([])
        
        for elemento in Lista:
            if (elemento % 2 == 0):
                Lista_Pares.append(elemento)
            else:
                continue
            
    return Lista_Pares

Resultado50 = Ejercicio48(Lista_Elemento23)

if (Resultado50 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista de numeros pares es {Resultado50}')
    
print (f'-' * 20)

def Ejercicio49(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_ImPares = list([])
        
        for elemento in Lista:
            if (elemento % 2 != 0):
                Lista_ImPares.append(elemento)
            else:
                continue
            
    return Lista_ImPares

Resultado51 = Ejercicio49(Lista_Elemento23)

if (Resultado51 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista de numeros impares es {Resultado51}')
    
print (f'-' * 20)

def Ejercicio50(Lista):
    Lista_Mult = []
    
    for elemento in Lista:
        Lista_Mult.append(elemento * 2)
        
    return Lista_Mult

Resultado52 = Ejercicio50(Lista_Elemento23)

if (len(Lista_Elemento23) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Elemento23}')
    print (f'Lista Actualizada: {Resultado52}')
    
print (f'-' * 20)

'''Lista_Promedios = list([])

Contador = 0

while (Contador < 3):
    while True:
        Numerito6 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito7 = float(Numerito6)
            if (Numerito7.is_integer()):
                print (f'Lo ingresado fue un numero entero')
                Lista_Promedios.append(Numerito7)
                break
            else:
                print (f'Lo ingresado fue un numero decimal')
                Lista_Promedios.append(Numerito7)
                break
        except ValueError:
            print (f'Error, ingrese un numero!!!')
    Contador+= 1
    
Promedio4 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas ingresadas es {round(Promedio4, 2)}')'''

def Ejercicio51(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Pares = []
        Lista_Impares = []
        
        for elemento in Lista:
            if (elemento % 2 == 0):
                Lista_Pares.append(elemento)
            else:
                Lista_Impares.extend([elemento])
                
    return Lista_Pares, Lista_Impares

Resultado53 = Ejercicio51(Lista_Elemento23)

if (Resultado53 is None):
    print (f'Error, la lista esta vacia')
else:
    Pares2, Impares2 = Resultado53
    
    print (f'Lista de numeros pares: {Pares2}')
    print (f'Lista de numeros impares: {Impares2}')
    
print (f'-' * 20)

Lista_Elemento24 = [5, -6, 0, -4, -3, 0]

def Ejercicio52(Lista):
    Negativo = 0
    Positivo = 0
    Cero = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Positivo += 1
        elif (elemento < 0):
            Negativo += 1
        else:
            Cero += 1
            
    return Positivo, Negativo, Cero

Resultado54 = Ejercicio52(Lista_Elemento24)

if (len(Lista_Elemento24) == 0):
    print (f'Error, la lista esta vacia')
else:
    Positivos2, Negativos2, Ceros2 = Resultado54
    
    print (f'Positivos Contabilizados: {Positivos2}')
    print (f'Negativos Contabilizados: {Negativos2}')
    print (f'Ceros Contabilizados: {Ceros2}')
    
print (f'-' * 20)

import re

Lista_Elemento25 = [
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
]

def Ejercicio53(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Validos = []
        Lista_Invalidos = list([])
        
        Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'
        
        for elemento in Lista:
            Buscar = bool(re.fullmatch(Pattern, elemento))
            if (Buscar == True):
                Lista_Validos.append(elemento)
            else:
                Lista_Invalidos.extend([elemento])
                
        return Lista_Validos, Lista_Invalidos

Resultado55 = Ejercicio53(Lista_Elemento25)

if (Resultado55 is None):
    print (f'Error, la lista esta vacia')
else:
    Correos_Validos, Correos_Invalidos = Resultado55
    
    print (f'Lista de correos validos: {Correos_Validos}')
    print (f'Lista de correos invalidos: {Correos_Invalidos}')
    
print (f'-' * 20)

def Ejercicio54(Lista):
    Temporal = Lista[0]
    for elemento in Lista:
        if (elemento > Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

Resultado56 = Ejercicio54(Lista_Elemento24)

if (len(Lista_Elemento22) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero mas alto de la lista es {Resultado56}')
    
print (f'-' * 20)

def Ejercicio55(Lista):
    Temporal = Lista[0]
    for elemento in Lista:
        if (elemento < Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

Resultado57 = Ejercicio55(Lista_Elemento24)

if (len(Lista_Elemento22) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero mas bajo de la lista es {Resultado57}')
    
print (f'-' * 20)

Lista_Elemento26 = [-15.5, -8, -3.2, -1, 0, 4, 7.5, 12, 19.1, 25]

def Ejercicio56(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador_Positivos = 0
        Sumatoria_Positivos = 0
        
        for elemento in Lista:
            if (elemento > 0):
                Contador_Positivos += 1
                Sumatoria_Positivos += elemento
            else:
                continue
            
    return Contador_Positivos, Sumatoria_Positivos

Resultado58 = Ejercicio56(Lista_Elemento26)

if (Resultado58 is None):
    print (f'Error, la lista esta vacia')
else:
    Positivos3, Sumatoria_Positivos = Resultado58
    
    print (f'La cantidad de numeros positivos en la lista es {Positivos3}')
    print (f'El resultado de sumar todos los numeros positivos de la lista es {Sumatoria_Positivos}')
    
print (f'-' * 20)

Lista_Elemento27 = [65, 70, 54, 80, 69, 66]

def Ejercicio57(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Aprobados = 0
        Reprobados = 0
        Aprobados_Sum = 0
        for elemento in Lista:
            if (elemento >= 70):
                Aprobados += 1
                Aprobados_Sum += elemento
            else:
                Reprobados += 1
                
    return Aprobados, Reprobados, Aprobados_Sum

Resultado59 = Ejercicio57(Lista_Elemento27)

if (Resultado59 is None):
    print (f'Error de codigo')
else:
    Aprobados2, Reprobados2, Suma_Aprobados2 = Resultado59
    
    print (f'La cantidad de estudiantes aprobados es {Aprobados2}')
    print (f'La cantidad de estudiantes reprobados es {Reprobados2}')
    print (f'La suma de las notas aprobadas es {Suma_Aprobados2}')
    
print (f'-' * 20)

Lista_Elemento28 = [120, 0, 350, 80, 0, 40, 600]

def Ejercicio58(Lista):
    Cliente_Compro = 0
    Cliente_No_Compro = 0
    Cliente_Compro_Total = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Cliente_Compro += 1
            Cliente_Compro_Total += elemento
        else:
            Cliente_No_Compro += 1
            
    return Cliente_Compro, Cliente_No_Compro, Cliente_Compro_Total

Resultado60 = Ejercicio58(Lista_Elemento28)

if (len(Lista_Elemento28) == 0):
    print (f'Error, la lista esta vacia')
else:
    Venta, No_Venta, Total_Ventas = Resultado60
    
    print (f'Cantidad de ventas completadas {Venta}')
    print (f'Cantidad de ventas no completadas {No_Venta}')
    print (f'Total vendido en el periodo ${Total_Ventas}')
    
print (f'-' * 20)

Lista_Elemento29 = [28, 31, 26, 35, 19, 29, 33]

def Ejercicio59(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Temp_Mayor_Igual_30 = 0
        Temp_Mayor_Igual_30_Sum = 0
        for elemento in Lista:
            if (elemento >= 30):
                Temp_Mayor_Igual_30 += 1
                Temp_Mayor_Igual_30_Sum += elemento
            else:
                continue
            
    return Temp_Mayor_Igual_30, Temp_Mayor_Igual_30_Sum

Resultado61 = Ejercicio59(Lista_Elemento29)

if (Resultado61 is None):
    print (f'Error, la lista esta vacia')
else:
    Temperatura, Suma_Temperatura = Resultado61
    if (Temperatura >= 4):
        print (f'Días calurosos: {Temperatura}')
        print (f'Suma de las temperaturas: {Suma_Temperatura}')
        print (f'Estado: Semana calurosa')
    else:
        print (f'Días calurosos: {Temperatura}')
        print (f'Suma de las temperaturas: {Suma_Temperatura}')
        print (f'Estado: Semana normal')
        
print (f'-' * 20)

Lista_Elemento30 =  [12, 8, 5, 1, 7, 6, 10]

def Ejercicio60(Lista):
    Posicion = 0
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] == 0):
            Posicion = Contador
            return Posicion
        Contador+= 1
        
    return None

Resultado62 = Ejercicio60(Lista_Elemento30)

if (len(Lista_Elemento30) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado62 is None):
        print (f'No hay productos agotados en el inventario')
    else:
        print (f'El primer producto agotado se encuentra en la posicion {Resultado62} -- {Lista_Elemento30[Resultado62]}')
        
print (f'-' * 20)

Lista_Elemento31 = [120, 350, 80, 600, 150, 550]

def Ejercicio61(Lista, Monto):
    Posicion = 0
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] > Monto):
            Posicion = Contador
            return Posicion
        Contador += 1
        
    return None

Resultado63 = Ejercicio61(Lista_Elemento31, 600)

if (len(Lista_Elemento31) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado63 is None):
        print (f'En la lista no hay ningun numero de ventas superior al monto ingresado por el usuario')
    else:
        print (f'La venta mayor al monto ingresado esta en la posicion {Resultado63} y el elemento de la lista en esa posicion es {Lista_Elemento31[Resultado63]}')
        
print (f'-' * 20)

Lista_Elemento32 = [10, 7, 1, 4, 3, 5, 6]

def Ejercicio62(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            
    return None

Resultado64 = Ejercicio62(Lista_Elemento32)

if (len(Lista_Elemento32) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado64 is None):
        print (f'No encontramos dos numeros iguales en la lista')
    else:
        print (f'El primer numero igual que se encontro en la lista es {Resultado64}')
        
print (f'-' * 20)

Lista_Elemento33 = [10, 1, 2, 4, 3, 5, 6]

def Ejercicio63(Lista):
    for i in range(0, len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                return Lista[i]
            else:
                continue
            
    return None

Resultado65 = Ejercicio63(Lista_Elemento33)

if (len(Lista_Elemento33) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado65 is None):
        print (f'No encontramos dos numeros iguales en la lista')
    else:
        print (f'El primer numero igual que se encontro en la lista es {Resultado65}')
        
print (f'-' * 20)

from Module_Own import Pokemon2 as Poke2

Objeto25 = Poke2(PEPE.Diccionario_Poke["Poke1"], 'Electrico', 'Impact Trueno')
Objeto26 = Poke2(PEPE.Diccionario_Poke["Poke2"], 'Roca', 'Sismo')

Objeto25.Mostrar()

print (f'-' * 20)

Objeto26.Mostrar()

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto27 = Poke_Kid2(PEPE.Diccionario_Poke["Poke3"], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto27)
Objeto27.Mostrar()

print (f'-' * 20)

class Camara():
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada')
        
class Reproductor_Musica():
    def Reproducir_Musica(self):
        print (f'La musica fue reproducida')
        
class Smartphone(Camara, Reproductor_Musica):
    def Encender_Smartphone(self):
        print (f'El smartphone fue encendido')
        
Objeto28 = Smartphone()

Objeto28.Encender_Smartphone()
Objeto28.Reproducir_Musica()
Objeto28.Tomar_Fotografia()

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
        
Objeto29 = Perro2('Chester', 5, 3.5, 'Poodle', 'Hipertension')

Veterinaria2.Mostrar(Objeto29)
Objeto29.Mostrar()

print (f'-' * 20)

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto30 = Gato2('Messi', 1.5, 2, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto30)
Objeto30.Mostrar()

print (f'-' * 20)

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto31 = Pajaro2('Polly', 31, 0.4, 'Guacamaya', 'Si')

Veterinaria2.Mostrar(Objeto31)
Objeto31.Mostrar()

print (f'-' * 20)

class Atacante2():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon
        
    def Mostrar(self):
        print (f'Damage: {self.Damage}pts')
        print (f'Weapon: {self.Weapon}')
        
class Defensor2():
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life

    def Mostrar(self):
        print (f'Healing: {self.Healing}pts')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}pts')
        
class Paladin2(Atacante2, Defensor2):
    def __init__(self, Damage, Weapon, Healing, Potion, Life, Name):
        Atacante2.__init__(self, Damage, Weapon)
        Defensor2.__init__(self, Healing, Potion, Life)
        self.Name = Name
        
    def Mostrar(self):
        print (f'Name: {self.Name}')
        
Objeto32 = Paladin2(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto32.Mostrar()
Atacante2.Mostrar(Objeto32)
Defensor2.Mostrar(Objeto32)

print (f'-' * 20)

Hija_Padre = issubclass(Poke_Kid2, Poke2)

print (f'{Hija_Padre}')

Hija_Padre2 = issubclass(Poke_Kid1, Poke2)

print (f'{Hija_Padre2}')

print (f'-' * 20)

Instancia1 = isinstance(Objeto32, Paladin2)
Instancia2 = isinstance(Objeto32, Defensor2)
Instancia3 = isinstance(Objeto32, Atacante2)
Instancia4 = isinstance(Objeto32, Defensor)

print (f'{Instancia1}')
print (f'{Instancia2}')
print (f'{Instancia3}')
print (f'{Instancia4}')

print (f'-' * 20)

class A2():
    def Mostrar(self):
        print (f'Hola nuevamente A2')
        
class E2():
    def Mostrar(self):
        print (f'Hola nuevamente E2')
        
class B2(E2):
    def Mostrar(self):
        print (f'Hola nuevamente B2')
        
class C2(A2):
    def Mostrar(self):
        print (f'Hola nuevamente C2')
        
class D2(B2, C2):
    def Mostrar(self):
        print (f'Hola nuevamente D2')
        
Objeto33 = D2()

A2.Mostrar(Objeto33)
B2.Mostrar(Objeto33)
C2.Mostrar(Objeto33)
Objeto33.Mostrar()
E2.Mostrar(Objeto33)

print (f'-' * 20)

class Efectivo2():
    def Pagar(self):
        print (f'El pago se realizo en Efectivo')
        
class Tarjeta2():
    def Pagar(self):
        print (f'El pago se realizo en Tarjeta')
        
class Cripto2():
    def Pagar(self):
        print (f'El pago se realizo en Cripto')
        
Objeto34 = Cripto2()
Objeto35 = Tarjeta2()
Objeto36 = Efectivo2()

Objeto34.Pagar()
Objeto35.Pagar()
Objeto36.Pagar()

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
        print (f'Su saldo a la fecha es de ${self.__Saldo}')
        
Objeto37 = Cuenta_Bancaria2(100)
Objeto37.Depositar(25)
Objeto37.Mostrar()

print (f'Hay una variable que es privada por tener informacion financiera de clientes y esta es {Objeto37.Dinero}')

Objeto37.Dinero = '50,000,000'

Objeto37.Mostrar()

print (f'Hay una variable que es privada por tener informacion financiera de clientes y esta es {Objeto37.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla2(Plantilla2):
    def Mostrar(self):
        print (f'Este es un metodo interno')
        
    def General(self):
        print (f'Este metodo es el que pertenece a la plantilla abstracta')
        
Objeto38 = Sub_Plantilla2()

Objeto38.Mostrar()
Objeto38.General()

class Cocina(ABC):
    @abstractmethod
    def Hornear(self):
        pass

class Pizza(Cocina):
    def Marinar(self):
        print (f'En este paso preparamos la salsa de la pizza')
        
    def Amasar(self):
        print (f'En este paso amasamos la masa y agregamos los ingredientes')
        
    def Hornear(self):
        print (f'Este es un paso obligatorio y aqui horneamos la pizza')
        
Objeto39 = Pizza()

Objeto39.Marinar()
Objeto39.Amasar()
Objeto39.Hornear()

print (f'-' * 20)

class Chocolate():
    def Elegir(self):
        return f'Chocolate'
    
class Vainilla():
    def Elegir(self):
        return f'Vainilla'
    
class Fresa():
    def Elegir(self):
        return f'Fresa'
    
class Pastel1():
    def __init__(self):
        self.Favorito = Chocolate()
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Objeto40 = Pastel1()

Objeto40.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Ingrediente1 = Chocolate()
Objeto41 = Pastel2(Ingrediente1)
Objeto41.Hornear()

Ingrediente2 = Vainilla()
Objeto42 = Pastel2(Ingrediente2)
Objeto42.Hornear()

Ingrediente3 = Fresa()
Objeto43 = Pastel2(Ingrediente3)
Objeto43.Hornear()

print (f'-' * 20)

class Usuario3():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto42 = Usuario3('Erick Perez')

print (f'Hola {Objeto42}')

print (f'-' * 20)

class Colores2():
    def __init__(self, Color):
        self.Color = Color
        
    def __repr__(self):
        return self.Color
        
Lista_Colores2 = [
    Colores2('Rojo'),
    Colores2('Amarillo'),
    Colores2('Azul')
]

print (f'Lista de colores: {Lista_Colores2}')

print (f'-' * 20)

class Inventario4():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)

Objeto43 = Inventario4()

Objeto43.Productos.append('Casa')
Objeto43.Productos.insert(1, 'Sillon')
Objeto43.Productos.extend(['Bola'])

print (f'La cantidad de productos de la lista es {len(Objeto43)}')

print (f'-' * 20)

class Igualdad2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto44 = Igualdad2('Erick')
Objeto45 = Igualdad2('Erick')

if (Objeto44 == Objeto45):
    print (f'Los objetos son iguales')
else:
    print (f'Error, los objetos no son iguales')

print (f'-' * 20)

class Caja2():
    def __init__(self, Numero):
        self.Numero = Numero
        
    def __add__(self, Otro):
        return self.Numero + Otro.Numero

Objeto46 = Caja2(5)
Objeto47 = Caja2(3)

print (f'El resultado de la sumatoria es {Objeto46 + Objeto47}')

print (f'-' * 20)

class Obtener():
    def __init__(self):
        self.Nombres = ['Erick', 'Josue', 'Karlita']
        
    def __getitem__(self, Indice):
        return self.Nombres[Indice]
        
Objeto48 = Obtener()

print (f'{Objeto48[0]}')
print (f'{Objeto48[1]}')
print (f'{Objeto48[2]}')

print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un
Long
String'''

variable4 = Objeto25.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = True, Objeto27.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke3"]}')

print (f'Mi nombre completo es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Sumatoria2(Anonima2(4), 1, 2)}, {Objeto26.Cantidad} o incluso {Anonima2(60)} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)
print (f'Josue' in PEPE.Lista1)
print (f'Gary' not in PEPE.Tupla_Poke)
print (f'{PEPE.Diccionario_Poke["Poke2"]}' in PEPE.Set_Conjunto_Poke1)

print (f'-' * 20)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables y al mismo tiempo es una declaracion snake case: {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto26.Cantidad, Sumatoria2(1, Anonima2(2), 1, 1))

print (f'El Cociente es {Cociente}')
print (f'El Residuo es {Residuo}')

print (f'{PEPE.Lista2}')
print (f'{PEPE.Lista2[::2]}')
print (f'{PEPE.Lista2[::3]}')
print (f'{PEPE.Lista2[2:3]}')
print (f'{PEPE.Lista2[0:None]}')
print (f'{PEPE.Lista2[:]}')

print (f'{Lista_Uno[2]} eso que ves ahi es un {PEPE.Lista2[2]} ? ')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, 200, 100)

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

print (f'{Lista_Uno_Copia}')
print (f'La lista 1 tiene {len(Lista_Uno_Copia)} elementos')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'{dir(PEPE)}')

print (f'-' * 20)

class Persona1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto49 = Persona1('Erick Perez')

print (f'Mi nombre es {Objeto49}')

print (f'-' * 20)

class Colores3():
    def __init__(self, Colores):
        self.Colores = Colores
        
    def __repr__(self):
        return self.Colores
    
    def __len__(self):
        return len(self.Colores)

Lista_Colores3 = list([
    Colores3('Rojo'),
    Colores3('Amarillo'),
    Colores3('Gris')
])

print (f'La lista de colores es {Lista_Colores3}')
print (f'La cantidad de elementos de la lista es {len(Lista_Colores3)}')

print (f'-' * 20)

class Inventario5():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto50 = Inventario5()

Objeto50.Productos.append('Lapicero')
Objeto50.Productos.insert(1, 'Cuaderno')
Objeto50.Productos.extend(['Borrador'])

print (f'La cantidad de elementos que tiene la lista es {len(Objeto50)}')

print (f'-' * 20)

class Igualdad3():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto51 = Igualdad3('Panda Rojo')
Objeto52 = Igualdad3('Panda Rojo')

if (Objeto51 == Objeto52):
    print (f'Los objetos son iguales')
else:
    print (f'Error, los objetos no son iguales')
    
print (f'-' * 20)

class Caja3():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto53 = Caja3(5)
Objeto54 = Caja3(3)

print (f'El resultado de la sumatoria es {Objeto53 + Objeto54}')

print (f'-' * 20)

class Productos():
    def __init__(self):
        self.Lista = ['Lapicero', 'Cuaderno', 'Borrador']
        
    def __getitem__(self, Indice):
        return self.Lista[Indice]
        
Objeto55 = Productos()

print (f'El producto en la posicion 0 es {Objeto55[0]}')
print (f'El producto en la posicion 1 es {Objeto55[1]}')
print (f'El producto en la posicion 2 es {Objeto55[2]}')

print (f'-' * 20)

Lista_Elemento34 = [120, 350, 80, 600, 150, 700]

def Ejercicio64(Lista, Monto):
    Posicion = 0
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] > Monto):
            Posicion = Contador
            return Posicion
        Contador += 1
        
    return None

Resultado66 = Ejercicio64(Lista_Elemento34, 800)

if (len(Lista_Elemento34) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado66 is None):
        print (f'No se encontro ninguna venta superior al monto ingresado')
    else:
        print (f'La posicion donde aparece la venta superior al monto es {Resultado66} y el monto en cuestion es {Lista_Elemento34[Resultado66]}')
        
print (f'-' * 20)

Lista_Elemento35 = [10, 1, 2, 4, 3, 5, 6]

def Ejercicio65(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            
    return None

Resultado67 = Ejercicio65(Lista_Elemento35)

if (len(Lista_Elemento35) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado67 is None):
        print (f'No se encontraron dos elementos iguales en la lista')
    else:
        print (f'El primer numero repetido que aparece en la lista es {Resultado67}')

print (f'-' * 20)

Lista_Elemento36 = [10, 1, 2, 4, 3, 5, 6]

def Ejercicio66(Lista):
    for i in range(0, len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                return Lista[j]
            else:
                continue
            
    return None

Resultado68 = Ejercicio65(Lista_Elemento36)

if (len(Lista_Elemento36) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado68 is None):
        print (f'No se encontraron dos elementos iguales en la lista')
    else:
        print (f'El primer numero repetido que aparece en la lista es {Resultado68}')
        
print (f'-' * 20)

Tupla1 = ('Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde')

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Green', 'Blue'))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{Tupla1[1]}')

Set_Conjunto1 = {'Roca', Objeto26.Tipo, Objeto26.Tipo, Objeto26.Tipo, Objeto26.Tipo, Objeto26.Tipo}

print (f'{Set_Conjunto1}')
Set_Conjunto1.add("Hada")
Set_Conjunto2 = set({Objeto27.Tipo})

Set_Conjunto1.update(Set_Conjunto2)

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Uno', 'Dos', 'Tres'})

print (f'{Set_Conjunto1}')

print (f'-' * 20)

Set_Conjunto3 = {1, 2, 3, 4, 5}
Set_Conjunto4 = {4, 5}
Set_Conjunto5 = set({8})

print (f'{Set_Conjunto3.issuperset(Set_Conjunto4)}')
print (f'{Set_Conjunto3 >= Set_Conjunto4}')

print (f'-' * 20)

print (f'{Set_Conjunto4.issubset(Set_Conjunto3)}')
print (f'{Set_Conjunto4 <= Set_Conjunto3}')

print (f'-' * 20)

print (f'{Set_Conjunto3.isdisjoint(Set_Conjunto5)}')

print (f'-' * 20)

SetA = {1, 2, 3, 4}
SetB = {3, 4, 5, 6}

print (f'{SetA.union(SetB)}')
print (f'{SetA | SetB}')

print (f'-' * 20)

print (f'{SetA.intersection(SetB)}')
print (f'{SetA & SetB}')

print (f'-' * 20)

print (f'{SetA.difference(SetB)}')
print (f'{SetA - SetB}')

print (f'-' * 20)

print (f'{SetB.difference(SetA)}')
print (f'{SetB - SetA}')

print (f'-' * 20)

print (f'{SetA.symmetric_difference(SetB)}')
print (f'{SetA ^ SetB}')

print (f'-' * 20)

'''SetA.update(SetB)

print (f'{SetA}')'''

'''SetA.intersection_update(SetB)

print (f'{SetA}')'''

'''SetA.difference_update(SetB)

print (f'{SetA}')'''

'''SetB.difference_update(SetA)

print (f'{SetB}')'''

SetA.symmetric_difference_update(SetB)

print (f'{SetA}')

print (f'-' * 20)

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add("Fresa")

print (f'{Set_Conjunto_Menu1}')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})
Set_Conjunto_Menu3 = set({'ChocoMani', Set_Conjunto_Menu2})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Objeto26.Cantidad,
    'Votante' : Variable_Funcion_Tupla[3]
}

Diccionario2 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
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

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2.values()}')
print (f'{Diccionario2.items()}')
print (f'{Diccionario2["Nombre"][2]}')
print (f'{Diccionario2.get("Edad")[1]}') #type: ignore

print (f'-' * 20)

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3.values()}')
print (f'{Diccionario3.items()}')
print (f'{Diccionario3["Ingresos"]}')
print (f'{Diccionario3.get("Gastos")}')

print (f'-' * 20)

Diccionario1["Nombre"] = variable1

print (f'{Diccionario1}')

Diccionario1_Copia = Diccionario1.copy()

del Diccionario1["Nombre"]
Diccionario1.pop("Edad")
Diccionario1.pop("Votante")

print (f'{Diccionario1}')
print (f'{Diccionario1_Copia}')

print (f'-' * 20)

Diccionario1 = dict({1 : "Karlita", 2 : 6, 3 : not True})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario2["Nombre"][2]} no puede votar ya que solo tiene {Diccionario1.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', f'{PEPE.Diccionario_Poke["Poke1"]}')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])

Diccionario_Vacio2["Dos"] = PEPE.Lista2[PEPE.Lista2.index("Koala")]

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio1.keys()}')
print (f'{Diccionario_Vacio1.values()}')
print (f'{Diccionario_Vacio1.items()}')
print (f'{Diccionario_Vacio1["A"]}')
print (f'{Diccionario_Vacio1.get("B")}')

print (f'-' * 20)

print (f'{Diccionario_Vacio2}')
print (f'{Diccionario_Vacio2.keys()}')
print (f'{Diccionario_Vacio2.values()}')
print (f'{Diccionario_Vacio2.items()}')
print (f'{Diccionario_Vacio2["Uno"]}')
print (f'{Diccionario_Vacio2.get("Dos")}')

print (f'-' * 20)

Lista_Diccionario = ['Erick', 'Josue', 'Karlita']

Diccionario_Vacio3 = dict.fromkeys(['Uno', 'Dos', 'Tres'])

for elemento in Diccionario_Vacio3.keys():
    if (elemento == 'Uno'):
        Diccionario_Vacio3[elemento] = Lista_Diccionario[0]
    elif (elemento == 'Dos'):
            Diccionario_Vacio3[elemento] = Lista_Diccionario[1]
    elif (elemento == 'Tres'):
            Diccionario_Vacio3[elemento] = Lista_Diccionario[1]
    else:
        continue
    
print (f'{Diccionario_Vacio3}')
print (f'{Diccionario_Vacio3.keys()}')
print (f'{Diccionario_Vacio3.values()}')
print (f'{Diccionario_Vacio3.items()}')
print (f'{Diccionario_Vacio3["Uno"]}')
print (f'{Diccionario_Vacio3.get("Dos")}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

print (f'-' * 20)

Fecha3 = '2026-04-01'

try:
    Fech3 = datetime.strptime(Fecha3, '%Y-%m-%d').date()
    Fech3_Formateada = pd.to_datetime(Fech3)
    Cargar_Csv3['date'] = pd.to_datetime(Cargar_Csv3['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato incorrecto')
    
Cargar_Csv3['TOTALITO'] = Cargar_Csv3['quantity'] * Cargar_Csv3['price']
    
Encontrado3 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech3_Formateada.date()] #type: ignore

if (Encontrado3.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! se encontraron ventas en esta fecha')
    
    Grupo5 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo5_Min = Grupo5.idxmin()
    Grupo5_Max = Grupo5.idxmax()
    Grupo5_Min_Cant = Grupo5.min()
    Grupo5_Max_Cant = Grupo5.max()
    
    print (f'En la fecha {Fech3_Formateada} el producto {Grupo5_Min} vendio un total de {Grupo5_Min_Cant} unidades') #type: ignore
    print (f'En la fecha {Fech3_Formateada} el producto {Grupo5_Max} vendio un total de {Grupo5_Max_Cant} unidades') #type: ignore
    
    print (f'Cantidad de clientes que compraron el dia de hoy {Grupo5.count()}')
    
    print (f'La cantidad de productos comprados el dia de hoy fue de {Grupo5.sum()}')
    
    Grupo6 = Encontrado3.groupby('product')['TOTALITO'].sum()
    
    print (f'El total de dinero vendido en esta fecha fue de ${Grupo6.sum()}')
    
    Promedio4 = Grupo6.sum() / Grupo5.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio4, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Grupo6.mean(), 2)}')
    
print (f'-' * 20)

print (f'{Cargar_Csv3}')

print (f'-' * 20)

Set_Conjunto_Csv = set(Cargar_Csv3['product'])

print (f'{Set_Conjunto_Csv}')

Lista_Csv = list(Set_Conjunto_Csv)

Key2 = [f'Key{i}' for i in range(len(Lista_Csv))]

print (f'{Key2}')

print (f'-' * 20)

Diccionario4 = dict(zip(Key2, Lista_Csv))

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Key3"]}')
print (f'{Diccionario4.get("Key4")}')

print (f'-' * 20)

Key3 = [f'Key_{i}' for i in range(len(Lista_Uno_Copia))]

Diccionario5 = dict(zip(Key3, Lista_Uno_Copia))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key_1"]}')
print (f'{Diccionario5.get("Key_2")}')

print (f'-' * 20)

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'-' * 20)

print (f'El tipo de dato en la variable es {type(variable1)}')
print (f'El tipo de dato en la variable es {type(variable4)}')
print (f'El tipo de dato en la variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de dato en la variable es {type(variable6)}')
print (f'El tipo de dato en la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato en la variable es {type(Tupla1)}')
print (f'El tipo de dato en la variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de dato en la variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de dato en la variable es {type(Diccionario5)}')
print (f'El tipo de dato en la variable es {type(Funcion_Diccionario)}')
print (f'El tipo de dato en la variable es {type(Objeto26)}')
print (f'El tipo de dato en la variable es {type(Poke2)}')
print (f'El tipo de dato en la variable es {type(Array1)}')
print (f'El tipo de dato en la variable es {type(Data_Frame2)}')
print (f'El tipo de dato en la variable es {type(PEPE)}')

print (f'-' * 20)

if (Diccionario3["Ingresos"] > 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos Altos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3["Ingresos"] == 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3["Ingresos"] < 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')
    
variable8 = 'Erick'
variable9 = 37

if (variable8 == 'Josue' and variable9 > 40):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')
    
if (variable8 == 'Erick' or variable9 > 30):
    print (f'Al menos una de las condciones se cumple')
else:
    print (f'Error, ninguna de las condiciones se cumple')
    
print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        
    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')
        
Objeto56 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Ash")], 'Kanto', Objeto25.Nombre)
Objeto57 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Brooke")], 'Alolah', Objeto26.Nombre)
Objeto58 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")], 'Paldea', Objeto27.Nombre)

Objeto56.Desplegar()
Objeto57.Desplegar()
Objeto58.Desplegar()

Negativo = -5

print (f'Ahora es positivo {int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima4 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable}')
print (f'{list(Anonima4)}')
print (f'{Lista_Iterable}')

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
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
    print (f'{indice} -- {elemento}')

print (f'-' * 20)

variable10 = 'eSteBAN'
variable10_letra = variable10[0]

print (f'{variable10}')
print (f'{variable10.lower()}')
print (f'{variable10.upper()}')
print (f'{variable10.capitalize()}')

print (f'{variable10.lower().find("t")}')
print (f'{variable10.lower().index("b")}')

print (f'La letra {variable10_letra} aparece un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = 'esto es un texto cualquiera pero que necesitamos ver si sirve al final o no'
Lista_variable11 = variable11.split(' ')

for elemento in enumerate(Lista_variable11):
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'La cantidad de palabras digitadas es {len(Lista_variable11)}')

print (f'-' * 20)

var6 = 'texto'

if (isinstance(var6, (str))):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Lo que ingresaste no es texto')
    
if (var6.isalpha()):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Lo que ingresaste no es texto')
    
try:
    Textico = str(var6)
    if (Textico.isalpha()):
        print (f'Lo que ingresaste es un texto')
    else:
        print (f'Lo que ingresaste es un numero')
except ValueError:
    print (f'Error, lo que ingresaste no es un texto')
    
print (f'-' * 20)

var7 = 3.5

if (isinstance(var7, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, esto no es un numero decimal')
    
try:
    Numerito6 = float(var7)
    if (Numerito6.is_integer()):
        print (f'Lo ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var8 = '3'

if (isinstance(var8, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
if (var8.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
try:
    Numerito7 = float(var8)
    if (Numerito7.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var9 = 'erick123'

if (isinstance(var9, (str, int))):
    print (f'Esto puede contener letras o numeros')
else:
    print (f'Error de formato')
    
if (var9.isalnum()):
    print (f'Esto puede contener letras o numeros')
else:
    print (f'Error de formato')
    
print (f'-' * 20)
    
var10 = 3.5

if (isinstance(var10, (int, float))):
    print (f'Esto puede contener enteros o decimales')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var11 = '      e           '

if (var11.isspace()):
    print (f'Esto esta compuesto unicamente por espacios')
else:
    print (f'Error, esto tiene mas que solo espacios')
    
print (f'-' * 20)

var12 = ' '

if (bool(var12) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, esta mica esta vacia')
    
print (f'-' * 20)

var13 = 'eSteBAN'

if (var13.lower().islower()):
    print (f'Todo este texto esta en minuscula')
else:
    print (f'Error, el texto no esta 100% en minuscula')
    
if (var13.upper().isupper()):
    print (f'Todo este texto esta en mayuscula')
else:
    print (f'Error, el texto no esta 100% en mayuscula')
    
print (f'-' * 20)

print (f'El elemento {PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

for elemento in Diccionario1_Copia:
    print (f'{Diccionario1_Copia[elemento]}')
    
print (f'-' * 20)

for elemento in Diccionario1_Copia.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario1_Copia.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario1_Copia.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

Contador = 0

while (Contador <= len(PEPE.Lista_Numeros)):
    print (f'El contador es {Contador + 1}')
    Contador+= 1
    
print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'El numero {PEPE.Lista_Numeros[Contador]} multiplicado x 100 es: {PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1
    
print (f'-' * 20)

Lista_Animales = ['Raton']
Lista_Animales.append('Gato')
Lista_Animales.insert(2, 'Perro')
Lista_Animales.extend([PEPE.Lista2[2]])

print (f'{Lista_Animales}')

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == "Perro"):
        print (f'Este es el mejor amigo del hombre')
        break
    else:
        Contador+= 1
        continue
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Set_Conjunto1, PEPE.Tupla_Poke):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento1, elemento2, elemento3, elemento4 in zip(Set_Conjunto1, PEPE.Tupla_Poke, Lista_Animales, Tupla1):
    print (f'{elemento1} -- {elemento2} -- {elemento2} -- {elemento4}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(0, len(Lista_Animales)):
    print (f'{elemento}')
    
print (f'-' * 20)

Lista_Multiplicado = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{PEPE.Lista_Numeros}')
print (f'{Lista_Multiplicado}')

print (f'-' * 20)

Menor4 = min(Lista_Multiplicado)
Mayor4 = max(Lista_Multiplicado)

Redondeo = round(14.458795, 2)

print (f'El numero redondeado: {Redondeo}')

print (f'{bool(False)}')
print (f'{bool(not True)}')
print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool("")}')

Todo_All = all([Lista_Multiplicado, Set_Conjunto1, Diccionario1_Copia, None])

print (f'{Todo_All}')

Sumatoria4 = sum(Lista_Multiplicado)

print (f'El resultado de la sumatoria es {Sumatoria4}')

Uno = int('500')
Dos = str(500)
Tres = float(Uno)
Cuatro = list(PEPE.Tupla_Poke)
Cinco = set(Lista_Animales)
Seis = tuple(Set_Conjunto1)

print (f'{type('500')} -- {type(Uno)}')
print (f'{type(500)} -- {type(Dos)}')
print (f'{type(Uno)} -- {type(Tres)}')
print (f'{type(PEPE.Tupla_Poke)} -- {type(Cuatro)}')
print (f'{type(Lista_Animales)} -- {type(Cinco)}')
print (f'{type(Set_Conjunto1)} -- {type(Seis)}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto_Poke1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

print (f'-' * 20)

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio(Lista):
        for elemento in range(Contador):
            Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
            Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
            Estudiante = [Alumno_Nombre, Alumno_Edad]
            Lista.append(Estudiante)
                
        Lista.sort(key = lambda Num : Num[1])
        Menore = Lista[0][0]
        Mayore = Lista[-1][0]
            
        print (f'El menor de los estudiantes de la lista es {Menore} y su edad es {Lista[0][1]} años')
        print (f'El mayor de los estudiantes de la lista es {Mayore} y su edad es {Lista[-1][1]} años')

Colegio(Lista_Alumnos)'''

def Exception_Finale(Numero):
    try:
        Numerito = float(Numero)
        if (Numerito.is_integer()):
            print (f'Lo que ingresaste es un numero entero')
        else:
            print (f'Lo que ingresate es un numero decimal')
    except (ValueError, TypeError):
        print (f'Error, lo que ingresaste no es un numero')

Exception_Finale('Hola')

print (f'-' * 20)

'''def Exception_Finalez():
    while True:
        Numerito = input(f'Ingrese un numero entero: ')
        try:
            Numerito1 = float(Numerito)
            if (Numerito1.is_integer()):
                print (f'Lo que ingresaste es un numero entero')
                break
            else:
                print (f'Error, esto es un numero decimal')
        except ValueError:
            print (f'Error, necesito que ingreses un numero')

Exception_Finalez()'''

import pandas as pd
import requests
import io

Ruta_Html2 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html2, headers=headers)

Leer_Html2 = io.StringIO(Response.text)

Cargar_Htm2 = pd.read_html(Leer_Html2)

print (f'{Cargar_Htm2[5].head()}')

print (f'-' * 20)

import re

Texto13 = 'ericksuper80@hotmail.com'

Pattern13 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|net|org)'

Buscar20 = bool(re.fullmatch(Pattern13, Texto13))

if (Buscar20  == True):
    print (f'El correo electronico tiene el formato correcto')
else:
    print (f'Error, formato incorrecto')
    
print (f'-' * 20)

class Panaderia():
    def __init__(self):
        self.Panes = ['Baguette', 'Croissant', 'Pan Dulce']
        
    def __iter__(self):
        return iter(self.Panes)
        
Objeto59 = Panaderia()

for elemento in Objeto59:
    print (f'{elemento}')