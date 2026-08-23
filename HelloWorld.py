try:
    import Module_Own as PEPE
except (ImportError, ModuleNotFoundError):
    print (f'Error, el modulo seleccionado no existe')
    exit() #raise
    
def Sumar(Numero):
    return Numero + 10

def Multiplicar(Numero):
    return Numero * 10

def Operar(Funcion, Numero):
    return Funcion(Numero)

print (f'El resultado de la suma es {Operar(Sumar, 5)}')
print (f'El resultado de la multiplicacion es {Operar(Multiplicar, 5)}')

print (f'-' * 20)

Lista_Nombres = ['Erick', 'Josue']
Lista_Nombres.append('Karlita')
Lista_Nombres.insert(1, 'Carmelo')
Lista_Nombres.extend(['Susanita', 'Roxana'])

print (f'{Lista_Nombres}')

def Recorrer_Lista1(Lista):
    for elemento in Lista[:3]:
        print (f'{elemento}')

def Recorrer_Lista2(Lista):
    for elemento in Lista[3:]:
        print (f'{elemento}')
    
def Recorrido(Funcion, Elementos):
    return Funcion(Elementos)

Recorrido(Recorrer_Lista1, Lista_Nombres)

print (f'-' * 20)

Recorrido(Recorrer_Lista2, Lista_Nombres)

print (f'-' * 20)

def Sumar2(Num1, Num2):
    return Num1 + Num2 + 10

def Multiplicar2(Num1, Num2):
    return Num1 * Num2 * 10

def Operar2(Funcion, Primero, Segundo):
    return Funcion(Primero, Segundo)

print (f'El resultado de la sumatoria es {Operar2(Sumar2, 1, 2)}')
print (f'El resultado de la multiplicacion es {Operar2(Multiplicar2, 1, 3)}')

Diccionario_Superior = dict({
    'Num1' : 1,
    'Num2' : 2,
    'Num3' : 3,
    'Num4' : 4,
    'Num5' : 5
})

def Dict_Pares(Diccionario):
    Lista_Pares = []
    
    for _, valor in Diccionario.items():
        if (valor % 2 == 0):
            Lista_Pares.append(valor)
        else:
            continue
        
    return Lista_Pares

def Dict_ImPares(Diccionario):
    Lista_Impares = list([])
    
    for valor in Diccionario.values():
        if (valor % 2 != 0):
            Lista_Impares.extend([valor])
        else:
            continue
        
    return Lista_Impares

def Evaluar1(Funcion, Dict):
    return Funcion(Dict)

print (f'Lista de elementos pares: {Evaluar1(Dict_Pares, Diccionario_Superior)}')
print (f'Lista de elementos impares: {Evaluar1(Dict_ImPares, Diccionario_Superior)}')

print (f'-' * 20)

Lista_Animales1 = ['Perro', 'Ardilla']
Lista_Animales1.append('Cocodrilo')
Lista_Animales1.insert(1, 'Canguro')
Lista_Animales1.extend(['Tiburon'])

def Ejercicio1(Lista):
    while (Lista):
        print (f'{Lista}')
        del Lista[0]

Sample1 = Ejercicio1(Lista_Animales1)

print (f'-' * 20)

def Ejercicio2(Num1:int, Num2:int) -> int:
    '''Esto es un docstring que explica la funcionalidad de esta funcion
        La funcion toma dos argumentos numericos, los suma y despliega el resultado
    '''
    return Num1 + Num2

Sample2 = Ejercicio2(12, 7)

print (f'{Sample2}')

print (f'{help(Ejercicio2)}')

print (f'-' * 20)

def Ejercicio3(texto='Nada que mostrar'):
    return texto

Sample3 = Ejercicio3()

print (f'{Sample3}')

print (f'-' * 20)

def Ejercicio4(Num1=1, Num2=2, Num3=3):
    return Num1 + Num2 + Num3

Sample4 = Ejercicio4()

print (f'El resultado de la operacion es {Sample4}')

print (f'-' * 20)

def Ejercicio5(Num1=1, Num2=2, Num3=3):
    return Num1 + Num2 + Num3

Sample5 = Ejercicio5(4, 5, 8)

print (f'El resultado de la operacion es {Sample5}')

print (f'-' * 20)

def Ejercicio6(Num1, Num2, Num3=300):
    return Num1 + Num2 + Num3

Sample6 = Ejercicio6(1, 1)

print (f'El resultado de la operacion es {Sample6}')

print (f'-' * 20)

def Ejercicio7(*args):
    return round(sum(args) / len(args), 2)

Sample7 = Ejercicio7(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print (f'El promedio de los numeros elegidos es {Sample7}')

print (f'-' * 20)

def Ejercicio8(**kwargs):
    Acumulador = 0
    
    for _, valor in kwargs.items():
        Acumulador += valor
        
    return Acumulador

Sample8 = Ejercicio8(
    Num1 = 2,
    Num2 = 5,
    Num3 = 7
)

print (f'El resultado de sumar todos los numeros del diccionario es {Sample8}')

print (f'-' * 20)

def Ejercicio9(Num1, Num2, *args, **kwargs):
    Acumulador = 0
    
    for _, valor in kwargs.items():
        Acumulador += valor

    return Num1 + Num2 + sum(args) + Acumulador

Sample9 = Ejercicio9(
    2, 3,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    num1=6, num2=8, num3=11
)

print (f'El resultado de la operacion es {Sample9}')

print (f'-' * 20)

def Ejercicio10(*participantes, **detalles):
    
    print (f'Lista de participantes: {participantes}')
    for elemento in participantes[:]:
        print (f'- {elemento}')
        
    print (f'Detalles del evento: {detalles}')
    
    for clave, valor in detalles.items():
        print (f'{clave} : {valor}')

Sample10 = Ejercicio10(
    'Erick', 'Josue', 'Karlita', 'Carmelo', 'Susanita', 'Roxana',
    dia_evento = 'lunes',
    lugar = 'Iglesia Santa Barbara',
    tema = 'Gran Vingo'
)

print (f'-' * 20)

def Ejercicio11(Limite):
    Lista_Fibonacci = [0, 1]
    Temporal = 0
    
    while (len(Lista_Fibonacci) < Limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

Sample11 = Ejercicio11(10)

print (f'La lista Fibonacci es {Sample11}')

print (f'-' * 20)

Lista_Primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
Lista_Segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]

def Ejercicio12(Lista1, Lista2):
    Set_Conjunto_Tercera = set({})
    Lista_Tercera = list([])
    
    for elemento in Lista1:
        if elemento in Lista2:
            Set_Conjunto_Tercera.add(elemento)
        else:
            continue
        
    Lista_Tercera = list(Set_Conjunto_Tercera)
    
    return Lista_Tercera

Sample12 = Ejercicio12(Lista_Primera, Lista_Segunda)

if (len(Lista_Primera) == 0 or len(Lista_Segunda) == 0):
    print (f'Error, al menos una de las listas esta vacia')
else:
    print (f'Lista resultado: {Sample12}')
    
print (f'-' * 20)

var1 = 3

print (f'{type(var1)}')

var1 += 3.5

print (f'{type(var1)}')

print (f'-' * 20)

var1 = 3

print (f'{type(var1)}')

var1 = str(var1)

print (f'{type(var1)}')

print (f'-' * 20)

Lista_Elemento1 = [1, 2, 3]
Lista_Elemento2 = list([4, 5, 6])

Tupla_Elemento1 = ('uno', 'dos', 'tres',)
Tupla_Elemento2 = 'cuatro', 'cinco', 'seis',

print (f'La concatenacion de listas es {Lista_Elemento1 + Lista_Elemento2}')

print (f'La concatenacion de tuplas es {Tupla_Elemento1 + Tupla_Elemento2}')

print (f'-' * 20)

var2 = 0 # 3, -3, -3.5 todo esto es valido, 0 no es valido

if (var2):
    print (f'Este numero es valido')
else:
    print (f'Esto es invalido')
    
print (f'-' * 20)

var3 = ''  # Cualquier texto es valido, vacio es invalido

if (var3):
    print (f'Este texto es valido')
else:
    print (f'Esto es invalido')
    
print (f'-' * 20)

Lista_Frutas = []

if (Lista_Frutas):
    print (f'Esta lista es valida')
else:
    print (f'Esto es invalido')
    
print (f'-' * 20)

Diccionario_Personas = dict({})

if (Diccionario_Personas):
    print (f'Este diccionario es valido')
else:
    print (f'Esto es invalido')
    
print (f'-' * 20)

var4 = None

if (var4):
    print (f'Esto tiene asignacion, es valido')
else:
    print (f'No tiene una asignacion, es invalido')
    
print (f'-' * 20)

Lista_Ejercicio1 = [1, 2, 3, 4, 5]

def Ejercicio13(Lista):
    if (not len(Lista)):
        return None
    else:
        Contador = 0
        while (Contador < len(Lista)):
            Contador += 1
            
        return Contador

Sample13 = Ejercicio13(Lista_Ejercicio1)

if (Sample13 is None):
    print (f'Error, La lista esta vacia')
else:
    print (f'La lista tiene {Sample13} elementos')
    
print (f'-' * 20)

def Ejercicio14(Lista):
    Acumulador = 0
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador += elemento
        else:
            continue
        
    return Acumulador

Sample14 = Ejercicio14(Lista_Ejercicio1)

if (not len(Lista_Ejercicio1)):
    print (f'Error, la lista esta vacia')
else:
    if (not Sample14):
        print (f'No hay numeros pares en la lista')
    else:
        print (f'El resultado de sumar todos los numeros pares de la lista es {Sample14}')
        
print (f'-' * 20)

def Ejercicio15(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        
        for elemento in Lista[:]:
            Acumulador += elemento
            
        return Acumulador

Sample15 = Ejercicio15(Lista_Ejercicio1)

if (Sample15 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El resultadod de sumar todos los elementos de la lista es {Sample15}')
    
print (f'-' * 20)

def Ejercicio16(Lista):
    Acumulador = 0
    for elemento in Lista[:-1]:
        Acumulador += elemento
        
    return Acumulador

Sample16 = Ejercicio16(Lista_Ejercicio1)

if (len(Lista_Ejercicio1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de los numeros de la lista menos el ultimo es {Sample16}')
    
print (f'-' * 20)

def Ejercicio17(Lista, Numero):
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

Identificado = 4

Sample17 = Ejercicio17(Lista_Ejercicio1, Identificado)

if (Sample17 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample17 == True):
        print (f'El numero {Identificado} fue encontrado en la lista')
    else:
        print (f'Error, el numero no fue encontrado en la lista')
        
print (f'-' * 20)

def Ejercicio18(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    Lista_Resultado = [Menore, Mayore]
    
    return Lista_Resultado

Sample18 = Ejercicio18(Lista_Ejercicio1)

if (not len(Lista_Ejercicio1)):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de los numeros de la lista es {min(Sample18)}')
    print (f'El mayor de los numeros de la lista es {max(Sample18)}')
    
print (f'-' * 20)

def Ejercicio19(Lista, Numero):
    if (not len(Lista)):
        return None
    else:
        Contador = 0
        
        for elemento in Lista[:]:
            if (elemento > Numero):
                Contador += 1
            else:
                continue
            
        return Contador
    
Limite1 = 2

Sample19 = Ejercicio19(Lista_Ejercicio1, Limite1)

if (Sample19 is None):
    print (f'Error, la lista esta vacia')
else:
    if (not Sample19):
        print (f'Error, no hay ningun numero en la lista mayor que {Limite1}')
    else:
        print (f'La cantidad de numeros mayores que {Limite1} es {Sample19}')
        
print (f'-' * 20)

def Ejercicio20(Lista):
    Lista_Pares = []
    Lista_Impares = list([])
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            Lista_Impares.extend([elemento])
            
    return Lista_Pares, Lista_Impares

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
        
        for elemento in Lista[:]:
            Lista_Mult.append(elemento * 2)
            
        return Lista_Mult

Sample21 = Ejercicio21(Lista_Ejercicio1)

if (Sample21 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Ejercicio1}')
    print (f'Lista Actualizada: {Sample21}')
    
print (f'-' * 20)

'''Lista_Promedio = []

def Ejercicio22(Limite):
    Contador = 0
    
    while (Contador < Limite):
        while (True):
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
                print (f'Error, lo ingresado no es un numero')
        Contador += 1

Sample22 = Ejercicio22(3)

Promedio1 = sum(Lista_Promedio) / Lista_Promedio.__len__()

print (f'El promedio de las notas ingresadas es {round(Promedio1, 2)}')'''

Lista_Ejercicio2 = list([5, -6, 0, -1, -3, 0])

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

if (not len(Lista_Ejercicio2)):
    print (f'Error, la lista esta vacia')
else:
    Num_Positivos, Num_Negativos, Num_Ceros = Sample22
    
    print (f'Cantidad numeros positivos: {Num_Positivos}')
    print (f'Cantidad numeros negativos: {Num_Negativos}')
    print (f'Cantidad numeros ceros: {Num_Ceros}')
    
print (f'-' * 20)

import re

Lista_Ejercicio3 = list([
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
])

def Ejercicio23(Lista):
    Lista_Validos = []
    Lista_Invalidos = list([])
    
    if (len(Lista) == 0):
        return None
    else:
        Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'
        
        for elemento in Lista[:]:
            Buscar = bool(re.fullmatch(Pattern, elemento))
            if (Buscar == True):
                Lista_Validos.append(elemento)
            else:
                Lista_Invalidos.extend([elemento])
                
        return Lista_Validos, Lista_Invalidos

Sample23 = Ejercicio23(Lista_Ejercicio3)

if (Sample23 is None):
    print (f'Error, la lista esta vacia')
else:
    Correos_Validos, Correos_Invalidos = Sample23
    
    print (f'Lista Original: {Lista_Ejercicio3}')
    print (f'Lista Validos: {Correos_Validos}')
    print (f'Lista Invalidos: {Correos_Invalidos}')
    
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

Lista_Ejercicio4 = [-15.5, -8, -3.2, -1, 0, 4, 7.5, 12, 19.1, 25]

def Ejercicio26(Lista):
    if (not len(Lista)):
        return None
    else:
        Contador = 0
        Acumulador = 0
        
        for elemento in Lista[:]:
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
    Cantidad_Positivos, Cantidad_Positivos_Sum = Sample26
    
    if (Cantidad_Positivos):
        print (f'La cantidad de numeros positivos de la lista son {Cantidad_Positivos}')
        print (f'La suma de numeros positivos de la lista es {Cantidad_Positivos_Sum}')
    else:
        print (f'Errorxxx no hay numeros positivos en la lista')
        
print (f'-' * 20)

Lista_Ejercicio5 = list([65, 70, 54, 80, 69, 66])

def Ejercicio27(Lista):
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

Sample27 = Ejercicio27(Lista_Ejercicio5)

if (len(Lista_Ejercicio5) == 0):
    print (f'Error, la lista esta vacia')
else:
    Total_Aprobados, Total_Reprobados, Total_Aprobados_Suma = Sample27
    
    print (f'El total de estudiantes aprobados es: {Total_Aprobados}')
    print (f'El total de estudiantes reprobados es: {Total_Reprobados}')
    print (f'Sumatoria de las notas aprobadas es: {Total_Aprobados_Suma}')
    
print (f'-' * 20)

Lista_Ejercicio6 = [15, 0, 8, 2, 0, 25, 4]

def Ejercicio28(Lista):
    if (not len(Lista)):
        return None
    else:
        Agotado = 0
        Stock_Bajo = 0
        Stock_Alto = 0
        Stock_Bajo_Sum = 0
        Stock_Alto_Sum = 0
        
        for elemento in Lista[0:None]:
            if (elemento == 0):
                Agotado += 1
            elif (elemento <= 1 or elemento <= 5):
                Stock_Bajo += 1
                Stock_Bajo_Sum += elemento
            else:
                Stock_Alto += 1
                Stock_Alto_Sum += elemento
                
        return Agotado, Stock_Bajo, Stock_Alto, Stock_Bajo_Sum, Stock_Alto_Sum

Sample28 = Ejercicio28(Lista_Ejercicio6)

if (Sample28 is None):
    print (f'Error, la lista esta vacia')
else:
    Prod_Agotado, Prod_Stock_Bajo, Prod_Stock_Alto, Prod_Stock_Bajo_Sum, Prod_Stock_Alto_Sum = Sample28
    
    print (f'La cantidad de productos agotados de la lista es {Prod_Agotado}')
    print (f'La cantidad de productos Stock_Bajo de la lista es {Prod_Stock_Bajo}')
    print (f'La cantidad de productos Stock_Alto de la lista es {Prod_Stock_Alto}')
    print (f'Sumatoria productos stock bajo {Prod_Stock_Bajo_Sum}')
    print (f'Sumatoria productos stock alto {Prod_Stock_Alto_Sum}')
    print (f'Sumatoria todos los productos con stock {Prod_Stock_Bajo_Sum + Prod_Stock_Alto_Sum}')
    
print (f'-' * 20)

Lista_Ejercicio7 = list([12, 8, 5, 1, 7, 2, 10])

def Ejercicio29(Lista):
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] == 0):
            return Contador
        else:
            Contador += 1
            continue
        
    return None

Sample29 = Ejercicio29(Lista_Ejercicio7)

if (len(Lista_Ejercicio7) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample29 is None):
        print (f'Por el momento no hay ningun producto agotado')
    else:
        print (f'El primer producto agotado del inventario aparece en la posicion {Sample29}')
        
print (f'-' * 20)

Lista_Ejercicio8 = list([120, 350, 80, 600, 150, 700])

def Ejercicio30(Lista, Numero):
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] > Numero):
            return Contador
        else:
            Contador += 1
            continue
        
    return None

Limite2 = 100

Sample30 = Ejercicio30(Lista_Ejercicio8, Limite2)

if (not len(Lista_Ejercicio8)):
    print (f'Error, la lista esta vacia')
else:
    if (Sample30 is None):
        print (f'No hay ninguna venta en la lista superior al monto limite ${Limite2}')
    else:
        print (f'La primer venta que aparece en la lista mayor que ${Limite2} aparece en la posicion {Sample30}')
        print (f'El monto de esta venta es ${Lista_Ejercicio8[Sample30]}')
        
print (f'-' * 20)

Lista_Ejercicio9 = [10, 2, 5, 4, 3, 1, 6]

# Version1

def Ejercicio31(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            
    return None

Sample31 = Ejercicio31(Lista_Ejercicio9)

if (not len(Lista_Ejercicio9)):
    print (f'Error, la lista esta vacia')
else:
    if (Sample31 is None):
        print (f'No hay ningun numero en la lista que se repita')
    else:
        print (f'El primer numero que se repite en la lista es {Sample31}')
        
print (f'-' * 20)

# Version2

Lista_Ejercicio10 = [10, 2, 1, 4, 3, 5, 6]

def Ejercicio32(Lista):
    for i in range(0, len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                return Lista[j]
            else:
                continue
            
    return None

Sample32 = Ejercicio32(Lista_Ejercicio10)

if (len(Lista_Ejercicio10) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample32 is None):
        print (f'No hay ningun numero en la lista que se repita')
    else:
        print (f'El primer numero que se repite en la lista es {Sample32}')
        
print (f'-' * 20)

Lista_Ejercicio11 = list([90, 91, 79, 82])

def Ejercicio33(Lista):
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] < Lista[i]):
            return i - 1, i
        else:
            continue
        
    return None

Sample33 = Ejercicio33(Lista_Ejercicio11)

if (len(Lista_Ejercicio11) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample33 is None):
        print (f'En la lista, nunca aparece un aumento de ventas en relacion al dia anterior')
    else:
        Anterior, Posterior = Sample33
        print (f'El primer aumento de ventas en relacion con el dia anterior aparece en la posicion {Posterior}')
        print (f'La venta anterior es {Lista_Ejercicio11[Anterior]}')
        print (f'La venta posterior es {Lista_Ejercicio11[Posterior]}')
        
print (f'-' * 20)

Lista_Ejercicio12 = [100, 97, 95, 80, 78]

def Ejercicio34(Lista, Caida):
    Grados = 0
    for i in range(0 + 1, len(Lista)):
        if (Lista[i-1] - Lista[i] >= Caida):
            Grados = Lista[i-1] - Lista[i]
            return Grados, i
        else:
            continue
        
    return None

Limite3 = 10

Sample34 = Ejercicio34(Lista_Ejercicio12, Limite3)

if (not len(Lista_Ejercicio12)):
    print (f'Error, la lista esta vacia')
else:
    if (Sample34 is None):
        print (f'En la ultima hora, no han habido caidas drasticas de temperatura')
    else:
        Cant_Grados, Posicion = Sample34
        print (f'Precaucion! en la posicion {Posicion} hubo una caida de {Cant_Grados} grados centigrados')
        
print (f'-' * 20)

Lista_Ejercicio13 = [1, 1, 0, 1, 3]

def Ejercicio35(Lista):
    for i in range(0 + 2, len(Lista)):
        if (Lista[i - 2] < Lista[i - 1] and Lista[i - 1] > Lista[i]):
            return Lista[i - 1]
        else:
            continue
        
    return None

Sample35 = Ejercicio35(Lista_Ejercicio13)

if (len(Lista_Ejercicio13) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample35 is None):
        print (f'No hay ningun numero en la lista que genere un pico')
    else:
        print (f'El pico en ventas lo produce el numero {Sample35}')
        
print (f'-' * 20)

# Consultar valores ✅ Consultar.

Capitales = {"Costa Rica": "San José", "México": "Ciudad de México", "Italia": "Roma",  "Argentina": "Buenos Aires", "España": "Madrid"}

Ubicado1 = Capitales.get('Italia')

if (Ubicado1 is None):
    print (f'Error, Italia no aparece en el diccionario')
else:
    print (f'La capital de Italia es {Ubicado1}')
    
print (f'-' * 20)

Productos1 = {"Laptop": 1200, "Mouse": 25, "Teclado": 45, "Monitor": 300}

def Ejercicio36(Diccionario, Articulo):
    if (len(Diccionario) == 0):
        return None
    else:
        Ubicado1 = Diccionario.get(Articulo)
        
        if (not Ubicado1):
            return False
        else:
            return True

Item1 = 'Escoba'

Sample36 = Ejercicio36(Productos1, Item1)

if (Sample36 is None):
    print (f'El diccionario esta vacio')
else:
    if (Sample36 == True):
        print (f'El articulo {Item1} aparece en el diccionario')
    else:
        print (f'Error, el articulo {Item1} no aparece en el diccionario')
        
print (f'-' * 20)

# Actualizar elementos ✅ Actualizar.

Productos2 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300
}

def Ejercicio37(Diccionario, Articulo, Precio):
    Ubicado1 = Diccionario.get(Articulo)
    
    if (Ubicado1 is None):
        return False
    else:
        Diccionario[Articulo] = Precio
        return True

Item2 = 'Escoba'
Item2_Price = 55

Sample37 = Ejercicio37(Productos2, Item2, Item2_Price)

if (len(Productos2) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample37 == True):
        print (f'Listo, el precio del articulo {Item2} fue actualizado exitosamente')
    else:
        print (f'Error, el articulo no existe en el diccionario, no se puede actualizar su precio')
        
print (f'-' * 20)

# Agregar elementos ✅ Agregar.

Productos3 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio38(Diccionario, Articulo, Precio):
    Ubicado1 = Diccionario.get(Articulo)
    
    if (Ubicado1 is None):
        Diccionario[Articulo] = Precio
        return True
    else:
        return False

Item3 = 'Monitor'
Item3_Price = 245

Sample38 = Ejercicio38(Productos3, Item3, Item3_Price)

if (not len(Productos3)):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample38 == True):
        print (f'El articulo {Item3} no existia en el inventario, fue agregado exitosamente!')
    else:
        print (f'Error, no podemos agregar este articulo al inventario porque ya existe')
        
print (f'-' * 20)

# Eliminar elementos ✅ Eliminar.

Productos4 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

Item4 = 'Mouse'

def Ejercicio39(Diccionario, Articulo):
    Ubicado1 = Diccionario.get(Articulo)
    
    if (Ubicado1 is None):
        return False
    else:
        del Diccionario[Articulo]
        return True

Sample39 = Ejercicio39(Productos4, Item4)

if (len(Productos4) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample39 == False):
        print (f'Error, no podemos eliminar este articulo, no existe en el inventario')
    else:
        print (f'El articulo {Item4} fue eliminado del inventario exitosamente!')
        
print (f'-' * 20)

Productos5 = {
    "Laptop": 100,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio40(Diccionario):
    Clave = next(iter(Diccionario))
    Valor = Diccionario[Clave]
    
    for indice, elemento in Diccionario.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    return Clave, Valor

Sample40 = Ejercicio40(Productos5)

if (not len(Productos5)):
    print (f'Error, el diccionario esta vacio')
else:
    Articulo, Precio = Sample40
    
    print (f'Nombre Articulo: {Articulo}')
    print (f'Precio Articulo: ${Precio}')
    
print (f'-' * 20)

Ventas = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio41(Diccionario, Numero):
    for Clave, Valor in Diccionario.items():
        if (Valor > Numero):
            return Clave, Valor
        else:
            continue
        
    return None

Limite4 = 300

Sample41 = Ejercicio41(Ventas, Limite4)

if (len(Ventas) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample41 is None):
        print (f'No hay ninguna venta en el diccionario que supere el limite ${Limite4}')
    else:
        Clave1, Valor1 = Sample41
        
        print (f'Dia Venta: {Clave1}')
        print (f'Dinero Vendido: ${Valor1}')
        
print (f'-' * 20)

Productos6 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}
    
def Ejercicio42(Diccionario, Numero):
    Acumulador = 0
    for _, valor in Diccionario.items():
        if (valor > Numero):
            Acumulador += 1
        else:
            continue
        
    return Acumulador

Limite5 = 20

Sample42 = Ejercicio42(Productos6, Limite5)

if (not len(Productos6)):
    print (f'Error, el diccionario esta vacio')
else:
    if (not Sample42):
        print (f'No hay ningun articulo cuyo precio sea mayor que ${Limite5}')
    else:
        print (f'La cantidad de articulos cuyo precio es mayor que ${Limite5} es {Sample42}')
        
print (f'-' * 20)

'''def Floating1(Numero):
    try:
        Numero1 = float(Numero)
        if (Numero1.is_integer()):
            print (f'Lo que ingresaste es un numero entero')
        else:
            print (f'Lo que ingresaste es un numero decimal')
    except (ValueError):
        print (f'Error, lo que ingresaste no es un numero')

Floating1(PEPE.Flotante1)

print (f'-' * 20)

Floating2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Floating2}')

def Floating3(Cadena):
    Cadena_Formateada = Cadena.replace(' ', '')
    if (isinstance(Cadena_Formateada, (str))):
        if (Cadena_Formateada.isalpha()):
            print (f'{Cadena} es un texto')
        else:
            print (f'Error, lo que ingresaste no es un texto')

Floating3(PEPE.Flotante3)

print (f'-' * 20)

def Floating4(Texto):
    Lista_Texto = Texto.split(' ')
    
    for indice, elemento in enumerate(Lista_Texto[0:None], start=1):
        print (f'El elemento en el indice {indice} es {elemento}')
        
    print (f'La cantidad de palabras digitadas es {len(Lista_Texto)}')

Floating4(PEPE.Flotante4)'''

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el alumno {elemento + 1}: ')
        Lista.append(Alumno)
        
    return Lista

print (f'La lista de estudiantes que visitaron el colegio hoy fue: {Colegio(Lista_Alumnos)}')'''

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
    
    print (f'El menos de los estudiantes es {Menore} y su edad es {Lista[0][1]} años')
    print (f'El mayor de los estudiantes es {Mayore} y su edad es {Lista[-1][1]} años')

Colegio(Lista_Alumnos)'''

Paises = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}

def Ejercicio43(Diccinario, Texto):
    Ubicado1 = Diccinario.get(Texto)
    
    if (Ubicado1 is None):
        return False
    else:
        return Ubicado1

Codigo = 'fr'

Sample43 = Ejercicio43(Paises, Codigo)

if (len(Paises) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample43 == False):
        print (f'Error, el codigo {Codigo} no pertenece a ningun pais registrado')
    else:
        print (f'El codigo {Codigo} pertenece a {Sample43}')
        
print (f'-' * 20)

# El except que se va a usar en este ejercicio es el except KeyError

'''def Ejercicio44(Diccionario):
    while (True):
        Codigo = input(f'Ingrese el codigo de un pais: ')
        Ubicado1 = Diccionario.get(Codigo)
        
        if (Codigo.lower() == 'salir'):
            print (f'Gracias por elegir nuestros servicios!')
            break
        else:
            if (Ubicado1 is None):
                print (f'Error, el codigo ingresado no pertenece a un pais del diccinario')
            else:
                print (f'El codigo {Codigo}, pertenece al pais {Ubicado1}')
                break

if (not len(Paises)):
    print (f'Error, el diccionario esta vacio')
else:
    Ejercicio44(Paises)'''
    
class Persona():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto1 = Persona('Erick Josue')

print (f'Hola, mi nombre es {Objeto1}')

print (f'-' * 20)

class Colores():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre
        
Lista_Colores = list([
    Colores('Rojo'),
    Colores('Azul'),
    Colores('Verde')
])

print (f'La lista de colores es {Lista_Colores}')

print (f'-' * 20)

class Inventario():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto2 = Inventario()

Objeto2.Productos.append('Borrador')
Objeto2.Productos.insert(1, 'Cuaderno')
Objeto2.Productos.extend(['Tajador'])

print (f'El inventario tiene {len(Objeto2)} productos')

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
        self.Ropa = [
            'Camiseta',
            'Pantalones',
            'Abrigo'
        ]
        
    def __getitem__(self, Indice):
        return self.Ropa[Indice]
        
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
            'Baguel'
        ]
        
    def __iter__(self):
        return iter(self.Panes)
        
Objeto8 = Panaderia()

for indice, elemento in enumerate(Objeto8, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

var5 = '3'

if (isinstance(var5, (int))):
    print (f'Esto es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var5.isnumeric()):
    print (f'Esto es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
try:
    Numerito1 = float(var5)
    if (Numerito1.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, esto no es un numero')
    
print (f'-' * 20)

var6 = 3.5

if (isinstance(var6, (float))):
    print (f'Esto es un numero decimal')
else:
    print (f'Error, esto no es un numero decimal')
    
try:
    Numerito2 = float(var6)
    if (Numerito2.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, esto no es un numero entero')
    
print (f'-' * 20)

var7 = 3.5

if (isinstance(var7, (int, float))):
    print (f'Lo que ingresaste es un numero entero o decimal')
else:
    print (f'Error de formato')
    
try:
    Numerito3 = float(var7)
    if (Numerito3.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, esto no es un numero')
    
print (f'-' * 20)

Ventas2 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def calcular_total_ventas(Diccionario):
    Acumulador = 0
    
    for elemento in Diccionario.values():
        Acumulador += elemento
        
    return Acumulador

Sample44 = calcular_total_ventas(Ventas2)

if (not len(Ventas2)):
    print (f'Error, el diccionario esta vacio')
else:
    print (f'La suma total de todas las ventas es {Sample44}')
    
print (f'-' * 20)

Ventas3 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def calcular_total_ventas_mayores(Diccionario, Numero):
    Acumulador = 0
    
    for elemento in Diccionario.values():
        if (elemento > Numero):
            Acumulador += elemento
        else:
            continue
        
    return Acumulador

Limite6 = 200

Sample45 = calcular_total_ventas_mayores(Ventas3, Limite6)

if (not len(Ventas3)):
    print (f'Error, el diccionario esta vacio')
else:
    if (not Sample45):
        print (f'Error, el numero de ventas superior al limite ${Limite6} es {Sample45}')
    else:
        print (f'La suma de las ventas superiores al limite ${Limite6} es ${Sample45}') 
        
print (f'-' * 20)

'''Dict_Personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}

def Ejercicio46(Diccionario):
    for clave, valor in Diccionario.items():
        with open (f'C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
            Documento_SobreEscribir = Docu.write(f'{clave.lower()} : {valor}\n')
            Docu.close()

Sample46 = Ejercicio46(Dict_Personas)

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()'''
    
import re

Texto1 = "   Hola!!!   mundo@@   123   "

print (f'{Texto1}')

Texto1_Version1 = Texto1.strip()

print (f'{Texto1_Version1}')

Texto1_Version2 = ' '.join(Texto1_Version1.split())

print (f'{Texto1_Version2}')

Texto1_Version3 = re.sub(r'\!|\@|\d+', '', Texto1_Version2)

print (f'{Texto1_Version3}')

Texto1_Version4 = Texto1_Version3.title()

print (f'{Texto1_Version4}')

Texto1_Version5 = Texto1_Version4.lower()

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
    print (f'Genial! hemos encontrado ventas en esta fecha')
    
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Min} vendio un total de {Grupo1_Min_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada} el producto {Grupo1_Max} vendio un total de {Grupo1_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que nos compraron hoy fue {Grupo1.count()}')
    
    print (f'La cantidad de productos vendidos hoy fue {Grupo1.sum()}')
    
    print (f'El promedio de productos vendidos hoy fue {round(Grupo1.mean(), 2)}')
    
    Grupo2 = Encontrado1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido hoy fue ${Grupo2.sum()}')
    
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
print (f'{Diccionario_Csv1["Key_4"]}')
print (f'{Diccionario_Csv1.get("Key_6")}')

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

# Formato 1

Pattern2 = r'\!|\?|\.{2,}|\d{2,4}\-[0-9]{3,}'

Buscar2 = re.sub(Pattern2, '', Texto3)

print (f'{Buscar2}')

print (f'-' * 20)

# Formato 2

Pattern3 = r'[^a-zA-Z0-9\s]+'

Buscar3 = re.sub(Pattern3, '', Texto3)

print (f'{Buscar3}')

print (f'-' * 20)

# Formato 3

Pattern4 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos1 = re.findall(Pattern4, Texto3)

print (f'{Correos1}')

Texto3_Temp1 = Texto3

for i, email in enumerate(Correos1, start=1):
    Texto3_Temp1 = Texto3_Temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto3_Temp1}')

Texto3_Temp2 = re.sub(r'\!|\?|\.{2,}|\d{2,4}\-[0-9]{4,}', '', Texto3_Temp1)

print (f'{Texto3_Temp2}')

for i, email in enumerate(Correos1, start=1):
    Texto3_Temp2 = Texto3_Temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto3_Temp2}')

print (f'-' * 20)

import re

Texto4 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Pattern5 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Correos2 = re.findall(Pattern5, Texto4)

print (f'{Correos2}')

Texto4_Temp1 = Texto4

for i, email in enumerate(Correos2, start=1):
    Texto4_Temp1 = Texto4_Temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto4_Temp1}')

Pattern6 = r'\!|\?'

Texto4_Temp2 = re.sub(Pattern6, '', Texto4_Temp1)

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
                Lista_Promedios.extend([Numerito5])
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador += 1
    
Promedio2 = sum(Lista_Promedios) / Lista_Promedios.__len__()

print (f'El promedio de las notas ingresadas es {round(Promedio2, 2)}')'''

print (f'-' * 20)

Lista_Nombres1 = ['erick perez', 'josue gutierrez', 'jacqueline hidalgo']
Lista_Nombres1_Actualizada = list([])

for elemento in Lista_Nombres1:
    Lista_Nombres1_Actualizada.append(elemento.title())
    
print (f'{Lista_Nombres1}')
print (f'{Lista_Nombres1_Actualizada}')

print (f'-' * 20)

import re

Texto5 = 'esto 12 es un hola ejemplo cuealquiera 9 VAMOS a hila ver si el texto 877 @ al fin hela funciona o no'

Buscar4 = re.search(r'si', Texto5)

print (f'{Buscar4}')

Buscar6 = re.findall(r'\d+', Texto5)

print (f'{Buscar6}')

Buscar7 = bool(re.fullmatch(r'esto 12 es un hola ejemplo cualquiera 9 VAMOS a hila ver si el texto 877 \@ al fin hela funciona o no', Texto5))

if (Buscar7 == True):
    print (f'Ambos texto son identicos')
else:
    print (f'Error, los textos no son iguales')
    
Buscar8 = re.findall(r'h.la', Texto5)

print (f'{Buscar8}')

'''
{2}
{2,4}
{2,}
? esto es cero o uno
* esto es cero o mas 
+ esto es uno o mas

\D esto es todo menos numeros
\d esto es numeros nada mas
\W esto es caracteres especiales nada mas
\w esto es todo menos caracteres especiales
\s esto es unicamente espacios
\S esto es todo menos espacios
'''

Buscar5 = bool(re.search(r'^e', Texto5))

if (Buscar5 == True):
    print (f'La cadena comienza con la letra e')
else:
    print (f'Error, la cadena no comienza con esa letra')
    
Buscar6 = bool(re.search(r'no$', Texto5))

if (Buscar6 == True):
    print (f'La cadena termina con la palabra no')
else:
    print (f'Error, la cadena no termina con esa palabra')

Buscar9 = re.findall(r'\d{3,}\s{1}\W{1,}', Texto5)

print (f'{Buscar9}')

Buscar10 = re.findall(r'[ae]{2,4}', Texto5)

print (f'{Buscar10}')

Buscar11 = re.findall(r'[ae]*', Texto5)

print (f'{Buscar11}')

Buscar12 = re.findall(r'hola|\d{2,4}', Texto5)

print (f'{Buscar12}')

print (f'-' * 20)

import re

Texto6 = 'ericksuper80@hotmail.com'

Pattern7 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}$'

Buscar13 = bool(re.fullmatch(Pattern7, Texto6))

if (Buscar13 == True):
    print (f'El correo electronico tiene un formato correcto')
else:
    print (f'Error, el formato del correo electronico es incorrecto')
    
print (f'-' * 20)

Pattern8 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.(?:com|net|org)$'

Buscar14 = bool(re.match(Pattern8, Texto6))

if (Buscar14 == True):
    print (f'El correo electronico 2 tiene un formato correcto')
else:
    print (f'Error, el formato del correo electronico 2 es incorrecto')
    
print (f'-' * 20)

import re

Texto7 = '32'

Pattern9 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar15 = bool(re.fullmatch(Pattern9, Texto7))

if (Buscar15 == True):
    print (f'El numero {Texto7} se encuentra entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

import re

Texto8 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern10 = r'\d{2,4}\/[0-9]{2,}\/\d{4}'

Replacement10 = 'XX/XX/XXXX'

Buscar16 = re.sub(Pattern10, Replacement10, Texto8)

print (f'{Buscar16}')

print (f'-' * 20)

Pattern11 = r'\+\d{1}\-[0-9]{2,3}\-\d{3,}\-[0-9]{4,10}'

Replacement11 = '+PHON3-NUMB3R'

Buscar17 = re.sub(Pattern11, Replacement11, Buscar16)

print (f'{Buscar17}')

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

Pattern12 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar18 = re.findall(Pattern12, Texto9)

print (f'{Buscar18}')

for elemento in Buscar18:
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

Pattern13 = r'\!|\?|\.{2,}|\d{2,4}\-[0-9]{3,}'

Buscar19 = re.sub(Pattern13, '', Texto10)

print (f'{Buscar19}')

print (f'-' * 20)

# Version2

import re

Pattern14 = r'[^a-zA-Z0-9\s(\d{4,})]+'

Buscar20 = re.sub(Pattern14, '', Texto10)

print (f'{Buscar20}')

print (f'-' * 20)

var8 = 3.5

if (isinstance(var8, (float))):
    print (f'Lo que se ingreso es un numero decimal')
else:
    print (f'Error, esto no es un numero decimal')
    
try:
    Numerito4 = float(var8)
    if (Numerito4.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
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
except ValueError:
    print (f'Error, lo que se ingreso no es un numero')
    
print (f'-' * 20)

import re

Texto11 = "   Hola!!!   mundo@@   123   "

print (f'{Texto11}')

Texto11_Version1 = Texto11.strip()

print (f'{Texto11_Version1}')

Texto11_Version2 = ' '.join(Texto11_Version1.split())

print (f'{Texto11_Version2}')

Texto11_Version3 = re.sub(r'\!|\@|\d+', '', Texto11_Version2)

print (f'{Texto11_Version3}')

Texto11_Version4 = Texto11_Version3.lower()

print (f'{Texto11_Version4}')

Texto11_Version5 = Texto11_Version4.title()

print (f'{Texto11_Version5}')

print (f'-' * 20)

try:
    print (f'{12 + "6"}') #type: ignore
except TypeError:
    print (f'Error, los tipos de datos son incorrectos')
    
print (f'-' * 20)

Lista_ValueError = list(['Erick', 'Josue', 'Karlita'])

try:
    Lista_ValueError.remove('Carmelo')
except ValueError:
    print (f'Error, el valor no existe en la lista')
    
print (f'-' * 20)

try:
    ValueError1, ValueError2 = Lista_ValueError
except ValueError:
    print (f'Error, la cantidad de variables es incorrecta')
    
print (f'-' * 20)

try:
    Variable_ValueError = int('Hola')
except ValueError:
    print (f'Error, el tipo es correcto, un str si puede volverse int pero no Hola')
    
print (f'-' * 20)

try:
    Lista_ValueError.index('Carmelo')
except ValueError:
    print (f'Error, Carmelo no existe en la lista')
    
print (f'-' * 20)

try:
    print (f'{4 + '5'}') #type: ignore
except Exception:
    print (f'Error, los tipos son incorrectos para esta operacion, usando comoding')
    
print (f'-' * 20)

try:
    del Lista_ValueError[3]
except IndexError as Errore1:
    print (f'Error, ese indice no existe -> {Errore1}')
    
print (f'-' * 20)

try:
    Resultado1 = 4 / Lista_ValueError.index("Carmelo")  # type: ignore
except ValueError:
    print(f'Error, Carmelo no existe en la lista')
except ZeroDivisionError:
    print(f'Error, el divisor no puede ser cero')
except IndexError:
    print(f'Error, el índice es incorrecto')
except Exception:
    print(f'Error genérico, los valores no pueden sumarse')
    
print (f'-' * 20)

var10 = '3'

try:
    if (isinstance(var10, (str))):
        if (var10.isalpha()):
            print (f'{var10} - Esto es un texto')
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
    except ValueError:
        print (f'Error, lo que ingresaste no es un numero')

Exception1('hola')

print (f'-' * 20)

def Exception2(Num1, Num2):
    try:
        Resultado = Num1 + Num2
        print (f'El resultado de la operacion es {Resultado}')
    except (ValueError, TypeError, Exception):
        print (f'Error, ambos elementos deben ser numeros para realizar la operacion')

Exception2(12, 'hola')

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        Resultado = Num1 / Num2
        
        print (f'El resultado de la division es {round(Resultado, 2)}')
    except ZeroDivisionError as Errore2:
        print (f'Error, el divisor no puede ser cero -> {Errore2}')

Exception3(12, 0)

print (f'-' * 20)

Lista_ValueError2 = list(['Erick', 'Josue', 'Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento con indice {Indice} es {Lista_ValueError2[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(3)

print (f'-' * 20)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Clave):
    try:
        print (f'El elemento con clave {Clave} es {Diccionario_Exception5[Clave]}')
    except KeyError:
        print (f'Error, la clave seleccionada no existe')

Exception5("Votante")

print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Leon')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo seleccionado no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()
    
print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nCamaleon'])
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nLobo')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nGato Pequeño', f'\nGato Mediano', f'\nGato Grande'])
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

# Aqui vamos a realizar operaciones sobre los elementos del txt

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    
    Lista_Txt = Documento_Lineas

for elemento in Lista_Txt[:]:
    if (elemento.strip() == 'Vaporeon'):
        print (f'Correcto, este poke es de agua')
        break
    else:
        continue
    
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

print (f'{Data_Frame_Concatenate}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate_Age}')

print (f'-' * 20)

print (f'El menor de los miembros del dataframe es {Data_Frame_Concatenate_Age.min()}')
print (f'El mayor de los miembros del dataframe es {Data_Frame_Concatenate_Age.max()}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Unidad1 = elemento['Nombre']
    Unidad2 = elemento['Edad']
    
    print (f'Hola, mi nombre es {Unidad1} y mi edad es {Unidad2} años')
    
Data_Frame_Concatenate['TOTALITO'] = Data_Frame_Concatenate['Edad'] * 100
    
print (f'-' * 20)

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()
Grupo3_Min_Cant = Grupo3.min()
Grupo3_Max_Cant = Grupo3.max()

print (f'El menor de los miembros del dataframe es {Grupo3_Min} y su edad es {Grupo3_Min_Cant} años')
print (f'El mayor de los miembros del dataframe es {Grupo3_Max} y su edad es {Grupo3_Max_Cant} años')

print (f'La cantidad de personas en el dataframe es {Grupo3.count()}')

print (f'La suma de todas las edades es {Grupo3.sum()}')

print (f'El promedio de la suma de las edades es {round(Grupo3.mean(), 2)}')

Grupo4 = Data_Frame_Concatenate.groupby('Nombre')['TOTALITO'].sum()

print (f'La suma de todas las nuevas edades es {Grupo4.sum()}')

print (f'El promedio de la suma de las nuevas edades es {round(Grupo4.mean(), 2)}')

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

print (f'El numero de Filas es {Filas}')
print (f'El numero de Columnas es {Columnas}')

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

print (f'{Cargar_Excel.head()}')

print (f'-' * 20)

Grupo5 = Cargar_Excel.groupby('nombre')['edad'].sum()
Grupo5_Min = Grupo5.idxmin()
Grupo5_Max = Grupo5.idxmax()
Grupo5_Min_Cant = Grupo5.min()
Grupo5_Max_Cant = Grupo5.max()

print (f'Del excel el menor es {Grupo5_Min} y su edad es {Grupo5_Min_Cant} años')
print (f'Del excel el menor es {Grupo5_Max} y su edad es {Grupo5_Max_Cant} años')

print (f'El excel tiene {Grupo5.count()} personas')

print (f'La suma de todas las edades es {Grupo5.sum()}')

print (f'La media de las edades es {round(Grupo5.mean(), 2)} años')

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

print (f'{Cargar_Excel3_Sorted.head()}')

print (f'-' * 20)

Cargar_Excel3_Sorted_Descending = Cargar_Excel3_Sorted.sort_values(by='cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending.head()}')

print (f'-' * 20)

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt.head()}')

print (f'-' * 20)

print (f'{Cargar_Txt}')

print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    Lista_Txt2 = Documento_Lineas
    
Contador = 0

while (Contador < len(Lista_Txt2)):
    print (f'El elemento en la posicion {Contador + 1} es {Lista_Txt2[Contador].strip()}')
    Contador += 1
    
print (f'-' * 20)

import pandas as pd

Ruta_Csv2 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

print (f'-' * 20)

Lista_Csv2 = list(Cargar_Csv2['Nombre'])
Key2 = [f'Key{i}' for i in range(len(Lista_Csv2))]

print (f'{Lista_Csv2}')
print (f'{Key2}')

Diccionario_Csv2 = dict(zip(Key2, Lista_Csv2))

print (f'{Diccionario_Csv2}')
print (f'{Diccionario_Csv2.keys()}')
print (f'{Diccionario_Csv2.values()}')
print (f'{Diccionario_Csv2.items()}')
print (f'{Diccionario_Csv2["Key0"]}')
print (f'{Diccionario_Csv2.get("Key1")}')

print (f'-' * 20)

print (f'{Cargar_Csv2}')

print (f'-' * 20)

Grupo6 = Cargar_Csv2.groupby('Nombre')['Edad'].sum()
Grupo6_Min = Grupo6.idxmin()
Grupo6_Max = Grupo6.idxmax()
Grupo6_Min_Cant = Grupo6.min()
Grupo6_Max_Cant = Grupo6.max()

print (f'El menor de los miembros del CSV file es {Grupo6_Min} y su edad es {Grupo6_Min_Cant} años')
print (f'El mayor de los miembros del CSV file es {Grupo6_Max} y su edad es {Grupo6_Max_Cant} años')

print (f'El csv tiene {Grupo6.count()} personas')

print (f'La suma de las edades del csv es {Grupo6.sum()}')

print (f'La media de las edades del csv es {round(Grupo6.mean(), 2)} años')

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
print (f'{Array0[1][::2]}')
print (f'{Array0[2][::3]}')
print (f'{Array0[0][:2]}')
print (f'{Array0[0][2:]}')
print (f'{Array0[:][2]}')
print (f'{Array0[1][2:3]}')
print (f'{Array0[2][0:None]}')
print (f'{Array0[2][:]}')

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
print (f'{Array2[1, 2]}')

print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[:, 2]}')
print (f'{Array2[0, 2:3]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 >= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'\nAcomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[1, 0:None])
Sumita4 = np.sum(Array2_Sorted[1, :])

print (f'Sumita: {Sumita1}')
print (f'Sumita: {Sumita2}')
print (f'Sumita: {Sumita3}')
print (f'Sumita: {Sumita4}')

print (f'-' * 20)

Array3 = np.array([[['a', 'b', 'c'], ['e', 'f', 'g']],     [['h', 'i', 'j'], ['k', 'l', 'm']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 2]}')

print (f'{Array3[1, 0, ::2]}')
print (f'{Array3[0, 1, ::3]}')
print (f'{Array3[1, 1, :2]}')
print (f'{Array3[1, 1, 2:]}')
print (f'{Array3[0, :, 1]}')
print (f'{Array3[0, 1, 2:3]}')
print (f'{Array3[1, 0, 0:None]}')
print (f'{Array3[1, 0, :]}')
print (f'{Array3[Array3 == "i"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],           [[[6, 5, 4], [9, 8, 7]], [[0, 9, 1], [6, 2, 3]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 0]}')

print (f'{Array4[1, 0, 1, ::2]}')
print (f'{Array4[1, 0, 0, ::3]}')
print (f'{Array4[0, 1, 1, :2]}')
print (f'{Array4[0, 1, 1, 2:]}')
print (f'{Array4[1, 1, :, 2]}')
print (f'{Array4[0, 0, 1, 2:3]}')
print (f'{Array4[1, 0, 0, 0:None]}')
print (f'{Array4[1, 0, 0, :]}')
print (f'{Array4[Array4 >= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

Sumita1 = np.sum(Array4_Sorted, axis=0)
Sumita2 = np.sum(Array4_Sorted, axis=1)
Sumita3 = np.sum(Array4_Sorted[1, 0, 1, 0:None])
Sumita4 = np.sum(Array4_Sorted[1, 0, 1, :])

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

print (f'Sumita: {Sumita1}')
print (f'Sumita: {Sumita2}')
print (f'Sumita: {Sumita3}')
print (f'Sumita: {Sumita4}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1) #type: ignore

print (f'{Array_Num1}')

Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El numero menor del array es {Array_Num1_Min}')
print (f'El numero mayor del array es {Array_Num1_Max}')

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

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 0]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value=f'{PEPE.Diccionario_Poke["Poke2"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[0, 2]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(10), fill_value=f'Fuecoco')

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[8]}')

Lista_Array1 = []

for elemento in Array_Gen2:
    Lista_Array1.append(str(elemento))
    
print (f'{type(Array_Gen2)}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Num3 = np.full(shape=(2, 3), fill_value=Array4[1, 0, 1, 2])

print (f'{Array_Num3}')
print (f'{Array_Num3.ndim}')
print (f'{Array_Num3.shape}')
print (f'{Array_Num3.size}')
print (f'{Array_Num3.dtype}')
print (f'{Array_Num3[1, 1]}')

print (f'-' * 20)

Tupla_Array = tuple(('Uno', 'Dos', 'Tres',))
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen3 = np.full(shape=(2, 3), fill_value=Tupla_Array)
Array_Gen4 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen5 = np.full(shape=(4, 1), fill_value=Diccionario_Array['Nombre'][1])

print (f'{Array_Gen3}')
print (f'{Array_Gen4}')
print (f'{Array_Gen5}')

print (f'-' * 20)

print (f'{Array_Gen5[2]}')

print (f'-' * 20)

Array_Num4 = np.arange(start=1, stop=6, step=1) #type: ignore
Array_Num5 = np.arange(start=2, stop=11, step=2) #type: ignore
Array_Num6 = np.arange(start=3, stop=31, step=3) #type: ignore
Array_Num7 = np.arange(start=10, stop=21, step=2) #type: ignore
Array_Num8 = np.arange(10) #type: ignore

print (f'{Array_Num4}')
print (f'{Array_Num5}')
print (f'{Array_Num6}')
print (f'{Array_Num7}')
print (f'{Array_Num8}')

print (f'-' * 20)

Array_Random1 = np.random.randint(low=1, high=10, size=(10))

print (f'{Array_Random1}')

print (f'-' * 20)

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Acomodado: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Acomodado: {Array_Random2_Sorted_Sum}')

print (f'-' * 20)

Matriz1 = np.array([8, 9, 14])
Matriz2 = np.array([2, 3, 7])

Suma = Matriz1 + Matriz2
Resta = Matriz1 / Matriz2
Multiplicacion = Matriz1 * Matriz2
Division = Matriz1 / Matriz2
Array_Random1_Cien = Array_Random1 + 100

print (f'El resultado de la operacion es {Suma}')
print (f'El resultado de la operacion es {Resta}')
print (f'El resultado de la operacion es {Multiplicacion}')
print (f'El resultado de la operacion es {Division}')
print (f'El resultado de la operacion es {Array_Random1_Cien}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=20)

print (f'{Array_Random3}')

Array_Random3_Reshape = np.reshape(Array_Random3, shape=(4, 5))

print (f'{Array_Random3_Reshape}')

Array_Random3_Reshape_Column_Min = np.min(Array_Random3_Reshape, axis=0)
Array_Random3_Reshape_Column_Max = np.max(Array_Random3_Reshape, axis=0)
Array_Random3_Reshape_Row_Min = np.min(Array_Random3_Reshape, axis=1)
Array_Random3_Reshape_Row_Max = np.max(Array_Random3_Reshape, axis=1)

print (f'Los menores de las columnas son {Array_Random3_Reshape_Column_Min}')
print (f'Los menores de las columnas son {Array_Random3_Reshape_Column_Max}')
print (f'Los menores de las columnas son {Array_Random3_Reshape_Row_Min}')
print (f'Los menores de las columnas son {Array_Random3_Reshape_Row_Max}')

print (f'-' * 20)

Lista_Array2 = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

Array5 = np.array(Lista_Array2)

print (f'{Lista_Array2}')
print (f'{type(Lista_Array2)}')
print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-' * 20)

Array_Random3_Reshape_Ravel = np.ravel(Array_Random3_Reshape)

print (f'{Array_Random3_Reshape_Ravel}')

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

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            for Elemento in Fila:
                print (f'{Elemento}')

print (f'-' * 20)

for Matriz1 in Array3:
    for Fila in Matriz1:
        print (f'{Fila}')

print (f'-' * 20)

Array_Random4 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random4}')

Array_Random4_Sum1 = np.sum(Array_Random4, axis=0)
Array_Random4_Sum2 = np.sum(Array_Random4, axis=1)

print (f'Sumatoria es {Array_Random4_Sum1}')
print (f'Sumatoria es {Array_Random4_Sum2}')

print (f'-' * 20)

Lista_Sorteo1 = list(['Erick', 'Josue', 'Karlita'])
Lista_Sorteo2 = ['Carmelo', 'Susanita', 'Roxana']

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

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Leer_Txt3 = Documento_Lineas = Docu.readlines()
        for indice, elemento in enumerate(Leer_Txt3[:], start=1):
            print (f'{indice} : {elemento.strip()}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
print (f'-' * 20)

personas = {
    'Juan' : 20,
    'Romina' : 32,
    'Tamara' : 25,
    'Melannie' : 19
}

with open ('C:\\Repo\\personas.txt', 'a', encoding='UTF-8') as Docu:
    for clave, valor in personas.items():
        Documento_Agregar = Docu.write(f'{clave.lower()} - {valor}\n')
    
try:
    with open ('C:\\Repo\\personas.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Leer = Docu.read()
        print (f'{Documento_Leer}')
        Docu.close()
except FileNotFoundError:
    print (f'Error el archivo no existe')
    
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
    print (f'El experimento termina aqui')
    
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
    print (f'El experimento termina aqui')
    
print (f'-' * 20)

def Generadora3():
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

Gen3 = Generadora3()

try:
    print (f'{next(Gen3)}')
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

print (f'{help(PEPE.Saludar3)}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 7)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int) -> int:
        return Num1 + Num2
    
    return Sumatoria_Interna(4)

Variable_Sumatoria = Sumatoria_Externa(3)

print (f'El resultado de la sumatoria es {Variable_Sumatoria}')

Lista_Funcion_Valor_Superior = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Suma_Superior(Lista):
    Resultado = 0
    
    for elemento in Lista:
        Resultado += elemento
        
    return Resultado

def Mul_Superior(Lista):
    Resultado = 0
    
    for elemento in Lista:
        Resultado *= elemento
        
    return Resultado

def Nivel_Superior1(Funcion, Lista):
    return Funcion(Lista)

print (f'El resultado de la sumatoria es {Nivel_Superior1(Suma_Superior, Lista_Funcion_Valor_Superior)}')
print (f'El resultado de la multiplicacion es {Nivel_Superior1(Mul_Superior, Lista_Funcion_Valor_Superior)}')

print (f'-' * 20)

if (PEPE.Par(Variable_Sumatoria) == True):
    print (f'Lo que ingresaste es un numero par')
else:
    print (f'Lo que ingresaste es un numero impar')
    
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
    
print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(36)}')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Docu.readlines()
        print (f'{Documento_Lineas}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
def Funcion_Tupla(*args):
    return args
    
Variable_Funcion_Tupla = Funcion_Tupla(3.5, 300, 'Koala', True)

print (f'{Funcion_Tupla(3.5, 300, 'Koala', True)}')
print (f'{Variable_Funcion_Tupla[2]}')
print (f'{Funcion_Tupla(3.5, 300, 'Koala', True)[3]}')
print (f'{type(Funcion_Tupla(3.5, 300, 'Koala', True))}')

print (f'-' * 20)

def Funcion_Tupla2(*args):
    for elemento in args:
        print (f'{elemento}')
        
Funcion_Tupla2(
    3.5, 300, 'Koala', not False
)

print (f'-' * 20)

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs:
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    for elemento in kwargs.keys():
        print (f'{elemento}')
        
    print (f'-' * 20)
        
    for elemento in kwargs.values():
        print (f'{elemento}')
            
    print (f'-' * 20)
        
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')
        
Funcion_Diccionario(
    Nombre='Erick',
    Edad=37,
    Votante=True
)

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6 ,7, 8, 9, 10)}')

def Sumatoria_Dos(Nombre='Erick', *args):
    return f'Mi nombre es {Nombre} y mi numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos('Karlita', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

if (PEPE.Any_Par == True):
    print (f'Los numeros pares de la lista son {PEPE.Lista_Par}')
    print (f'Los numeros pares de la lista son {list(Anonima3)}')
else:
    print (f'Error, no hay numeros pares en la lista')
    
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

print (f'-' * 20)

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

print (f'-' * 20)

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    if (Any_Impar == True):
        Anonima = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impar = [num for num in Lista if num % 2 != 0]
        
        print (f'Los numeros impares de la lista son {list(Anonima)}')
        print (f'Los numeros impares de la lista son {Lista_Impar}')
    else:
        print (f'Error, no hay numeros impares en la lista')

Filtrador(PEPE.Lista_Numeros)

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'>>> ANTES')
        Segunda()
        print (f'DESPUES <<<')
        
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
    '''Esto es un docstring que explica lo que hace esta funcion'''
    return Num1 + Num2

print (f'El resultado de la operacion es {Sumatoria3(12, 7)}')

print (f'{help(Sumatoria3)}')

print (f'-' * 20)

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'John'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)
        
    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    return f'Mi nombre es {Nombre} {Apellido}'

print (f'{Usuario2("Erick", "Perez")}')

print (f'-' * 20)

from Module_Own import Pokemon as Poke1

Objeto9 = Poke1(PEPE.Diccionario_Poke["Poke1"], 'Electrico', 'Impact Trueno')
Objeto10 = Poke1(PEPE.Diccionario_Poke["Poke2"], 'Roca', 'Sismo')

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
        
Objeto11 = Poke_Kid1(PEPE.Diccionario_Poke["Poke3"], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto11)
Objeto11.Mostrar()

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
    def __init__(self, Nombre, Peso, Edad):
        self.Nombre = Nombre
        self.Peso = Peso
        self.Edad = Edad

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Peso: {self.Peso}kgs')
        print (f'Edad: {self.Edad} años')
        
class Perro(Veterinaria):
    def __init__(self, Nombre, Peso, Edad, Raza, Padecimiento):
        super().__init__(Nombre, Peso, Edad)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        
    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        
Objeto13 = Perro('Chester', 2.8, 5, 'Poodle', 'Hipertension')

Veterinaria.Mostrar(Objeto13)
Objeto13.Mostrar()

print (f'-' * 20)

class Gato(Veterinaria):
    def __init__(self, Nombre, Peso, Edad, Color, Paciente):
        super().__init__(Nombre, Peso, Edad)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto14 = Gato('Messi', 1.8, 1.5, 'Gris', 'No')

Veterinaria.Mostrar(Objeto14)
Objeto14.Mostrar()

print (f'-' * 20)

class Pajaro(Veterinaria):
    def __init__(self, Nombre, Peso, Edad, Especie, Habla):
        super().__init__(Nombre, Peso, Edad)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto15 = Pajaro('Polly', 0.4, 31, 'Guacamaya', 'Si')

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

print (f'{Hija_Padre}')

Instancia1 = isinstance(Objeto16, Atacante)
Instancia2 = isinstance(Objeto16, Defensor)
Instancia3 = isinstance(Objeto16, Paladin)

print (f'{Instancia1}')
print (f'{Instancia2}')
print (f'{Instancia3}')

print (f'-' * 20)

class A1():
    def Mostrar(self):
        print (f'Hola como estas A1?')
        
class E1():
    def Mostrar(self):
        print (f'Hola como estas E1?')
        
class B1(E1):
    def Mostrar(self):
        print (f'Hola como estas B1?')
        
class C1(A1):
    def Mostrar(self):
        print (f'Hola como estas C1?')
        
class D1(B1, C1):
    def Mostrar(self):
        print (f'Hola como estas D1?')
        
Objeto17 = D1()

A1.Mostrar(Objeto17)
B1.Mostrar(Objeto17)
C1.Mostrar(Objeto17)
Objeto17.Mostrar()
E1.Mostrar(Objeto17)

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
        print (f'Su saldo a la fecha es de ${self.__Saldo}')
        
Objeto21 = Cuenta_Bancaria(100)
Objeto21.Depositar(25)
Objeto21.Mostrar()

print (f'Su saldo privado es de {Objeto21.Dinero}, esto no deberia de compartirse')

Objeto21.Dinero = '15,000,000'

Objeto21.Mostrar()

print (f'Su saldo privado es de {Objeto21.Dinero}, esto no deberia de compartirse')

class Automovil():
    def __init__(self, marca, modelo, velocidad_maxima):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = 0
        self.__velocidad_maxima = velocidad_maxima
        
    # Métodos
    def acelerar(self, kms_h):
        if kms_h >= 0:
            velocidad_aux = self.__velocidad + kms_h
            if velocidad_aux <= self.__velocidad_maxima:
                self.__velocidad = velocidad_aux
            else:
                self.__velocidad = self.__velocidad_maxima

    # get / set
    def get_velocidad(self):
        return self.__velocidad
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def set_color(self, color):
        self.__color = color

class Persona():
    
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__appellido = apellido


auto_01 = Automovil('Ford', 'Ka', 170)
auto_02 = Automovil('Jeep', 'Renegade', 190)
print(auto_01.get_velocidad())
auto_01.acelerar(50)
print(auto_01.get_velocidad())
auto_01.acelerar(100)
print(auto_01.get_velocidad())
auto_01.acelerar(130)
print(auto_01.get_velocidad())
auto_01.acelerar(45651655450)
print(auto_01.get_velocidad())
cliente_a = Persona('Sofía', 'Prida')

auto_01.set_color('Amarillo')

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
        
Objeto22 = Pastel1()

Objeto22.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Ingrediente1 = Chocolate()
Objeto23 = Pastel2(Ingrediente1)
Objeto23.Hornear()

Ingrediente2 = Vainilla()
Objeto24 = Pastel2(Ingrediente2)
Objeto24.Hornear()

Ingrediente3 = Fresa()
Objeto25 = Pastel2(Ingrediente3)
Objeto25.Hornear()

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla(Plantilla):
    def Mostrar(self):
        print (f'Este metodo es de la sub plantilla')
        
    def General(self):
        print (f'Obligados a usar este metodo')
        
Objeto24 = Sub_Plantilla()

Objeto24.Mostrar()
Objeto24.General()

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
    
class Batalla1():
    def __init__(self):
        self.Favorito = Bulbasaur()
        
    def Batallar(self):
        print (f'El lider de gimnasio ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Objeto26 = Batalla1()

Objeto26.Batallar()

print (f'-' * 20)

class Batalla2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El lider del gimnasio ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Criatura1 = Bulbasaur()
Objeto27 = Batalla2(Criatura1)
Objeto27.Batallar()

Criatura2 = Treekoo()
Objeto28 = Batalla2(Criatura2)
Objeto28.Batallar()

Criatura3 = Chikorita()
Objeto29 = Batalla2(Criatura3)
Objeto29.Batallar()

print (f'-' * 20)

class Persona1():
    def __init__(self, Edad):
        self.Edad = Edad
        
    @property
    def Mostrar(self):
        return self.Edad

Objeto30 = Persona1(26)

print (f'Mi edad es {Objeto30.Mostrar}')

print (f'-' * 20)

x = 10

x += 5

print (f'El resultado de la operacion es {x}')

print (f'-' * 20)

x = 10

x -= 5

print (f'El resultado de la operacion es {x}')

print (f'-' * 20)

x = 10

x *= 5

print (f'El resultado de la operacion es {x}')

print (f'-' * 20)

x = 10

x /= 5

print (f'El resultado de la operacion es {x}')

print (f'-' * 20)

x = 10

x **= 5

print (f'El resultado de la operacion es {x}')

print (f'-' * 20)

x = 10

x %= 6

print (f'El resultado de la operacion es {x}')

print (f'-' * 20)

x = 10

x //= 5

print (f'El resultado de la operacion es {x}')

print (f'-' * 20)

for elemento in range(Limite:=5):
    print (f'El elemento es {elemento}')
    
print (f'-' * 20)

print (Nombre:= "Erick Perez")

print (f'Hola mi nombre es {(Nombre:="Carmelito Alvarez")}')

Contador = 0

while (Contador < len(Lista_Walrus:=[1, 2, 3, 4, 5])):
    print (f'El elemento es {Lista_Walrus[Contador]}')
    Contador += 1
    
print (f'-' * 20)
    
Productos7 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def calcular_productos_mayores(Diccionario, Num):
    Contador = 0
    Acumulador = 0
    for Valor in Diccionario.values():
        if (Valor > Num):
            Contador += 1
            Acumulador += Valor
            
    return Contador, Acumulador

Limite7 = 2000

Sample46 = calcular_productos_mayores(Productos7, Limite7)

if (len(Productos7) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Contador2, Acumulador2 = Sample46
    if (Contador2 == 0):
        print (f'Cantidad -> {Contador2}')
        print (f'Total -> {Acumulador2}')
    else:
        print (f'Cantidad -> {Contador2}')
        print (f'Total -> {Acumulador2}')
        
print (f'-' * 20)

Productos8 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def buscar_primer_producto_mayor(Diccionario, Num):
    Diccionario_Sorted = dict(sorted(Diccionario.items(), key=lambda item: item[1]))
    
    for Clave, Valor in Diccionario_Sorted.items():
        if (Valor > Num):
            return Clave, Valor
        
    return None

Limite8 = 200

Sample47 = buscar_primer_producto_mayor(Productos8, Limite8)

if (len(Productos8) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample47 is None):
        print (f'No se encontro ningun articulo cuyo precio super el limite ${Limite8}')
    else:
        Clave2, Valor2 = Sample47
        print (f'Nombre Producto: {Clave2}')
        print (f'Precio Producto: ${Valor2}')
        
print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''
Esto
Es
Un
Long
String'''

variable4 = Objeto10.Cantidad

variable5 = PEPE.Division_Flotante

variable6, variable7 = True, Objeto11.Catched

# Esto es un comentario simple

'''
Esto es un docstring
O
Tambien
Un
Comentario
Compuesto
'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke2"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene actualmente {Sumatoria2(1, 2, 3, 4, 5)}, {Anonima2(Variable_Sumatoria)} o incluso {Objeto9.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Erick' in Lista_Uno)
print (f'{PEPE.Tupla_Poke[1]}' in PEPE.Tupla_Poke)
print (f'{PEPE.Diccionario_Poke["Poke3"]}' in PEPE.Set_Conjunto_Poke1)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables y snake case {snake_case2}')

print (f'{Productos8}')

Productos8_Sorted = dict(sorted(Productos8.items(), key=lambda item : item[1]))

print (f'{Productos8_Sorted}')

print (f'-' * 20)

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')

print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

print (f'-' * 20)

print (f'{Productos8}')

Productos8_Sorted = dict(sorted(Productos8.items(), key=lambda item : item[1]))

print (f'{Productos8_Sorted}')

print (f'-' * 20)

Cociente, Residuo = divmod(Objeto11.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El Cociente es {Cociente}')
print (f'El Residuo es {Residuo}')

print (f'{PEPE.Lista2}')
print (f'{PEPE.Lista2[::2]}')
print (f'{PEPE.Lista2[::3]}')
print (f'{PEPE.Lista2[:2]}')
print (f'{PEPE.Lista2[2:]}')
print (f'{PEPE.Lista2[2:3]}')
print (f'{PEPE.Lista2[0:None]}')
print (f'{PEPE.Lista2[:]}')

print (f'{Lista_Uno[2]} eso que esta ahi es un {PEPE.Lista2[2]}?')

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

print (f'-' * 20)

print (f'{Lista_Uno_Copia}')
print (f'La lista 1 tiene {len(Lista_Uno_Copia)} elementos')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'-' * 20)

print (f'{Productos8}')

Productos8_Sorted = dict(sorted(Productos8.items(), key=lambda item : item[1]))

print (f'{Productos8_Sorted}')

print (f'-' * 20)

print (f'{dir(PEPE)}')

Tupla1 = ('Electrico', Objeto10.Tipo, Objeto10.Tipo, Objeto10.Tipo, Objeto10.Tipo, Objeto10.Tipo)
Tupla2 = 'Uno', 'Dos', 'Tres',
Tupla3 = 'Uno',

print (f'{Tupla1}')

Tupla1 = tuple(('Uno', 'Dos', 'Tres',))

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')

Set_Conjunto1 = {'Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde'}
Set_Conjunto1.add('Azul')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Red', 'Green', 'Blue'})

print (f'{Set_Conjunto1}')

Productos8_Sorted = dict(sorted(Productos8.items(), key=lambda item : item[1]))

print (f'{Productos8}')
print (f'{Productos8_Sorted}')

print (f'-' * 20)

Set_Conjunto2 = {1, 2, 3, 4, 5}
Set_Conjunto3 = {4, 5}
Set_Conjunto4 = set({8})

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto2 >= Set_Conjunto3}')

print (f'-' * 20)

print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto3 <= Set_Conjunto2}')

print (f'-' * 20)

print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')

print (f'-' * 20)

SetA = {1, 2, 3, 4}
SetB = set([3, 4, 5, 6])

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

'''SetA.symmetric_difference_update(SetB)

print (f'{SetA}')'''

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')
Set_Conjunto_Menu2 = frozenset({'Caramelo'})
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, Objeto11.Nombre})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : "Erick",
    'Edad' : 37,
    'Votante' : not False
}

Diccionario2 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
}

Diccionario3 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "Q"})

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

Diccionario1_Copia = Diccionario1.copy()

del Diccionario1['Nombre']

Diccionario1.pop("Edad")

Diccionario1.clear()

print (f'{Diccionario1}')

print (f'-' * 20)

print (f'{Diccionario1_Copia}')

Diccionario1_Copia['Nombre'] = Saludar_Dos()

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

Diccionario4 = {
    'Tres' : 3,
    'Uno' : 1,
    'Cuatro' : 4,
    'Dos' : 2
}

Diccionario4_Sorted = dict(sorted(Diccionario4.items(), key=lambda item : item[1]))

'''print (f'{Diccionario4}')
print (f'{Diccionario4_Sorted}')'''

print (f'-' * 20)

print (f'{Diccionario4}')

Diccionario4_Sorted = dict(sorted(Diccionario4.items(), key=lambda item : item[1]))

print (f'{Diccionario4_Sorted}')

print (f'-' * 20)

print (f'{Diccionario2["Nombre"][2]} no puede votar ya que solo tiene {Diccionario1.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', Objeto9.Nombre)
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2["Dos"] = PEPE.Tupla_Poke[1]

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

Key3 = [f'Key_{i}' for i in range(len(Lista_Uno_Copia))]

Diccionario5 = dict(zip(Key3, Lista_Uno_Copia))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key_2"]}')
print (f'{Diccionario5.get("Key_3")}')

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

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Fecha3 = '2026-04-01'

try:
    Fech3 = datetime.strptime(Fecha3, '%Y-%m-%d').date()
    Fech3_Formateada = pd.to_datetime(Fech3)
    Cargar_Csv3['date'] = pd.to_datetime(Cargar_Csv3['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato incorrecto')
    exit()
    
Cargar_Csv3['TOTALITO'] = Cargar_Csv3['quantity'] * Cargar_Csv3['price']
    
Encontrado3 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech3_Formateada.date()]

if (Encontrado3.empty):
    print (f'No hay ventas en esta fecha')
else:
    print (f'Genial! se encontraron ventas en esta fecha')
    
    Grupo7 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo7_Min = Grupo7.idxmin()
    Grupo7_Max = Grupo7.idxmax()
    Grupo7_Min_Cant = Grupo7.min()
    Grupo7_Max_Cant = Grupo7.max()
    
    print (f'En la fecha {Fech3_Formateada} el producto {Grupo7_Min} vendio un total de {Grupo7_Min_Cant} unidades')
    print (f'En la fecha {Fech3_Formateada} el producto {Grupo7_Max} vendio un total de {Grupo7_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron es {Grupo7.count()}')
    
    print (f'La cantidad de productos vendidos en esta fecha fue {Grupo7.sum()}')
    
    print (f'El promedio de productos vendidos es {Grupo7.mean()}')
    
    Grupo8 = Encontrado3.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue ${Grupo8.sum()}')
    
    Promedio3 = Grupo8.sum() / Grupo7.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Promedio3, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Grupo8.mean(), 2)}')
    
Lista_Csv3 = list(Cargar_Csv3['product'])

print (f'{Lista_Csv3}')

Key4 = [f'Key{i}' for i in range(len(Lista_Csv3))]

Diccionario6 = dict(zip(Key4, Lista_Csv3))

print (f'{Diccionario6}')
print (f'{Diccionario6.keys()}')
print (f'{Diccionario6.values()}')
print (f'{Diccionario6.items()}')
print (f'{Diccionario6["Key2"]}')
print (f'{Diccionario6.get("Key6")}')

print (f'-' * 20)

for clave, valor in Diccionario6.items():
    print (f'{clave} : {valor}')
    
print (f'-' * 20)

try:
    with open('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        for elemento in Documento_Lineas:
            if (elemento.strip() == PEPE.Diccionario_Poke['Poke1']):
                print (f'Este es el pokemon favorito de {PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Ash")]}')
                break
            else:
                continue
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo buscado no existe')
    
print (f'-' * 20)

for indice, elemento in Cargar_Csv3.iterrows():
    Unidad3 = elemento["product"]
    Unidad4 = elemento["price"]
    
    print (f'El precio de {Unidad3} es ${Unidad4}')
    
print (f'-' * 20)

Division_Baja = 14 // 7
Exponente = 4 ** 3
Modulo = 20 % 6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {Division_Baja}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'-' * 20)

print (f'El tipo de dato de la variable es {type(variable1)}')
print (f'El tipo de dato de la variable es {type(variable4)}')
print (f'El tipo de dato de la variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de dato de la variable es {type(variable6)}')
print (f'El tipo de dato de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato de la variable es {type(PEPE.Tupla_Poke)}')
print (f'El tipo de dato de la variable es {type(Diccionario_Vacio1)}')
print (f'El tipo de dato de la variable es {type(Objeto9)}')
print (f'El tipo de dato de la variable es {type(Funcion_Diccionario)}')
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

variable8 = 'Erick'
variable9 = 19

if (variable8 == variable1 and variable9 > 20):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')
    
print (f'-' * 20)

if (variable8 == variable2 or variable9 > 20):
    print (f'Al menos una de las condiciones se cumple')
else:
    print (f'Error, ninguna condicion se cumple')
    
print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorito):
        self.Trainer = Trainer
        self.City = City
        self.Favorito = Favorito
        self.Pokedex = Sumatoria2(1, 2, 3, 4, 5)
        self.Classified = True

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorito} while visiting {self.City}')
        
Objeto31 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto9.Nombre)
Objeto32 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto10.Nombre)
Objeto33 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto11.Nombre)

Objeto31.Desplegar()
Objeto32.Desplegar()
Objeto33.Desplegar()

print (f'La cantidad de pokemones que hay en la ciudad de {Objeto32.City} es de {Objeto32.Pokedex}')

print (f'-' * 20)

Negativo = -5

print (f'Ahora el numero es positivo {int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]
Anonima4 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)

if (Any_Iterable == True):
    print (f'Los numeros pares de la lista son {Lista_Iterable}')
    print (f'Los numeros pares de la lista son {list(Anonima4)}')
else:
    print (f'Error, no hay numeros pares en la lista')
    
print (f'-' * 20)

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, la cadena esta vacia')
    
Cociente2, Residuo2 = divmod(Objeto11.Cantidad, Sumatoria2(1, 2, 3, 1))

print (f'El Cociente2 es {Cociente2}')
print (f'El Residuo2 es {Residuo2}')

print (f'-' * 20)

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

Lista_Nombres2 = ['juan salvo', 'henry courtney', 'elizabeth bennet', 'marge simpson']
Lista_Nombres2_Actualizada = list([])

for elemento in Lista_Nombres2:
    Lista_Nombres2_Actualizada.extend([elemento.title()])
    
print (f'Lista Original: {Lista_Nombres2}')
print (f'Lista Actualizada: {Lista_Nombres2_Actualizada}')

variable11 = 'Erick josue'

if (variable11.istitle()):
    print (f'Correcto, cada palabra comienza con mayuscula')
else:
    print (f'Error, cada palabra no comienza con mayuscula')
    
print (f'{variable10.lower().find("t")}')
print (f'{variable10.lower().index("b")}')

print (f'La letra {variable10_letra} aparece un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable12 = '          Laut   aro     '

print (f'{variable12}')

print (f'{variable12.strip()}')

print (f''.join(variable12.split()))

variable13 = '----hola mundo***'

print (f'{variable13}')
print (f'{variable13.strip("-*")}')

variable14 = 'esto es un texto cualquiera pero lo que deseo es ver si esto sirve o no'

Lista_variable14 = variable14.split(' ')

for elemento in Lista_variable14:
    print (f'{elemento}')
    
print (f'La cantidad de palabras digitadas es {len(Lista_variable14)}')

var11 = 'erick'

if (isinstance(var11, (str))):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Error, lo que ingresaste no es un texto')
    
if (var11.isalpha()):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Error, lo que ingresaste no es un texto')
    
try:
    Valor3 = int(var11)
    print (f'Lo que ingresaste no es texto')
except (ValueError):
    print (f'Lo que ingresaste es texto')
    
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
except Exception:
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
    print (f'Lo ingresado es un numero entero o decimal')
else:
    print (f'Error de formato no es ni entero ni decimal')
    
try:
    Numerito8 = float(var14)
    if (Numerito8.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except Exception as Errore2:
    print (f'Error lo que ingresaste no es un numero -> {str(Errore2)}')
    
print (f'-' * 20)

var15 = 'erick'

if (isinstance(var15, (int, str))):
    print (f'Lo ingresado es texto, numero o ambos')
else:
    print (f'Error de formato')
    
if (var15.isalnum()):
    print (f'Lo ingresado es texto, numero o ambos')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var16 = '  s  '

if (var16.isspace()):
    print (f'Esto esta compuesto por solo espacios')
else:
    print (f'Error, lo ingresado tiene mas que solo espacios')
    
var17 = 'eSteBAN aLVARaDO'

if (var17.replace(' ', '').lower().islower() == True):
    print (f'Lo que se ingreso esta completamente en minuscula')
else:
    print (f'Error, esto no esta totalmente en minuscula')
    
if (var17.replace(' ', '').upper().isupper() == True):
    print (f'Lo que se ingreso esta completamente en mayuscula')
else:
    print (f'Error, esto no esta totalmente en mayuscula')
    
if (var17.replace(' ', '').title().istitle() == True):
    print (f'Lo que se ingreso esta completamente en camel case')
else:
    print (f'Error, esto no esta totalmente en camel case')
    
print (f'-' * 20)

var18 = ''

if (bool(var18) == True):
    print (f'Ya no esta vacio')
else:
    print (f'Esto esta completamente vacio')
    
print (f'-' * 20)

print (f'{PEPE.Tupla_Poke[2]} aparece en la posicion {PEPE.Tupla_Poke.index("Misty")}')

Eliminado1 = Diccionario1_Copia.pop("Nombre")

print (f'El elemento eliminado es {Eliminado1}')

Contador = 0

while (Contador < 5):
    print (f'El contador es {Contador + 1}')
    Contador += 1
    
print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'{PEPE.Lista_Numeros[Contador]} X 100 es {PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1
    
print (f'-' * 20)

Lista_Animales2 = ['Jirafa']
Lista_Animales2.append(PEPE.Lista2[PEPE.Tupla_Poke.index("Misty")])
Lista_Animales2.insert(1, 'Cocodrilo')
Lista_Animales2.extend(['Ardilla'])

print (f'{Lista_Animales2}')

Lista_Animales3 = []

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        for indice, elemento in enumerate(Documento_Lineas, start=1):
            Lista_Animales3.append(elemento.strip())
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
print (f'{Lista_Animales2}')
print (f'{Lista_Animales3}')

Contador = 0

while (Contador < len(Lista_Animales2)):
    if (Lista_Animales2[Contador] == 'Koala'):
        print (f'Me gustan los animales de Australia')
        break
    else:
        Contador += 1
        continue
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Tupla1, Lista_Uno_Copia):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento1, elemento2, elemento3, elemento4 in zip(Tupla1, Lista_Uno_Copia, PEPE.Set_Conjunto_Poke1, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2} -- {elemento3} -- {elemento4}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(0 + 5, len(Lista_Animales3)):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Lista_Animales3[:-7]:
    print (f'{elemento}')
    
print (f'-' * 20)

Lista_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Mult}')

Menor = min(Lista_Mult)
Mayor = max(Lista_Mult)
Redondeado = round(14.458795, 2)
Sumatoria4 = sum(Lista_Mult)

print (f'El menor de los numeros es {Menor}')
print (f'El mayor de los numeros es {Mayor}')
print (f'El redodndeado con dos unidades es {Redondeado}')
print (f'El resultado de la sumatoria es {Sumatoria4}')

print (f'{bool("")}')
print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool(not True)}')
print (f'{bool(False)}')

print (f'-' * 20)

Todo_All = all([Lista_Nombres2_Actualizada, Tupla_Elemento1, Set_Conjunto_Menu1, PEPE.Diccionario_Poke, variable7])

print (f'{Todo_All}')

print (f'-' * 20)

Uno = int('500')
Dos = str(500)
Tres = float(Uno)
Cuatro = list(Set_Conjunto_Menu1)
Cinco = tuple(PEPE.Set_Conjunto_Poke1)
Seis = set(Lista_Animales3)

print (f'{type('500')} -- {type(int('500'))}')
print (f'{type(500)} -- {type(str(500))}')
print (f'{type(Uno)} -- {type(float(Uno))}')
print (f'{type(Set_Conjunto_Menu1)} -- {type(list(Set_Conjunto_Menu1))}')
print (f'{type(PEPE.Set_Conjunto_Poke1)} -- {type(tuple(PEPE.Set_Conjunto_Poke1))}')
print (f'{type(Lista_Animales3)} -- {type(set(Lista_Animales3))}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto_Poke1))

print (f'-' * 20)

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

print (f'-' * 20)

import Paquete.Sub_Paquete.Segundo as PEPE3

variable_PEPE3 = PEPE3

print (f'-' * 20)

'''def Exception_Finale():
    while (True):
        try:
            Numerito = input(f'Ingrese un numero: ')
            Numerito1 = float(Numerito)
            if (Numerito1.is_integer()):
                print (f'Lo que ingresaste es un numero entero')
                break
            else:
                print (f'Lo que ingresaste es un numero decimal')
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')

Exception_Finale()'''

'''import requests

Diccionario_API = {
    'Nombre' : ["Pistacho", "ChocoMenta", "Limon", "Mango"],
    'Indice' : [0, 1, 2, 3]
}

Segunda1 = requests.post('http://127.0.0.1:8002/grupo7/unidad1', json=(Diccionario_API))
Segunda2 = Segunda1.json()

print (f'Agregado {Segunda2}')

print (f'-' * 20)

Tercera1 = requests.put('http://127.0.0.1:8002/grupo7/unidad1', json=(Diccionario_API))
Tercera2 = Tercera1.json()

print (f'Reemplazo {Tercera2}')

print (f'-' * 20)

Cuarta1 = requests.delete('http://127.0.0.1:8002/grupo7/unidad1', json=(Diccionario_API))
Cuarta2 = Cuarta1.json()

print (f'Elimiando {Cuarta2}')

print (f'-' * 20)

Primera1 = requests.get('http://127.0.0.1:8002/grupo7/')
Primera2 = Primera1.json()

print (f'La lista de helados es {Primera2["Helados"]}')'''