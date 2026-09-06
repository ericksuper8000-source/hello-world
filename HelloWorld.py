try:
    import Module_Own as PEPE
except (ImportError, ModuleNotFoundError):
    print (f'Error, este modulo no existe')
    raise

Diccionario_Lenguajes = {"python": 2, "java": 2, "c++": 2, "go": 1}

def Ejercicio1(Diccionario):
    Lista_Claves = []
    Clave = next(iter(Diccionario_Lenguajes))
    Valor = Diccionario[Clave]
    
    for indice, elemento in Diccionario.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    for indice, elemento in Diccionario.items():
        if (elemento == Valor):
            Lista_Claves.append(indice)
        else:
            continue
        
    if (len(Lista_Claves) > 1):
        return Lista_Claves
    else:
        return Clave

Sample1 = Ejercicio1(Diccionario_Lenguajes)

if (Diccionario_Lenguajes):
    print (f'{Sample1}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Lista_Productos = ["manzana", "zanahoria", "kiwi", "pera", "tomate"]

Canastas = {
    "frutas": [],     # se llenará con frutas
    "verduras": [],   # se llenará con verduras
    "otros": []       # se llenará con lo que no sea fruta ni verdura
}

def Ejercicio2(Diccionario, Lista):
    Fruta = ["manzana","banana","pera"]
    Verdura = ["zanahoria","lechuga","tomate"]
    for elemento in Lista:
        if (elemento in Fruta):
            Diccionario['frutas'].append(elemento)
        elif (elemento in Verdura):
            Diccionario['verduras'].extend([elemento])
        else:
            Diccionario['otros'].append(elemento)
            
    return Diccionario

Sample2 = Ejercicio2(Canastas, Lista_Productos)

if (len(Canastas) == 0 or len(Lista_Productos) == 0):
    print (f'Error, alguno esta vacio, no se puede trabajar asi')
else:
    if (len(Sample2) == 0):
        print (f'El diccionario no se actualizo')
    else:
        print (f'{Sample2}')
        
print (f'-' * 20)

Lista_Feria = [("fruta","manzana"), ("verdura","zanahoria"), ("fruta","pera"), ("fruta","banana"), ("verdura","tomate")]

def Ejercicio3(Lista):
    Diccionario_Vacio = dict({})
    if (len(Lista) == 0):
        return None
    else:
        for clave, valor in Lista:
            if (clave not in Diccionario_Vacio):
                Diccionario_Vacio[clave] = []
                Diccionario_Vacio[clave].append(valor)
            else:
                Diccionario_Vacio[clave].append(valor)
                
        return Diccionario_Vacio

Sample3 = Ejercicio3(Lista_Feria)

if (Sample3 is None):
    print (f'Error, la lista esta vacia')
else:
    for valor, clave in Sample3.items():
        print (f'{valor} : {clave}')
        
print (f'-' * 20)

def Ejercicio4(Numero):
    return Numero + 10

def Ejercicio5(Numero):
    return Numero * 10

def Ejercicio6(Funcion, Numero):
    return Funcion(Numero)

print (f'El resultado de la sumatoria es {Ejercicio6(Ejercicio4, 5)}')
print (f'El resultado de la multiplicacion es {Ejercicio6(Ejercicio5, 5)}')

print (f'-' * 20)

Lista_Nombres1 = ['Erick', 'Josue']
Lista_Nombres2 = list(['Karlita'])
Lista_Nombres2.append('Carmelo')
Lista_Nombres2.insert(1, 'Susanita')
Lista_Nombres1.extend(['Roxana'])

def Ejercicio_Lista_Nombres1(Lista):
    for elemento in Lista:
        print (f'Mi nombre es {elemento}')

def Ejercicio_Lista_Nombres2(Lista):
    for elemento in Lista:
        print (f'Mi nombre es {elemento}')

def Ejercicio_Elegir_Lista(Funcion, Lista):
    return Funcion(Lista)

Ejercicio_Elegir_Lista(Ejercicio_Lista_Nombres1, Lista_Nombres1)

print (f'-' * 20)

Ejercicio_Elegir_Lista(Ejercicio_Lista_Nombres2, Lista_Nombres2)

print (f'-' * 20)

def Ejercicio_Sumar(Num1, Num2):
    return Num1 + Num2 + 5

def Ejercicio_Multiplicar(Num1, Num2):
    return Num1 * Num2 * 5

def Ejercicio_Elegir_Operacion(Funcion, Num1, Num2):
    return Funcion(Num1, Num2)

print (f'El resultado de la suma es {Ejercicio_Elegir_Operacion(Ejercicio_Sumar, 2, 3)}')
print (f'El resultado de la multiplicacion es {Ejercicio_Elegir_Operacion(Ejercicio_Multiplicar, 2, 3)}')

print (f'-' * 20)

Diccionario_Numeral = {
    'Num1' : 45,
    'Num2' : 4,
    'Num3' : 71,
    'Num4' : 9,
    'Num5' : 0,
    'Num6' : 8
}

def Ejercicio_Pares(Diccionario):
    Lista_Pares = []
    
    for clave, valor in Diccionario.items():
        if (valor % 2 == 0):
            Lista_Pares.append(clave)
        else:
            continue
        
    return Lista_Pares

def Ejercicio_Impares(Diccionario):
    Lista_Impares = list([])
    
    for clave, valor in Diccionario.items():
        if (valor % 2 != 0):
            Lista_Impares.append(clave)
        else:
            continue
        
    return Lista_Impares

def Ejercicio_Elegir_Lista2(Funcion, Diccionario):
    return Funcion(Diccionario)

print (f'Lista de claves pares: {Ejercicio_Elegir_Lista2(Ejercicio_Pares, Diccionario_Numeral)}')
print (f'Lista de claves impares: {Ejercicio_Elegir_Lista2(Ejercicio_Impares, Diccionario_Numeral)}')

print (f'-' * 20)

Lista_Animales = ['Canguro', 'Perro', 'Salamandra']
Lista_Animales.append('Raton')
Lista_Animales.insert(3, 'Tortuga')
Lista_Animales.extend(['Lombriz'])

print (f'{Lista_Animales}')

def Ejercicio7(Lista):
    while (Lista):
        print (f'{Lista}')
        Lista.pop(-1)

Sample7 = Ejercicio7(Lista_Animales)

if (len(Lista_Animales) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample7):
        print (f'{Sample7}')
        
print (f'-' * 20)

def Ejercicio8(Num1:int, Num2:int) -> int:
    '''Esta es una funcion que suma dos argumentos y retorna el resultado de la operacion'''
    return Num1 + Num2

Sample8 = Ejercicio8(12, 7)

print (f'El resultado de la operacion es {Sample8}')

print (f'{help(Ejercicio8)}')

print (f'-' * 20)

def Ejercicio9(Texto = 'Nada que mostrar'):
    return Texto

Sample9 = Ejercicio9()

print (f'{Sample9}')

print (f'-' * 20)

def Ejercicio10(Num1=2, Num2=5, Num3=8):
    return Num1 + Num2 + Num3

Sample10 = Ejercicio10()

print (f'El resultado de la operacion es {Sample10}')

def Ejercicio11(Num1=2, Num2=5, Num3=8):
    return Num1 + Num2 + Num3

Sample11 = Ejercicio11(10, 20)

print (f'El resultado de la operacion es {Sample11}')

def Ejercicio12(Num1, Num2, Num3=8):
    return Num1 + Num2 + Num3

Sample12 = Ejercicio12(1, 2)

print (f'El resultado de la operacion es {Sample12}')

print (f'-' * 20)

def Ejercicio13(*args):
    Promedio = sum(args) / len(args)
    return Promedio

Sample11 = Ejercicio13(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print (f'El promedio de los numeros ingresados es {round(Sample11, 2)}')

print (f'-' * 20)

Diccionario_Numeral2 = dict({
    'Num1' : 45,
    'Num2' : 4,
    'Num3' : 71,
    'Num4' : 9,
    'Num5' : 0,
    'Num6' : 8
})

def Ejercicio14(**kwargs):
    if (len(kwargs) == 0):
        return None
    else:
        Acumulador = 0
        
        for _, valor in kwargs.items():  # Esto se agrega cuando un valor no se va a usar
            Acumulador += valor

        return Acumulador

Sample14 = Ejercicio14(
    Num1 = 45,
    Num2 = 4,
    Num3 = 71,
    Num4 = 9,
    Num5 = 0,
    Num6 = 8
)

if (Sample14 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample14):
        print (f'El resultado de sumar todos los numeros del diccionario es {Sample14}')
    else:
        print (f'Error, no se sumo ningun numero')
        
print (f'-' * 20)

def Ejercicio15(Num1, Num2, *args, **kwargs):
    acumulador = 0
    for elemento in kwargs.values():
        acumulador += elemento
        
    return Num1 + Num2 + sum(args) + acumulador

Sample15 = Ejercicio15(
    1, 2, 
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    num1=50,
    num2=50)

print (f'El resultado de la operacion es {Sample15}')

def Ejercicio16(*args, **kwargs):
    print (f'Participantes: ')
    for elemento in args:
        print (f'{elemento}')
        
    print (f'\nDetalles del evento: ')
    
    for clave, valor in kwargs.items():
        print (f'{clave} : {valor}')

Sample16 = Ejercicio16(
    'Erick', 'Josue', 'Karlita',
    fecha = 'domingo', lugar = 'Iglesia Santa Barbara', evento = 'gran bingo'
)

print (f'-' * 20)

def Ejercicio17(Limite):
    Lista_Fibonacci = [0, 1]
    
    while (len(Lista_Fibonacci) < Limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

Sample17 = Ejercicio17(10)

print (f'La lista Fibonacci de 10 numeros es {Sample17}')

print (f'-' * 20)

Lista_Primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
Lista_Segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]

def Ejercicio18(Lista1, Lista2):
    Set_Conjunto_Tercera = set({})
    Lista_Tercera = []
    if (len(Lista1) == 0 or len(Lista2) == 0):
        return None
    else:
        for elemento in Lista1:
            if elemento in Lista2:
                Set_Conjunto_Tercera.add(elemento)
            else:
                continue
            
        Lista_Tercera = list(Set_Conjunto_Tercera)
        
        return Lista_Tercera

Sample18 = Ejercicio18(Lista_Primera, Lista_Segunda)

if (Sample18 is None):
    print (f'Error, ninguna de las listas puede estar vacia')
else:
    if (len(Sample18) == 0):
        print (f'No hay ningun numero en las listas que cumplan estas caracteristicas')
    else:
        print (f'Lista de numeros que aparecen en ambas listas pero no se repiten: {Sample18}')
        
print (f'-' * 20)

var0 = 15

print (f'{type(var0)}')

var0 += 2.5

print (f'{type(var0)}')

print (f'-' * 20)

var0 = '500'

print (f'{type(var0)}')

var0 = int(var0)

print (f'{type(var0)}')

print (f'-' * 20)

Lista_Suma1 = [1, 2, 3]
Lista_Suma2 = list([4, 5, 6])
Tupla_Suma1 = 1, 2, 3,
Tupla_Suma2 = (4, 5, 6,)

print (f'{Lista_Suma1 + Lista_Suma2}')
print (f'{Tupla_Suma1 + Tupla_Suma2}')

print (f'-' * 20)

var1 = 0

if (var1):
    print (f'El numero es correcto')
else:
    print (f'Este numero es incorrecto')
    
print (f'-' * 20)

var2 = ''

if (var2):
    print (f'El texto es correcto')
else:
    print (f'Este texto es incorrecto')
    
print (f'-' * 20)

Lista_Verduras = []

if (Lista_Verduras):
    print (f'La lista es correcta')
else:
    print (f'La lista esta vacia')
    
print (f'-' * 20)

Diccionario_Numeral3 = dict({
})

if (Diccionario_Numeral3):
    print (f'El diccinario es correcto')
else:
    print (f'El diccionario esta vacio')
    
print (f'-' * 20)

var3 = None

if (var3):
    print (f'La variable es correcta')
else:
    print (f'La variable es incorrecta')
    
if (var3 is None):
    print (f'La variable es correcta')
else:
    print (f'La variable es incorrecta')
    
if (not var3):
    print (f'La variable es correcta')
else:
    print (f'La variable es incorrecta')
    
print (f'-' * 20)

Lista_Ejercicio1 = [1, 2, 3, 4, 5]

def Ejercicio19(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        
        while (Contador < len(Lista)):
            Contador += 1
            
        return Contador

Sample19 = Ejercicio19(Lista_Ejercicio1)

if (Sample19 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La cantidad de elementos de la lista es {Sample19}')
    
def Ejercicio20(Lista):
    Acumulador = 0
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador += elemento
        else:
            continue
        
    return Acumulador

Sample20 = Ejercicio20(Lista_Ejercicio1)

if (len(Lista_Ejercicio1) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample20):
        print (f'La suma de los numeros pares es {Sample20}')
    else:
        print (f'Error, no se encontraron numeros pares en la lista')
        
print (f'-' * 20)

def Ejercicio21(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        
        for _, elemento in enumerate(Lista, start=1):
            Acumulador += elemento
            
        return Acumulador

Sample21 = Ejercicio21(Lista_Ejercicio1)

if (Sample21 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de cada elemento de la lista es {Sample21}')
    
print (f'-' * 20)

def Ejercicio22(Lista):
    Acumulador1 = 0
    Acumulador2 = 0
    Acumulador3 = 0
    Acumulador4 = 0
    
    for elemento in Lista[:-1]:
        Acumulador1 += elemento
        
    for elemento in Lista[:-2]:
        Acumulador2 += elemento
        
    for elemento in Lista[:-3]:
        Acumulador3 += elemento
        
    for elemento in Lista[:-4]:
        Acumulador4 += elemento
        
    return Acumulador1, Acumulador2, Acumulador3, Acumulador4

Sample22 = Ejercicio22(Lista_Ejercicio1)

if (Sample22):
    Adder1, Adder2, Adder3, Adder4 = Sample22
    
    print (f'Suma del acumulador: {Adder1}')
    print (f'Suma del acumulador: {Adder2}')
    print (f'Suma del acumulador: {Adder3}')
    print (f'Suma del acumulador: {Adder4}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio23(Lista, Num):
    Founder = False

    for elemento in Lista:
        if (elemento == Num):
            Founder = True
            break
        else:
            continue
        
    return Founder

Numerito = 4

Sample23 = Ejercicio23(Lista_Ejercicio1, Numerito)

if (len(Lista_Ejercicio1) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample23 == False):
        print (f'Error, el numero {Numerito} no fue encontrado en la lista')
    else:
        print (f'Exito, el numero {Numerito} fue encontrado en la lista')
        
print (f'-' * 20)

def Ejercicio24(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Menor = min(Lista)
        Mayor = max(Lista)
        Lista_Resultado = [Menor, Mayor]
        
        return Lista_Resultado

Sample24 = Ejercicio24(Lista_Ejercicio1)

if (Sample24 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero menor de la lista es {min(Sample24)}')
    print (f'El numero mayor de la lista es {max(Sample24)}')
    
print (f'-' * 20)

def Ejercicio25(Lista, Num):
    Contador = 0
    
    for elemento in Lista:
        if (elemento > Num):
            Contador += 1
        else:
            continue
        
    return Contador

Numerito1 = 2

Sample25 = Ejercicio25(Lista_Ejercicio1, Numerito1)

if (len(Lista_Ejercicio1) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample25):
        print (f'La cantidad de numeros mayores que {Numerito1} es {Sample25}')
    else:
        print (f'Error, no hay numeros mayores que {Numerito1}')
        
print (f'-' * 20)

def Ejercicio26(Lista):
    Lista_Pares = []
    Lista_Impares = list([])
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            Lista_Impares.extend([elemento])
            
    return Lista_Pares, Lista_Impares

Sample26 = Ejercicio26(Lista_Ejercicio1)

if (Lista_Ejercicio1):
    Lista_Num_Pares, Lista_Num_Impares = Sample26
    
    print (f'Lista Original: {Lista_Ejercicio1}')
    print (f'Lista Pares: {Lista_Num_Pares}')
    print (f'Lista Impares: {Lista_Num_Impares}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio27(Lista):
    Lista_Mult = []
    
    for elemento in Lista:
        Lista_Mult.append(elemento * 2)
        
    return Lista_Mult

Sample27 = Ejercicio27(Lista_Ejercicio1)

if (len(Lista_Ejercicio1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Ejercicio1}')
    print (f'Lista Multiplicado: {Sample27}')
    
print (f'-' * 20)

'''Lista_Promedios = []

Contador = 0

while (Contador < 3):
    while (True):
        Numerito2 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito3 = float(Numerito2)
            if (Numerito3.is_integer()):
                print (f'La nota {Contador + 1} es un numero entero')
                Lista_Promedios.append(Numerito3)
                break
            else:
                print (f'La nota {Contador + 1} es un numero decimal')
                Lista_Promedios.extend([Numerito3])
                break
        except Exception as Errore1:
            print (f'Error, lo que ingresaste no es un numero -> {str(Errore1)}')
    Contador += 1
    
Promedio1 = sum(Lista_Promedios) / Lista_Promedios.__len__()

print (f'El promedio de las notas elegidas es {round(Promedio1, 2)}')'''

Lista_Ejercicio2 = [5, -6, 0, -1, -3, 0]

def Ejercicio28(Lista):
    Positivos = 0
    Negativos = 0
    Ceros = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Positivos += 1
        elif (elemento < 0):
            Negativos += 1
        else:
            Ceros += 1
            
    return Positivos, Negativos, Ceros

Sample28 = Ejercicio28(Lista_Ejercicio2)

if (Lista_Ejercicio2):
    Num_Positivos, Num_Negativos, Num_Ceros = Sample28
    
    print (f'Cantidad de numeros Positivos: {Num_Positivos}')
    print (f'Cantidad de numeros Negativos: {Num_Negativos}')
    print (f'Cantidad de numeros Ceros: {Num_Ceros}')
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

def Ejercicio29(Lista):
    Lista_Validos = []
    Lista_Invalidos = list([])
    
    if (len(Lista) == 0):
        return None
    else:
        Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'
        
        for elemento in Lista:
            Buscar = bool(re.fullmatch(Pattern, elemento))
            
            if (Buscar == True):
                Lista_Validos.append(elemento)
            else:
                Lista_Invalidos.extend([elemento])
                
        return Lista_Validos, Lista_Invalidos

Sample29 = Ejercicio29(Lista_Ejercicio3)

if (Sample29 is None):
    print (f'Error, la lista esta vacia')
else:
    
    Lista_Correos_Validos, Lista_Correos_Invalidos = Sample29
    print (f'Lista Original: {Lista_Ejercicio3}')
    print (f'Lista Validos: {Lista_Correos_Validos}')
    print (f'Lista Invalidos: {Lista_Correos_Invalidos}')
    
print (f'-' * 20)

def Ejercicio30(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Temporal = Lista[0]
        
        for elemento in Lista:
            if (elemento > Temporal):
                Temporal = elemento
            else:
                continue
            
    return Temporal

Sample30 = Ejercicio30(Lista_Ejercicio1)

if (Sample30 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El mayor de todos los numeros de la lista es {Sample30}')
    
print (f'-' * 20)

def Ejercicio31(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Temporal = Lista[0]
        
        for elemento in Lista:
            if (elemento < Temporal):
                Temporal = elemento
            else:
                continue
            
    return Temporal

Sample31 = Ejercicio31(Lista_Ejercicio1)

if (Sample31 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de todos los numeros de la lista es {Sample31}')
    
print (f'-' * 20)

Lista_Ejercicio4 = list([-15.5, -8, -3.2, -1, 0, 4, 7.5, 12, 19.1, 25])

def Ejercicio32(Lista):
    Contador = 0
    Acumulador = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Contador += 1
            Acumulador += elemento
        else:
            continue
        
    return Contador, Acumulador

Sample32 = Ejercicio32(Lista_Ejercicio4)

if (len(Lista_Ejercicio4) == 0):
    print (f'Error, la lista esta vacia')
else:
    Contador1, Acumulador1 = Sample32
    
    print (f'La cantidad de numeros positivos es {Contador1}')
    print (f'La suma de estos numeros positivos es {Acumulador1}')
    
print (f'-' * 20)

Lista_Ejercicio5 = [65, 70, 54, 80, 69, 66]

def Ejercicio33(Lista):
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

Sample33 = Ejercicio33(Lista_Ejercicio5)

if (Lista_Ejercicio5):
    Alumnos_Aprobados, Alumnos_Aprobados_Sum, Alumnos_Reprobados = Sample33
    
    print (f'Cuantos alumnos aprobaron el curso? {Alumnos_Aprobados}')
    print (f'Cuantos alumnos reprobaron el curso? {Alumnos_Reprobados}')
    print (f'Total sumas de las notas aprobadas {Alumnos_Aprobados_Sum}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejercicio6 = list([15, 0, 8, 2, 0, 25, 4])

def Ejercicio34(Lista):
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
            elif (elemento > 1 and elemento < 5):
                Stock_Bajo += 1
                Stock_Bajo_Sum += elemento
            else:
                Stock_Alto += 1
                Stock_Alto_Sum += elemento
                
        return Agotados, Stock_Bajo, Stock_Alto, Stock_Bajo_Sum, Stock_Alto_Sum

Sample34 = Ejercicio34(Lista_Ejercicio6)

if (Sample34 is None):
    print (f'Error, la lista esta vacia')
else:
    Prod_Agotado, Prod_Stock_Bajo, Prod_Stock_Alto, Prod_Stock_Bajo_Sum, Prod_Stock_Alto_Sum = Sample34
    
    print (f'Total prod con stock agotado: {Prod_Agotado}')
    print (f'Total prod con stock Stock_Bajo: {Prod_Stock_Bajo}')
    print (f'Total prod con stock Stock_Alto: {Prod_Stock_Alto}')
    print (f'Total suma prod stock bajo: {Prod_Stock_Bajo_Sum}')
    print (f'Total suma prod stock alto: {Prod_Stock_Alto_Sum}')
    print (f'Total suma de todos los prod con stock: {Prod_Stock_Bajo_Sum + Prod_Stock_Alto_Sum}')
    
print (f'-' * 20)

Lista_Ejercicio7 = [12, 8, 5, 0, 7, 0, 10]

def Ejercicio35(Lista):
    Posicion = 0
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] == 0):
            Posicion = Contador
            return Posicion
        else:
            Contador += 1
            continue
        
    return None

Sample35 = Ejercicio35(Lista_Ejercicio7)

if (len(Lista_Ejercicio7) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample35 is None):
        print (f'No hay ningun producto agotado en la lista')
    else:
        print (f'El primero producto agotado del inventario aparece en la posicion {Sample35}')
        
print (f'-' * 20)

Lista_Ejercicio8 = list([120, 350, 80, 600, 150, 700])

def Ejercicio36(Lista, Numero):
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] > Numero):
            return Contador
        else:
            Contador += 1
            continue
        
    return None

Monto = 150

Sample36 = Ejercicio36(Lista_Ejercicio8, Monto)

if (len(Lista_Ejercicio8) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample36 is None):
        print (f'No encontramos una venta que supere al monto ingresado')
    else:
        print (f'La primer venta que supera el monto ${Monto} aparece en la posicion {Sample36} y la venta fue por ${Lista_Ejercicio8[Sample36]}')
        
print (f'-' * 20)

Lista_Ejercicio9 = [10, 2, 1, 4, 3, 5, 6]

def Ejercicio37(Lista):
    
    for i in range(0, len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                return Lista[i]
            else:
                continue
            
    return None

Sample37 = Ejercicio37(Lista_Ejercicio9)

if (len(Lista_Ejercicio9) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample37 is None):
        print (f'No hay ningun numero repetido en la lista')
    else:
        print (f'El primero numero repetido que aparece en la lista es {Sample37}')
        
print (f'-' * 20)

def Ejercicio38(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            
    return None

Sample38 = Ejercicio38(Lista_Ejercicio9)

if (Lista_Ejercicio9):
    if (Sample38 is None):
        print (f'No hay ningun numero repetido en la lista')
    else:
        print (f'El primero numero repetido que aparece en la lista es {Sample38}') 
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejercicio10 = [90, 89, 79, 78]

def Ejercicio39(Lista):
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] < Lista[i]):
            return i
        else:
            continue
        
    return None

Sample39 = Ejercicio39(Lista_Ejercicio10)

if (len(Lista_Ejercicio10) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample39 is None):
        print (f'No hay ningun numero que sea mayor que el anterior')
    else:
        print (f'El primer aumento en comparacion del numero anterior pasa en la posicion {Sample39}')
        
print (f'-' * 20)

Lista_Ejercicio11 = list([100, 97, 95, 80, 78])

def Ejercicio40(Lista, Num):
    Anterior = 0
    Actual = 0
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] - Lista[i] > Num):
            Anterior = Lista[i - 1]
            Actual = Lista[i]
            return Anterior, Actual, i
        else:
            continue
        
    return None

Temperatura = 30

Sample40 = Ejercicio40(Lista_Ejercicio11, Temperatura)

if (Lista_Ejercicio11):    
    if (Sample40 is None):
        print (f'No han habido caidas de temperatura drasticas en la ultima hora')
    else:
        Numero_Anterior, Numero_Actual, Posicion = Sample40 #type: ignore
        print (f'Alerta! acaba de suceder una caida en temperatura de {Numero_Anterior - Numero_Actual} grados en la posicion {Posicion}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejercicio12 = [1, 1, 0, 0, 3]

def Ejercicio41(Lista):
    for i in range(0 + 2, len(Lista)):
        if (Lista[i - 2] < Lista[i - 1] > Lista[i]):
            return i - 1
        else:
            continue
        
    return None

Sample41 = Ejercicio41(Lista_Ejercicio12)

if (len(Lista_Ejercicio12) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample41 is None):
        print (f'No hay ningun numero con estas condiciones')
    else:
        print (f'El pico sucede en la posicion {Sample41} con el numero {Lista_Ejercicio12[Sample41]}')
        
print (f'-' * 20)

# Consultar valores ✅ Consultar.

Capitales = {"Costa Rica": "San José", "México": "Ciudad de México", "Argentina": "Buenos Aires", "Italia" : "Roma", "España": "Madrid"}

Ubicado = Capitales.get('Italia')

if (Ubicado is None):
    print (f'Italia no esta en el diccionario')
else:
    print (f'La capital de Italia es {Ubicado}')
    
print (f'-' * 20)

# Consultar valores ✅ Consultar.

Productos1 = {"Laptop": 1200, "Mouse": 25, "Teclado": 45, "Monitor": 300}

def Ejercicio42(Diccionario, Articulo):
    if (len(Diccionario) == 0):
        return None
    else:
        Ubicado = Diccionario.get(Articulo)
        
        if (Ubicado is None):
            return False
        else:
            return Ubicado
    
Item1 = 'Teclado'

Sample42 = Ejercicio42(Productos1, Item1)

if (Sample42 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample42 == False):
        print (f'Error, el articulo {Item1} no fue encontrado en el diccionario')
    else:
        print (f'El articulo {Item1} fue encontrado en el diccionario con un precio de ${Sample42}')
        
print (f'-' * 20)

# Actualizar elementos ✅ Actualizar.

Productos2 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300
}

def Ejercicio43(Diccionario, Articulo, Precio):
    Ubicado = Diccionario.get(Articulo)
    
    if (Ubicado is None):
        return False
    else:
        Diccionario[Articulo] = Precio
        return True

Item2 = 'Escoba'
Item2_Price = 55

Sample43 = Ejercicio43(Productos2, Item2, Item2_Price)

if (len(Productos2) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample43  == True):
        print (f'El precio de {Item2} fue actualizado a ${Item2_Price}')
    else:
        print (f'Error, el producto {Item2} no existe, no se puede actualizar')
        
print (f'-' * 20)

# Agregar elementos ✅ Agregar.

Productos3 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio44(Diccionario, Articulo, Precio):
    Ubicado = Diccionario.get(Articulo)
    
    if (Ubicado is None):
        Diccionario[Articulo] = Precio
        return True
    else:
        return False
    
Item3 = 'Teclado'
Item3_Price = 8

Sample44 = Ejercicio44(Productos3, Item3, Item3_Price)

if (len(Productos3) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample44 == True):
        print (f'El articulo {Item3} fue agregado al diccionario')
    else:
        print (f'Error, el producto ya existe, no se puede volver a agregar')
        
print (f'-' * 20)

# Eliminar elementos ✅ Eliminar.

Productos4 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio45(Diccionario, Articulo):
    if (len(Diccionario) == 0):
        return None
    else:
        Ubicado = Diccionario.get(Articulo)
        if (Ubicado is None):
            return False
        else:
            del Diccionario[Articulo]
            return True
    
Item4 = 'Mouse'

Sample45 = Ejercicio45(Productos4, Item4)

if (Sample45 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample45 == True):
        print (f'Listo, el articulo {Item4} fue eliminado correctamente')
    else:
        print (f'Error, el articulo {Item4} no existe, no puede eliminarse')
        
print (f'-' * 20)

Productos5 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio46(Diccionario):
    Clave = next(iter(Diccionario))
    Valor = Diccionario[Clave]
    
    for indice, elemento in Diccionario.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    return Clave, Valor

Sample46 = Ejercicio46(Productos5)

if (len(Productos5) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Clave1, Valor1 = Sample46
    
    print (f'Nombre del producto: {Clave1}')
    print (f'Precio del producto: {Valor1}')
    
print (f'-' * 20)

def Ejercicio47(Diccionario):
    Clave = next(iter(Diccionario))
    Valor = Diccionario[Clave]
    
    for indice, elemento in Diccionario.items():
        if (elemento < Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    return Clave, Valor

Sample47 = Ejercicio47(Productos5)

if (len(Productos5) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Clave2, Valor2 = Sample47
    
    print (f'Nombre del producto: {Clave2}')
    print (f'Precio del producto: {Valor2}')
    
print (f'-' * 20)

Ventas = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio48(Diccionario, Precio):
    for clave, valor in Diccionario.items():
        if (valor == Precio):
             return clave
        else:
             continue
            
    return None

Monto1 = 80

Sample48 = Ejercicio48(Ventas, Monto1)

if (len(Ventas) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample48 is None):
        print (f'No se encontro una venta cuyo valor sea igual al monto ${Monto1}')
    else:
        print (f'La venta cuyo monto es igual a ${Monto1} sucedio en {Sample48}')
        
print (f'-' * 20)

Productos6 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio49(Diccionario, Num):
    Contador = 0
    
    for elemento in Diccionario.values():
        if (elemento > Num):
            Contador += 1
        else:
            continue
        
    return Contador

Limite1 = 100

Sample49 = Ejercicio49(Productos6, Limite1)

if (Productos6):
    print (f'La cantidad de elementos que tiene el diccionario es {Sample49}')
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

def Ejercicio50(Diccionario):
    Acumulador = 0
    
    for elemento in Diccionario.values():
        Acumulador += elemento
        
    return Acumulador

Sample50 = Ejercicio50(Ventas1)

if (len(Ventas1) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    print (f'El resultado de acumular todas las ventas es ${Sample50}')
    
print (f'-' * 20)

Diccionario_Lenguajes2 = {"python": 2, "java": 2, "c++": 2, "go": 1}

def Ejercicio51(Diccionario):
    Lista_Repetidos = []
    Clave = next(iter(Diccionario))
    Valor = Diccionario[Clave]
    
    for indice, elemento in Diccionario.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    for indice, elemento in Diccionario.items():
        if (elemento == Valor):
            Lista_Repetidos.append(indice)
        else:
            continue
        
    if (len(Lista_Repetidos) > 1):
        return Lista_Repetidos
    else:
        return Clave

Sample51 = Ejercicio51(Diccionario_Lenguajes2)

if (len(Diccionario_Lenguajes2) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    print (f'{Sample51}')
    
print (f'-' * 20)

Lista_Ejercicio13 = ["manzana", "zanahoria", "kiwi", "pera", "tomate"]

Canastas = {
    "frutas": [],     # se llenará con frutas
    "verduras": [],   # se llenará con verduras
    "otros": []       # se llenará con lo que no sea fruta ni verdura
}

def Ejercicio52(Diccionario, Lista):
    fruta = ["manzana","banana","pera"]
    verdura = ["zanahoria","lechuga","tomate"]
    
    for elemento in Lista:
        if (elemento in fruta):
            Diccionario['frutas'].append(elemento)
        elif (elemento in verdura):
            Diccionario['verduras'].append(elemento)
        else:
            Diccionario['otros'].append(elemento)
            
    return Diccionario

Sample52 = Ejercicio52(Canastas, Lista_Ejercicio13)

if (len(Canastas) == 0):
    print (f'El diccionario esta vacio')
else:
    for elemento in Sample52:
        print (f'{Sample52[elemento]}')
        
print (f'-' * 20)

Lista_Ejercicio14 = [("fruta","manzana"), ("verdura","zanahoria"), ("fruta","pera"), ("fruta","banana"), ("verdura","tomate")]

for elemento in Lista_Ejercicio14:
    print (f'{elemento}')
    
print (f'-' * 20)
    
for indice, elemento in Lista_Ejercicio14:
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)
    
def Ejercicio53(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Diccionario_Vacio = dict({})
        
        for indice, elemento in Lista:
            if (indice not in Diccionario_Vacio):
                Diccionario_Vacio[indice] = []
                Diccionario_Vacio[indice].append(elemento)
            else:
                Diccionario_Vacio[indice].append(elemento)
                
        return Diccionario_Vacio

Sample53 = Ejercicio53(Lista_Ejercicio14)

if (Sample53 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'{Sample53}')
    
print (f'-' * 20)

Ventas2 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio54(Diccionario, Numero):
    if (len(Diccionario) == 0):
        return None
    else:
        Acumulador = 0
        
        for elemento in Diccionario.values():
            if (elemento > Numero):
                Acumulador += elemento
            else:
                continue
            
        return Acumulador
    
Limite2 = 1000

Sample54 = Ejercicio54(Ventas2, Limite2)

if (Sample54 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (not Sample54):
        print (f'No hay ningun monto en el diccionario que supere ${Limite2}')
    else:
        print (f'La suma de los montos superiores a ${Limite2} es ${Sample54}')
        
print (f'-' * 20)

Productos7 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

Limite3 = 2000

def Ejercicio55(Diccionario, Num):
    Contador = 0
    Acumulador = 0
    
    for elemento in Diccionario.values():
        if (elemento > Num):
            Contador += 1
            Acumulador += elemento
        else:
            continue
        
    return Contador, Acumulador

Sample55 = Ejercicio55(Productos7, Limite3)

if (len(Productos7) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Contador2, Acumulador2 = Sample55
    
    if (Contador2):
        print (f'La cantidad de articulos cuyo precio es mayor que ${Limite3} es {Contador2}')
        print (f'La suma de los precios es ${Acumulador2}')
    else:
        print (f'No hay ninguna venta superior al monto ${Limite3}')
        
print (f'-' * 20)

Productos8 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio56(Diccionario, Num):
    Diccionario_Sorted = dict(sorted(Diccionario.items(), key=lambda item : item[1]))
    
    for clave, valor in Diccionario_Sorted.items():
        if (valor > Num):
            return clave
        else:
            continue
        
    return None
    
Limite4 = 2000    

Sample56 = Ejercicio56(Productos8, Limite4)

if (len(Productos8) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample56 is None):
        print (f'No hay ningu producto cuyo precio sea mayor que el monto ${Limite4}')
    else:
        print (f'El primero articulo cuyo precio es mayor que el limite ${Limite4} es {Sample56}')
        
print (f'-' * 20)

Lista_Ejercicio15 = ["python", "java", "python", "c++", "java", "python", "go", "c++", "python"]

def Ejercicio57(Lista):
    Diccionario_Palabras = dict({})
    
    for elemento in Lista:
        if (elemento not in Diccionario_Palabras):
            Diccionario_Palabras[elemento] = 0
            Diccionario_Palabras[elemento] += 1
        else:
            Diccionario_Palabras[elemento] += 1
            
    return Diccionario_Palabras

Sample57 = Ejercicio57(Lista_Ejercicio15)

if (Lista_Ejercicio15):
    print (f'{Sample57}')
else:
    print (f'Error, la lista esta vacia')
    
'''def Floating1(Numero):
    Resultado = 10 + 5 * Numero

    return Resultado

print (f'El resultado de la operacion es {Floating1(PEPE.Flotante1)}')

Floating2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Floating2}')

def Floating3(Texto):
    Texto_Formateado = Texto.replace(' ', '')
    
    try:
        if (isinstance(Texto_Formateado, (str))):
            if (Texto_Formateado.isalpha()):
                print (f'Lo que ingresaste es una cadena de texto')
    except TypeError:
        print (f'Error, lo que ingresaste no es un texto')

Floating3(PEPE.Flotante3)

print (f'-' * 20)

def Floating4(Texto):
    Cadena_Texto = Texto.split(' ')
    
    for elemento in enumerate(Cadena_Texto):
        print (f'{elemento[0]} : {elemento[1]}')
        
    print (f'La cantidad de palabras digitadas es {len(Cadena_Texto)}')

Floating4(PEPE.Flotante4)'''

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'El alumno {elemento + 1}: ')
        Lista.append(Alumno)
        
    return Lista

print (f'La lista de alumnos es {Colegio(Lista_Alumnos)}')'''

'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda num : num[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes es {Menore} y su edad es {Lista[0][1]} años')
    print (f'El mayor de los estudiantes es {Mayore} y su edad es {Lista[-1][1]} años')

Colegio(Lista_Alumnos)'''

'''Paises = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}

def Ejercicio58(Diccionario):
    if (len(Diccionario) == 0):
        return None
    else:
        while (True):
            Codigo = input(f'Ingrese el codigo de un pais: ')
                
            Ubicado = Diccionario.get(Codigo)
            
            if (Ubicado is None):
                print (f'Error, el codigo es incorrecto')
            else:
                return f'El codigo {Codigo} pertenece al pais {Ubicado}'

Sample58 = Ejercicio58(Paises)

if (Sample58 is None):
    print (f'Error, el diccionario esta vacio')
else:
    print (f'{Sample58}')'''
    
class Persona():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
    
Objeto1 = Persona('Erick Perez')

print (f'Mi nombre es {Objeto1}')

class Colores():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre
        
Lista_Colores = [
    Colores('Rojo'),
    Colores('Azul'),
    Colores('Amarillo')
]

print (f'La lista de colores es {Lista_Colores}')

class Inventario():
    def __init__(self):
        self.Productos = [
        ]
        
    def __len__(self):
        return len(self.Productos)
        
Objeto2 = Inventario()

Objeto2.Productos.append('Borrador')
Objeto2.Productos.insert(1, 'Cuaderno')
Objeto2.Productos.extend(['Lapicero'])

print (f'La lista tiene un total de {len(Objeto2)} elementos')

class Igualdad():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto3 = Igualdad('Panda Rojo')
Objeto4 = Igualdad('Panda Rojo')

if (Objeto3 == Objeto4):
    print (f'Los objetos son iguales')
else:
    print (f'Los objetos no son iguales')
    
class Caja():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto5 = Caja(5)
Objeto6 = Caja(3)

print (f'El resultado de la sumatoria es {Objeto5 + Objeto6}')

class Armario():
    def __init__(self):
        self.Ropita = [
            'Chaleco',
            'Camiseta',
            'Pantalon'
        ]
        
    def __getitem__(self, Indice):
        return self.Ropita[Indice]
        
Objeto7 = Armario()

print (f'El elemento en la posicion 0 es {Objeto7[0]}')
print (f'El elemento en la posicion 1 es {Objeto7[1]}')
print (f'El elemento en la posicion 2 es {Objeto7[2]}')

class Panaderia():
    def __init__(self):
        self.Panaderia = [
            'Croissant',
            'Baguette',
            'Donas'
        ]
        
    def __iter__(self):
        return iter(self.Panaderia)
        
Objeto8 = Panaderia()

for indice, elemento in enumerate(Objeto8, start=1):
    print (f'{indice} : {elemento}')
        
print (f'-' * 20)

var4 = '3'

if (isinstance(var4, (int))):
    print (f'El numero es entero')
else:
    print (f'Error, esto no es un numero entero')

if (var4.isnumeric()):
    print (f'El numero es entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var4.isdecimal()):
    print (f'El numero es entero')
else:
    print (f'Error, esto no es un numero entero')
    
try:
    Numerito2 = float(var4)
    if (Numerito2.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError as Errore2:
    print (f'Error, lo que ingresaste no es un numero -> {str(Errore2)}')
    
print (f'-' * 20)

var5 = 3.5

if (isinstance(var5, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, esto no es un numero decimal')
    
try:
    Numerito2 = float(var5)
    if (Numerito2.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except Exception:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var6 = 3

if (isinstance(var6, (int, float))):
    print (f'Lo ingresado es un numero entero o decimal')
else:
    print (f'Error de formato el valor es incorrecto')
    
try:
    Numerito3 = float(var6)
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
    print (f'Genial! Encontramos ventas en esta fecha')
    
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Min} vendio un total de {Grupo1_Min_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Max} vendio un total de {Grupo1_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que nos compraron fue {Grupo1.count()}')
    
    print (f'La cantidad de productos vendidos en esta fecha fue de {Grupo1.sum()}')
    
    print (f'La media de productos vendidos en esta fecha fue de {Grupo1.mean()}')
    
    Grupo2 = Encontrado1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue ${Grupo2.sum()}')
    
    Promedio1 = Grupo2.sum() / Grupo1.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio1, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Grupo2.mean(), 2)}')
    
print (f'-' * 20)

Lista_Csv1 = list(Cargar_Csv1['product'])
Key1 = [f'Key{i}' for i in range(len(Lista_Csv1))]

Diccionario_Csv1 = dict(zip(Key1, Lista_Csv1))

print (f'{Diccionario_Csv1}')
print (f'{Diccionario_Csv1.keys()}')
print (f'{Diccionario_Csv1.values()}')
print (f'{Diccionario_Csv1.items()}')
print (f'{Diccionario_Csv1["Key1"]}')
print (f'{Diccionario_Csv1.get("Key2")}')

print (f'-' * 20)

for elemento in Diccionario_Csv1:
    print (f'{Diccionario_Csv1[elemento]}')
    
print (f'-' * 20)

for elemento in Diccionario_Csv1.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario_Csv1.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario_Csv1.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

for indice, elemento in Cargar_Csv1.iterrows():
    Unidad1 = elemento['product']
    Unidad2 = elemento['price']
    
    print (f'El producto {Unidad1} tiene un precio de ${Unidad2}')
    
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

for elemento in enumerate(Buscar1):
    print (f'{elemento[0]} : {elemento[1]}')
    
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

Texto4 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern3 = r'[^a-zA-Z0-9\s]+'

Buscar3 = re.sub(Pattern3, '', Texto4)

print (f'{Buscar3}')

print (f'-' * 20)

import re

Texto5 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Texto5_Temp1 = Texto5

Pattern4 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.[a-z]{2,}'

Correos1 = re.findall(Pattern4, Texto5)

print (f'{Correos1}')

for i, email in enumerate(Correos1, start=1):
    Texto5_Temp1 = Texto5_Temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto5_Temp1}')

Pattern5 = r'\!|\?'

Texto5_Temp2 = re.sub(Pattern5, '', Texto5_Temp1)

print (f'{Texto5_Temp2}')

for i, email in enumerate(Correos1, start=1):
    Texto5_Temp2 = Texto5_Temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto5_Temp2}')

print (f'-' * 20)

print (f'{PEPE.Diccionario_Poke}')
print (f'{PEPE.Diccionario_Poke.keys()}')
print (f'{PEPE.Diccionario_Poke.values()}')
print (f'{PEPE.Diccionario_Poke.items()}')
print (f'{PEPE.Diccionario_Poke["Poke1"]}')
print (f'{PEPE.Diccionario_Poke.get("Poke2")}')

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

'''Lista_Promedio = []

Contador = 0

while (Contador < 3):
    while (True):
        Numerito4 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito5 = float(Numerito4)
            if (Numerito5.is_integer()):
                print (f'La nota {Contador + 1} es un numero entero')
                Lista_Promedio.append(Numerito5)
                break
            else:
                print (f'La nota {Contador + 1} es un numero decimal')
                Lista_Promedio.extend([Numerito5])
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador += 1
    
Promedio2 = sum(Lista_Promedio) / len(Lista_Promedio)

print (f'El promedio de las notas ingresadas es {round(Promedio2, 2)}')'''

'''import requests

Diccionario_API = {
    'Nombre' : ['Pistacho', 'Nueces', 'Pastel', 'Chicle'],
    'id' : [0, 1, 2, 3]
}

Primera1 = requests.get('http://127.0.0.1:8091/grupo1/')
Primera2 = Primera1.json()

print (f'{Primera2["Texto"]}')
print (f'{Primera1.status_code}')

print (f'-' * 20)

Primera3 = requests.get('http://127.0.0.1:8091/grupo1/unidad1/?Texto=Juanita')
Primera4 = Primera3.json()

print (f'{Primera4}')
print (f'{Primera3.status_code}')

print (f'-' * 20)

Primera5 = requests.get('http://127.0.0.1:8091/grupo1/unidad2/?Texto=Erick')
Primera6 = Primera5.json()

print (f'{Primera6}')
print (f'{Primera5.status_code}')

print (f'-' * 20)

Primera7 = requests.get('http://127.0.0.1:8091/grupo1/unidad3/?Texto=hola')
Primera8 = Primera7.json()

print (f'{Primera8}')
print (f'{Primera7.status_code}')

print (f'-' * 20)

Primera9 = requests.get('http://127.0.0.1:8091/grupo1/unidad4/')
Primera10 = Primera9.json()

print (f'{Primera10}')
print (f'{Primera9.status_code}')

print (f'-' * 20)

Primera11 = requests.get('http://127.0.0.1:8091/grupo1/unidad4/?Numero=15')
Primera12 = Primera11.json()

print (f'{Primera12}')
print (f'{Primera11.status_code}')

print (f'-' * 20)

Primera13 = requests.get('http://127.0.0.1:8091/grupo1/unidad4/?Numero=200')
Primera14 = Primera13.json()

print (f'{Primera14}')
print (f'{Primera13.status_code}')

print (f'-' * 20)

Primera15 = requests.get('http://127.0.0.1:8091/grupo1/unidad5/')
Primera16 = Primera15.json()

print (f'{Primera16}')
print (f'{Primera15.status_code}')

print (f'-' * 20)

Primera17 = requests.get('http://127.0.0.1:8091/grupo1/unidad5/?Texto=Erick')
Primera18 = Primera17.json()

print (f'{Primera18}')
print (f'{Primera17.status_code}')

print (f'-' * 20)

Primera19 = requests.get('http://127.0.0.1:8091/grupo1/unidad6')
Primera20 = Primera19.json()

print (f'{Primera20}')
print (f'{Primera19.status_code}')

print (f'-' * 20)

Segunda1 = requests.post('http://127.0.0.1:8091/grupo1/', json=(Diccionario_API))
Segunda2 = Segunda1.json()

print (f'{Segunda2}')
print (f'{Segunda1.status_code}')

print (f'-' * 20)

Tercera1 = requests.put('http://127.0.0.1:8091/grupo1/', json=(Diccionario_API))
Tercera2 = Tercera1.json()

print (f'{Tercera2}')
print (f'{Tercera1.status_code}')

print (f'-' * 20)

Primera21 = requests.get('http://127.0.0.1:8091/grupo1/unidad6/')
Primera22 = Primera21.json()

print (f'{Primera22["Helados"]}')
print (f'{Primera21.status_code}')'''

import re

Texto6 = 'esto 152 hala es un texto de ejercicio 123 @ para ver 99 hila si puedo hola trabajar correctamente 1 con expresiones regulares'

Buscar3 = re.search('puedo', Texto6)

print (f'{Buscar3}')

Buscar4 = re.findall('la', Texto6)

print (f'{Buscar4}')

Buscar5 = bool(re.fullmatch('esto 152 hala es un texto de ejercicio 123 \@ para ver 99 hila si pueba hola trabajar correctamente 1 con exprbaesiones regulares', Texto6))

if (Buscar5 == True):
    print (f'Los texto son iguales')
else:
    print (f'Los textos no son iguales')
    
Buscar6 = re.findall(r'\d+', Texto6)

print (f'{Buscar6}')

Buscar7 = re.findall(r'h.la', Texto6)

print (f'{Buscar7}')

Buscar8 = re.search(r'res$', Texto6)

print (f'{Buscar8}')

Buscar9 = re.search(r'^esto', Texto6)

print (f'{Buscar9}')

Buscar10 = re.findall(r'\d+\s\W', Texto6)

print (f'{Buscar10}')

Buscar11 = re.findall(r'[al]{2,}', Texto6)

print (f'{Buscar11}')

Buscar12 = re.findall(r'[ab]+', Texto6)

print (f'{Buscar12}')

Buscar13 = re.findall(r'\d{2,}|h.la', Texto6)

print (f'{Buscar13}')

print (f'-' * 20)

import re

Texto7 = 'ericksuper80@hotmail.com'

Pattern6 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)$'

Buscar14 = bool(re.fullmatch(Pattern6, Texto7))

if (Buscar14 == True):
    print (f'El correo electronico 1 es valido')
else:
    print (f'Error, el formato del correo 1 es invalido')
    
print (f'-' * 20)

Texto8 = 'ericksuper80@hotmail.com'

Pattern7 = r'^[a-zA-Z0-9\.\/\*\-\+_]+\@[a-zA-Z0-9]+\.[a-z]{2,}$'

Buscar15 = bool(re.match(Pattern7, Texto8))

if (Buscar15 == True):
    print (f'El correo electronico 2 es valido')
else:
    print (f'Error, el formato del correo 2 es invalido')
    
print (f'-' * 20)

import re

Texto9 = '32'

Pattern8 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar16 = bool(re.fullmatch(Pattern8, Texto9))

if (Buscar16 == True):
    print (f'El numero esta entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

import re

Texto10 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern9 = r'\d{1,2}\/[0-9]{2,}\/\d{4}'

Replacement9 = 'XX/XX/XXXX'

Buscar17 = re.sub(Pattern9, Replacement9, Texto10)

print (f'{Buscar17}')

Pattern10 = r'\+\d{1}\-[0-9]{1,3}\-\d{3,}\-[0-9]{4}'

Replacement10 = 'PH0N3_NVMB3R'

Buscar18 = re.sub(Pattern10, Replacement10, Buscar17)

print (f'{Buscar18}')

print (f'-' * 20)

Texto11 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Pattern11 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar19 = re.findall(Pattern11, Texto11)

print (f'{Buscar19}')

for indice, elemento in enumerate(Buscar19, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

import re

Texto12 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Version1

Pattern12 = r'\!|\?|\.{2,}|\d{1,4}\-[0-9]{4,}'

Buscar20 = re.sub(Pattern12, '', Texto12)

print (f'{Buscar20}')

# Version2

Pattern13 = r'[^a-zA-Z0-9\s]+'

Buscar21 = re.sub(Pattern13, '', Texto12)

print (f'{Buscar21}')

print (f'-' * 20)

var7 = 3.5

if (isinstance(var7, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, lo que ingresaste no es un numero decimal')
    
try:
    Numerito4 = float(var7)
    if (Numerito4.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except Exception:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var8 = '3'

if (isinstance(var8, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var8.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var8.isdecimal()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
try:
    Numerito5 = float(var8)
    if (Numerito5.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')

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

Lista_Exception1 = [1, 2, 3]

try:
    Lista_Exception1.remove(4)
except ValueError as Errore3:
    print (f'Error, este elemento no existe -> {str(Errore3)}')
    
print (f'-' * 20)

try:
    paquete1, paquete2, paquete3, paquete4 = Lista_Exception1
except ValueError:
    print (f'Este desempaquetado es incorrecto')
    
print (f'-' * 20)

Fecha2 = 'hola-04-01'

try:
    Fech2 = datetime.strptime(Fecha2, '%Y-%m-%d').date()
    Fech2_Formateada = pd.to_datetime(Fech2)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato incorrecto')
    
print (f'-' * 20)

try:
    print (f'El resultado de la operacion es {10 + "9"}') #type: ignore
except TypeError:
    print (f'Error, ambos elementos deben ser numeritos')
    
print (f'-' * 20)

try:
    print (f'El resultado de la operacion es {'hola' * "3"}') #type: ignore
except TypeError:
    print (f'Error, ambos elementos deben ser numeritos')
    
print (f'-' * 20)

try:
    Resultado1 = int('HolaMundo')
except ValueError:
    print (f'Error, no se puede convertir en integer un texto')
    
try:
    print (f'{Lista_Exception1.index("Carmelo")}') #type: ignore
except ValueError:
    print (f'Error, el elemento esta bien pero no existe')
    
print (f'-' * 20)

try:
    Resultado2 = int(Lista_Exception1) #type: ignore
except Exception:
    print (f'Este es el error de comodin')
    
print (f'-' * 20)

try:
    print (f'{Lista_Exception1[5]}')
except IndexError as Errore4:
    print (f'Error, la llave elegida no existe -> {str(Errore4)}')
    
print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo2.txt', r, encoding='UTF-8') as Docu: #type: ignore
        Documento_Leer = Docu.readlines()
        print (f'{Documento_Leer}')
        Docu.close()
except ValueError:
    print (f'Error, el elemento que se desea eliminar no existe')
except TypeError:
    print (f'Error, el tipo del dato es incorrecto no se puede convertir en entero una lista')
except ZeroDivisionError:
    print (f'Error, el divisor nunca puede ser cero')
except IndexError:
    print (f'Error, este index no existe')
except KeyError:
    print (f'Error, esta clave no existe')
except Exception:
    print (f'Exception Final')
    
print (f'-' * 20)

var9 = 3

try:
    Resultado3 = len(var9) #type: ignore
    print (f'Esto es un texto')
except TypeError:
    print (f'Error, lo que ingresaste no es un texto')
    
print (f'-' * 20)

def Exception1(Numero):
    try:
        Numerito = float(Numero)
        if (Numerito.is_integer()):
            print (f'Lo que ingresaste es un numero entero')
        else:
            print (f'Lo que ingresaste es un numero decimal')
    except ValueError as Errore5:
        print (f'Error, lo que ingresaste no es un numero -> {str(Errore5)}')

Exception1('hola')

print (f'-' * 20)

def Exception2(Num1, Num2):
    try:
        Resultado4 = Num1 + Num2
        print (f'El resultado de la operacion es {Resultado4}')
    except (TypeError, ValueError, Exception):
        print (f'Error, ambos elementos deben deben ser numeros')

Exception2(12, 'hola')

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        Resultado4 = Num1 / Num2
        print (f'El resultado de la operacion es {Resultado4}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(7, 0)

print (f'-' * 20)

def Exception4(Indice):
    try:
        print (f'El elemento con indice {Indice} es {Lista_Exception1[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(3)

print (f'-' * 20)

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Lenguajes[Llave]}')
    except KeyError as Errore6:
        print (f'Error, la llave usada esta fuera de rango')

Exception5("javascript")

print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
    Documento_SobreEscribir = Docu.write(f'Lobo')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Linea = Docu.readline()
        print (f'{Documento_Linea}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo elegido no existe')
    
print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nLagartija'])
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        print (f'{Documento_Lineas}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo elegido no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nPez Globo')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nHiena Pequeña'])
    Documento_Agregar = Docu.writelines([f'\nHiena Mediana'])
    Documento_Agregar = Docu.writelines([f'\nHiena Grande'])
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    for elemento in PEPE.Diccionario_Poke:
            Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke[elemento]}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
Diccionario_Lenguajes3 = {"python": 2, "java": 2, "c++": 2, "go": 1}

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    for indice, elemento in Diccionario_Lenguajes3.items():
        Documento_Agregar = Docu.write(f'\n{indice} : {elemento}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\n'])
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Set_Conjunto_Poke1)])
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Leer = Docu.read()
        print (f'{Documento_Leer}')
        Docu.close()
except Exception:
    print (f'Error, el archivo no existe')
    
print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
    Especial = Docu.readlines()
    Docu.close()
    
print (f'{type(Especial)}')

for indice, elemento in enumerate(Especial, start=1):
    if (elemento.strip() == 'Graveler'):
        print (f'{indice} : {elemento}')
        break
    else:
        continue
    
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

print (f'{Data_Frame_Concatenate_Age}')

print (f'La menor de las edades es {Data_Frame_Concatenate_Age.min()}')
print (f'La mayor de las edades es {Data_Frame_Concatenate_Age.max()}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Unidad3 = elemento['Nombre']
    Unidad4 = elemento['Edad']
    
    print (f'Mi nombre es {Unidad3} y mi edad es {Unidad4} años')
    
print (f'-' * 20)

Lista_DataFrame = list(Data_Frame_Concatenate['Nombre'])

print (f'{Lista_DataFrame}')

Key2 = [f'Key{i}' for i in range(len(Lista_DataFrame))]

Diccionario_DataFrame = dict(zip(Key2, Lista_DataFrame))

print (f'{Diccionario_DataFrame}')
print (f'{Diccionario_DataFrame.keys()}')
print (f'{Diccionario_DataFrame.values()}')
print (f'{Diccionario_DataFrame.items()}')
print (f'{Diccionario_DataFrame["Key2"]}')
print (f'{Diccionario_DataFrame.get("Key3")}')

print (f'-' * 20)

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()
Grupo3_Min_Cant = Grupo3.min()
Grupo3_Max_Cant = Grupo3.max()

print (f'El menor de los personajes del dataframe es {Grupo3_Min}, su edad es {Grupo3_Min_Cant} años')
print (f'El menor de los personajes del dataframe es {Grupo3_Max}, su edad es {Grupo3_Max_Cant} años')

print (f'-' * 20)

print (f'La cantidad de personas en el dataframe son {Grupo3.count()}')

print (f'Si sumo todas las edades del dataframe me da el numero {Grupo3.sum()}')

print (f'Y si saco el promedio de estas edades sumadas me da el numero {round(Grupo3.mean(), 2)}')

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

Columnas, Filas = Data_Frame_Concatenate.shape

print (f'La cantidad de Columnas es {Columnas}')
print (f'La cantidad de Filas es {Filas}')

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

Cargar_Excel = pd.read_excel(Ruta_Excel, engine='openpyxl')

print (f'{Cargar_Excel}')

print (f'-' * 20)

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tarifa')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tarifa', usecols='E:I')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tarifa', usecols='E:I', nrows=1)

print (f'{Cargar_Excel1}')

print (f'-' * 20)

print (f'{Cargar_Excel2}')

print (f'-' * 20)

print (f'{Cargar_Excel3}')

print (f'-' * 20)

print (f'{Cargar_Excel4}')

print (f'-' * 20)

print (f'{Cargar_Excel5}')

print (f'-' * 20)

print (f'{Cargar_Excel6}')

print (f'-' * 20)

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by='cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'-' * 20)

Cargar_Excel3_Sorted_Descending = Cargar_Excel3_Sorted.sort_values(by='cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

Grupo4 = Cargar_Excel3_Sorted.groupby('tres')['cinco'].sum()
Grupo4_Min = Grupo4.idxmin()
Grupo4_Max = Grupo4.idxmax()
Grupo4_Min_Cant = Grupo4.min()
Grupo4_Max_Cant = Grupo4.max()

print (f'Del excel, la persona menor es {Grupo4_Min} y su edad es {Grupo4_Min_Cant} años')
print (f'Del excel, la persona mayor es {Grupo4_Max} y su edad es {Grupo4_Max_Cant} años')

print (f'La cantidad de personas en el dataframe es {Grupo4.count()}')

print (f'La suma de las edades del dataframe es {Grupo4.sum()}')

print (f'La media de las edades sumadas es {Grupo4.mean()}')

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

Grupo5 = Cargar_Csv2.groupby('Nombre')['Edad'].sum()
Grupo5_Min = Grupo5.idxmin()
Grupo5_Max = Grupo5.idxmax()
Grupo5_Min_Cant = Grupo5.min()
Grupo5_Max_Cant = Grupo5.max()

print (f'El menor del csv es {Grupo5_Min} y su edad es {Grupo5_Min_Cant} años')
print (f'El mayor del csv es {Grupo5_Max} y su edad es {Grupo5_Max_Cant} años')

print (f'La cantidad de personas del csv es {Grupo5.count()}')

print (f'La suma de las edades es {Grupo5.sum()}')

print (f'La media de la suma de las edades es {round(Grupo5.mean(), 2)}')

print (f'-' * 20)

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

header = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html, headers=header)

Leer_Html = io.StringIO(Response.text)

Cargar_Html = pd.read_html(Leer_Html)

print (f'{Cargar_Html[2].head()}')

print (f'-' * 20)

Datos = {
    "ana":  {"edad": 25, "ciudad": "Quito"},
    "luis": {"edad": 30, "ciudad": "Guayaquil"}
}
#   # Nivel 1: datos["ana"]  -> {"edad":25, "ciudad":"Quito"}  (devuelve un dict)
#   # Nivel 2: datos["ana"]["ciudad"] -> "Quito"

for indice, elemento in Datos.items():
    
    print (f'{indice}')
    
    for uno, dos in elemento.items():
        print (f'{uno} : {dos}')
        
print (f'-' * 20)

Array0 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print (f'{Array0}')
print (f'{Array0[1][::2]}')
print (f'{Array0[2][::3]}')
print (f'{Array0[0][:2]}')
print (f'{Array0[0][2:]}')
print (f'{Array0[1][2:3]}')
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

Array2 = np.array([[1, 2, 3], [1, 2, 3]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 0]}')

print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[0, 2:3]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 >= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {Array2_Sorted_Mean}')
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
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 0]}')

print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[0, :, 0]}')
print (f'{Array3[1, 1, 2:3]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "g"]}')


print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]],             [[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.size}') # 2x2x2x3
print (f'{Array4.shape}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[0, 1, 0, 2]}')

print (f'{Array4[1, 0, 1, ::2]}')
print (f'{Array4[1, 1, 0, ::3]}')
print (f'{Array4[0, 1, 1, :2]}')
print (f'{Array4[0, 1, 1, 2:]}')
print (f'{Array4[1, 0, :, 1]}')
print (f'{Array4[0, 1, 0, 2:3]}')
print (f'{Array4[1, 0, 0, 0:None]}')
print (f'{Array4[1, 0, 0, :]}')
print (f'{Array4[Array4 >= 3]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[1, 0, 1, 0:None])
Sumita8 = np.sum(Array4_Sorted[1, 0, 1, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'-' * 20)

def Ejercicio58(Limite):
    Lista_Fibonacci = [0, 1]
    
    while (len(Lista_Fibonacci) < Limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

Sample58 = Ejercicio58(10)

print (f'Lista Fibonacci de diez elementos: {Sample58}')

print (f'-' * 20)

Diccionario_Lenguajes4 = {"python": 4, "java": 2, "c++": 2, "go": 1}

def Ejercicio59(Diccionario):
    Lista_Repetidos = list([])
    if (len(Diccionario) == 0):
        return None
    else:
        Clave = next(iter(Diccionario))
        Valor = Diccionario[Clave]
        
        for indice, elemento in Diccionario.items():
            if (elemento > Valor):
                Clave = indice
                Valor = elemento
            else:
                continue
            
        for indice, elemento in Diccionario.items():
            if (elemento == Valor):
                Lista_Repetidos.append(indice)
            else:
                continue
            
        if (len(Lista_Repetidos) > 1):
            return Lista_Repetidos
        else:
            return Clave

Sample59 = Ejercicio59(Diccionario_Lenguajes4)

if (Sample59 is None):
    print (f'Error, el diccionario esta vacio')
else:
    print (f'{Sample59}')

print (f'-' * 20)

Diccionario_Lenguajes4_Sorted = dict(sorted(Diccionario_Lenguajes4.items(), key=lambda item : item[1]))

print (f'{Diccionario_Lenguajes4}')
print (f'{Diccionario_Lenguajes4_Sorted}')

Diccionario_Lenguajes4_Sorted_Min = min(Diccionario_Lenguajes4.items(), key=lambda item : item[1])
Diccionario_Lenguajes4_Sorted_Max = max(Diccionario_Lenguajes4.items(), key=lambda item : item[1])

print (f'El menor de los elementos es {Diccionario_Lenguajes4_Sorted_Min}')
print (f'El mayor de los elementos es {Diccionario_Lenguajes4_Sorted_Max}')

print (f'-' * 20)

Lista_Ejercicio16 = ["manzana", "zanahoria", "kiwi", "pera", "tomate"]

Canastas2 = {
    "frutas": [],
    "verduras": [],
    "otros": []
}

def Ejercicio60(Diccionario, Lista):
    fruta = ["manzana","banana","pera"]
    verdura = ["zanahoria","lechuga","tomate"]
    
    for elemento in Lista:
        if (elemento in fruta):
            Diccionario['frutas'].append(elemento)
        elif (elemento in verdura):
            Diccionario['verduras'].append(elemento)
        else:
            Diccionario['otros'].append(elemento)
            
    return Diccionario

Sample60 = Ejercicio60(Canastas2, Lista_Ejercicio16)

if (len(Canastas2) == 0 or len(Lista_Ejercicio16) == 0):
    print (f'Error, ninguna puede estar vacia')
else:
    print (f'{Sample60}')

print (f'-' * 20)

Lista_Ejercicio17 = [("fruta","manzana"), ("verdura","zanahoria"), ("fruta","pera"), ("fruta","banana"), ("verdura","tomate")]

def Ejercicio61(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Diccionario_Vacio = dict({})
        
        for indice, elemento in Lista:
            if (indice not in Diccionario_Vacio):
                Diccionario_Vacio[indice] = []
                Diccionario_Vacio[indice].append(elemento)
            else:
                Diccionario_Vacio[indice].append(elemento)
                
        return Diccionario_Vacio

Sample61 = Ejercicio61(Lista_Ejercicio17)

if (Sample61 is None):
    print (f'Error, lista vacia')
else:
    print (f'{Sample61}')

print (f'-' * 20)

def Ejercicio_Sumar2(Num1):
    return Num1 + 10

def Ejercicio_Multiplicar2(Num1):
    return Num1 * 10

def Elegir_Operacion2(Funcion, Numero):
    return Funcion(Numero)

print (f'El resultado de la sumatoria es {Elegir_Operacion2(Ejercicio_Sumar2, 5)}')
print (f'El resultado de la multiplicacion es {Elegir_Operacion2(Ejercicio_Multiplicar2, 5)}')

print (f'-' * 20)

Lista_Ejercicio18 = ['Erick', 'Josue', 'Karlita']
Lista_Ejercicio19 = list(['Carmelo', 'Susanita', 'Roxana'])

def Ejercicio_Lista1(Lista):
    for elemento in Lista:
        print (f'{elemento}')

def Ejercicio_Lista2(Lista):
    for elemento in Lista:
        print (f'{elemento}')

def Ejercicio_Elegir_Lista3(Funcion, Lista):
    return Funcion(Lista)

Ejercicio_Elegir_Lista3(Ejercicio_Lista2, Lista_Ejercicio19)

print (f'-' * 20)

Ejercicio_Elegir_Lista3(Ejercicio_Lista2, Lista_Ejercicio19)

print (f'-' * 20)

def Ejercicio62(Num1, Num2):
    return Num1 + Num2 + 10

def Ejercicio63(Num1, Num2):
    return Num1 * Num2 * 10

def Ejercicio_Elegir_Operacion2(Funcion, Numero1, Numero2):
    return Funcion(Numero1, Numero2)

print (f'El resultado de la operacion es {Ejercicio_Elegir_Operacion2(Ejercicio62, 2, 3)}')
print (f'El resultado de la operacion es {Ejercicio_Elegir_Operacion2(Ejercicio63, 2, 3)}')

print (f'-' * 20)

Diccionario_Ambos = dict({
    'Num1' : 5,
    'Num2' : 2,
    'Num3' : 7,
    'Num4' : 9,
    'Num5' : 1
})

def Ejercicio64(Diccionario):
    Lista_Pares = []
    
    for clave, valor in Diccionario.items():
        if (valor % 2 == 0):
            Lista_Pares.append(clave)
        else:
            continue
        
    return Lista_Pares

def Ejercicio65(Diccionario):
    Lista_ImPares = []
    
    for clave, valor in Diccionario.items():
        if (valor % 2 != 0):
            Lista_ImPares.append(clave)
        else:
            continue
        
    return Lista_ImPares

def Ejercicio_Dict(Funcion, Diccionario):
    return Funcion(Diccionario)

print (f'{Ejercicio_Dict(Ejercicio64, Diccionario_Ambos)}')
print (f'{Ejercicio_Dict(Ejercicio65, Diccionario_Ambos)}')

print (f'-' * 20)

Lista_Animales1 = ['Cabra', 'Elefante']
Lista_Animales1.append('Salamandra')
Lista_Animales1.insert(2, 'Avestruz')
Lista_Animales1.extend(['Escarabajo'])

Contador = 0

while (Contador < len(Lista_Animales1)):
    print (f'{Lista_Animales1}')
    Lista_Animales1.pop(-1)

print (f'-' * 20)

def Ejercicio66(Num1:int, Num2:int) -> int:
    '''Esto es un docstring, la funcion toma dos argumentos, los suma y retorna el resultado'''
    return Num1 + Num2

Sample66 = Ejercicio66(12, 7)

print (f'{help(Ejercicio66)}')

print (f'-' * 20)

def Ejercicio67(Num1=10, Num2=15, Num3=3):
    return Num1 + Num2 + Num3

Sample67 = Ejercicio67()

print (f'El resultado de la operacion es {Sample67}')

print (f'-' * 20)

def Ejercicio68(Num1=10, Num2=15, Num3=3):
    return Num1 + Num2 + Num3

Sample68 = Ejercicio68(2, 3)

print (f'El resultado de la operacion es {Sample68}')

print (f'-' * 20)

def Ejercicio69(Num1, Num2, Num3=3):
    return Num1 + Num2 + Num3

Sample69 = Ejercicio69(1, 2)

print (f'El resultado de la operacion es {Sample69}')

print (f'-' * 20)

def Ejercicio70(Texto='No hay nada que mostrar'):
    return Texto

Sample70 = Ejercicio70()

print (f'{Sample70}')

print (f'-' * 20)

def Ejercicio71(*args):
    Promedio = sum(args) / args.__len__()
    return round(Promedio, 2)

Sample71 = Ejercicio71(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print (f'El promedio de los numeros elegidos es {Sample71}')

print (f'-' * 20)

def Ejercicio72(**kwargs):
    Acumulador = 0
    for _, elemento in kwargs.items():
        Acumulador += elemento
        
    return Acumulador

Sample72 = Ejercicio72(
    num1=12,
    num2=5,
    num3=6,
    num4=11,
    num5=0
)

print (f'El resultado del acumulador es {Sample72}')

print (f'-' * 20)

def Ejercicio73(Num1, Num2, *args, **kwargs):
    Acumulador = 0
    for elemento in kwargs.values():
        Acumulador += elemento
        
    return Num1 + Num2 + sum(args) + Acumulador

Sample73 = Ejercicio73(
    2, 3,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    num1=12, num2=10, num3=3
)

print (f'El resultado de la operacion es {Sample73}')

print (f'-' * 20)

def Ejercicio74(*participantes, **detalles):
    print (f'Lista de participantes: \n')
    
    for elemento in participantes:
        print (f'- {elemento}')
        
    print (f'-' * 20)
    
    print (f'Detalles del evento: \n')
    
    for indice, elemento in detalles.items():
        print (f'{indice} : {elemento}')

Sample74 = Ejercicio74(
    'Erick', 'Josue', 'Karlita',
    Fecha='Domingo', Lugar='Iglesia Santa Lucia', Tema='Gran Bingo De Verano'
)

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1) #type: ignore

print (f'{Array_Num1}')

Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El menor de los numeros es {Array_Num1_Min}')
print (f'El mayor de los numeros es {Array_Num1_Max}')

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

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 2]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value=f'{PEPE.Diccionario_Poke["Poke2"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 2]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(10), fill_value=f'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[4]}')

Lista_Array1 = []

for elemento in Array_Gen2:
    Lista_Array1.append(str(elemento))
    
print (f'{Array_Gen2}')
print (f'{type(Array_Gen2)}')
print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value = Array4[1, 1, 0, 2])

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
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array["Nombre"][2])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
print (f'{Array_Gen6}')

print (f'-' * 20)

print (f'{Array_Gen6[2]}')

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
print (f'{Array_Random1.ndim}')
print (f'{Array_Random1.shape}')
print (f'{Array_Random1.size}')
print (f'{Array_Random1.dtype}')
print (f'{Array_Random1[5]}')

Array_Random1_Sorted = np.sort(Array_Random1)
Array_Random1_Sorted_Mean = np.mean(Array_Random1_Sorted)
Array_Random1_Sorted_Sum = np.sum(Array_Random1_Sorted)

print (f'Acomodado: {Array_Random1_Sorted}')
print (f'Media: {round(Array_Random1_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random1_Sorted_Sum}')

print (f'-' * 20)

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Suma = Arr1 + Arr2
Resta = Arr1 - Arr2
Multiplicacion = Arr1 * Arr2
Division = Arr1 - Arr2
Array_Random1_Cien = Array_Random1 + 100

print (f'El resultado de la operacion es {Suma}')
print (f'El resultado de la operacion es {Resta}')
print (f'El resultado de la operacion es {Multiplicacion}')
print (f'El resultado de la operacion es {Division}')
print (f'El resultado de la operacion es {Array_Random1_Cien}')

print (f'-' * 20)

Array_Random2 = np.random.randint(low=1, high=10, size=(20))

print (f'{Array_Random2}')

Array_Random2_Reshape = np.reshape(Array_Random2, shape=(4, 5))

print (f'{Array_Random2_Reshape}')

Array_Random2_Reshape_Ravel = np.ravel(Array_Random2_Reshape)

print (f'{Array_Random2_Reshape_Ravel}')

print (f'-' * 20)

Lista_Array2 = ['Erick', 'Josue', 'Karlita']

Array5 = np.array(Lista_Array2)

print (f'{Lista_Array2}')
print (f'{type(Lista_Array2)}')
print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-' * 20)

Array6 = np.array([1, 2,3 ])
Array7 = np.array([4, 5, 6])

Array_Concatenate = np.concatenate([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'-' * 20)

Array_Concatenate_Splitted1 = np.split(Array_Concatenate, 1)
Array_Concatenate_Splitted2 = np.split(Array_Concatenate, 2)
Array_Concatenate_Splitted3 = np.split(Array_Concatenate, 3)
Array_Concatenate_Splitted4 = np.split(Array_Concatenate, 6)

print (f'{Array_Concatenate_Splitted1[0]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Splitted2[0]}')
print (f'{Array_Concatenate_Splitted2[1]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Splitted3[0]}')
print (f'{Array_Concatenate_Splitted3[1]}')
print (f'{Array_Concatenate_Splitted3[2]}')

print (f'-' * 20)

print (f'{Array_Concatenate_Splitted4[0]}')
print (f'{Array_Concatenate_Splitted4[1]}')
print (f'{Array_Concatenate_Splitted4[2]}')
print (f'{Array_Concatenate_Splitted4[3]}')
print (f'{Array_Concatenate_Splitted4[4]}')
print (f'{Array_Concatenate_Splitted4[5]}')

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

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Array_Random3_Sorted = np.sort(Array_Random3)
Array_Random3_Sorted_Mean = np.mean(Array_Random3_Sorted)
Array_Random3_Sorted_Sum = np.sum(Array_Random3_Sorted)

print (f'Acomodado: {Array_Random3_Sorted}')
print (f'Media: {round(Array_Random3_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random3_Sorted_Sum}')

print (f'-' * 20)

Set_Conjunto_Sorteo1 = {'Erick', 'Josue', 'Karlita'}
Set_Conjunto_Sorteo2 = set({'Carmelo', 'Susanita', 'Roxana'})

Set_Conjunto_Sorteo1.update(Set_Conjunto_Sorteo2)

Lista_Sorteo = list(Set_Conjunto_Sorteo1)

print (f'{Lista_Sorteo}')

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
    print (f'El experimento termina aqui!')

print (f'-' * 20)

def Generadora2():
    for elemento in range(0, 5):
        if (elemento % 2 == 0):
            yield f'El numero es par'
        else:
            yield f'El numero es impar'

Gen2 = Generadora2()

try:
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
    print (f'{next(Gen2)}')
except StopIteration:
    print (f'El experimento termina aqui!')

print (f'-' * 20)

def Generadora3():
    for elemento in range(0, 5):
        if (elemento == 0):
            yield f'El numero es cero'
        elif (elemento == 1):
            yield f'El numero es uno'
        elif (elemento == 2):
            yield f'El numero es dos'
        elif (elemento == 3):
            yield f'El numero es tres'
        elif (elemento == 4):
            yield f'El numero es cuatro'
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
    print (f'El experimento termina aqui!')

print (f'-' * 20)

print (f'{PEPE.Saludar1()}')

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la operacion es {PEPE.Sumatoria1(12, 7)}')

print (f'{help(PEPE.Sumatoria1)}')

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
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(44)}')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo2.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        print (f'{Documento_Lineas}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
print (f'-' * 20)
    
def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla(3.5, 300, 'Koala', not False)

print (f'{Funcion_Tupla(3.5, 300, 'Koala', not False)}')
print (f'{Funcion_Tupla(3.5, 300, 'Koala', not False)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla(3.5, 300, 'Koala', not False))}')

print (f'-' * 20)

def Funcion_Diccionario(**Argumentos):
    for elemento in Argumentos:
        print (f'{Argumentos[elemento]}')
        
    print (f'-' * 20)
    
    for elemento in Argumentos.keys():
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    for elemento in Argumentos.values():
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    for elemento in Argumentos.items():
        print (f'{elemento[0]} -- {elemento[1]}')
        
Funcion_Diccionario(
    Nombre='Erick',
    Edad=37,
    Votante=True
)

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

def Sumatoria_Dos(Nombre, *args):
    return f'Mi nombre es {Nombre} y mi numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos(Saludar_Dos(), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3, Variable_Funcion_Anonima4 as Anonima4

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

if (PEPE.Any_Par == True):
    print (f'Los numeros pares de la lista son {PEPE.Lista_Par}')
    print (f'Los numeros pares de la lista son {list(Anonima3)}')
else:
    print (f'Error, no hay elementos pares en la lista')
    
print (f'{PEPE.Diccionario_Numeral}')
print (f'{Anonima4}')
print (f'{PEPE.Variable_Funcion_Anonima4_Min}')
print (f'{PEPE.Variable_Funcion_Anonima4_Max}')

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda(*args) - 42
        
    return Tercera

@Primera
def Operacion(Numero):
    Local = Numero
    return PEPE.GLOBAL + Local

print (f'El resultado de la operacion es {Operacion(12)}')

print (f'-' * 20)

def Externa(Nombre):
    def Interna(Apellido):
        return f'Mi nombre es {Nombre} {Apellido}'
    
    return Interna('PEREZ GUTIERREZ')

print (f'{Externa('ERICK JOSUE')}')

def Closure_Externo():
    Lista_Closure = list([])
    def Closure_Interno(x):
        Lista_Closure.append(x)
        
        return Lista_Closure
    
    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(26)}')
print (f'{Variable_Closure(37)}')

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
        
        print (f'Los elementos impares de la lista son {list(Anonima)}')
        print (f'Los elementos impares de la lista son {Lista_Impar}')
    else:
        print (f'Error, no hay numeros impares en la lista')

Filtrador(PEPE.Lista_Numeros)

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'>>>>>')
        Segunda()
        print (f'<<<<<')
        
    return Tercera

@Primera
def Saludar4():
    print (f'Hola Mundo')
    
Saludar4()

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) + 8
        
    return Tercera

@Primera
def Sumatoria3(Num1=5, Num2=0):
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(1, 1)}')

print (f'-' * 20)

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'John'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)
        
    return Tercera

@Primera
def Usuario2(Nombre, Apellido='Perez'):
    return f'Mi nombre es {Nombre} {Apellido}'

print (f'{Usuario2('Erick')}')

from Module_Own import Pokemon as Poke1

Objeto9 = Poke1(PEPE.Diccionario_Poke["Poke1"], 'Electrico', 'Impact Trueno')
Objeto10 = Poke1(PEPE.Diccionario_Poke["Poke2"], 'Roca', 'Mega Sismo')

Objeto9.Mostrar()

print (f'-' * 20)

Objeto10.Mostrar()

print (f'-' * 20)

print (f'Actualmente yo tengo {Objeto10.Cantidad} pokemones')

if (Objeto9.Catched == True):
    print (f'El pokemon fue atrapado')
else:
    print (f'El pokemon no fue atrapado')
    
print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto11 = Poke_Kid1(PEPE.Diccionario_Poke["Poke3"], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto11)
Objeto11.Mostrar()

print (f'La cantidad de pokemones es {Objeto11.Cantidad}')

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
        
Objeto12 = Smartphone()

Objeto12.Encender_Smartphone()
Objeto12.Reproducir_Musica()
Objeto12.Tomar_Fotografia()

print (f'-' * 20)

class Veterinaria():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso
        self.Adoptado = True

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
        
Objeto13 = Perro('Terry', 6, 3, 'Dobberman', 'Obesidad')

Veterinaria.Mostrar(Objeto13)
Objeto13.Mostrar()

print (f'{Objeto13.Nombre} fue adoptado? {Objeto13.Adoptado}')

print (f'-' * 20)

class Gato(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto14 = Gato('Messi', 1.5, 1.8, 'Gris', 'No')

Veterinaria.Mostrar(Objeto14)
Objeto14.Mostrar()

print (f'{Objeto14.Nombre} fue adoptado? {Objeto14.Adoptado}')

print (f'-' * 20)

class Pajaro(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto15 = Pajaro('Polly', 31, 0.4, 'Guacamaya Azul', 'Si')

Veterinaria.Mostrar(Objeto15)
Objeto15.Mostrar()

print (f'{Objeto15.Nombre} fue adoptado? {not Objeto15.Adoptado}')

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

print (f'{Hija_Padre}')

Instancia1 = isinstance(Objeto16, Paladin)
Instancia2 = isinstance(Objeto16, Defensor)
Instancia3 = isinstance(Objeto16, Atacante)

print (f'{Instancia1}')
print (f'{Instancia2}')
print (f'{Instancia3}')

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
        
Objeto17 = D1()

A1.Mostrar(Objeto17)
B1.Mostrar(Objeto17)
C1.Mostrar(Objeto17)
Objeto17.Mostrar()
E1.Mostrar(Objeto17)

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
        
Objeto18 = Efectivo()
Objeto19 = Tarjeta()
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
        print (f'Su saldo a la fecha es de ${self.__Saldo}')
        
Objeto21 = Cuenta_Bancaria(100)

Objeto21.Depositar(25)

Objeto21.Mostrar()

print (f'Este es un valor privado, nunca haga publico este saldo privado {Objeto21.Dinero}')

Objeto21.Dinero = '50,000,000'

Objeto21.Mostrar()

print (f'Este es un valor privado, nunca haga publico este saldo privado {Objeto21.Dinero}')

print (f'-' * 20)

class Voladora():
    def __init__(self, Nombre):
        self.Nombre = Nombre

    def Mostrar(self):
        return self.Nombre
    
    @property
    def Mostrar2(self):
        return self.Nombre
        
Objeto22 = Voladora('Erick Josue')
        
print (f'Mi nombre es {Objeto22.Mostrar()}')

print (f'Mi nombre es {Objeto22.Mostrar2}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    def General(self):
        pass

class Sub_Plantilla(Plantilla):
    def Mostrar(self):
        print (f'Esto es un metodo de la sub_plantilla')
        
    def General(self):
        print (f'ESTE METODO ES OBLIGATORIO POR LA PLANTILLA')
        
Objeto23 = Sub_Plantilla()

Objeto23.Mostrar()
Objeto23.General()

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
        
Objeto24 = Pastel1()

Objeto24.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Ingrediente1 = Chocolate()
Objeto25 = Pastel2(Ingrediente1)
Objeto25.Hornear()

Ingrediente2 = Vainilla()
Objeto26 = Pastel2(Ingrediente2)
Objeto26.Hornear()

Ingrediente3 = Fresa()
Objeto27 = Pastel2(Ingrediente3)
Objeto27.Hornear()

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
        
    def Luchar(self):
        print (f'El retador ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Objeto28 = Battle1()

Objeto28.Luchar()

print (f'-' * 20)

class Battle2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Luchar(self):
        print (f'El retador ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Criatura1 = Bulbasaur()
Objeto29 = Battle2(Criatura1)
Objeto29.Luchar()

Criatura2 = Treekoo()
Objeto30 = Battle2(Criatura2)
Objeto30.Luchar()

Criatura3 = Chikorita()
Objeto31 = Battle2(Criatura3)
Objeto31.Luchar()

print (f'-' * 20)

var10 = 117

var10 += 5

print (f'Sumatoria {var10}')

var10 -= 5

print (f'Resta {var10}')

var10 *= 5

print (f'Multiplicacion {var10}')

var10 /= 5

print (f'Division Flotante {var10}')

var10 //= 5

print (f'Division Baja {var10}')

var10 %= 5

print (f'Modulo {var10}')

var10 **= 5

print (f'Exponente {var10}')

print (f'-' * 20)

print (f'Mi nombre es {(Nombre:= "Sofia Vergara")}')

for elemento in range(0, Limite:= 5):
    print (f'El elemento es {elemento}')
    
print (f'-' * 20)

Contador = 0

while (Contador < len(Lista_Walrus := ["Erick", "Josue", "Karlita"])):
    print (f'El nombre del participante es {Lista_Walrus[Contador]}')
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

variable4 = Objeto10.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = True, Objeto11.Catched

# Esto es un comentario simple

'''
Esto
Es
Un
Comentario
Compuesto o
Un DocString
'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene actualmente {Variable_Sumatoria}, {Sumatoria2(1, 2, 3, 4)} o incluso {Objeto10.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Erick' in PEPE.Lista1)
print (f'Gary' not in PEPE.Tupla_Poke)
print (f'{PEPE.Diccionario_Poke["Poke3"]}' in PEPE.Set_Conjunto_Poke1)

try:
    snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke
    
    print (f'Esto es un desempaquetado de variables {snake_case2}')
except ValueError as Errore5:
    print (f'Error, la declaracion snake case y desempaquetado es incorrecto -> {str(Errore5)}')
    
print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto11.Cantidad, Sumatoria2(1, 2, 1, 1))

print (f'El Cociente de la operacion es {Cociente}')
print (f'El Residuo de la operacion es {Residuo}')

print (f'{PEPE.Lista2}')
print (f'{PEPE.Lista2[::2]}')
print (f'{PEPE.Lista2[::3]}')
print (f'{PEPE.Lista2[:2]}')
print (f'{PEPE.Lista2[2:]}')
print (f'{PEPE.Lista2[2:3]}')
print (f'{PEPE.Lista2[0:None]}')
print (f'{PEPE.Lista2[:]}')

print (f'{Lista_Uno[0]} eso que esta ahi es un {PEPE.Lista2[2]}?')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, 200, Anonima1(50, 2))

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

Diccionario_Numeral4 = dict({
    'Num1' : 45,
    'Num2' : 4,
    'Num3' : 71,
    'Num4' : 9,
    'Num5' : 0,
    'Num6' : 8
})

print (f'{Diccionario_Numeral4}')

Diccionario_Numeral4_Sorted = dict(sorted(Diccionario_Numeral4.items(), key=lambda item : item[1]))

print (f'{Diccionario_Numeral4_Sorted}')

Diccionario_Numeral4_Sorted_Min = min(Diccionario_Numeral4_Sorted.items(), key=lambda item : item[1])
Diccionario_Numeral4_Sorted_Max = max(Diccionario_Numeral4_Sorted.items(), key=lambda item : item[1])

print (f'{Diccionario_Numeral4_Sorted_Min}')
print (f'{Diccionario_Numeral4_Sorted_Max}')

print (f'{dir(PEPE)}')

Tupla1 = ('Uno', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos',)

print (f'{Tupla1}')

Tupla1 = tuple(('Uno', 'Dos', 'Tres',))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')

Set_Conjunto1 = {Objeto9.Tipo, 'Electrico', 'Electrico', 'Electrico', 'Electrico', 'Electrico', 'Electrico'}
Set_Conjunto2 = set({f'{Objeto11.Sub_Tipo}'})
Set_Conjunto1.add('Dragon')
Set_Conjunto1.update(Set_Conjunto2)

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Uno', 'Dos', 'Tres'})

print (f'{Set_Conjunto1}')

Set_Conjunto3 = {1, 2, 3, 4, 5}
Set_Conjunto4 = {4, 5}
Set_Conjunto5 = set({8})

print (f'{Set_Conjunto3.issuperset(Set_Conjunto4)}')
print (f'{Set_Conjunto3 >= Set_Conjunto4}')

print (f'{Set_Conjunto4.issubset(Set_Conjunto3)}')
print (f'{Set_Conjunto4 <= Set_Conjunto3}')

print (f'{Set_Conjunto3.isdisjoint(Set_Conjunto5)}')

print (f'-' * 20)

Set_ConjuntoA = {1, 2, 3, 4}
Set_ConjuntoB = {3, 4, 5, 6}

print (f'{Set_ConjuntoA.union(Set_ConjuntoB)}')
print (f'{Set_ConjuntoA | Set_ConjuntoB}')

print (f'-' * 20)

print (f'{Set_ConjuntoA.intersection(Set_ConjuntoB)}')
print (f'{Set_ConjuntoA & Set_ConjuntoB}')

print (f'-' * 20)

print (f'{Set_ConjuntoA.difference(Set_ConjuntoB)}')
print (f'{Set_ConjuntoA - Set_ConjuntoB}')

print (f'-' * 20)

print (f'{Set_ConjuntoB.difference(Set_ConjuntoA)}')
print (f'{Set_ConjuntoB - Set_ConjuntoA}')

print (f'-' * 20)

print (f'{Set_ConjuntoA.symmetric_difference(Set_ConjuntoB)}')
print (f'{Set_ConjuntoA ^ Set_ConjuntoB}')

print (f'-' * 20)

'''Set_ConjuntoA.update(Set_ConjuntoB)

print (f'{Set_ConjuntoA}')'''

'''Set_ConjuntoA.difference_update(Set_ConjuntoB)

print (f'{Set_ConjuntoA}')'''

'''Set_ConjuntoB.difference_update(Set_ConjuntoA)

print (f'{Set_ConjuntoB}')'''

'''Set_ConjuntoA.intersection_update(Set_ConjuntoB)

print (f'{Set_ConjuntoA}')'''

'''Set_ConjuntoA.symmetric_difference_update(Set_ConjuntoB)

print (f'{Set_ConjuntoA}')'''

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')
Set_Conjunto_Menu2 = frozenset({'Caramelo'})
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, 'ChocoMenta'})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Objeto11.Cantidad,
    'Votante' : variable6
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

Diccionario1["Nombre"] = variable1

print (f'{Diccionario1}')

Diccionario1_Copia = Diccionario1.copy()

del Diccionario1["Nombre"]

Diccionario1.pop("Edad")

Diccionario1.clear()

print (f'{Diccionario1}')
print (f'{Diccionario1_Copia}')

print (f'-' * 20)

Diccionario1 = dict({1 : PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Ash")], 2 : Variable_Sumatoria, 3 : Objeto11.Catched})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario2["Nombre"][2]} no puede votar ya que solo tiene {Diccionario1[2]} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', Objeto9.Tipo)
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio3 = dict({})

Diccionario2['Dos'] = variable1

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')
print (f'{Diccionario_Vacio3}')

for clave, valor in PEPE.Diccionario_Poke.items():
    Diccionario_Vacio3[clave] = valor
    
print (f'{Diccionario_Vacio3}')

print (f'-' * 20)

Key3 = [f'Key{i}' for i in range(len(Lista_Uno_Copia))]

print (f'{Key3}')
print (f'{Lista_Uno_Copia}')

Diccionario4 = dict(zip(Key3, Lista_Uno_Copia))

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Key1"]}')
print (f'{Diccionario4.get("Key2")}')

print (f'-' * 20)

for elemento in Diccionario1:
    print (f'{Diccionario1[elemento]}')
    
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
    print (f'Error, la fecha tiene un formato invalido')
    exit()
    
Cargar_Csv3['TOTALITO'] = Cargar_Csv3['quantity'] * Cargar_Csv3['price']
    
Encontrado3 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech3_Formateada.date()]

if (Encontrado3.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! se han encontrado ventas en esta fecha')
    
    Grupo6 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo6_Min = Grupo6.idxmin()
    Grupo6_Max = Grupo6.idxmax()
    Grupo6_Min_Cant = Grupo6.min()
    Grupo6_Max_Cant = Grupo6.max()
    
    print (f'En la fecha {Fech3_Formateada} el producto {Grupo6_Min} vendio {Grupo6_Min_Cant} unidades')
    print (f'En la fecha {Fech3_Formateada} el producto {Grupo6_Max} vendio {Grupo6_Max_Cant} unidades')
    
    print (f'La cantidad de clieentes que compraron hoy fue {Grupo6.count()}')
    
    print (f'La cantidad de ventas registradas en esta fecha fue {Grupo6.sum()}')
    
    print (f'El promedio de ventas en esta fecha fue de {round(Grupo6.mean(), 2)}')
    
    Grupo7 = Encontrado3.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue ${Grupo7.sum()}')
    
    Promedio2 = Grupo7.sum() / Grupo6.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio2, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Grupo7.mean(), 2)}')
    
print (f'-' * 20)

Lista_Csv3 = list(Cargar_Csv3['product'])
Key4 = [f'Key_{i}' for i in range(len(Lista_Csv3))]

Diccionario5 = dict(zip(Key4, Lista_Csv3))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key_3"]}')
print (f'{Diccionario5.get("Key_5")}')

print (f'-' * 20)

for indice, elemento in Diccionario5.items():
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

for indice, elemento in Cargar_Csv3.iterrows():
    Unidad5 = elemento['product']
    Unidad6 = elemento['price']
    
    print (f'El precio del producto {Unidad5} es ${Unidad6}')
    
print (f'-' * 20)

Diccionario_Numeral5 = dict({
    'Num1' : 45,
    'Num2' : 4,
    'Num3' : 71,
    'Num4' : 9,
    'Num5' : 0,
    'Num6' : 8
})

Diccionario_Numeral5_Sorted = dict(sorted(Diccionario_Numeral5.items(), key=lambda item : item[1]))

Diccionario_Numeral5_Sorted_Min = min(Diccionario_Numeral5.items(), key=lambda item : item[1])
Diccionario_Numeral5_Sorted_Max = max(Diccionario_Numeral5.items(), key=lambda item : item[1])

print (f'{Diccionario_Numeral5}')
print (f'{Diccionario_Numeral5_Sorted}')
print (f'{Diccionario_Numeral5_Sorted_Min}')
print (f'{Diccionario_Numeral5_Sorted_Max}')

print (f'-' * 20)

'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda num : num[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El nombre del estudiante menor es {Menore} y su edad es {Lista[0][1]} años')
    print (f'El nombre del estudiante menor es {Mayore} y su edad es {Lista[-1][1]} años')

Colegio(Lista_Alumnos)'''

print (f'-' * 20)

Division_Baja = 14 // 7 
Exponente = 4**3
Modulo = 20 % 6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'El tipo de variable es {type(variable1)}')
print (f'El tipo de variable es {type(variable4)}')
print (f'El tipo de variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de variable es {type(Objeto11.Catched)}')
print (f'El tipo de variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de variable es {type(PEPE.Tupla_Poke)}')
print (f'El tipo de variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de variable es {type(Data_Frame_Concatenate)}')
print (f'El tipo de variable es {type(Array2_Sorted)}')
print (f'El tipo de variable es {type(Diccionario1_Copia)}')
print (f'El tipo de variable es {type(Objeto12)}')
print (f'El tipo de variable es {type(Funcion_Diccionario)}')
print (f'El tipo de variable es {type(PEPE)}')

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

variable8 = Saludar_Dos()
variable9 = Variable_Sumatoria

if (variable8 == Lista_Uno_Copia[0] and variable9 < 20):
    print (f'Correcto, ambas variables se cumplen')
else:
    print (f'Error, al menos una de las variables no se cumple')
    
print (f'-' * 20)

if (variable8 == Lista_Uno_Copia[0] or variable9 > 20):
    print (f'Al menos una de las variables se cumple')
else:
    print (f'Error, ninguna de las variables se cumple')
    
print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Variable_Sumatoria,
        self.Classified = [True, not True, False]

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')
        
    def __str__(self):
        return self.City
    
    def __getitem__(self, Indice):
        return self.Classified[Indice]
    
Objeto32 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto9.Nombre)
Objeto33 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto10.Nombre)
Objeto34 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto11.Nombre)

Objeto32.Desplegar()
Objeto33.Desplegar()
Objeto34.Desplegar()

print (f'-' * 20)

print (f'El nombre de la ciudad es {Objeto32.City}')
print (f'El nombre de la ciudad es {Objeto33.City}')
print (f'El nombre de la ciudad es {Objeto34.City}')

print (f'-' * 20)

print (f'El elemento con indice 0 es {Objeto33[0]}')
print (f'El elemento con indice 0 es {Objeto33[1]}')
print (f'El elemento con indice 0 es {Objeto33[2]}')

print (f'-' * 20)

Negativo = -8

print (f'Ahora es positivo {int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima5 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable}')
print (f'{list(Anonima5)}')
print (f'{Lista_Iterable}')

print (f'-' * 20)

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
    print (f'Gracias por la informacion ingresada')
else:
    print (f'Error, ingrese una cadena de texto')
    
for elemento in Lista_Uno_Copia:
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in enumerate(Lista_Uno_Copia):
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

print (f'-' * 20)

Lista_Nombres3 = ['juan salvo', 'henry courtney', 'elizabeth bennet', 'marge simpson']
Lista_Nombres3_Updated = []

for elemento in Lista_Nombres3:
    Lista_Nombres3_Updated.append(elemento.title())
    
print (f'{Lista_Nombres3}')
print (f'{Lista_Nombres3_Updated}')

print (f'-' * 20)

print (f'{variable10.lower().find("t")}')
print (f'{variable10.lower().index("b")}')

print (f'La letra {variable10_letra} aparece un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = '          Lautaro'

print (f'{variable11}')
print (f'{variable11.strip()}')

variable11_Version1 = ' '.join(variable11.split())

print (f'{variable11_Version1}')

variable12 = '----hola mundo***'

print (f'{variable12.strip("-*")}')

variable13 = 'esto es un texto cualquiera para ver si esto sirve o no'

Lista_variable13 = variable13.split(' ')

for elemento in enumerate(Lista_variable13, start=1):
    print (f'{elemento[0]} : {elemento[1]}')
    
print (f'La cantidad de palabras digitadas es {len(Lista_variable13)}')

print (f'-' * 20)

var11 = 'hola'

if (isinstance(var11, (str))):
    print (f'Lo que ingresaste es un texto')
else:
    print (f'Error, lo que ingresaste no es un texto')
    
if (var11.isalpha()):
    print (f'Lo que ingresaste es un texto')
else:
    print (f'Error, lo que ingresaste no es un texto')
    
try:
    Textico = var11.__len__()
    print (f'Lo que ingresaste es un texto')
except Exception:
    print (f'Error, lo que ingresaste no es un texto')
    
print (f'-' * 20)

var12 = 3.5

if (isinstance(var12, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, lo que ingresaste no es un numero decimal')
    
try:
    Numerito6 = float(var12)
    if (Numerito6.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var13 = '3'

if (isinstance(var13, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')
    
if (var13.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')
    
if (var13.isdecimal()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')
    
try:
    Numerito7 = float(var13)
    if (Numerito7.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var14 = 3

if (isinstance(var14, (int, float))):
    print (f'Lo que ingresaste es un numero entero o decimal')
else:
    print (f'Error, lo que ingresaste no es un numero')
    
try:
    Numerito8 = float(var14)
    if (Numerito8.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except Exception:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var15 = 'erick123'

if (isinstance(var15, (str, int))):
    print (f'Esta variable tiene texto o numeros')
else:
    print (f'Error, el formato es incorrecto')
    
if (var15.isalnum()):
    print (f'Esta variable tiene texto o numeros')
else:
    print (f'Error, el formato es incorrecto')
    
print (f'-' * 20)

var16 = '    a      w'

if (var16.isspace()):
    print (f'Esto esta compuesto por espacios nada mas')
else:
    print (f'Error, esto tiene mas que solo espacios')
    
print (f'{var16}')
print (f'{var16.strip()}')

var16_Version1 = ' '.join(var16.split())

print (f'{var16_Version1}')

print (f'-' * 20)

var17 = 'eSteBAN'

if (var17.lower().islower()):
    print (f'Esto esta compuesto solo por letras minusculas')
else:
    print (f'Error, esto tiene mucho mas que solo minusculas')
    
if (var17.upper().isupper()):
    print (f'Esto esta compuesto solo por letras mayusculas')
else:
    print (f'Error, esto tiene mucho mas que solo mayusculas')
    
if (var17.title().istitle()):
    print (f'Esto esta compuesto solo por letras camel case')
else:
    print (f'Error, esto tiene mucho mas que solo camel case')
    
print (f'-' * 20)

var18 = ' '

if (bool(var18) == True):
    print (f'Gracias por ingresar esta informacion')
else:
    print (f'Error, ingrese una cadena de texto')
    
print (f'-' * 20)

print (f'{PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

Eliminado1 = Diccionario1_Copia.pop("Nombre")

print (f'El elemento eliminado es {Eliminado1}')

try:
    snake_case4, snake_case5, snake_case6, snake_case7 = PEPE.Set_Conjunto_Poke1
except ValueError as Errore6:
    print (f'Error, el desempaquetado fue hecho erroneamente -> {str(Errore6)}')
    
print (f'-' * 20)

Contador = 0

while (Contador < 5):
    print (f'El contador es {Contador + 1}')
    Contador += 1
    
print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros[:])):
    print (f'El numero es {PEPE.Lista_Numeros[Contador] * 100}')
    Contador += 1
    
print (f'-' * 20)

Lista_Animales2 = list([])
Lista_Animales2.append('Oso')
Lista_Animales2.insert(1, 'Caballo')
Lista_Animales2.extend(['Tortuga'])
Lista_Animales3 = ['Raton']

Lista_Animales4 = Lista_Animales2 + Lista_Animales3

Contador = 0

while (Contador < len(Lista_Animales4)):
    if (Lista_Animales4[Contador] == Lista_Animales3[0]):
        print (f'This animal is mouse in english')
        break
    else:
        Contador += 1
        continue
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Csv3, PEPE.Set_Conjunto_Poke1):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento1, elemento2, elemento3, elemento4 in zip(Lista_Csv3, PEPE.Set_Conjunto_Poke1, Tupla1, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2} -- {elemento3} -- {elemento4}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'El numero es {elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'El numero es {elemento}')
    
print (f'-' * 20)

for elemento in range(0 + 2, len(Lista_Animales4[:])):
    print (f'El numero es {elemento}')
    
print (f'-' * 20)

Lista_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{PEPE.Lista_Numeros}')
print (f'{Lista_Mult}')

Menor = min(Lista_Mult)
Mayor = max(Lista_Mult)
Redondeado = round(14.458795, 2)
Sumatoria4 = sum(Lista_Mult)

print (f'{bool("")}')
print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool(not True)}')
print (f'{bool(False)}')
print (f'{bool()}')

Todo_All = all([Lista_Animales4, Set_Conjunto1, None])

print (f'{Todo_All}')

print (f'-' * 20)

Uno = int('500')
Dos = str(variable4)
Tres = float(Uno)
Cuatro = list(PEPE.Set_Conjunto_Poke1)
Cinco = tuple(Lista_Animales4)
Seis = set(PEPE.Tupla_Poke)

print(f'Original: {type("500")} -- Actualizado: {type(Uno)}')
print(f'Original: {type(variable4)} -- Actualizado: {type(Dos)}')
print(f'Original: {type(Uno)} -- Actualizado: {type(Tres)}')
print(f'Original: {type(PEPE.Set_Conjunto_Poke1)} -- Actualizado: {type(Cuatro)}')
print(f'Original: {type(Lista_Animales4)} -- Actualizado: {type(Cinco)}')
print(f'Original: {type(PEPE.Tupla_Poke)} -- Actualizado: {type(Seis)}')

print (f'-' * 20)

Any_Iterable2 = any(num % 2 != 0 for num in PEPE.Lista_Numeros)
Anonima6 = filter(lambda Num : Num % 2 != 0, PEPE.Lista_Numeros)
Lista_Iterable2 = [num for num in PEPE.Lista_Numeros if num % 2 != 0]

print (f'{Any_Iterable2}')
print (f'{list(Anonima6)}')
print (f'{Lista_Iterable2}')

Diccionario_Lenguajes5 = {"python": 4, "java": 2, "c++": 2, "go": 1}

Diccionario_Lenguajes5_Sorted = dict(sorted(Diccionario_Lenguajes5.items(), key=lambda item : item[1]))

Diccionario_Lenguajes5_Sorted_Min = min(Diccionario_Lenguajes5.items(), key=lambda item : item[1])
Diccionario_Lenguajes5_Sorted_Max = max(Diccionario_Lenguajes5.items(), key=lambda item : item[1])

print (f'{Diccionario_Lenguajes5}')
print (f'{Diccionario_Lenguajes5_Sorted}')
print (f'{Diccionario_Lenguajes5_Sorted_Min}')
print (f'{Diccionario_Lenguajes5_Sorted_Max}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto_Poke1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

print (f'-' * 20)

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE2 = PEPE3

print (f'-' * 20)

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda Num : Num[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El estudiante {Menore} tiene {Lista[0][1]} años')
    print (f'El estudiante {Mayore} tiene {Lista[-1][1]} años')

Colegio(Lista_Alumnos)'''

'''def Exception_Finale():
    while True:
        Numerito9 = input(f'Ingrese un numero: ')
        try:
            Numerito10 = float(Numerito9)
            if (Numerito10.is_integer()):
                print (f'Lo que ingresaste fue un numero entero')
                break
            else:
                print (f'Lo que ingresaste fue un numero decimal')
                break
        except Exception:
            print (f'Errror, necesito que ingreses un numero')

Exception_Finale()'''

import pandas as pd
import requests
import io

Ruta_Html2 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html2, headers=headers)

Leer_Html2 = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Leer_Html2)

print (f'{Cargar_Html2[2].head()}')

print (f'-' * 20)

import re

Texto14 = 'ericksuper80@gmail.com'

Pattern14 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)$'

Buscar22 = bool(re.fullmatch(Pattern14, Texto14))

if (Buscar22 == True):
    print (f'El correo electronico tiene un formato correcto')
else:
    print (f'Error, el correo tiene un formato incorrecto')
    
print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv4 = 'C:\\Repo\\Store.csv'

Cargar_Csv4 = pd.read_csv(Ruta_Csv4)

print (f'{Cargar_Csv4}')

print (f'-' * 20)

Fecha4 = '2026-04-01'

try:
    Fech4 = datetime.strptime(Fecha4, '%Y-%m-%d').date()
    Fech4_Formateada = pd.to_datetime(Fech4)
    Cargar_Csv4['date'] = pd.to_datetime(Cargar_Csv4['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato incorrecto')
    exit()
    
Cargar_Csv4['TOTALITO'] = Cargar_Csv4['quantity'] * Cargar_Csv4['price']
    
Encontrado4 = Cargar_Csv4[Cargar_Csv4['date'].dt.date == Fech4_Formateada.date()]

if (Encontrado4.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! Encontramos ventas en esta fecha')
    
    Grupo8 = Encontrado4.groupby('product')['quantity'].sum()
    Grupo8_Min = Grupo8.idxmin()
    Grupo8_Max = Grupo8.idxmax()
    Grupo8_Min_Cant = Grupo8.min()
    Grupo8_Max_Cant = Grupo8.max()
    
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo8_Min} vendio {Grupo8_Min_Cant} unidades')
    print (f'En la fecha {Fech4_Formateada} el producto {Grupo8_Max} vendio {Grupo8_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron fue {Grupo8.count()}')
    
    print (f'La cantidad de productos vendidos fue {Grupo8.sum()}')
    
    print (f'El promedio de productos vendidos es {round(Grupo8.mean(), 2)}')
    
    Grupo9 = Encontrado4.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue ${Grupo9.sum()}')
    
    Promedio4 = Grupo9.sum() / Grupo9.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Promedio4, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Grupo9.mean(), 2)}')
    
print (f'-' * 20)

Diccionario_Lenguajes6 = {}

def Ejercicio75(Diccionario):
    Lista_Repetidos = list([])
    Clave = next(iter(Diccionario))
    Valor = Diccionario[Clave]
    
    for indice, elemento in Diccionario.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    for indice, elemento in Diccionario.items():
        if (elemento == Valor):
            Lista_Repetidos.extend([indice])
        else:
            continue
        
    if (len(Lista_Repetidos) > 1):
        return Lista_Repetidos
    else:
        return Clave

if (len(Diccionario_Lenguajes6) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Sample75 = Ejercicio75(Diccionario_Lenguajes6)
    print (f'{Sample75}')
    
print (f'-' * 20)

Lista_Ejercicio20 = ["manzana", "zanahoria", "kiwi", "pera", "tomate"]

Canastas3 = {
    "frutas": [],     # se llenará con frutas
    "verduras": [],   # se llenará con verduras
    "otros": []       # se llenará con lo que no sea fruta ni verdura
}

def Ejercicio76(Diccionario, Lista):
    if (len(Lista) == 0):
        return None
    else:
        fruta = ["manzana","banana","pera"]
        verdura = ["zanahoria","lechuga","tomate"]
        
        for elemento in Lista:
            if (elemento in fruta):
                Diccionario['frutas'].append(elemento)
            elif (elemento in verdura):
                Diccionario['verduras'].append(elemento)
            else:
                Diccionario['otros'].append(elemento)
                
        return Diccionario

Sample76 = Ejercicio76(Canastas3, Lista_Ejercicio20)

if (Sample76 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'{Sample76}')
    
print (f'-' * 20)

Lista_Ejercicio21 = [("fruta","manzana"), ("verdura","zanahoria"), ("fruta","pera"), ("fruta","banana"), ("verdura","tomate")]

def Ejercicio77(Lista):
    Diccionario_Vacio4 = dict({})
    
    for clave, valor in Lista:
        if (clave not in Diccionario_Vacio4):
            Diccionario_Vacio4[clave] = []
            Diccionario_Vacio4[clave].append(valor)
        else:
            Diccionario_Vacio4[clave].append(valor)
            
    return Diccionario_Vacio4

Sample77 = Ejercicio77(Lista_Ejercicio21)

if (Lista_Ejercicio21):
    print (f'{Sample77}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)