try:
    import Module_Own as PEPE
except (ImportError, ModuleNotFoundError):
    print (f'Error, el modulo seleccionado no existe')
    raise

Diccionario1X = {
    'Nombre' : "Erick"
}

for clave, valor in Diccionario1X.items():
    print (f'{clave} : {valor}')
    
print (f'-' * 20)

Diccionario2X = {
    'Nombre' : ["Erick", "Josue", "Karlita"]
}

for clave, valor in Diccionario2X.items():
    for elemento in enumerate(valor, start=1):
        print (f'{elemento[0]} -- {elemento[1]}')
        
print (f'-' * 20)

Diccionario3X = {
    'User1' : {
        'Nombre' : "Erick",
        'Edad' : 37,
        'Votante' : True
    },
    
    'User2' : {
            'Nombre' : "Carmelo",
            'Edad' : 55,
            'Votante' : True
        }
}

for Nivel1_Clave, Nivel1_Valor in Diccionario3X.items():
    for Nivel2_Clave, Nivel2_Valor in Nivel1_Valor.items():
        print (f'{Nivel2_Clave} : {Nivel2_Valor}')
        
Usuario1 = 'User2'
Campo1 = 'Ubicacion'

for clave, valor in Diccionario3X.items():
    Ubicado1 = Diccionario3X.get(Usuario1)
    if (Ubicado1 is None):
        print (f'Error, el Usuario esta mal')
        break
    else:
        Ubicado2 = Ubicado1.get(Campo1)
        if (Ubicado2 is None):
            print (f'Error, el Campo esta mal')
            break
        else:
            print (f'Usuario y Campos son correctos')
            break
        
print (f'-' * 20)

Diccionario4X = {
    "ana": {"edad": 25, "ciudad": "Quito"},
    "luis": {"edad": 30, "ciudad": "Guayaquil"}
}

def Ejercicio1(Diccionario, Persona, Elemento):
    Ubicado1 = Diccionario.get(Persona)
    if (Ubicado1 is None):
        return (False, 'Error, el Usuario2 es incorrecto')
    else:
        Ubicado2 = Ubicado1.get(Elemento)
        if (Ubicado2 is None):
            return (False, 'Error, el Campo2 es incorrecto')
        else:
            return (True, 'Ambos Usuario2 y Campo2 son correctos')

Usuario2 = "ana" #type: ignore
Campo2 = 'profesion'

if (Diccionario4X):
    Sample1 = Ejercicio1(Diccionario4X, Usuario2, Campo2)
    if (Sample1 == True):
        print (f'{Sample1}')
    else:
        print (f'{Sample1}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Datos1 = {
    "ana":  {"edad": 25, "ciudad": "Quito"},
    "luis": {"edad": 30, "ciudad": "Guayaquil"}
    }

Usuario3 = 'luis'
Campo3 = 'ciudad'
Nuevo_Valor3 = 'San Jose'

def Ejercicio2(Diccionario, Persona, Elemento, Nuevo):
    Ubicado1 = Diccionario.get(Persona)
    if (Ubicado1 is None):
        return (False, 'El Usuario3 es incorrecto')
    else:
        Ubicado2 = Ubicado1.get(Elemento)
        if (Ubicado2 is None):
            return (False, 'El Campo3 es incorrecto')
        else:
            Diccionario[Persona][Elemento] = Nuevo
            return (True, f'Tanto el Usuario3 como el Campo3 son correctos {Diccionario}')

if (len(Datos1) == 0):
    print (f'Error, el diccionario anidado esta vacio')
else:
    Sample2 = Ejercicio2(Datos1, Usuario3, Campo3, Nuevo_Valor3)
    if (Sample2 == True):
        print (f'{Sample2}')
    else:
        print (f'{Sample2}')
        
print (f'-' * 20)

def Ejercicio3(Numero):
    return Numero + 10

def Ejercicio4(Numero):
    return Numero * 10

def Ejercicio5(Funcion, Numero):
    return Funcion(Numero)

print (f'El resultado de la sumatoria es {Ejercicio5(Ejercicio3, 5)}')
print (f'El resultado de la multiplicacion es {Ejercicio5(Ejercicio4, 5)}')

print (f'-' * 20)

Lista_Nombres1 = ['Erick', 'Josue', 'Karlita']
Lista_Nombres2 = list(['Carmelo', 'Susanita', 'Roxana'])

def Ejercicio6(Lista):
    for indice, elemento in enumerate(Lista, start=1):
        print (f'{indice} : {elemento}')

def Ejercicio7(Lista):
    for indice, elemento in enumerate(Lista, start=1):
        print (f'{indice} : {elemento}')
        
def Ejercicio8(Funcion, Lista):
    return Funcion(Lista)

Ejercicio8(Ejercicio6, Lista_Nombres1)

print (f'-' * 20)

Ejercicio8(Ejercicio7, Lista_Nombres2)

print (f'-' * 20)

def Ejercicio9(Num1, Num2):
    return Num1 + Num2 + 5

def Ejercicio10(Num1, Num2):
    return Num1 * Num2 * 5

def Ejercicio11(Funcion, Numero1, Numero2):
    return Funcion(Numero1, Numero2)

print (f'El resultado de la sumatoria es {Ejercicio11(Ejercicio9, 2, 3)}')

print (f'-' * 20)

print (f'El resultado de la multiplicacion es {Ejercicio11(Ejercicio10, 2, 3)}')

print (f'-' * 20)

def Ejercicio12(Num1, Num2, *args, **kwargs):
    Acumulador = 0
    for elemento in kwargs.values():
        Acumulador += elemento
        
    return Num1 + Num2 + sum(args) + Acumulador

def Ejercicio13(Num1, Num2, *args, **kwargs):
    Acumulador = 0
    for elemento in kwargs.values():
        Acumulador += elemento
        
    return Num1 * Num2 * sum(args) * Acumulador

def Ejercicio14(Funcion, Numero1, Numero2, *argumentos, **diccionario):
    return Funcion(Numero1, Numero2, *argumentos, **diccionario)

print (f'El resultado de la operacion es {Ejercicio14(Ejercicio12, 1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, num1=5, num2=15)}')

print (f'-' * 20)

print (f'El resultado de la operacion es {Ejercicio14(Ejercicio13, 1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, num1=5, num2=15)}')

print (f'-' * 20)

Diccionario_Numeral1 = dict({
    'Num1' : 7,
    'Num2' : 3,
    'Num3' : 1,
    'Num4' : 6,
    'Num5' : 2
})

def Ejercicio15(Diccionario):
    if (len(Diccionario) == 0):
        return None
    else:
        Lista_Par = []
        
        for clave, valor in Diccionario.items():
            if (valor % 2 == 0):
                Lista_Par.append(clave)
            else:
                continue
            
        return Lista_Par
            
def Ejercicio16(Diccionario):
    if (len(Diccionario) == 0):
        return None
    else:
        Lista_ImPar = []
        
        for clave, valor in Diccionario.items():
            if (valor % 2 != 0):
                Lista_ImPar.append(clave)
            else:
                continue
            
        return Lista_ImPar

Sample15 = Ejercicio15(Diccionario_Numeral1)
Sample16 = Ejercicio16(Diccionario_Numeral1)

if (Sample15 is None or Sample16 is None):
    print (f'Error, el diccionario esta vacio')
else:
    def Ejercicio17(Funcion, Lista):
        return Funcion(Lista)
    
    print (f'Los numeros pares son {Ejercicio17(Ejercicio15, Diccionario_Numeral1)}')
    
    print (f'-' * 20)
    
    print (f'Los numeros pares son {Ejercicio17(Ejercicio16, Diccionario_Numeral1)}')
    
print (f'-' * 20)

Lista_Animales1 = ['Cocodrilo', 'Capibara']
Lista_Animales1.append('Avestruz')
Lista_Animales1.insert(2, 'Tortuga')
Lista_Animales1.extend(['Sapo'])

# print (f'{Lista_Animales1}')

def Ejercicio18(Lista):
    if (len(Lista) == 0):
        return None
    else:
        while (Lista[:]):
            print (f'{Lista}')
            Lista.pop(-1)

Sample18 = Ejercicio18(Lista_Animales1)

if (Sample18 is None):
    print (f'Error, la lista esta vacia')
else:
    Sample18 #type: ignore
    
print (f'-' * 20)

def Ejercicio19(Numero1:int, Numero2:int) -> int:
    '''Esto es un docstring, la funcion suma dos argumentos y retorna el resultado'''
    return Numero1 + Numero2

Sample19 = Ejercicio19(12, 7)

print (f'El resultado de la operacion es {Sample19}')

print (f'{help(Ejercicio19)}')

print (f'-' * 20)

def Ejercicio20(Texto = 'No hay nada que mostrar'):
    return Texto

Sample20 = Ejercicio20()

print (f'{Sample20}')

def Ejercicio21(Num1, Num2, Num3):
    return Num1 + Num2 + Num3

print (f'El resultado de la operacion es {Ejercicio21(1, 2, 3)}')

print (f'-' * 20)

def Ejercicio22(Num1=500, Num2=700, Num3=120):
    return Num1 + Num2 + Num3

print (f'El resultado de la operacion es {Ejercicio22(1, 2, 3)}')

print (f'-' * 20)

def Ejercicio23(Num1=500, Num2=700, Num3=120):
    return Num1 + Num2 + Num3

print (f'El resultado de la operacion es {Ejercicio23()}')

print (f'-' * 20)

def Ejercicio24(Num1, Num2, Num3=120):
    return Num1 + Num2 + Num3

print (f'El resultado de la operacion es {Ejercicio24(1, 2)}')

print (f'-' * 20)

def Ejercicio25(*args):
    Promedio = sum(args) / len(args)
    return round(Promedio, 2)

Sample25 = Ejercicio25(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print (f'El promedio de los numeros ingresados es {Sample25}')

print (f'-' * 20)

def Ejercicio26(**kwargs):
    Acumulador = 0
    for _, valor in kwargs.items(): # Si un valor no se necesita se puede reemplazar por el simbolo _
        Acumulador += valor

    return Acumulador

Sample26 = Ejercicio26(
    Num1=5,
    Num2=3,
    Num3=2,
    Num4=0,
    Num5=7
)

if (Sample26):
    print (f'El resultado de la operacion es {Sample26}')
else:
    print (f'Error, el acumulador es cero')
    
print (f'-' * 20)

def Ejercicio27(Num1, Num2, *args, **kwargs):
    Acumulador = 0
    
    for elemento in kwargs.values():
        Acumulador += elemento
        
    return Num1 + Num2 + sum(args) + Acumulador

Sample27 = Ejercicio27(
    2, 3,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    Numero1 = 50,
    Numero2 = 13
)

print (f'El resultado de la operacion es {Sample27}')

print (f'-' * 20)

def Ejercicio28(*participantes, **detalles):
    print (f'Los participantes son: ')
    
    for elemento in enumerate(participantes):
        print (f'{elemento[0]} : {elemento[1]}')
    
    print (f'-' * 20)
    
    print (f'Los detalles del evento son: ')
    
    for clave, valor in detalles.items():
        print (f'{clave} : {valor}')

Sample28 = Ejercicio28(
    'Erick', 'Josue', 'Karlita',
    Fecha = 'Domingo',
    Lugar = 'Iglesia de Santa Barbara',
    Tema = 'Gran Bingo'
)

print (f'-' * 20)

def Ejercicio29(Limite):
    Lista_Fibonacci = list([0, 1])
    
    while (len(Lista_Fibonacci) < Limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

Sample29 = Ejercicio29(10)

if (Sample29):
    print (f'La lista Fibonacci es: {Sample29}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
Lista_Segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]

def Ejercicio30(Lista1, Lista2):
    Set_Conjunto = set({})
    Lista_Tercera = list([])
    for elemento in Lista1:
        if (elemento in Lista2):
            Set_Conjunto.add(elemento)
        else:
            continue
        
    Lista_Tercera = list(Set_Conjunto)
    
    return Lista_Tercera

Sample30 = Ejercicio30(Lista_Primera, Lista_Segunda)

if (Lista_Primera and Lista_Segunda):
    if (Sample30):
        print (f'La lista resultado es {Sample30}')
    else:
        print (f'No hay ningun numero en las listas originales que cumplan esta condicion')
else:
    print (f'Error, ambas listas deben tener contenido')
    
print (f'-' * 20)

var0 = 1

print (f'{type(var0)}')
print (f'{type(var0 + 0.1)}')

var0 = '35'

print (f'{type(var0)}')

var0 = int(var0)

print (f'{type(var0)}')

Lista_Concatenacion1 = ['Erick', 'Josue']
Lista_Concatenacion2 = ['Karlita', 'Roxana']

print (f'{Lista_Concatenacion1 + Lista_Concatenacion2}')

print (f'-' * 20)

Tupla_Concatenacion1 = ('Erick', 'Josue',)
Tupla_Concatenacion2 = 'Karlita', 'Roxana',

print (f'{Tupla_Concatenacion1 + Tupla_Concatenacion2}')

print (f'-' * 20)

var1 = 0

if (var1):
    print (f'El numero es valido, puede ser positivo, negativo o decimal')
else:
    print (f'Error, esto no puede ser cero')
    
print (f'-' * 20)

var2 = ''

if (var2):
    print (f'Correcto, esto debe ser texto')
else:
    print (f'Error, esto no puede estar vacio')
    
print (f'-' * 20)

var3 = []

if (var3):
    print (f'Correcto, la lista tiene contenido')
else:
    print (f'Error, la lista no puede estar vacia')
    
print (f'-' * 20)

var4 = {

}

if (var4):
    print (f'Correcto, el diccionario anidado tiene contenido')
else:
    print (f'Error, el diccionario no puede estar vacio')
    
print (f'-' * 20)

var5 = None

if (var5):
    print (f'Correcto, esto tiene una asignacion')
else:
    print (f'Error, la variable debe tener una asignacion')
    
if (not var5):
    print (f'Correcto, esto tiene una asignacion')
else:
    print (f'Error, la variable debe tener una asignacion')
    
print (f'-' * 20)

Lista_Elementos1 = [1, 2, 3, 4, 5]

def Ejercicio31(Lista):
    Contador = 0
    if (len(Lista) == 0):
        return None
    else:
        while (Contador < len(Lista)):
            Contador += 1
            
        return Contador

Sample31 = Ejercicio31(Lista_Elementos1)

if (Sample31 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample31):
        print (f'La lista esta compuesta por {Sample31} elementos')
    else:
        print (f'Error, la lista actualmente no tiene nada')
        
print (f'-' * 20)

def Ejercicio32(Lista):
    Acumulador = 0
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador += elemento
        else:
            continue
        
    return Acumulador

Sample32 = Ejercicio32(Lista_Elementos1)

if (len(Lista_Elementos1) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample32):
        print (f'El resultado de sumar los numeros pares es {Sample32}')
    else:
        print (f'Error, no hay numeros pares que sumar')
        
print (f'-' * 20)

def Ejercicio33(Lista):
    Acumulador = 0
    
    for elemento in Lista:
        Acumulador += elemento
        
    return Acumulador

if (Lista_Elementos1):
    Sample33 = Ejercicio33(Lista_Elementos1)
    print (f'El resultado de sumar todos los numeros de la lista es {Sample33}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio34(Lista):
    Acumulador1 = 0
    Acumulador2 = 0
    Acumulador3 = 0
    Acumulador4 = 0
    Acumulador5 = 0
    if (len(Lista) == 0):
        return None
    else:
        for elemento in Lista[:]:
            Acumulador1 += elemento
            
        for elemento in Lista[:-1]:
            Acumulador2 += elemento
            
        for elemento in Lista[:-2]:
            Acumulador3 += elemento
            
        for elemento in Lista[:-3]:
            Acumulador4 += elemento
            
        for elemento in Lista[:-4]:
            Acumulador5 += elemento
            
    return Acumulador1, Acumulador2, Acumulador3, Acumulador4, Acumulador5

Sample34 = Ejercicio34(Lista_Elementos1)

if (Sample34 is None):
    print (f'La lista esta vacia')
else:
    Suma_Acumulada1, Suma_Acumulada2, Suma_Acumulada3, Suma_Acumulada4, Suma_Acumulada5 = Sample34
    
    print (f'La sumatoria de elementos es {Suma_Acumulada1}')
    print (f'La sumatoria de elementos es {Suma_Acumulada2}')
    print (f'La sumatoria de elementos es {Suma_Acumulada3}')
    print (f'La sumatoria de elementos es {Suma_Acumulada4}')
    print (f'La sumatoria de elementos es {Suma_Acumulada5}')
    
print (f'-' * 20)

def Ejercicio35(Lista, Num):
    Finder = False

    for elemento in Lista[:]:
        if (elemento == Num):
            Finder = True
            break
        else:
            continue
        
    return Finder

Numero1 = 4

if (len(Lista_Elementos1) == 0):
    print (f'Error, la lista esta vacia')
else:
    Sample35 = Ejercicio35(Lista_Elementos1, Numero1)
    if (Sample35 == True):
        print (f'El numero {Numero1} fue encontrado en la lista')
    else:
        print (f'Error, el numero no fue encontrado')
        
print (f'-' * 20)

def Ejercicio36(Lista):
    Menor = min(Lista)
    Mayor = max(Lista)
    
    Lista_Resultado = [Menor, Mayor]
    
    return Lista_Resultado

Sample36 = Ejercicio36(Lista_Elementos1)

if (Lista_Elementos1):
    print (f'El menor de los numeros de la lista es {min(Sample36)}')
    print (f'El mayor de los numeros de la lista es {max(Sample36)}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio37(Lista, Num):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        for elemento in Lista[:]:
            if (elemento > Num):
                Contador += 1
            else:
                continue
            
        return Contador
    
Numero2 = 2

Sample37 = Ejercicio37(Lista_Elementos1, Numero2)

if (Sample37 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample37):
        print (f'La cantidad de numeros mayores que {Numero2} es {Sample37}')
    else:
        print (f'Error, no hay ningun numero mayor que {Numero2}')
        
print (f'-' * 20)

def Ejercicio38(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Pares = []
        Lista_Impares = list([])
        
        for elemento in Lista:
            if (elemento % 2 == 0):
                Lista_Pares.append(elemento)
            else:
                Lista_Impares.extend([elemento])
                
        return Lista_Pares, Lista_Impares

Sample38 = Ejercicio38(Lista_Elementos1)

if (Sample38 is None):
    print (f'Error, la lista esta vacia')
else:
    Lista_Numeros_Pares, Lista_Numeros_Impares = Sample38
    print (f'Lista Original: {Lista_Elementos1}')
    print (f'Lista Pares: {Lista_Numeros_Pares}')
    print (f'Lista Impares: {Lista_Numeros_Impares}')
    
print (f'-' * 20)

def Ejercicio39(Lista):
    Lista_Mult = []
    
    for _, elemento in enumerate(Lista, start=1):
        Lista_Mult.append(elemento * 2)
        
    return Lista_Mult

Sample39 = Ejercicio39(Lista_Elementos1)

if (len(Lista_Elementos1) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample39):
        print (f'Lista original: {Lista_Elementos1}')
        print (f'Lista multiplicado: {Sample39}')
        
print (f'-' * 20)

'''Lista_Promedios = []

Contador = 0

while (Contador < 3):
    while (True):
        Numero3 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numero4 = float(Numero3)
            if (Numero4.is_integer()):
                print (f'La nota {Contador + 1} es un numero entero')
                Lista_Promedios.append(Numero4)
                break
            else:
                print (f'La nota {Contador + 1} es un numero decimal')
                Lista_Promedios.extend([Numero4])
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador += 1
    
Promedio1 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas ingresadas es {round(Promedio1, 2)}')'''

Lista_Elementos2 = list([5, -6, 0, -1, -3, 0])

def Ejercicio40(Lista):
    Negativos = 0
    Positivos = 0
    Ceros = 0
    for elemento in Lista[0:None]:
        if (elemento > 0):
            Positivos += 1
        elif (elemento < 0):
            Negativos += 1
        else:
            Ceros += 1
            
    return Negativos, Positivos, Ceros

if (Lista_Elementos2):
    Sample40 = Ejercicio40(Lista_Elementos2)
    Total_Negativos, Total_Positivos, Total_Ceros = Sample40
    
    print (f'Total Numeros Positivos: {Total_Positivos}')
    print (f'Total Numeros Negativos: {Total_Negativos}')
    print (f'Total Numeros Ceros: {Total_Ceros}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

import re

Lista_Elementos3 = [
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
]

def Ejercicio41(Lista):
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
                Lista_Invalidos.append(elemento)
                
        return Lista_Validos, Lista_Invalidos

Sample41 = Ejercicio41(Lista_Elementos3)

if (Sample41 is None):
    print (f'Error, la lista esta vacia')
else:
    Lista_Correos_Validos, Lista_Correos_Invalidos = Sample41
    
    print (f'Lista correos originales: {Lista_Elementos3}')
    print (f'Lista correos validos: {Lista_Correos_Validos}')
    print (f'Lista correos invalidos: {Lista_Correos_Invalidos}')
    
print (f'-' * 20)

def Ejercicio42(Lista):
    Temporal = Lista[0]
    
    for elemento in Lista[:]:
        if (elemento > Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

Sample42 = Ejercicio42(Lista_Elementos1)

if (len(Lista_Elementos1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero mayor de la lista es {Sample42}')
    
print (f'-' * 20)

def Ejercicio43(Lista):
    Temporal = Lista[0]
    
    for elemento in Lista[:]:
        if (elemento < Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

Sample43 = Ejercicio43(Lista_Elementos1)

if (len(Lista_Elementos1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero menor de la lista es {Sample43}')
    
print (f'-' * 20)

Lista_Elementos4 = list([-15.5, -8, -3.2, -1, 0, 4, 7.5, 12, 19.1, 25])

def Ejercicio44(Lista):
    Contador = 0
    Acumulador = 0
    for elemento in Lista:
        if (elemento > 0):
            Contador += 1
            Acumulador += elemento
        else:
            continue
        
    return Contador, Acumulador

if (Lista_Elementos4):
    Sample44 = Ejercicio44(Lista_Elementos4)
    Contador1, Acumulador1 = Sample44
    
    print (f'Cantidad de numeros positivos: {Contador1}')
    print (f'Total suma de los numeros positivos: {Acumulador1}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Elementos5 = [65, 70, 54, 80, 69, 66]

def Ejercicio45(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Aprobados = 0
        Reprobados = 0
        Aprobados_Sum = 0
        
        for elemento in Lista[0:None]:
            if (elemento >= 70):
                Aprobados += 1
                Aprobados_Sum += elemento
            else:
                Reprobados += 1
                
        return Aprobados, Aprobados_Sum, Reprobados

Sample45 = Ejercicio45(Lista_Elementos5)

if (Sample45 is None):
    print (f'Error, la lista esta vacia')
else:
    Alumnos_Aprobados, Alumnos_Aprobados_Sum, Alumnos_Reprobados = Sample45
    
    print (f'Cantidad de alumnos aprobados: {Alumnos_Aprobados}')
    print (f'Suma de las notas aprobadas: {Alumnos_Aprobados_Sum}')
    print (f'Cantidad de alumnos reprobados: {Alumnos_Reprobados}')
    
print (f'-' * 20)

Lista_Elementos6 = list([15, 0, 8, 2, 0, 25, 4])

def Ejercicio46(Lista):
    Agotados = 0
    Stock_Bajo = 0
    Stock_Alto = 0
    Stock_Bajo_Sum = 0
    Stock_Alto_Sum = 0
    
    for elemento in Lista:
        if (elemento >= 1 and elemento <= 5):
            Stock_Bajo += 1
            Stock_Bajo_Sum += elemento
        elif (elemento == 0):
            Agotados += 1
        else:
            Stock_Alto += 1
            Stock_Alto_Sum += elemento
            
    return Agotados, Stock_Bajo, Stock_Alto, Stock_Bajo_Sum, Stock_Alto_Sum

Sample46 = Ejercicio46(Lista_Elementos6)

if (len(Lista_Elementos6) == 0):
    print (f'Error, la lista esta vacia')
else:
    Prod_Agotados, Prod_Stock_Bajo, Prod_Stock_Alto, Prod_Stock_Bajo_Sum, Prod_Stock_Alto_Sum = Sample46
    
    print (f'Total prod agotados: {Prod_Agotados}')
    print (f'Total prod stock bajo: {Prod_Stock_Bajo}')
    print (f'Total prod stock alto: {Prod_Stock_Alto}')
    print (f'Suma prod stock bajo: {Prod_Stock_Bajo_Sum}')
    print (f'Suma prod stock alto: {Prod_Stock_Alto_Sum}')
    print (f'Suma prod con stock: {Prod_Stock_Bajo_Sum + Prod_Stock_Alto_Sum}')
    
print (f'-' * 20)

Lista_Elementos7 = [12, 8, 5, 1, 7, 2, 10]

def Ejercicio47(Lista):
    for indice, elemento in enumerate(Lista, start=0):
        if (elemento == 0):
            return indice
        else:
            continue
        
    return None

Sample47 = Ejercicio47(Lista_Elementos7)

if (Lista_Elementos7):
    if (Sample47 is None):
        print (f'No se ha encontrado ningun producto agotado en inventario')
    else:
        print (f'El primer producto agotado del inventario aparece en la posicion {Sample47}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Elementos8 = list([120, 350, 80, 600, 150, 700])

def Ejercicio48(Lista, Cantidad):
    Contador = 0
    
    while (Contador < len(Lista[:])):
        if (Lista[Contador] > Cantidad):
            return Contador
        else:
            Contador += 1
            continue
        
    return None

Monto1 = 800

Sample48 = Ejercicio48(Lista_Elementos8, Monto1)

if (len(Lista_Elementos8) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample48 is None):
        print (f'Error, el Monto ${Monto1} no aparecio en el inventario')
    else:
        print (f'La primer venta que supera el monto ${Monto1} aparece en la posicion {Sample48} y la venta es de ${Lista_Elementos8[Sample48]}')
        
print (f'-' * 20)

# Modo Solucion1

Lista_Elementos9 = [10, 1, 2, 4, 3, 5, 6]

def Ejercicio49(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            
    return None

Sample49 = Ejercicio49(Lista_Elementos9)

if (Lista_Elementos9):
    if (Sample49 is None):
        print (f'No hay numeros repetidos en la lista')
    else:
        print (f'El primer numero repetido es {Sample49}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)
    
# Modo Solucion2

Lista_Elementos10 = [10, 1, 2, 4, 3, 5, 6]

def Ejercicio50(Lista):
    for i in range(len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                return Lista[i]
            else:
                continue
            
    return None

Sample50 = Ejercicio50(Lista_Elementos10)

if (Lista_Elementos10):
    if (Sample50 is None):
        print (f'No hay numeros repetidos en la lista')
    else:
        print (f'El primer numero repetido de la lista es {Sample50}') 
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Elementos11 = list([90, 91, 79, 70])

def Ejercicio51(Lista):
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] < Lista[i]):
            return i
        else:
            continue
        
    return None

Sample51 = Ejercicio51(Lista_Elementos11)

if (len(Lista_Elementos11) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample51 is None):
        print (f'No hay ningun aumento en ventas')
    else:
        print (f'El primer aumento en ventas sucede en la posicion {Sample51} y es con el monto {Lista_Elementos11[Sample51]}')
        
print (f'-' * 20)

Lista_Elementos12 = [100, 97, 95, 80, 78]

def Ejercicio52(Lista, Num):
    for i in range(0+1, len(Lista[0:None])):
        if (Lista[i - 1] - Lista[i] >= Num):
            return Lista[i - 1], Lista[i], Lista[i - 1] - Lista[i], i
        else:
            continue
        
    return None

Caida = 20

if (Lista_Elementos12):
    Sample52 = Ejercicio52(Lista_Elementos12, Caida)
    if (Sample52 is None):
        print (f'No ha habido una caida en temperatura en la ultima hora')
    else:
        Temperatura_Anterior, Temperatura_Actual, Grados, Posicion = Sample52
        print (f'Alerta!!! acaba de suceder una caida en temperatura en la posicion {Posicion}')
        print (f'Temperatura_Anterior {Temperatura_Anterior}')
        print (f'Temperatura_Actual {Temperatura_Actual}')
        print (f'Grados: {Grados}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Elementos13 = list([1, 1, 0, 1, 3])

def Ejercicio53(Lista):
    for i in range(0 + 2, len(Lista[:])):
        if (Lista[i - 2] < Lista[i - 1] and Lista[i - 1] > Lista[i]):
            return i - 1
        else:
            continue
        
    return None

Sample53 = Ejercicio53(Lista_Elementos13)

if (len(Lista_Elementos13) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample53 is None):
        print (f'No hay ningun pico en la lista')
    else:
        print (f'El pico sucede en la posicion {Sample53} con el numero {Lista_Elementos13[Sample53]}')
        
print (f'-' * 20)

# Consultar valores ✅ Consultar.

Capitales = {"Costa Rica": "San José", "México": "Ciudad de México", "Italia" : "Roma", "Argentina": "Buenos Aires", "España": "Madrid"}

Ubicado3 = Capitales.get('Italia')

if (Ubicado3 is None):
    print (f'Error, Italia no es parte del diccionario')
else:
    print (f'La capital de Italia es {Ubicado3}')
    
print (f'-' * 20)

Productos1 = {"Laptop": 1200, "Mouse": 25, "Teclado": 45, "Monitor": 300}

Item1 = 'Escoba'

def Ejercicio54(Diccionario, Articulo):
    Ubicado = Diccionario.get(Articulo)
    if (Ubicado is None):
        return False
    else:
        return Ubicado

if (len(Productos1) == 0):
    print (f'El diccionario esta vacio')
else:
    Sample54 = Ejercicio54(Productos1, Item1)
    if (Sample54 == False):
        print (f'Error, el articulo {Item1} no existe en el inventario')
    else:
        print (f'El precio del articulo {Item1} es ${Sample54}')
        
print (f'-' * 20)

# Actualizar elementos ✅ Actualizar.

Productos2 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300
}

Item2 = 'Escoba'
Item2_Price = 55

def Ejercicio55(Diccionario, Articulo, Precio):
    Ubicado = Diccionario.get(Articulo)
    if (Ubicado is None):
        return False
    else:
        Diccionario[Articulo] = Precio
        return True

Sample55 = Ejercicio55(Productos2, Item2, Item2_Price)

if (Productos2):
    if (Sample55 == True):
        print (f'El precio del articulo {Item2} fue actualizado exitosamente!')
    else:
        print (f'Error, el articulo {Item2} no existe en el inventario')
else:
    print (f'Error, el diccionario esta')
    
print (f'-' * 20)

# Agregar elementos ✅ Agregar.

Productos3 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio56(Diccionario, Articulo, Precio):
    Ubicado = Diccionario.get(Articulo)
    
    if (Ubicado is None):
        Diccionario[Articulo] = Precio
        return False
    else:
        return True

Item3 = 'Escoba'
Item3_Price = 200

Sample56 = Ejercicio56(Productos3, Item3, Item3_Price)

if (len(Productos3) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample56 == True):
        print (f'Error, el articulo {Item3} ya existe en el inventario, no puede agregarse nuevamente')
    else:
        print (f'El articulo {Item3} no estaba incluido en el inventario, fue agregado exitosamente!')
        
print (f'-' * 20)

# Eliminar elementos ✅ Eliminar.

Productos4 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio57(Diccionario, Articulo):
    Ubicado = Diccionario.get(Articulo)
    if (Ubicado is None):
        return False
    else:
        del Diccionario[Articulo]
        return True

Item4 = 'Mouse'

Sample57 = Ejercicio57(Productos4, Item4)

if (not Productos4):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample57 == True):
        print (f'El articulo {Item4} fue eliminado exitosamente!')
    else:
        print (f'Error, el articulo {Item4} no existe')
        
print (f'-' * 20)

Productos5 = {
    "Laptop": 20,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 50,
    "Impresora": 180
}

def Ejercicio58(Diccionario):
    Diccionario_Sorted = dict(sorted(Diccionario.items(), key=lambda item : item[1]))
    Clave = next(iter(Diccionario_Sorted))
    Valor = Diccionario_Sorted[Clave]
    
    for indice, elemento in Diccionario_Sorted.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    return Clave, Valor

Sample58 = Ejercicio58(Productos5)

if (Productos5):
    Clave1, Valor1 = Sample58
    
    print (f'Articulo: {Clave1}')
    print (f'Precio: ${Valor1}')
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

Limite1 = 150

def Ejercicio59(Diccionario, Num):
    Diccionario_Sorted = dict(sorted(Diccionario.items(), key=lambda item : item[1]))
    for indice, elemento in Diccionario_Sorted.items():
        if (elemento > Num):
            return indice
        else:
            continue
        
    return None

Sample59 = Ejercicio59(Ventas1, Limite1)

if (len(Ventas1) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample59 is None):
        print (f'Error, no se ha encontrado una venta que supere el limite')
    else:
        print (f'El dia que tuvimos ventas que superaron al limite ${Limite1} fue {Sample59}')
        
print (f'-' * 20)

Productos6 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio60(Diccionario, Precio):
    Contador = 0
    
    for valor in Diccionario.values():
        if (valor > Precio):
            Contador += 1
        else:
            continue
        
    return Contador

Limite2 = 2000

Sample60 = Ejercicio60(Productos6, Limite2)

if (Productos6):
    if (Sample60):
        print (f'La cantidad de articulos cuyo valor supera el limite es {Sample60}')
    else:
        print (f'Error, no hay ningun producto cuyo valor supere el limite')
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

def Ejercicio61(Diccionario):
    if (len(Diccionario) == 0):
        return None
    else:
        Acumulador = 0
        
        for Valor in Diccionario.values():
            Acumulador += Valor
            
        return Acumulador

Sample61 = Ejercicio61(Ventas2)

if (Sample61 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample61):
        print (f'La suma de las ventas totales es ${Sample61}')
    else:
        print (f'Error, no hay montos que sumar')
        
print (f'-' * 20)

Ventas3 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio62(Diccionario, Num):
    Acumulador = 0
    
    for Valor in Diccionario.values():
        if (Valor > Num):
            Acumulador += Valor
        else:
            continue
        
    return Acumulador
    
Limite3 = 700    

Sample62 = Ejercicio62(Ventas3, Limite3)

if (len(Ventas3) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample62):
        print (f'La suma de los montos superiores a ${Limite3} es ${Sample62}')
    else:
        print (f'Error, no hay montos de ventas superiores al limite')
        
print (f'-' * 20)

Productos7 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio63(Diccionario, Num):
    Contador = 0
    Acumulador = 0
    for _, Valor in Diccionario.items():
        if (Valor > Num):
            Contador += 1
            Acumulador += Valor
        else:
            continue
        
    return Contador, Acumulador

Limite4 = 2000

Sample63 = Ejercicio63(Productos7, Limite4)

if (not Productos7):
    print (f'Error, el diccionario esta vacio')
else:
    Contador2, Acumulador2 = Sample63
    
    if (Contador2  and Acumulador2):
        print (f'La cantidad de productos que superan el limite es {Contador2}')
        print (f'La suma de los productos que superan el limite es {Acumulador2}')
    else:
        print (f'Error, no hay articulos que superen el limite')
        
print (f'-' * 20)

Productos8 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio64(Diccionario, Num):
    Diccionario_Sorted = dict(sorted(Diccionario.items(), key=lambda item : item[1]))
    for clave, valor in Diccionario_Sorted.items():
        if (valor > Num):
            return clave, valor
        else:
            continue
            
    return None
    
Limite5 = 2000

Sample64 = Ejercicio64(Productos8, Limite5)

if (len(Productos8) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample64 is None):
        print (f'Error, no hay ningun precio que supere el limite')
    else:
        Clave2, Valor2 = Sample64
        print (f'Articulo Nombre: {Clave2}')
        print (f'Articulo Precio: ${Valor2}')
        
print (f'-' * 20)

Lista_Lenguaje1 = ["python", "java", "python", "c++", "java", "python", "go", "c++", "python"]

def Ejercicio65(Lista):
    Diccionario_Vacio = dict({"python" : 0, "java" : 0, "c++" : 0, "go" : 0})
    for elemento in Lista:
        if (elemento in Diccionario_Vacio):
            Diccionario_Vacio[elemento] += 1
        else:
            continue
        
    return Diccionario_Vacio

Sample65 = Ejercicio65(Lista_Lenguaje1)

if (len(Lista_Lenguaje1) == 0):
    print (f'La lista esta vacia')
else:
    Sample65_Sorted = dict(sorted(Sample65.items(), key=lambda item : item[1]))
    Sample65_Sorted_Min = min(Sample65_Sorted.items(), key=lambda item : item[1])
    Sample65_Sorted_Max = max(Sample65_Sorted.items(), key=lambda item : item[1])
    print (f'{Sample65}')
    print (f'{Sample65_Sorted}')
    print (f'{Sample65_Sorted_Min}')
    print (f'{Sample65_Sorted_Max}')
    
print (f'-' * 20)

Diccionario_Anidado1 = {
    'Usuario1' : {
        'Nombre' : "Erick",
        'Edad' : 37,
        'Votante' : True
    },
    'Usuario2' : {
            'Nombre' : "Carmelo",
            'Edad' : 55,
            'Votante' : False
        }
}

for Nivel1_Clave, Nivel1_Valor in Diccionario_Anidado1.items():
    for Nivel2_Clave, Nivel2_Valor in Nivel1_Valor.items():
        print (f'{Nivel2_Clave} : {Nivel2_Valor}')
        
print (f'-' * 20)

Diccionario5X = {
    'Nombre' : 'Erick',
    'Edad' : 37,
    'Votante' : not True
}

Diccionario6X = dict({
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
})

Diccionario7X = {
    'Usuario1' : {
        'Nombre' : "Erick",
        'Edad' : 37,
        'Votante' : True
    },
    'Usuario2' : {
            'Nombre' : "Carmelo",
            'Edad' : 55,
            'Votante' : False
        }
}

for clave, valor in Diccionario5X.items():
    print (f'{clave} : {valor}')
    
print (f'-' * 20)

for clave, valor in Diccionario6X.items():
    for indice, elemento in enumerate(valor, start=1):
        print (f'{indice} : {elemento}')
        
print (f'-' * 20)

for Nivel1_Clave, Nivel1_Valor in Diccionario7X.items():
    for Nivel2_Clave, Nivel2_Valor in Nivel1_Valor.items():
        print (f'{Nivel2_Clave} : {Nivel2_Valor}')
        
print (f'-' * 20)

Diccionario8X = {
    "ana": {"edad": 25, "ciudad": "Quito"},
    "luis": {"edad": 30, "ciudad": "Guayaquil"}
}

def Ejercicio66(Diccionario, Usuario, Elemento):
    Ubicado1 = Diccionario.get(Usuario)
    
    if (Ubicado1 is None):
        return (False, 'Error, el nombre es incorrecto')
    else:
        Ubicado2 = Ubicado1.get(Elemento)
        if (Ubicado2 is None):
            return (not True, 'Error, el campo es incorrecto')
        else:
            return (True, 'Correcto, tanto nombre como campo aparecen en el diccionario')

Nombre1 = 'luis'
Campo1 = 'votante'

Sample66 = Ejercicio66(Diccionario8X, Nombre1, Campo1)

if (len(Diccionario8X) == 0):
    print (f'El diccionario esta vacio')
else:
    if (Sample66 == True):
        print (f'{Sample66}')
    else:
        print (f'{Sample66}')
        
print (f'-' * 20)

Datos2 = {
    "ana":  {"edad": 25, "ciudad": "Quito"},
    "luis": {"edad": 30, "ciudad": "Guayaquil"}
    }

Usuario4 = 'ana'
Campo4 = 'votante'
Nuevo_Valor4 = '90,000'

def Ejercicio67(Diccionario, Persona, Elemento, Nuevo):
    Ubicado1 = Diccionario.get(Persona)
    if (Ubicado1 is not None):
        Ubicado2 = Ubicado1.get(Elemento)
        if (Ubicado2 is None):
            return (False, 'Error, el campo no existe')
        else:
            Diccionario[Persona][Elemento] = Nuevo
            return Diccionario
    else:
        return (not True, 'Error, el usuario no existe')

if (len(Datos2) == 0):
    print (f'El diccionario esta vacio')
else:
    Sample67 = Ejercicio67(Datos2, Usuario4, Campo4, Nuevo_Valor4)
    if (Sample67 == False):
        print (f'{Sample67}')
    else:
        print (f'{Sample67}')
        
print (f'-' * 20)

Diccionario_Lenguaje1 = {"python": 2, "java": 2, "c++": 2, "go": 1}

def Ejercicio68(Diccionario):
    Diccionario_Sorted = dict(sorted(Diccionario.items(), key=lambda item : item[1]))
    clave = next(iter(Diccionario_Sorted))
    valor = Diccionario_Sorted[clave]
    
    for indice, elemento in Diccionario_Sorted.items():
        Lista_Repetidos = []
        if (elemento > valor):
            clave = indice
            valor = elemento
        else:
            continue
        
    for indice, elemento in Diccionario_Sorted.items():
        if (elemento == valor):
            Lista_Repetidos.append(indice) #type: ignore
        else:
            continue
        
    if (len(Lista_Repetidos) > 1): #type: ignore
        return Lista_Repetidos #type: ignore
    else:
        return clave

if (Diccionario_Lenguaje1):
    Sample68 = Ejercicio68(Diccionario_Lenguaje1)
    print (f'{Sample68}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Lista_Elementos14 = list(["manzana", "zanahoria", "kiwi", "pera", "tomate"])

Canastas1 = {
    "frutas": [],     # se llenará con frutas
    "verduras": [],   # se llenará con verduras
    "otros": []       # se llenará con lo que no sea fruta ni verdura
}

def Ejercicio69(Diccionario, Lista):
    if (len(Diccionario) == 0 or len(Lista) == 0):
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

Sample69 = Ejercicio69(Canastas1, Lista_Elementos14)

if (Sample69 is None):
    print (f'Error, el diccionario o la lista estan vacias')
else:
    if (Sample69):
        print (f'{Sample69}')
    else:
        print (f'Error, el diccionario sigue vacio')

print (f'-' * 20)

Lista_Elementos15 = [("fruta","manzana"), ("verdura","zanahoria"), ("fruta","pera"), ("fruta","banana"), ("verdura","tomate")]

def Ejercicio70(Lista):
    Diccionario_Vacio = dict({})
    
    if (len(Lista) == 0):
        return None
    else:
        for indice, elemento in Lista:
            if (indice not in Diccionario_Vacio):
                Diccionario_Vacio[indice] = []
                Diccionario_Vacio[indice].append(elemento)
            else:
                Diccionario_Vacio[indice].append(elemento)
                
        return Diccionario_Vacio

Sample70 = Ejercicio70(Lista_Elementos15)

if (Sample70 is None):
    print (f'Error, la lista esta vacia')
else:
    for indice, elemento in Sample70.items():
        for elemento2 in enumerate(elemento):
            print (f'{elemento2[0]} : {elemento2[1]}')
            
print (f'-' * 20)

'''def Ejercicio71(Numero):
    Resultado = 20 + Numero * 2
    return Resultado

Sample71 = Ejercicio71(PEPE.Flotante1)

if (Sample71):
    print (f'El resultado de la operacion es {Sample71}')
else:
    print (f'Error, el resultado es incorrecto')
    
print (f'-' * 20)

Resultado1 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado1}')

print (f'-' * 20)

def Ejercicio72(Texto):
    Cadena = Texto.replace(' ', '')
    
    if (isinstance(Cadena, (str))):
        if (Cadena.isalpha()):
            print (f'Lo que ingresaste es una cadena de texto')
        else:
            print (f'Error2 esto no es un texto')
    else:
        print (f'Error1 esto no es un texto')

Sample72 = Ejercicio72(PEPE.Flotante3)

print (f'-' * 20)

def Ejercicio73(Cadena):
    Lista_Cadena = Cadena.split(' ')
    
    for indice, elemento in enumerate(Lista_Cadena, start=1):
        print (f'{indice} : {elemento}')
        
    print (f'La cantidad de palabras digitadas es {Lista_Cadena.__len__()}')

Sample73 = Ejercicio73(PEPE.Flotante4)

print (f'-' * 20)'''

'''Lista_Estudiantes = []

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio(Lista):
    for elemento in range(0, Contador):
        Estudiante = input(f'Ingrese el nombre del estudiante {elemento + 1}: ')
        Lista.append(Estudiante)
        
    return Lista

Sample71 = Colegio(Lista_Estudiantes)

if (Sample71):
    print (f'La lista de estudiantes es {Sample71}')
else:
    print (f'Error, la lista de estudiantes esta vacia')'''
    
'''Lista_Estudiantes = list([])

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio(Lista):
    for elemento in range(0, Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
        
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda num : num[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes es {Menore} y su edad es {Lista[0][1]} años')
    print (f'El mayor de los estudiantes es {Mayore} y su edad es {Lista[-1][1]} años')

Sample71 = Colegio(Lista_Estudiantes)'''

Paises = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}

def Ejercicio71(Diccionario, Elemento):
    Ubicado = Diccionario.get(Elemento)
    if (Ubicado is None):
        return False
    else:
        return Ubicado

Codigo = 'op'

Sample71 = Ejercicio71(Paises, Codigo)

if (Paises):
    if (Sample71 == False):
        print (f'Error, el codigo ingresado no pertenece a ningun pais')
    else:
        print (f'El codigo {Codigo} pertenece al pais {Sample71}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

class Persona():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto1 = Persona('Erick')

print (f'Mi nombre es {Objeto1}')

print (f'-' * 20)

class Colores():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre
        
Lista_Colores = [
    Colores('Rojo'),
    Colores('Amarillo'),
    Colores('Azul')
]

print (f'La lista de colores es {Lista_Colores}')

print (f'-' * 20)

class Inventario():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto2 = Inventario()

Objeto2.Productos.append('Escritorio')
Objeto2.Productos.insert(1, 'Escoba')
Objeto2.Productos.extend(['Balon'])

print (f'La cantidad de elementos de la lista es {len(Objeto2)}')

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
    print (f'Error los objetos no son iguales')
    
print (f'-' * 20)

class Caja():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto5 = Caja(5)
Objeto6 = Caja(3)

print (f'El resultado de la sumatoria es {Objeto5 + Objeto6}')

print (f'-' * 20)

class Armario():
    def __init__(self):
        self.Ropa = [
            'Camisetas',
            'Zapatos',
            'Pantalones'
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
            'Donas',
            'Croissant'
        ]
        
    def __iter__(self):
        return iter(self.Panes)
        
Objeto8 = Panaderia()

for indice, elemento in enumerate(Objeto8, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

'''import requests

Diccionario_Api = dict({
    'Nombre' : ['Pistacho', 'Caramelo', 'Chocofresa'],
    'Indice' : [0, 1, 2]
})

print (f'-' * 20)

Unidad3 = requests.post('http://127.0.0.1:8000/grupo1/unidad2', json=(Diccionario_Api))
Unidad4 = Unidad3.json()

print (f'Agregado: {Unidad4}')
print (f'Status Code: {Unidad3.status_code}')

print (f'-' * 20)

Unidad5 = requests.put('http://127.0.0.1:8000/grupo1/unidad1', json=(Diccionario_Api))
Unidad6 = Unidad5.json()

print (f'Reemplazado: {Unidad6}')
print (f'Status Code: {Unidad5.status_code}')

print (f'-' * 20)

Unidad7 = requests.delete('http://127.0.0.1:8000/grupo1/unidad1', json=(Diccionario_Api))
Unidad8 = Unidad7.json()

print (f'Eliminado: {Unidad8}')
print (f'Status Code: {Unidad7.status_code}')

print (f'-' * 20)

Unidad1 = requests.get('http://127.0.0.1:8000/grupo1/unidad1')
Unidad2 = Unidad1.json()

print (f'{Unidad2}')
print (f'Status Code: {Unidad1.status_code}')'''

var6 = '3'

if (isinstance(var6, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, el numero no es entero')
    
if (var6.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, el numero no es entero')

if (var6.isdecimal()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, el numero no es entero')
    
try:
    Numero3 = float(var6)
    if (Numero3.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError as Errore1:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var7 = 3.5

if (isinstance(var7, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, lo que ingresaste no es decimal')
    
try:
    Numero4 = float(var7)
    if (Numero4.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except Exception as Errore2:
    print (f'Lo que ingresaste no es un numero -> {str(Errore2)}')
    
print (f'-' * 20)

var8 = 3.5

if (isinstance(var8, (int, float))):
    print (f'Lo ingresado es un numero entero o decimal')
else:
    print (f'Error de formato')
    
try:
    Numero5 = float(var8)
    if (Numero5.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except (ValueError, Exception):
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

Texto1_Version4 = re.sub(r'\!|\@', '', Texto1_Version3)

print (f'{Texto1_Version4}')

Texto1_Version5 = Texto1_Version4.title()

print (f'{Texto1_Version5}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv1 = 'C:\\Repo\\Store.csv'

Cargar_Csv1 = pd.read_csv(Ruta_Csv1)

print (f'{Cargar_Csv1.head()}')

print (f'-' * 20)

Fecha1 = '2026-04-01'

try:
    Fech1 = datetime.strptime(Fecha1, '%Y-%m-%d').date()
    Fech1_Formateada = pd.to_datetime(Fech1)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato invalido')
    exit()
    
Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrado1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()]

if (Encontrado1.empty):
    print (f'En esta fecha no hemos encontrado ventas')
else:
    print (f'Genial! hemos encontrado ventas en esta fecha {Fech1_Formateada}')
    
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'En la fecha {Fech1_Formateada}, el producto {Grupo1_Min} vendio {Grupo1_Min_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada}, el producto {Grupo1_Max} vendio {Grupo1_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que nos compraron en esta fecha fue {Grupo1.count()}')
    
    print (f'La cantidad de articulos vendidos en esta fecha fue de {Grupo1.sum()}')
    
    print (f'La media de productos vendidos en esta fecha fue de {round(Grupo1.mean(), 2)}')
    
    Grupo2 = Encontrado1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue de ${Grupo2.sum()}')
    
    Promedio1 = Grupo2.sum() / Grupo1.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio1, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Grupo2.mean(), 2)}')
    
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

print (f'-' * 20)

for elemento in Buscar1:
    print (f'{elemento}')
    
print (f'-' * 20)

import re

Texto3 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Metodo #1

Pattern2 = r'\!|\?|\.{2,}|\d{2,4}\-[0-9]{4,}'

Buscar2 = re.sub(Pattern2, '', Texto3)

print (f'{Buscar2}')

print (f'-' * 20)

import re

# Metodo #2

Pattern3 = r'[^a-zA-Z0-9\s]+'

Buscar3 = re.sub(Pattern3, '', Texto3)

print (f'{Buscar3}')

print (f'-' * 20)

import re

# Metodo #3

Texto3_temp1 = Texto3

Pattern4 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos1 = re.findall(Pattern4, Texto3)

print (f'{Correos1}')

for i, email in enumerate(Correos1, start=1):
    Texto3_temp1 = Texto3_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto3_temp1}')

Pattern5 = r'\!|\?|\.{2,}|[0-9]{1,4}\-\d{3,}'

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

Texto4_temp1 = Texto4

Pattern6 = r'[a-zA-Z0-9\.\/\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Correos2 = re.findall(Pattern6, Texto4)

print (f'{Correos2}')

for i, email in enumerate(Correos2, start=1):
    Texto4_temp1 = Texto4_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto4_temp1}')

Pattern7 = r'\!|\?'

Texto4_temp2 = re.sub(Pattern7, '', Texto4_temp1)

print (f'{Texto4_temp2}')

for i, email in enumerate(Correos2, start=1):
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

'''Lista_Promedio = []

Contador = 0

while (Contador < 3):
    while (True):
        Numero6 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numero7 = float(Numero6)
            if (Numero7.is_integer()):
                print (f'Lo que ingresaste es un numero entero')
                Lista_Promedio.append(Numero7)
                break
            else:
                print (f'Lo que ingresaste es un numero decimal')
                Lista_Promedio.extend([Numero7])
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador += 1
    
Promedio2 = sum(Lista_Promedio) / len(Lista_Promedio)

print (f'El promedio de las notas ingresadas es {round(Promedio2, 2)}')'''

import re

Texto5 = 'esto hola 123 es un @ texto cualquiera, vambabaos a ver hila si lo que acabamos de ingresar 2 sirve o hela! realmente no es 288 % necesario'

Buscar4 = re.search(r'acabamos', Texto5)

print (f'{Buscar4}')

Buscar5 = re.search(r'^esto', Texto5)
Buscar6 = re.search(r'o$', Texto5)

print (f'{Buscar5}')
print (f'{Buscar6}')

Buscar7 = re.findall(r'\d+', Texto5)

print (f'{Buscar7}')

Buscar8 = bool(re.fullmatch(r'esto hola 123 es un \@ texto cualquiera, vaamos a ver hila si lo que acabamos de ingresar 2 sirve o hela\! realmenaote no es 288 \% necesarioaoao', Texto5))

if (Buscar8 == True):
    print (f'El texto es exactamente igual')
else:
    print (f'Error, los textos no son iguales')
    
Buscar9 = re.findall(r'h.la', Texto5)

print (f'{Buscar9}')

'''
\D esto toma todo menos numeros
\d esto toma solo numeros
\s esto toma solamente espacios
\S esto toma todo menos espacios
\W esto solo toma caracteres especiales
\w todo menos caracteres especiales
+ 1 o mas 
* 0 o mas 
? 0 o 1
'''

Buscar10 = re.findall(r'\D', Texto5)
Buscar11 = re.findall(r'\s', Texto5)
Buscar12 = re.findall(r'\S', Texto5)
Buscar13 = re.findall(r'\W', Texto5)
Buscar14 = re.findall(r'\w', Texto5)

print (f'{Buscar10}')

print (f'-' * 20)

print (f'{Buscar11}')

print (f'-' * 20)

print (f'{Buscar12}')

print (f'-' * 20)

print (f'{Buscar13}')

print (f'-' * 20)

print (f'{Buscar14}')

print (f'-' * 20)

Buscar15 = re.findall(r'\d{3}\s\W', Texto5)

print (f'{Buscar15}')

Buscar16 = re.findall(r'(ba){2,4}', Texto5)

print (f'{Buscar16}')

Buscar17 = re.findall(r'ao+', Texto5)

print (f'{Buscar17}')

Buscar18 = re.findall(r'\d{2,4}|h.la', Texto5)

print (f'{Buscar18}')

import re

Texto6 = 'ericksuper80@hotmail.com'

Pattern8 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)$'

Buscar18 = bool(re.fullmatch(Pattern8, Texto6))

if (Buscar18 == True):
    print (f'El correo tiene el formato correcto')
else:
    print (f'Error, el correo tiene un formato incorrecto')
    
print (f'-' * 20)

import re

Pattern9 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z0-9]+\.[a-z]{2,}$'

Buscar19 = bool(re.match(Pattern9, Texto6))

if (Buscar19 == True):
    print (f'El correo tiene el formato correcto')
else:
    print (f'Error, el correo tiene un formato incorrecto')
    
print (f'-' * 20)

import re

Texto7 = '38'

Pattern10 = r'([0-9]|[12][0-9]|3[01])'

Buscar20 = bool(re.fullmatch(Pattern10, Texto7))

if (Buscar20 == True):
    print (f'El numero se encuentra entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

Texto8 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern11 = r'\d{2}\/[0-9]{1,3}\/\d{3,}'

Replacement11 = 'XX/XX/XXXX'

Buscar21 = re.sub(Pattern11, Replacement11, Texto8)

print (f'{Buscar21}')

Pattern12 = r'\+\d{1}\-[0-9]{2,4}\-\d{3,}\-[0-9]{1,5}'

Replacement12 = 'PH0N3_NVMB3R'

Buscar22 = re.sub(Pattern12, Replacement12, Buscar21)

print (f'{Buscar22}')

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

Pattern13 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Buscar23 = re.findall(Pattern13, Texto9)

for elemento in enumerate(Buscar23):
    print (f'{elemento[0]} : {elemento[1]}')
    
print (f'-' * 20)

import re

Texto10 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# version 1

Pattern14 = r'\!|\?|\.{2,}|[0-9]{1,4}\-\d{4,}'

Buscar24 = re.sub(Pattern14, '', Texto10)

print (f'{Buscar24}')

print (f'-' * 20)

# version 2

import re

Pattern15 = r'[^a-zA-Z0-9\s]+'

Buscar25 = re.sub(Pattern15, '', Texto10)

print (f'{Buscar25}')

print (f'-' * 20)

# version 3

import re

Texto10_temp1 = Texto10

Pattern16 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos3 = re.findall(Pattern16, Texto10)

print (f'{Correos3}')

for i, email in enumerate(Correos3, start=1):
    Texto10_temp1 = Texto10_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto10_temp1}')

Pattern17 = r'\!|\?|\.{2,}|\d{1,4}\-[0-9]{4,}'

Texto10_temp2 = re.sub(Pattern17, '', Texto10_temp1)

print (f'{Texto10_temp2}')

for i, email in enumerate(Correos3, start=1):
    Texto10_temp2 = Texto10_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto10_temp2}')

print (f'-' * 20)

var9 = 'hola'

if (isinstance(var9, (float))):
    print (f'Esto es un numero decimal')
else:
    print (f'Error, lo que enviaste no es un numero decimal')
    
try:
    Numero6 = float(var9)
    if (Numero6.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var10 = '3'

if (isinstance(var10, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')
    
if (var10.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')

if (var10.isdecimal()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')
    
try:
    Numero7 = float(var10)
    if (Numero7.is_integer()):
        print (f'Esto es un numero entero')
    else:
        print (f'Esto es un numero decimal')
except Exception:
    print (f'Error, esto no es un numero')
    
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

Texto11_Version5 = Texto11_Version4.title()

print (f'{Texto11_Version5}')

print (f'-' * 20)

var11 = 'hola'

try:
    Resultado = 12 + var11 #type: ignore
except TypeError as Errore3:
    print (f'Error, no se puede realizar la operacion -> {str(Errore3)}')
    
Lista_Exception1 = ['Erick', 'Josue', 'karlita']

Diccionario_Exception1 = {
    'Nombre' : Lista_Exception1
}

try:
    Lista_Exception1.remove('Roxana')
except ValueError:
    print (f'Error, este elemento no existe')
    
try:
    Snake_Case1, Snake_Case2, Snake_Case3, Snake_Case4 = Lista_Exception1
except (ValueError, Exception):
    print (f'Este desempaquetado es incorrecto')
    
import pandas as pd
from datetime import datetime
    
Fecha2 = 'hola-04-01'

try:
    Fech2 = datetime.strptime(Fecha2, '%Y-%m-%d').date()
    Fech2_Formateado = pd.to_datetime(Fech2)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'La fecha es invalida, formato incorrecto')
    
try:
    Resultado = 'hola' * '3' #type: ignore
except TypeError:
    print (f'Error de formato, estos valores no se pueden evaluar')
    
try:
    print (f'El valor es {Lista_Exception1.index("Roxana")}')
except ValueError:
    print (f'Error, este indice no existe')
    
print (f'-' * 20)
    
try:
    # print (f'El elemento es {Lista_Exception1.index("Roxana")}')
    
    # print (f'El resultado de la operacion es {6 + "Hola"}') #type: ignore
    
    # print (f'El resultado de la operacion es {12 / 0}')
    
    # print (f'El elemento es {Lista_Exception1[6]}')
    
    # print (f'El elemento es {Diccionario_Exception1["Edad"]}')
    
    with open ('C:\\Repo\\HolaMuno.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        Docu.close()
except ValueError:
    print (f'Esto es un ValueError')
except TypeError:
    print (f'Esto es un TypeError')
except ZeroDivisionError:
    print (f'Esto es un ZeroDivisionError')
except IndexError:
    print (f'Esto es un IndexError')
except KeyError:
    print (f'Esto es un KeyError')
except Exception:
    print (f'Esto es un Exception')
    
print (f'-' * 20)

var12 = 3.5

try:
    Resultado = var12.lower() #type: ignore
    print (f'Esto es un texto')
except AttributeError:
    print (f'Error, esto no es un texto')
    
print (f'-' * 20)

def Exception1(Numero):
    try:
        Numero8 = float(Numero)
        if (Numero8.is_integer()):
            print (f'El numero es entero')
        else:
            print (f'El numero es decimal')
    except (ValueError, Exception):
        print (f'Error, lo que ingresaste no es un numero')

Exception1('hola')

print (f'-' * 20)

def Exception2(Num1:int, Num2:int) -> int: #type: ignore
    '''Docstring, en esta funcion se suman dos argumentos y se retorna el resultado'''
    try:
        Resultado = Num1 + Num2
        print (f'El resultado de la operacion es {Resultado}')
    except TypeError as Errore4:
        print (f'Error, ambos elementos deben ser numeros -> {str(Errore4)}')

Exception2(12, 'hola') #type: ignore

print (f'{help(Exception2)}')

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        print (f'El resultado de la division es {round(Num1 / Num2, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(7, 3)

print (f'-' * 20)

def Exception4(Indice):
    try:
        print (f'El elemento con indice {Indice} es {Lista_Exception1[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(3)

print (f'-' * 20)

Diccionario_Exception2 = {
    'Nombre' : "Erick",
    'Edad' : 37
}

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception2[Llave]}')
    except KeyError as Errore5:
        print (f'Error, la llave esta fuera de rango -> {str(Errore5)}')

Exception5('Votante')

print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
    Documento_SobreEscribir = Docu.write(f'Oso')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Linea = Docu.readline()
        print (f'{Documento_Linea}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo es incorrecto')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nSalamandra'])
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        print (f'{Documento_Lineas}')
        Docu.close()
except ValueError:
    print (f'Error, el archivo es incorrecto')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nAvestruz')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nHiena Pequeña', f'\nHiena Mediana', f'\nHiena Grande'])
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Linea = Docu.readline()
        print (f'{Documento_Linea}')
        Docu.close()
except ValueError:
    print (f'Error, el archivo es incorrecto')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke1"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke2"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke3"]}')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        print (f'{Documento_Lineas}')
        Docu.close()
except ValueError:
    print (f'Error, el archivo es incorrecto')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    for indice, elemento in PEPE.Diccionario_Animal.items():
        for otro in elemento[:]:
            Documento_Agregar = Docu.write(f'\n{otro.upper()}')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Leer = Docu.read()
        print (f'{Documento_Leer}')
        Docu.close()
except ValueError:
    print (f'Error, el archivo es incorrecto')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\n'])
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Set_Conjunto_Poke1)])
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        # print (f'{Documento_Lineas}')
        for indice, elemento in enumerate(Documento_Lineas[0:None], start=1):
            if (elemento.strip() == 'Vaporeon'):
                print (f'Este es mi pokemon favorito y es de hielo - agua')
                break
            else:
                continue
        Docu.close()
except Exception:
    print (f'Error, el archivo es incorrecto')
    
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

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame1])

print (f'{Data_Frame1}')

print (f'-' * 20)

Data_Frame_Concatenate_Age1 = Data_Frame_Concatenate['Edad']
Data_Frame_Concatenate_Age2 = Data_Frame_Concatenate['Edad'].sum()

print (f'{Data_Frame_Concatenate_Age1}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate_Age2}')

print (f'-' * 20)

print (f'De las edades, la menor es {Data_Frame_Concatenate_Age1.min()}')
print (f'De las edades, la menor es {Data_Frame_Concatenate_Age1.max()}')

print (f'{Data_Frame_Concatenate_Age1.info()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Unidad1 = elemento['Nombre']
    Unidad2 = elemento['Edad']
    
    print (f'Mi nombre es {Unidad1} y mi edad {Unidad2} años')
    
print (f'-' * 20)

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()
Grupo3_Min_Cant = Grupo3.min()
Grupo3_Max_Cant = Grupo3.max()

print (f'Del dataframe el menor es {Grupo3_Min} y su edad es {Grupo3_Min_Cant} años')
print (f'Del dataframe el mayor es {Grupo3_Max} y su edad es {Grupo3_Max_Cant} años')

print (f'La cantidad de personas en el dataframe es {Grupo3.count()}')

print (f'Si sumo todas las edades me da el numero {Grupo3.sum()}')

Promedio2 = Grupo3.sum() / Grupo3.count()

print (f'El promedio de edades es {round(Promedio2, 2)}')
print (f'El promedio de edades es {round(Grupo3.mean(), 2)}')

Data_Frame_Concatenate['TOTALITO'] = Data_Frame_Concatenate['Edad']  + 500

Grupo4 = Data_Frame_Concatenate.groupby('Nombre')['TOTALITO'].sum()
Grupo4_Min = Grupo4.idxmin()
Grupo4_Max = Grupo4.idxmax()
Grupo4_Min_Cant = Grupo4.min()
Grupo4_Max_Cant = Grupo4.max()

print (f'De las nuevas edades, el menor es {Grupo4_Min} y su nueva edad es {Grupo4_Min_Cant} años')
print (f'De las nuevas edades, el mayor es {Grupo4_Max} y su nueva edad es {Grupo4_Max_Cant} años')

print (f'La cantidad de elementos en el dataframe es {Grupo4.count()}')

print (f'La suma de las nuevas edades es {Grupo4.sum()}')

Promedio3 = Grupo4.sum() / Grupo4.count()

print (f'El promedio de edades es {round(Promedio3, 2)}')
print (f'El promedio de edades es {round(Grupo4.mean(), 2)}') 

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

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenate)

plt.show()'''

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'-' * 20)

Filas, Columnas = Data_Frame_Concatenate.shape

print (f'La cantidad de Filas del dataframe es {Filas}')
print (f'La cantidad de Columnas del dataframe es {Columnas}')

Elemento1 = Data_Frame1.loc[0, 'Nombre']
Elemento2 = Data_Frame1.loc[1, 'Edad']
Elemento3 = Data_Frame1.loc[2, 'Votante']
Elemento4 = Data_Frame1.loc[1, :]
Elemento5 = Data_Frame1.loc[:,  'Votante']

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

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tiquete')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tiquete', usecols='E:K')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tiquete', usecols='E:K', nrows=1)

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

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending.head()}')

print (f'-' * 20)

Grupo5 = Cargar_Excel3_Sorted.groupby('tres')['cinco'].sum()
Grupo5_Min = Grupo5.idxmin()
Grupo5_Max = Grupo5.idxmax()
Grupo5_Min_Cant = Grupo5.min()
Grupo5_Max_Cant = Grupo5.max()

print (f'Del excel el menor es {Grupo5_Min} con una edad de {Grupo5_Min_Cant} años')
print (f'Del excel el menor es {Grupo5_Max} con una edad de {Grupo5_Max_Cant} años')

print (f'La cantidad de personas del excel es {Grupo5.count()}')

print (f'La suma de las edades es {Grupo5.sum()}')

Promedio4 = Grupo5.sum() / Grupo5.count()

print (f'El promedio de las edades es {round(Promedio4, 2)}')
print (f'El promedio de las edades es {round(Grupo5.mean(), 2)}')

print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        # print (f'{Documento_Lineas}')
        for indice, elemento in enumerate(Documento_Lineas, start=1):
            if (elemento.strip() == 'HoRMIga'.upper()):
                print (f'The name of this animal is ant in english')
                break
            else:
                continue
        Docu.close()
except Exception:
    print (f'Error, el archivo es incorrecto')
    
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

for i in range(0, len(Array0)):
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
print (f'{Array1[1]}')

print (f'{Array1[::2]}')
print (f'{Array1[::3]}')
print (f'{Array1[:2]}')
print (f'{Array1[2:]}')
print (f'{Array1[1:2]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 > 2]}')

print (f'-' * 20)

Array2 = np.array([[1, 2, 3], [1, 2, 3]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 0]}')

print (f'{Array2[1, ::2]}')
print (f'{Array2[1, ::3]}')
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

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[1, 0:None])
Sumita4 = np.sum(Array2_Sorted[1, :])

print (f'Acomodados: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

print (f'La sumita es {Sumita1}')
print (f'La sumita es {Sumita2}')
print (f'La sumita es {Sumita3}')
print (f'La sumita es {Sumita4}')

print (f'-' * 20)

Array3 = np.array([[['e', 'i', 'k'], ['a', 'b', 'c']],       [['d', 'g', 'h'], ['j', 'l', 'n']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 0]}')

print (f'{Array3[1, 0, ::2]}')
print (f'{Array3[1, 1, ::3]}')
print (f'{Array3[0, 1, :2]}')
print (f'{Array3[0, 1, 2:]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[0, 1, 2:3]}')
print (f'{Array3[0, 0, 0:None]}')
print (f'{Array3[0, 0, :]}')
print (f'{Array3[Array3 == "g"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],               [[[6, 5, 4], [9, 8, 7]], [[2, 5, 8], [9, 1, 7]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 2]}')

print (f'{Array4[1, 0, 0, ::2]}')
print (f'{Array4[1, 1, 0, ::3]}')
print (f'{Array4[0, 1, 1, :2]}')
print (f'{Array4[0, 1, 1, 2:]}')
print (f'{Array4[1, 0, :, 0]}')
print (f'{Array4[0, 1, 1, 2:3]}')
print (f'{Array4[1, 1, 1, 0:None]}')
print (f'{Array4[1, 1, 1, :]}')
print (f'{Array4[Array4 >= 5]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[0, 1, 1, 0:None])
Sumita8 = np.sum(Array4_Sorted[0, 1, 1, :])

print (f'Sumita: {Sumita5}')
print (f'Sumita: {Sumita6}')
print (f'Sumita: {Sumita7}')
print (f'Sumita: {Sumita8}')

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

Array_Zero = np.zeros(shape=(2, 3))

print (f'{Array_Zero}')
print (f'{Array_Zero.ndim}') # 2
print (f'{Array_Zero.shape}') # 2x3
print (f'{Array_Zero.size}') # 6
print (f'{Array_Zero.dtype}') # int64
print (f'{Array_Zero[1, 1]}')

print (f'-' * 20)

Array_One = np.ones(shape=(2, 3))

print (f'{Array_One}')
print (f'{Array_One.ndim}')
print (f'{Array_One.shape}')
print (f'{Array_One.size}')
print (f'{Array_One.dtype}')
print (f'{Array_One[1, 2]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value=f'{PEPE.Diccionario_Animal['Nombres'][2]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 2]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(10), fill_value=f'Fuecoco')

Lista_Array1 = []

for elemento in Array_Gen2[:]:
    Lista_Array1.extend([str(elemento)])
    
print (f'{Array_Gen2}')
print (f'{type(Array_Gen2)}')
print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value=f'{Array4_Sorted[1, 0, 0, 2]}')

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[0, 2]}')

print (f'-' * 20)

Tupla_Array = ('Rojo', 'Verde', 'Azul',)
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({
    'Nombre' : ['Erick', 'Josue', 'Karlita']
})

Array_Gen4 = np.full(shape=(2, 3), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array['Nombre'][2])

print (f'{Array_Gen4}')
print (f'{Array_Gen5}')
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

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

Sumita9 = np.sum(Array_Random2_Sorted, axis=0)
Sumita10 = np.sum(Array_Random2_Sorted, axis=1)
Sumita11 = np.sum(Array_Random2_Sorted[0, 0:None])
Sumita12 = np.sum(Array_Random2_Sorted[0, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

print (f'-' * 20)

Matriz1 = np.array([8, 9, 14])
Matriz2 = np.array([2, 3, 7])

Matriz_Suma = Matriz1 + Matriz2
Matriz_Resta = Matriz1 - Matriz2
Matriz_Multiplicacion = Matriz1 * Matriz2
Matriz_Division_Baja = Matriz1 // Matriz2
Matriz_Division_Flotante = Matriz1 / Matriz2
Matriz_Exponente = Matriz1 ** Matriz2
Matriz_Modulo = Matriz1 % Matriz2

Array_Random1_Cien = Array_Random1 + 100

print (f'El resultado es {Matriz_Suma}')
print (f'El resultado es {Matriz_Resta}')
print (f'El resultado es {Matriz_Multiplicacion}')
print (f'El resultado es {Matriz_Division_Baja}')
print (f'El resultado es {Matriz_Division_Flotante}')
print (f'El resultado es {Matriz_Exponente}')
print (f'El resultado es {Matriz_Modulo}')
print (f'El resultado es {Array_Random1_Cien}')

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

Lista_Array2 = ['Erick', 'Josue', 'Karlita']

Array_Num9 = np.array(Lista_Array2)

print (f'{Array_Num9}')
print (f'{type(Array_Num9)}')
print (f'{Lista_Array2}')
print (f'{type(Lista_Array2)}')

print (f'-' * 20)

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Array6 = np.array([1, 2, 3])
Array7 = np.array([4, 5, 6])

Array_Concatenate = np.concatenate([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'-' * 20)

Array_Concatenate_Where = np.where(Array_Concatenate == 3)

print (f'{Array_Concatenate_Where}')

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

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

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

Array_Random3_Sorted = np.sort(Array_Random3)
Array_Random3_Sorted_Mean = np.mean(Array_Random3_Sorted)
Array_Random3_Sorted_Sum = np.sum(Array_Random3_Sorted)

print (f'Acomodado: {Array_Random3_Sorted}')
print (f'Media: {Array_Random3_Sorted_Mean}')
print (f'Sumatoria: {Array_Random3_Sorted_Sum}')

print (f'-' * 20)

Set_Conjunto_Sorteo1 = set({'Erick'})
Set_Conjunto_Sorteo1.add('Josue')
Set_Conjunto_Sorteo1.add('Karlita')

Set_Conjunto_Sorteo2 = {'Carmelo', 'Susanita', 'Roxana'}

Set_Conjunto_Sorteo1.update(Set_Conjunto_Sorteo2)

print (f'{Set_Conjunto_Sorteo1}')

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
    for elemento in range(0, 5):
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
    for elemento in range(len(PEPE.Lista_Numeros[:])):
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
    print (f'El experimento termina aqui')
    
print (f'-' * 20)

def Generadora3():
    for elemento in range(1, 5):
        if (elemento == 1):
            yield f'This is number one'
        elif (elemento == 2):
            yield f'This is number two'
        elif (elemento == 3):
            yield f'This is number three'
        elif (elemento == 4):
            yield f'This is number four'
        else:
            continue

Gen3 = Generadora3()

try:
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

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(2)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int) -> int:
        return Num1 + Num2
    
    return Sumatoria_Interna(3)

Variable_Sumatoria = Sumatoria_Externa(4)

print (f'El resultado de la sumatoria es {Variable_Sumatoria}')

if (PEPE.Par(Variable_Sumatoria) == True):
    print (f'El numero ingresado es par')
else:
    print (f'El numero ingresado es impar')
    
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
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(57)}')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        print (f'{Documento_Lineas}')
        Docu.close()
except FileNotFoundError as Errore4:
    print (f'Error, el archivo seleccionado no existe -> {str(Errore4)}')
    
def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla(3.5, 500, 'Koala', False)

print (f'{Funcion_Tupla(3.5, 500, 'Koala', False)}')
print (f'{Funcion_Tupla(3.5, 500, 'Koala', False)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla(3.5, 500, 'Koala', False))}')

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
    Nombre = 'Erick',
    Edad = 37,
    Votante = True
)

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

def Sumatoria_Dos(Nombre, *numeritos):
    return f'Mi nombre es {Nombre} y mi numero favorito es {sum(numeritos)}'

print (f'{Sumatoria_Dos(Saludar_Dos(), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

if (PEPE.Any_Par == True):
    print (f'Los numeros pares de la lista son {list(Anonima3)}')
    print (f'Los numeros pares de la lista son {PEPE.Lista_Par}')
else:
    print (f'No hay numeros pares en la lista')
    
print (f'El menor es {PEPE.Menor1}, {PEPE.Lista_Estudiantes[0][1]} años')
print (f'El mayor es {PEPE.Mayor1}, {PEPE.Lista_Estudiantes[-1][1]} años')

Diccionario_Numeral2 = dict({
    'Num1' : 7,
    'Num2' : 3,
    'Num3' : 1,
    'Num4' : 6,
    'Num5' : 2
})

Diccionario_Numeral2_Sorted = dict(sorted(Diccionario_Numeral2.items(), key=lambda item : item[1]))

Diccionario_Numeral2_Sorted_Min = min(Diccionario_Numeral2.items(), key=lambda item : item[1])
Diccionario_Numeral2_Sorted_Max = max(Diccionario_Numeral2.items(), key=lambda item : item[1])

print (f'{Diccionario_Numeral2}')
print (f'{Diccionario_Numeral2_Sorted}')
print (f'{Diccionario_Numeral2_Sorted_Min}')
print (f'{Diccionario_Numeral2_Sorted_Max}')

print (f'-' * 20)

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')
print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda(*args) - 42
        
    return Tercera

@Primera
def Operacion(Num:int) -> int:
    Local = Num
    return PEPE.GLOBAL + Local

print (f'El resultado de la operacion es {Operacion(12)}')

def Externa(Nombre):
    def Interna(Apellido):
        return f'{Nombre} {Apellido}'
    
    return Interna('PEREZ GUTIERREZ')

print (f'Mi nombre es {Externa('ERICK JOSUE')}')

def Closure_Externo():
    Lista_Closure = list([])
    def Closure_Interno(x):
        Lista_Closure.append(x)
        
        return Lista_Closure
    
    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(30)}')
print (f'{Variable_Closure(58)}')

print (f'-' * 20)

def Closure_Crear_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y
    
    return Closure_Multiplicador

Mult1 = Closure_Crear_Multiplicador(2)
Mult2 = Closure_Crear_Multiplicador(3)

print (f'El multiplicador es {Mult1(100)}')
print (f'El multiplicador es {Mult2(100)}')

print (f'-' * 20)

def Filtrador(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    Anonima = filter(lambda Num : Num % 2 != 0, Lista)
    Lista_Impar = [num for num in Lista if num % 2 != 0]
    
    if (Any_Impar == True):
        print (f'Los impares de la lista son {list(Anonima)}')
        print (f'Los impares de la lista son {Lista_Impar}')
    else:
        print (f'Error, la lista no tiene elementos impares')

Filtrador(PEPE.Lista_Numeros)

print (f'-' * 20)

Estudiantes = ['Erick', 50]

Lista_Estudiantes = list([])

Lista_Estudiantes.append(Estudiantes)

Estudiantes = ['Roxana', 26]

Lista_Estudiantes.append(Estudiantes)

print (f'{Lista_Estudiantes}')

for indice, elemento in Lista_Estudiantes:
    print (f'{indice} : {elemento}')
    
Lista_Estudiantes.sort(key= lambda Num : Num[1])

Menor2 = Lista_Estudiantes[0][0]
Mayor2 = Lista_Estudiantes[-1][0]

print (f'{Lista_Estudiantes}')
print (f'{Menor2}')
print (f'{Mayor2}')

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'>>>>> ANTES')
        Segunda()
        print (f'<<<<< DESPUES')
        
    return Tercera

@Primera
def Saludar4():
    print (f'Hola Mundo')
    
Saludar4()

def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda(*args) - 80
        
    return Tercera

@Primera
def Sumatoria3(Num1, Num2=80):
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(2)}')

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonathan'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)
        
    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    return f'Mi nombre es {Nombre} {Apellido}'

print (f'{Usuario2("Erick", "Perez")}')

print (f'-' * 20)

from Module_Own import Pokemon1 as Poke1

Objeto9 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')

Objeto9.Mostrar()

print (f'Actualmente tengo {Objeto9.Cantidad} {Objeto9.Nombre}s')

if (Objeto9.Catched == True):
    print (f'Felicidades, atrapaste un pokemon')
else:
    print (f'Oh no!!!, mejor suerte la proxima vez')
    
print (f'-' * 20)

Objeto10 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto10.Mostrar()

print (f'Actualmente tengo {Objeto10.Cantidad} {Objeto10.Nombre}s')

if (Objeto10.Catched == True):
    print (f'Felicidades, atrapaste un pokemon')
else:
    print (f'Oh no!!!, mejor suerte la proxima vez')
    
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

from Module_Own import Pokemon2 as Poke2

Objeto13 = Poke2('Tagedemaru', 'Electrico', 'Voltio Cruel')
Objeto14 = Poke2('Cofin', 'Veneno', 'Pantalla De Humo')

Objeto13.Mostrar()

print (f'Yo tengo {Objeto13.Cantidad} {Objeto13.Nombre}s')

if (Objeto13.Catched == True):
    print (f'Felicidades, atrapaste un pokemon')
else:
    print (f'Oh no!!!, mejor suerte la proxima vez')
    
print (f'-' * 20)

Objeto14.Mostrar()

print (f'Yo tengo {Objeto14.Cantidad} {Objeto14.Nombre}s')

if (Objeto14.Catched == True):
    print (f'Felicidades, atrapaste un pokemon')
else:
    print (f'Oh no!!!, mejor suerte la proxima vez')
    
print (f'-' * 20)
    
class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto15 = Poke_Kid2('Lapras', 'Hielo', 'Rompe Olas', 'Hada')

Poke2.Mostrar(Objeto15)
Objeto15.Mostrar()

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
        
Objeto16 = Perro('Terry', 6, 11, 'Doberman', 'Obesidad')

Veterinaria.Mostrar(Objeto16)
Objeto16.Mostrar()

print (f'-' * 20)

class Gato(Veterinaria):
    def __init__(self, Nombre, Peso, Edad, Color, Paciente):
        super().__init__(Nombre, Peso, Edad)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto17 = Gato('Messi', 2.8, 1.5, 'Gris/Amarillo', 'No')

Veterinaria.Mostrar(Objeto17)
Objeto17.Mostrar()

print (f'-' * 20)

class Pajaro(Veterinaria):
    def __init__(self, Nombre, Peso, Edad, Especie, Habla):
        super().__init__(Nombre, Peso, Edad)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto18 = Pajaro('Polly', 0.4, 31, 'Papagayo', 'Si')

Veterinaria.Mostrar(Objeto18)
Objeto18.Mostrar()

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
        
Objeto19 = Paladin(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto19.Mostrar()
Atacante.Mostrar(Objeto19)
Defensor.Mostrar(Objeto19)

print (f'-' * 20)

Clase_Hija1 = issubclass(Poke_Kid2, Poke2)

print (f'{Clase_Hija1}')

Clase_Hija2 = issubclass(Poke_Kid2, Poke1)

print (f'{Clase_Hija2}')

print (f'-' * 20)

Instancia1 = isinstance(Objeto19, Paladin)
Instancia2 = isinstance(Objeto19, Atacante)
Instancia3 = isinstance(Objeto19, Defensor)

print (f'{Instancia1}')
print (f'{Instancia2}')
print (f'{Instancia3}')

print (f'-' * 20)

class A1():
    def Mostrar(self):
        print (f'Hola clase A1')
        
class E1():
    def Mostrar(self):
        print (f'Hola clase E1')
        
class B1(E1):
    def Mostrar(self):
        print (f'Hola clase B1')
        
class C1(A1):
    def Mostrar(self):
        print (f'Hola clase C1')
        
class D1(B1, C1):
    def Mostrar(self):
        print (f'Hola clase D1')
        
Objeto20 = D1()

A1.Mostrar(Objeto20)
B1.Mostrar(Objeto20)
C1.Mostrar(Objeto20)
Objeto20.Mostrar()
E1.Mostrar(Objeto20)

print (f'-' * 20)

class Efectivo():
    def Pagar(self):
        print (f'El pago se realizo con Efectivo')
        
class Tarjeta():
    def Pagar(self):
        print (f'El pago se realizo con Tarjeta')
        
class Cripto():
    def Pagar(self):
        print (f'El pago se realizo con Cripto')
        
Objeto21 = Cripto()
Objeto22 = Tarjeta()
Objeto23 = Efectivo()

Objeto21.Pagar()
Objeto22.Pagar()
Objeto23.Pagar()

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
    def Dinero(self, Nuevo):
        self.__Saldo = Nuevo
        
    def Mostrar(self):
        print (f'Su saldo a la fecha es de ${self.__Saldo}')
        
Objeto24 = Cuenta_Bancaria(100)
Objeto24.Depositar(25)
Objeto24.Mostrar()

print (f'Tu saldo privado que no deberias compartir es {Objeto24.Dinero}')

Objeto24.Dinero = '20,000,000'

Objeto24.Mostrar()

print (f'Tu saldo privado que no deberias compartir es {Objeto24.Dinero}')

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
        
Objeto25 = Batalla1()

Objeto25.Batallar()

print (f'-' * 20)

class Batalla2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El lider de gimnasio ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Criatura1 = Bulbasaur()
Objeto26 = Batalla2(Criatura1)
Objeto26.Batallar()

print (f'-' * 20)

Criatura2 = Treekoo()
Objeto27 = Batalla2(Criatura2)
Objeto27.Batallar()

print (f'-' * 20)

Criatura3 = Chikorita()
Objeto28 = Batalla2(Criatura3)
Objeto28.Batallar()

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def General(self):
        pass
    
class Sub_Plantilla(Plantilla):
    def Mostrar(self):
        print (f'Este metodo pertenece a la sub plantilla')
        
    def General(self):
        print (f'Este es el metodo de la abstraccion')
        
Objeto29 = Sub_Plantilla()

Objeto29.Mostrar()
Objeto29.General()

print (f'-' * 20)

class Cocinar(ABC):
    @abstractmethod
    def Hornear(self):
        pass

class Pizza(Cocinar):
    def Amasar(self):
        print (f'En esta etapa se amaso la masa')
        
    def Encender(self):
        print (f'En esta etapa se encendio el horno')
        
    def Hornear(self):
        print (f'La pizza ha sido horneada')
        
Objeto30 = Pizza()

Objeto30.Amasar()
Objeto30.Encender()
Objeto30.Hornear()

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
        
Objeto31 = Pastel1()
Objeto31.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Ingrediente1 = Chocolate()
Objeto32 = Pastel2(Ingrediente1)
Objeto32.Hornear()

print (f'-' * 20)

Ingrediente2 = Vainilla()
Objeto33 = Pastel2(Ingrediente2)
Objeto33.Hornear()

print (f'-' * 20)

Ingrediente3 = Fresa()
Objeto34 = Pastel2(Ingrediente3)
Objeto34.Hornear()

print (f'-' * 20)

class Persona2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
        
Objeto35 = Persona2('Erick Josue')

print (f'Mi nombre es {Objeto35}')

print (f'-' * 20)

class Igualdad2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
        
Objeto36 = Igualdad2('Panda Rojo')
Objeto37 = Igualdad2('Panda Rojo')

if (Objeto36 == Objeto37):
    print (f'Ambos objetos son iguales')
else:
    print (f'Error, los objetos son diferentes')
    
print (f'-' * 20)

class Colores2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Colores2 = [
    Colores2('Amarillo'),
    Colores2('Rojo'),
    Colores2('Azul')
]

print (f'La lista de colores es {Lista_Colores2}')

print (f'-' * 20)

class Caja2():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto38 = Caja2(5)
Objeto39 = Caja2(2)

print (f'El resultado de la sumatoria es {Objeto38 + Objeto39}')

print (f'-' * 20)

class Inventario2():
    def __init__(self):
        self.Utiles = [
            'Cuaderno',
            'Lapicero',
            'Borrador'
        ]
        
    def __getitem__(self, Indice):
        return self.Utiles[Indice]
        
Objeto40 = Inventario2()

print (f'El elemento en la posicion 0 es {Objeto40[0]}')
print (f'El elemento en la posicion 1 es {Objeto40[1]}')
print (f'El elemento en la posicion 2 es {Objeto40[2]}')

print (f'-' * 20)

class Panaderia2():
    def __init__(self):
        self.Panes = [
            'Baguette',
            'Croissant',
            'Masa Madre'
        ]
        
    def __iter__(self):
        return iter(self.Panes)
        
Objeto41 = Panaderia2()

for indice, elemento in enumerate(Objeto41, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

class Persona3():
    def __init__(self):
        self.Individuos = []
        
    def __len__(self):
        return len(self.Individuos)
        
Objeto42 = Persona3()

Objeto42.Individuos.extend(['Erick'])
Objeto42.Individuos.insert(1, 'Josue')
Objeto42.Individuos.append('Karlita')

print (f'El total de personas en la lista es {len(Objeto42)}')

print (f'-' * 20)

class Persona4():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    # Manera 1 para mostrar el nombre
    def __str__(self):
        return self.Nombre
    
    # Manera 2 para mostrar el nombre
    @property
    def Usted1(self):
        return self.Nombre
    
    def Usted2(self):
        return self.Nombre
    
    def __repr__(self):
        return self.Nombre

Objeto43 = Persona4('Erick Perez Gutierrez')

print (f'Mi nombre es {Objeto43}')

print (f'Mi nombre es {Objeto43.Usted1}')
print (f'Mi nombre es {Objeto43.Usted2()}')

print (f'-' * 20)

var13 = 20
var13 += 1

print (f'El resultado es {var13}')

var13 -= 1

print (f'El resultado es {var13}')

var13 *= 1

print (f'El resultado es {var13}')

var13 //= 2

print (f'El resultado es {var13}')

var13 /= 1

print (f'El resultado es {var13}')

var13 **= 3

print (f'El resultado es {var13}')

var13 %= 6

print (f'El resultado es {var13}')

print (f'-' * 20)

# Esto es una declaracion walrus
print (f'Mi nombre es {(Presentacion := "Erick Josue Perez Gutierrez")}')

for elemento in range(0, limite := 5):
    print (f'{elemento}')
    
print (f'-' * 20)

Contador = 0

while (Contador < len(Lista_Limite := ['Erick', 'Josue', 'Karlita'])):
    print (f'La persona en la posicion {Contador + 1} es {Lista_Limite[Contador]}')
    Contador += 1
    
from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

Variable1 = Lista_Uno[0]
Variable2 = 'Perez'
Variable3 = '''Esto
Es
Una
Variable
Long
String'''

Variable4 = Objeto11.Cantidad
Variable5 = PEPE.Division_Flotante

try:
    Variable6, Variable7, = True, Objeto9.Catched
except ValueError:
    print (f'Error, al declaracion fue hecha de manera incorrecta')
    
# Esto es un comentario simple

'''
Esto
Es
Un
Comentario
Compuesto
DocString'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke2"]}')

class Persona5():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto44 = Persona5(Lista_Uno[0])

print (f'Mi nombre completo es {Objeto44} {Variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Variable_Sumatoria}, {Anonima2(15)} o incluso {Objeto10.Cantidad} pokemones')

del Variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in Variable3)

print (f'-' * 20)

print (f'Erick' in Lista_Uno)
print (f'Gary' not in PEPE.Tupla_Poke)
print (f'{PEPE.Diccionario_Poke["Poke3"]}' in PEPE.Set_Conjunto_Poke1)
print (f'{PEPE.Diccionario_Poke["Poke1"]}' in PEPE.Set_Conjunto_Poke2)
print (f'{PEPE.Diccionario_Poke["Poke3"]}' in PEPE.Set_Conjunto_Poke2)

print (f'-' * 20)

Snake_Case5, Snake_Case6, Snake_Case7 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables y una declaracion snake_case {Snake_Case6}')

print (f'La lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Elemento1', 'Elemento2', 'Elemento3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto10.Cantidad, Variable_Sumatoria)

print (f'El Cociente de la operacion es {Cociente}')
print (f'El Residuo de la operacion es {Residuo}')

print (f'Un rango de elementos es {PEPE.Lista2}')
print (f'Un rango de elementos es {PEPE.Lista2[:2]}')
print (f'Un rango de elementos es {PEPE.Lista2[2:]}')
print (f'Un rango de elementos es {PEPE.Lista2[::2]}')
print (f'Un rango de elementos es {PEPE.Lista2[::3]}')
print (f'Un rango de elementos es {PEPE.Lista2[2:3]}')
print (f'Un rango de elementos es {PEPE.Lista2[0:None]}')
print (f'Un rango de elementos es {PEPE.Lista2[:]}')
print (f'Un rango de elementos es {PEPE.Lista2[:-1]}')
print (f'Un rango de elementos es {PEPE.Lista2[:-2]}')
print (f'Un rango de elementos es {PEPE.Lista2[:-3]}')

print (f'-' * 20)

print (f'Mi nombre es {Lista_Uno[0]} y yo te juro que vi un {PEPE.Lista2[PEPE.Lista2.index("Koala")]} la semana pasada')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, Anonima1(150, 2))

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

Diccionario_Numeral3 = dict({
    'Num1' : 7,
    'Num2' : 3,
    'Num3' : 1,
    'Num4' : 6,
    'Num5' : 2
})

Diccionario_Numeral3_Sorted = dict(sorted(Diccionario_Numeral3.items(), key=lambda item : item[1]))

Diccionario_Numeral3_Sorted_Min = min(Diccionario_Numeral3_Sorted.items(), key=lambda item : item[1])
Diccionario_Numeral3_Sorted_Max = max(Diccionario_Numeral3_Sorted.items(), key=lambda item : item[1])

print (f'{Diccionario_Numeral3}')
print (f'{Diccionario_Numeral3_Sorted}')
print (f'{Diccionario_Numeral3_Sorted_Min}')
print (f'{Diccionario_Numeral3_Sorted_Max}')

Lista_Estudiantes1 = list([])

Nombre2 = 'Erick'
Edad2 = 37

Estudiantes1 = [Nombre2, Edad2]

Lista_Estudiantes1.append(Estudiantes1)

Nombre2 = 'Karlita'
Edad2 = 6

Estudiantes1 = [Nombre2, Edad2]

Lista_Estudiantes1.append(Estudiantes1)

print (f'{Lista_Estudiantes1}')

for indice, elemento in Lista_Estudiantes1:
    print (f'{indice} : {elemento}')
    
Lista_Estudiantes1.sort(key=lambda num : num[1])

Menor3 = Lista_Estudiantes1[0][0]
Mayor3 = Lista_Estudiantes1[-1][0]

print (f'{Menor3} - {Lista_Estudiantes1[0][1]} años')
print (f'{Mayor3} - {Lista_Estudiantes1[-1][1]} años')

print (f'-' * 20)

print (f'{dir(PEPE)}')

Tupla1 = ('Uno', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos',) # En una tupla, los elementos repetidos se muestran

print (f'{Tupla1}')

# del Tupla1[1]  No se pueden eliminar elementos de una tupla

# Tupla1[2] = 'Hola' No se puede reemplazar el contenido de un elemento de una tupla

Tupla1 = tuple(('One', 'Two', 'Three',)) # Una tupla solo puede reconstruirse

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{Tupla1}')
print (f'{Tupla2}')
print (f'{Tupla3}')

Set_Conjunto1 = {'Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde'}

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Red', 'Green'})

print (f'{Set_Conjunto1}')

Set_Conjunto1.add('Blue')

print (f'{Set_Conjunto1}')

Set_Conjunto2 = {1, 2, 3, 4, 5}
Set_Conjunto3 = {3, 4}
Set_Conjunto4 = set({8})

print (f'{Set_Conjunto2.issuperset(Set_Conjunto3)}')
print (f'{Set_Conjunto2 >= Set_Conjunto3}')

print (f'-' * 20)

print (f'{Set_Conjunto3.issubset(Set_Conjunto2)}')
print (f'{Set_Conjunto3 <= Set_Conjunto2}')

print (f'-' * 20)

print (f'{Set_Conjunto2.isdisjoint(Set_Conjunto4)}')

print (f'-' * 20)

SetA1 = {1, 2, 3, 4}
SetB1 = {3, 4, 5, 6}

print (f'{SetA1.union(SetB1)}')
print (f'{SetA1 | SetB1}')

print (f'-' * 20)

print (f'{SetA1.intersection(SetB1)}')
print (f'{SetA1 & SetB1}')

print (f'-' * 20)

print (f'{SetA1.difference(SetB1)}')
print (f'{SetA1 - SetB1}')

print (f'-' * 20)

print (f'{SetB1.difference(SetA1)}')
print (f'{SetB1 - SetA1}')

print (f'-' * 20)

print (f'{SetA1.symmetric_difference(SetB1)}')
print (f'{SetA1 ^ SetB1}')

print (f'-' * 20)

SetC1 = {1, 2, 3}
SetD1 = {3}
SetE1 = set({8})

print (f'{SetC1.issuperset(SetD1)}')
print (f'{SetC1 >= SetD1}')

print (f'-' * 20)

print (f'{SetD1.issubset(SetC1)}')
print (f'{SetD1 <= SetC1}')

print (f'-' * 20)

print (f'{SetC1.isdisjoint(SetE1)}')

print (f'-' * 20)

'''SetA1.update(SetB1)

print (f'{SetA1}')'''

'''SetA1.intersection_update(SetB1)

print (f'{SetA1}')'''

'''SetA1.difference_update(SetB1)

print (f'{SetA1}')'''

'''SetB1.difference_update(SetA1)

print (f'{SetB1}')'''

SetA1.symmetric_difference_update(SetB1)

print (f'{SetA1}')

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})

Set_Conjunto_Menu3 = set({'ChocoFresa', Set_Conjunto_Menu2})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

Diccionario1 = {
    'Nombre' : 'Erick',
    'Edad' : 37,
    'Votante' : not False
}

Diccionario2 = {
    'Nombre' : ['Erick', 'Josue', 'Karlita'],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
}

Diccionario3 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

print (f'-' * 20)

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
print (f'{Diccionario2["Nombre"][0]}')
print (f'{Diccionario2.get("Edad")[1]}') #type: ignore

print (f'-' * 20)

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3.values()}')
print (f'{Diccionario3.items()}')
print (f'{Diccionario3["Ingresos"]}')
print (f'{Diccionario3.get("Gastos")}')

print (f'-' * 20)

Diccionario1['Nombre'] = Saludar_Dos()

print (f'{Diccionario1}')

Diccionario1_Copia = Diccionario1.copy()

del Diccionario1['Nombre']

Diccionario1.pop('Edad')

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1["Votante"]}')

print (f'-' * 20)

Diccionario1 = dict({1 : "Karlita", 2 : 6, 3 : Variable7}) #type: ignore

print (f'{Diccionario1[1]} no puede votar ya que solo tiene {Diccionario2.get("Edad")[2]} añitos') #type: ignore

Diccionario_Vacio1 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2 = dict.fromkeys('ABC', f'{PEPE.Diccionario_Poke["Poke3"]}')

Diccionario_Vacio1['Dos'] = 'HelloWorld'

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio2}')

print (f'-' * 20)

Diccionario_Vacio3 = dict.fromkeys(['Nombre', 'Edad', 'Votante'])

Lista_Agrupar = [("Nombre","Erick"), ("Edad",37), ("Nombre","Josue"), ("Nombre","Karlita"), ("Edad",20)]

Diccionario_Vacio3 = {
    'Nombre' : [],
    'Edad' : [],
    'Votante' : []
}

for indice, elemento in Lista_Agrupar:
    if (indice in Diccionario_Vacio3):
        Diccionario_Vacio3[indice].append(elemento)
    else:
        continue
    
print (f'{Diccionario_Vacio3}')

print (f'-' * 20)

for elemento in Diccionario1:
    print (f'{Diccionario1[elemento]}')
    
print (f'-' * 20)

for elemento in Diccionario2.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario2.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario2.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

import pandas as pd

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3.head()}')

Set_Csv3 = set(Cargar_Csv3['product'])

print (f'{Set_Csv3}')

Lista_Csv3 = list(Set_Csv3)

print (f'{Lista_Csv3}')

Key1 = [f'Key{i}' for i in range(0, len(Lista_Csv3))]

print (f'{Key1}')

Diccionario4 = dict(zip(Key1, Lista_Csv3))

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Key2"]}')
print (f'{Diccionario4.get("Key4")}')

print (f'-' * 20)

for elemento in Diccionario4.items():
    print (f'{elemento[0]} : {elemento[1]}')
    
print (f'-' * 20)

import pandas as pd
from datetime import datetime

print (f'{Cargar_Csv3.head()}')

print (f'-' * 20)

Fecha3 = '2026-04-01'

try:
    Fech3 = datetime.strptime(Fecha3, '%Y-%m-%d').date()
    Fech3_Formateada = pd.to_datetime(Fech3)
    Cargar_Csv3['date'] = pd.to_datetime(Cargar_Csv3['date'])
except (ValueError, Exception):
    print (f'Error, la fecha tiene un formato invalido')
    
Cargar_Csv3['TOTALITO'] = Cargar_Csv3['quantity'] * Cargar_Csv3['price']
    
Encontrado3 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech3_Formateada.date()] #type: ignore

if (Encontrado3.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! Encontramos ventas en esta fecha')
    
    Grupo6 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo6_Min = Grupo6.idxmin()
    Grupo6_Max = Grupo6.idxmax()
    Grupo6_Min_Cant = Grupo6.min()
    Grupo6_Max_Cant = Grupo6.max()
    
    print (f'En la fecha {Fech3_Formateada} el producto {Grupo6_Min} vendio un total de {Grupo6_Min_Cant} unidades') #type: ignore
    print (f'En la fecha {Fech3_Formateada} el producto {Grupo6_Max} vendio un total de {Grupo6_Max_Cant} unidades') #type: ignore
    
    print (f'La cantidad de clientes que compraron fue de {Grupo6.count()}')
    
    print (f'La cantidad de productos vendidos fue de {Grupo6.sum()}')
    
    Grupo7 = Encontrado3.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue de ${Grupo7.sum()}')
    
    Promedio5 = Grupo7.sum() / Grupo6.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio5, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Grupo7.mean(), 2)}')
    
print (f'-' * 20)

Diccionario9X = {
    'Nombre' : "Erick"
}

for elemento in Diccionario9X.items():
    print (f'{elemento[0]} : {elemento[1]}')
    
print (f'-' * 20)

Diccionario10X = {
    'Nombre' : ["Erick", "Josue"]
}

for indice, elemento in Diccionario10X.items():
    for cajitas in elemento[:]:
        print (f'{cajitas}')
        
print (f'-' * 20)

Diccionario11X = {
    "ana": {"edad": 25, "ciudad": "Quito"}, 
    "luis": {"edad": 30, "ciudad": "Guayaquil"}
    }

for Nivel1_Clave, Nivel1_Valor in Diccionario11X.items():
    for Nivel2_Clave, Nivel2_Valor in Nivel1_Valor.items():
        print (f'{Nivel2_Clave} : {Nivel2_Valor}')
        
print (f'-' * 20)

def Ejercicio72(Diccionario, User, Field):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        return (False, f'Error, el usuario no existe')
    else:
        Ubicado2 = Ubicado1.get(Field)
        if (Ubicado2 is None):
            return (False, f'Error, el campo no existe')
        else:
            return (True, f'Ambos usuario y campo existen')

Usuaria1 = 'luis'
Campo5 = 'casa'

Sample72 = Ejercicio72(Diccionario11X, Usuaria1, Campo5)

if (not Diccionario11X):
    print (f'Error el diccionario esta vacio')
else:
    if (Sample72 == True):
        print (f'{Sample72}')
    else:
        print (f'{Sample72}')
        
print (f'-' * 20)

Datos3 = {
    "ana":  {"edad": 25, "ciudad": "Quito"},
    "luis": {"edad": 30, "ciudad": "Guayaquil"}
    }

def Ejercicio73(Diccionario, User, Field, New_Value):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        return (False, f'Error, el usuario no existe')
    else:
        Ubicado2 = Ubicado1.get(Field)
        if (Ubicado2 is None):
            return (False, f'Error, el campo no existe')
        else:
            Diccionario[User][Field] = New_Value
            return Diccionario

Usuaria2 = 'luis'
Campo6 = 'ciudad'
Nuevo_Valor6 = 'San Jose'

Sample73 = Ejercicio73(Datos3, Usuaria2, Campo6, Nuevo_Valor6)

if (Datos3):
    if (Sample73 == False):
        print (f'{Sample73}')
    else:
        print (f'{Sample73}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Datos4 = {}

def Ejercicio74(Diccionario, User, Field, New_Value):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        Diccionario[User] = {}
        Diccionario[User][Field] = New_Value
        return (True, f'Usuario Creado')
    else:
        Diccionario[User][Field] = New_Value
        return (True, f'Usuario Actualizado')

Usuaria3 = 'jose'
Campo7 = 'ciudad'
Nuevo_Valor7 = 'Dubai'

Sample74 = Ejercicio74(Datos4, Usuaria3, Campo7, Nuevo_Valor7)

print (f'{Sample74}')

print (f'-' * 20)

Datos5 = {"ana": {"edad": 25, "ciudad": "Quito"}}

def Ejercicio75(Diccionario, User, Field, New_Value):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        Diccionario[User] = {}
        Diccionario[User][Field] = New_Value
        return (True, "creado")
    else:
        Ubicado2 = Ubicado1.get(Field)
        if (Ubicado2 is None):
            Diccionario[User][Field] = New_Value
            return (True, "campo nuevo")
        else:
            Diccionario[User][Field] = New_Value
            return (True, "actualizado")

Usuaria4 = 'ana'
Campo8 = 'telefono'
Nuevo_Valor8 = 999

Sample75 = Ejercicio75(Datos5, Usuaria4, Campo8, Nuevo_Valor8)

print (f'-' * 20)

Datos6 = {"ana": {"edad": 25, "ciudad": "Quito"}}

def Ejercicio76(Diccionario, User, Field, New_Value):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        Diccionario[User] = {}
        Diccionario[User][Field] = New_Value
        return (True, "creado")
    else:
        Ubicado2 = Ubicado1.get(Field)
        if (Ubicado2 is None):
            Diccionario[User][Field] = New_Value
            return (True, "campo nuevo")
        else:
            Diccionario[User][Field] = New_Value
            return (True, "actualizado")

Usuaria5 = 'roberto'
Campo9 = 'telefono'
Nuevo_Valor9 = '999'

Sample76 = Ejercicio76(Datos6, Usuaria5, Campo9, Nuevo_Valor9)

print (f'{Sample76}')

print (f'-' * 20)

Diccionario_Numeral4 = dict({
    'Num1' : 7,
    'Num2' : 3,
    'Num3' : 1,
    'Num4' : 6,
    'Num5' : 2
})

print (f'{Diccionario_Numeral4}')

Diccionario_Numeral4_Sorted = dict(sorted(Diccionario_Numeral4.items(), key=lambda item : item[1]))

print (f'{Diccionario_Numeral4_Sorted}')

Diccionario_Numeral4_Sorted_Min = min(Diccionario_Numeral4_Sorted.items(), key=lambda item : item[1])
Diccionario_Numeral4_Sorted_Max = max(Diccionario_Numeral4_Sorted.items(), key=lambda item : item[1])

print (f'{Diccionario_Numeral4_Sorted_Min}')
print (f'{Diccionario_Numeral4_Sorted_Max}')

print (f'-' * 20)

'''Lista_Estudiantes2 = []

Contador = 3

def Colegio1(Lista):
    for elemento in range(0, Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del estudiante {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del estudiante {elemento + 1}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda num : num[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes es {Menore} y su edad es {Lista[0][1]} años')
    print (f'El mayor de los estudiantes es {Mayore} y su edad es {Lista[-1][1]} años')

Colegio1(Lista_Estudiantes2)'''

Division_Baja = 14 // 7
Exponente = 4**3
Modulo = 20 % 6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {round(Division_Baja, 2)}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'-' * 20)

print (f'{type(Variable1)}')
print (f'{type(Variable4)}')
print (f'{type(PEPE.Division_Flotante)}')
print (f'{type(Lista_Uno)}')
print (f'{type(PEPE.Set_Conjunto_Poke1)}')
print (f'{type(Tupla3)}')
print (f'{type(Diccionario11X)}')
print (f'{type(Funcion_Tupla)}')
print (f'{type(Poke_Kid1)}')
print (f'{type(Objeto10)}')
print (f'{type(Array2)}')
print (f'{type(Data_Frame_Concatenate)}')
print (f'{type(PEPE)}')

print (f'-' * 20)

if (Diccionario3['Ingresos'] > 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos Altos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo interno')
elif (Diccionario3['Ingresos'] == 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo interno')
elif (Diccionario3['Ingresos'] < 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Al Limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Altos')
    else:
        print (f'Error de codigo interno')
else:
    print (f'Error de codigo externo')
    
print (f'-' * 20)

var14 = Saludar_Dos()
var15 = Variable_Sumatoria

if (var14 == Variable1 and var15 >= 20):
    print (f'Correcto, ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')
    
print (f'-' * 20)

if (var14 == Variable1 or var15 >= 20):
    print (f'Correcto, al menos una condicion se cumple')
else:
    print (f'Error, ninguna de las condiciones se cumplen')
    
print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Otros = []
        
    def __str__(self):
        return self.Favorite
    
    def __len__(self):
        return len(self.Otros)
    
    def Desplegar(self):
        print (f'El entrenador {self.Trainer} acaba de atrapar un {self.Favorite} mientras viajaba por {self.City}')
        
Objeto45 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Ash")], 'Kanto', Objeto9.Nombre)
Objeto46 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Brooke")], 'Alolah', Objeto10.Nombre)
Objeto47 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")], 'Paldea', Objeto11.Nombre)

print (f'El nombre del pokemon es {Objeto45.Favorite}')
print (f'El nombre del pokemon es {Objeto45}')

Objeto46.Otros.append(PEPE.Diccionario_Poke['Poke1'])
Objeto46.Otros.insert(1, 'Moltres')
Objeto46.Otros.extend(['Asumarri'])

print (f'La cantidad de pokemones en el pokedex es {len(Objeto46)}')

Objeto45.Desplegar()
Objeto46.Desplegar()
Objeto47.Desplegar()

print (f'-' * 20)

Negativo = -5

print (f'Este numero ahora es positivo {int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima4 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable}')
print (f'{list(Anonima4)}')
print (f'{Lista_Iterable}')

print (f'-' * 20)

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
    print (f'Gracias por ingresar la informacion')
else:
    print (f'Error, necesito que ingreses una cadena de texto')
    
Cociente2, Residuo2 = divmod(Objeto9.Cantidad, Variable_Sumatoria)

print (f'El Cociente2 de la operacion es {Cociente2}')
print (f'El Residuo2 de la operacion es {Residuo2}')

print (f'-' * 20)

for elemento in range(5):
    print (f'El elemento es {elemento}')
    
print (f'-' * 20)

for elemento in range(0, 5):
    print (f'El elemento es {elemento}')
    
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

for indice, elemento in enumerate(Lista_Uno_Copia[:], start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia[0:None], start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia[:-1], start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia[:-2], start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia[:-3], start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

Variable8 = 'eSteBAN'
Variable8_Letra = Variable8[0]

print (f'{Variable8}')
print (f'{Variable8.lower()}')
print (f'{Variable8.upper()}')
print (f'{Variable8.capitalize()}')
print (f'{Variable8.title()}')

print (f'-' * 20)

print (f'{Variable8.lower()}')

Lista_Nombres3 = ['juan salvo', 'henry courtney', 'elizabeth bennet', 'marge simpson']
Lista_Nombres3_Actualizada = list([])

for elemento in Lista_Nombres3:
    Lista_Nombres3_Actualizada.append(elemento.title())
    
print (f'{Lista_Nombres3}')
print (f'{Lista_Nombres3_Actualizada}')

print (f'-' * 20)

print (f'{Variable8.lower().find("t")}')
print (f'{Variable8.lower().index("b")}')

print (f'La letra {Variable8_Letra} aparece un total de {Variable8.lower().count(Variable8_Letra)} veces')

print (f'{Variable8.lower().startswith(Variable8_Letra)}')
print (f'{Variable8.lower().endswith("n")}')

print (f'{Variable8.lower().replace("ban", "POPOTAMO")}')

Nombre3 = '          Lautaro'

print (f'{Nombre3}')

Nombre3_Version1 = Nombre3.strip()

print (f'{Nombre3_Version1}')

Nombre3_Version2 = ' '.join(Nombre3_Version1.split())

print (f'{Nombre3_Version2}')

Textico1 = '----hola mundo***'

print (f'{Textico1}')
print (f'{Textico1.strip("-*")}')

Variable9 = 'esto es un texto cualquiera, lo que queremos es ver si esto sirve o no'

Lista_Variable9 = Variable9.split(' ')

for indice, elemento in enumerate(Lista_Variable9, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

print (f'La cantidad de palabras digitadas es {len(Lista_Variable9)}')

print (f'-' * 20)

var16 = 'texto'

if (isinstance(var16, (str))):
    print (f'Lo que ingresaste es un texto')
else:
    print (f'Error de formato, esto no es un texto')
    
if (var16.isalpha()):
    print (f'Lo que ingresaste es un texto')
else:
    print (f'Error de formato, esto no es un texto')
    
try:
    Resultado = 3 ** var16 #type: ignore
    print (f'Error, lo que ingresaste no es un texto')
except TypeError:
    print (f'Lo que ingresaste es un texto')
    
print (f'-' * 20)

var17 = 3.5

if (isinstance(var17, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, lo que ingresaste no es un numero decimal')
    
try:
    Numero8 = float(var17)
    if (Numero8.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var18 = 3.5

if (isinstance(var18, (int, float))):
    print (f'Lo que ingresaste es un numero entero o decimal')
else:
    print (f'Error de formato')
    
try:
    Numero9 = float(var18)
    if (Numero9.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except (ValueError, Exception):
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var19 = 'hola'

if (isinstance(var19, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var19.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var19.isdecimal()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
try:
    Numero10 = float(var19)
    if (Numero10.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError as Errore5:
    print (f'Error, lo que ingresaste no es un numero -> {str(Errore5)}')
    
print (f'-' * 20)

var20 = 'erick'

if (isinstance(var20, (int, str))):
    print (f'Esta mica tiene numeros o texto')
else:
    print (f'Error de formato')
    
if (var20.isalnum()):
    print (f'Esta mica tiene numeros o texto')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var21 = '    s   '

if (var21.isspace()):
    print (f'Esto solo tiene espacios')
else:
    print (f'Error, esto tiene mucho mas que solo espacios')
    
print (f'-' * 20)

var22 = 'eSteBAN'

if (var22.lower().islower()):
    print (f'Esto esta compuesto unicamente por minusculas')
else:
    print (f'Error, esto tiene mucho mas que solo minusculas')
    
print (f'-' * 20)

if (var22.upper().isupper()):
    print (f'Esto esta compuesto unicamente por mayusculas')
else:
    print (f'Error, esto tiene mucho mas que solo mayusculas')
    
print (f'-' * 20)

if (var22.title().istitle()):
    print (f'Esto esta compuesto unicamente por camel case')
else:
    print (f'Error, esto tiene mucho mas que solo camel case')
    
print (f'-' * 20)

var23 = ' '

if (bool(var23) == True):
    print (f'Esto tiene algun tipo de contenido')
else:
    print (f'Error, esto esta completamente vacio')
    
print (f'-' * 20)

print (f'{Lista_Uno_Copia.index("Perez")}')

Dict_Eliminado = Diccionario1_Copia.pop("Nombre")

print (f'{Dict_Eliminado}')

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'El elemento es {PEPE.Lista_Numeros[Contador]}')
    Contador += 1
    
print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros[:])):
    print (f'El elemento {Contador + 1} es {PEPE.Lista_Numeros[Contador] * 100}')
    Contador += 1
    
print (f'-' * 20)

Lista_Animales2 = ['Cocodrilo']
Lista_Animales2.append('Perro')
Lista_Animales2.insert(2, 'Tortuga')
Lista_Animales2.extend(['Petirrojo'])

Contador = 0

while (Contador < len(Lista_Animales2)):
    if (Lista_Animales2[Contador] == 'Tortuga'):
        print (f'Este bichillo es mi animal favorito')
        break
    else:
        Contador += 1
        continue
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Uno_Copia, Set_Conjunto_Menu1):
    print (f'{elemento1} : {elemento2}')
    
print (f'-' * 20)

for elemento1, elemento2, elemento3, elemento4 in zip(Lista_Uno_Copia, Set_Conjunto_Menu1, PEPE.Set_Conjunto_Poke1, Lista_Animales2):
    print (f'{elemento1} : {elemento2} : {elemento3} : {elemento4}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'El elemento es {elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'El elemento es {elemento}')
    
print (f'-' * 20)

for elemento in range(0, len(Lista_Colores2)):
    print (f'El elemento es {elemento}')
    
print (f'-' * 20)

for elemento in range(995 + 3, 1000):
    print (f'El elemento es {elemento}')

print (f'-' * 20)

Lista_Mult1 = [num  * 100 for num in PEPE.Lista_Numeros]

print (f'{PEPE.Lista_Numeros}')
print (f'{Lista_Mult1}')

print (f'-' * 20)

Contador = 0

while (Contador < 5):
    print (f'El contador es {Contador + 1}')
    Contador += 1
    
print (f'-' * 20)

Menor4 = min(Lista_Mult1)
Mayor4 = max(Lista_Mult1)

Redondeado = round(14.458795, 2)

Sumatoria4 = sum(Lista_Mult1)

print (f'El numero menor de la lista es {Menor4}')

print (f'El numero Mayor de la lista es {Mayor4}')

print (f'El redondeo del numero 14.458795 es {Redondeado}')

print (f'El resultado de la sumatoria es {Sumatoria4}')

print (f'{bool(False)}')
print (f'{bool(not True)}')
print (f'{bool(0)}')
print (f'{bool(None)}')
print (f'{bool("")}')

Todo_All = all([Lista_Mult1, Tupla_Array, PEPE.Set_Conjunto_Poke1, None])

print (f'{Todo_All}')

Uno = int('500')
Dos = str(Variable4)
Tres = float(Uno)
Cuatro = list(Tupla_Array)
Cinco = set(PEPE.Lista_Numeros)
Seis = tuple(Set_Conjunto_Menu1)

print (f'{type('500')} : {type(Uno)}')
print (f'{type(Variable4)} : {type(Dos)}')
print (f'{type(Uno)} : {type(Tres)}')
print (f'{type(Tupla_Array)} : {type(Cuatro)}')
print (f'{type(PEPE.Lista_Numeros)} : {type(Cinco)}')
print (f'{type(Set_Conjunto_Menu1)} : {type(Seis)}')

print (f'-' * 20)

Any_Iterable2 = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima5 = filter(lambda num : num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable2 = [num for num in PEPE.Lista_Numeros if num % 2 == 0]

print (f'{Any_Iterable2}')
print (f'{list(Anonima5)}')
print (f'{Lista_Iterable2}')

Diccionario_Numeral5 = dict({
    'Num1' : 7,
    'Num2' : 3,
    'Num3' : 1,
    'Num4' : 6,
    'Num5' : 2
})

Diccionario_Numeral5_Sorted = dict(sorted(Diccionario_Numeral5.items(), key=lambda item : item[1]))

Diccionario_Numeral5_Sorted_Min = min(Diccionario_Numeral5_Sorted.items(), key=lambda item : item[1])
Diccionario_Numeral5_Sorted_Max = max(Diccionario_Numeral5_Sorted.items(), key=lambda item : item[1])

print (f'{Diccionario_Numeral5}')
print (f'{Diccionario_Numeral5_Sorted}')
print (f'{Diccionario_Numeral5_Sorted_Min}')
print (f'{Diccionario_Numeral5_Sorted_Max}')

print (f'-' * 20)

'''Lista_Estudiantes2 = list([])

Contador = 3

def Colegio(Lista):
    for elemento in range(0, Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno: {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda num : num[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El Menore de los estudiantes es {Menore}')
    print (f'El Mayore de los estudiantes es {Mayore}')

Colegio(Lista_Estudiantes2)'''

print (f' - '.join(PEPE.Set_Conjunto_Poke1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

print (f'-' * 20)

from Paquete.Sub_Paquete import Segundo as PEPE4

Variable_PEPE4 = PEPE4

print (f'-' * 20)

'''def Exception_Finale():
    while (True):
        try:
            Numero = input(f'Ingrese un numero: ')
            Numero11 = float(Numero)
            if (Numero11.is_integer()):
                print (f'Lo que ingresaste es un numero entero')
                break
            else:
                print (f'Lo que ingresaste es un numero decimal')
                break
        except (ValueError, Exception):
            print (f'Error, lo que ingresaste no es un numero')

Exception_Finale()'''

import pandas as pd
import requests
import io

Ruta_Html2 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response2 = requests.get(Ruta_Html2, headers=headers)

Leer_Html2 = io.StringIO(Response2.text)

Cargar_Html2 = pd.read_html(Leer_Html2)

print (f'{Cargar_Html2[2].head()}')

print (f'-' * 20)

import re

Texto12 = 'ericksuper80@hotmail.com'

Pattern18 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}$'

Buscar26 = bool(re.fullmatch(Pattern18, Texto12))

if (Buscar26 == True):
    print (f'El correo tiene el formato correcto')
else:
    print (f'Error, formato de correo invalido')
    
print (f'-' * 20)

import re

Texto13 = '39'

Pattern19 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar27 = bool(re.match(Pattern19, Texto13))

if (Buscar27 == True):
    print (f'El numero se encuentra entre 01 - 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
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
except ValueError as Errore6:
    print (f'Error, la fecha tiene un formato incorrecto -> {str(Errore6)}')
    exit()
    
Cargar_Csv4['TOTALITO'] = Cargar_Csv4['quantity'] * Cargar_Csv4['price']
    
Encontrado4 = Cargar_Csv4[Cargar_Csv4['date'].dt.date == Fech4_Formateada.date()]

if (Encontrado4.empty):
    print (f'No hay ventas registradas en esta fecha')
else:
    print (f'Genial! se encontraron ventas en esta fecha')
    
    Grupo8 = Encontrado4.groupby('product')['quantity'].sum()
    Grupo8_Min = Grupo8.idxmin()
    Grupo8_Max = Grupo8.idxmax()
    Grupo8_Min_Cant = Grupo8.min()
    Grupo8_Max_Cant = Grupo8.max()
    
    print (f'El producto {Grupo8_Min} vendio {Grupo8_Min_Cant} unidades')
    print (f'El producto {Grupo8_Max} vendio {Grupo8_Max_Cant} unidades')
    
    print (f'Hoy recibidos {Grupo8.count()} clientes')
    
    print (f'La cantidad de productos vendidos fue de {Grupo8.sum()}')
    
    Promedio6 = Grupo8.sum() / Grupo8.count()
    
    print (f'El promedio de productos vendidos fue de {round(Promedio6, 2)}')
    print (f'El promedio de productos vendidos fue de {round(Grupo8.mean(), 2)}')
    
    Grupo9 = Encontrado4.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue de ${Grupo9.sum()}')
    
    Promedio7 = Grupo9.sum() / Grupo8.count()
    
    print (f'El promedio de ventas en dinero vendido fue de ${round(Promedio7, 2)}')
    print (f'El promedio de ventas en dinero vendido fue de ${round(Grupo9.mean(), 2)}')
    
print (f'-' * 20)

Diccionario_Lenguaje1 = {"python": 2, "java": 2, "c++": 2, "go": 1}

def Ejercicio77(Diccionario):
    Lista_Repetidos = []
    Diccionario_Sorted = dict(sorted(Diccionario.items(), key= lambda item : item[1]))
    Clave = next(iter(Diccionario_Sorted))
    Valor = Diccionario_Sorted[Clave]
    
    for indice, elemento in Diccionario_Sorted.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    for indice, elemento in Diccionario_Sorted.items():
        if (elemento == Valor):
            Lista_Repetidos.extend([indice])
        else:
            continue
        
    if (len(Lista_Repetidos) > 1):
        return Lista_Repetidos
    else:
        return Clave

Sample77 = Ejercicio77(Diccionario_Lenguaje1)

if (len(Diccionario_Lenguaje1) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample77):
        print (f'{Sample77}')
    else:
        print (f'Error adicional del diccionario')
        
print (f'-' * 20)

Lista_Productos = ["manzana", "zanahoria", "kiwi", "pera", "tomate"]

Canastas2 = {
    "frutas": [],     # se llenará con frutas
    "verduras": [],   # se llenará con verduras
    "otros": []       # se llenará con lo que no sea fruta ni verdura
}

def Ejercicio78(Lista, Diccionario):
    
    fruta = ["manzana","banana","pera"]
    verdura = ["zanahoria","lechuga","tomate"]
    
    if (len(Lista) == 0 or len(Diccionario) == 0):
        return None
    else:
        for elemento in Lista[0:None]:
            if (elemento in fruta):
                Diccionario['frutas'].append(elemento)
            elif (elemento in verdura):
                Diccionario['verduras'].append(elemento)
            else:
                Diccionario['otros'].append(elemento)
                
        return Diccionario

Sample78 = Ejercicio78(Lista_Productos, Canastas2)

if (Sample78 is None):
    print (f'Error, la lista esta vacia o el diccionario')
else:
    if (Sample78):
        for indice, elemento in Sample78.items():
            print (f'{indice} : {elemento}')
    else:
        print (f'Error, el diccionario resultado sigue vacio')
        
print (f'-' * 20)
        
Lista_Agrupar2 = [("fruta","manzana"), ("verdura","zanahoria"), ("fruta","pera"), ("fruta","banana"), ("verdura","tomate")]

def Ejercicio79(Lista):
    Diccionario_Vacio = dict({})
    for indice, elemento in Lista:
        if (indice not in Diccionario_Vacio):
            Diccionario_Vacio[indice] = []
            Diccionario_Vacio[indice].append(elemento)
        else:
            Diccionario_Vacio[indice].append(elemento)
            
    return Diccionario_Vacio

if (Lista_Agrupar2):
    Sample79 = Ejercicio79(Lista_Agrupar2)
    if (Sample79):
        print (f'{Sample79}')
    else:
        print (f'Error, el diccionario aun sigue vacio')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

