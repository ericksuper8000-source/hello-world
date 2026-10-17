try:
    import Module_Own as PEPE
except (ImportError, ModuleNotFoundError):
    print (f'Error, el modulo no se encontro')
    raise

Ventas1 = {"ana": ["manzana", "pera"], "luis": ["zanahoria", "manzana"]}

def Ejercicio1(Diccionario, Articulo):
    for indice, elemento in Diccionario.items():
        for finale in elemento[0:None]:
            if (finale == Articulo):
                return indice
            else:
                continue
            
    return None
        
Item1 = 'berenjena'

if (Ventas1):
    Sample1 = Ejercicio1(Ventas1, Item1)
    if (Sample1 is None):
        print (f'El producto no fue encontrado en el inventario')
    else:
        print (f'El producto fue vendido por {Sample1}')
else:
    print (f'Error, el diccionario anidado esta vacio')
    
print (f'-' * 20)

Diccionario_Anidado1 = {
    'Usuario1' : {
        'Nombre' : "Erick",
        'Edad' : 37,
        'Votante' : True
    },
    'Usuario2' : {
        'Nombre' : "Karlita",
        'Edad' : 6,
        'Votante' : not True
    }
}

def Ejercicio2(Diccionario, User, Field, New_Value):
    if (len(Diccionario) == 0):
        return None
    else:
        Ubicado1 = Diccionario.get(User)
        if (Ubicado1 is None):
            Diccionario[User] = {}
            Diccionario[User][Field] = New_Value
            return (False, f'El usuario no existia, se acaba de crear')
        else:
            Ubicado2 = Ubicado1.get(Field)
            if (Ubicado2 is None):
                Diccionario[User][Field] = New_Value
                return (False, f'El campo no existia, se acaba de crear')
            else:
                Diccionario[User][Field] = New_Value
                return (True, f'El usuario y el campo existian, valor actualizado')
    
Usuario1 = 'Usuario1'
Campo1 = 'Edad'
Nuevo_Valor1 = '500'

Sample2 = Ejercicio2(Diccionario_Anidado1, Usuario1, Campo1, Nuevo_Valor1)

if (Sample2 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample2[0] == True):
        print (f'{Sample2[1]}')
    else:
        print (f'{Sample2[1]}')
        
print (f'-' * 20)

Diccionario1X = {
    'Nombre' : "Erick"
}

for indice, elemento in Diccionario1X.items():
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

Diccionario2X = {
    'Nombre' : ["Erick", "Josue", "Karlita"]
}

for indice, elemento in Diccionario2X.items():
    for finale in enumerate(elemento[:]):
        print (f'{finale[0]} -- {finale[1]}')
        
print (f'-' * 20)

Diccionario3X = {
    'Usuario1' : {
        'Nombre' : "Erick",
        'Edad' : 37,
        'Votante' : True
    },
    'Usuario2' : {
        'Nombre' : "Karlita",
        'Edad' : 6,
        'Votante' : not True
    }
}

for nivel1_clave, nivel1_valor in Diccionario3X.items():
    for nivel2_clave, nivel2_valor in nivel1_valor.items():
        print (f'{nivel2_clave} : {nivel2_valor}')
        
print (f'-' * 20)

Diccionario4X = {
    'Usuario1' : {
        'Nombre' : "Erick",
        'Edad' : 37,
        'Votante' : True
    },
    'Usuario2' : {
        'Nombre' : "Karlita",
        'Edad' : 6,
        'Votante' : not True
    }
}

def Ejercicio3(Diccionario, User, Field):
    if (len(Diccionario) == 0):
        return None
    else:
        Ubicado1 = Diccionario.get(User)
        if (Ubicado1 is None):
            return (False, f'El usuario no existe')
        else:
            Ubicado2 = Ubicado1.get(Field)
            if (Ubicado2 is None):
                return (False, f'El campo no existe')
            else:
                return (True, f'Tanto el usuario como el campo existen')
    
Usuario2 = 'Usuario1'
Campo2 = 'Telefono'

Sample3 = Ejercicio3(Diccionario4X, Usuario2, Campo2)

if (Sample3 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample3[0] == True):
        print (f'{Sample3[1]}')
    else:
        print (f'{Sample3[1]}')
        
print (f'-' * 20)

Diccionario_Lenguaje1 = dict({"python": 2, "java": 2, "c++": 2, "go": 1})

def Ejercicio4(Diccionario):
    Lista_Repetidos = list([])
    Diccionario_Sorted = dict(sorted(Diccionario.items(), key=lambda item : item[1]))
    Clave = next(iter(Diccionario_Sorted))
    Valor = Diccionario[Clave]
    for indice, elemento in Diccionario_Sorted.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    for indice, elemento in Diccionario_Sorted.items():
        if (elemento == Valor):
            Lista_Repetidos.append(indice)
        else:
            continue
        
    if (len(Lista_Repetidos) > 1):
        return Lista_Repetidos
    else:
        return Clave

if (len(Diccionario_Lenguaje1) == 0):
    print (f'El diccionario esta vacio')
else:
    Sample4 = Ejercicio4(Diccionario_Lenguaje1)
    if (Sample4):
        print (f'El lenguaje con mayor valor: {Sample4}')
    else:
        print (f'Este codigo esta roto')
        
print (f'-' * 20)

Lista_Productos1 = ["manzana", "zanahoria", "kiwi", "pera", "tomate"]

Canastas1 = {
    "frutas": [],     # se llenará con frutas
    "verduras": [],   # se llenará con verduras
    "otros": []       # se llenará con lo que no sea fruta ni verdura
}

def Ejercicio5(Lista, Diccionario):
    Fruta = ["manzana","banana","pera"]
    Verdura = ["zanahoria","lechuga","tomate"]
    for elemento in enumerate(Lista):
        if (elemento[1] in Fruta):
            Diccionario["frutas"].append(elemento[1])
        elif (elemento[1] in Verdura):
            Diccionario["verduras"].append(elemento[1])
        else:
            Diccionario["otros"].append(elemento[1])
            
    return Diccionario

Sample5 = Ejercicio5(Lista_Productos1, Canastas1)

if (Lista_Productos1 and Canastas1):
    if (Sample5):
        print (f'{Sample5}')
    else:
        print (f'Error, el diccionario sufrio algun fallo')
else:
    print (f'Error, o la lista o el diccionario aparecen vacios')
    
print (f'-' * 20)

Lista_Agrupar1 = [("fruta","manzana"), ("verdura","zanahoria"), ("fruta","pera"), ("fruta","banana"), ("verdura","tomate")]

def Ejercicio6(Lista):
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

Sample6 = Ejercicio6(Lista_Agrupar1)

if (Sample6 is None):
    print (f'Error, la lista esta vacia')
else:
    if (not Sample6):
        print (f'Error, el diccionario resultado esta vacio')
    else:
        print (f'Diccionario Resultado: {Sample6}')
        for indice, elemento in Sample6.items():
            for finale in elemento[0:None]:
                print (f'{finale}')
                
print (f'-' * 20)

Datos1 = {
    "ana":  {"edad": 25, "ciudad": "Quito"},
    "luis": {"edad": 30, "ciudad": "Guayaquil"}
    }

def Ejercicio7(Diccionario, User, Field, New_Value):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        return (False, f'Not Ok, User Not Found')
    else:
        Ubicado2 = Ubicado1.get(Field)
        if (Ubicado2 is not None):
            Diccionario[User][Field] = New_Value
            return (True, f'Ok, User Found, Field Found')
        else:
            return (False, f'Not Ok, Field Not Found')

Usuario3 = 'luis'
Campo3 = 'ciudad'
Nuevo_Valor3 = 'Cartago'

Sample7 = Ejercicio7(Datos1, Usuario3, Campo3, Nuevo_Valor3)

if (len(Datos1) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample7[0] == True):
        print (f'{Sample7[1]}')
    else:
        print (f'{Sample7[1]}')
        
print (f'-' * 20)

def Sumando1(Num1):
    return Num1 + 10

def Multiplicando1(Num1):
    return Num1 * 10

def Elegir_Operacion1(Funcion, Num):
    return Funcion(Num)

print (f'El resultado de la operacion 1 es {Elegir_Operacion1(Sumando1, 5)}')
print (f'El resultado de la operacion 2 es {Elegir_Operacion1(Multiplicando1, 5)}')

print (f'-' * 20)

Lista_Nombres1 = ['Erick', 'Josue', 'Karlita']
Lista_Nombres2 = list(['Carmelo', 'Susanita', 'Roxana'])

def Listando1(Lista):
    return Lista

def Listando2(Lista):
    return Lista

def Elegir_Lista(Funcion, Lista):
    return Funcion(Lista)

print (f'Elementos lista 1: {Elegir_Lista(Listando1, Lista_Nombres1)}')
print (f'Elementos lista 2: {Elegir_Lista(Listando2, Lista_Nombres2)}')

print (f'-' * 20)

def Sumando2(Num, *args, **kwargs):
    Acumulador = 0
    for elemento in kwargs.values():
        Acumulador += elemento
        
    return Num + sum(args) + Acumulador

def Multiplicando2(Num, *args, **kwargs):
    Acumulador = 0
    for elemento in kwargs.values():
        Acumulador += elemento
        
    return Num * sum(args) * Acumulador

def Elegir_Operacion2(Funcion, Num, *args, **kwargs):
    return Funcion(Num, *args, **kwargs)

print (f'El resultado de la operacion 1 es: {Elegir_Operacion2(Sumando2, 2, 1, 2, 3, 4, 5, Numerito1 = 15, Numerito2 = 20)}')
print (f'El resultado de la operacion 1 es: {Elegir_Operacion2(Multiplicando2, 2, 1, 2, 3, 4, 5, Numerito1 = 15, Numerito2 = 20)}')

print (f'-' * 20)

Diccionario_Numeral1 = {
    'Num1' : 7,
    'Num2' : 2,
    'Num3' : 8,
    'Num4' : 0,
    'Num5' : 1
}

def Pares(Diccionario):
    Lista_Pares = list([])
    
    for indice, elemento in Diccionario.items():
        if (elemento % 2 == 0):
            Lista_Pares.append(indice)
        else:
            continue
        
    return Lista_Pares

def ImPares(Diccionario):
    Lista_ImPares = list([])
    
    for indice, elemento in Diccionario.items():
        if (elemento % 2 != 0):
            Lista_ImPares.append(indice)
        else:
            continue
        
    return Lista_ImPares

def Filtrar_Lista1(Funcion, Diccionario):
    return Funcion(Diccionario)

print (f'La lista de numeros pares es {Filtrar_Lista1(Pares, Diccionario_Numeral1)}')
print (f'La lista de numeros impares es {Filtrar_Lista1(ImPares, Diccionario_Numeral1)}')

print (f'-' * 20)

Lista_Animales1 = ['Coyote']
Lista_Animales1.append('Ballena')
Lista_Animales1.insert(3, 'Escarabajo')
Lista_Animales1.extend(['Gato', 'Tigre'])

def Ejercicio8(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        while (Contador < len(Lista)):
            print (f'{Lista}')
            del Lista[-1]

Sample8 = Ejercicio8(Lista_Animales1)

if (Sample8 is None):
    print (f'Error, la lista esta vacia')
else:
    Sample8 = Ejercicio8(Lista_Animales1)
    
print (f'-' * 20)

def Ejercicio9(Num1:int, Num2:int) -> int:
    '''Esto es un docstring, la funcion suma dos argumentos y devuelve el resultado'''
    return Num1 + Num2

Sample9 = Ejercicio9(12, 7)

print (f'El resultado de la operacion es {Sample9}')

print (f'{help(Ejercicio9)}')

print (f'-' * 20)

def Ejercicio10(Texto = 'Nada asignado'):
    return Texto

Sample10 = Ejercicio10()

print (f'{Sample10}')

print (f'-' * 20)

def Ejercicio11(Num1, Num2, Num3):
    return Num1 + Num2 + Num3

Sample11 = Ejercicio11(1, 2, 3)

print (f'El resultado de la operacion es {Sample11}')

print (f'-' * 20)

def Ejercicio12(Num1=10, Num2=20, Num3=30):
    return Num1 + Num2 + Num3

Sample12 = Ejercicio12()

print (f'El resultado de la operacion es {Sample12}')

print (f'-' * 20)

def Ejercicio13(Num1=10, Num2=20, Num3=30):
    return Num1 + Num2 + Num3

Sample13 = Ejercicio13(0, 0, 1)

print (f'El resultado de la operacion es {Sample13}')

print (f'-' * 20)

def Ejercicio14(Num1, Num2, Num3=30):
    return Num1 + Num2 + Num3

Sample14 = Ejercicio14(1, 1)

print (f'El resultado de la operacion es {Sample14}')

print (f'-' * 20)

def Ejercicio15(*args):
    Promedio = sum(args) / len(args)
    return Promedio

Sample15 = Ejercicio15(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print (f'El promedio de los numeros elegidos es {round(Sample15, 2)}')

print (f'-' * 20)

def Ejercicio16(**kwargs):
    Acumulador = 0
    for _, elemento in kwargs.items(): # El primer valor no se va a usar por eso usamos el _, es una buena practica
        Acumulador += elemento
        
    return Acumulador

Sample16 = Ejercicio16(
    Numero1 = 5,
    Numero2 = 2,
    Numero3 = 6,
    Numero4 = 1,
    Numero5 = 0
)

if (Sample16):
    print (f'El resultado de la suma de los elementos del **kwargs es {Sample16}')
else:
    print (f'Error, la suma no fue exitosa')
    
print (f'-' * 20)

def Ejercicio17(Num, *args, **kwargs):
    Acumulador = 0
    
    for elemento in kwargs.values():
        Acumulador += elemento
        
    return Num + sum(args) + Acumulador

Sample17 = Ejercicio17(
    5,
    1, 2, 3, 4, 5,
    Numerito1 = 50, Numerito2 = 60
)

print (f'El resultado de la operacion es {Sample17}')

print (f'-' * 20)

def Ejercicio18(*participantes, **detalles):
    print (f'Participantes del evento: ')
    
    for indice, elemento in enumerate(participantes, start=1):
        print (f'{indice} : {elemento}')
        
    print (f'-' * 20)
    
    print (f'Detalles del evento: ')

    for indice, elemento in detalles.items():
        print (f'{indice} : {elemento}')

Sample18 = Ejercicio18(
    'Roberto', 'Susanita', 'Carmencita',
    Fecha = 'Domingo', Lugar = 'Iglesia de Chomes', Actividad = 'Gran Bingo Mensual'
)

print (f'-' * 20)

def Ejercicio19(Limite):
    Lista_Fibonacci = [0, 1]
    while (len(Lista_Fibonacci) < Limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

Sample19 = Ejercicio19(10)

print (f'La lista Fibonacci es {Sample19}')

print (f'-' * 20)

Lista_Primera = [7, 5]
Lista_Segunda = [6, 9]

def Ejercicio20(Lista1, Lista2):
    Set_Conjunto = set({})
    Lista_Finale = list([])
    
    for elemento in Lista1[0:None]:
        if (elemento in Lista2):
            Set_Conjunto.add(elemento)
        else:
            continue
        
    Lista_Finale = list(Set_Conjunto)
    
    return Lista_Finale

Sample20 = Ejercicio20(Lista_Primera, Lista_Segunda)

if (len(Lista_Primera) != 0 and Lista_Segunda):
    if (Sample20):
        print (f'La lista de numeros que cumplen esta condicion es {Sample20}')
    else:
        print (f'Error, no hay numeros que cumplan esta condicion')
else:
    print (f'Error, al menos una de las listas esta vacia')
    
print (f'-' * 20)

var0 = 3

print (f'El tipo de dato es {type(var0)}')

var0 += 3.5

print (f'El tipo de dato es {type(var0)}')

print (f'-' * 20)

var0 = '5'

print (f'El tipo de dato es {type(var0)}')

var0 = int(var0)

print (f'El tipo de dato es {type(var0)}')

print (f'-' * 20)

Lista_Nombres3 = ['Erick', 'Josue', 'Karlita']
Lista_Nombres4 = list(['Carmelo'])

Tupla_Nombres3 = ('Erick', 'Josue', 'Karlita',)
Tupla_Nombres4 = tuple(('Carmelo',))

print (f'{Lista_Nombres3 + Lista_Nombres4}')

print (f'{Tupla_Nombres3 + Tupla_Nombres4}')

print (f'-' * 20)

var1 = 0

if (var1):
    print (f'Correcto, esto puede ser numero entero, decimal y negativo')
else:
    print (f'Error, esto no puede ser nunca 0')
    
print (f'-' * 20)

var2 = ''

if (var2):
    print (f'Correcto, esto puede ser texto de cualquier tipo')
else:
    print (f'Error, esto no puede estar vacio')
    
print (f'-' * 20)

var3 = []

if (var3):
    print (f'Correcto, esto puede ser una lista con contenido')
else:
    print (f'Error, la lista no puede estar vacia')
    
print (f'-' * 20)

var4 = dict({

})

if (var4):
    print (f'Correcto, esto puede ser un diccionario con contenido')
else:
    print (f'Error, el diccionario no puede estar vacio')
    
print (f'-' * 20)

var5 = None

if (var5):
    print (f'Correcto, esto debe tener un valor asignado')
else:
    print (f'Error, la variable debe tener un contenido asignado')
    
print (f'-' * 20)

if not (var5):
    print (f'Correcto, esto debe tener un valor asignado')
else:
    print (f'Error, la variable debe tener un contenido asignado')
    
print (f'-' * 20)

Lista_Ejemplo1 = [1, 2, 3, 4, 5]

def Ejercicio21(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        
        while (Contador < len(Lista[:])):
            Contador += 1
            
        return Contador

Sample21 = Ejercicio21(Lista_Ejemplo1)

if (Sample21 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample21):
        print (f'La cantidad de nuemeros en la lista es {Sample21}')
    else:
        print (f'Otra vez aparece la lista vacia')
        
print (f'-' * 20)

def Ejercicio22(Lista):
    Suma_Pares = 0
    Suma_Impares = 0
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Suma_Pares += elemento
        else:
            Suma_Impares += elemento
            
    return Suma_Pares, Suma_Impares

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    Sample22 = Ejercicio22(Lista_Ejemplo1)
    Result_Suma_Pares, Result_Suma_Impares = Sample22
    
    print (f'El resultado de la suma de los pares es {Result_Suma_Pares}')
    print (f'El resultado de la suma de los impares es {Result_Suma_Impares}')

print (f'-' * 20)

def Ejercicio23(Lista):
    Acumulador = 0
    
    for elemento in Lista[0:None]:
        Acumulador += elemento
        
    return Acumulador

Sample23 = Ejercicio23(Lista_Ejemplo1)

if (Lista_Ejemplo1):
    print (f'El resultado de la sumatoria es {Sample23}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio24(Lista):
    if (len(Lista) == 0):
        return None
    else:
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

Sample24 = Ejercicio24(Lista_Ejemplo1)

if (Sample24 is None):
    print (f'Error, la lista esta vacia')
else:
    Resultado1, Resultado2, Resultado3, Resultado4 = Sample24
    
    print (f'El resultado de la sumatoria 1 es {Resultado1}')
    print (f'El resultado de la sumatoria 2 es {Resultado2}')
    print (f'El resultado de la sumatoria 3 es {Resultado3}')
    print (f'El resultado de la sumatoria 4 es {Resultado4}')
    
print (f'-' * 20)

def Ejercicio25(Lista, Num):
    Founder = False
    for elemento in Lista[0:None]:
        if (elemento == Num):
            Founder = True
            break
        else:
            continue
        
    return Founder

Numerito1 = 3

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    Sample25 = Ejercicio25(Lista_Ejemplo1, Numerito1)
    if (Sample25 == True):
        print (f'El numero {Numerito1} fue encontrado')
    else:
        print (f'Error, el numero no fue encontrado en la lista')
        
print (f'-' * 20)

def Ejercicio26(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Menore = min(Lista)
        Mayore = max(Lista)
        Lista_Resultado = [Menore, Mayore]
        return Lista_Resultado

Sample26 = Ejercicio26(Lista_Ejemplo1)

if (Sample26 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero menor de la lista es {min(Sample26)}')
    print (f'El numero mayor de la lista es {max(Sample26)}')
    
print (f'-' * 20)

def Ejercicio27(Lista, Num):
    Contador = 0
    for elemento in Lista[:]:
        if (elemento > Num):
            Contador += 1
        else:
            continue
        
    return Contador

Numerito2 = 2

Sample27 = Ejercicio27(Lista_Ejemplo1, Numerito2)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample27):
        print (f'La cantidad de numeros mayores que {Numerito2} es {Sample27}')
    else:
        print (f'Error, no hay ningun numero mayor que {Numerito2}')
        
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

def Ejercicio29(Lista):
    Lista_Mult = []
    
    for elemento in enumerate(Lista):
        Lista_Mult.append(elemento[1] * 2)
        
    return Lista_Mult

Sample29 = Ejercicio29(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Ejemplo1}')
    print (f'Lista Multiplicada: {Sample29}')
    
print (f'-' * 20)

'''Contador = 0

Lista_Promedio = list([])
while (Contador < 3):
    while (True):
        Numerito1 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito2 = float(Numerito1)
            if (Numerito2.is_integer()):
                print (f'La nota {Contador + 1} es un numero entero')
                Lista_Promedio.append(Numerito2)
                break
            else:
                print (f'La nota {Contador + 1} es un numero decimal')
                Lista_Promedio.append(Numerito2)
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador += 1
    
Promedio1 = sum(Lista_Promedio) / len(Lista_Promedio)

print (f'El promedio de los numeros ingresados es {round(Promedio1, 2)}')'''

Lista_Ejemplo2 = list([5, -6, 0, -8, -3, 0])

def Ejercicio30(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Positivos = 0
        Negativos = 0
        Ceros = 0
        
        for elemento in Lista[0:None]:
            if (elemento > 0):
                Positivos += 1
            elif (elemento < 0):
                Negativos += 1
            else:
                Ceros += 1
                
        return Positivos, Negativos, Ceros

Sample30 = Ejercicio30(Lista_Ejemplo2)

if (Sample30 is None):
    print (f'Error, la lista esta vacia')
else:
    Num_Positivos, Num_Negativos, Num_Ceros = Sample30
    
    print (f'Total numeros Positivos: {Num_Positivos}')
    print (f'Total numeros Negativos: {Num_Negativos}')
    print (f'Total numeros Ceros: {Num_Ceros}')
    
print (f'-' * 20)

import re

Lista_Ejemplo3 = [
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
]

def Ejercicio31(Lista):
    Validos = []
    Invalidos = []
    Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'
    
    for elemento in Lista:
        Buscar = bool(re.fullmatch(Pattern, elemento))
        if (Buscar == True):
            Validos.append(elemento)
        else:
            Invalidos.extend([elemento])
            
    return Validos, Invalidos

Sample31 = Ejercicio31(Lista_Ejemplo3)

if (len(Lista_Ejemplo3) == 0):
    print (f'Error, la lista esta vacia')
else:
    Lista_Validos, Lista_Invalidos = Sample31
    print (f'Lista Original: {Lista_Ejemplo3}')
    print (f'Lista Validos: {Lista_Validos}')
    print (f'Lista Invalidos: {Lista_Invalidos}')
    
print (f'-' * 20)

def Ejercicio32(Lista):
    Temporal = Lista[0]
    
    for elemento in Lista:
        if (elemento > Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

if (Lista_Ejemplo1):
    Sample32 = Ejercicio32(Lista_Ejemplo1)
    print (f'El numero mayor de la lista es {Sample32}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio33(Lista):
    Temporal = Lista[0]
    
    for elemento in Lista:
        if (elemento < Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

if (Lista_Ejemplo1):
    Sample33 = Ejercicio33(Lista_Ejemplo1)
    print (f'El numero menor de la lista es {Sample33}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejemplo4 = [-15.5, -8, -3.2, -1, 0, 4, 7.5, 12, 19.1, 25]

def Ejercicio34(Lista):
    if (len(Lista) == 0):
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

Sample34 = Ejercicio34(Lista_Ejemplo4)

if (Sample34 is None):
    print (f'Error, la lista esta vacia')
else:
    Contador1, Acumulador1 = Sample34
    
    print (f'La cantidad de numeros positivos es {Contador1}')
    print (f'La suma total de los numeros positivos es {Acumulador1}')
    
print (f'-' * 20)

Lista_Ejemplo5 = list([65, 70, 54, 80, 69, 66])

def Ejercicio35(Lista):
    Aprobados = 0
    Reprobados = 0
    Aprobados_Sum = 0
    
    for elemento in enumerate(Lista[0:None]):
        if (elemento[1] >= 70):
            Aprobados += 1
            Aprobados_Sum += elemento[1]
        else:
            Reprobados += 1
            
    return Aprobados, Reprobados, Aprobados_Sum

if (len(Lista_Ejemplo5) == 0):
    print (f'Error, la lista esta vacia')
else:
    Sample35 = Ejercicio35(Lista_Ejemplo5)
    Num_Aprobados, Num_Reprobados, Num_Aprobados_Sum = Sample35
    
    print (f'La cantidad de estudiantes aprobados es {Num_Aprobados}')
    print (f'La cantidad de estudiantes reprobados es {Num_Reprobados}')
    print (f'La sumatoria de las notas aprobadas es {Num_Aprobados_Sum}')
    
print (f'-' * 20)

Lista_Ejemplo6 = [15, 0, 8, 2, 0, 25, 4]

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
            
    return Agotados, Stock_Bajo, Stock_Alto, Stock_Bajo_Sum, Stock_Alto_Sum

Sample36 = Ejercicio36(Lista_Ejemplo6)

if (Lista_Ejemplo6):
    Prod_Agotados, Prod_Stock_Bajo, Prod_Stock_Alto, Prod_Stock_Bajo_Sum, Prod_Stock_Alto_Sum = Sample36
    print (f'Productos Agotados: {Prod_Agotados}')
    print (f'Productos Stock_Bajo: {Prod_Stock_Bajo}')
    print (f'Productos Stock_Alto: {Prod_Stock_Alto}')
    print (f'Productos Stock_Bajo_Sum: {Prod_Stock_Bajo_Sum}')
    print (f'Productos Stock_Alto_Sum: {Prod_Stock_Alto_Sum}')
    print (f'Productos Totales: {Prod_Stock_Bajo_Sum + Prod_Stock_Alto_Sum}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejemplo7 = list([12, 8, 5, 1, 7, 2, 10])

def Ejercicio37(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        while (Contador < len(Lista)):
            if (Lista[Contador] == 0):
                return Contador
            else:
                Contador += 1
                continue
            
        return False

Sample37 = Ejercicio37(Lista_Ejemplo7)

if (Sample37 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample37 is False):
        print (f'Actualmente no hay ningun producto agotado en el inventario')
    else:
        print (f'El primer producto agotado del inventario aparece en la posicion {Sample37}')
        
print (f'-' * 20)

Lista_Ejemplo8 = [120, 350, 80, 600, 150, 700]

def Ejercicio38(Lista, Num):
    Contador = 0
    Lista.sort()
    Lista.sort(reverse = True)
    Lista.reverse()
    while (Contador < len(Lista[0:None])):
        if (Lista[Contador] > Num):
            return Contador
        else:
            Contador += 1
            continue

Monto1 = 700

if (len(Lista_Ejemplo8) == 0):
    print (f'Error, la lista esta vacia')
else:
    Sample38 = Ejercicio38(Lista_Ejemplo8, Monto1)
    if (Sample38 is None):
        print (f'Error, no hay ninguna venta que supere al monto ${Monto1}')
    else:
        print (f'La primera venta que supera al limite ${Monto1} aparece en la posicion {Sample38}')
        
print (f'-' * 20)

# Metodo para encontrar numeros repetidos en una lista #1

Lista_Ejemplo9 = list([10, 1, 2, 4, 3, 5, 6])

def Ejercicio39(Lista):
    for i in range(0, len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                return i
            else:
                continue
            
    return None

Sample39 = Ejercicio39(Lista_Ejemplo9)

if (Lista_Ejemplo9):
    if (Sample39 is None):
        print (f'Error, no hay ningun numero repetido en la lista')
    else:
        print (f'El primer numero repetido aparece en la posicion {Sample39} y el numero es {Lista_Ejemplo9[Sample39]}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

# Metodo para encontrar numeros repetidos en una lista #2

Lista_Ejemplo10 = list([10, 2, 1, 4, 3, 5, 6])

def Ejercicio40(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            
    return None

Sample40 = Ejercicio40(Lista_Ejemplo10)

if (Lista_Ejemplo10):
    if (Sample40 is None):
        print (f'Error, no hay ningun numero repetido en la lista')
    else:
        print (f'El primer numero repetido de la lista es {Sample40}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejemplo11 = [90, 80, 79, 78]

def Ejercicio41(Lista):
    Lista.sort()
    for i in range(0 + 1, len(Lista[:])):
        if (Lista[i - 1] < Lista[i]):
            return i
        else:
            continue
        
    return None

Sample41 = Ejercicio41(Lista_Ejemplo11)

if (len(Lista_Ejemplo11) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample41 is None):
        print (f'Error, no hay ningun aumento consecutivo')
    else:
        print (f'El primer aumento consecutivo aparece en la posicion {Sample41} y sucede con el numero {Lista_Ejemplo11[Sample41]}')
        
print (f'-' * 20)

Lista_Ejemplo12 = list([100, 97, 95, 80, 78])

def Ejercicio42(Lista, Num):
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] - Lista[i] >= Num):
            return Lista[i - 1], Lista[i], i
        else:
            continue
        
    return None

Limite1 = 30

Sample42 = Ejercicio42(Lista_Ejemplo12, Limite1)

if (Lista_Ejemplo12):
    if (Sample42 is None):
        print (f'No hubo una caida drastica durante la ultima hora')
    else:
        Anterior1, Actual1, Posicion1 = Sample42
        print (f'Alerta! acaba de haber una caida de temperatura de {Anterior1 - Actual1} grados')
        print (f'Temperatura anterior: {Anterior1} grados')
        print (f'Temperatura actual: {Actual1} grados')
        print (f'Posicion donde sucede la caida: {Posicion1}')
        print (f'Caida de temperatura en grados: {Anterior1 - Actual1}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejemplo13 = [1, 1, 0, 1, 3]

def Ejercicio43(Lista):
    for i in range(0 + 2, len(Lista[0:None])):
        if (Lista[i - 2] < Lista[i - 1] > Lista[i]):
            return i - 1
        else:
            continue
        
    return None

Sample43 = Ejercicio43(Lista_Ejemplo13)

if (len(Lista_Ejemplo13) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample43 is None):
        print (f'Error, no hay ningun numero en la lista que genere un pico')
    else:
        print (f'El pico sucede en la posicion {Sample43} y el numero que genera este pico es {Lista_Ejemplo13[Sample43]}')
        
print (f'-' * 20)

# Consultar valores ✅ Consultar.

Capitales1 = {"Costa Rica": "San José", "México": "Ciudad de México", "Italia": "Roma", "Argentina": "Buenos Aires", "España": "Madrid"}

def Ejercicio44(Diccionario, Texto):
    if (len(Diccionario) == 0):
        return None
    else:
        Ubicado1 = Diccionario.get(Texto)
        if (Ubicado1):
            return Ubicado1
        else:
            return (False)
    
Pais1 = 'Italia'

Sample44 = Ejercicio44(Capitales1, Pais1)

if (Sample44 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample44 == False):
        print (f'Error, el pais seleccionado no aparece en la base de datos')
    else:
        print (f'La capital de {Pais1} es {Sample44}')
        
print (f'-' * 20)

Productos1 = {"Laptop": 1200, "Mouse": 25, "Teclado": 45, "Monitor": 300}

def Ejercicio45(Diccionario, Articulo):
    Ubicado1 = Diccionario.get(Articulo)
    if (Ubicado1 is None):
        return False
    else:
        return Ubicado1

Item1 = 'Escoba'

if (len(Productos1) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Sample45 = Ejercicio45(Productos1, Item1)
    if (Sample45 == False):
        print (f'Error, este producto no es parte del inventario')
    else:
        print (f'El precio del articulo {Item1} es ${Sample45}')
        
print (f'-' * 20)

# Actualizar elementos ✅ Actualizar.

Productos2 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300
}

def Ejercicio46(Diccionario, Articulo, Precio):
    Ubicado1 = Diccionario.get(Articulo)
    if (Ubicado1 is None):
        return False
    else:
        Diccionario[Articulo] = Precio
        return Diccionario

Item2 = 'Escoba'
Price2 = 55

Sample46 = Ejercicio46(Productos2, Item2, Price2)

if (Productos2):
    if (Sample46 == False):
        print (f'El articulo seleccionado no aparece en el inventario')
    else:
        print (f'{Sample46}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

# Agregar elementos ✅ Agregar.

Productos3 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio47(Diccionario, Articulo, Precio):
    if (Diccionario):
        Ubicado1 = Diccionario.get(Articulo)
        if (Ubicado1 is None):
            Diccionario[Articulo] = Precio
            return (True, f'El producto fue agregado al inventario')
        else:
            return (False, f'Error, el producto ya existe en el inventario')
    else:
        return None
    
Item3 = 'Teclado'
Price3 = 200

Sample47 = Ejercicio47(Productos3, Item3, Price3)

if (Sample47 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample47[0] == True):
        print (f'{Sample47[1]}')
    else:
        print (f'{Sample47[1]}')
        
print (f'-' * 20)

# Eliminar elementos ✅ Eliminar.

Productos4 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio48(Diccionario, Articulo):
    Ubicado1 = Diccionario.get(Articulo)
    if (Ubicado1 is None):
        return False
    else:
        del Diccionario[Articulo]
        return Diccionario

Item4 = 'Escoba'

if (len(Productos4) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Sample48 = Ejercicio48(Productos4, Item4)
    if (Sample48 == False):
        print (f'Error, el producto no existe, no se puede eliminar')
    else:
        print (f'{Sample48}')
        
print (f'-' * 20)

Productos5 = {
    "Laptop": 60,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 20,
    "Impresora": 180
}

def Ejercicio49(Diccionario):
    Clave = next(iter(Diccionario))
    Valor = Diccionario[Clave]
    
    for indice, elemento in Diccionario.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    return Clave, Valor

Sample49 = Ejercicio49(Productos5)

if (Productos5):
    Clave1, Valor1 = Sample49
    print (f'Nombre Producto: {Clave1}')
    print (f'Precio Producto: ${Valor1}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Productos6 = {
    "Laptop": 1200,
    "Mouse": 50,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio50(Diccionario):
    Diccionario_Sorted = dict(sorted(Diccionario.items(), key= lambda item : item[1]))
    Clave = next(iter(Diccionario_Sorted))
    Valor = Diccionario_Sorted[Clave]
    for indice, elemento in Diccionario_Sorted.items():
        if (elemento < Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    return Clave, Valor

Sample50 = Ejercicio50(Productos6)

if (Productos6):
    Clave1, Valor1 = Sample50
    print (f'Nombre Producto: {Clave1}')
    print (f'Precio Producto: ${Valor1}')
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

def Ejercicio51(Diccionario, Num):
    Diccionario_Sorted = dict(sorted(Diccionario.items(), key= lambda item : item[1]))
    for indice, elemento in Diccionario_Sorted.items():
        if (elemento > Num):
            return indice
        else:
            continue
            
    return None
    
Limite2 = 100

Sample51 = Ejercicio51(Ventas2, Limite2)

if (len(Ventas2) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample51 is None):
        print (f'Error, no hay ninguna venta superior al monto limite')
    else:
        print (f'La venta que supera el limite sucedio el {Sample51}')
        
print (f'-' * 20)

Productos7 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio52(Diccionario, Num):
    Contador = 0
    for _, elemento in Diccionario.items():
        if (elemento > Num):
            Contador += 1
        else:
            continue
        
    return Contador

Limite3 = 2000

if (len(Productos7) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Sample52 = Ejercicio52(Productos7, Limite3)
    if (Sample52):
        print (f'La cantidad de productos cuyo precio es mayor que ${Limite3} es {Sample52}')
    else:
        print (f'Error, no hay ningun producto cuyo precio sea mayor al limite')
        
print (f'-' * 20)

Ventas3 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio53(Diccionario):
    Acumulador1 = 0
    for elemento in Diccionario.values():
        Acumulador1 += elemento
        
    return Acumulador1

Sample53 = Ejercicio53(Ventas3)

if (Ventas3):
    if (Sample53 == 0):
        print (f'Error, no se pudo realizar la sumatoria')
    else:
        print (f'El resultado de la suma de los elementos del diccionario es {Sample53}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Ventas4 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio54(Diccionario, Num):
    Acumulador1 = 0
    for elemento in Diccionario.values():
        if (elemento > Num):
            Acumulador1 += elemento
        else:
            continue
        
    return Acumulador1

Limite4 = 1000

Sample54 = Ejercicio54(Ventas4, Limite4)

if (len(Ventas4) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample54):
        print (f'La suma de las ventas que superan el monto es {Sample54}')
    else:
        print (f'Error, no hay ninguna venta que supere el limite ${Limite4}')
        
print (f'-' * 20)

Productos8 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio55(Diccionario, Num):
    Contador1 = 0
    Acumulador1 = 0
    
    for elemento in Diccionario.values():
        if (elemento > Num):
            Contador1 += 1
            Acumulador1 += elemento
        else:
            continue
        
    return Contador1, Acumulador1

Limite5 = 150

if (len(Productos8) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Sample55 = Ejercicio55(Productos8, Limite5)
    Contador2, Acumulador2 = Sample55
    if (Contador2 == 0 and Acumulador2 == 0):
        print (f'Error, no hay ningun precio mayor al limite')
    else:
        print (f'Cantidad precios mayores que el limite {Contador2}')
        print (f'La suma de los precios mayores que el limite es ${Acumulador2}')
        
print (f'-' * 20)

Productos9 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio56(Diccionario, Num):
    Diccionario_Sorted = dict(sorted(Diccionario.items(), key= lambda item : item[1]))
    Clave = next(iter(Diccionario_Sorted))
    Valor = Diccionario_Sorted[Clave]
    for indice, elemento in Diccionario_Sorted.items():
        if (elemento > Num):
            Clave = indice
            Valor = elemento
            return Clave, Valor
        else:
            continue
        
    return None

Limite6 = 150

if (Productos9):
    Sample56 = Ejercicio56(Productos9, Limite6)
    if (Sample56 is None):
        print (f'Error, no hay ningun producto con un precio mayor al limite')
    else:
        Clave2, Valor2 = Sample56
        print (f'Producto Nombre: {Clave2}')
        print (f'Producto Precio: ${Valor2}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Lista_Ejemplo14 = list(["python", "java", "python", "c++", "java", "python", "go", "c++", "python"])

def Ejercicio57(Lista): #type: ignore
    Diccionario_Vacio = dict({})
    
    for elemento in Lista[:]:
        if (elemento not in Diccionario_Vacio):
            Diccionario_Vacio[elemento] = 0
            Diccionario_Vacio[elemento] += 1
        else:
            Diccionario_Vacio[elemento] += 1
            
    return Diccionario_Vacio

Sample57 = Ejercicio57(Lista_Ejemplo14)

if (len(Lista_Ejemplo14) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample57):
        for indice, elemento in Sample57.items():
            print (f'{indice} : {elemento}')
    else:
        print (f'Error, por alguna razon, el diccionario vacio se mantiene vacio')
        
print (f'-' * 20)

Sample57_Sorted = dict(sorted(Sample57.items(), key= lambda item : item[1]))
Sample57_Sorted_Min = min(Sample57_Sorted.items(), key=lambda item : item[1])
Sample57_Sorted_Max = max(Sample57_Sorted.items(), key=lambda item : item[1])

print (f'{Sample57}')
print (f'{Sample57_Sorted}')
print (f'{Sample57_Sorted_Min}')
print (f'{Sample57_Sorted_Max}')

print (f'-' * 20)

Paises1 = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}

def Ejercicio58(Diccionario, Codigo):
    Ubicado1 = Diccionario.get(Codigo)
    if (Ubicado1 is None):
        return False
    else:
        return Codigo, Ubicado1

if (Paises1):
    Sample58 = Ejercicio58(Paises1, 'us')
    if (Sample58 == False):
        print (f'Error, este codigo no pertenece a ningun pais')
    else:
        Codigo1, Pais2 = Sample58
        print (f'El codigo {Codigo1} pertenece al pais {Pais2}')
else:
    print (f'Error, el diccioanrio esta vacio')
    
print (f'-' * 20)

class Persona1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
        
Objeto1 = Persona1('Erick')

print (f'Mi nombre es {Objeto1}')

print (f'-' * 20)

class Colores1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Colores1 = [
    Colores1('Amarillo'),
    Colores1('Azul'),
    Colores1('Gris')
]

print (f'Lista Colores: {Lista_Colores1}')

print (f'-' * 20)

class Inventario1():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto2 = Inventario1()

Objeto2.Productos.append('Cuaderno')
Objeto2.Productos.insert(1, 'Lapicero')
Objeto2.Productos.extend(['Borrador'])

print (f'El inventario esta compuesto por {len(Objeto2)} elementos')

print (f'-' * 20)

class Igualdad():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
        
Objeto3 = Igualdad('Erick')
Objeto4 = Igualdad('Erick')

if (Objeto3 == Objeto4):
    print (f'Correcto, ambos objetos son iguales')
else:
    print (f'Error, los objetos no son iguales')
    
print (f'-' * 20)

class Caja1():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso
        
Objeto5 = Caja1(5)
Objeto6 = Caja1(3)

print (f'El resultado de la sumatoria es {Objeto5 + Objeto6}')

print (f'-' * 20)

class Armario1():
    def __init__(self):
        self.Ropa = [
            'Zapatos',
            'Camiseta',
            'Pantalones'
        ]
        
    def __getitem__(self, Indice):
        return self.Ropa[Indice]
        
Objeto7 = Armario1()

print (f'En la posicion 0 aparece la prenda {Objeto7[0]}')
print (f'En la posicion 1 aparece la prenda {Objeto7[1]}')
print (f'En la posicion 2 aparece la prenda {Objeto7[2]}')

print (f'-' * 20)

class Panaderia1():
    def __init__(self):
        self.Panes = [
            'Baguette',
            'Donas',
            'Croissant'
        ]
        
    def __iter__(self):
        return iter(self.Panes)
        
Objeto8 = Panaderia1()

for indice, elemento in enumerate(Objeto8, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

from Module_Own import Pokemon1 as Poke1

Objeto9 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto10 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Mega Sismo')

Objeto9.Mostrar()

print (f'-' * 20)

Objeto10.Mostrar()

print (f'-' * 20)

print (f'El pokemon es {Objeto9.Nombre}')
print (f'El pokemon es {Objeto9}')

print (f'-' * 20)

print (f'El pokemon es {Objeto10.Nombre}')
print (f'El pokemon es {Objeto10}')

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
        
Objeto13 = Perro('Terry', 5, 2.5, 'Dobberman', 'Asma De Perro')

Veterinaria.Mostrar(Objeto13)
Objeto13.Mostrar()

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

print (f'-' * 20)

class Pajaro(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto15 = Pajaro('Polly', 31, 0.4, 'Guacamaya Roja', 'Si')

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
        
Objeto16 = Paladin(25, 'Battle Axe', 75, 'Dark Crystal', 200, 'Ghost Knight')

Objeto16.Mostrar()
Atacante.Mostrar(Objeto16)
Defensor.Mostrar(Objeto16)

print (f'-' * 20)

Hija_Padre = issubclass(Poke_Kid1, Poke1)

print (f'{Hija_Padre}')

Instancia1 = isinstance(Objeto16, Defensor)
Instancia2 = isinstance(Objeto16, Atacante)
Instancia3 = isinstance(Objeto16, Paladin)
Instancia4 = isinstance(Objeto16, Poke_Kid1)

print (f'{Instancia1}')
print (f'{Instancia2}')
print (f'{Instancia3}')
print (f'{Instancia4}')

print (f'-' * 20)

class A1():
    def Mostrar(self):
        print (f'Hola nuevamente A1')
        
class E1():
    def Mostrar(self):
        print (f'Hola nuevamente E1')
        
class B1(E1):
    def Mostrar(self):
        print (f'Hola nuevamente B1')
        
class C1(A1):
    def Mostrar(self):
        print (f'Hola nuevamente C1')
        
class D1(B1, C1):
    def Mostrar(self):
        print (f'Hola nuevamente D1')
        
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
        
Objeto18 = Cripto()
Objeto19 = Tarjeta()
Objeto20 = Efectivo()

Objeto18.Pagar()
Objeto19.Pagar()
Objeto20.Pagar()

print (f'-' * 20)

class Cuenta_Bancaria():
    def __init__(self, Saldo):
        self.Saldo = Saldo
        
    def Depositar(self, Dinero):
        self.Saldo += Dinero
      
    @property  
    def Dinero(self):
        return self.Saldo
    
    @Dinero.setter
    def Dinero(self, Nuevo_Saldo):
        self.Saldo = Nuevo_Saldo
    
    def Mostrar(self):
        print (f'Su saldo a la fecha es de ${self.Saldo}')
    
Objeto19 = Cuenta_Bancaria(100)
Objeto19.Depositar(25)
Objeto19.Mostrar()

print (f'Su saldo privado es {Objeto19.Dinero}, nunca muestres este numero')

Objeto19.Dinero = '50,000,000'

Objeto19.Mostrar()

print (f'Su saldo privado es {Objeto19.Dinero}, nunca muestres este numero')

print (f'-' * 20)

class Ejemplar():
    def __init__(self, Nombre):
        self.Nombre = Nombre

    def Mostrar(self):
        print (f'{self.Nombre}')
        
    def __str__(self):
        return self.Nombre
    
    @property
    def Nombrecito(self):
        return self.Nombre
        
Objeto21 = Ejemplar('Erick Perez Gutierrez')

Objeto21.Mostrar()
print (f'{Objeto21}')
print (f'{Objeto21.Nombrecito}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def Generico(self):
        pass

class Sub_Plantilla(Plantilla):
    def Mostrar(self):
        print (f'Este mensaje es de la sub plantilla')
        
    def Generico(self):
        print (f'Esto es el metodo de la plantilla abstraccion')
        
Objeto22 = Sub_Plantilla()

Objeto22.Mostrar()
Objeto22.Generico()

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
        print (f'El entrenador eligio a {self.Favorito.Elegir()} para la batalla')
        
Objeto22 = Battle1()

Objeto22.Batallar()

print (f'-' * 20)

class Battle2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El entrenador eligio a {self.Favorito.Elegir()} para la batalla')
        
Criatura1 = Bulbasaur()
Objeto23 = Battle2(Criatura1)
Objeto23.Batallar()

Criatura2 = Treekoo()
Objeto24 = Battle2(Criatura2)
Objeto24.Batallar()

Criatura3 = Chikorita()
Objeto25 = Battle2(Criatura3)
Objeto25.Batallar()

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
        print (f'Para el programa de hoy, vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Objeto24 = Pastel1()
Objeto24.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Para el programa de hoy, vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
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

class Persona2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def Mostrar(self):
        return self.Nombre
     
    @property   
    def Nombrecito(self):
        return self.Nombre
        
    def __str__(self):
        return self.Nombre
    
Objeto26 = Persona2('Erick Josue Perez Gutierrez')

print (f'Hola, mi nombre completo es {Objeto26.Mostrar()}')
print (f'Hola, mi nombre completo es {Objeto26.Nombrecito}')
print (f'Hola, mi nombre completo es {Objeto26}')

print (f'-' * 20)

'''def Ejercicio59(Numero):
    try:
        Resultado = 12 + Numero * 2
        print (f'El resultado de la operacion es {Resultado}')
    except Exception:
        print (f'Error, lo que ingresaste no es un numero')

Sample59 = Ejercicio59(PEPE.Flotante1)

print (f'-' * 20)

def Ejercicio60(Todito):
    Resultado = eval(Todito)
    print (f'El resultado de la operacion es {Resultado}')

Sample60 = Ejercicio60(PEPE.Flotante2)

print (f'-' * 20)

def Ejercicio61(Texto):
    Cadena = Texto.replace(' ', '')
    try:
        if (isinstance(Cadena, (str))):
            if (Cadena.isalpha()):
                print (f'Lo que ingresaste es un texto')
            else:
                print (f'Error 2')
        else:
            print (f'Error 1')
    except ValueError:
        print (f'Error, lo que ingresaste no es un texto')

Sample61 = Ejercicio61(PEPE.Flotante3)

print (f'-' * 20)

def Ejercicio62(Cadena):
    Lista_Cadena = Cadena.split(' ')
    
    for indice, elemento in enumerate(Lista_Cadena[0:None]):
        print (f'{indice} : {elemento}')
        
    print (f'La cantidad de palabras digitadas es {len(Lista_Cadena)}')

Sample62 = Ejercicio62(PEPE.Flotante4)
'''
'''
Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(0, Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento}: ')
        Lista.append(Alumno)
        
    return Lista

Sample59 = Colegio(Lista_Alumnos)

print (f'La lista de alumnos es {Sample59}')'''

'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

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

Sample59 = Colegio(Lista_Alumnos)'''

'''import requests

Diccionario_API1 = {
    'Nombre' : ["Pistacho", "Chicle", "Pastel"]
}

Unidad1 = requests.get('http://127.0.0.1:8010/unidad1/')
Unidad2 = Unidad1.json()

print (f'{Unidad2}')
print (f'El status code es: {Unidad1.status_code}')

print (f'-' * 20)

Unidad3 = requests.post('http://127.0.0.1:8010/unidad1/toto', json=(Diccionario_API1))
Unidad4 = Unidad3.json()

print (f'{Unidad4}')
print (f'El status code es: {Unidad3.status_code}')'''

var6 = '6'

if (isinstance(var6, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var6.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var6.isdecimal()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
try:
    Numerito3 = float(var6)
    if (Numerito3.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError as Errore1:
    print (f'Error, lo que ingresaste no es un numero entero')
    
print (f'-' * 20)

var7 = 3.45

if (isinstance(var7, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, esto no es un numero decimal')
    
try:
    Numerito4 = float(var7)
    if (Numerito4.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var8 = 3

if (isinstance(var8, (int, float))):
    print (f'Lo que ingresaste es un numero entero o decimal')
else:
    print (f'Error, lo que ingresaste no es un numero')
    
try:
    Numerito5 = float(var8)
    if (Numerito5.is_integer()):
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

Texto1_Version4 = re.sub(r'\!|\@|\d+', '', Texto1_Version3)

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
    print (f'Error, la fecha tiene el formato incorrecto')
    exit()
    
Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrado1 = Cargar_Csv1[Cargar_Csv1["date"].dt.date == Fech1_Formateada.date()]

if (Encontrado1.empty):
    print (f'En esta fecha no se han encontrado ventas')
else:
    print (f'Genial! encontramos ventas papis!!!!')
    
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'El producto que vendio menos en esta fecha fue {Grupo1_Min} y la cantidad de unidades es {Grupo1_Min_Cant}')
    print (f'El producto que vendio mas en esta fecha fue {Grupo1_Max} y la cantidad de unidades es {Grupo1_Max_Cant}')
    
    print (f'La cantidad de productos vendidos fue {Grupo1.sum()}')
    
    print (f'La cantidad de clientes que nos compraron en esta fecha fue {Grupo1.count()}')
    
    Promedio1 = Grupo1.sum() / Grupo1.count()
    
    print (f'El promedio de productos vendidos en esta fecha fue de {round(Promedio1, 2)}')
    print (f'El promedio de productos vendidos en esta fecha fue de {round(Grupo1.mean(), 2)}')
    
    Grupo2 = Encontrado1.groupby('product')['TOTALITO'].sum()
    Grupo2_Min = Grupo2.idxmin()
    Grupo2_Max = Grupo2.idxmax()
    Grupo2_Min_Cant = Grupo2.min()
    Grupo2_Max_Cant = Grupo2.max()
    
    print (f'El producto con precio menor es {Grupo2_Min} ${Grupo2_Min_Cant}')
    print (f'El producto con precio mayor es {Grupo2_Max} ${Grupo2_Max_Cant}')
    
    print (f'La cantidad de productos vendidos en esta fecha fue de {Grupo2.count()}')
    
    print (f'La suma de todas las ventas en $ es de ${Grupo2.sum()}')
    
    Promedio2 = Grupo2.sum() / Grupo2.count()
    
    print (f'El promedio de productos vendidos en esta fecha fue de {round(Promedio2, 2)}')
    print (f'El promedio de productos vendidos en esta fecha fue de {round(Grupo2.mean(), 2)}')
    
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

Texto2_temp1 = Texto2

Pattern2 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|net|org)'

Correos1 = re.findall(Pattern2, Texto2)

print (f'{Correos1}')

for i, email in enumerate(Correos1, start=1):
    Texto2_temp1 = Texto2_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto2_temp1}')

for i, email in enumerate(Correos1, start=1):
    Texto2_temp1 = Texto2_temp1.replace(f'SAMPLE{i}', email)
    
print (f'{Texto2_temp1}')

print (f'-' * 20)

import re

Texto3 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Metodo de solucion #1

Pattern3 = r'\!|\?|\.{2,}|\d{2,4}\-[0-9]{3,}'

Buscar2 = re.sub(Pattern3, '', Texto3)

print (f'{Buscar2}')

print (f'-' * 20)

# Metodo de solucion #2

import re

Pattern4 = r'[^a-zA-Z0-9\s]+'

Buscar3 = re.sub(Pattern4, '', Texto3)

print (f'{Buscar3}')

print (f'-' * 20)

# Metodo de solucion #3

Texto3_temp1 = Texto3

Pattern5 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Correos2 = re.findall(Pattern5, Texto3)

print (f'{Correos2}')

for i, email in enumerate(Correos2, start=1):
    Texto3_temp1 = Texto3_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto3_temp1}')

Pattern6 = r'\!|\?|\.{2,}|\d{1,4}\-[0-9]{4,}'

Texto3_temp2 = re.sub(Pattern6, '', Texto3_temp1)

print (f'{Texto3_temp2}')

for i, email in enumerate(Correos2, start=1):
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

Pattern7 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos3 = re.findall(Pattern7, Texto4)

Texto4_temp1 = Texto4

for i, email in enumerate(Correos3, start=1):
    Texto4_temp1 = Texto4_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto4_temp1}')

Pattern8 = r'\!|\?'

Texto4_temp2 = re.sub(Pattern8, '', Texto4_temp1)

print (f'{Texto4_temp2}')

for i, email in enumerate(Correos3, start=1):
    Texto4_temp2 = Texto4_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto4_temp2}')

print (f'-' * 20)

for elemento in PEPE.Diccionario_Poke.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in PEPE.Diccionario_Poke.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for indice, elemento in PEPE.Diccionario_Poke.items():
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

for elemento in PEPE.Diccionario_Poke:
    print (f'{PEPE.Diccionario_Poke[elemento]}')
    
print (f'-' * 20)

'''Lista_Promedios = []

Contador = 0

while (Contador < 3):
    while (True):
        Numerito6 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito7 = float(Numerito6)
            if (Numerito7.is_integer()):
                print (f'La nota {Contador + 1} es un numero entero')
                Lista_Promedios.append(Numerito7)
                break
            else:
                print (f'La nota {Contador + 1} es un numero decimal')
                Lista_Promedios.extend([Numerito7])
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador += 1
    
Promedio3 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas ingresadas es {round(Promedio3, 2)}')'''

'''Esto es un docstring
La idea de esto es tener una cadena de texto
dividida en varias lineas'''

'''
\D todo menos numeros
\d solo numeros
\W solo simbolos especiales
\w todo menos simbolos especiales
\s solo espacios
\S todo menos espacios
+ uno o mas
? cero o uno
* cero o mas
{4} especificamente 4
{1-4} entre uno y 4
{3,} tres o mas
^ Comienza con 
[^0-9] todo menos numeros
$ termina con 
h.la puede ser hola, hela, hila, el punto es un comodin
'''

import re

Texto5 = 'Esto es un texto 12 cualquiera hola 123 ! de prueba#, necesitamos saber si el texto 569 que se ingresa -sirve hula para trabajar 9000 con expresiones hela regulares @ o no'

Buscar4 = re.search('saber', Texto5)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\d+', Texto5)

print (f'{Buscar5}')

Texto6 = 'Hola Mundo'

Buscar6 = bool(re.fullmatch(r'H.la Mundo', Texto6))

if (Buscar6 == True):
    print (f'El texto es exacto')
else:
    print (f'Error, el texto no es igual')
    
Buscar7 = re.search(r'^Esto', Texto5)

print (f'{Buscar7}')

Buscar8 = re.search(r'o$', Texto5)

print (f'{Buscar8}')

Buscar9 = re.findall(r'\d{3}\s{1}\W{1}', Texto5)

print (f'{Buscar9}')

Buscar10 = re.findall(r'[ab]{2,4}', Texto5)

print (f'{Buscar10}')

Buscar11 = re.findall(r'\d{2,4}|h.la', Texto5)

print (f'{Buscar11}')

print (f'-' * 20)

import re

Texto6 = 'ericksuper80@hotmail.com'

Pattern9 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Buscar12 = bool(re.fullmatch(Pattern9, Texto6))

if (Buscar12 == True):
    print (f'El correo electronico tiene el formato correcto')
else:
    print (f'Error, el correo electronico es invalido')
    
print (f'-' * 20)

Texto7 = '33'

Pattern10 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar13 = bool(re.match(Pattern10, Texto7))

if (Buscar13 == True):
    print (f'El numero esta entre 00 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

Texto8 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern11 = r'\d{1,2}\/[0-9]{2,}\/\d{4}'

Replace11 = 'XX/XX/XXXX'

Buscar14 = re.sub(Pattern11, Replace11, Texto8)

print (f'{Buscar14}')

Pattern12 = r'\+\d*\-[0-9]{1,3}\-\d{1,}\-[0-9]{4}'

Replace12 = 'PH0N3_NVMB3R'

Buscar15 = re.sub(Pattern12, Replace12, Buscar14)

print (f'{Buscar15}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv2 = 'C:\\Repo\\Store.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

Fecha2 = '2026-04-01'

try:
    Fech2 = datetime.strptime(Fecha2, '%Y-%m-%d').date()
    Fech2_Formateada = pd.to_datetime(Fech2)
    Cargar_Csv2['date'] = pd.to_datetime(Cargar_Csv2['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato incorrecto')
    exit()
    
Cargar_Csv2['TOTALITO'] = Cargar_Csv2['quantity'] * Cargar_Csv2['price']
    
Encontrado2 = Cargar_Csv2[Cargar_Csv2['date'].dt.date == Fech2_Formateada.date()]

if (Encontrado2.empty):
    print (f'No encontramos ventas en esta fecha')
else:
    print (f'Genial! encontramos ventas')
    
    Grupo3 = Encontrado2.groupby('product')['quantity'].sum()
    Grupo3_Min = Grupo3.idxmin()
    Grupo3_Max = Grupo3.idxmax()
    Grupo3_Min_Cant = Grupo3.min()
    Grupo3_Max_Cant = Grupo3.max()
    
    print (f'El que vendio menos fue {Grupo3_Min} con un total de {Grupo3_Min_Cant} unidades')
    print (f'El que vendio mas fue {Grupo3_Max} con un total de {Grupo3_Max_Cant} unidades')
    
    print (f'La cantidad de productos vendidos en esta fecha fue de {Grupo3.sum()}')
    
    print (f'La cantidad de clientes que compraron en esta fecha fue {Grupo3.count()}')
    
    print (f'El promedio de productos vendidos fue {round(Grupo3.mean(), 2)}')
    
    Grupo4 = Encontrado2.groupby('product')['TOTALITO'].sum()
    
    Promedio3 = Grupo4.sum() / Grupo3.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Promedio3, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Grupo4.mean(), 2)}')
    
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

Buscar16 = re.findall(Pattern13, Texto9)

for indice, elemento in enumerate(Buscar16, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

import re

# METODO NUMERO 1

Texto10 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern14 = r'\!|\?|\.{2,}|\d{2,4}\-[0-9]{4,}'

Buscar17 = re.sub(Pattern14, '', Texto10)

print (f'{Buscar17}')

print (f'-' * 20)

# METODO NUMERO 2

Pattern15 = r'[^a-zA-Z0-9\s]+|\d{5,8}'

Buscar18 = re.sub(Pattern15, '', Texto10)

print (f'{Buscar18}')

print (f'-' * 20)

# METODO NUMERO 3

Texto10_temp1 = Texto10

Pattern16 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos4 = re.findall(Pattern16, Texto10)

print (f'{Correos4}')

for i, email in enumerate(Correos4, start=1):
    Texto10_temp1 = Texto10_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto10_temp1}')

Pattern17 = r'\!|\?|\.{2,}|\d{2,4}\-[0-9]{4,}'

Texto10_temp2 = re.sub(Pattern17, '', Texto10_temp1)

print (f'{Texto10_temp2}')

for i, email in enumerate(Correos4, start=1):
    Texto10_temp2 = Texto10_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto10_temp2}')

print (f'-' * 20)

var9 = 3.5

if (isinstance(var9, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, lo que ingresaste no es un numero decimal')
    
try:
    Numerito6 = float(var9)
    if (Numerito6.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except (ValueError, KeyError):
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var10 = '5'

if (isinstance(var10, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var10.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var10.isdecimal()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
try:
    Numerito7 = float(var10)
    if (Numerito7.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError as Errore1:
    print (f'Error, lo que ingresaste no es un numero -> {str(Errore1)}')
    
print (f'-' * 20)

import re

Texto11 = "   Hola!!!   mundo@@   123   "

print (f'{Texto11}')

Texto11_version1 = Texto11.strip()

print (f'{Texto11_version1}')

Texto11_version2 = ' '.join(Texto11_version1.split())

print (f'{Texto11_version2}')

Texto11_version3 = Texto11_version2.lower()

print (f'{Texto11_version3}')

Texto11_version4 = re.sub(r'\!|\@|\d+', '', Texto11_version3)

print (f'{Texto11_version4}')

Texto11_version5 = Texto11_version4.title()

print (f'{Texto11_version5}')

print (f'-' * 20)

try:
    Resultado5 = 'hola' * '3' #type: ignore
    print (f'El resultado de la operacion es {Resultado5}')
except TypeError:
    print (f'Error, estas variables no pueden operarse')
    
print (f'-' * 20)

var11 = ['Erick', 'Josue']

try:
    var11.remove('Karlita')
    print (f'{var11}')
except ValueError:
    print (f'Error, este elemento no puede borrarse de la lista')
    
print (f'-' * 20)

try:
    snake_case1, snake_case2, snake_case3 = var11
except Exception:
    print (f'Error, el desempaquetado es incorrecto')
    
print (f'-' * 20)

Fecha3 = 'hola-04-01'

try:
    Fech3 = datetime.strptime(Fecha3, '%Y-%m-%d').date()
    Fech3_Formateada = pd.to_datetime(Fech3)
    Cargar_Csv2['date'] = pd.to_datetime(Cargar_Csv2['date'])
except ValueError as Errore2:
    print (f'Error, la fecha es invalida -> {str(Errore2)}')
    
print (f'-' * 20)

try:
    Resultado6 = 5 + '9' #type: ignore
    print (f'{Resultado6}')
except (TypeError, Exception):
    print (f'Error, la operacion no puede realizarse')
    
print (f'-' * 20)

try:
    print (f'{int("Hola")}')
except ValueError:
    print (f'Error, esto no esta bien')
    
print (f'-' * 20)

var12 = [1, 2, 3]

try:
    print (f'{var12[3]}')
except IndexError:
    print (f'Error, este indice esta fuera de rango')
    
try:
    print (f'{var12.index(4)}')
except ValueError:
    print (f'Error, este indice esta fuera de rango')
    
print (f'-' * 20)

var13 = list(['Erick', 'Josue', 'Karlita'])
var14 = dict({
    'Nombre' : "Erick",
    'Edad' : 37
})

try:
    # print (f'El elemento {int(var13[0])}')
    # print (f'El resultado de la operacion es {4 + "5"}') #type: ignore
    # print (f'El resultado de la operacion es {15 / 0}')
    # print (f'El elemento es {var13[3]}')
    # print (f'El elemento es {var14["Votante"]}')
    '''with open ('C:\\Repo\\HolaMuno.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Linea = Docu.readline()
        print (f'{Documento_Linea}')
        Docu.close()'''
    # import Modle_Own as PEPE2
    # import Module_wn as PEPE3
except ValueError:
    print (f'Error, esto es un ValueError')
except TypeError:
    print (f'Error, esto es un TypeError') 
except ZeroDivisionError:
    print (f'Error, esto es un ZeroDivisionError') 
except IndexError:
    print (f'Error, esto es un IndexError') 
except KeyError:
    print (f'Error, esto es un KeyError') 
except FileNotFoundError:
    print (f'Error, esto es un FileNotFoundError') 
except ImportError:
    print (f'Error, esto es un ImportError') 
except Exception:
    print (f'Error, esto es un Exception') 

print (f'-' * 20)

var15 = 13

try:
    print (f'El numero es {var15 * "3"}')
except TypeError:
    print (f'Lo que ingresaste es un texto')
    
print (f'-' * 20)

def Ejercicio59(Numero):
    try:
        Numerito8 = float(Numero)
        if (Numerito8.is_integer()):
            print (f'Lo que ingresaste es un numero entero')
        else:
            print (f'Lo que ingresaste es un numero decimal')
    except ValueError:
        print (f'Error, lo que ingresaste no es un numero')

Sample59 = Ejercicio59('hola')

print (f'-' * 20)

def Ejercicio60(Num1, Num2 = 'hola'):
    try:
        print (f'El resultado de la operacion es {Num1 + Num2}')
    except (ValueError, TypeError):
        print (f'Error, ambos elementos deben ser numeros')

Sample60 = Ejercicio60(5)

print (f'-' * 20)

def Ejercicio61(Num1=12, Num2=0):
    try:
        print (f'El resultado de la operacion es {Num1 / Num2}')
    except ZeroDivisionError as Errore3:
        print (f'Error, el divisor no puede ser cero -> {str(Errore3)}')

Sample61 = Ejercicio61()

print (f'-' * 20)

def Ejercicio62(*args):
    try:
        print (f'El elemento es {args[3]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Sample62 = Ejercicio62('Erick', 'Josue', 'Karlita')

print (f'-' * 20)

Diccionario_Excepcion = {
    'Nombre' : "Erick",
    'Edad' : 37
}

def Ejercicio63(Diccionario, Clave):
    try:
        print (f'El elemento con la clave {Clave} es {Diccionario[Clave]}')
    except KeyError:
        print (f'Error, la clave esta fuera de rango')

Sample63 = Ejercicio63(Diccionario_Excepcion, 'Nombre')

print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMudo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        print (f'{Documento_Lineas}')
        Docu.close()
except FileNotFoundError as Errore3:
    print (f'Error, el documento es incorrecto -> {str(Errore3)}')
    
print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
    Documento_SobreEscribir = Docu.write(f'Calabaza')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Linea = Docu.readline()
        print (f'{Documento_Linea}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
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
    Documento_Agregar = Docu.write(f'\nUvas')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Leer = Docu.read()
        print (f'{Documento_Leer}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nFresa Pequeña', f'\nFresa Mediana', f'\nFresa Grande'])
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Linea = Docu.readline()
        print (f'{Documento_Linea}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding = 'UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke1"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke2"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke3"]}')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        print (f'{Documento_Lineas}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')
    
with open('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    # Documento_Agregar = Docu.write(f'\n')
    for _, elemento in PEPE.Diccionario_Poke.items():
        Documento_Agregar = Docu.write(f'\n{elemento}')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Leer = Docu.read()
        print (f'{Documento_Leer}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no existe')\
        
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\n')
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Set_Conjunto_Poke1)])
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        print (f'{Documento_Lineas}')
        Docu.close()
except ValueError:
    print (f'Error, el archivo no existe')
    
print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        # print (f'{Documento_Lineas}')
        for indice, elemento in enumerate(Documento_Lineas, start=1):
            if (elemento.strip() == 'Uvas'):
                print (f'The name of this fruit is grape in english')
                break
            else:
                continue
        Docu.close()
except ValueError:
    print (f'Error, el archivo no existe')
    
print (f'-' * 20)

import pandas as pd

DataFrame1 = pd.DataFrame({
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
})

DataFrame2 = pd.DataFrame({
    'Nombre' : ["Carmelo", "Susanita", "Roxana"],
    'Edad' : [55, 14, 26],
    'Votante' : [True, False, not False]
})

Data_Frame_Concatenado = pd.concat([DataFrame1, DataFrame2])

Data_Frame_Concatenado_Edad = Data_Frame_Concatenado['Edad']

print (f'{Data_Frame_Concatenado_Edad}')

print (f'{Data_Frame_Concatenado_Edad.sum()}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenado}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenado.shape}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenado.info()}')

Columnas1, Filas1 = Data_Frame_Concatenado.shape

print (f'La cantidad de Columnas1 es {Columnas1}')
print (f'La cantidad de Filas1 es {Filas1}')

print (f'-' * 20)

Grupo5 = Data_Frame_Concatenado.groupby('Nombre')['Edad'].sum()

print (f'{Grupo5}')

Grupo5_Min = Grupo5.idxmin()
Grupo5_Max = Grupo5.idxmax()
Grupo5_Min_Cant = Grupo5.min()
Grupo5_Max_Cant = Grupo5.max()

print (f'{Grupo5}')

print (f'El menor de las personas es {Grupo5_Min} y su edad es {Grupo5_Min_Cant} años')
print (f'El mayor de las personas es {Grupo5_Max} y su edad es {Grupo5_Max_Cant} años')

print (f'La cantidad de personas en el dataframe es {Grupo5.count()}')

print (f'La suma de todas las edades es {Grupo5.sum()}')

print (f'La media o promedio de la suma de las edades es {round(Grupo5.mean(), 2)}')

print (f'La menor de las edades es {Data_Frame_Concatenado_Edad.min()}')
print (f'La mayor de las edades es {Data_Frame_Concatenado_Edad.max()}')

for indice, elemento in Data_Frame_Concatenado.iterrows():
    Unidad1 = elemento['Nombre']
    Unidad2 = elemento['Edad']
    
    print (f'Mi nombre es {Unidad1} y mi edad es {Unidad2} años')
    
print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3}')

print (f'-' * 20)

Fecha4 = '2026-04-01'

try:
    Fech4 = datetime.strptime(Fecha4, '%Y-%m-%d').date()
    Fech4_Formateada = pd.to_datetime(Fech4)
    Cargar_Csv3['date'] = pd.to_datetime(Cargar_Csv3['date'])
except ValueError:
    print (f'Error, la fecha es invalida')
    exit()
    
Cargar_Csv3['TOTALITO'] = Cargar_Csv3['quantity'] * Cargar_Csv3['price']
    
Encontrado3 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech4_Formateada.date()]

if (Encontrado3.empty):
    print (f'No se encontraron ventas en esta fecha')
else:
    print (f'GENIAL! Encontramos ventas')
    
    Grupo6 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo6_Min = Grupo6.idxmin()
    Grupo6_Max = Grupo6.idxmax()
    Grupo6_Min_Cant = Grupo6.min()
    Grupo6_Max_Cant = Grupo6.max()
    
    print (f'El producto que menos vendio fue {Grupo6_Min} con un total de unidades {Grupo6_Min_Cant}')
    print (f'El producto que mas vendio fue {Grupo6_Max} con un total de unidades {Grupo6_Max_Cant}')
    
    print (f'La cantidad de clientes que compraron hoy fue {Grupo6.count()}')
    
    print (f'La suma de todos los productos vendidos fue {Grupo6.sum()}')
    
    Grupo7 = Encontrado3.groupby('product')['TOTALITO'].sum()
    
    Promedio4 = Grupo7.sum() / Grupo6.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio4, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Grupo7.mean(), 2)}')
    
print (f'-' * 20)

'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenado)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenado)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=Data_Frame_Concatenado)

plt.show()'''

print (f'-' * 20)

print (f'{Data_Frame_Concatenado.head(1)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenado.head(3)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenado.tail(1)}')

print (f'-' * 20)

Filas2, Columnas2 = Data_Frame_Concatenado.shape

print (f'La cantidad de Filas2 es {Filas2}')
print (f'La cantidad de Columnas2 es {Columnas2}')

print (f'-' * 20)

Elemento1 = DataFrame1.loc[0, 'Nombre']
Elemento2 = DataFrame1.loc[1, 'Edad']
Elemento3 = DataFrame1.loc[2, 'Votante']
Elemento4 = DataFrame1.loc[:, 'Nombre']
Elemento5 = DataFrame1.loc[2, :]

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')
print (f'{Elemento4}')
print (f'{Elemento5}')

print (f'-' * 20)

Elemento6 = DataFrame2.iloc[0, 0]
Elemento7 = DataFrame2.iloc[1, 1]
Elemento8 = DataFrame2.iloc[2, 2]
Elemento9 = DataFrame2.iloc[1, :]
Elemento10 = DataFrame2.iloc[:, 2]

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
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tarifa', usecols='E:K')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tarifa', usecols='E:K', nrows=1)

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

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'-' * 20)

print (f'{Cargar_Txt.head()}')

print (f'-' * 20)

Grupo8 = Cargar_Excel3.groupby('tres')['cinco'].sum()
Grupo8_Min = Grupo8.idxmin()
Grupo8_Max = Grupo8.idxmax()
Grupo8_Min_Cant = Grupo8.min()
Grupo8_Max_Cant = Grupo8.max()

print (f'Del excel la menor de las personas es {Grupo8_Min} y su edad es {Grupo8_Min_Cant} años')
print (f'Del excel la mayor de las personas es {Grupo8_Max} y su edad es {Grupo8_Max_Cant} años')

print (f'La cantidad de personas en el excel es {Grupo8.count()}')

print (f'La suma de las edades es {Grupo8.sum()}')

Promedio5 = Grupo8.sum() / Grupo8.count()

print (f'El promedio de la suma de las edades es {round(Promedio5, 2)}')
print (f'El promedio de la suma de las edades es {round(Grupo8.mean(), 2)}')

print (f'-' * 20)

import pandas as pd

Ruta_Csv4 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv4 = pd.read_csv(Ruta_Csv4)

print (f'{Cargar_Csv4}')

print (f'-' * 20)

Cargar_Csv4_Edad = Cargar_Csv4['Edad']

print (f'{Cargar_Csv4_Edad}')

print (f'{Cargar_Csv4_Edad.sum()}')

print (f'La menor de las edades es {Cargar_Csv4_Edad.min()}')
print (f'La mayor de las edades es {Cargar_Csv4_Edad.max()}')

print (f'-' * 20)

import pandas as pd
import requests
import io

Ruta_Html = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozila/5.0'}

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
print (f'{Array0[0][2]}')
print (f'{Array0[1][0:None]}')
print (f'{Array0[1][:]}')
print (f'{Array0[2][2:3]}')
print (f'{Array0[0][:2]}')
print (f'{Array0[0][2:]}')
print (f'{Array0[1][::2]}')
print (f'{Array0[2][::3]}')

print (f'-' * 20)

for i in range(len(Array0)):
    for j in range(i, len(Array0)):
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
print (f'{Array1[2:3]}')
print (f'{Array1[0:None]}')
print (f'{Array1[:]}')
print (f'{Array1[Array1 > 2]}')

print (f'-' * 20)

Array2 = np.array([[1, 2, 3],    [4, 5, 6]])

print (f'{Array2}')
print (f'{Array2.ndim}') # 2
print (f'{Array2.shape}') # 2x3
print (f'{Array2.size}') # 6
print (f'{Array2.dtype}') # int64
print (f'{Array2[1, 1]}')

print (f'{Array2[1, ::2]}')
print (f'{Array2[0, ::3]}')
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

Array3 = np.array([[['a', 'b', 'c'], ['d', 'e', 'f']],       [['g', 'h', 'i'], ['j', 'k', 'l']]])

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
print (f'{Array3[1, :, 0]}')
print (f'{Array3[0, 0, 2:3]}')
print (f'{Array3[1, 0, 0:None]}')
print (f'{Array3[1, 0, :]}')
print (f'{Array3[Array3 == "b"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],        [[[6, 5, 4], [9, 8, 7]], [[0, 4, 6], [2, 9, 7]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 0, 2]}')

print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[0, 1, 1, ::3]}')
print (f'{Array4[1, 0, 1, :2]}')
print (f'{Array4[1, 0, 1, 2:]}')
print (f'{Array4[1, 0, :, 1]}')
print (f'{Array4[1, 0, 0, 2:3]}')
print (f'{Array4[0, 0, 0, 0:None]}')
print (f'{Array4[0, 0, 0, :]}')
print (f'{Array4[Array4 >= 7]}')

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

Array_Num1 = np.arange(start=1, stop=11, step=1) #type: ignore

print (f'{Array_Num1}')

Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El numero menor de la lista es {Array_Num1_Min}')
print (f'El numero mayor de la lista es {Array_Num1_Max}')

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
print (f'Los mayor de las columnas son {Array_Num2_Reshape_Column_Max}')
print (f'Los menores de las columnas son {Array_Num2_Reshape_Row_Min}')
print (f'Los mayor de las columnas son {Array_Num2_Reshape_Row_Max}')

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
print (f'{Array_Zeros[1, :2]}')
print (f'{Array_Zeros[1, 2:]}')
print (f'{Array_Zeros[:, 2]}')
print (f'{Array_Zeros[0, 2:3]}')
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
print (f'{Array_Ones[1, 1]}')

print (f'{Array_Ones[0, ::2]}')
print (f'{Array_Ones[1, ::3]}')
print (f'{Array_Ones[1, :2]}')
print (f'{Array_Ones[1, 2:]}')
print (f'{Array_Ones[:, 1]}')
print (f'{Array_Ones[1, 2:3]}')
print (f'{Array_Ones[0, 0:None]}')
print (f'{Array_Ones[0, :]}')
print (f'{Array_Ones[Array_Ones == 1]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value=f'Fuecoco')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 2]}')

print (f'{Array_Gen1[1, :2]}')
print (f'{Array_Gen1[1, 2:]}')
print (f'{Array_Gen1[0, ::2]}')
print (f'{Array_Gen1[1, ::3]}')
print (f'{Array_Gen1[:, 2]}')
print (f'{Array_Gen1[1, 2:3]}')
print (f'{Array_Gen1[0, 0:None]}')
print (f'{Array_Gen1[0, :]}')
print (f'{Array_Gen1[Array_Gen1 == "Fuecoco"]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value=Array4[0, 1, 1, 1])

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[4]}')

Lista_Array1 = list([])

for elemento in Array_Gen2[0:None]:
    Lista_Array1.append(str(elemento))
    
print (f'{Array_Gen2}')
print (f'{type(Array_Gen2)}')
print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value=f'{Array1[2]}')

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 0]}')

print (f'-' * 20)

Tupla_Array = tuple(('Uno', 'Dos', 'Tres'))
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({
    'Nombre' : ["Erick", "Josue", "Karlita"]
})

Array_Gen4 = np.full(shape=(2, 3), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array['Nombre'][2])

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

print (f'-' * 20)

print (f'{Array_Gen6}')
print (f'{Array_Gen6.ndim}')
print (f'{Array_Gen6.shape}')
print (f'{Array_Gen6.size}')
print (f'{Array_Gen6.dtype}')

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
print (f'{Array_Random1.ndim}')
print (f'{Array_Random1.shape}')
print (f'{Array_Random1.size}')
print (f'{Array_Random1.dtype}')
print (f'{Array_Random1[8]}')

print (f'-' * 20)

Array_Random2 = np.random.randint(low=1, high=10, size=(2, 3))

print (f'{Array_Random2}')
print (f'{Array_Random2.ndim}')
print (f'{Array_Random2.shape}')
print (f'{Array_Random2.size}')
print (f'{Array_Random2.dtype}')
print (f'{Array_Random2[0, 2]}')

Array_Random2_Sorted = np.sort(Array_Random2)
Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)
Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'Acomodado: {Array_Random2_Sorted}')
print (f'Media: {round(Array_Random2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random2_Sorted_Sum}')

Sumita9 = np.sum(Array_Random2_Sorted, axis=0)
Sumita10 = np.sum(Array_Random2_Sorted, axis=1)
Sumita11 = np.sum(Array_Random2_Sorted[1, 0:None])
Sumita12 = np.sum(Array_Random2_Sorted[1, :])

print (f'El resultado de la sumita es {Sumita9}')
print (f'El resultado de la sumita es {Sumita10}')
print (f'El resultado de la sumita es {Sumita11}')
print (f'El resultado de la sumita es {Sumita12}')

print (f'-' * 20)

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Array_Sum = Arr1 + Arr2
Array_Rest = Arr1 - Arr2
Array_Mult = Arr1 * Arr2
Array_Div_Baja = Arr1 // Arr2
Array_Div_Flotante = Arr1 / Arr2
Array_Exp = Arr1 ** Arr2
Array_Mod = Arr1 % Arr2

Array_Random1_Cien = Array_Random1 + 100

print (f'Resultado: {Array_Sum}')
print (f'Resultado: {Array_Rest}')
print (f'Resultado: {Array_Mult}')
print (f'Resultado: {Array_Div_Baja}')
print (f'Resultado: {Array_Div_Flotante}')
print (f'Resultado: {Array_Exp}')
print (f'Resultado: {Array_Mod}')
print (f'Resultado: {Array_Random1_Cien}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(20))

print (f'{Array_Random3}')

Array_Random3_Reshape = np.reshape(Array_Random3, shape=(4, 5))

print (f'{Array_Random3_Reshape}')

Array_Random3_Reshape_Column_Min = np.min(Array_Random3_Reshape, axis=0)
Array_Random3_Reshape_Column_Max = np.max(Array_Random3_Reshape, axis=0)
Array_Random3_Reshape_Row_Min = np.min(Array_Random3_Reshape, axis=1)
Array_Random3_Reshape_Row_Max = np.max(Array_Random3_Reshape, axis=1)

print (f'Los menores de las columnas son {Array_Random3_Reshape_Column_Min}')
print (f'Los mayores de las columnas son {Array_Random3_Reshape_Column_Max}')
print (f'Los menores de las filas son {Array_Random3_Reshape_Row_Min}')
print (f'Los mayores de las filas son {Array_Random3_Reshape_Row_Max}')

print (f'-' * 20)

Lista_Array2 = ['Erick', 'Josue', 'Karlita']

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
Array7 = np.array([4, 5, 6])

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

for Matriz2 in Array4:
    for Matriz1 in Matriz2:
        for Fila in Matriz1:
            print (f'{Fila}')

print (f'-' * 20)

for Matriz1 in Array3:
    for Fila in Matriz1:
        for Elemento in Fila:
            print (f'{Elemento}')

print (f'-' * 20)

Array_Random4 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random4}')
print (f'{Array_Random4.ndim}')
print (f'{Array_Random4.shape}')
print (f'{Array_Random4.size}')
print (f'{Array_Random4.dtype}')
print (f'{Array_Random4[1, 0, 2]}')

Array_Random4_Column_Min = np.min(Array_Random4, axis=0)
Array_Random4_Column_Max = np.max(Array_Random4, axis=0)
Array_Random4_Row_Min = np.min(Array_Random4, axis=1)
Array_Random4_Row_Max = np.max(Array_Random4, axis=1)

print (f'Los menores de las columnas son {Array_Random4_Column_Min}')
print (f'Los mayores de las columnas son {Array_Random4_Column_Max}')
print (f'Los menores de las filas son {Array_Random4_Row_Min}')
print (f'Los mayores de las filas son {Array_Random4_Row_Max}')

print (f'-' * 20)

Participantes_Sorteo1 = set({'Erick'})
Participantes_Sorteo1.add('Josue')
Participantes_Sorteo1.add('Karlita')
Participantes_Sorteo2 = {'Carmelo', 'Susanita'}
Participantes_Sorteo2.add('Roxana')

Participantes_Sorteo1.update(Participantes_Sorteo2)

Lista_Participantes = list(Participantes_Sorteo1)

Ganador1 = np.random.choice(Lista_Participantes, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Participantes, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Participantes, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-' * 20)

Array_Linspace = np.linspace(start=0, stop=10, num=3)

print (f'{Array_Linspace}')

print (f'-' * 20)

def Generadora1():
    for elemento in range(5):
        yield f'El numero es {elemento}'

Gen1 = Generadora1()

try:
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
    print (f'{next(Gen1)}')
except StopIteration:
    print (f'Aqui termina el experimento')

print (f'-' * 20)

def Generadora2():
    for elemento in range(0 + 1, 5):
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
    print (f'Aqui termina el experimento')

print (f'-' * 20)

def Generadora3():
    for elemento in range(0, 5):
        if (elemento == 0):
            yield f'The number zero'
        elif (elemento == 1):
            yield f'The number one'
        elif (elemento == 2):
            yield f'The number two'
        elif (elemento == 3):
            yield f'The number three'
        elif (elemento == 4):
            yield f'The number four'
        else:
            yield f'Error Generadora'

Gen3 = Generadora3()

try:
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
except StopIteration:
    print (f'Aqui termina el experimento')

print (f'-' * 20)

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la operacion es {PEPE.Sumatoria1(12, 7)}')

def Suma_Externa(Num1):
    def Suma_Interna(Num2:int) -> int:
        return Num1 + Num2
    
    return Suma_Interna(4)

Variable_Sumatoria = Suma_Externa(3)

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
    
print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(45)}')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Leer = Docu.read()
        print (f'{Documento_Leer}')
        Docu.close()
except (Exception, FileNotFoundError):
    print (f'Error, el archivo seleccionado no existe')
    
print (f'-' * 20)
    
def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla(
    3.5,
    'Koala',
    200,
    not False
)

print (f'{Funcion_Tupla(
    3.5,
    'Koala',
    200,
    not False
)}')
print (f'{Funcion_Tupla(
    3.5,
    'Koala',
    200,
    not False
)[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla(
    3.5,
    'Koala',
    200,
    not False
))}')

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

def Sumatoria_Dos(Num1, Num2, *numeros, **dict_num):
    Acumulado = 0
    for elemento in dict_num.values():
        Acumulado += elemento
        
    return Num1 + Num2 + sum(numeros) + Acumulado

print (f'El resultado de la segunda sumatoria es {Sumatoria_Dos(2, 3, 1, 2, 3, 4, 5, 6, num1=50, num2=100)}')

print (f'-' * 20)

def Sumatoria_Tres(Nombre:str, *args):
    return f'Hola, mi nombre es {Nombre} y mi numero favorito es {sum(args)}'

print (f'{Sumatoria_Tres(Saludar_Dos(), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

print (f'Los numeros pares de la lista son {list(Anonima3)}')

print (f'{PEPE.Par}')

print (f'Los numeros pares de la lista son {PEPE.Lista_Par}')

Diccionario_Numeral2 = {
    'Num1' : 7,
    'Num2' : 2,
    'Num3' : 8,
    'Num4' : 0,
    'Num5' : 1
}

Diccionario_Numeral2_Sorted = dict(sorted(Diccionario_Numeral2.items(), key=lambda item : item[1]))
Diccionario_Numeral2_Sorted_Min = min(Diccionario_Numeral2.items(), key=lambda item : item[1])
Diccionario_Numeral2_Sorted_Max = max(Diccionario_Numeral2.items(), key=lambda item : item[1])

print (f'{Diccionario_Numeral2}')
print (f'{Diccionario_Numeral2_Sorted}')
print (f'{Diccionario_Numeral2_Sorted_Min}')
print (f'{Diccionario_Numeral2_Sorted_Max}')

print (f'-' * 20)

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(0, Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda item : item[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes de la lista es {Menore} y su edad es {Lista[0][1]} años')
    print (f'El mayor de los estudiantes de la lista es {Mayore} y su edad es {Lista[-1][1]} años')

Sample58 = Colegio(Lista_Alumnos)'''

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

print (f'-' * 20)

def Closure_Externo():
    Lista_Closure = []
    def Closure_Interno(x):
        Lista_Closure.append(x)
        return Lista_Closure
        
    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(30)}')
print (f'{Variable_Closure(78)}')

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
        Lista_Impares = [num for num in Lista if num % 2 != 0]
        Anonima = filter(lambda Num : Num % 2 != 0, Lista)
        
        print (f'Los numeros impares de la lista son {Lista_Impares}')
        print (f'Los numeros impares de la lista son {list(Anonima)}')
    else:
        print (f'Error, no hay elementos impares en la lista')

Sample64 = Filtrador(PEPE.Lista_Numeros1)

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'>>>>>')
        Segunda()
        print (f'>>>>>')
        
    return Tercera

@Primera
def Saludar4():
    print (f'Hola Mundo')

Saludar4()

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 7
        
    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria3(4, 3)}')

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Robert'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)
        
    return Tercera

@Primera
def El_Usuario(Nombre, Apellido):
    return f'Mi nombre es {Nombre} {Apellido}'

print (f'{El_Usuario("Erick", "Perez")}')

print (f'-' * 20)

var16 = 1

var16 += 2

print (f'El resultado de la operacion es {var16}')

var16 -= 2

print (f'El resultado de la operacion es {var16}')

var16 *= 2

print (f'El resultado de la operacion es {var16}')

var16 //= 2

print (f'El resultado de la operacion es {var16}')

var16 /= 2

print (f'El resultado de la operacion es {var16}')

var16 **= 6

print (f'El resultado de la operacion es {var16}')

var16 %= 3

print (f'El resultado de la operacion es {var16}')

print (f'-' * 20)

print (f'Mi nombre es {(var17 := "Erick Josue Perez Gutierrez")}')

for elemento in (Lista_Walrus := [1, 2, 3, 4, 5]):
    print (f'{elemento}')
    
for indice, elemento in (Diccionario_Walrus := dict({'Nombre' : "Erick", 'Edad' : 37, 'Votante' : True}).items()):
    print (f'{indice} : {elemento}')
    
print (f'La tupla es {(Tupla_Walrus := ('Uno', 'Dos', 'Tres',))}')

print (f'El set o conjunto es {(Set_Conjunto_Walrush := {1, 2, 3})}')

for elemento in range(Lista_Walrus2 := 10):
    print (f'{elemento}')
    
Contador = 0

while (Contador < len(Lista_Walrus3 := ['Erick', 'Josue', 'Karlita'])):
    print (f'El elemento {Contador + 1} es {Lista_Walrus3[Contador]}')
    Contador += 1
    
from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

Variable1 = Lista_Uno[0]
Variable2 = 'Perez'
Variable3 = '''Esto
Es
Un
Long
String'''

Variable4 = Objeto9.Cantidad
Variable5 = PEPE.Division_Flotante

try:
    Variable6, Variable7 = not False, Objeto10.Catched
except ValueError as Errore4:
    print (f'La declaracion snake case con desempaquetado de variables es incorrecta -> {str(Errore4)}')
    
# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke1"]}')

print (f'Mi nombre es {str(Lista_Uno[:-3])} {Variable2}')

print (f'Actualmente {PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Objeto11.Cantidad} pokemones')

del Variable5

print (f'MELO'.lower() in Saludar_Dos())
print (f'Long' not in Variable3)

print (f'{PEPE.Diccionario_Poke["Poke3"]}' in PEPE.Set_Conjunto_Poke1)
print (f'{Variable2}' in Lista_Uno)
print (f'Dragonite' not in PEPE.Set_Conjunto_Poke1)

print (f'-' * 20)

snake_case4, snake_case5, snake_case6 = PEPE.Tupla_Poke

print (f'Esto es una declaracion snake case y es desempaquetado de variables {snake_case5}')

print (f'La lista tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista tiene {len(Lista_Uno)} elementos')

try:
    Cociente, Residuo = divmod(Objeto9.Cantidad, Variable_Sumatoria)
    print (f'El Cociente de la operacion es {Cociente}')
    print (f'El Residuo de la operacion es {Residuo}')
except ValueError:
    print (f'Error, el desempaquetado es incorrecto')
    
print (f'{PEPE.Lista2}')
print (f'{PEPE.Lista2[:2]}')
print (f'{PEPE.Lista2[2:]}')
print (f'{PEPE.Lista2[::2]}')
print (f'{PEPE.Lista2[::3]}')
print (f'{PEPE.Lista2[2:3]}')
print (f'{PEPE.Lista2[0:None]}')
print (f'{PEPE.Lista2[:]}')
print (f'{PEPE.Lista2[:-1]}')
print (f'{PEPE.Lista2[:-2]}')
print (f'{PEPE.Lista2[:-3]}')
print (f'{PEPE.Lista2[:-4]}')

print (f'-' * 20)

print (f'{Lista_Uno[2:3]} eso que esta ahi es un {PEPE.Lista2[PEPE.Lista2.index("Koala")]}?')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, 200, 100)

print (f'{Lista_Cuatro}')

del Lista_Uno[1]
Lista_Uno.remove('Coco Rayado')
Lista_Uno.pop(-1)
Lista_Uno.pop(-1)
Lista_Uno.pop(-2)

print (f'{Lista_Uno}')
print (f'La lista tiene {len(Lista_Uno)} elementos')

print (f'-' * 20)

Lista_Uno_Copia = Lista_Uno.copy()

Lista_Uno.clear()

print (f'{Lista_Uno}')
print (f'La lista tiene {len(Lista_Uno)} elementos')

print (f'-' * 20)

print (f'{Lista_Uno_Copia}')
print (f'La lista tiene {len(Lista_Uno_Copia)} elementos')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'-' * 20)

print (f'{dir(PEPE)}')

Tupla1 = ('Uno', 'Dos', 'Dos', 'Dos', 'Dos', 'Tres',)

print (f'{Tupla1}')

# del Tupla1[0]

# Tupla1[1] = 'HOla'

Tupla1 = tuple(('One', 'Two', 'Three',))

print (f'{Tupla1}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Variable_Funcion_Tupla)}')

print (f'{Tupla1[::2]}')
print (f'{Tupla1[::3]}')
print (f'{Tupla1[:2]}')
print (f'{Tupla1[2:]}')
print (f'{Tupla1[2:3]}')
print (f'{Tupla1[0:None]}')
print (f'{Tupla1[:]}')
print (f'{Tupla1[:-1]}')
print (f'{Tupla1[:-2]}')
print (f'{Tupla1[:-3]}')

print (f'-' * 20)

Set_Conjunto1 = {'Red', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'}
Set_Conjunto2 = set({'Yellow'})

Set_Conjunto1.add('Green')

print (f'{Set_Conjunto1}')

Set_Conjunto1.update(Set_Conjunto2)

print (f'{Set_Conjunto1}')

print (f'El conjunto tiene {len(Set_Conjunto1)} elementos')

Set_Conjunto1 = set({'Rojo', 'Azul'})

print (f'{Set_Conjunto1}')

Set_Conjunto3 = {1, 2, 3, 4, 5}
Set_Conjunto4 = set({4, 5})
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

SetC = {1, 2, 3, 4, 5}
SetD = {4, 5}
SetE = set({8})

print (f'{SetC.issuperset(SetD)}')
print (f'{SetC >= SetD}')

print (f'-' * 20)

print (f'{SetD.issubset(SetC)}')
print (f'{SetD <= SetC}')

print (f'-' * 20)

print (f'{SetC.isdisjoint(SetE)}')

print (f'-' * 20)

# SetA.update(SetB)

# SetA.intersection_update(SetB)

# SetA.difference_update(SetB)

# SetB.difference_update(SetA)

SetA.symmetric_difference_update(SetB)

print (f'{SetA}')

print (f'-' * 20)

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

print (f'{Set_Conjunto_Menu1}')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})

Set_Conjunto_Menu3 = set({'Menta', Set_Conjunto_Menu2})

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

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1["Nombre"]}')
print (f'{Diccionario1.get("Edad")}')

for indice, elemento in Diccionario1.items():
    print (f'{indice} : {elemento}')
    
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

Diccionario2 = {
    'Nombre' : ['Erick', 'Josue', 'Karlita'],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
}

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2.values()}')
print (f'{Diccionario2.items()}')
print (f'{Diccionario2["Nombre"][1]}')
print (f'{Diccionario2.get("Edad")[2]}') #type: ignore

for indice, elemento in Diccionario2.items():
    for finale1, finale2 in enumerate(elemento[:], start=1):
        print (f'{finale1} : {finale2}')

Diccionario3 = dict({
    'Ingresos' : 501,
    'Gastos' : 199,
    'Vacio' : "q"
})

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3.values()}')
print (f'{Diccionario3.items()}')
print (f'{Diccionario3["Ingresos"]}')
print (f'{Diccionario3.get("Gastos")}')

Diccionario4 = {
    'Usuario1' : {
        'Nombre' : "Erick",
        'Edad' : 37,
        'Votante' : True
    },

    'Usuario2' : {
        'Nombre' : "Josue",
        'Edad' : 20,
        'Votante' : not False
    }
}

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Usuario1"]}')
print (f'{Diccionario4["Usuario1"]["Nombre"]}')

print (f'-' * 20)

for nivel1_indice, nivel1_elemento in Diccionario4.items():
    for nivel2_indice, nivel2_elemento in nivel1_elemento.items():
        print (f'{nivel2_indice} : {nivel2_elemento}')
        
print (f'-' * 20)

Diccionario1["Nombre"] = Saludar_Dos()

print (f'{Diccionario1}')

Diccionario1_Copia = Diccionario1.copy()

del Diccionario1["Nombre"]
Diccionario1.pop("Edad")

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')
print (f'{Diccionario1_Copia}')

Diccionario1 = dict({1 : "Karlita", 2 : 6, 3 : False})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario1.get(1)} no puede votar ya que solamente tiene {Diccionario2["Edad"][2]} añitos')

print (f'Mi nombre completo es {Lista_Uno_Copia[0]} {Diccionario4["Usuario2"]["Nombre"]} {Variable2}')

Diccionario_Vacio1 = dict.fromkeys('ABC', Saludar_Dos())
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])

Diccionario_Vacio2['Dos'] = PEPE.Diccionario_Poke["Poke2"]

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

Diccionario_Vacio3 = dict({})

Lista_Vacio3 = ['Aniz', 'Carambola', 'Coco', 'Aniz', 'Papaya', 'Coco', 'Aniz']

for elemento in Lista_Vacio3[0:None]:
    if (elemento not in Diccionario_Vacio3):
        Diccionario_Vacio3[elemento] = 0
        Diccionario_Vacio3[elemento] += 1
    else:
        Diccionario_Vacio3[elemento] += 1
        
print (f'{Diccionario_Vacio3}')
print (f'{Diccionario_Vacio3.keys()}')
print (f'{Diccionario_Vacio3.values()}')
print (f'{Diccionario_Vacio3.items()}')
print (f'{Diccionario_Vacio3["Papaya"]}')
print (f'{Diccionario_Vacio3.get("Aniz")}')

print (f'-' * 20)

Keys1 = [f'Key{i}' for i in range(len(Lista_Uno_Copia))]

Diccionario_Vacio4 = dict(zip(Keys1, Lista_Uno_Copia))

print (f'{Diccionario_Vacio4}')
print (f'{Diccionario_Vacio4.keys()}')
print (f'{Diccionario_Vacio4.values()}')
print (f'{Diccionario_Vacio4.items()}')
print (f'{Diccionario_Vacio4["Key0"]}')
print (f'{Diccionario_Vacio4.get("Key2")}')

print (f'-' * 20)

Diccionario_Vacio5 = dict.fromkeys(["Uno", "Dos", "Tres", "Cuatro"])

Contador = 0

while (Contador < len(Lista_Uno_Copia)):
    for elemento in Diccionario_Vacio5.keys():
        if (elemento == 'Uno'):
            Diccionario_Vacio5[elemento] = Lista_Uno_Copia[Contador]
            continue
        elif (elemento == 'Dos'):
            Diccionario_Vacio5[elemento] = Lista_Uno_Copia[Contador]
            continue
        elif (elemento == 'Tres'):
            Diccionario_Vacio5[elemento] = Lista_Uno_Copia[Contador]
            continue
        else:
            Diccionario_Vacio5[elemento] = Lista_Uno_Copia[Contador]
            continue
    Contador += 1
    
print (f'{Diccionario_Vacio5}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv5 = 'C:\\Repo\\Store.csv'

Cargar_Csv5 = pd.read_csv(Ruta_Csv5)

print (f'{Cargar_Csv5}')

Lista_Csv5 = list(Cargar_Csv5["product"])

print (f'{Lista_Csv5}')

Keys2 = [f'Key{i}' for i in range(len(Lista_Csv5))]

Diccionario_Vacio6 = dict(zip(Keys2, Lista_Csv5))

print (f'{Diccionario_Vacio6}')
print (f'{Diccionario_Vacio6.keys()}')
print (f'{Diccionario_Vacio6.values()}')
print (f'{Diccionario_Vacio6.items()}')
print (f'{Diccionario_Vacio6["Key4"]}')
print (f'{Diccionario_Vacio6.get("Key5")}')

print (f'-' * 20)

Fecha5 = '2026-04-01'

try:
    Fech5 = datetime.strptime(Fecha5, '%Y-%m-%d').date()
    Fech5_Formateada = pd.to_datetime(Fech5)
    Cargar_Csv5['date'] = pd.to_datetime(Cargar_Csv5['date'])
except (Exception, ValueError):
    print (f'Error, la fecha tiene un formato incorrecto')
    exit()
    
Cargar_Csv5['TOTALITO'] = Cargar_Csv5['quantity'] * Cargar_Csv5['price']
    
Encontrado4 = Cargar_Csv5[Cargar_Csv5['date'].dt.date == Fech5_Formateada.date()]

if (Encontrado4.empty):
    print (f'No hay ventas reportadas en esta fecha')
else:
    print (f'Genial! Encontramos ventas')
    
    Grupo9 = Encontrado4.groupby('product')['quantity'].sum()
    Grupo9_Min = Grupo9.idxmin()
    Grupo9_Max = Grupo9.idxmax()
    Grupo9_Min_Cant = Grupo9.min()
    Grupo9_Max_Cant = Grupo9.max()
    
    print (f'El producto {Grupo9_Min} vendio {Grupo9_Min_Cant} unidades')
    print (f'El producto {Grupo9_Max} vendio {Grupo9_Max_Cant} unidades')
    
    print (f'El total de unidades vendidas en esta fecha fue de {Grupo9.sum()}')
    
    print (f'La cantidad de clientes que nos compraron hoy fue {Grupo9.count()}')
    
    Promedio6 = Grupo9.sum() / Grupo9.count()
    
    print (f'El promedio de ventas en esta fecha fue de {round(Promedio6, 2)}')
    print (f'El promedio de ventas en esta fecha fue de {round(Grupo9.mean(), 2)}')
    
    Grupo10 = Encontrado4.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue de ${Grupo10}')
    
    Promedio7 = Grupo10.sum() / Grupo9.count()
    
    print (f'El promedio de dinero vendido fue de ${round(Promedio7, 2)}')
    print (f'El promedio de dinero vendido fue de ${round(Grupo10.mean(), 2)}')
    
print (f'-' * 20)

Diccionario_Numeral3 = {
    'Num1' : 7,
    'Num2' : 2,
    'Num3' : 8,
    'Num4' : 0,
    'Num5' : 1
}

print (f'{Diccionario_Numeral3}')

Diccionario_Numeral3_Sorted = dict(sorted(Diccionario_Numeral3.items(), key=lambda item : item[1]))

Diccionario_Numeral3_Sorted_Min = min(Diccionario_Numeral3_Sorted.items(), key=lambda item : item[1])
Diccionario_Numeral3_Sorted_Max = max(Diccionario_Numeral3_Sorted.items(), key=lambda item : item[1])

print (f'{Diccionario_Numeral3_Sorted}')
print (f'{Diccionario_Numeral3_Sorted_Min}')
print (f'{Diccionario_Numeral3_Sorted_Max}')

print (f'-' * 20)

Division_Baja = 14 // 7
Exponente = 4**3
Modulo = 12 % 7

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(Division_Baja)}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'-' * 20)

print (f'El tipo de dato de la variable es {type(Variable1)}')
print (f'El tipo de dato de la variable es {type(Variable4)}')
print (f'El tipo de dato de la variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de dato de la variable es {type(Objeto10.Catched)}')
print (f'El tipo de dato de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato de la variable es {type(Tupla_Nombres3)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de dato de la variable es {type(Diccionario_Vacio3)}')
print (f'El tipo de dato de la variable es {type(Funcion_Diccionario)}')
print (f'El tipo de dato de la variable es {type(Objeto11)}')
print (f'El tipo de dato de la variable es {type(Poke_Kid1)}')
print (f'El tipo de dato de la variable es {type(Array2_Sorted_Mean)}')
print (f'El tipo de dato de la variable es {type(Data_Frame_Concatenado)}')
print (f'El tipo de dato de la variable es {type(PEPE)}')

print (f'-' * 20)

if (Diccionario3['Ingresos'] > 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Los ingresos son altos, Los gastos son bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Los ingresos son altos, Los gastos estan al limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Los ingresos son altos, Los gastos son altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] == 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Los ingresos son minimos, Los gastos son bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Los ingresos son minimos, Los gastos estan al limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Los ingresos son minimos, Los gastos son altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] < 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Los ingresos son bajos, Los gastos son bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Los ingresos son bajos, Los gastos estan al limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Los ingresos son bajos, Los gastos son altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')
    
print (f'-' * 20)

if (len(Lista_Uno_Copia) > 5):
    print (f'Tenemos mas de 5 elementos')
else:
    print (f'Tenemos 5 o menos elementos')
    
if (Variable1.__len__() > 5):
    print (f'La palabra tiene mas de 5 letras')
else:
    print (f'La palabra tiene 5 o menos letras')
    
print (f'-' * 20)

var18 = Saludar_Dos()
var19 = 29

if (var18 == Variable1 and var19 >= 30):
    print (f'Correcto, ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumplen')
    
if (var18 == Variable1 or var19 >= 30):
    print (f'Correcto, al menos una de las condiciones se cumple')
else:
    print (f'Error, ninguna de las condiciones se cumplen')
    
print (f'-' * 20)

print (f'{dir(PEPE)}')

def Ejercicio57(Num1:int, Num2:int) -> int:
    '''Esto es un docstring, recibimos dos parametros y devolvemos el resultado de la suma'''
    return Num1 + Num2

print (f'El resultado de la operacion es {Ejercicio57(12, 7)}')

print (f'{help(Ejercicio57)}')

print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorito):
        self.Trainer = Trainer
        self.City = City
        self.Favorito = Favorito
        self.Pokedex = 18 * 2
        
    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorito} while visiting {self.City}')
        
    def Mostrar(self):
        return self.Trainer
    
    @property
    def Mostrar2(self):
        return self.Trainer
    
    def __str__(self):
        return self.Trainer
    
Objeto28 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto9.Nombre)
Objeto29 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto10.Nombre)
Objeto30 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto11.Nombre)

Objeto28.Desplegar()
Objeto29.Desplegar()
Objeto30.Desplegar()

print (f'-' * 20)

print (f'Hola, mi nombre es {Objeto28.Mostrar()}')
print (f'Hola, mi nombre es {Objeto28}')
print (f'Hola, mi nombre es {Objeto28.Trainer}')

print (f'-' * 20)

print (f'Hola, mi nombre es {Objeto29.Mostrar()}')
print (f'Hola, mi nombre es {Objeto29}')
print (f'Hola, mi nombre es {Objeto29.Trainer}')

print (f'-' * 20)

print (f'Hola, mi nombre es {Objeto30.Mostrar()}')
print (f'Hola, mi nombre es {Objeto30}')
print (f'Hola, mi nombre es {Objeto30.Trainer}')

print (f'-' * 20)

Negativo = -5

print (f'Ahora es positivo {abs(int(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros1)
Anonima4 = filter(lambda num : num % 2 == 0, PEPE.Lista_Numeros1)
Lista_Iterable = [Num for Num in PEPE.Lista_Numeros1 if Num % 2 == 0]

print (f'{Any_Iterable}')
print (f'{list(Anonima4)}')
print (f'{Lista_Iterable}')

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

Diccionario_Numeral4 = {
    'Num1' : 7,
    'Num2' : 2,
    'Num3' : 8,
    'Num4' : 0,
    'Num5' : 1
}

Diccionario_Numeral4_Sorted = dict(sorted(Diccionario_Numeral4.items(), key=lambda item : item[1]))
Diccionario_Numeral4_Sorted_Min = min(Diccionario_Numeral4_Sorted.items(), key=lambda item : item[1])
Diccionario_Numeral4_Sorted_Max = max(Diccionario_Numeral4_Sorted.items(), key=lambda item : item[1])

print (f'{Diccionario_Numeral4}')
print (f'{Diccionario_Numeral4_Sorted}')
print (f'{Diccionario_Numeral4_Sorted_Min}')
print (f'{Diccionario_Numeral4_Sorted_Max}')

print (f'-' * 20)

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, ingrese una cadena de texto')
    
print (f'-' * 20)

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in enumerate(Lista_Uno_Copia[0:None]):
    print (f'{elemento[0]} : {elemento[1]}')
    
print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia[:], start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Uno_Copia, Set_Conjunto_Menu1):
    print (f'{elemento1} : {elemento2}')
    
print (f'-' * 20)

var20 = 'eSteBAN'
var20_letra = var20[0]

print (f'{var20}')
print (f'{var20.lower()}')
print (f'{var20.upper()}')
print (f'{var20.capitalize()}')
print (f'{var20.title()}')

Lista_Nombres5 = ['juan salvo', 'henry courtney', 'elizabeth bennet', 'marge simpson']
Lista_Nombres5_Actualizada = []

for elemento in Lista_Nombres5:
    Lista_Nombres5_Actualizada.extend([elemento.title()])
    
print (f'{Lista_Nombres5}')
print (f'{Lista_Nombres5_Actualizada}')

print (f'-' * 20)

print (f'La letra {var20_letra} se encuentra en la posicion {var20.index("e")}')
print (f'La letra {var20_letra} se encuentra en la posicion {var20.find("e")}')

print (f'La letra {var20_letra} aparece un total de {var20.count(var20_letra)} veces')

print (f'{var20.lower().startswith(var20_letra)}')
print (f'{var20.lower().endswith("n")}')

print (f'{var20.lower().replace("ban", "POPOTAMO")}')

var21 = '          Lautaro'

print (f'{var21}')
print (f'{var21.strip()}')
print (f' '.join(var21.split()))

var22 = '----hola mundo***'

print (f'{var22}')
print (f'{var22.strip("-*")}')

var23 = 'esto es un texto cualquiera, quiero saber si es posible recorrer este texto'

Lista_var23 = var23.split(' ')

for elemento in Lista_var23:
    print (f'{elemento}')
    
print (f'La cantidad de palabras es {len(Lista_var23)}')

print (f'-' * 20)

var24 = 'texto'

if (isinstance(var24, (str))):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Error, esto no es un texto')
    
if (var24.isalpha()):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Error, esto no es un texto')
    
try:
    Resultado = 12 + var24 #type: ignore
except TypeError:
    print (f'Lo que ingresaste es texto')
    
print (f'-' * 20)
    
var25 = 3.5

if (isinstance(var25, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, esto no es un numero decimal')
    
try:
    Numerito8 = float(var25)
    if (Numerito8.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var26 = '3'

if (isinstance(var26, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var26.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
if (var26.isdecimal()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, esto no es un numero entero')
    
try:
    Numerito9 = float(var26)
    if (Numerito9.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var27 = 3

if (isinstance(var27, (int, float))):
    print (f'Esto es un numero entero o decimal')
else:
    print (f'Error de formato')
    
try:
    Numerito10 = float(var27)
    if (Numerito10.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var28 = 'erick12'

if (isinstance(var28, (int, str))):
    print (f'Eesto es un numero o un texto')
else:
    print (f'Error de formato')
    
if (var28.isalnum()):
    print (f'Eesto es un numero o un texto')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var29 = '   e    '

if (var29.isspace()):
    print (f'Esto esta compuesto unicamente por espacios')
else:
    print (f'Error, esto contiene mucho mas que espacios')
    
print (f'-' * 20)

var30 = 'eSteBAN RaMIREz'

if (var30.lower().islower()):
    print (f'Correcto, todo esto esta en minuscula')
    
if (var30.upper().isupper()):
    print (f'Correcto, todo esto esta en mayuscula')
    
if (var30.title().istitle()):
    print (f'Correcto, todo esto esta en camel case')
    
print (f'-' * 20)

var31 = ' '

if (bool(var31) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, ingrese una cadena de texto')
    
print (f'-' * 20)

print (f'El elemento {PEPE.Tupla_Poke[2]} aparece en la posicion {PEPE.Tupla_Poke.index("Misty")}')

Lista_var23_Copia = Lista_var23.copy()

print (f'{Lista_var23_Copia}')

print (f'{Diccionario1_Copia}')
Diccionario1_Copia.clear()
print (f'{Diccionario1_Copia}')

Diccionario_Eliminado = Diccionario3.pop("Ingresos")

print (f'{Diccionario3}')
print (f'El elemento que se elimino fue {Diccionario_Eliminado}')

print (f'-' * 20)

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')
    
for indice, elemento in Diccionario2.items():
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

for elemento in Diccionario2:
    print (f'{Diccionario2[elemento]}')
    
print (f'-' * 20)

for elemento in Diccionario2.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario2.values():
    print (f'{elemento}')
    
print (f'-' * 20)

try:
    snake_case7, snake_case8, snake_case9 = PEPE.Tupla_Poke
except ValueError as Errore5:
    print (f'Error, este desempaquetado de variables es incorrecto -> {Errore5}')
    
Contador = 0

while (Contador < 5):
    print (f'El contador es {Contador + 1}')
    Contador += 1
    
print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros1)):
    print (f'El numero es {PEPE.Lista_Numeros1[Contador] * 100}')
    Contador += 1
    
print (f'-' * 20)

Lista_Animales2 = ['Avestruz', 'Hiena']
Lista_Animales2.append('Tortuga')
Lista_Animales2.insert(3, 'Gusano')
Lista_Animales2.extend([PEPE.Lista2[2]])

print (f'{Lista_Animales2}')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        # print (f'{Documento_Lineas}')
        for elemento in Documento_Lineas:
            if (elemento.strip() == "Pikachu"):
                Lista_Animales2.extend([elemento.strip()])
                break
            else:
                continue
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo seleccionado es incorrecto')
    
print (f'{Lista_Animales2}')

Contador = 0

while (Contador < len(Lista_Animales2)):
    if (Lista_Animales2[Contador] == 'Tortuga'):
        print (f'La tortuga siempre ha sido uno de mis animales favoritos')
        break
    else:
        Contador += 1
        continue
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Uno_Copia, Set_Conjunto_Menu1):
    print (f'{elemento1} : {elemento2}')
    
print (f'-' * 20)

for elemento1, elemento2, elemento3 in zip(Lista_Uno_Copia, Set_Conjunto_Menu1, PEPE.Tupla_Poke):
    print (f'{elemento1} : {elemento2} : {elemento3}')
    
print (f'-' * 20)

for elemento1 in zip(Lista_Uno_Copia):
    print (f'{elemento1}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(0 + 1, 5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(0 + 1, len(Lista_Uno_Copia)):
    print (f'{elemento}')
    
Lista_Numeros1_Mult = [Num  * 100 for Num in PEPE.Lista_Numeros1]

print (f'{PEPE.Lista_Numeros1}')
print (f'{Lista_Numeros1_Mult}')

print (f'-' * 20)

Menor = min(Lista_Numeros1_Mult)
Mayor = max(Lista_Numeros1_Mult)

print (f'El Menor de los numeros es {Menor}')
print (f'El Mayor de los numeros es {Mayor}')

Redondeado = round(14.458795, 2)

print (f'El numero 14.458795 redondeado es {Redondeado}')

print (f'{bool(False)}')
print (f'{bool(not True)}')
print (f'{bool("")}')
print (f'{bool(None)}')
print (f'{bool(0)}')

print (f'-' * 20)

Todo_All = all([Lista_Uno_Copia, Set_Conjunto1, Tupla1, None])

print (f'{Todo_All}')

Sumatoria4 = sum(Lista_Numeros1_Mult)

print (f'El resultado de la sumatoria es {Sumatoria4}')

var33 = int('500')
var34 = str(500)
var35 = float(var33)
var36 = list(PEPE.Tupla_Poke)
var37 = set(Lista_Uno_Copia)
var38 = tuple(Set_Conjunto_Menu2)

print (f'El tipo de variable {type('500')} se convierte en {type(var33)}')
print (f'El tipo de variable {type(500)} se convierte en {type(var34)}')
print (f'El tipo de variable {type(var33)} se convierte en {type(var35)}')
print (f'El tipo de variable {type(PEPE.Tupla_Poke)} se convierte en {type(var36)}')
print (f'El tipo de variable {type(Lista_Uno_Copia)} se convierte en {type(var37)}')
print (f'El tipo de variable {type(Set_Conjunto_Menu2)} se convierte en {type(var38)}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto_Poke1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

from Paquete.Sub_Paquete import Segundo as PEPE3

variable_PEPE3 = PEPE3

print (f'-' * 20)

'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese la cantidad de alumnos '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.extend([Estudiante])
        
    Lista.sort(key = lambda num : num[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes es {Menore}')
    print (f'El mayor de los estudiantes es {Mayore}')

Colegio(Lista_Alumnos)'''

'''def Ejercicio63(Limite):
    Contador = 0
    while (Contador < Limite):
        while (True):
            Numerito11 = input(f'Ingrese un numero: ')
            try:
                Numerito12 = float(Numerito11)
                if (Numerito12.is_integer()):
                    print (f'Lo que ingresaste es un numero entero')
                    break
                else:
                    print (f'Lo que ingresaste es un numero decimal')
                    break
            except ValueError:
                print (f'Error, lo que ingresastes no es un numero')
        Contador += 1

Sample63 = Ejercicio63(1)'''

import pandas as pd
import requests
import io

Ruta_Html2 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html2, headers=headers)

Leer_Html2 = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Leer_Html2)

print (f'{Cargar_Html2[1].head()}')

print (f'-' * 20)

import re

Texto12 = 'ericksuper80@gmail.com'

Pattern18 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Buscar19 = bool(re.fullmatch(Pattern18, Texto12))

if (Buscar19 == True):
    print (f'El correo electronico tiene el formato correcto')
else:
    print (f'Error, el correo electronico tiene el formato incorrecto')
    
print (f'-' * 20)

import re

Texto13 = '32'

Pattern19 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar20 = bool(re.match(Pattern19, Texto13))

if (Buscar20 == True):
    print (f'Correcto, el numero esta entre 00 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv6 = 'C:\\Repo\\Store.csv'

Cargar_Csv6 = pd.read_csv(Ruta_Csv6)

print (f'{Cargar_Csv6}')

print (f'-' * 20)

Fecha6 = '2026-04-01'

try:
    Fech6 = datetime.strptime(Fecha6, '%Y-%m-%d').date()
    Fech6_Formateada = pd.to_datetime(Fech6)
    Cargar_Csv6['date'] = pd.to_datetime(Cargar_Csv6['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato incorrecto')
    exit()
    
Cargar_Csv6['TOTALITO'] = Cargar_Csv6['quantity'] * Cargar_Csv6['price']
    
Encontrado5 = Cargar_Csv6[Cargar_Csv6['date'].dt.date == Fech6_Formateada.date()]

if (Encontrado5.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! se han encontrado ventas en esta fecha')
    
    Grupo11 = Encontrado5.groupby('product')['quantity'].sum()
    Grupo11_Min = Grupo11.idxmin()
    Grupo11_Max = Grupo11.idxmax()
    Grupo11_Min_Cant = Grupo11.min()
    Grupo11_Max_Cant = Grupo11.max()
    
    print (f'El producto que vendio menos de la lista fue {Grupo11_Min} con una cantidad de {Grupo11_Min_Cant} unidades')
    print (f'El producto que vendio mas de la lista fue {Grupo11_Max} con una cantidad de {Grupo11_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron hoy fueron {Grupo11.count()}')
    
    print (f'La cantidad total de productos vendidos fue {Grupo11.sum()}')
    
    Promedio8 = Grupo11.sum() / Grupo11.count()
    
    print (f'El promedio de productos vendidos fue {round(Promedio8, 2)}')
    print (f'El promedio de productos vendidos fue {round(Grupo11.mean(), 2)}')
    
    Grupo12 = Encontrado5.groupby('product')['TOTALITO'].sum()
    
    Promedio8 = Grupo12.sum() / Grupo12.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio8, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Grupo12.mean(), 2)}')
    
print (f'-' * 20)

class Inventario2():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
    
Objeto31 = Inventario2()

Objeto31.Productos.append('Cuaderno')
Objeto31.Productos.insert(1, 'Lapicero')
Objeto31.Productos.extend(['Calculadora'])

print (f'La cantidad de productos es {len(Objeto31)}')

print (f'-' * 20)

class Persona3():
    def __init__(self, Nombre):
        self.Nombre = Nombre

    def Mostrar(self):
        return self.Nombre
    
    @property
    def Mostrar2(self):
        return self.Nombre
    
    def __len__(self):
        return self.Nombre
    
Objeto32 = Persona3('Erick Josue Perez Gutierrez')

print (f'Mi nombre completo es {Objeto32.Mostrar()}')
print (f'Mi nombre completo es {Objeto32.Mostrar2}')
print (f'Mi nombre completo es {Objeto32.Nombre}')

print (f'-' * 20)

class Persona4():
    def __init__(self, Pokemon):
        self.Pokemon = Pokemon
        
    def Mostrar(self):
        return self.Pokemon
    
    @property
    def Mostrar2(self):
        return self.Pokemon
    
    def __repr__(self):
        return self.Pokemon
        
Objeto33 = Persona4(PEPE.Diccionario_Poke["Poke3"])

print (f'{Objeto33.Mostrar()}')
print (f'{Objeto33.Mostrar2}')
print (f'{Objeto33.Pokemon}')

print (f'-' * 20)

class Persona5():
    def __init__(self, Color):
        self.Color = Color

    def __repr__(self):
        return self.Color
    
Lista_Colores2 = [
    Persona5('Rojo'),
    Persona5('Azul'),
    Persona5('Verde')
]

print (f'La lista de colores es {Lista_Colores2}')

print (f'-' * 20)

class Igualdad2():
    def __init__(self, Nombre):
        self.Nombre = Nombre

    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
    
Objeto34 = Igualdad2('Erick')
Objeto35 = Igualdad2('Erick')

if (Objeto34 == Objeto35):
    print (f'Ambos objetos son iguales')
else:
    print (f'Error, los objetos no son iguales')
    
print (f'-' * 20)

class Caja2():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto36 = Caja2(5)
Objeto37 = Caja2(3)

print (f'La suma de los pesos es {Objeto36 + Objeto37}')

print (f'-' * 20)

class Inventario3():
    def __init__(self):
        self.Articulos = []
        
    def __getitem__(self, Indice):
        return self.Articulos[Indice]
        
Objeto38 = Inventario3()

Objeto38.Articulos.append('Calculadora')
Objeto38.Articulos.insert(1, 'Zapatos')
Objeto38.Articulos.extend(['Cucharas'])

print (f'El elemento en la posicion 0 es {Objeto38[0]}')
print (f'El elemento en la posicion 1 es {Objeto38[1]}')
print (f'El elemento en la posicion 2 es {Objeto38[2]}')

print (f'-' * 20)

class Panaderia2():
    def __init__(self):
        self.Panes = [
            'Baguettes',
            'Croissant',
            'Donas'
        ]
        
    def __iter__(self):
        return iter(self.Panes)
    
Objeto39 = Panaderia2()

for indice, elemento in enumerate(Objeto39, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

'''import requests

Diccionario_Api = {
    'Helado1' : "Pistacho",
    'Helado2' : "Chicle",
    'Helado3' : "Macadamia"
}

Elemento_Api1 = requests.get('http://127.0.0.1:8000/unidad1/')
Elemento_Api2 = Elemento_Api1.json()

print (f'{Elemento_Api2}')
print (f'{Elemento_Api1.status_code}')

print (f'-' * 20)

Elemento_Api3 = requests.post('http://127.0.0.1:8000/unidad1/elemento1', json=(Diccionario_Api))
Elemento_Api4 = Elemento_Api3.json()

print (f'Agregado: {Elemento_Api4}')
print (f'{Elemento_Api3.status_code}')'''