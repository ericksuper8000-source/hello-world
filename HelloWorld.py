try:
    import Module_Own as PEPE
except (ModuleNotFoundError, ImportError, Exception):
    print (f'Error, el modulo buscado no fue encontrado')
    raise

# Funciones de orden superior

def Sumar(Numero):
    return Numero + 10

def Multiplicar(Numero):
    return Numero * 10

def Operacion1(Funcion, Numerito):
    return Funcion(Numerito)

print (f'El resultado de la sumatoria es {Operacion1(Sumar, 5)}')
print (f'El resultado de la multiplicacion es {Operacion1(Multiplicar, 5)}')

print (f'-' * 20)

Lista_Nombres1 = ['Erick', 'Josue', 'Karlita']
Lista_Nombres2 = list(['Carmelo', 'Susanita', 'Roxana'])

def Mostrar_Lista1(Lista):
    for elemento in Lista:
        print (f'{elemento}')

def Mostrar_Lista2(Lista):
    for elemento in Lista:
        print (f'{elemento}')
    
def Elegir_Lista(Funcion, Lista):
    return Funcion(Lista)

Elegir_Lista(Mostrar_Lista1, Lista_Nombres1)

print (f'-' * 20)

Elegir_Lista(Mostrar_Lista2, Lista_Nombres2)

print (f'-' * 20)

def Sumar2(Num1, Num2):
    return Num1 + Num2 + 10

def Multiplicar2(Num1, Num2):
    return Num1 * Num2 * 10

def Operacion2(Funcion, Unidad1, Unidad2):
    return Funcion(Unidad1, Unidad2)

print (f'El resultado de la sumatoria es {Operacion2(Sumar2, 2, 3)}')
print (f'El resultado de la multiplicacion es {Operacion2(Multiplicar2, 2, 3)}')

print (f'-' * 20)

Diccionario_Superior = dict({
    'num1' : 4,
    'num2' : 7,
    'num3' : 0,
    'num4' : 1,
    'num5' : 3
})

def Dict_Pares(Diccionario):
    Lista_Pares = []
    
    for Clave, Valor in Diccionario.items():
        if (Valor % 2 == 0):
            Lista_Pares.append(Clave)
        else:
            continue
        
    return Lista_Pares

def Dict_Impares(Diccionario):
    Lista_Impares = list([])

    for Clave, Valor in Diccionario.items():
        if (Valor % 2 != 0):
            Lista_Impares.extend([Clave])
        else:
            continue
        
    return Lista_Impares
        
def Elegir_Dict(Funcion, Diccionario):
    return Funcion(Diccionario)

print (f'Lista de elementos pares: {Elegir_Dict(Dict_Pares, Diccionario_Superior)}')
print (f'Lista de elementos impares: {Elegir_Dict(Dict_Impares, Diccionario_Superior)}')

print (f'-' * 20)

Lista_Animales1 = ['Oso', 'Pez Vela']
Lista_Animales1.append('Leon')
Lista_Animales1.insert(2, 'Avestruz')
Lista_Animales1.extend(['Caracol'])

while (Lista_Animales1):
    print (f'Animales: {Lista_Animales1}')
    del Lista_Animales1[-1]
    
print (f'-' * 20)

def Ejercicio1(Num1:int, Num2:int) -> int:
    '''Esto es un docstring, esta funcion suma dos argumentos y retorna el resultado'''
    return Num1 + Num2

Sample1 = Ejercicio1(12, 7)

print (f'El resultado de la operacion es {Sample1}')

print (f'{help(Ejercicio1)}')

print (f'-' * 20)

def Ejercicio2(Texto = 'Nada que mostrar'):
    return Texto

Sample2 = Ejercicio2()

print (f'{Sample2}')

def Ejercicio3(Num1=100, Num2=50, Num3=40):
    return Num1 + Num2 + Num3

Sample3 = Ejercicio3()

print (f'El resultado de la operacion es {Sample3}')

print (f'-' * 20)

def Ejercicio4(Num1=100, Num2=50, Num3=40):
    return Num1 + Num2 + Num3

Sample4 = Ejercicio4(1, 5, 4)

print (f'El resultado de la operacion es {Sample4}')

print (f'-' * 20)

def Ejercicio5(Num1=100, Num2=50, Num3=40):
    return Num1 + Num2 + Num3

Sample5 = Ejercicio5(1, 5)

print (f'El resultado de la operacion es {Sample5}')

# Funciones con argumentos de longitud variable

def Ejercicio6(*args):
    Promedio = sum(args) / args.__len__()
    return round(Promedio, 2)

Sample6 = Ejercicio6(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print (f'El promedio de los valores agregados es {Sample6}')

print (f'-' * 20)

def Ejercicio7(**kwargs):
    Acumulado = 0
    for _, valor in kwargs.items():
        Acumulado += valor
        
    return Acumulado

print (f'El resultado de sumar los valores del diccionario es {Ejercicio7(
    num1 = 4,
    num2 = 6,
    num3 = 2,
    num4 = 0,
    num5 = 7
)}')

print (f'-' * 20)

def Ejercicio8(Num1, Num2, *args, **kwargs):
    Acumulador = 0
    print (f'La suma de los numeros es {Num1 + Num2}')
    print (f'La suma de los args es {sum(args)}')
    
    for Valor in kwargs.values():
        Acumulador += Valor
        
    print (f'La suma de los kwargs es {Acumulador}')

Ejercicio8(
    2, 3,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    num1=5, num2=20
)

def Ejercicio9(*participantes, **detalles):
    print (f'Los participantes son: ')
    for elemento in participantes:
        print (f'- {elemento}')
        
    print (f'-' * 20)
    
    print (f'Detalles del evento: ')
    for clave, valor in detalles.items():
        print (f'{clave} : {valor}')

Ejercicio9(
    'erick', 'josue', 'karlita',
    fecha='domingo', lugar='iglesia de santa barbara', tema='gran bingo'
)

print (f'-' * 20)

def Ejercicio10(Limite):
    Lista_Fibonacci = [0, 1]
    
    while (len(Lista_Fibonacci) < Limite):
        Proximo = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Proximo)
        
    return Lista_Fibonacci

Sample10 = Ejercicio10(10)

print (f'La lista Fibonacci es {Sample10}')

print (f'-' * 20)

Lista_Primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
Lista_Segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]

def Ejercicio11(Lista1, Lista2):
    Set_Conjunto_Tercera = set({})
    Lista_Tercera = []
    
    for elemento in Lista1:
        if (elemento in Lista2):
            Set_Conjunto_Tercera.add(elemento)
        else:
            continue
        
    Lista_Tercera = list(Set_Conjunto_Tercera)
    
    return Lista_Tercera

Sample11 = Ejercicio11(Lista_Primera, Lista_Segunda)

if (len(Lista_Primera) == 0 or len(Lista_Segunda) == 0):
    print (f'Error, ambas listas deben contener elementos')
else:
    print (f'Lista 1 original: {Lista_Primera}')
    print (f'Lista 2 original: {Lista_Segunda}')
    print (f'La lista de numeros que aparecen en ambas listas pero no se repiten es {Sample11}')
    
print (f'-' * 20)

# Casting implicito

var1 = 3

print (f'{type(var1)}')

var1 += 0.5

print (f'{type(var1)}')

print (f'-' * 20)

# Casting explicito

var1 = '3'
print (f'{type(var1)}')

var1 = int(var1)
print (f'{type(var1)}')

print (f'-' * 20)

Lista_Nombres3 = Lista_Nombres1 + Lista_Nombres2

print (f'Al sumar dos listas el resultado es una concatenacion {Lista_Nombres3}')

Tupla_Nombres1 = ('Erick', 'Josue', 'Karlita',)

Tupla_Nombres2 = 'Carmelo', 'Susanita', 'Roxana',

Tupla_Nombres3 = Tupla_Nombres1 + Tupla_Nombres2

print (f'Al sumar dos tuplas el resultado es una concatenacion {Tupla_Nombres3}')

print (f'-' * 20)

# Truthness

var2 = 0

if (var2):
    print (f'Truthness, esto puede ser positivo, negavito o decimal')
else:
    print (f'Error, si es cero muestra este mensaje')
    
print (f'-' * 20)

var3 = ''

if (var3):
    print (f'Truthness correcto si tiene texto')
else:
    print (f'Error, esto esta vacio')
    
print (f'-' * 20)

Lista_Frutas = []

if (Lista_Frutas):
    print (f'La lista tiene contenido')
else:
    print (f'La lista esta vacia')
    
print (f'-' * 20)

Diccionario_Inventario = {

}

if (Diccionario_Inventario):
    print (f'El diccionario tiene contenido')
else:
    print (f'El diccionario esta vacio')
    
print (f'-' * 20)

var4 = None

if (var4):
    print (f'Esto no es None')
else:
    print (f'Esto es None')
    
print (f'-' * 20)

Lista_Ejercicio1 = [1, 2, 3, 4, 5]

def Ejercicio12(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        
        while (Contador < len(Lista)):
            Contador += 1
            
        return Contador

Sample12 = Ejercicio12(Lista_Ejercicio1)

if (Sample12 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La cantidad de numeros de la lista es {Sample12}')
    
print (f'-' * 20)

def Ejercicio13(Lista):
    Acumulador = 0
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador += elemento
        else:
            continue
        
    return Acumulador

Sample13 = Ejercicio13(Lista_Ejercicio1)

if (not Lista_Ejercicio1):
    print (f'Error, la lista esta vacia')
else:
    if (not Sample13):
        print (f'No hay numeros pares en la lista')
    else:
        print (f'La suma de los numeros pares de la lista es {Sample13}')
        
print (f'-' * 20)

def Ejercicio14(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        
        for elemento in Lista[0:None]:
            Acumulador += elemento
            
        return Acumulador

Sample14 = Ejercicio14(Lista_Ejercicio1)

if (Sample14 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de todos los elementos de la lista es {Sample14}')
    
print (f'-' * 20)

def Ejercicio15(Lista):
    Acumulador = 0
    for elemento in Lista[:-1]:
        Acumulador += elemento
        
    return Acumulador

Sample15 = Ejercicio15(Lista_Ejercicio1)

if (len(Lista_Ejercicio1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de todos los numeros menos el ultimo es {Sample15}')
    
print (f'-' * 20)

def Ejercicio16(Limite):
    Lista_Fibonacci = [0, 1]
    
    while (len(Lista_Fibonacci) < Limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

Sample16 = Ejercicio16(10)

print (f'La lista Fibonacci: {Sample16}')

print (f'-' * 20)

def Ejercicio17(Lista, Numero):
    Founder = False
    if (len(Lista) == 0):
        return None
    else:
        for elemento in Lista[:]:
            if (elemento == Numero):
                Founder = True
                break
            else:
                continue
            
        return Founder

Num1 = 4

Sample17 = Ejercicio17(Lista_Ejercicio1, Num1)

if (Sample17 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample17 == True):
        print (f'El numero {Num1} fue encontrado en la lista')
    else:
        print (f'Error, el numero {Num1} no fue encontrado')
        
print (f'-' * 20)

def Ejercicio18(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    Lista_Resultado = [Menore, Mayore]
    
    return Lista_Resultado

Sample18 = Ejercicio18(Lista_Ejercicio1)

if (len(Lista_Ejercicio1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de la lista es {min(Sample18)}')
    print (f'El mayor de la lista es {max(Sample18)}')
    
print (f'-' * 20)

def Ejercicio19(Lista, Numero):
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

Num2 = 2

Sample19 = Ejercicio19(Lista_Ejercicio1, Num2)

if (Sample19 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample19):
        print (f'La cantidad de numeros mayores que {Num2} es {Sample19}')
    else:
        print (f'No hay ningun numero mayor que {Num2}')
        
print (f'-' * 20)

def Ejercicio20(Lista):
    Lista_Par = []
    Lista_Impar = list([])
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Par.append(elemento)
        else:
            Lista_Impar.extend([elemento])
            
    return Lista_Par, Lista_Impar

Sample20 = Ejercicio20(Lista_Ejercicio1)

if (len(Lista_Ejercicio1) == 0):
    print (f'Error, la lista esta vacia')
else:
    Lista_Num_Pares, Lista_Num_Impares = Sample20
    
    print (f'Lista Original: {Lista_Ejercicio1}')
    print (f'Lista Pares: {Lista_Num_Pares}')
    print (f'Lista Impares: {Lista_Num_Impares}')
    
print (f'-' * 20)

def Ejercicio21(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Mult = []
        
        for elemento in Lista:
            Lista_Mult.append(elemento * 2)
            
        return Lista_Mult

Sample21 = Ejercicio21(Lista_Ejercicio1)

if (Sample21 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Ejercicio1}')
    print (f'Lista Actualizada: {Sample21}')
    
print (f'-' * 20)

'''Lista_Promedio = list([])
Contador = 0

while (Contador < 3):
    while (True):
        Numero = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numero1 = float(Numero)
            if (Numero1.is_integer()):
                print (f'La nota {Contador + 1} es un numero entero')
                Lista_Promedio.append(Numero1)
                break
            else:
                print (f'La nota {Contador + 1} es un numero decimal')
                Lista_Promedio.extend([Numero1])
                break
        except Exception:
            print (f'Error, necesito que ingreses un numero')
    Contador += 1
    
Promedio1 = sum(Lista_Promedio) / len(Lista_Promedio)

print (f'El promedio de las notas ingresadas es {round(Promedio1, 2)}')'''

Lista_Ejercicio2 = [5, -6, 0, -1, -3, 0]

def Ejercicio22(Lista):
    Positivo = 0
    Negativo = 0
    Cero = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Positivo += 1
        elif (elemento < 0):
            Negativo += 1
        else:
            Cero += 1
            
    return Positivo, Negativo, Cero

Sample22 = Ejercicio22(Lista_Ejercicio2)

if (Lista_Ejercicio2):
    Num_Positivos, Num_Negativos, Num_Cero = Sample22
    
    print (f'Cantidad de numeros positivos: {Num_Positivos}')
    print (f'Cantidad de numeros negativos: {Num_Negativos}')
    print (f'Cantidad de numeros ceros: {Num_Cero}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

import re

Lista_Ejercicio3 = [
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
]

def Ejercicio23(Lista):
    Validos = []
    Invalidos = list([])
    
    if (len(Lista) == 0):
        return None
    else:
        Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'
        
        for elemento in Lista[0:None]:
            Buscar = bool(re.fullmatch(Pattern, elemento))
            if (Buscar == True):
                Validos.append(elemento)
            else:
                Invalidos.extend([elemento])
                
        return Validos, Invalidos

Sample23 = Ejercicio23(Lista_Ejercicio3)

if (Sample23 is None):
    print (f'Error, la lista esta vacia')
else:
    Lista_Validos, Lista_Invalidos = Sample23
    
    print (f'Lista Original: {Lista_Ejercicio3}')
    print (f'Lista Validos: {Lista_Validos}')
    print (f'Lista Invalidos: {Lista_Invalidos}')
    
print (f'-' * 20)

def Ejercicio24(Lista):
    Temporal = Lista[0]
    
    for elemento in Lista:
        if (elemento > Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

Sample24 = Ejercicio24(Lista_Ejercicio1)

if (len(Lista_Ejercicio1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero mayor de la lista es {Sample24}')
    
print (f'-' * 20)

def Ejercicio25(Lista):
    Temporal = Lista[0]
    
    for elemento in Lista:
        if (elemento < Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

Sample25 = Ejercicio25(Lista_Ejercicio1)

if (len(Lista_Ejercicio1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero menor de la lista es {Sample25}')
    
print (f'-' * 20)

Lista_Ejercicio4 = list([-15.5, -8, -3.2, -1, 0, 4, 7.5, 12, 19.1, 25])

def Ejercicio26(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        Acumulador = 0
        
        for elemento in Lista:
            if (elemento > 0):
                Contador += 1
                Acumulador += elemento
            else:
                continue
            
        return Contador, Acumulador

Sample26 = Ejercicio26(Lista_Ejercicio4)

if (Sample26 is None):
    print (f'Error, la lista esta vacia')
else:
    Total1, Total1_Suma = Sample26
    
    print (f'El total de numeros positivos es {Total1}')
    print (f'La suma de los numeros positivos es {Total1_Suma}')
    
print (f'-' * 20)

Lista_Ejercicio5 = [65, 70, 54, 80, 69, 66]

def Ejercicio27(Lista):
    Aprobados = 0
    Aprobados_Sum = 0
    Reprobados = 0
    
    for elemento in Lista:
        if (elemento >= 70):
            Aprobados += 1
            Aprobados_Sum += elemento
        else:
            Reprobados += 1
            
    return Aprobados, Aprobados_Sum, Reprobados

Sample27 = Ejercicio27(Lista_Ejercicio5)

if (len(Lista_Ejercicio5) == 0):
    print (f'Error, la lista esta vacia')
else:
    Total_Aprobados, Total_Aprobados_Sum, Total_Reprobados = Sample27
    
    print (f'Estudiantes aprobados: {Total_Aprobados}')
    print (f'Estudiantes aprobados sumatoria: {Total_Aprobados_Sum}')
    print (f'Estudiantes reprobados: {Total_Reprobados}')
    
print (f'-' * 20)

Lista_Ejercicio6 = list([15, 0, 8, 2, 0, 25, 4])

def Ejercicio28(Lista):
    if (len(Lista) == 0):
        return None
    else:
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
                
        return Agotados, Stock_Bajo, Stock_Alto, Stock_Bajo_Sum, Stock_Alto_Sum

Sample28 = Ejercicio28(Lista_Ejercicio6)

if (Sample28 is None):
    print (f'Error, la lista esta vacia')
else:
    Prod_Agotados, Prod_Stock_Bajo, Prod_Stock_Alto, Prod_Stock_Bajo_Sum, Prod_Stock_Alto_Sum = Sample28
    
    print (f'Lista Productos Agotados: {Prod_Agotados}')
    print (f'Lista Productos Stock Bajo: {Prod_Stock_Bajo}')
    print (f'Lista Productos Stock Alto: {Prod_Stock_Alto}')
    print (f'Lista Productos Stock Bajo Sumatoria: {Prod_Stock_Bajo_Sum}')
    print (f'Lista Productos Stock Alto Sumatoria: {Prod_Stock_Alto_Sum}')
    print (f'Sumatoria productos con stock: {Prod_Stock_Bajo_Sum + Prod_Stock_Alto_Sum}')
    
print (f'-' * 20)

Diccionario_Lenguaje = {"python": 4, "java": 2, "c++": 2, "go": 3}

def moda_terminos(Diccionario):
    if (len(Diccionario) == 0):
        return None
    else:
        Lista_Adicionales = []
        Clave  = next(iter(Diccionario))
        Valor = Diccionario[Clave]
        
        for indice, elemento in Diccionario.items():
            if (elemento > Valor):
                Valor = elemento
                Clave = indice
            
        for indice, elemento in Diccionario.items():
            if (Valor == elemento):
                Lista_Adicionales.append(indice)
            
        if (len(Lista_Adicionales) == 1):
            return Clave
        else:
            return Lista_Adicionales

Sample29 = moda_terminos(Diccionario_Lenguaje)

if (Sample29 is None):
    print (f'Error, el diccionario esta vacio')
else:
    print (f'{Sample29}')
    
print (f'-' * 20)

def Ejercicio30(Limite):
    Lista_Fibonacci = [0, 1]
    
    while (len(Lista_Fibonacci) < Limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

Sample30 = Ejercicio30(10)

print (f'La lista Fibonacci es {Sample30}')

print (f'-' * 20)

Diccionario_Lenguaje_Sorted = dict(sorted(Diccionario_Lenguaje.items(), key=lambda item : item[1]))
Diccionario_Lenguaje_Mayor = max(Diccionario_Lenguaje.items(), key=lambda item: item[1])

print (f'{Diccionario_Lenguaje}')

print (f'{Diccionario_Lenguaje_Sorted}')

print (f'{Diccionario_Lenguaje_Mayor}')

print (f'-' * 20)

Lista_Ejercicio7 = [12, 8, 5, 1, 7, 2, 10]

def Ejercicio31(Lista):
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] == 0):
            return Contador
        else:
            Contador += 1
            continue
        
    return None

Sample31 = Ejercicio31(Lista_Ejercicio7)

if (len(Lista_Ejercicio7) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample31 is None):
        print (f'No hay ningun articulo agotado en el inventario')
    else:
        print (f'El primer producto agotado aparece en la posicion {Sample31}')
        
print (f'-' * 20)

Lista_Ejercicio8 = list([120, 350, 80, 600, 150, 700])

def Ejercicio32(Lista, Num):
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] > Num):
            return Contador
        else:
            Contador += 1
            continue
        
    return None

Limite1 = 1500

Sample32 = Ejercicio32(Lista_Ejercicio8, Limite1)

if (len(Lista_Ejercicio8) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample32 is None):
        print (f'No hay ninguna venta superior al monto ${Limite1}')
    else:
        print (f'La primera venta superior al monto ${Limite1} aparece en la posicion {Sample32} y el monto es ${Lista_Ejercicio8[Sample32]}')
        
print (f'-' * 20)

Diccionario_Lenguaje_Mayor2 = max(Diccionario_Lenguaje.items(), key=lambda item: item[1])

print (f'{Diccionario_Lenguaje_Mayor2}')

print (f'-' * 20)

# Manera 1

Lista_Ejercicio9 = list([10, 1, 2, 4, 3, 5, 6])

def Ejercicio33(Lista):
    for i in range(0, len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                return Lista[i]
            else:
                continue
            
    return None

Sample33 = Ejercicio33(Lista_Ejercicio9)

if (Lista_Ejercicio9):
    if (Sample33 is None):
        print (f'No hay numeros repetidos en la lista')
    else:
        print (f'El primer numero repetido es {Sample33}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)
    
# Manera 2

Lista_Ejercicio10 = list([10, 2, 1, 4, 3, 5, 6])

def Ejercicio34(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            
    return None

Sample34 = Ejercicio34(Lista_Ejercicio10)

if (Lista_Ejercicio10):
    if (Sample34 is None):
        print (f'No hay numeros repetidos en la lista')
    else:
        print (f'El primer numero repetido es {Sample34}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejercicio11 = [90, 89, 79, 20]

def Ejercicio35(Lista):
    Posicion = 0
    Anterior = 0
    Numero = 0
    
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] < Lista[i]):
            Posicion = i
            Anterior = Lista[i - 1]
            Numero = Lista[i]
            return Posicion, Anterior, Numero
        else:
            continue
        
    return None

Sample35 = Ejercicio35(Lista_Ejercicio11)

if (len(Lista_Ejercicio11) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample35 is None):
        print (f'No hay un aumento de ventas respecto al dia anterior')
    else:
        Posicion, Num_Anterior, Num_Actual = Sample35
        
        print (f'La posicion donde sucede un aumento en comparacion con el dia anterior es {Posicion}')
        print (f'Numero anterior: {Num_Anterior}')
        print (f'Numero actual: {Num_Actual}')
        
print (f'-' * 20)

Lista_Ejercicio12 = [100, 97, 95, 80, 78]

def Ejercicio36(Lista, Num):
    Posicion = 0
    Anterior = 0
    Actual = 0
    
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] - Lista[i] >= Num):
            Posicion = i
            Anterior = Lista[i - 1]
            Actual = Lista[i]
            return Posicion, Anterior, Actual
        else:
            continue
        
    return None

Limite2 = 10

Sample36 = Ejercicio36(Lista_Ejercicio12, Limite2)

if (Lista_Ejercicio12):
    if (Sample36 is None):
        print (f'No ha habido ninguna caida de temperatura drastica en la ultima hora')
    else:
        Posicion2, Num_Anterior2, Num_Actual2 = Sample36
        print (f'Alerta! acaba de suceder una caida de {Num_Anterior2 - Num_Actual2} grados en la ultima hora')
        print (f'Posicion de la caida: {Posicion2}')
        print (f'Temperatura anterior: {Num_Anterior2}')
        print (f'Temperatura actual: {Num_Actual2}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejercicio13 = list([1, 1, 0, 1, 3])

def Ejercicio37(Lista):
    for i in range(0 + 2, len(Lista)):
        if (Lista[i - 2] < Lista[i - 1] > Lista[i]):
            return i - 1
        else:
            continue
        
    return None

Sample37 = Ejercicio37(Lista_Ejercicio13)

if (len(Lista_Ejercicio13) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample37 is None):
        print (f'En la lista de numeros no sucede un pico')
    else:
        print (f'El pico sucede en la posicion {Sample37} y con el numero {Lista_Ejercicio13[Sample37]}')
        
print (f'-' * 20)

# Consultar valores ✅ Consultar.

Capitales1 = {"Costa Rica": "San José", "México": "Ciudad de México", "Italia" : "Roma", "Argentina": "Buenos Aires", "España": "Madrid"}

Ubicado1 = Capitales1.get('Italia')

if (Ubicado1 is None):
    print (f'Italia no aparece en el diccionario')
else:
    print (f'La capital de italia es {Ubicado1}')
    
print (f'-' * 20)

Productos1 = {"Laptop": 1200, "Mouse": 25, "Teclado": 45, "Monitor": 300}

def Ejercicio38(Dict, Prod):
    Ubicado1 = Dict.get(Prod)
    
    if (Ubicado1):
        return Ubicado1
    else:
        return None

Item1 = 'Escoba'

Sample38 = Ejercicio38(Productos1, Item1)

if (Productos1):
    if (Sample38 is None):
        print (f'El producto {Item1} no existe en el diccionario')
    else:
        print (f'El precio del articulo {Item1} es ${Sample38}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

# Actualizar elementos ✅ Actualizar.

Productos2 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300
}

def Ejercicio39(Dict, Articulo, Precio):
    Ubicado1 = Dict.get(Articulo)
    
    if (Ubicado1 is None):
        return False
    else:
        Dict[Articulo] = Precio
        return True

Item2 = 'Borrador'
Item2_Price = 55

Sample39 = Ejercicio39(Productos2, Item2, Item2_Price)

if (len(Productos2) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample39 == True):
        print (f'El precio del articulo {Item2} fue actualizado exitosamente!')
    else:
        print (f'Error, el articulo {Item2} no existe en el diccionario')
        
print (f'-' * 20)

# Agregar elementos ✅ Agregar.

Productos3 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio40(Dict, Articulo, Precio):
    Ubicado1 = Dict.get(Articulo)
    
    if (Ubicado1):
        return False
    else:
        Dict[Articulo] = Precio
        return Dict

Item3 = 'Escoba'
Item3_Price = '5'

Sample40 = Ejercicio40(Productos3, Item3, Item3_Price)

if (Productos3):
    if (Sample40 == False):
        print (f'El producto {Item3} ya existe en el diccionario, no puede agregarse nuevamente')
    else:
        print (f'El articulo {Item3} fue agregado, nuevo diccionario: {Sample40}')
else:
    print (f'Error el diccionario esta vacio')
    
print (f'-' * 20)

# Eliminar elementos ✅ Eliminar.

Productos4 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio41(Dict, Articulo):
    Ubicado1 = Dict.get(Articulo)
    
    if (Ubicado1 is None):
        return False
    else:
        Dict.pop(Articulo)
        return Dict

Item4 = 'Mouse'

Sample41 = Ejercicio41(Productos4, Item4)

if (len(Productos4) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample41 == False):
        print (f'Error, el articulo {Item4} no existe, no se puede eliminar')
    else:
        print (f'El articulo {Item4} fue eliminado : {Sample41}')
        
print (f'-' * 20)

Productos5 = {
    "Laptop": 100,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 90,
    "Impresora": 180
}

def Ejercicio42(Dict):
    Clave = next(iter(Dict))
    Valor = Dict[Clave]
    
    for indice, elemento in Dict.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    return Clave

Sample42 = Ejercicio42(Productos5)

if (Productos5):
    print (f'El producto mas caro del inventario es {Sample42}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Ventas1 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio43(Dict, Num):
    Dict_Sorted = dict(sorted(Dict.items(), key=lambda item : item[1]))
    for clave, valor in Dict_Sorted.items():
        if (valor > Num):
            return clave, valor
        else:
            continue
        
    return None

Limite3 = 400

Sample43 = Ejercicio43(Ventas1, Limite3)

if (len(Ventas1) == 0):
    print (f'Error, el diccinario esta vacio')
else:
    if (Sample43 is None):
        print (f'No hay ninguna venta superior al limite ${Limite3}')
    else:
        Dia, Monto = Sample43
        print (f'El dia que supero el limite fue {Dia} y el monto fue ${Monto}')
        
print (f'-' * 20)

Ventas1_Max = max(Ventas1.items(), key=lambda item : item[1])
Ventas1_Sorted = dict(sorted(Ventas1.items(), key=lambda item : item[1]))

print (f'{Ventas1_Max}')
print (f'{Ventas1_Sorted}')

print (f'-' * 20)

Productos6 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio44(Dict, Num):
    Contador = 0
    for elemento in Dict.values():
        if (elemento > Num):
            Contador += 1
        else:
            continue
        
    return Contador

Limite4 = 2000

Sample44 = Ejercicio44(Productos6, Limite4)

if (Productos6):
    if (Sample44):
        print (f'La cantidad de precios que superan el limite ${Limite4} es {Sample44}')
    else:
        print (f'No hay ningun producto que supere en precio el monto ${Limite4}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Ventas2 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio45(Dict):
    Acumulador = 0
    for valor in Dict.values():
        Acumulador += valor
        
    return Acumulador

Sample45 = Ejercicio45(Ventas2)

if (Ventas2):
    print (f'La suma de todas las ventas es ${Sample45}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Ventas3 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio46(Dict, Num):
    Acumulador = 0
    for elemento in Dict.values():
        if (elemento > Num):
            Acumulador += elemento
        else:
            continue
        
    return Acumulador

Limite5 = 900

Sample46 = Ejercicio46(Ventas3, Limite5)

if (len(Ventas3) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample46):
        print (f'La suma de los montos superiores al limite es ${Sample46}')
    else:
        print (f'No hay ventas superiores al limite ${Limite5}')
        
print (f'-' * 20)

Productos7 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio47(Dict, Num):
    Contador = 0
    Acumulador = 0

    for valor in Dict.values():
        if (valor > Num):
            Contador += 1
            Acumulador += valor
        else:
            continue
        
    return Contador, Acumulador
        
Limite6 = 2000

Sample47 = Ejercicio47(Productos7, Limite6)

if (len(Productos7) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Contador, Acumulador = Sample47
    
    if (Contador):
        print (f'La cantidad de numeros mayores que el limite es {Contador}')
        print (f'La suma de los numeros mayores que el limite es {Acumulador}')
    else:
        print (f'No hay ningun producto que supere el limite')
        
print (f'-' * 20)

Productos8 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio48(Dict, Num):
    Dict_Sorted = dict(sorted(Dict.items(), key=lambda item : item[1]))
    for clave, valor in Dict_Sorted.items():
        if (valor > Num):
            return clave, valor
        else:
            continue
        
    return None

Limite7 = 2000

Sample48 = Ejercicio48(Productos8, Limite7)

if (Productos8):
    if (Sample48 is None):
        print (f'No hay ningun producto que supere el monto limite')
    else:
        Articulo1, Precio1 = Sample48
        print (f'Producto: {Articulo1}')
        print (f'Precio: ${Precio1}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Lista_Ejercicio14 = ["python", "java", "python", "c++", "java", "python", "go", "c++", "python"]

def contar_terminos(Lista):
    Diccionario_Lenguaje = dict({'python' : 0, 'java' : 0, 'c++' : 0, 'go' : 0})
    
    for elemento in Lista:
        if (elemento in Diccionario_Lenguaje):
            Diccionario_Lenguaje[elemento] += 1
        else:
            continue
        
    return Diccionario_Lenguaje
    
    

Sample49 = contar_terminos(Lista_Ejercicio14)

if (len(Lista_Ejercicio14) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'{Sample49}')
    
print (f'-' * 20)

'''def Floating1(Numero):
    Resultado = Numero + 10 * 3
    print (f'El resultado de la operacion es {Resultado}')

Floating1(PEPE.Flotante1)

Floating2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Floating2}')

def Floating3(Cadena):
    Cadena_Formateada = Cadena.replace(' ', '')
    
    if (isinstance(Cadena_Formateada, (str))):
        if (Cadena_Formateada.isalpha()):
            print (f'Lo que ingresaste es un texto {Cadena_Formateada}')
        else:
            print (f'Lo que ingresaste no es un texto')

Floating3(PEPE.Floating3)

print (f'-' * 20)

def Floating4(Cadena):
    Cadena_Splitted = Cadena.split(' ')
    
    for elemento in Cadena_Splitted:
        print (f'{elemento}')
        
    print (f'La cantidad de palabras digitadas es {len(Cadena_Splitted)}')

Floating4(PEPE.Floating4)'''

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio(Lista):
    for elemento in range(0, Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Lista.append(Alumno)
        
    return Lista

Sample50 = Colegio(Lista_Alumnos)

print (f'La lista de estudiantes es {Sample50}')'''

'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.extend([Estudiante])
        
    Lista.sort(key = lambda num : num[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes es {Menore}, su edad es {Lista[0][1]} años')
    print (f'El mayor de los estudiantes es {Mayore}, su edad es {Lista[-1][1]} años')

Sample50 = Colegio(Lista_Alumnos)'''

Dict_Num = {"a":5, "b":3, "c":1, "d":3}

def palabras_mas_frecuentes_que(Diccionario, Numero):
    Contador = 0
    Lista_Palabras = []
    for clave, valor in Diccionario.items():
        if (valor > Numero):
            Contador += 1
            Lista_Palabras.append(clave)
        else:
            continue
        
    return Contador, Lista_Palabras

Limite8 = 2

Sample50 = palabras_mas_frecuentes_que(Dict_Num, Limite8)

if (Dict_Num):
    Contador2, Lista_Palabras = Sample50
    Tupla0 = tuple((Contador2, Lista_Palabras,))
    
    if (Contador2):
        print (f'{Tupla0}')
    else:
        print (f'No hay ninguna palabra cuyo valor sea superior al limite {Limite8}')
        print (f'{Tupla0}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Dict_Letras = {"a":5, "b":3, "c":1}

def resumen_frecuencias(Diccionario):
    Tupla_Resultado = tuple(())
    Acumulador = 0
    Contador = 0
    for clave, valor in Diccionario.items():
        if (clave):
            Acumulador += valor
            Contador += 1
        else:
            continue
        
    Tupla_Resultado = Acumulador, Contador,
    
    return Tupla_Resultado 

Sample51 = resumen_frecuencias(Dict_Letras)

if (len(Dict_Letras) == 0):
    print (f'{Sample51}')
else:
    print (f'{Sample51}')
    
# Para sacar la cantidad de elementos tambien pude haber usado esto, lo agrego como referencia, no es parte del codigo
print (f'{len(Dict_Letras)}')

print (f'-' * 20)

Diccionario_Lenguaje2 = {"a":5, "b":3, "c":1, "d":3, "e":5}

def buscar_por_frecuencia(Diccionario, Numero):
    Lista_Resultado = list([])
    
    for clave, valor in Diccionario.items():
        if (valor == Numero):
            Lista_Resultado.append(clave)
        else:
            continue
        
    return Lista_Resultado

Objetivo = 10

Sample52 = buscar_por_frecuencia(Diccionario_Lenguaje2, Objetivo)

if (Diccionario_Lenguaje2):
    if (Sample52):
        print (f'Lista: {Sample52}')
    else:
        print (f'Lista: {Sample52}')
else:
    print (f'vacio: []')
    
# clase educacion it

class Persona1():
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        
    def nombre_completo(self):
        print (f'Mi nombre completo es {self.__nombre} {self.__apellido}')

class Estudiante1(Persona1):
    def __init__(self, nombre, apellido, carrera):
        super().__init__(nombre, apellido)
        self.__carrera = carrera
        
    def mostrar_carrera(self):
        print (f'Su carrera es: {self.__carrera}')
        
    # Con esto cambiamos el valor de la carrera con un set
    def set_carrera(self, nueva_carrera):
        self.__carrera = nueva_carrera
        
Objeto1 = Estudiante1('Erick', 'Perez', 'DevOps')

Objeto1.nombre_completo()
Objeto1.mostrar_carrera()

Objeto1.set_carrera('Mecanica')

Objeto1.mostrar_carrera()

print (f'-' * 20)

# Paquetes o librerias, modulos

print (f'{PEPE.sumar(12, 7)}')
print (f'{PEPE.restar(12, 7)}')
print (f'{PEPE.multiplicar(12, 7)}')

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

# Digamos que tengamos varios modulos que son de una misma categoria, por ejemplo un modulo aritmetica y un modulo algebra, estos se pueden
# organizar bajo una misma categoria matematica, ambos modulos se pueden guardar bajo el mismo modulo
# Un paquete es un conjunto de modulos, cuyos modulos solucionan problemas similares
# Se debe agregar ambos archivos en un folder, dentro de este folder se debe agregar un archivo __init__.py. al agregar esto, se convierte en un paquete

from Paquete.Sub_Paquete import Segundo as PEPE3

variable_PEPE3 = PEPE3

# Frameworks son paquetes, uso de Paquetes de terceros
# pip install seguido del nombre directamente en la terminal

import openpyxl
import requests
import psutil
import tabulate
import pymysql
import flask
import django

print (f'-' * 20)

def Ejercicio49(Limite):
    Lista_Fibonacci = list([0, 1])
    
    while (len(Lista_Fibonacci) < Limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

print (f'La lista Fibonacci es {Ejercicio49(10)}')

print (f'-' * 20)

print (f'{Diccionario_Lenguaje2}')

Diccionario_Lenguaje2_Sorted = dict(sorted(Diccionario_Lenguaje2.items(), key=lambda item : item[1]))

print (f'{Diccionario_Lenguaje2_Sorted}')

Diccionario_Lenguaje2_Sorted_Mayor = max(Diccionario_Lenguaje2_Sorted.items(), key=lambda item : item[1])
Diccionario_Lenguaje2_Sorted_Menor = min(Diccionario_Lenguaje2_Sorted.items(), key=lambda item : item[1])

print (f'{Diccionario_Lenguaje2_Sorted_Mayor}')
print (f'{Diccionario_Lenguaje2_Sorted_Menor}')

print (f'-' * 20)

'''paises = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}

def Ejericicio50(Diccionario):
    while (True):
        codigo = input(f'Ingrese el codigo de un pais: ')
        Ubicado1 = Diccionario.get(codigo)
        if (Ubicado1 is None):
            print (f'Error, el codigo ingresado no pertenece a ningun pais')
        else:
            return Ubicado1

Sample53 = Ejericicio50(paises)

if (len(paises) == 0):
    print (f'Error, El diccionario esta vacio')
else:
    print (f'El codigo pertenece al pais: {Sample53}')'''
    
print (f'-' * 20)

class persona2():
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
        return self.nombre

Objeto2 = persona2('Erick Perez')

print (f'Mi nombre es {Objeto2}')

print (f'-' * 20)

class colores():
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __repr__(self):
        return self.nombre

lista_colores = [
    colores('rojo'),
    colores('azul'),
    colores('amarillo')
]

print (f'La lista de colores es {lista_colores}')

print (f'-' * 20)

class inventario():
    def __init__(self):
        self.productos = list([])
        
    def __len__(self):
        return len(self.productos)
        
Objeto3 = inventario()

Objeto3.productos.append('manzana')
Objeto3.productos.insert(1, 'uvas')
Objeto3.productos.extend(['pera'])

print (f'La lista tiene un total de {len(Objeto3)} elementos')

print (f'-' * 20)

class igualdad():
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __eq__(self, otro):
        return self.nombre == otro.nombre

Objeto4 = igualdad('Panda Rojo')
Objeto5 = igualdad('Panda Rojo')

if (Objeto4 == Objeto5):
    print (f'Ambos objetos son iguales')
else:
    print (f'Error, los objetos no son iguales')
    
print (f'-' * 20)

class caja():
    def __init__(self, peso):
        self.peso = peso
        
    def __add__(self, otro):
        return self.peso + otro.peso

Objeto6 = caja(5)
Objeto7 = caja(3)

print (f'El resultado de la suma es {Objeto6 + Objeto7}')

print (f'-' * 20)

class armario():
    def __init__(self):
        self.productos = [
            'camiseta',
            'pantalones',
            'abrigo'
        ]
        
    def __getitem__(self, Indice):
        return self.productos[Indice]
        
Objeto8 = armario()

print (f'El elemento en la posicion 0 es {Objeto8[0]}')
print (f'El elemento en la posicion 1 es {Objeto8[1]}')
print (f'El elemento en la posicion 2 es {Objeto8[2]}')

print (f'-' * 20)

class panaderia():
    def __init__(self):
        self.panes = list({
            'baguette',
            'croissant',
            'donas'
        })
        
    def __iter__(self):
        return iter(self.panes)
        
Objeto9 = panaderia()

for indice, elemento in enumerate(Objeto9, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

Diccionario_API = dict({'Nombre' : ["Natilla", "Mora", "Pastel", "ChocoFresa"], 'Indice' : [0, 1, 2, 3]})

'''import requests

Unidad3 = requests.post('http://127.0.0.1:8000/grupo1/unidad1', json=(Diccionario_API))
Unidad4 = Unidad3.json()

print (f'Agregado : {Unidad4}')

print (f'-' * 20)

Unidad5 = requests.put('http://127.0.0.1:8000/grupo1/', json=(Diccionario_API))
Unidad6 = Unidad5.json()

print (f'Reemplazado: {Unidad6}')

print (f'-' * 20)

Unidad7 = requests.delete('http://127.0.0.1:8000/grupo1/', json=(Diccionario_API))
Unidad8 = Unidad7.json()

print (f'Eliminado: {Unidad8}')

print (f'-' * 20)

Unidad1 = requests.get('http://127.0.0.1:8000/grupo1/')
Unidad2 = Unidad1.json()

print (f'Lista de Helados: {Unidad2["Helados"]}')
'''

var5 = '3'

if (isinstance(var5, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')
    
if (var5.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')
    
if (var5.isdecimal()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')
    
try:
    Numerito1 = float(var5)
    if (Numerito1.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var6 = 3.5

if (isinstance(var6, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, lo que ingresaste no es un numero decimal')
    
try:
    Numerito2 = float(var6)
    if (Numerito2.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var7 = 3

if (isinstance(var7, (int, float))):
    print (f'Lo que ingresastes es un numero entero o decimal')
else:
    print (f'Esto es un error de formato')
    
try:
    Numerito3 = float(var7)
    if (Numerito3.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
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

Texto1_Version5 = Texto1_Version4.title()

print (f'{Texto1_Version5}')

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
    print (f'Genial! encontramos ventas')
    
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Min} vendido {Grupo1_Min_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Max} vendido {Grupo1_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que nos compraron en esta fecha fue {Grupo1.count()}')
    
    print (f'La cantidad de productos vendidios en esta fecha fue {Grupo1.sum()}')
    
    print (f'La media promedia de productos vendidos en esta fecha fue {round(Grupo1.mean(), 2)}')
    
    Grupo2 = Encontrado1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue ${Grupo2.sum()}')
    
    Promedio1 = Grupo2.sum() / Grupo1.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Promedio1, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Grupo2.mean(), 2)}')
    
print (f'-' * 20)

for indice, elemento in Cargar_Csv1.iterrows():
    Unidad1 = elemento['product']
    Unidad2 = elemento['price']
    
    print (f'El producto {Unidad1} tiene un valor de ${Unidad2}')
    
print (f'-' * 20)

Lista_Csv1 = list(Cargar_Csv1['product'])
Key1 = [f'Key{i}' for i in range(len(Lista_Csv1))]

print (f'{Lista_Csv1}')
print (f'{Key1}')

Diccionario0 = dict(zip(Key1, Lista_Csv1))

print (f'{Diccionario0}')
print (f'{Diccionario0.keys()}')
print (f'{Diccionario0.values()}')
print (f'{Diccionario0.items()}')
print (f'{Diccionario0["Key5"]}')
print (f'{Diccionario0.get("Key6")}')

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

Pattern1 = r'[A-Za-z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar1 = re.findall(Pattern1, Texto2)

print (f'{Buscar1}')

for elemento in enumerate(Buscar1):
    print (f'{elemento[0]} -- {elemento[1]}')
    
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

print (f'-' * 20)

# Version2

Pattern3 = r'[^A-Za-z0-9\s]'

Buscar3 = re.sub(Pattern3, '', Texto3)

print (f'{Buscar3}')

print (f'-' * 20)

# Version3

import re

Texto3_temp1 = Texto3

Pattern4 = r'[A-Za-z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Correos1 = re.findall(Pattern4, Texto3)

print (f'{Correos1}')

for i, email in enumerate(Correos1, start=1):
    Texto3_temp1 = Texto3_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto3_temp1}')

Pattern5 = r'\!|\?|\.{2,}|\d{2,4}\-[0-9]{3,}'

Texto3_temp2 = re.sub(Pattern5, '', Texto3_temp1)

print (f'{Texto3_temp2}')

for i, email in enumerate(Correos1, start=1):
    Texto3_temp2 = Texto3_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto3_temp2}')

print (f'-' * 20)

import re

Texto4 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Texto4_Temp1 = Texto4

Pattern6 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos2 = re.findall(Pattern6, Texto4)

print (f'{Correos2}')

for i, email in enumerate(Correos2, start=1):
    Texto4_Temp1 = Texto4_Temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto4_Temp1}')

Pattern7 = r'\!|\?'

Texto4_Temp2 = re.sub(Pattern7, '', Texto4_Temp1)

print (f'{Texto4_Temp2}')

for i, email in enumerate(Correos2, start=1):
    Texto4_Temp2 = Texto4_Temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto4_Temp2}')

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

'''Lista_Promedios = list([])

Contador = 0

while (Contador < 3):
    while (True):
        Numerito4 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito5 = float(Numerito4)
            if (Numerito5.is_integer()):
                print (f'La nota {Contador + 1} es un numero entero')
                Lista_Promedios.append(Numerito5)
                break
            else:
                print (f'La nota {Contador + 1} es un numero decimal')
                Lista_Promedios.append(Numerito5)
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador += 1
    
Promedio2 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas elegidas es {round(Promedio2, 2)}')'''

print (f'-' * 20)

import re

Texto5 = 'esto es 2 un texto 66 cualquiera hola lo que requeremos es aseegurarnos 123 @ que haela la mica esta sirva ! hula bien'

Buscar4 = re.search(r'queremos', Texto5)

print (f'{Buscar4}')

Buscar5 = bool(re.fullmatch(r'esto es 2 un texto 66 cualquiera hola lo que requeremos es asegurarnos 123 \@ que hela la mica esta sirva \! hula bien', Texto5))

if (Buscar5 == True):
    print (f'El texto es completamente igual')
else:
    print (f'Error, lo que ingresaste es diferente')
    
Buscar6 = re.findall(r'h.la', Texto5)

print (f'{Buscar6}')

Buscar7 = bool(re.findall(r'^esto', Texto5))

if (Buscar7 == True):
    print (f'Esta cadena comienza con la palabra -> esto')
else:
    print (f'Error, la cadena no comienza con -> esto')
    
Buscar8 = bool(re.search(r'n$', Texto5))

if (Buscar8 == True):
    print (f'Esta cadena termina con la letra -> n')
else:
    print (f'Error, Esta cadena no termina con la letra -> n')
    
'''
{1}
{2,}
{2,3}
? esto es 0 o 1
* esto es 0 o mas
+ esto es 1 o mas
\d esto son solo numeros
\D esto es todo menos numeros
\W esto son caracteres especiales nada mas
\w esto es todo menos caracteres especiales
\s esto son espacios
\S esto es todo menos espacios
'''

Buscar8 = re.findall(r'\d{3,}\s\W', Texto5)

print (f'{Buscar8}')

Buscar9 = re.findall(r'(re){1,4}', Texto5)

print (f'{Buscar9}')

Buscar10 = re.findall(r'[abc]+', Texto5)

print (f'{Buscar10}')

Buscar11 = re.findall(r'hola|\d{1,2}', Texto5)

print (f'{Buscar11}')

import re

Texto6 = 'ericksuper80@gmail.com'

Pattern8 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|net|org)$'

Buscar12 = bool(re.fullmatch(Pattern8, Texto6))

if (Buscar12 == True):
    print (f'Correcto, el correo tiene un formato correcto')
else:
    print (f'Error, formato de correo 1 invalido')
    
print (f'-' * 20)

import re

Texto7 = 'ericksuper80@gmail.com'

Pattern9 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.[a-z]{2,}$'

Buscar13 = bool(re.match(Pattern9, Texto7))

if (Buscar13 == True):
    print (f'Correcto, el correo 2 tiene un formato correcto')
else:
    print (f'Error, formato de correo 2 invalido')
    
print (f'-' * 20)

import re

Texto8 = '32'

Pattern10 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar14 = bool(re.fullmatch(Pattern10, Texto8))

if (Buscar14 == True):
    print (f'El numero se encuentra entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

import re

Texto9 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern11 = r'\d{1,2}\/[0-9]{2,}\/\d{4}'

Replacement11 = 'XX/XX/XXXX'

Buscar15 = re.sub(Pattern11, Replacement11, Texto9)

print (f'{Buscar15}')

Pattern12 = r'\+\d{1}\-[0-9]{2,}\-\d{1,3}\-[0-9]{4}'

Replacement12 = 'PH0N3_NVMB3R'

Buscar16 = re.sub(Pattern12, Replacement12, Buscar15)

print (f'{Buscar16}')

print (f'-' * 20)

import re

Texto10 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Pattern13 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.[a-z]{2,}'

Buscar17 = re.findall(Pattern13, Texto10)

print (f'{Buscar17}')

for indice, elemento in enumerate(Buscar17, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

import re

# Version 1

Texto11 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern14 = r'[^a-zA-Z0-9\s]+'

Buscar18 = re.sub(Pattern14, '', Texto11)

print (f'{Buscar18}')

print (f'-' * 20)

# Version 2

Pattern15 = r'\!|\?|\.{2,}|[0-9]{4}\-\d{1,4}'

Buscar19 = re.sub(Pattern15, '', Texto11)

print (f'{Buscar19}')

print (f'-' * 20)

# Version 3

Texto12 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Texto12_Temp1 = Texto12

Pattern16 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(com|net|org)'

Correos3 = re.findall(Pattern16, Texto12)

for i, email in enumerate(Correos3, start=1):
    Texto12_Temp1 = Texto12_Temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto12_Temp1}')

Pattern17 = r'\!|\?|\d{1,4}\-[0-9]{4,}|\.{2,}'

Texto12_Temp2 = re.sub(Pattern17, '', Texto12_Temp1)

print (f'{Texto12_Temp2}')

for i, email in enumerate(Correos3, start=1):
    Texto12_Temp2 = Texto12_Temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto12_Temp2}')

print (f'-' * 20)

var8 = 3.5

if (isinstance(var8, (float))):
    print (f'Lo que se ingreso es un numero decimal')
else:
    print (f'Error, lo que se ingreso no es un numero decimal')
    
try:
    Numerito4 = float(var8)
    if (Numerito4.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except Exception:
    print (f'Error, lo que se ingreso no es un numero')
    
print (f'-' * 20)

var9 = '3'

if (isinstance(var9, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var9.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var9.isdecimal()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
try:
    Numerito5 = float(var9)
    if (Numerito5.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError as Errore1:
    print (f'Error, lo que se ingreso no es un numero -> {str(Errore1)}')
    
print (f'-' * 20)

import re

Texto13 = "   Hola!!!   mundo@@   123   "

print (f'{Texto13}')

Texto13_Version1 = Texto13.strip()

print (f'{Texto13_Version1}')

Texto13_Version2 = ' '.join(Texto13_Version1.split())

print (f'{Texto13_Version2}')

Texto13_Version3 = Texto13_Version2.lower()

print (f'{Texto13_Version3}')

Texto13_Version4 = re.sub(r'\!|\@|\d+', '', Texto13_Version3)

print (f'{Texto13_Version4}')

Texto13_Version5 = Texto13_Version4.title()

print (f'{Texto13_Version5}')

print (f'-' * 20)

Lista_Exception = [1, 2, 3]

try:
    Lista_Exception.remove(4)
except ValueError:
    print (f'Error, este elemento no existe')
    
try:
    snake_case1, snake_case2, snake_case3, snake_case4 = Lista_Exception
except ValueError:
    print (f'Error de desempaquetado')
    
Fecha2 = 'hola-04-01'

try:
    Fech2 = datetime.strptime(Fecha2, '%Y-%m-%d').date()
    Fech2_Formateada = pd.to_datetime(Fech2)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Error, el formato de la fecha es incorrecto')
    
try:
    var10 = int('hola')    
except ValueError:
    print (f'Error, este valor no puede convertirse en integer')
    
print (f'-' * 20)

try:
    print (f'La suma es {3 + "hola"}') #type: ignore
except TypeError:
    print (f'Error, no se pueden sumar un integer y un string')
    
try:
    var11 = 'Hola' * '3'  #type: ignore
except Exception:
    print (f'No puedo multiplicar un texto por otro texto')
    
try:
    print (f'{Lista_Exception.index(4)}')
except ValueError as Errore1:
    print (f'Error, el indice no existe -> {str(Errore1)}')
    
print (f'-' * 20)
    
var12 = ['Erick', 12, 3.5, True]
var13 = dict({'Nombre' : "Erick"})

try:
    # snake_case5, snake_case6, snake_case7, snake_case8, snake_case9 = var12
    # print (f'El resultado de la suma es {var12[1] + var12[0]}')
    # print (f'El valor es {var12[4]}')
    # print (f'El valor con llave {var13["Edad"]}')
    print (f'{var12.index(4)}')
except ValueError:
    print (f'Error, el desempaquetado de variables es incorrecto ValueError')
except TypeError:
    print (f'Error, no se pueden sumar los valores TypeError')
except IndexError:
    print (f'Error, el indice es incorrecto IndexError')
except KeyError:
    print (f'Error, la llave es incorrecta KeyError')
except Exception:
    print (f'Error, es un ComodinError')
    
print (f'-' * 20)

var13 = 3

try:
    print (f'{len(var13)}') #type: ignore
except TypeError:
    print (f'Error, lo que ingresaste no es texto')
    
def Exception1(Numero):
    try:
        Numerito = float(Numero)
        if (Numerito.is_integer()):
            print (f'Lo que ingresaste es un numero entero')
        else:
            print (f'Lo que ingresaste es un numero decimal')
    except ValueError as Errore2:
        print (f'Error, lo que ingresaste no es un numero -> {Errore2}')

Exception1('hola')

print (f'-' * 20)

def Exception2(Num1, Num2):
    try:
        Resultado = Num1 + Num2
        
        print (f'El resultado de la suma es {Resultado}')
    except (ValueError, TypeError):
        print (f'Error, ambos elementos deben ser numericos')

Exception2(12, 'hola')

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        Resultado = Num1 / Num2
        print (f'El resultado de la division es {round(Resultado, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(12, 0)

print (f'-' * 20)

Lista_Exception4 = ['Erick', 'Josue', 'Karlita']

def Exception4(Indice):
    try:
        print (f'El elemento con indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(3)

print (f'-' * 20)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El elemento con llave {Llave} es {Diccionario_Exception5[Llave]}')
    except (KeyError, Exception):
        print (f'Error, la llave esta fuera de rango')

Exception5("Votante")

print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
    Documento_SobreEscribir = Docu.write(f'Calabaza')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Linea = Docu.readline()
        print (f'{Documento_Linea}')
        Docu.close()
except FileNotFoundError as Errore3:
    print (f'Error, el archivo no existe -> {str(Errore3)}')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nManzana'])
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        print (f'{Documento_Lineas}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nNaranja')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Leer = Docu.read()
        print (f'{Documento_Leer}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.writelines([f'\nFresa Pequeña', f'\nFresa Mediana', f'\nFresa Grande'])
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Linea = Docu.readline()
        print (f'{Documento_Linea}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke1"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke2"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke3"]}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
Lista_Frutas = []
Lista_Frutas.append('Guanabana')
Lista_Frutas.insert(1, 'Durazno')
Lista_Frutas.extend(['Uvas'])

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    for elemento in Lista_Frutas:
        Documento_Agregar = Docu.write(f'\n{elemento}')
        
    Docu.close()

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Leer = Docu.read()
        print (f'{Documento_Leer}')
        Docu.close()
except (FileNotFoundError, Exception):
    print (f'Error, el archivo no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\n'])
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Set_Conjunto_Poke1)])
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Leer = Docu.read()
        print (f'{Documento_Leer}')
        Docu.close()
except FileNotFoundError as Errore4:
    print (f'Error, el archivo no existe -> {str(Errore4)}')
    
print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
    Bundle1 = Docu.readlines()
    
for elemento in enumerate(Bundle1):
    print (f'El elemento {elemento[0]} es {elemento[1].strip()}')
    
print (f'-' * 20)
    
Contador = 0

while (Contador < len(Bundle1)):
    if (Bundle1[Contador].strip() == PEPE.Diccionario_Poke['Poke1']):
        print (f'Este bichillo es mi pokemon favorito')
        break
    else:
        Contador += 1
        continue
    
print (f'-' * 20)

print (f'{Bundle1[2].strip().lower()}')
print (f'{Bundle1[2].strip().capitalize()}')
print (f'{Bundle1[2].strip().upper()}')
print (f'{Bundle1[2].strip().title()}')

print (f'-' * 20)

import pandas as pd

Data_Frame1 = pd.DataFrame({
    'Nombre' : ['Erick', 'Josue', 'Karlita'],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
})

Data_Frame2 = pd.DataFrame({
    'Nombre' : ['Carmelo', 'Susanita', 'Roxana'],
    'Edad' : [55, 14, 26],
    'Votante' : [True, False, not False]
})

Data_Frame_Concatenate = pd.concat([Data_Frame1, Data_Frame2])

print (f'{Data_Frame1}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate}')

print (f'-' * 20)

Data_Frame_Concatenate_Age = Data_Frame_Concatenate['Edad']

print (f'-' * 20)

print (f'{Data_Frame_Concatenate_Age}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

print (f'El menor de los numeritos del dataframe es {Data_Frame_Concatenate_Age.min()}')
print (f'El mayor de los numeritos del dataframe es {Data_Frame_Concatenate_Age.max()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Unidad3 = elemento['Nombre']
    Unidad4 = elemento['Edad']
    
    print (f'Mi nombre es {Unidad3} y mi edad {Unidad4} años')
    
print (f'-' * 20)

import pandas as pd

print (f'{Data_Frame_Concatenate}')

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()
Grupo3_Min_Cant = Grupo3.min()
Grupo3_Max_Cant = Grupo3.max()

print (f'La persona {Grupo3_Min} tiene {Grupo3_Min_Cant} años')
print (f'La persona {Grupo3_Max} tiene {Grupo3_Max_Cant} años')

print (f'La cantidad de personas en el dataframe es {Grupo3.count()}')

print (f'Si sumo todas las edades me da {Grupo3.sum()} años')
print (f'La media de edades es {round(Grupo3.mean(), 2)}')

Data_Frame_Concatenate['TOTALITO'] = Data_Frame_Concatenate['Edad'] * 100

Grupo4 = Data_Frame_Concatenate.groupby('Nombre')['TOTALITO'].sum()
Grupo4_Min = Grupo4.idxmin()
Grupo4_Max = Grupo4.idxmax()
Grupo4_Min_Cant = Grupo4.min()
Grupo4_Max_Cant = Grupo4.max()

print (f'La persona {Grupo4_Min} tiene {Grupo4_Min_Cant} años')
print (f'La persona {Grupo4_Max} tiene {Grupo4_Max_Cant} años')

print (f'La cantidad de personas es {Grupo4.count()}')

print (f'La suma de las edades es {Grupo4.sum()}')

print (f'La media de las edades es {round(Grupo4.mean(), 2)}')

Promedio2 = Grupo4.sum() / Grupo3.count()

print (f'La media de las edades es {round(Promedio2, 2)}')

print (f'-' * 20)

Lista_Csv2 = list(Data_Frame_Concatenate['Nombre'])
Key2 = [f'Key{i}' for i in range(len(Lista_Csv2))]

print (f'{Lista_Csv2}')
print (f'{Key2}')

Diccionario1 = dict(zip(Key2, Lista_Csv2))

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1["Key2"]}')
print (f'{Diccionario1.get("Key5")}')

print (f'-' * 20)

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

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'-' * 20)

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'El dataframe tiene {Filas} Filas')
print (f'El dataframe tiene {Columnas} Columnas')

Elemento1 = Data_Frame1.loc[0, 'Nombre']
Elemento2 = Data_Frame1.loc[1, 'Edad']
Elemento3 = Data_Frame1.loc[2, 'Votante']
Elemento4 = Data_Frame1.loc[:, 'Nombre']
Elemento5 = Data_Frame1.loc[1, :]

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

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt.head()}')

print (f'{Cargar_Txt}')

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

print (f'{Cargar_Html[3].head()}')

print (f'-' * 20)

def Ejercicio50(Limite):
    Lista_Fibonacci = [0, 1]

    while (len(Lista_Fibonacci) < Limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

print (f'Creamos una lista Fibonacci: {Ejercicio50(10)}')

print (f'-' * 20)

print (f'{Diccionario_Lenguaje}')

Diccionario_Lenguaje_Sorted2 = dict(sorted(Diccionario_Lenguaje.items(), key=lambda item : item[1]))

print (f'{Diccionario_Lenguaje_Sorted2}')

Diccionario_Lenguaje_Sorted2_Menor = min(Diccionario_Lenguaje.items(), key=lambda item : item[1])
Diccionario_Lenguaje_Sorted2_Mayor = max(Diccionario_Lenguaje.items(), key=lambda item : item[1])

print (f'{Diccionario_Lenguaje_Sorted2_Menor}')
print (f'{Diccionario_Lenguaje_Sorted2_Mayor}')

'''
Desde python vamos a crear a un motor de base de datos.
Python viene con un modulo para trabajar con sqlite
sqlite si la base de datos no existe, automaticamente la crea, si existe se conecta
sqlitebrowser.org/dl/
'''

'''import sqlite3

conn = sqlite3.connect('contabilidad.sqlite') # Esta base no existe, entonces la crea

cursor = conn.cursor() # Cursor me permite trabajar bajo esta conexion a travez de codigo SQL

# Para crear una tabla
# cursor.execute('CREATE TABLE personas (nombre TEXT, edad NUMERIC)')

# Para evitar la inyeccion de codigo SQL usamos marcadores de posicion (?, ?)

nombre = 'Emilia'
edad = 38

cursor.execute(f'INSERT INTO TABLE personas VALUES (?, ?)', (nombre, edad))

conn.commit()

conn.close()'''

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
print (f'{Array0[0][1:2]}')
print (f'{Array0[:][2]}')
print (f'{Array0[1][0:None]}')
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
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 0]}')

print (f'{Array2[1, ::2]}')
print (f'{Array2[0, ::3]}')
print (f'{Array2[0, :2]}')
print (f'{Array2[0, 2:]}')
print (f'{Array2[1, 2:3]}')
print (f'{Array2[:, 1]}')
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

Array3 = np.array([[['a', 'b', 'c'], ['d', 'e', 'f']],        [['g', 'h', 'i'], ['j', 'k', 'l']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 2]}')

print (f'{Array3[1, 0, ::2]}')
print (f'{Array3[1, 1, ::3]}')
print (f'{Array3[0, 1, :2]}')
print (f'{Array3[0, 1, 2:]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[0, 1, 2:3]}')
print (f'{Array3[0, 0, 0:None]}')
print (f'{Array3[0, 0, :]}')
print (f'{Array3[Array3 == "b"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],          [[[6, 5, 4], [9, 8, 7]], [[0, 5, 2], [9, 7, 6]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 2]}')

print (f'{Array4[0, 1, 1, ::2]}')
print (f'{Array4[0, 0, 1, ::3]}')
print (f'{Array4[1, 0, 1, :2]}')
print (f'{Array4[1, 0, 1, 2:]}')
print (f'{Array4[0, 1, :, 2]}')
print (f'{Array4[1, 0, 1, 2:3]}')
print (f'{Array4[0, 1, 1, 0:None]}')
print (f'{Array4[0, 1, 1, :]}')
print (f'{Array4[Array4 >= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[0, 1, 0, 0:None])
Sumita8 = np.sum(Array4_Sorted[0, 1, 0, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

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

print (f'Los menores de las columns son {Array_Num2_Reshape_Column_Min}')
print (f'Los mayores de las columns son {Array_Num2_Reshape_Column_Max}')
print (f'Los menores de las row son {Array_Num2_Reshape_Row_Min}')
print (f'Los mayores de las row son {Array_Num2_Reshape_Row_Max}')

print (f'-' * 20)

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 1]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 2]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value = f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[0, 2]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(10), fill_value=f'Fuecoco')

print (f'{Array_Gen2}')

Lista_Array1 = []

for elemento in Array_Gen2:
    Lista_Array1.append(str(elemento))
    
print (f'{Array_Gen2}')
print (f'{type(Array_Gen2)}')
print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value=Array4[0, 1, 0, 2])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 0]}')

print (f'-' * 20)

Tupla_Array = ('Uno', 'Dos', 'Tres',)
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(2, 3), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array["Nombre"][1])

print (f'{Array_Gen4}')
print (f'{Array_Gen4.ndim}')
print (f'{Array_Gen4.shape}')
print (f'{Array_Gen4.size}')
print (f'{Array_Gen4.dtype}')
print (f'{Array_Gen4[1, 2]}')

print (f'-' * 20)

print (f'{Array_Gen5}')
print (f'{Array_Gen5.ndim}')
print (f'{Array_Gen5.shape}')
print (f'{Array_Gen5.size}')
print (f'{Array_Gen5.dtype}')
print (f'{Array_Gen5[1, 0]}')

print (f'-' * 20)

print (f'{Array_Gen6}')
print (f'{Array_Gen6.ndim}')
print (f'{Array_Gen6.size}')
print (f'{Array_Gen6.shape}')
print (f'{Array_Gen6.dtype}')
print (f'{Array_Gen6[3, 0]}')
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

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')
print (f'{Array_Random2.ndim}')
print (f'{Array_Random2.shape}')
print (f'{Array_Random2.size}')
print (f'{Array_Random2.dtype}')
print (f'{Array_Random2[1, 2]}')

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

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Lista_Array2 = list(['Erick', 'Josue', 'Karlita'])

Array5 = np.array(Lista_Array2)

print (f'{Lista_Array2}')
print (f'{type(Lista_Array2)}')
print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-' * 20)

Array6 = np.array([1, 2, 3])
Array7 = np.array([4, 5, 6])

Array_Concatenate = np.concat([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'-' * 20)

Array_Concatenate_Splited1 = np.split(Array_Concatenate, 1)
Array_Concatenate_Splited2 = np.split(Array_Concatenate, 2)
Array_Concatenate_Splited3 = np.split(Array_Concatenate, 3)
Array_Concatenate_Splited4 = np.split(Array_Concatenate, 6)

print (f'-' * 20)

print (f'{Array_Concatenate_Splited1[0]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Splited2[0]}')
print (f'{Array_Concatenate_Splited2[1]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Splited3[0]}')
print (f'{Array_Concatenate_Splited3[1]}')
print (f'{Array_Concatenate_Splited3[2]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Splited4[0]}')
print (f'{Array_Concatenate_Splited4[1]}')
print (f'{Array_Concatenate_Splited4[2]}')
print (f'{Array_Concatenate_Splited4[3]}')
print (f'{Array_Concatenate_Splited4[4]}')
print (f'{Array_Concatenate_Splited4[5]}')

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

Set_Conjunto_Sorteo1 = {'Erick', 'Josue', 'Karlita'}
Set_Conjunto_Sorteo2 = set({'Carmelo', 'Susanita'})
Set_Conjunto_Sorteo2.add('Roxana')
Set_Conjunto_Sorteo1.update(Set_Conjunto_Sorteo2)

Lista_Sorteo = list(Set_Conjunto_Sorteo1)

Ganador1 = np.random.choice(Lista_Sorteo, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Sorteo, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Sorteo, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-' * 20)

Array_Linspace = np.linspace(start=1, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-' * 20)

def Generadora1():
    for elemento in range(5):
        yield f'El elememento es {elemento}'

Gen1 = Generadora1()

try:
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
except StopIteration as Errore1:
    print (f'El experimento termina aqui')

print (f'-' * 20)

def Generadora2():
    for elemento in range(0, 5):
        if (elemento % 2 == 0):
            yield f'El numero es PAR'
        else:
            yield f'El numero es IMPAR'

Gen2 = Generadora2()

try:
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
except (StopIteration, Exception):
    print (f'El experimento termina aqui')

print (f'-' * 20)

def Generadora3():
    for elemento in range(0, 5):
        if (elemento == 0):
            yield f'The numer is Zero'
        elif (elemento == 1):
            yield f'The numer is One'
        elif (elemento == 2):
            yield f'The numer is Two'
        elif (elemento == 3):
            yield f'The numer is Three'
        elif (elemento == 4):
            yield f'The numer is Four'
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
    print (f'El experimento termina aqui')

print (f'-' * 20)

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int) -> int:
        return Num1 + Num2
    
    return Sumatoria_Interna(4)

Variable_Sumatoria = Sumatoria_Externa(3)

print (f'El resultado de la operacion es {Variable_Sumatoria}')

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
    
with open (f'C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(44)}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    
    for elemento in Documento_Lineas:
        Pattern18 = r'[a-z]{3}\d{1,3}'
        Buscar20 = re.findall(Pattern18, elemento.strip())
        
        if (Buscar20):
            print (f'Encontre tu contrasena temporal en la base de datos -> {Buscar20}')
            break
        else:
            continue
        
    Docu.close()
    
print (f'-' * 20)
    
def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla(3.5, True, 300, 'Koala')

print (f'{Funcion_Tupla(3.5, True, 300, 'Koala')}')
print (f'{Variable_Funcion_Tupla[2]}')
print (f'{Funcion_Tupla(3.5, True, 300, 'Koala')[3]}')
print (f'{type(Funcion_Tupla(3.5, True, 300, 'Koala'))}')

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
        
Variable_Funcion_Diccionario = Funcion_Diccionario(
    nombre='Erick',
    edad=37,
    votante=True
)

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

def Sumatoria_Dos(Nombre='Erick', *args):
    return f'Mi nombre es {Nombre} y mi numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos('Juana La Cubana', 1, 2, 3, 4, 5, 6, 7, 8,9 , 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

if (PEPE.Any_Par == True):
    print (f'Los numeros pares de la lista son {list(Anonima3)}')
    print (f'Los numeros pares de la lista son {PEPE.Lista_Par}')
    
print (f'-' * 20)

def Primera(Segunda): #type: ignore
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
        return f'Mi nombre es {Nombre} {Apellido}'
    
    return Interna('PEREZ GUTIERREZ')

print (f'{Externa('ERICK JOSUE')}')

def Closure_Externo():
    Lista_Closure = []
    def Closure_Interno(x):
        Lista_Closure.append(x)
        
        return Lista_Closure
    
    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(26)}')
print (f'{Variable_Closure(39)}')

print (f'-' * 20)

def Closure_Crear_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y

    return Closure_Multiplicador

Mult1 = Closure_Crear_Multiplicador(2)
Mult2 = Closure_Crear_Multiplicador(3)

print (f'El multiplicador es {Mult1(10)}')
print (f'El multiplicador es {Mult2(10)}')

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    if (Any_Impar == True):
        Anonima = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impar = [num for num in Lista if num % 2 != 0]
        
        print (f'Los numeros impares de la lista son {list(Anonima)}')
        print (f'Los numeros impares de la lista son {Lista_Impar}')
    else:
        print (f'Error, no tenemos elementos impares en la lista')

Filtrador(PEPE.Lista_Numeros)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'<<<<')
        Segunda()
        print (f'>>>>')
        
    return Tercera

@Primera
def Saludar4():
    print (f'Hola Mundo')
    
Saludar4()

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 15
        
    return Tercera

@Primera
def Sumatoria3(Num1, Num2=5):
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(10)}')

print (f'-' * 20)

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonathan'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)
        
    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    return f'Mi nombre es {Nombre} {Apellido}'

print (f'{Usuario2("ERICK", "PEREZ")}')

print (f'-' * 20)

from Module_Own import Pokemon as Poke1

Objeto10 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto11 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Mega Sismo')

Objeto10.Mostrar()

print (f'-' * 20)

Objeto11.Mostrar()

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto12 = Poke_Kid1(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto12)
Objeto12.Mostrar()

print (f'-' * 20)

class Camara():
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada')
        
class Reproductor_Musica():
    def Reproducir_Musica(self):
        print (f'Musica Reproducida')
        
class Smartphone(Camara, Reproductor_Musica):
    def Encender_Smartphone(self):
        print (f'Smartphone Encendido')
        
Objeto13 = Smartphone()

Objeto13.Encender_Smartphone()
Objeto13.Reproducir_Musica()
Objeto13.Tomar_Fotografia()

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
        
Objeto14 = Perro('Chester', 5, 2.5, 'Poodle', 'Asma De Perro')

Veterinaria.Mostrar(Objeto14)
Objeto14.Mostrar()

print (f'-' * 20)

class Gato(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto15 = Gato('Messi', 1.5, 1.8, 'Gris', 'No')

Veterinaria.Mostrar(Objeto15)
Objeto15.Mostrar()

print (f'-' * 20)

class Pajaro(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie : {self.Especie}')
        print (f'Habla : {self.Habla}')
        
Objeto16 = Pajaro('Polly', 31, 0.4, 'Guacamaya Roja', 'Si')

Veterinaria.Mostrar(Objeto16)
Objeto16.Mostrar()

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
        
Objeto17 = Paladin(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto17.Mostrar()
Atacante.Mostrar(Objeto17)
Defensor.Mostrar(Objeto17)

print (f'-' * 20)

hija_padre = issubclass(Poke_Kid1, Poke1)

print (f'{hija_padre}')

Instancia1 = isinstance(Objeto17, Paladin)
Instancia2 = isinstance(Objeto17, Defensor)
Instancia3 = isinstance(Objeto17, Atacante)
Instancia4 = isinstance(Objeto17, Poke_Kid1)

print (f'{Instancia1}')
print (f'{Instancia2}')
print (f'{Instancia3}')
print (f'{Instancia4}')

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
        
Objeto18 = D1()

A1.Mostrar(Objeto18)
B1.Mostrar(Objeto18)
C1.Mostrar(Objeto18)
Objeto18.Mostrar()
E1.Mostrar(Objeto18)

print (f'-' * 20)

class Efectivo():
    def Pagar(self):
        print (f'El pago se realizo en Efectivo')
        
class Tarjeta():
    def Pagar(self):
        print (f'El pago se realizo en Tarjeta')
        
class Cripto():
    def Pagar(self):
        print (f'El pago se realizo en Cripto')
        
Objeto19 = Efectivo()
Objeto20 = Tarjeta()
Objeto21 = Cripto()

Objeto19.Pagar()
Objeto20.Pagar()
Objeto21.Pagar()

print (f'-' * 20)

class cuenta_bancaria():
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
        
Objeto22 = cuenta_bancaria(100)
Objeto22.Depositar(25)
Objeto22.Mostrar()

print (f'Esto es un saldo privado que nunca deberia publicarse: ${Objeto22.Dinero}')

Objeto22.Dinero = '50,000,000'

Objeto22.Mostrar()

print (f'Esto es un saldo privado que nunca deberia publicarse: ${Objeto22.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla(Plantilla):
    def Mostrar(self):
        print (f'Este metodo pertenece a sub_plantilla')
        
    def General(self):
        print (f'Abstraccion')
        
Objeto23 = Sub_Plantilla()

Objeto23.Mostrar()
Objeto23.General()

print (f'-' * 20)

class Individuo(ABC):
    @abstractmethod
    
    def Caminar(self):
        pass

class Bebe(Individuo):
    def Gatear(self):
        print (f'El bebe al inicio gatea')
        
    def Caminar(self):
        print (f'El bebe despues camina')
        
Objeto24 = Bebe()

Objeto24.Gatear()
Objeto24.Caminar()

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
        print (f'El retador ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Objeto29 = Battle1()

Objeto29.Batallar()

print (f'-' * 20)

class Battle2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El retador ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Criatura1 = Bulbasaur()
Objeto30 = Battle2(Criatura1)
Objeto30.Batallar()

Criatura2 = Treekoo()
Objeto31 = Battle2(Criatura2)
Objeto31.Batallar()

Criatura3 = Chikorita()
Objeto32 = Battle2(Criatura3)
Objeto32.Batallar()

print (f'-' * 20)

class Persona3():
    def __init__(self, Nombre):
        self.Nombre = Nombre

    def Mostrar1(self):
        return self.Nombre
    
    @property
    def Mostrar2(self):
        return self.Nombre
    
Objeto33 = Persona3('Erick')

print (f'{Objeto33.Mostrar1()}')
print (f'{Objeto33.Mostrar2}')

print (f'-' * 20)

Opera_Mismo = 10

Opera_Mismo += 10

print (f'{Opera_Mismo}')

Opera_Mismo -= 10

print (f'{Opera_Mismo}')

Opera_Mismo *= 10

print (f'{Opera_Mismo}')

Opera_Mismo /= 10

print (f'{Opera_Mismo}')

Opera_Mismo **= 10

print (f'{Opera_Mismo}')

Opera_Mismo %= 10

print (f'{Opera_Mismo}')

Opera_Mismo //= 10

print (f'{Opera_Mismo}')

print (f'-' * 20)

print (f'Hola mi nombre es {(Nombre:= "ERICK JOSUE")}')

print (f'La lista de colores es {(Paleta:= ["Rojo", "Verde", "Azul"])}')

for elemento in range(0, limite:=5):
    print (f'El numero es {elemento}')
    
print (f'-' * 20)

Contador = 0

while (Contador < len(Lista_Walrus := ['Eric', 'Josue', 'Karlita'])):
    print (f'Mi nombre es {Lista_Walrus[Contador]}')
    Contador += 1
    
print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un
Long
String'''

variable4 = Objeto11.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = not False, Objeto12.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
DocString'''

print (f'Esta es una concatenacion simple {PEPE.Diccionario_Poke["Poke3"]}')

print (f'Mi nombre es {Lista_Uno[Lista_Uno.index("Erick")]} {variable2}')

print (f'{PEPE.Poke_Tupla[PEPE.Poke_Tupla.index("Misty")]} tiene {Variable_Sumatoria}, {Anonima2(15)} o incluso {Objeto10.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Erick' in PEPE.Lista1)
print (f'Gary' not in PEPE.Poke_Tupla)
print (f'{PEPE.Diccionario_Poke["Poke1"]}' in PEPE.Set_Conjunto_Poke1)

print (f'-' * 20)

snake_case5, snake_case6, snake_case7 = PEPE.Poke_Tupla

print (f'Esto es un desempaquetado de variables y tambien declaracion snake_case: {snake_case6}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Resisuo = divmod(Objeto12.Cantidad, Sumatoria2(1, 2, 2))

print (f'El Cociente de la operacion es {Cociente}')
print (f'El Resisuo de la operacion es {Resisuo}')

print (f'{PEPE.Lista2}')
print (f'{PEPE.Lista2[::2]}')
print (f'{PEPE.Lista2[::3]}')
print (f'{PEPE.Lista2[:2]}')
print (f'{PEPE.Lista2[2:]}')
print (f'{PEPE.Lista2[2:3]}')
print (f'{PEPE.Lista2[0:None]}')
print (f'{PEPE.Lista2[:]}')
print (f'{PEPE.Lista2[:-1]}')
print (f'{PEPE.Lista2[:-2]}')
print (f'{PEPE.Lista2[:-3]}')

print (f'{Lista_Uno[0]} eso que esta ahi es un {PEPE.Lista2[2]}???')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, 200, Objeto11.Cantidad + 64)

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

Tupla1 = ('Rojo', 'Verde', 'Azul',)

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Green', 'Blue',))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Variable_Funcion_Tupla)}')
print (f'{type(Variable_Funcion_Diccionario)}')

Set_Conjunto1 = {'Electrico', Objeto10.Tipo, Objeto10.Tipo, Objeto10.Tipo, Objeto10.Tipo, Objeto10.Tipo, Objeto10.Tipo}
Set_Conjunto1.add(PEPE.Diccionario_Poke["Poke2"]) #type: ignore
Set_Conjunto1.update(PEPE.Set_Conjunto_Poke2)

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Uno', 'Dos', 'Tres'})

print (f'{Set_Conjunto1}')

print (f'-' * 20)

SetA = {1, 2, 3, 4, 5}
SetB = {4, 5}
SetC = set({8})

print (f'{SetA.issuperset(SetB)}')
print (f'{SetA >= SetB}')
print (f'{SetB.issubset(SetA)}')
print (f'{SetB <= SetA}')
print (f'{SetA.isdisjoint(SetC)}')

print (f'-' * 20)

SetA2 = {1, 2, 3, 4}
SetB2 = {3, 4, 5, 6}

print (f'{SetA2.union(SetB2)}')
print (f'{SetA2 | SetB2}')

print (f'-' * 20)

print (f'{SetA2.intersection(SetB2)}')
print (f'{SetA2 & SetB2}')

print (f'-' * 20)

print (f'{SetA2.difference(SetB2)}')
print (f'{SetA2 - SetB2}')

print (f'-' * 20)

print (f'{SetB2.difference(SetA2)}')
print (f'{SetB2 - SetA2}')

print (f'-' * 20)

print (f'{SetA2.symmetric_difference(SetB2)}')
print (f'{SetA2 ^ SetB2}')

print (f'-' * 20)

'''SetA2.update(SetB2)

print (f'{SetA2}')'''

'''SetA2.intersection_update(SetB2)

print (f'{SetA2}')'''

'''SetA2.difference_update(SetB2)

print (f'{SetA2}')'''

'''SetB2.difference_update(SetA2)

print (f'{SetB2}')'''

SetA2.symmetric_difference_update(SetB2)

print (f'{SetA2}')

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})

Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, 'ChocoFresas'})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario2 = {
    'Nombre' : "Erick",
    'Edad' : 37,
    'Votante' : True
}

Diccionario3 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
}

Diccionario4 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "Q"})

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2.values()}')
print (f'{Diccionario2.items()}')
print (f'{Diccionario2["Nombre"]}')
print (f'{Diccionario2.get("Edad")}')

print (f'-' * 20)

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3.values()}')
print (f'{Diccionario3.items()}')
print (f'{Diccionario3["Nombre"][1]}')
print (f'{Diccionario3.get("Edad")[2]}') #type: ignore

print (f'-' * 20)

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Ingresos"]}')
print (f'{Diccionario4.get("Gastos")}')

print (f'-' * 20)

Diccionario2['Nombre'] = Saludar_Dos()

print (f'{Diccionario2}')

Diccionario2_Copia = Diccionario2.copy()

del Diccionario2['Nombre']
Diccionario2.pop('Edad')
Diccionario2.pop('Votante')

print (f'{Diccionario2}')
print (f'{len(Diccionario2)}')

print (f'{Diccionario2_Copia}')
print (f'{len(Diccionario2_Copia)}')

Diccionario2 = dict({1 : 'Karlita', 2 : 6, 3 : False})

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2.values()}')
print (f'{Diccionario2.items()}')
print (f'{Diccionario2[1]}')
print (f'{Diccionario2.get(2)}')

print (f'-' * 20)

print (f'{Diccionario3["Nombre"][2]} no puede votar ya que solamente tiene {Diccionario2.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'HelloWorld')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = Objeto10.Nombre

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

Key3 = [f'Key{i}' for i in range(len(Lista_Uno_Copia))]

Diccionario5 = dict(zip(Key3, Lista_Uno_Copia))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key2"]}')
print (f'{Diccionario5.get("Key3")}')

print (f'-' * 20)

Diccionario5_Sorted = dict(sorted(Diccionario5.items(), key=lambda item : item[1]))

print (f'{Diccionario5}')
print (f'{Diccionario5_Sorted}')

Diccionario5_Sorted_Min = min(Diccionario5_Sorted.items(), key=lambda item : item[1])
Diccionario5_Sorted_Max = max(Diccionario5_Sorted.items(), key=lambda item : item[1])

print (f'La menor de las tuplas es {Diccionario5_Sorted_Min}')
print (f'La mayor de las tuplas es {Diccionario5_Sorted_Max}')

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
except ValueError as Errore5:
    print (f'Error, la fecha tiene un formato incorrecto -> {str(Errore5)}')
    exit()
    
Cargar_Csv3['TOTALITO'] = Cargar_Csv3['quantity'] * Cargar_Csv3['price']
    
Encontrado3 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech3_Formateada.date()]

if (Encontrado3.empty):
    print (f'No hay ventas registradas en esta fecha')
else:
    print (f'Genial! encontramos ventas en esta fecha!!!')
    
    Grupo5 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo5_Min = Grupo5.idxmin()
    Grupo5_Max = Grupo5.idxmax()
    Grupo5_Min_Cant = Grupo5.min()
    Grupo5_Max_Cant = Grupo5.max()
    
    print (f'En la fecha {Fech3_Formateada} el producto {Grupo5_Min} vendio un total de {Grupo5_Min_Cant} unidades')
    print (f'En la fecha {Fech3_Formateada} el producto {Grupo5_Max} vendio un total de {Grupo5_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que nos compraron en esta fecha fue {Grupo5.count()}')
    
    print (f'La cantidad de productos vendidos en esta fecha fue {Grupo5.sum()}')
    
    print (f'El promedio de productos vendidos fue {round(Grupo5.mean(), 2)}')
    
    Grupo6 = Encontrado3.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue de ${Grupo6.sum()}')
    
    Promedio3 = Grupo6.sum() / Grupo5.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio3, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${Grupo6.mean()}')
    
print (f'-' * 20)

for indice, elemento in Cargar_Csv3.iterrows():
    Unidad5 = elemento['product']
    Unidad6 = elemento['price']
    
    print (f'El producto es {Unidad5} y su precio es ${Unidad6}')
    
print (f'-' * 20)

Lista_Csv3 = list(Cargar_Csv3['product'])
Key4 = [f'Key_{i}' for i in range(len(Lista_Csv3))]

Diccionario6 = dict(zip(Key4, Lista_Csv3))

print (f'{Diccionario6}')
print (f'{Diccionario6.keys()}')
print (f'{Diccionario6.values()}')
print (f'{Diccionario6.items()}')
print (f'{Diccionario6["Key_5"]}')
print (f'{Diccionario6.get("Key_6")}')

print (f'-' * 20)

Diccionario7 = dict({'Num1' : 5, 'Num2' : 2, 'Num3' : 4, 'Num4' : 1, 'Num5' : 3})

Diccionario7_Sorted = dict(sorted(Diccionario7.items(), key=lambda item : item[1]))

print (f'{Diccionario7}')
print (f'{Diccionario7_Sorted}')

Diccionario7_Sorted_Min = min(Diccionario7_Sorted.items(), key=lambda item : item[1])
Diccionario7_Sorted_Max = max(Diccionario7_Sorted.items(), key=lambda item : item[1])

print (f'{Diccionario7_Sorted_Min}')
print (f'{Diccionario7_Sorted_Max}')

print (f'-' * 20)

Division_Baja = 14 // 7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {Division_Baja}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'{type(variable1)}')
print (f'{type(variable4)}')
print (f'{type(PEPE.Division_Flotante)}')
print (f'{type(Lista_Uno_Copia)}')
print (f'{type(Tupla_Nombres1)}')
print (f'{type(Set_Conjunto_Menu1)}')
print (f'{type(Set_Conjunto_Menu2)}')
print (f'{type(Diccionario5_Sorted)}')
print (f'{type(Objeto10)}')
print (f'{type(Funcion_Diccionario)}')
print (f'{type(Data_Frame1)}')
print (f'{type(Array1)}')
print (f'{type(PEPE)}')

if (Diccionario4['Ingresos'] > 500): #type: ignore
    if (Diccionario4['Gastos'] < 200): #type: ignore
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario4['Gastos'] > 200): #type: ignore
        print (f'Ingresos Altos, Gastos Altos')
    elif (Diccionario4['Gastos'] == 200): #type: ignore
        print (f'Ingresos Altos, Gastos Al limite')
    else:
        print (f'Error de codigo')
elif (Diccionario4['Ingresos'] == 500): #type: ignore
    if (Diccionario4['Gastos'] < 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario4['Gastos'] > 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Altos')
    elif (Diccionario4['Gastos'] == 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Al limite')
    else:
        print (f'Error de codigo')
elif (Diccionario4['Ingresos'] < 500): #type: ignore
    if (Diccionario4['Gastos'] < 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario4['Gastos'] > 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Altos')
    elif (Diccionario4['Gastos'] == 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Al limite')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')
    
print (f'-' * 20)

variable8, variable9 = 'Josue', 20

if (variable8 == 'erick'.title() and variable9 >= 30):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')
    
if (variable8 == 'erick'.title() or variable9 >= 30):
    print (f'Al menos una de las condiciones se cumple')
else:
    print (f'Error, ninguna de las condiciones se cumple')
    
print (f'-' * 20)

def Ejercicio51(Num1:int, Num2:int) -> int:
    '''Esta funcion toma dos arguementos, los suma y devulve el resultado'''
    return Num1 + Num2

Sample51 = Ejercicio51(12, 7)

print (f'El resultado de la operacion es {Sample51}')

print (f'{help(Ejercicio51)}')

print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Sumatoria2(1, 2, 3, 4)
        self.Classified = variable6
        self.Lista_Pokemones = [
            PEPE.Diccionario_Poke['Poke1'],
            PEPE.Diccionario_Poke['Poke2'],
            PEPE.Diccionario_Poke['Poke3']
        ]
        
    def Desplegar(self):
        print (f'The trainer {self.Trainer} just catched a {self.Favorite} while visiting {self.City}')
        
    def __getitem__(self, Indice):
        return self.Lista_Pokemones[Indice]
    
Objeto34 = Entrenador(PEPE.Poke_Tupla[0], 'Kanto', Objeto10.Nombre)
Objeto35 = Entrenador(PEPE.Poke_Tupla[1], 'Paldea', Objeto11.Nombre)
Objeto36 = Entrenador(PEPE.Poke_Tupla[2], 'Alolah', Objeto12.Nombre)

Objeto34.Desplegar()
Objeto35.Desplegar()
Objeto36.Desplegar()
        
print (f'-' * 20)

print (f'El elemento en la posicion 0 es {Objeto35[0]}')
print (f'El elemento en la posicion 1 es {Objeto35[1]}')
print (f'El elemento en la posicion 2 es {Objeto35[2]}')

print (f'-' * 20)

Negativo = -5

print (f'El negativo ahora es positivo {int(abs(Negativo))}')
    
Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima4 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable}')
print (f'{list(Anonima4)}')
print (f'{Lista_Iterable}')

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario4['Vacio']) == True):
    print (f'Gracias por la informacion ingresada')
else:
    print (f'Error, ingrese una cadena de texto')
    
for elemento in Lista_Uno_Copia:
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

variable10 = 'eSteBAN'
variable10_letra = variable10[0]

print (f'{variable10}')
print (f'{variable10.lower()}')
print (f'{variable10.upper()}')
print (f'{variable10.capitalize()}')
print (f'{variable10.title()}')

Lista_Nombres4 = ['juan salvo', 'henry courtney', 'elizabeth bennet', 'marge simpson']
Lista_Nombres4_Actualizada = []

for elemento in Lista_Nombres4:
    Lista_Nombres4_Actualizada.extend([elemento.title()])
    
print (f'{Lista_Nombres4}')
print (f'{Lista_Nombres4_Actualizada}')

print (f'{variable10.lower().find("t")}')
print (f'{variable10.lower().index("b")}')

print (f'La letra {variable10_letra} aparece un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = '          Lautaro'

print (f'{variable11}')
print (f'{variable11.strip()}')

variable12 = '----hola mundo***'

print (f'{variable12}')
print (f'{variable12.strip("-*")}') # Si no le agregamos nada a strip, elimina los espacios, si le agregamos -* eliminara los caracteres

variable13 = 'esto es una cadena de texto cualquiera, lo que deseamos ver aqui es si es posible partir esta mica en partes'
variable13_Splitted = variable13.split(' ')

for elemento in enumerate(variable13_Splitted):
    print (f'{elemento[0]} : {elemento[1]}')
    
print (f'La cantidad de palabras digitadas es {variable13_Splitted.__len__()}')

print (f'-' * 20)

var14 = '3'

if (isinstance(var14, (str))):
    print (f'Lo que ingresaste es una cadena de texto')
else:
    print (f'Error, lo que ingresaste no es un texto')
    
if (var14.isalpha()):
    print (f'Lo que ingresaste es una cadena de texto')
else:
    print (f'Error, lo que ingresaste no es un texto')
    
try:
    Resultado = len(var14)
    print (f'Lo que ingresaste es un texto')
except TypeError:
    print (f'Lo que ingresaste no es un texto')
    
print (f'-' * 20)

var15 = 3.5

if (isinstance(var15, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, lo que ingresaste no es un numero decimal')
    
try:
    Numerito6 = float(var15)
    if (Numerito6.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except Exception:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var16 = '3'

if (isinstance(var16, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')
    
try:
    if (var16.isnumeric()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Error, lo que ingresaste no es un numero entero')
except AttributeError:
    print (f'Error de Atributo')
    
try:
    if (var16.isdecimal()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Error, lo que ingresaste no es un numero entero')
except AttributeError:
    print (f'Error de Atributo')
    
try:
    Numerito7 = float(var16)
    if (Numerito7.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except (ValueError, Exception):
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var17 = 3

if (isinstance(var17, (int, float))):
    print (f'Esto es un numero entero o decimal')
else:
    print (f'Error, el formato es incorrecto')
    
try:
    Numerito8 = float(var17)
    if (Numerito8.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError as Errore6:
    print (f'Error, lo que ingresaste no es un numero -> {str(Errore6)}')
    
print (f'-' * 20)

var18 = 'erick123'

if (isinstance(var18, (int, str))):
    print (f'Lo que ingresaste contiene letras o numeros')
else:
    print (f'Error, el formato es incorrecto')
    
if (var18.isalnum()):
    print (f'Lo que ingresaste contiene letras o numeros')
else:
    print (f'Error, el formato es incorrecto')
    
print (f'-' * 20)

var19 = '        a       '

if (var19.isspace()):
    print (f'Esto solo contiene espacios')
else:
    print (f'Esto contiene mucho mas que solo espacios')
    
print (f'-' * 20)

var20 = 'eSteBAN'

if (var20.lower().islower()):
    print (f'Esto contiene unicamente letras en minuscula')
else:
    print (f'Error esto no es solo minuscula')
    
if (var20.upper().isupper()):
    print (f'Esto contiene unicamente letras en mayuscula')
else:
    print (f'Error esto no es solo mayuscula')
    
if (var20.title().istitle()):
    print (f'Esto contiene unicamente letras en camel case')
else:
    print (f'Error esto no es solo camel case')
    
print (f'-' * 20)

var21 = ' '

if (bool(var21) == True):
    print (f'Gracias por ingresar la informacion deseada')
else:
    print (f'Error, no ingresaste nada')
    
print (f'-' * 20)

print (f'{PEPE.Poke_Tupla[2]} se encuentra actualmente en la posicion {PEPE.Poke_Tupla.index("Misty")}')

Eliminado = Lista_Uno_Copia.pop(-1)

print (f'El elemento eliminado es {Eliminado}')

Contador = 0

while (Contador < 5):
    print (f'El contador es {Contador + 1}')
    Contador += 1
    
print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista3)):
    print (f'{PEPE.Lista3[Contador]} : {PEPE.Lista3[Contador] * 100}')
    Contador += 1
    
print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        
        Contador = 0
        
        while (Contador < len(Documento_Lineas)):
            if (Documento_Lineas[Contador].strip() == 'Guanabana'):
                print (f'Esta fruta es muy rica pero dificil de encontrar')
                break
            else:
                Contador += 1
                continue
        
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Tupla1, lista_colores):
    print (f'{elemento1} : {elemento2}')
    
print (f'-' * 20)

Lista_Ejemplo1 = ['Erick', 'Josue']
Set_Ejemplo1 = 'Erick', 'Josue',
Tupla_Ejemplo1 = set({'Erick', 'Josue'})
Set_Ejemplo2 = {'Erick', 'Josue'}

for elemento1, elemento2, elemento3, elemento4 in zip(Lista_Ejemplo1, Set_Ejemplo1, Tupla_Ejemplo1, Set_Ejemplo2):
    print (f'{elemento1} : {elemento2} : {elemento3} : {elemento4}')
    
print (f'-' * 20)

for elemento in range(0 + 1, len(Lista_Uno_Copia[0:None])):
    print (f'{elemento}')
    
print (f'-' * 20)

Lista_Mult = [num  * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Mult}')

Menor = min(Lista_Mult)
Mayor = max(Lista_Mult)
Redondeado = round(14.458795, 2)
Sumatoria4 = sum(Lista_Mult)

print (f'El Menor de los numeros es {Menor}')
print (f'El Mayor de los numeros es {Mayor}')
print (f'El redondeado del numero 14.458795 es {Redondeado}')
print (f'El resultado de la sumatoria es {Sumatoria4}')

print (f'{bool(False)}')
print (f'{bool(not True)}')
print (f'{bool("")}')
print (f'{bool(None)}')
print (f'{bool(0)}')

Todo_All = all([Lista_Mult, Set_Conjunto_Menu1, PEPE.Poke_Tupla, Diccionario2_Copia, None])

print (f'{Todo_All}')

Uno = int('500')
Dos = str(500)
Tres = float(Uno)
Cuatro = list(PEPE.Set_Conjunto_Poke1)
Cinco = tuple(Lista_Animales1)
Seis = set(Tupla_Nombres1)

print (f'{type('500')} : {type(Uno)}')
print (f'{type(500)} : {type(Dos)}')
print (f'{type(Uno)} : {type(Tres)}')
print (f'{type(PEPE.Set_Conjunto_Poke1)} : {type(Cuatro)}')
print (f'{type(Lista_Animales1)} : {type(Cinco)}')
print (f'{type(Tupla_Nombres1)} : {type(Seis)}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto_Poke1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE4

PEPE4.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE5

Variable_PEPE5 = PEPE5

'''def Exception_Final():
    while (True):
        Numerito = input(f'Ingrese un numero: ')
        try:
            Numerito9 = float(Numerito)
            if (Numerito9.is_integer()):
                print (f'Lo que ingresaste es un numero entero')
                break
            else:
                print (f'Lo que ingresaste es un numero decimal')
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')

Exception_Final()'''

Diccionario_Lenguaje3 = {"python": 2, "java": 2, "c++": 2, "go": 1}

def Ejercicio53(Diccionario):
    Clave = next(iter(Diccionario))
    Valor = Diccionario[Clave]
    
    Lista_Empatados = []
    
    for indice, elemento in Diccionario.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    for indice, elemento in Diccionario.items():
        if (elemento == Valor):
            Clave = indice
            Valor = elemento
            Lista_Empatados.append(Clave)
        else:
            continue
        
    if (len(Lista_Empatados) > 1):
        return Lista_Empatados
    else:
        return Clave

Sample53 = Ejercicio53(Diccionario_Lenguaje3)

if (len(Diccionario_Lenguaje3) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    print (f'{Sample53}')
