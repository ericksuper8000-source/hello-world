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

def Ejercicio57(Lista):
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
# Borre un valor de una lista Uno usando del
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


'''

✅ Operaciones principales de conjuntos en Python
Supongamos los siguientes conjuntos para los ejemplos:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

1. 🔹 Unión (union)
Devuelve todos los elementos de ambos conjuntos sin repetir.
A.union(B)
# o también
A | B
Resultado:
{1, 2, 3, 4, 5, 6}

2. 🔹 Intersección (intersection)
Devuelve los elementos comunes entre los conjuntos.
A.intersection(B)
# o también
A & B
Resultado:
{3, 4}

3. 🔹 Diferencia (difference)
Devuelve los elementos que están en un conjunto pero no en el otro.
A.difference(B)
# o también
A - B
Resultado:
{1, 2}
También puedes obtener la diferencia inversa:
B - A  # {5, 6}

4. 🔹 Diferencia simétrica (symmetric_difference)
Devuelve los elementos que están en uno u otro conjunto, pero no en ambos.
A.symmetric_difference(B)
# o también
A ^ B
Resultado:
{1, 2, 5, 6}

5. 🔹 Subconjunto (issubset)
Verifica si todos los elementos de un conjunto están contenidos en otro.
A.issubset(B)
# o también
A <= B
Ejemplo:
C = {1, 2}
C.issubset(A)  # True

6. 🔹 Superconjunto (issuperset)
Verifica si un conjunto contiene todos los elementos de otro.
A.issuperset(C)
# o también
A >= C

7. 🔹 Conjuntos disjuntos (isdisjoint)
Determina si dos conjuntos no tienen elementos en común.
A.isdisjoint(B)
Ejemplo:
D = {7, 8}
A.isdisjoint(D)  # True

8. 🔹 Operaciones con actualización (modifican el conjunto original)

Unión   update()    -----  Conserva los elementos no comunes
Intersección    intersection_update()    --- Conserva solo los elementos comunes
Diferencia      difference_update()    ---  Elimina los elementos presentes en el otro conjunto
Diferencia simétrica     symmetric_difference_update()      --- Conserva los elementos no comunes

Conserva los elementos no comunes
Ejemplo:
A = {1, 2, 3}
B = {3, 4}
A.update(B)
print(A)  # {1, 2, 3, 4}


'''


Jugar con APIs
En un GET, FastAPI convierte dict → JSON y requests hace JSON → dict.
En un POST, requests hace dict → JSON y FastAPI hará JSON → dict.


Unidad1 = requests.get('http://127.0.0.1:8002/grupo1/')

Agregado1 = requests.post(URL, params={'Elemento' : Nuevo_Sabor})   "Ojo esto se usa si usamos Query"
Agregado1 = requests.post(URL, json=Nuevo_Sabor)   "Esto se usa si usamos Body"

Reemplazado1 = requests.put(URL2, params={"Indice": Indice}, json=Nuevo_Saborcito)

Indice = 1
URL_DELETE = 'http://127.0.0.1:8002/grupo1/'

Eliminado1 = requests.delete(
    URL_DELETE,
    params={
        "Indice": Indice
    }
)



# El restaurante tiene un menú fijo de jugos. Este menú nunca cambia, entonces hagamos un set con frozenset({}) de 3 sabores que no pueden cambiar
# Intentar agregar un nuevo sabor con el metodo .add() para obtener un error
# Ahora hacemos otro set_conjunto con 3 sabores, pero este es un set normal
# Intentar agregar un nuevo sabor con el metodo .add()



-----------------------------------------------------------------


Jugar con APIs
En un GET, FastAPI convierte dict → JSON y requests hace JSON → dict.
En un POST, requests hace dict → JSON y FastAPI hará JSON → dict.


Unidad1 = requests.get('http://127.0.0.1:8002/grupo1/')

Agregado1 = requests.post(URL, params={'Elemento' : Nuevo_Sabor})   "Ojo esto se usa si usamos Query"
Agregado1 = requests.post(URL, json=Nuevo_Sabor)   "Esto se usa si usamos Body"

Reemplazado1 = requests.put(URL2, params={"Indice": Indice}, json=Nuevo_Saborcito)

Indice = 1
URL_DELETE = 'http://127.0.0.1:8002/grupo1/'

Eliminado1 = requests.delete(
    URL_DELETE,
    params={
        "Indice": Indice
    }
)


----------------------------------------------------------------------------------

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
# Ahora hagamos un diccinario completamente vacio dict({}) y vamos a meterle elementos a un diciconario que no tiene claves ni valores

# Hagamos un diccionario vacio con fromkeys, luego una lista de elementos y agregue los elementos de la lista al diccionario con un ciclo    i=0

'''Hagamos un diccionario nuevo y saquemos diferentes elementos con
.keys()
.values()
.items()
'''


# A partir de los elementos del csv file, vamos a crear primero una lista de llaves, luego vamos a tomar los nombres y agregarlos a una lista
# finalmente vamos a crear un diccionario y emparejar las llaves creadas y los nombres y mostramos el nuevo diccionario creado

# Haga un diccionario con Claves tres, uno, cuatro... y valores 3, 1, 4... y ordene los valores para que se muestren en orden 
Diccionario4_Sorted = dict(sorted(Diccionario4.items(), key=lambda item : item[1]))
Ahora con ese mismo diccionario saquemos el menor de todas las tuplas
Ahora con ese mismo diccionario saquemos el mayor de todas las tuplas

--------------------------------------------

---------------------------------------------

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
# Haga la primera letra de cada una de las palabras de una cadena con title

# En este ejercicio se solicita que cada una de las palabras de la lista comiencen con letra mayuscula. 
Lista_Nombres2 = ['juan salvo', 'henry courtney', 'elizabeth bennet', 'marge simpson']
Recorra la lista con for, use el metodo .title() para que tanto nombre como apellido comiencen con Mayuscula y el resultado agreguelo a una lista actualizada.

# Busque una letra en especifico en una cadena de texto con el metodo find e index
# Cuantas veces esta la letra a en una cadena con el metodo count
# Verifiquemos si una cadena comienza con x letra con el metodo startswith
# Verifiquemos si una cadena termina con x letra con el metodo endswith
# Reemplace una parte de una cadena con el metodo replace(Este tiene dos parametros, lo que se quiere cambiar y lo nuevo)

Strip lo que hace es eliminar espacios
nombre = '          Lautaro'
print (f'{nombre.strip()}')

# que pasa cuando a strip le pasamos argumentos? Elimina ese argumento de la cadena
Textico3 = '----hola mundo***'
print (f'{Textico3.strip("-*")}')

# Tome una variable de texto y separe cada elemento de la variable en una lista separada por ',' utilizando el metodo split()


'''
| Método        | Descripción                            |
| ------------- | -------------------------------------- |
| `isalpha()`   | Solo letras                            |
| `isinstance()`| Solo dígitos decimales                 |  mas util
| `isnumeric()` | Cualquier carácter numérico            | # Si vas a usar int() para convertir el texto a número, usa siempre isdecimal().
| `isnumeric()` | Entero o decimal    (int, float)       |
| `isalnum()`   | Letras y números                       |
| `isspace()`   | Solo espacios                          |
| `islower()`   | Letras en minúsculas                   |
| `isupper()`   | Letras en mayúsculas                   |
| `istitle()`   | Cada palab comienza mayuscula          |
| `bool()`   | Vacio                 |
'''

variable13 = 4.3

if (isinstance(variable13, float)):
    print (f'El numero es decimal')
else:
    print (f'Error, no es decimal')


# Busque un elemento en una lista o tupla con index, ojo find no es un metodo para listas
# Declare una variable y asignele una copia de una lista con el metodo copy()
# Borrar todos los elementos de un diccionario con clear()
# Eliminar un elemento del diccinario con pop()
    Precio = Productos5.pop("Mouse")
    Elimina esta clave -- Devuelve el valor que tenía.
    
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
# Hagamos un ciclo for con la funcion range range(0 + 2, len(Lista_Animales)
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
# Convierte un número a texto y viceversa  str(), int(), float(), tambien convierta un set en una lista, una lista en un set, y un set en una tupla
# Despliegue los numeros de 90 a 100 con range()
# Imprime los elementos de una lista con su posición.     enumerate()
# Combina dos listas y muéstralas juntas    zip()
# Ordena una lista de números con sort, sort(reverse = True) reverse()

# Verifique si un elemento de una tupla es par con any()
# Cree una list(), tuple(), set(), dict()
# Cree una lista de 4 palabras por ejemplo mi nombre completo y unalas con la funcion print ("-".join(Lista))

# Divide un texto por espacios con split()



# Usemos elementos de un modulo por medio de un import
# Renombremos un modulo con la instrucion "as" Saludar as OtroNombre




##############################     ENRUTAMIENTO DE MODULOS     ######################################
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
# Ojo hagamos un ejemplo de validacion de correo electronico que pida explicitamente hotmail, gmail, yahoo o .com, .net .org  pattern1 = r'^[a-zA-Z0-9./*-+=_/?]+\@(hotmail|gmail|yahoo)\.(com|net|org)$'

# Busque un numero que debe estar explicitamente entre 01 y 31. pattern1 = r'(0[0-9]|[12][0-9]|3[01])'

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


Quiero crear una columna nueva agregada sobre el mismo csv con el total en precio multiplicando cantidad x price

Cargar_Csv5['Total'] = Cargar_Csv5['quantity'] * Cargar_Csv5['price']

print (f'{Cargar_Csv5}')

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


class Inventario:
    def __init__(self):
        self.productos = []

    def __len__(self):
        return len(self.productos)

inventario = Inventario()

inventario.productos.append("Laptop")
inventario.productos.append("Mouse")

print(len(inventario))

------------------------

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

usuario = Usuario("Erick", "erick@gmail.com")

print(usuario)

Salida:

<__main__.Usuario object at 0x00000123456789>

------------------------

Con __str__:

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return self.nombre

usuario = Usuario("Erick", "erick@gmail.com")

print(usuario)

Salida:

Erick

------------------------

class Persona4:
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
        
Objeto49 = Persona4('Erick')
Objeto50 = Persona4('Erick')

print (f'{Objeto49 == Objeto50}')

----------------------------


class Persona7():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Objeto65 = Persona7('Carmen')

Lista_Persona7 = [
    Persona7('Julian'),
    Persona7('Roberta'),
    Persona7('Ana')
]

print (f'{Lista_Persona7}')



class Caja():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto70 = Caja(5)
Objeto71 = Caja(4)

print (f'El resultado de la suma es {Objeto70 + Objeto71}')




class Inventario2():
    def __init__(self):
        self.Productos = ['Laptop', 'Parlante', 'Celular']
        
    def __getitem__(self, indice):
        return self.Productos[indice]
    
Objeto45 = Inventario2()

print (f'{Objeto45[0]}')
print (f'{Objeto45[1]}')
print (f'{Objeto45[2]}')

------------------------


class Panaderia():
    def __init__(self):
        self.Panes = ['Baguette', 'Croissant', 'Pan Dulce']
        
    def __iter__(self):
        return iter(self.Panes)
        
Objeto59 = Panaderia()

for elemento in Objeto59:
    print (f'{elemento}')
    
    
-------------------------

Hay un Api.py que tiene un mini programa, por medio de request quiero que llames esa api tomes el nombre y hagas algun tipo de operacion con este API
Recuerda encender la API antes de consumirla

------------------------


from fastapi import FastAPI

app = FastAPI()

Lista_Elementos = list([])

@app.get('/ejemplo')
def Primera():
    return {
        'Resultado' : Lista_Elementos
    }

@app.post('/ejemplo')
def Segunda(
        Elemento : dict
):
    Lista_Elementos.append(Elemento)
    return {
        'Agregado' : Lista_Elementos
    }
    
------------------------------------------


# POO
class Automovil:
    
    ''' Clase que identifica un automóvil '''

    # Visibilidad (públicos / privados)
    # __ -> atr. privado
    # Encapsulamiento
    
    # Constructor
    def __init__(self, marca, modelo, velocidad_maxima):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = 0
        self.__velocidad_max = velocidad_maxima

    # Métodos
    def acelerar(self, kms_h):
        if kms_h >= 0:
            velocidad_aux = self.__velocidad + kms_h
            if velocidad_aux <= self.__velocidad_max:
                self.__velocidad = velocidad_aux
            else:
                self.__velocidad = self.__velocidad_max

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


-------------------------------------