try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado es incorrecto')
    raise

try:
    import Module_Own as PEPE
except ModuleNotFoundError:
    print (f'Error, el modulo seleccionado es incorrecto')
    raise

# Funciones de orden superior

def Ejercicio1(Numero):
    return Numero + 10

def Ejercicio2(Numero):
    return Numero * 10

def Calcular(Funcion, Num):
    return Funcion(Num)

print (f'El resultado de la suma es {Calcular(Ejercicio1, 5)}')
print (f'El resultado de la multiplicacion es {Calcular(Ejercicio2, 5)}')

print (f'-' * 20)

Lista_Nombres1 = ['Erick', 'Josue', 'Karlita']
Lista_Nombres2 = list(['Carmelo', 'Susanita', 'Roxana'])

def Ejercicio3(Lista):
    for elemento in Lista:
        print (f'Mi nombre es {elemento}')

def Ejercicio4(Lista):
    for elemento in Lista:
        print (f'Mi nombre es {elemento}')
        
def Llamando(Funcion, Nombres):
    return Funcion(Nombres)

Llamando(Ejercicio3, Lista_Nombres1)

print (f'-' * 20)

Llamando(Ejercicio4, Lista_Nombres2)

print (f'-' * 20)

def Ejercicio5(Num1, Num2):
    return Num1 + Num2 + 10

def Ejercicio6(Num1, Num2):
    return Num1 + Num2 * 10

def Calcular2(Funcion, Primero, Segundo):
    return Funcion(Primero, Segundo)

print (f'El resultado de la suma es {Calcular2(Ejercicio5, 2, 3)}')
print (f'El resultado de la multiplicacion es {Calcular2(Ejercicio6, 2, 3)}')

print (f'-' * 20)

Diccionario_Ejemplo = dict({'Num1' : 1, 'Num2' : 2, 'Num3' : 3, 'Num4' : 4, 'Num5' : 5, 'Num6' : 6, 'Num7' : 7})

def Ejercicio7(Diccio):
    Lista_Pares = []
    
    for clave, valor in Diccio.items():
        if (valor % 2 == 0):
            Lista_Pares.append(clave)
            
    return Lista_Pares

def Ejercicio8(Diccio):
    Lista_Impares = list([])
    
    for clave, valor in Diccio.items():
        if (valor % 2 != 0):
            Lista_Impares.extend([clave])
            
    return Lista_Impares
            
def Evaluar(Funcion, Diccinario):
    return Funcion(Diccinario)

print (f'Lista Pares: {Evaluar(Ejercicio7, Diccionario_Ejemplo)}')
print (f'Lista Impares: {Evaluar(Ejercicio8, Diccionario_Ejemplo)}')

print (f'-' * 20)

Lista_Animales1 = ['Camaron', 'Hiena', 'Leon']
Lista_Animales1.append('Salamandra')
Lista_Animales1.insert(1, 'Pez Vela')
Lista_Animales1.extend(['Koala'])

def Ejercicio9(Lista):
    while (Lista):
        del Lista[0]
        print (f'{Lista}')

Ejercicio9(Lista_Animales1)

print (f'-' * 20)

def Ejercicio10(Num1:int, Num2:int) -> int:
    '''Este es el titulo de la funcion, esta es una funcion que toma dos argumentos, los suma y devuelve el resultado'''
    return Num1 + Num2

Ejercicio10(12, 7)

print (f'{help(Ejercicio10)}')

print (f'-' * 20)

def Ejercicio11(texto='Nada que mostrar'):
    return texto

print (f'{Ejercicio11()}')

print (f'-' * 20)

def Ejercicio12(Num1=20, Num2=30, Num3=15):
    return Num1 + Num2 + Num3

print (f'Resultado: {Ejercicio12()}')

print (f'-' * 20)

def Ejercicio13(Num1=20, Num2=30, Num3=15):
    return Num1 + Num2 + Num3

print (f'Resultado: {Ejercicio13(1, 4)}')

print (f'-' * 20)

def Ejercicio14(Num1, Num2, Num3=15):
    return Num1 + Num2 + Num3

print (f'Resultado: {Ejercicio14(5, 30)}')

print (f'-' * 20)

def Ejercicio15(*args):
    return round(sum(args) / len(args), 2)

print (f'El promedio de los numeros es {Ejercicio15(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

def Ejercicio16(**kwargs):
    Acumulador = 0
    
    for _, valor in kwargs.items():  # Se usa el underscore cuando un valor no se va a usar como buena practica
        Acumulador += valor
        
    return Acumulador

print (f'El resultado de la operacion es {Ejercicio16(num1=4, num2=6, num3=3)}')

def Ejercicio17(num1, num2, *args, **kwargs):
    print (f'La suma de los numeros es {num1 + num2}')
    print (f'{args}')
    
    for elemento in args:
        print (f'- {elemento}')
        
    print (f'-' * 20)
    
    print (f'\n{kwargs}')
    
    for clave, valor in kwargs.items():
        print (f'{clave} : {valor}')

Ejercicio17(
    1, 2,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    nombre1='Erick', nombre2='Karlita', nombre3='Josue'
)

print (f'-' * 20)

def Ejercicio18(*participantes, **detalles):
    print (f'Participantes: {participantes}')
    
    for elemento in participantes:
        print (f'- {elemento}')
        
    print (f'-' * 20)
    
    print (f'\nDetalles: {detalles}')
    
    for clave, valor in detalles.items():
        print (f'{clave} : {valor}')

Ejercicio18(
    'Erick', 'Josue', 'Karlita', 'Carmelo', 'Susanita', 'Roxana',
    nombre='Mascarada Comunal',
    lugar='Parque de Santa Barbara',
    dia='Domingo'
)

print (f'-' * 20)

def Ejercicio19(limite):
    Temporal = 0
    Lista_Fibonacci = [0, 1]
    
    while (len(Lista_Fibonacci) < limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

print (f'Lista Fibonacci: {Ejercicio19(10)}')

print (f'-' * 20)

Lista_Primera = [1, 2, 7, 9]
Lista_Segunda = [3, 4, 5, 6]

def Ejercicio20(Primera, Segunda):
    Set_Conjunto = set({})
    Lista_Tercera = []
    
    for elemento in Primera:
        if (elemento in Segunda):
            Set_Conjunto.add(elemento)
        else:
            continue
        
    Lista_Tercera = list(Set_Conjunto)
    
    return Lista_Tercera

Sample20 = Ejercicio20(Lista_Primera, Lista_Segunda)

if (len(Lista_Primera) == 0 or len(Lista_Segunda) == 0):
    print (f'Error, al menos una de las listas esta vacia')
else:
    if (Sample20):
        print (f'La lista con numeros que pertenecen a ambas pero no se repiten es {Sample20}')
    else:
        print (f'Error, no hay ningun numero que pertenezca a ambas listas')
        
print (f'-' * 20)

var1 = 50

print (f'{type(var1)}')

var1+= 3.5

print (f'{type(var1)}')

print (f'-' * 20)

var2 = 50

print (f'{type(var2)}')

var2 = float(var2)

print (f'{type(var2)}')

print (f'-' * 20)

Lista_Nombres3 = ['Erick', 'Josue']
Lista_Nombres4 = list(['Perez', 'Gutierrez'])

print (f'{Lista_Nombres3 + Lista_Nombres4}')

Tupla_Nombres3 = ('Erick', 'Josue',)
Tupla_Nombres4 = 'Perez', 'Gutierrez',

print (f'{Tupla_Nombres3 + Tupla_Nombres4}')

print (f'-' * 20)

var3 = 0 # Esto puede ser 3, -3, -3.5, pero no 0

if (var3):
    print (f'Valido')
else:
    print (f'Invalido')
    
print (f'-' * 20)

var4 = '' # Esta vara debe tener contenido o espacios para que sea valido, sin nada es invalido

if (var4):
    print (f'Valido')
else:
    print (f'Invalido')
    
print (f'-' * 20)

var5 = [] # Contenido es True, sin contenido es False

if (var5):
    print (f'Valido')
else:
    print (f'Invalido')
    
print (f'-' * 20)

var6 = {} # Contenido es True, sin contenido es False

if (var6):
    print (f'Valido')
else:
    print (f'Invalido')
    
print (f'-' * 20)

var7 = None # None siempre va a ser sin asignacion, siempre que sea None, sera vacio

if (not var7):
    print (f'Valido')
else:
    print (f'Invalido')
    
print (f'-' * 20)

Lista_Ejemplo1 = [1, 2, 3, 4, 5]

def Ejercicio21(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        
        while (Contador < len(Lista)):
            Contador += 1
            
        return Contador

Sample21 = Ejercicio21(Lista_Ejemplo1)

if (Sample21 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista tiene {Sample21} elementos')
    
print (f'-' * 20)

def Ejercicio22(Lista):
    Acumulador = 0
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador += elemento
        else:
            continue
        
    return Acumulador

Sample22 = Ejercicio22(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample22 > 0):
        print (f'La suma de los numeros pares de la lista es {Sample22}')
    else:
        print (f'Error, no hay ningun numero par en la lista')
        
print (f'-' * 20)

def Ejercicio23(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        
        for elemento in Lista:
            Acumulador += elemento
            
        return Acumulador

Sample23 = Ejercicio23(Lista_Ejemplo1)

if (Sample23 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de todos los elementos de la lista es {Sample23}')
    
print (f'-' * 20)

Lista_Ejemplo2 = [10]

def Ejercicio24(Lista):
    Acumulador = 0
    
    for elemento in Lista[:-1]:
        Acumulador += elemento
        
    return Acumulador

Sample24 = Ejercicio24(Lista_Ejemplo2)

if (len(Lista_Ejemplo2) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de los numeros de la lista es {Sample24}')
    
print (f'-' * 20)

def Ejercicio25(Lista, Numero):
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
        
Unidad1 = 4

Sample25 = Ejercicio25(Lista_Ejemplo1, Unidad1)

if (Sample25 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample25 == True):
        print (f'El numero {Unidad1} fue encontrado en la lista')
    else:
        print (f'Error, el numero no fue encontrado en la lista')
        
print (f'-' * 20)

def Ejercicio26(Lista):
    Menor = min(Lista)
    Mayor = max(Lista)
    
    Lista_Resultado = [Menor, Mayor]
    
    return Lista_Resultado

Sample26 = Ejercicio26(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de los numeros de la lista es {min(Sample26)}')
    print (f'El mayor de los numeros de la lista es {max(Sample26)}')
    
print (f'-' * 20)

def Ejercicio27(Lista, Numero):
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
    
Unidad2 = 2

Sample27 = Ejercicio27(Lista_Ejemplo1, Unidad2)

if (Sample27 is None):
    print (f'Error la lista esta vacia')
else:
    if (Sample27 > 0):
        print (f'La cantidad de numeros mayores que {Unidad2} es {Sample27}')
    else:
        print (f'Error, no hay ningun numero mayor que {Unidad2} en la lista')
        
print (f'-' * 20)

def Ejercicio28(Lista):
    Lista_Pares = []
    Lista_Impares = list([])
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            Lista_Impares.extend([elemento])
            
    return Lista_Pares, Lista_Impares

Sample28 = Ejercicio28(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    Lista_Num_Pares, Lista_Num_Impares = Sample28
    
    print (f'Lista Original: {Lista_Ejemplo1}')
    print (f'Lista Pares: {Lista_Num_Pares}')
    print (f'Lista Impares: {Lista_Num_Impares}')
    
print (f'-' * 20)

def Pares(Lista):
    Lista_Pares = []
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            continue
        
    return Lista_Pares

def Impares(Lista):
    Lista_ImPares = []
    for elemento in Lista:
        if (elemento % 2 != 0):
            Lista_ImPares.extend([elemento])
        else:
            continue
        
    return Lista_ImPares

def Evaluador1(Funcion, Listado):
    return Funcion(Listado)

print (f'Lista Original: {Lista_Ejemplo1}')
print (f'Lista Original: {Evaluador1(Pares, Lista_Ejemplo1)}')
print (f'Lista Original: {Evaluador1(Impares, Lista_Ejemplo1)}')

print (f'-' * 20)

def Ejercicio29(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Mult = []
        
        for elemento in Lista:
            Lista_Mult.append(elemento * 2)
            
        return Lista_Mult

Sample29 = Ejercicio29(Lista_Ejemplo1)

if (Sample29 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Ejemplo1}')
    print (f'Lista Actualizada: {Sample29}')
    
print (f'-' * 20)

'''Lista_Promedio = list([])
Contador = 0

while (Contador < 3):
    while True:
        Numerito = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito1 = float(Numerito)
            if (Numerito1.is_integer()):
                print (f'La nota {Contador + 1} es un numero entero')
                Lista_Promedio.append(Numerito1)
                break
            else:
                print (f'La nota {Contador + 1} es un numero decimal')
                Lista_Promedio.extend([Numerito1])
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador += 1
    
Promedio1 = sum(Lista_Promedio) / Lista_Promedio.__len__()

print (f'El promedio de las notas ingresadas es {round(Promedio1, 2)}')'''

Lista_Ejemplo3 = [5, -6, 0, -1, -3, 0]

def Ejercicio30(Lista):
    Negativos = 0
    Positivos = 0
    Ceros = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Positivos += 1
        elif (elemento < 0):
            Negativos += 1
        else:
            Ceros += 1
            
    return Positivos, Negativos, Ceros

Sample30 = Ejercicio30(Lista_Ejemplo3)

if (len(Lista_Ejemplo3) == 0):
    print (f'Error, la lista esta vacia')
else:
    Numeros_Positivos, Numeros_Negativos, Numeros_Cero = Sample30
    
    print (f'Lista Original: {Lista_Ejemplo3}')
    print (f'Lista Positivos: {Numeros_Positivos}')
    print (f'Lista Negativos: {Numeros_Negativos}')
    print (f'Lista Ceros: {Numeros_Cero}')
    
print (f'-' * 20)

import re

Lista_Ejemplo4 = list([
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
])

def Ejercicio31(Lista):
    Lista_Validos = []
    Lista_Invalidos = list([])
    
    if (len(Lista) == 0):
        return None
    else:
        Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'
        
        for elemento in Lista:
            Buscar = bool(re.fullmatch(Pattern, elemento))
            
            if (Buscar == True):
                Lista_Validos.append(elemento)
            else:
                Lista_Invalidos.extend([elemento])
                
        return Lista_Validos, Lista_Invalidos

Sample31 = Ejercicio31(Lista_Ejemplo4)

if (Sample31 is None):
    print (f'Error, la lista esta vacia')
else:
    Correos_Validos, Correos_Invalidos = Sample31
    
    print (f'Lista Correos Original: {Lista_Ejemplo4}')
    print (f'Lista Correos Validos: {Correos_Validos}')
    print (f'Lista Correos Invalidos: {Correos_Invalidos}')
    
print (f'-' * 20)

def Ejercicio32(Lista):
    Temporal = Lista[0]
    
    for elemento in Lista:
        if (elemento > Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

Sample32 = Ejercicio32(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El mayor de los numeros de la lista es {Sample32}')
    
print (f'-' * 20)

def Ejercicio33(Lista):
    Temporal = Lista[0]
    
    for elemento in Lista:
        if (elemento < Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

Sample33 = Ejercicio33(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de los numeros de la lista es {Sample33}')
    
print (f'-' * 20)

Lista_Ejemplo5 = [-15.5, -8, -3.2, -1, 0, 4, 7.5, 12, 19.1, 25]

def Ejercicio34(Lista):
    Contador = 0
    Acumulador = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Contador += 1
            Acumulador += elemento
        else:
            continue
        
    return Contador, Acumulador

Sample34 = Ejercicio34(Lista_Ejemplo5)

if (len(Lista_Ejemplo5) == 0):
    print (f'Error, la lista esta vacia')
else:
    Total_Positivos, Total_Positivos_Sum = Sample34
    
    print (f'Los numeros positivos de la lista son {Total_Positivos}')
    print (f'La suma de estos numeros positivos es {round(Total_Positivos_Sum)}')
    
print (f'-' * 20)

Lista_Ejemplo6 = list([65, 70, 54, 80, 69, 66])

def Ejercicio35(Lista):
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
                
        return Aprobados, Aprobados_Sum, Reprobados

Sample35 = Ejercicio35(Lista_Ejemplo6)

if (Sample35 is None):
    print (f'Error, la lista esta vacia')
else:
    Total_Aprobados, Total_Aprobados_Sum, Total_Reprobados = Sample35
    
    print (f'Lista estudiantes aprobados: {Total_Aprobados}')
    print (f'Suma notas estudiantes aprobados: {Total_Aprobados_Sum}')
    print (f'Lista estudiantes reprobados: {Total_Reprobados}')
    
print (f'-' * 20)

Lista_Ejemplo7 = list([15, 0, 8, 2, 0, 25, 4])

def Ejercicio36(Lista):
    Agotados = 0
    Stock_Bajo = 0
    Stock_Alto = 0
    Stock_Bajo_Sum = 0
    Stock_Alto_Sum = 0
    
    for elemento in Lista:
        if (elemento == 0):
            Agotados += 1
        elif (elemento >= 1 and elemento <= 5):
            Stock_Bajo += 1
            Stock_Bajo_Sum += elemento
        else:
            Stock_Alto += 1
            Stock_Alto_Sum += elemento
            
    return Agotados, Stock_Bajo, Stock_Bajo_Sum, Stock_Alto, Stock_Alto_Sum

Sample36 = Ejercicio36(Lista_Ejemplo7)
    
if (len(Lista_Ejemplo7) == 0):
    print (f'Error la lista esta vacia')
else:
    Prod_Agotados, Prod_Stock_Bajo, Prod_Stock_Bajo_Sum, Prod_Stock_Alto, Prod_Stock_Alto_Sum = Sample36
    
    print (f'Cantidad de productos agotados: {Prod_Agotados}')
    print (f'Cantidad de productos con stock bajo: {Prod_Stock_Bajo}')
    print (f'Suma de productos con stock bajo: {Prod_Stock_Bajo_Sum}')
    print (f'Cantidad de productos con stock alto: {Prod_Stock_Alto}')
    print (f'Suma de productos con stock alto: {Prod_Stock_Alto_Sum}')
    print (f'Suma de todos los productos con stock: {Prod_Stock_Bajo_Sum + Prod_Stock_Alto_Sum}')
    
print (f'-' * 20)

Lista_Ejemplo8 = [12, 8, 5, 1, 7, 0, 10]

def Ejercicio37(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Posicion = 0
        Contador = 0
        
        while (Contador < len(Lista)):
            if (Lista[Contador] == 0):
                Posicion = Contador
                break
            else:
                Contador += 1
                continue
            
        return Posicion

Sample37 = Ejercicio37(Lista_Ejemplo8)

if (Sample37 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La primera posicion donde aparece un producto agotado es {Sample37}')
    
print (f'-' * 20)

Lista_Ejemplo9 = list([120, 350, 80, 600, 150, 700])

def Ejercicio38(Lista, Numero):
    Posicion = 0
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] > Numero):
            return Contador
        else:
            Contador += 1
            continue
        
    return None

Limite = 200

Sample38 = Ejercicio38(Lista_Ejemplo9, Limite)

if (len(Lista_Ejemplo9) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample38 is None):
        print (f'Error, no se ha encontrado ninguna venta mayor que {Limite}')
    else:
        print (f'La primer venta mayor que {Limite} aparece en la posicion {Sample38} y la venta en cuestion es ${Lista_Ejemplo9[Sample38]}')
        
print (f'-' * 20)

Lista_Ejemplo10 = [10, 1, 2, 4, 3, 5, 6]

def Ejercicio39(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            
    return None

Sample39 = Ejercicio39(Lista_Ejemplo10)

if (len(Lista_Ejemplo10) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample39 is None):
        print (f'No hay ningun numero en la lista que se repita')
    else:
        print (f'El primer numero de la lista que se repite es {Sample39}')
        
print (f'-' * 20)

Lista_Ejemplo11 = list([10, 1, 2, 4, 3, 5, 6])

def Ejercicio40(Lista):
    for i in range(len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                return Lista[j]
            else:
                continue
            
    return None

Sample40 = Ejercicio40(Lista_Ejemplo11)

if (len(Lista_Ejemplo10) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample40 is None):
        print (f'No hay ningun numero en la lista que se repita')
    else:
        print (f'El primer numero de la lista que se repite es {Sample40}')
        
print (f'-' * 20)

Lista_Ejemplo12 = [90, 80, 79, 78]

def Ejercicio41(Lista):

    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] < Lista[i]):
            return i
        else:
            continue
        
    return None

Sample41 = Ejercicio41(Lista_Ejemplo12)

if (len(Lista_Ejemplo12) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample41 is None):
        print (f'En la lista no hay ningun aumento consecutivo de ventas')
    else:
        print (f'El primer aumento consecutivo de ventas sucede en la posicion {Sample41} y la venta en cuestion es ${Lista_Ejemplo12[Sample41]}')
        
print (f'-' * 20)

Lista_Ejemplo13 = list([100, 97, 95, 80, 78])

def Ejercicio42(Lista, Numero):
    Grados = 0
    
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] - Lista[i] >= Numero):
            Grados = Lista[i - 1] - Lista[i]
            return i, Grados
        else:
            continue
        
    return None

Grados = 10

Sample42 = Ejercicio42(Lista_Ejemplo13, Grados)

if (len(Lista_Ejemplo13) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample42 is None):
        print (f'En la ultima hora no se han registrado caidas bruscas de temperatura')
    else:
        Posicion, Caida = Sample42
        print (f'Alerta!!! se registro una caida de {Caida} grados en la posicion {Posicion}')
        
print (f'-' * 20)

Lista_Ejemplo14 = [1, 1, 0, 1, 3]

def Ejercicio43(Lista):
    for i in range(0 + 2, len(Lista)):
        if (Lista[i - 2] < Lista[i - 1] and Lista[i - 1] > Lista[i]):
            return Lista[i - 1]
        else:
            continue
        
    return None

Sample43 = Ejercicio43(Lista_Ejemplo14)

if (len(Lista_Ejemplo14) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample43 is None):
        print (f'Error, no se ha localizado un numero con estas caracteristicas')
    else:
        print (f'El pico lo produce el numero {Sample43}')
        
print (f'-' * 20)

# Consultar valores ✅ Consultar.

Capitales1 = {"Costa Rica": "San José", "México": "Ciudad de México", "Argentina": "Buenos Aires", "Italia": "Roma", "España": "Madrid"}

Ubicar1 = Capitales1.get("Italia")

if (Ubicar1 is None):
    print (f'Error, Italia no esta en el diccionario')
else:
    print (f'La capital de Italia es {Ubicar1}')
    
print (f'-' * 20)

# Consultar valores ✅ Consultar.

Productos1 = {"Laptop": 1200, "Mouse": 25, "Teclado": 45, "Monitor": 300}

def Ejercicio44(Diccionario, Articulo):
    Ubicado = Diccionario.get(Articulo)
    
    if (Ubicado is None):
        return False
    else:
        return True

Item1 = 'Escoba'

Sample44 = Ejercicio44(Productos1, Item1)

if (len(Productos1) == 0):
    print (f'Error, el diccinario esta vacio')
else:
    if (Sample44 == True):
        print (f'El articulo {Item1} fue ubicado en el diccinario')
    else:
        print (f'Error, el articulo no existe en el diccionario')
        
print (f'-' * 20)

# Actualizar elementos ✅ Actualizar.

Productos2 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300
}

def Ejercicio45(Diccionario, Articulo, Precio):
    Ubicado = Diccionario.get(Articulo)
    
    if (Ubicado is None):
        return False
    else:
        Diccionario[Articulo] = Precio
        return True

Item2 = 'Escoba'
Item2_Price = 55

Sample45 = Ejercicio45(Productos2, Item2, Item2_Price)

if (len(Productos2) == 0):
    print (f'Error, el diccinario esta vacio')
else:
    if (Sample45 == True):
        print (f'El precio del articulo {Item2} fue actualizado a ${Item2_Price}')
    else:
        print (f'Error, el articulo no existe en el diccionario, no se puede actualizar el precio')
        
print (f'-' * 20)

# Agregar elementos ✅ Agregar.

Productos3 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio46(Diccionario, Articulo, Precio):
    Ubicar = Diccionario.get(Articulo)
    
    if (Ubicar is None):
        Diccionario[Articulo] = Precio
        return True
    else:
        return False

Item3 = 'Escoba'
Item3_Price = 20

Sample46 = Ejercicio46(Productos3, Item3, Item3_Price)

if (len(Productos3) == 0):
    print (f'Error, el diccinario esta vacio')
else:
    if (Sample46 == True):
        print (f'Este articulo no existia en el diccionario, {Item3} agregado!!!')
    else:
        print (f'Error {Item3} ya existe en el diccionario, no se debe agregar de nuevo')
        
print (f'-' * 20)

# Eliminar elementos ✅ Eliminar.

Productos4 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio47(Diccionario, Articulo):
    Ubicar = Diccionario.get(Articulo)
    
    if (Ubicar is None):
        return False
    else:
        del Diccionario[Articulo]
        return True

Item4 = 'Teclado'

Sample47 = Ejercicio47(Productos4, Item4)

if (len(Productos4) == 0):
    print (f'Error, el diccinario esta vacio')
else:
    if (Sample47 == True):
        print (f'El articulo {Item4} fue eliminado correctamente')
    else:
        print (f'Error, el articulo no existe en la lista, no se puede eliminar')
        
print (f'-' * 20)

Productos5 = {
    "Laptop": 60,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio48(Diccionario):
    Clave = next(iter(Diccionario))
    Valor = Diccionario[Clave]
    
    for indice, elemento in Diccionario.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    return Clave, Valor

Sample48 = Ejercicio48(Productos5)

if (len(Productos5) == 0):
    print (f'Error, el diccinario esta vacio')
else:
    Clave, Valor = Sample48
    
    print (f'Articulo: {Clave}')
    print (f'Valor: ${Valor}')

print (f'-' * 20)

Productos6 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio49(Diccionario, Numero):
    for indice, elemento in Diccionario.items():
        if (elemento > Numero):
            return indice, elemento
        else:
            pass
        
    return None

Limite2 = 1500

Sample49 = Ejercicio49(Productos6, Limite2)

if (len(Productos6) == 0):
    print (f'Error, el diccinario esta vacio')
else:
    if (Sample49 is None):
        print (f'No hay ninguna venta que haya superado al limite en el diccionario')
    else:
        Clave2, Valor2 = Sample49
        print (f'La venta que supero el limite ${Limite2} se realizo el {Clave2} y el monto de la venta fue ${Valor2}')
        
print (f'-' * 20)

Productos7 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio50(Diccionario, Numero):
    Contador = 0
    for elemento in Diccionario.values():
        if (elemento > Numero):
            Contador += 1
        else:
            pass
        
    return Contador

Limite3 = 2000

Sample50 = Ejercicio50(Productos7, Limite3)

if (len(Productos7) == 0):
    print (f'Error, el diccinario esta vacio')
else:
    if (Sample50 > 0):
        print (f'La cantidad de ventas que superan el limite ${Limite3} fueron {Sample50}')
    else:
        print (f'Error, no hay ninguna venta en el diccionario que supere al limite')
        
print (f'-' * 20)

Lista_Ejemplo15 = [1, 2, 3, 4]

def Ejercicio51(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumular = 0
        for elemento in Lista[:-1]:
            Acumular += elemento
            
        return Acumular

Sample51 = Ejercicio51(Lista_Ejemplo15)

if (Sample51 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de todos los numeros menos el ultimo es {Sample51}')
    
print (f'-' * 20)

'''def Floating1(Numero):
    Resultado = Numero ** 2
    return Resultado

print (f'El numero {PEPE.Flotante1} al cuadrado es {Floating1(PEPE.Flotante1)}')

Floating2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Floating2}')

def Floating3(Texto):
    try:
        Texto_Formateado = Texto.replace(' ', '')
        if (isinstance(Texto_Formateado, (str))):
            if (Texto_Formateado.isalpha()):
                print (f'{Texto} es un texto')
    except AttributeError:
        print (f'Error, lo que ingresaste no es un texto')

Floating3(PEPE.Flotante3)

print (f'-' * 20)

def Floating4(Cadena):
    Lista_Cadena = Cadena.split(' ')
    
    for elemento in Lista_Cadena:
        print (f'{elemento}')
        
    print (f'La cantidad de palabras digitadas es {len(Lista_Cadena)}')

Floating4(PEPE.Flotante4)

print (f'-' * 20)'''

'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Lista.append(Alumno)
        
    return Lista

print (f'La lista de estudiantes es {Colegio(Lista_Alumnos)}')'''

'''Lista_Alumnos = []

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
    
    print (f'El menor de los estudiantes es {Menore} y su edad es {Lista[0][1]} año')
    print (f'El menor de los estudiantes es {Mayore} y su edad es {Lista[-1][1]} años')

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
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Colores = [
    Colores('Rojo'),
    Colores('Azul'),
    Colores('Verde')
]

print (f'La lista de colores es {Lista_Colores}')

print (f'-' * 20)

class Inventario():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto2 = Inventario()

Objeto2.Productos.append('Borrador')
Objeto2.Productos.insert(1, 'Lapicero')
Objeto2.Productos.extend(['Cuaderno'])

print (f'La cantidad de elementos es {len(Objeto2)}')

print (f'-' * 20)

class Igualdad():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
        
Objeto3 = Igualdad('Panda Rojo')
Objeto4 = Igualdad('Panda Rojo')

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

print (f'La suma de los objetos es {Objeto5 + Objeto6}')

print (f'-' * 20)

class Armario():
    def __init__(self):
        self.GuardaRopa = [
            'Camiseta',
            'Pantalon',
            'Chaqueta'
        ]
        
    def __getitem__(self, Indice):
        return self.GuardaRopa[Indice]
        
Objeto7 = Armario()

print (f'El elemento en la posicion 0 es {Objeto7[0]}')
print (f'El elemento en la posicion 1 es {Objeto7[1]}')
print (f'El elemento en la posicion 2 es {Objeto7[2]}')

print (f'-' * 20)

class Panaderia():
    def __init__(self):
        self.Panes = [
            'Baguette',
            'Croissant',
            'Baggel'
        ]
        
    def __iter__(self):
        return iter(self.Panes)
        
Objeto8 = Panaderia()

for indice, elemento in enumerate(Objeto8, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

Lista_Ejemplo16 = [1, 2, 3, 4, 5]

def Cuadrado(Lista):
    for elemento in Lista:
        print (f'El numero al cuadrado es {elemento ** 2}')

def Cubo(Lista):
    for elemento in Lista:
        print (f'El numero al cubo es {elemento ** 3}')
        
def Evaluador2(Funcion, Lista):
    return Funcion(Lista)

Evaluador2(Cuadrado, Lista_Ejemplo16)

print (f'-' * 20)

Evaluador2(Cubo, Lista_Ejemplo16)

'''Paises1 = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}

def Ejercicio52(Diccionario):
    while (True):
        Texto = input(f'Ingrese el codigo de un pais: ')
        Texto_Formateado = Texto.lower()
        try:
            Ubicado = Diccionario.get(Texto_Formateado)
            
            if (Ubicado):
                print (f'El codigo ingresado pertenece a {Ubicado}')
                break
            elif (Texto_Formateado == 'salir'):
                print (f'Gracias por usar nuestros servicios, que tenga un lindo dia!')
                break
            else:
                print (f'El codigo que ingresaste no es correcto, intente nuevamente')
        except ValueError:
            print (f'Error, el valor es incorrecto')

Ejercicio52(Paises1)'''

var8 = '3'

if (isinstance(var8, (int))):
    print (f'Esto es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var8.isnumeric()):
    print (f'Esto es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
try:
    Numerito1 = float(var8)
    if (Numerito1.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var9 = 3.5

if (isinstance(var9, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, lo ingresado no es un numero decimal')
    
try:
    Numerito2 = float(var9)
    if (Numerito2.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var10 = '3'

if (isinstance(var10, (int, float))):
    print (f'Lo que ingresaste puede ser un numero entero o decimal')
else:
    print (f'Error de formato')
    
try:
    Numerito3 = float(var10)
    if (Numerito3.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
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
    print (f'Error, la fecha tiene un formato incorrecto')
    exit()
    
Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrado1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()]

if (Encontrado1.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! se han encontrado ventas en esta fecha')
    
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Min} vendio {Grupo1_Min_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Max} vendio {Grupo1_Max_Cant} unidades')
    
    print (f'Cantidad de clientes que nos compraron hoy: {Grupo1.count()}')
    
    print (f'La cantidad de productos comprados en esta fecha es {Grupo1.sum()}')
    
    print (f'La media de productos vendidos en esta fecha es {Grupo1.mean()}')
    
    Grupo2 = Encontrado1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue ${Grupo1.sum()}')
    
    Promedio1 = Grupo2.sum() / Grupo1.count()

    print (f'El promedio de dinero vendido en esta fecha fue ${round(Promedio1, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue ${Grupo2.mean()}')
    
print (f'-' * 20)

print (f'{Cargar_Csv1}')

print (f'-' * 20)

Lista_Csv1 = list(Cargar_Csv1['product'])
Key1 = [f'Key_{i}' for i in range(len(Lista_Csv1))]

print (f'{Lista_Csv1}')
print (f'{Key1}')

Diccionario_Csv1 = dict(zip(Key1, Lista_Csv1))

print (f'{Diccionario_Csv1}')
print (f'{Diccionario_Csv1.keys()}')
print (f'{Diccionario_Csv1.values()}')
print (f'{Diccionario_Csv1.items()}')
print (f'{Diccionario_Csv1["Key_3"]}')
print (f'{Diccionario_Csv1.get("Key_6")}')

print (f'-' * 20)

for indice, elemento in Cargar_Csv1.iterrows():
    Unidad3 = elemento['product']
    Unidad4 = elemento['price']
    
    print (f'The price of the {Unidad3} is ${Unidad4}')
    
print (f'-' * 20)

import re

Texto2 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Pattern1 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Buscar1 = re.findall(Pattern1, Texto2)

print (f'{Buscar1}')

for indice, elemento in enumerate(Buscar1, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

import re

Texto3 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Version1

Pattern2 = r'\!|\?|\.{2,}|\d{2,4}\-[0-9]{4,}'

Buscar2 = re.sub(Pattern2, '', Texto3)

print (f'{Buscar2}')

# Version2

Pattern3 = r'[^a-zA-Z0-9\s]'

Buscar3 = re.sub(Pattern3, '', Texto3)

print (f'{Buscar3}')

print (f'-' * 20)

import re

Texto4 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Pattern4 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos1 = re.findall(Pattern4, Texto4)

Texto4_temp1 = Texto4

print (f'{Correos1}')

for i, email in enumerate(Correos1, start=1):
    Texto4_temp1 = Texto4_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto4_temp1}')

Pattern5 = r'\!|\?'

Texto4_temp2 = re.sub(Pattern5, '', Texto4_temp1)

print (f'{Texto4_temp2}')

for i, email in enumerate(Correos1, start=1):
    Texto4_temp2 = Texto4_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto4_temp2}')

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

'''Lista_Promedios = []

Contador = 0

while (Contador < 3):
    while True:
        Numerito = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito4 = float(Numerito)
            if (Numerito4.is_integer()):
                print (f'La nota {Contador + 1} es un numero entero')
                Lista_Promedios.append(Numerito4)
                break
            else:
                print (f'La nota {Contador + 1} es un numero decimal')
                Lista_Promedios.extend([Numerito4])
                break
        except ValueError:
            print (f'Error, necesito que ingreses un numero')
    Contador += 1
    
Promedio2 = sum(Lista_Promedios) / Lista_Promedios.__len__()

print (f'El promedio de las notas ingresadas es {round(Promedio2, 2)}')'''

import re

Texto5 = 'esto 4 es un 9 tex_to hola baratadocualquierba pero lo que mas me hela interesa 123 ! es saber si@ funciona hula o no'

Buscar4 = re.search(r'pero', Texto5)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\d+', Texto5)

print (f'{Buscar5}')

Buscar6 = re.findall(r'\W+', Texto5)

print (f'{Buscar6}')

'''
{1}
{2,6}
{2,}
? Esto significa 0 o 1
* Esto significa 0 o mas
+ Esto significa 1 o mas

\d Solo numeros
\D Todo menos numeros
\s Solo espacios
\S sin espacios
\W solo caracteres especiales
\w Sin caracteres especiales
'''

Buscar7 = bool(re.fullmatch(r'esto 4 es un 9 tex\_to hola cualquiera pero lo que mas me hela interesa 123 \! es saber si\@ funciona hula o no', Texto5))

if (Buscar7 == True):
    print (f'Ambos textos son exactamente iguales')
else:
    print (f'Error, los textos no son iguales')
    
Buscar8 = re.findall(r'h.la', Texto5)

print (f'{Buscar8}')

Buscar9 = bool(re.match(r'^esto', Texto5))

if (Buscar9 == True):
    print (f'Correcto, el texto comienza con --> esto')
else:
    print (f'Error, el texto no comienza con --> esto')
    
Buscar10 = bool(re.search(r'no$', Texto5))

if (Buscar10 == True):
    print (f'Correcto, el texto termina con --> no')
else:
    print (f'Error, el texto no termina con --> no')
    
Buscar11 = re.findall(r'\d{3,}\s\W', Texto5)

print (f'{Buscar11}')

Buscar12 = re.findall(r'[ab]{2,4}', Texto5)

print (f'{Buscar12}')

Buscar13 = re.findall(r'hola|\d{2,4}', Texto5)

print (f'{Buscar13}')

print (f'-' * 20)

import re

Texto6 = 'ericksuper80@gmail.com'

Pattern6 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}$'

Buscar14 = bool(re.fullmatch(Pattern6, Texto6))

if (Buscar14 == True):
    print (f'Correcto, el correo electronico tiene el formato correcto')
else:
    print (f'Error, formato de correo incorrecto')

print (f'-' * 20)

Pattern7 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.(?:com|net|org)$'

Buscar15 = bool(re.match(Pattern7, Texto6))

if (Buscar15 == True):
    print (f'Correcto, el correo 2 electronico tiene el formato correcto')
else:
    print (f'Error, formato de correo 2 incorrecto')
    
print (f'-' * 20)

import re

Texto7 = '32'

Pattern8 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar16 = bool(re.fullmatch(Pattern8, Texto7))

if (Buscar16 == True):
    print (f'El numero se encuentra entre 01 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

import re

Texto8 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern9 = r'\d{2,}\/[0-9]{2}\/\d{3,5}'

Replacement9 = 'XX/XX/XXXX'

Buscar17 = re.sub(Pattern9, Replacement9, Texto8)

print (f'{Buscar17}')

Pattern10 = r'\+\d{1}\-[0-9]{2,3}\-\d{3,}\-[0-9]{4}'

Replacement10 = 'Ph0n3_NuMb3r'

Buscar18 = re.sub(Pattern10, Replacement10, Buscar17)

print (f'{Buscar18}')

print (f'-' * 20)

import re

Texto9 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Pattern11 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar19 = re.findall(Pattern11, Texto9)

print (f'{Buscar19}')

for elemento in Buscar19[:]:
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Buscar19[:-1]:
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Buscar19[:-2]:
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Buscar19[:-3]:
    print (f'{elemento}')
    
print (f'-' * 20)

import re

Texto10 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Version1

Pattern12 = r'\!|\?|\.{2,}|\d{4,}\-[0-9]{2,5}'

Buscar20 = re.sub(Pattern12, '', Texto10)

print (f'{Buscar20}')

# Version2

Pattern13 = r'[^a-zA-Z0-9\s]+'

Buscar21 = re.sub(Pattern13, '', Texto10)

print (f'{Buscar21}')

print (f'-' * 20)

var11 = '3.5'

try:
    Numerito4 = float(var11)
    if (Numerito4.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que se ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que se ingreso no es un numero')
    
print (f'-' * 20)

var12 = '3'

try:
    Numerito5 = float(var12)
    if (Numerito5.is_integer()):
        print (f'Lo que ingresastes es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que se ingreso no es numero')
    
print (f'-' * 20)

import re

Texto11 = "   Hola!!!   mundo@@   123   "

print (f'{Texto11}')

Texto11_Version1 = Texto11.strip()

print (f'{Texto11_Version1}')

Texto11_Version2 = ' '.join(Texto11_Version1.split())

print (f'{Texto11_Version2}')

Texto11_Version3 = Texto11_Version2.lower()

print (f'{Texto11_Version3}')

Texto11_Version4 = re.sub(r'\!|\@|\d+', '', Texto11_Version3)

print (f'{Texto11_Version4}')

print (f'-' * 20)

var13 = 45
var14 = 'Perro'
var15 = [1, 2, 3]
var16 = dict({'Nombre' : ['Erick', 'Josue', 'Karlita']})
var17 = set({})
var18 = tuple(())
var19 = int('5')

try:
    print (f'El resultado de la operacion es {var13 + var14}') #type: ignore
except TypeError:
    print (f'Error, ambos elementos deben ser numeros')
    
print (f'-' * 20)

try:
    print (f'La union es {var15 + var14}') #type: ignore
except TypeError:
    print (f'Error, ambos elementos deben ser numeros')
    
print (f'-' * 20)

try:
    print (f'La suma es {var13 + var19}') #type: ignore
except ValueError:
    print (f'Error, ambos elementos deben ser numeros')
    
print (f'-' * 20)

# Ejemplo type error

try:
    print (f'Hola' * '3') #type: ignore
except TypeError:
    print (f'Error, el segundo elemento debe ser un numero')
    
print (f'-' * 20)

try:
    Numerito6 = int(var14)
    print (f'El numero es {Numerito6}')
except ValueError:
    print (f'Error, no puedes convertir un texto a entero')
    
print (f'-' * 20)

try:
    Buscar22 = var15.index(4) # Esto buscara la posicion donde aparezca el numero 4
    print (f'La posicion es {Buscar22}')
except ValueError:
    print (f'El numero a buscar es correcto, el tipo es el correcto pero el valor es incorrecto, no esta en la lista')
    
print (f'-' * 20)

try:
    Unidad5 = var16['Nombre'][3]
    print (f'La persona del diccionario es  {Unidad5}')
except Exception:
    print (f'Error, el tipo es correcto, pero la persona que buscas no existe, el valor es incorrecto')
    
print (f'-' * 20)

try:
    print (f'El resultado de la division es {50 / 0}')
except Exception as Zero:
    print (f'El error detectado es {str(Zero)}')
    
print (f'-' * 20)

try:
    Resultado1 = var15.index(0) + int(var14) / 0

    print(f'El resultado de la operación es {Resultado1}')

except ValueError:
    print('Error: el valor no es válido.')

except TypeError:
    print('Error: el tipo de dato no es correcto.')

except ZeroDivisionError as Zero2:
    print(f'Error: no se puede dividir por cero. {str(Zero2)}')
    
print (f'-' * 20)

var20 = 3

try:
    print (f'Mi nombre es {'Erick' + var20}') #type: ignore
except TypeError as Txt:
    print (f'Error, ambos elementos deben ser un texto, error detectado {str(Txt)}')
    
print (f'-' * 20)

def Exception1(Numero):
    try:
        Numerito = float(Numero)
        if (Numerito.is_integer()):
            print (f'Lo que ingresaste fue un numero entero')
        else:
            print (f'Lo que ingresaste fue un numero decimal')
    except ValueError:
        print (f'Error, lo que ingresaste no es un numero')

Exception1('Hola')

print (f'-' * 20)

def Exception2(Num1:int, Num2:int) -> int: #type: ignore
    '''Esta sera una funcion que tome dos argumentos y los sume'''
    try:
        Resultado = Num1 + Num2
        print (f'El resultado de la operacion es {Resultado}')
    except (ValueError, TypeError):
        print (f'Error, ambos elementos deben ser numeros enteros')

Exception2(12, 'hola') #type: ignore

print (f'{help(Exception2)}')

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        Resultado = round(Num1 / Num2, 2)
        print (f'El resultado de la operacion es {Resultado}')
    except ZeroDivisionError as Zero3:
        print (f'Error, el divisor no puede ser cero -> {str(Zero3)}')

Exception3(12, 0)

print (f'-' * 20)

Lista_Exception4 = []
Lista_Exception4.append('Erick')
Lista_Exception4.insert(1, 'Josue')
Lista_Exception4.extend(['Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento con indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(3)

print (f'-' * 20)

Diccionario_Exception5 = dict({'Nombre' : 'Erick', 'Edad' : 37})

def Exception5(Clave):
    try:
        print (f'El Valor en la Clave {Clave} es {Diccionario_Exception5[Clave]}')
    except KeyError as Cl1:
        print (f'Error, la clave esta fuera de rango -> {str(Cl1)}')

Exception5("Votante")

print (f'-' * 20)

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
    Documento_Agregar = Docu.write(f'\nDurian')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nFresa Pequeña', f'\nFresa Mediana', f'\nFresa Grande'])
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

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'El menor de los numeros del dataframe es {Data_Frame_Concatenate_Age.min()}')
print (f'El mayor de los numeros del dataframe es {Data_Frame_Concatenate_Age.max()}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Unidad6 = elemento['Nombre']
    Unidad7 = elemento['Edad']
    
    print (f'Mi nombre es {Unidad6} y mi edad {Unidad7} años')
    
print (f'-' * 20)

print (f'{Data_Frame_Concatenate}')

Data_Frame_Concatenate['TOTALITO'] = Data_Frame_Concatenate['Edad'] + 1000

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()
Grupo3_Min_Cant = Grupo3.min()
Grupo3_Max_Cant = Grupo3.max()

print (f'El menor de las personas del dataframe es {Grupo3_Min} con una edad de {Grupo3_Min_Cant} años')
print (f'El mayor de las personas del dataframe es {Grupo3_Max} con una edad de {Grupo3_Max_Cant} años')

print (f'El dataframe tiene {Grupo3.count()} personas')

print (f'La suma de todas las edades del dataframe es {Grupo3.sum()}')

print (f'La media de las edades sumadas es {round(Grupo3.mean(), 2)}')

Grupo4 = Data_Frame_Concatenate.groupby('Nombre')['TOTALITO'].sum()

print (f'La menor de las edades nuevas es {Grupo4.min()}')
print (f'La mayor de las edades nuevas es {Grupo4.max()}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate}')

Lista_DataFrame = list(Data_Frame_Concatenate['Nombre'])
Key2 = [f'Key{i}' for i in range(len(Lista_DataFrame))]

print (f'{Lista_DataFrame}')
print (f'{Key2}')

Diccionario_DataFrame = dict(zip(Key2, Lista_DataFrame))

print (f'-' * 20)

print (f'{Diccionario_DataFrame}')
print (f'{Diccionario_DataFrame.keys()}')
print (f'{Diccionario_DataFrame.values()}')
print (f'{Diccionario_DataFrame.items()}')
print (f'{Diccionario_DataFrame["Key3"]}')
print (f'{Diccionario_DataFrame.get("Key5")}')

'''print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

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

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()'''

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'-' * 20)

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'La cantidad de Filas es {Filas}')
print (f'La cantidad de Columnas es {Columnas}')

Elemento1 = Data_Frame1.loc[0, 'Nombre']
Elemento2 = Data_Frame1.loc[0, 'Edad']
Elemento3 = Data_Frame1.loc[0, 'Votante']
Elemento4 = Data_Frame1.loc[:, 'Edad']
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
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tarifa')
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

print (f'{Cargar_Excel4.head()}')

print (f'-' * 20)

print (f'{Cargar_Excel6.head()}')

print (f'-' * 20)

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'-' * 20)

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

Cargar_Excel3_Sorted['TOTALITO'] = Cargar_Excel3_Sorted['cinco'] + 1000

Grupo5 = Cargar_Excel3_Sorted.groupby('tres')['cinco'].sum()

Grupo5_Min = Grupo5.idxmin()
Grupo5_Max = Grupo5.idxmax()
Grupo5_Min_Cant = Grupo5.min()
Grupo5_Max_Cant = Grupo5.max()

print (f'La persona con menor edad del excel es {Grupo5_Min} y su edad es {Grupo5_Min_Cant} años')
print (f'La persona con menor edad del excel es {Grupo5_Max} y su edad es {Grupo5_Max_Cant} años')

print (f'La cantidad de personas en el excel es {Grupo5.count()}')

print (f'La suma de las edades es {Grupo5.sum()}')

print (f'El promedio de las edades ingresadas es {round(Grupo5.mean(), 2)}')

Grupo6 = Cargar_Excel3_Sorted.groupby('tres')['TOTALITO'].sum()

print (f'La suma de las nuevas edades es {Grupo6.sum()}')

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
print (f'{Array0[2][2:]}')
print (f'{Array0[2][:2]}')
print (f'{Array0[:][2]}')
print (f'{Array0[1][2:3]}')
print (f'{Array0[2][0:None]}')
print (f'{Array0[2][:]}')

print (f'-' * 20)

for i in range(len(Array0)):
    for j in range(len(Array0[i])):
        print (f'{Array0[i][j]}')
        
print (f'-' * 20)

'''import requests

Diccionario_API = {
    'Nombre1' : ["Pistacho", 0],
    'Nombre2' : ["Chicle", 1],
    'Nombre3' : ["Napolitano", 2]
}

Segunda1 = requests.post('http://127.0.0.1:8000/grupo7/unidad1', json=(Diccionario_API))
Segunda2 = Segunda1.json()

print (f'Agregado: {Segunda2}')

print (f'-' * 20)

Tercera1 = requests.put('http://127.0.0.1:8000/grupo7/', json=(Diccionario_API))
Tercera2 = Tercera1.json()

print (f'Reemplazado: {Tercera2}')

print (f'-' * 20)

Cuarta1 = requests.delete('http://127.0.0.1:8000/grupo7/', json=(Diccionario_API))
Cuarta2 = Cuarta1.json()

print (f'Eliminado: {Cuarta2}')

print (f'-' * 20)

Primera1 = requests.get('http://127.0.0.1:8000/grupo7/')
Primera2 = Primera1.json()

print (f'La lista de helados es {Primera2["Helados"]}')'''

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
print (f'{Array1[2:]}')
print (f'{Array1[:2]}')
print (f'{Array1[2:3]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 >= 2]}')

print (f'-' * 20)

Array2 = np.array([[1, 2, 3], [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 2]}')

print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[1, :2]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[1, 2:3]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 >= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
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

Array3 = np.array([[['a', 'e', 'i'], ['d', 'u', 'n']],       [['k', 'f', 'b'], ['c', 'x', 'm']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 2]}')

print (f'{Array3[1, 0, ::2]}')
print (f'{Array3[1, 1, ::3]}')
print (f'{Array3[0, 1, 2:]}')
print (f'{Array3[0, 1, :2]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[1, 1, 2:3]}')
print (f'{Array3[0, 0, 0:None]}')
print (f'{Array3[0, 0, :]}')
print (f'{Array3[Array3 == "c"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],            [[[6, 5, 4], [9, 8, 7]], [[0, 9, 4], [7, 5, 3]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[0, 1, 1, 2]}')

print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[0, 0, 1, ::3]}')
print (f'{Array4[1, 0, 1, 2:]}')
print (f'{Array4[1, 0, 1, :2]}')
print (f'{Array4[0, 0, :, 0]}')
print (f'{Array4[0, 1, 1, 2:3]}')
print (f'{Array4[0, 1, 0, 0:None]}')
print (f'{Array4[0, 1, 0, :]}')
print (f'{Array4[Array4 >= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodados: {Array4_Sorted}')
print (f'Mediado: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[1, 1, 0, 0:None])
Sumita8 = np.sum(Array4_Sorted[1, 1, 0, :])

print (f'La sumita es {Sumita5}')
print (f'La sumita es {Sumita6}')
print (f'La sumita es {Sumita7}')
print (f'La sumita es {Sumita8}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1) #type: ignore

print (f'{Array_Num1}')

Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El menor de los numeros del array es {Array_Num1_Min}')
print (f'El mayor de los numeros del array es {Array_Num1_Max}')

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
print (f'{Array_Zeros[1, 0]}')

print (f'{Array_Zeros[1, ::2]}')
print (f'{Array_Zeros[0, ::3]}')
print (f'{Array_Zeros[0, 2:]}')
print (f'{Array_Zeros[0, :2]}')
print (f'{Array_Zeros[:, 1]}')
print (f'{Array_Zeros[1, 2:3]}')
print (f'{Array_Zeros[1, 0:None]}')
print (f'{Array_Zeros[1, :]}')
print (f'{Array_Zeros[Array_Zeros == 0]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 2]}')

print (f'{Array_Ones[0, ::2]}')
print (f'{Array_Ones[1, ::3]}')
print (f'{Array_Ones[0, 2:]}')
print (f'{Array_Ones[0, :2]}')
print (f'{Array_Ones[:, 2]}')
print (f'{Array_Ones[1, 2:3]}')
print (f'{Array_Ones[1, 0:None]}')
print (f'{Array_Ones[1, :]}')
print (f'{Array_Ones[Array_Ones == 1]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke3"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[0, 1]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value=f'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[4]}')

Lista_Array1 = list([])

for elemento in Array_Gen2[:]:
    Lista_Array1.extend([str(elemento)])
    
print (f'{Array_Gen2}')
print (f'{type(Array_Gen2)}')
print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value=Array4[1, 0, 0, 2])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 2]}')

print (f'-' * 20)

Tupla_Array = tuple(('Uno', 'Dos', 'Tres',))
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre': ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(2, 3), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array["Nombre"][2])

print (f'{Array_Gen4}')

print (f'-' * 20)

print (f'{Array_Gen5}')

print (f'-' * 20)

print (f'{Array_Gen6}')

print (f'-' * 20)

print (f'{Array_Gen6[3]}')

print (f'-' * 20)

Array_Num3 = np.arange(start=1, stop=6, step=1) #type: ignore
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

Lista_Ejemplo17 = list([1, 2, 3, 4, 5])

def Ejercicio52(Lista):
    Pares = []
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Pares.append(elemento)
            
    return Pares

def Ejercicio53(Lista):
    Impares = list([])
    
    for elemento in Lista[:]:
        if (elemento % 2 != 0):
            Impares.extend([elemento])
            
    return Impares

def Ejercicio54(Funcion, Lista):
    return Funcion(Lista)

print (f'Lista de numeros pares {Ejercicio54(Ejercicio52, Lista_Ejemplo17)}')
print (f'Lista de numeros impares {Ejercicio54(Ejercicio53, Lista_Ejemplo17)}')

print (f'-' * 20)

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

print (f'-' * 20)

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Suma = Arr1 + Arr2
Resta = Arr1 - Arr2
Multiplicacion = Arr1 * Arr2
Division = Arr1 / Arr2

Array_Random1_Cien = Array_Random1 + 100

print (f'El resultado de la operacion es {Suma}')
print (f'El resultado de la operacion es {Resta}')
print (f'El resultado de la operacion es {Multiplicacion}')
print (f'El resultado de la operacion es {Division}')
print (f'El resultado de la operacion es {Array_Random1_Cien}')

print (f'-' * 20)

Array_Num8 = np.arange(start=1, stop=21, step=1) #type: ignore

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

print (f'-' * 20)

Lista_Array2 = ['Erick', 'Josue', 'Karlita']

Array5 = np.array(Lista_Array2)

print (f'{Array5}')

print (f'-' * 20)

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1) #type: ignore

Array_Concatenate = np.concatenate([Array6, Array7])

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

print (f'-' * 20)

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

print (f'-' * 20)

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'-' * 20)

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'-' * 20)

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')
print (f'{Array_Random3.ndim}')
print (f'{Array_Random3.shape}')
print (f'{Array_Random3.size}')
print (f'{Array_Random3.dtype}')
print (f'{Array_Random3[1, 0, 2]}')

print (f'-' * 20)

Array_Random3_Column_Min = np.min(Array_Random3, axis=0)
Array_Random3_Column_Max = np.max(Array_Random3, axis=0)
Array_Random3_Row_Min = np.min(Array_Random3, axis=1)
Array_Random3_Row_Max = np.max(Array_Random3, axis=1)

print (f'Los menores de las columnas son {Array_Random3_Column_Min}')
print (f'Los mayores de las columnas son {Array_Random3_Column_Max}')
print (f'Los menores de las filas son {Array_Random3_Row_Min}')
print (f'Los mayores de las filas son {Array_Random3_Row_Max}')

print (f'-' * 20)

Lista_Sorteo1 = ['Erick', 'Josue', 'Karlita']
Lista_Sorteo2 = list(['Carmelo', 'Susanita', 'Roxana'])

Lista_Sorteo3 = Lista_Sorteo1 + Lista_Sorteo2

Ganador1 = np.random.choice(Lista_Sorteo3, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Sorteo3, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Sorteo3, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-' * 20)

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-' * 20)

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
            yield f'El numero {elemento} es par'
        else:
            yield f'El numero {elemento} es impar'

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

def Generado3():
    for elemento in range(0, 5):
        if (elemento == 0):
            yield f'The number is zero'
        elif (elemento == 1):
            yield f'The number is one'
        elif (elemento == 2):
            yield f'The number is two'
        elif (elemento == 3):
            yield f'The number is three'
        elif (elemento == 4):
            yield f'The number is four'
        else:
            continue

Gen3 = Generado3()

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

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'{help(PEPE.Saludar3)}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'-' * 20)

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

print (f'-' * 20)

def primer_nombre(Texto):
    return f'Mi primer nombre es {Texto}'

def segundo_nombre(Texto):
    return f'Mi segundo nombre es {Texto}'

def imprimir_nombre(Funcion, Cadena):
    return Funcion(Cadena)

print (f'{imprimir_nombre(primer_nombre, "Erick")}')
print (f'{imprimir_nombre(segundo_nombre, "Josue")}')

print (f'-' * 20)

def Suma_Externa(Num1):
    def Suma_Interna(Num2:int) -> int:
        return Num1 + Num2
    
    return Suma_Interna(4)

Variable_Sumatoria = Suma_Externa(3)

print (f'El resultado de la sumatoria es {Variable_Sumatoria}')

print (f'-' * 20)

if (PEPE.Par(Variable_Sumatoria) == True):
    print (f'El numero es par')
else:
    print (f'El numero es impar')
    
PEPE.Usuario(Saludar_Dos(), 'MASCUlinO')

print (f'-' * 20)

def Usuario_Externo():
    def Usuario_Interno(Sexo):
        Genero = Sexo.lower()
        if (Genero == 'masculino'):
            return True
        else:
            return False

    return Usuario_Interno('MASCUlinO')

Variable_Usuario = Usuario_Externo()

if (Variable_Usuario == True):
    print (f'YOU ARE A MAN')
else:
    print (f'YOU ARE A WOMAN')
    
print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(23)}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    raise

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
print (f'-' * 20)

def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla(3.5, 200, 'Koala', not True)

print (f'{Funcion_Tupla(3.5, 200, 'Koala', not True)}')
print (f'{Variable_Funcion_Tupla[2]}')
print (f'{Funcion_Tupla(3.5, 200, 'Koala', not True)[3]}')
print (f'{type(Funcion_Tupla(3.5, 200, 'Koala', not True))}')

print (f'-' * 20)

def Promedio2(*args):
    return round(sum(args) / len(args), 2)

print (f'El promedio es {Promedio2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

def Participantes(*participantes):
    for elemento in participantes[:]:
        print (f'El participante es {elemento}')
        
Participantes(
    'Jose',
    'Maria',
    'Jesus',
    'Carlos',
    'Roxana'
)

print (f'-' * 20)

def Funcion_Diccionario(**kwargs):
    print (f'Usuario: {kwargs}')
    
    for clave, valor in kwargs.items():
        print (f'{clave} : {valor}')

Funcion_Diccionario(
    Nombre='Erick',
    Edad=37,
    Votante=True
)

print (f'-' * 20)

def Orden(Num1=15, Num2=1, *args, **kwargs):
    print (f'El resultado de la operacion 1 es: {Num1 + Num2}')
    print (f'El resultado de la operacion 2 es: {sum(args)}')
    
    Acumulador = 0
    
    for _, valor in kwargs.items():
        Acumulador += valor
        
    print (f'El resultado de la operacion 3 es: {Acumulador}')

Orden(
    1, 2,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    num1=30, num2=20
)

print (f'-' * 20)

def Sumatoria2(*numeros):
    return sum(numeros)

print (f'Tu numero favorito es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre} tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos('Erick', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 2)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

if (PEPE.Any_Par == True):
    print (f'Los numeros pares de la lista son {PEPE.Lista_Par}')
    print (f'Los numeros pares de la lista son {list(Anonima3)}')
else:
    print (f'Error, no hay numeros pares en la lista')
    
def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda(*args) - 42
        
    return Tercera
    
@Primera
def Operacion(Numero:int) -> int:
    '''Esto es una funcion que ejecuta una variable global y una local'''
    Local = Numero
    return PEPE.GLOBAL + Local

print (f'El resultado de la operacion es {Operacion(12)}')

def Externa(Nombre):
    def Interna(Apellido):
        return f'Mi nombre es {Nombre} {Apellido}'
    
    return Interna('PEREZ GUTIERREZ')

print (f'{Externa('ERICK JOSUE')}')

print (f'-' * 20)

def Closure_Externo():
    Lista_Closure = list([])
    def Closure_Interno(x):
        Lista_Closure.append(x)
        
        return Lista_Closure
    
    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(25)}')
print (f'{Variable_Closure(31)}')

print (f'-' * 20)

def Closure_Crear_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y

    return Closure_Multiplicador

Mult1 = Closure_Crear_Multiplicador(2)
Mult2 = Closure_Crear_Multiplicador(3)

print (f'El multiplicador es {Mult1(10)}')
print (f'El multiplicador es {Mult2(10)}')

print (f'-' * 20)

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    
    if (Any_Impar == True):
        Anonima = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impar = [num for num in Lista if num % 2 != 0]
        
        print (f'Los numeros impares de la lista son {list(Anonima)}')
        print (f'Los numeros impares de la lista son {Lista_Impar}')
    else:
        print (f'Error, no hay numeros impares de la lista')

Filtrador(PEPE.Lista_Numeros)

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'>>> Esto va antes')
        Segunda()
        print (f'Esto va despues <<<')
        
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

print (f'-' * 20)

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonathan'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)
        
    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    return f'Hola, mi nombre es {Nombre} {Apellido}'

print (f'{Usuario2('Erick', 'Perez')}')

print (f'-' * 20)

from Module_Own import Pokemon1 as Poke1

Objeto9 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto10 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto9.Mostrar()

print (f'-' * 20)

Objeto10.Mostrar()

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto11 = Poke_Kid1(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto11)
Objeto11.Mostrar()

print (f'-' * 20)

class Camara():
    def Tomar_Fotografia(self):
        print (f'Fotografia Tomada')
        
class Reproductor_Musica():
    def Reproducir_Musica(self):
        print (f'Musica Reproducida')
        
class Smartphone(Camara, Reproductor_Musica):
    def Encender_Smartphone(self):
        print (f'Smartphone Encendido')
        
Objeto12 = Smartphone()

Objeto12.Tomar_Fotografia()
Objeto12.Reproducir_Musica()
Objeto12.Encender_Smartphone()

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
        
Objeto13 = Perro('Terry', 9, 5, 'Dobberman', 'Hipertension')

Veterinaria.Mostrar(Objeto13)
Objeto13.Mostrar()

print (f'-' * 20)

class Gato(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente_Activo):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente_Activo = Paciente_Activo
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente_Activo}')
        
Objeto14 = Gato('Messi', 1.8, 1.5, 'Gris', 'No')

Veterinaria.Mostrar(Objeto14)
Objeto14.Mostrar()

print (f'-' * 20)

class Pajaro(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto15 = Pajaro('Polly', 31, 0.4, 'Guacamaya', 'Si')

Veterinaria.Mostrar(Objeto15)
Objeto15.Mostrar()

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
        
Objeto16 = Paladin(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto16.Mostrar()
Atacante.Mostrar(Objeto16)
Defensor.Mostrar(Objeto16)

print (f'-' * 20)

Hija_Padre = issubclass(Poke_Kid1, Poke1)

if (Hija_Padre == True):
    print (f'Poke_Kid1 es una clase hija de la clase Poke1')
else:
    print (f'La clase Poke_Kid no es hija de Poke1')
    
print (f'-' * 20)

Instancia1 = isinstance(Objeto16, Paladin)
Instancia2 = isinstance(Objeto16, Atacante)
Instancia3 = isinstance(Objeto16, Defensor)

print (f'{Instancia1}')
print (f'{Instancia2}')
print (f'{Instancia3}')

print (f'-' * 20)

class A1():
    def Mostrar(self):
        print (f'Hola, buenos dias A1')
        
class E1():
    def Mostrar(self):
        print (f'Hola, buenos dias E1')
        
class B1(E1):
    def Mostrar(self):
        print (f'Hola, buenos dias B1')
        
class C1(A1):
    def Mostrar(self):
        print (f'Hola, buenos dias C1')
        
class D1(B1, C1):
    def Mostrar(self):
        print (f'Hola, buenos dias D1')
        
Objeto17 = D1()

A1.Mostrar(Objeto17)
B1.Mostrar(Objeto17)
C1.Mostrar(Objeto17)
Objeto17.Mostrar()
E1.Mostrar(Objeto17)

print (f'-' * 20)

class Tarjeta():
    def Pagar(self):
        print (f'El pago se realizo en Tarjeta')
        
class Efectivo():
    def Pagar(self):
        print (f'El pago se realizo en Efectivo')
        
class Cripto():
    def Pagar(self):
        print (f'El pago se realizo en Cripto')
        
Objeto18 = Tarjeta()
Objeto19 = Efectivo()
Objeto20 = Cripto()

Objeto18.Pagar()
Objeto19.Pagar()
Objeto20.Pagar()

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
        print (f'Su saldo a la fecha es ${self.__Saldo}')
        
Objeto21 = Cuenta_Bancaria(100)
Objeto21.Depositar(25)
Objeto21.Mostrar()

print (f'Hay una variable privada que tiene su saldo, esto no deberia ser publico {Objeto21.Dinero}')

Objeto21.Dinero = '50,000,000'

Objeto21.Mostrar()

print (f'Hay una variable privada que tiene su saldo, esto no deberia ser publico {Objeto21.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def General(self):
        pass
    
class Sub_Plantilla(Plantilla):
    def Mostrar(self):
        print (f'Este es un metodo interno')
        
    def General(self):
        print (f'Esta es una plantilla obligatoria')
        
Objeto22 = Sub_Plantilla()

Objeto22.Mostrar()

Objeto22.General()

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
        print (f'El retador, eligio un {self.Favorito.Elegir()} para la batalla!!!')
        
Objeto23 = Battle1()

Objeto23.Batallar()

print (f'-' * 20)

class Battle2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El retador, eligio un {self.Favorito.Elegir()} para la batalla')
        
Criatura1 = Bulbasaur()
Objeto24 = Battle2(Criatura1)
Objeto24.Batallar()

Criatura2 = Treekoo()
Objeto25 = Battle2(Criatura2)
Objeto25.Batallar()

Criatura3 = Chikorita()
Objeto26 = Battle2(Criatura3)
Objeto26.Batallar()

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
        
Objeto25 = Pastel1()
Objeto25.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Ingrediente1 = Chocolate()
Objeto26 = Pastel2(Ingrediente1)
Objeto26.Hornear()

Ingrediente2 = Vainilla()
Objeto27 = Pastel2(Ingrediente2)
Objeto27.Hornear()

Ingrediente3 = Fresa()
Objeto28 = Pastel2(Ingrediente3)
Objeto28.Hornear()

print (f'-' * 20)

class Ejemplo_Mio():
    def __init__(self, Nombre):
        self.Nombre = Nombre

    @property
    def Mostrar(self):
        return f'{self.Nombre}'
    
    def Mostrar2(self):
        return f'{self.Nombre}'
    
Objeto29 = Ejemplo_Mio('Erick')

print (f'Mi nombre es {Objeto29.Mostrar}')
print (f'Mi nombre es {Objeto29.Mostrar2()}')

print (f'-' * 20)

var21 = 15

'''var21 += 5
print(var21)'''

'''var21 -= 5

print(var21)'''

'''var21 *= 5

print(var21)'''

'''var21 //= 5

print(var21)'''

'''var21 /= 5

print(var21)'''

'''var21 %= 6

print(var21)'''

'''var21 **= 2

print(var21)'''

for elemento in range(Limite4:= 5):
    print (f'{elemento}')
    
print (f'Mi nombre es {(Nombre := "Erick")}')

Contador = 0

while (Contador < len(Lista_Walrus := ['Erick', 'Josue', 'Karlita'])):
    print (f'El elemento en la posicion {Contador} es {Lista_Walrus[Contador]}')
    Contador += 1
    
from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Una
Variable
Long
String'''

variable4 = Objeto9.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = True, Objeto11.Catched

# Esto es un comentario simple

'''
Esto
Es
Un
docstring 
O
Un
Comentario
Compuesto
'''
print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Sumatoria2(1, 2, 3)} o {Anonima2(Variable_Sumatoria)} o incluso {Objeto10.Cantidad} pokemones')

print (f'-' * 20)

del variable5

print (f'Juana' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Josue' in PEPE.Lista1)
print (f'Gary' not in PEPE.Tupla_Poke)
print (f'{PEPE.Diccionario_Poke["Poke1"]}' in PEPE.Set_Conjunto_Poke1)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables y una declaracion snake_case {snake_case2}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto11.Cantidad, Sumatoria2(1, 2, 1, 1))

print (f'El Cociente de la operacion es {Cociente}')
print (f'El Residuo de la operacion es {Residuo}')

print (f'-' * 20)

print (f'{PEPE.Lista2}')
print (f'{PEPE.Lista2[::2]}')
print (f'{PEPE.Lista2[::3]}')
print (f'{PEPE.Lista2[2:]}')
print (f'{PEPE.Lista2[:2]}')
print (f'{PEPE.Lista2[2:3]}')
print (f'{PEPE.Lista2[0:None]}')
print (f'{PEPE.Lista2[:]}')
print (f'{PEPE.Lista2[:-1]}')
print (f'{PEPE.Lista2[:-2]}')
print (f'{PEPE.Lista2[:-3]}')

print (f'-' * 20)

print (f'{Lista_Uno[1]} eso que esta ahi es un {PEPE.Lista2[2]}? que genial!')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'-' * 20)

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

print (f'{dir(PEPE)}')

Tupla1 = ('Uno', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos',)

print (f'{Tupla1}')

Tupla1 = tuple(('One', 'Two', 'Three',))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Funcion_Tupla)}')

print (f'-' * 20)

print (f'{Tupla1[:]}')
print (f'{Tupla1[:-1]}')
print (f'{Tupla1[:-2]}')
print (f'{Tupla1[1]}')

print (f'-' * 20)

Set_Conjunto1 = {'Agua', 'Hada', Objeto10.Tipo, Objeto10.Tipo, Objeto10.Tipo, Objeto10.Tipo}

Set_Conjunto1.add(f'{Objeto11.Tipo}')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Fairy', 'Rock'})
Set_Conjunto1.add('Water')

print (f'{Set_Conjunto1}')

Set_Conjunto2 = {1, 2, 3, 4, 5}
Set_Conjunto3 = {4, 5}
Set_Conjunto4 = set({8})

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto2 >= Set_Conjunto3}')

print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto3 <= Set_Conjunto2}')

print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')

print (f'-' * 20)

Set_ConjuntoA1 = {1, 2, 3, 4}
Set_ConjuntoB1 = set({4, 5, 6, 7})

print (f'{Set_ConjuntoA1.union(Set_ConjuntoB1)}')
print (f'{Set_ConjuntoA1 | Set_ConjuntoB1}')

print (f'-' * 20)

print (f'{Set_ConjuntoA1.intersection(Set_ConjuntoB1)}')
print (f'{Set_ConjuntoA1 & Set_ConjuntoB1}')

print (f'-' * 20)

print (f'{Set_ConjuntoA1.difference(Set_ConjuntoB1)}')
print (f'{Set_ConjuntoA1 - Set_ConjuntoB1}')

print (f'-' * 20)

print (f'{Set_ConjuntoB1.difference(Set_ConjuntoA1)}')
print (f'{Set_ConjuntoB1 - Set_ConjuntoA1}')

print (f'{Set_ConjuntoA1.symmetric_difference(Set_ConjuntoB1)}')
print (f'{Set_ConjuntoA1 ^ Set_ConjuntoB1}')

print (f'-' * 20)

'''Set_ConjuntoA1.update(Set_ConjuntoB1)

print (f'{Set_ConjuntoA1}')'''

'''Set_ConjuntoA1.intersection_update(Set_ConjuntoB1)

print (f'{Set_ConjuntoA1}')'''

'''Set_ConjuntoA1.difference_update(Set_ConjuntoB1)

print (f'{Set_ConjuntoA1}')'''

'''Set_ConjuntoB1.difference_update(Set_ConjuntoA1)

print (f'{Set_ConjuntoB1}')'''

Set_ConjuntoA1.symmetric_difference_update(Set_ConjuntoB1)

print (f'{Set_ConjuntoA1}')

print (f'-' * 20)

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})

Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, 'ChocoMenta'})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Objeto9.Cantidad,
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
print (f'{Diccionario2["Nombre"][1]}')
print (f'{Diccionario2.get("Edad")[2]}') #type: ignore

print (f'-' * 20)

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3.values()}')
print (f'{Diccionario3.items()}')
print (f'{Diccionario3["Ingresos"]}')
print (f'{Diccionario3.get("Gastos")}')

print (f'-' * 20)

Diccionario1['Nombre'] = variable1

print (f'{Diccionario1}')

Diccionario1_Copia = Diccionario1.copy()

del Diccionario1['Nombre']

Diccionario1.pop('Edad')

print (f'{Diccionario1}')
print (f'El diccionario tiene {len(Diccionario1)} elemento')

print (f'-' * 20)

Diccionario1.clear()

print (f'{Diccionario1}')
print (f'El diccionario tiene {len(Diccionario1)} elemento')

print (f'-' * 20)

print (f'{Diccionario1_Copia}')
print (f'El diccionario tiene {len(Diccionario1_Copia)} elemento')

print (f'-' * 20)

Diccionario1 = dict({1 : "Karlita", 2 : Sumatoria2(1, 2, 1, 1, 2), 3 : not True})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario2["Nombre"][2]} tu no puedes votar ya que solo tienes {Diccionario1.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', f'{PEPE.Diccionario_Poke["Poke2"]}')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = variable2

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
print (f'{Diccionario_Vacio2["Dos"]}')
print (f'{Diccionario_Vacio2.get("Tres")}')

print (f'-' * 20)

Key3 = [f'Key_{i}' for i in range(len(Lista_Uno_Copia))]

Diccionario4 = dict(zip(Key3, Lista_Uno_Copia))

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Key_2"]}')
print (f'{Diccionario4.get("Key_3")}')

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
    Fech3_Formateado = pd.to_datetime(Fech3)
    Cargar_Csv3['date'] = pd.to_datetime(Cargar_Csv3['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato incorrecto')
    exit()
    
Cargar_Csv3['TOTALITO'] = Cargar_Csv3['quantity'] * Cargar_Csv3['price']
    
Encontrado3 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech3_Formateado.date()]

if (Encontrado3.empty):
    print (f'No hay ventas registradas en esta fecha')
else:
    print (f'Genial! encontramos ventas en esta fecha {Fech3_Formateado}')
    
    Grupo7 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo7_Min = Grupo7.idxmin()
    Grupo7_Max = Grupo7.idxmax()
    Grupo7_Min_Cant = Grupo7.min()
    Grupo7_Max_Cant = Grupo7.max()
    
    print (f'En la fecha {Fech3_Formateado} el producto {Grupo7_Min} vendio un total de {Grupo7_Min_Cant} unidades')
    print (f'En la fecha {Fech3_Formateado} el producto {Grupo7_Max} vendio un total de {Grupo7_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron en esta fecha fue {Grupo7.count()}')
    
    print (f'La cantidad de productos vendidos en esta fecha fue {Grupo7.sum()}')
    
    print (f'La media de productos vendidos es {round(Grupo7.mean(), 2)}')
    
    Grupo8 = Encontrado3.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue ${Grupo8.sum()}')
    
    Promedio3 = Grupo8.sum() / Grupo7.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Promedio3, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue ${Grupo8.mean()}')
    
print (f'-' * 20)
    
print (f'{Cargar_Csv3}')

print (f'-' * 20)

Lista_Csv3 = list(Cargar_Csv3['product'])

Key4 = [f'Key{i}' for i in range(len(Lista_Csv3))]

Diccionario5 = dict(zip(Key4, Lista_Csv3))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key1"]}')
print (f'{Diccionario5.get("Key2")}')

print (f'-' * 20)

Division_Baja = 14 // 7
Exponente = 4**3
Modulo = 20 % 6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {round(int(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'El tipo de dato de la variable es {type(variable1)}')
print (f'El tipo de dato de la variable es {type(variable4)}')
print (f'El tipo de dato de la variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de dato de la variable es {type(Objeto10.Catched)}')
print (f'El tipo de dato de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato de la variable es {type(Tupla_Nombres3)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de dato de la variable es {type(Diccionario_DataFrame)}')
print (f'El tipo de dato de la variable es {type(Funcion_Diccionario)}')
print (f'El tipo de dato de la variable es {type(Objeto9)}')
print (f'El tipo de dato de la variable es {type(Array2_Sorted)}')
print (f'El tipo de dato de la variable es {type(Data_Frame_Concatenate)}')
print (f'El tipo de dato de la variable es {type(PEPE)}')

print (f'-' * 20)

if (Diccionario3['Ingresos'] > 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos Altos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] == 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] < 500): #type: ignore
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
    
print (f'-' * 20)

var22 = 'Carlos'
var23 = 20

if (var22 == 'Erick' and var23 > 30):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')
    
print (f'-' * 20)

if (var22 == 'Erick' or var23 > 30):
    print (f'Al menos una de las condiciones se cumple')
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
        
Objeto30 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto9.Nombre)
Objeto31 = Entrenador(PEPE.Tupla_Poke[0], 'Alolah', Objeto10.Nombre)
Objeto32 = Entrenador(PEPE.Tupla_Poke[0], 'Paldea', Objeto11.Nombre)

Objeto30.Desplegar()
Objeto31.Desplegar()
Objeto32.Desplegar()

print (f'-' * 20)

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
    print (f'Gracias por la informacion ingresada')
else:
    print (f'Error, ingrese una cadena de texto')
    
print (f'-' * 20)

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'El indice es {indice} y el elemento es {elemento}')
    
print (f'-' * 20)

variable8 = 'eSteBAN'
variable8_letra = variable8[0]

print (f'{variable8}')
print (f'{variable8.lower()}')
print (f'{variable8.upper()}')
print (f'{variable8.capitalize()}')

print (f'{variable8.lower().index("t")}')
print (f'{variable8.lower().find("n")}')

print (f'La letra {variable8_letra} aparece un total de {variable8.lower().count(variable8_letra)} veces')

print (f'{variable8.lower().startswith(variable8_letra)}')
print (f'{variable8.lower().endswith("n")}')

print (f'{variable8.lower().replace("ban", "POPOTAMO")}')

variable9 = 'esto es una cadena de texto para ver si esto funciona o no'

Lista_variable9 = variable9.split(' ')

for elemento in Lista_variable9[:]:
    print (f'{elemento}')
    
print (f'La cantidad de palabras digitadas es {len(Lista_variable9)}')

print (f'-' * 20)

var24 = 'Erick'
var25 = 'Perez'

if (isinstance(var24, (str))):
    print (f'Lo que ingresaste es un texto')
else:
    print (f'Error, lo que ingresaste no es un texto')
    
'''if (var24.isalpha()):
    print (f'Lo que ingresaste es un texto')
else:
    print (f'Error, lo que ingresaste no es un texto')'''
    
try:
    print (f'Mi nombre es {var24 +  var25}')
except TypeError as Tipo:
    print (f'Error, necesito que ingreses un texto -> {str(Tipo)}')
    
print (f'-' * 20)

var26 = 3.5

if (isinstance(var26, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error de formato')
    
try:
    Numerito7 = float(var26)
    if (Numerito7.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var27 = '3'

if (isinstance(var27, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error de formato')
    
try:
    if (var27.isnumeric()): #type: ignore
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Error de formato')
except AttributeError:
    print (f'Error, el atributo es incorrecto')
    
try:
    Numerito8 = float(var27)
    if (Numerito8.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var28 = 3.5

if (isinstance(var28, (int, float))):
    print (f'Lo que ingresaste es un numero entero o decimal')
else:
    print (f'Error de formatoxxx')
    
try:
    Numerito9 = float(var28)
    if (Numerito9.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except (ValueError, Exception, TypeError):
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)
    
var29 = 'erick123'

if (isinstance(var29, (str, int))):
    print (f'Lo que ingresaste es un numero o texto')
else:
    print (f'Error de formato')
    
if (var29.isalnum()):
    print (f'Lo que ingresaste es un numero o texto')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var30 = '     a     '

if (var30.isspace()):
    print (f'Esto esta compuesto solo por espacios')
else:
    print (f'Error, esto tiene mucho mas que solo espacios')
    
print (f'-' * 20)

var31 = 'eSteBAN'

if (var31.lower().islower()):
    print (f'Esto esta compuesto solamente por letras minusculas')
else:
    print (f'Error de formato')
    
if (var31.upper().isupper()):
    print (f'Esto esta compuesto solamente por letras mayusculas')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var32 = ' '

if (bool(var32) == False):
    print (f'Esto esta vacio')
else:
    print (f'Error, esto no esta vacio')
    
print (f'-' * 20)

print (f'El elemento {PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

Borrado1 = Lista_Csv3.pop(-1)

print (f'El elemento borrado es {Borrado1}')

print (f'-' * 20)

Contador = 0

while (Contador < 5):
    print (f'El elemento es {Contador + 1}')
    Contador += 1

print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'El elemento es {PEPE.Lista_Numeros[Contador] * 100}')
    Contador += 1
    
print (f'-' * 20)

Lista_Animales2 = ['Perro']
Lista_Animales2.append('Tiburon')
Lista_Animales2.insert(2, 'Tigre')
Lista_Animales2.extend(['Lince', 'Tortuga'])

Contador = 0

while (Contador < len(Lista_Animales2)):
    if (Lista_Animales2[Contador] == 'Tigre'):
        print (f'El tigre es el felino mas grande del mundo')
        break
    else:
        Contador += 1
        continue
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Animales2, Tupla1):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento1, elemento2, elemento3, elemento4 in zip(Lista_Animales2, Tupla1, Set_Conjunto_Menu1, Lista_Uno_Copia):
    print (f'{elemento1} -- {elemento2} -- {elemento3} -- {elemento4}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(0 + 3, len(Lista_Animales2)):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(len(Lista_Uno_Copia[:-2])):
    print (f'{elemento}')
    
print (f'-' * 20)

Lista_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'Lista Original: {PEPE.Lista_Numeros}')
print (f'Lista Multiplicada: {Lista_Mult}')

print (f'-' * 20)

Minimo = min(Lista_Mult)
Maximo = max(Lista_Mult)

print (f'El minimo de los numeros es {Minimo}')
print (f'El maximo de los numeros es {Maximo}')

Redondeado = round(14.458795, 2)

print (f'El redondeado del numero 14.458795 es {Redondeado}')

print (f'{bool(False)}')
print (f'{bool(0)}')
print (f'{bool(None)}')
print (f'{bool("")}')

Todo_All = all([Lista_Uno_Copia, Set_Conjunto_Menu1, Tupla3, None])

print (f'{Todo_All}')

print (f'-' * 20)

Sumatoria4 = sum(Lista_Mult)

print (f'El resultado de la sumatoria es {Sumatoria4}')

Uno = int('500')
Dos = str(500)
Tres = float(Uno)
Cuatro = list(Tupla3)
Cinco = tuple(PEPE.Set_Conjunto_Poke1)
Seis = set(Lista_Animales2)

print (f'{type(Uno)}')
print (f'{type(Dos)}')
print (f'{type(Tres)}')
print (f'{type(Cuatro)}')
print (f'{type(Cinco)}')
print (f'{type(Seis)}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto_Poke1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

print (f'-' * 20)

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

print (f'-' * 20)

'''def Exception_Finale():
    while True:
        Numerito = input(f'Ingrese un numero: ')
        try:
            Numerito_Finale = float(Numerito)
            if (Numerito_Finale.is_integer()):
                print (f'Lo que ingresaste fue un numero entero')
                break
            else:
                print (f'Lo que ingresaste fue un numero decimal')
                break
        except (ValueError, TypeError, ZeroDivisionError):
            print (f'Error, lo que ingresaste no es un numero')

Exception_Finale()'''
