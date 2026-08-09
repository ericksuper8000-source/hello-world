try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo es incorrecto')
    raise

variable1 = 3

print (f'{type(variable1)}')

variable1 = 'hola'

print (f'{type(variable1)}')

variable2 = '500'

print (f'{type(variable2)}')
print (f'{type(int(variable2))}')

Lista_Primera = ['Erick', 'Josue']
Lista_Segunda = list(['Karlita'])

print (f'{Lista_Primera + Lista_Segunda}')

Tupla_Primera = ('Erick', 'Josue')
Tupla_Segunda = ('Karlita',)

print (f'{Tupla_Primera + Tupla_Segunda}')

variable3 = 0

if (variable3):
    print (f'Esto se puede usar como divisor')
else:
    print (f'Esto no se puede usar como divisor')
    
print (f'-' * 20)

variable4 = ''

if (variable4):
    print (f'Esta es una cadena de texto util')
else:
    print (f'Perdon pero esto no se puede usar')
    
print (f'-' * 20)

Lista_Tercera = []

if (Lista_Tercera):
    print (f'La lista tiene contenido')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Diccionario_Primera = dict({})

if (Diccionario_Primera):
    print (f'El diccionario tiene contenido')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

variable5 = None

if (variable5):
    print (f'Esto es True')
else:
    print (f'Esto es False')
    
print (f'-' * 20)

Lista_Ejemplo1 = [1, 2, 3, 4, 5]

def Ejercicio1(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        
        while (Contador < len(Lista)):
            Contador += 1
            
        return Contador

Sample1 = Ejercicio1(Lista_Ejemplo1)

if (Sample1 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La cantidad de elementos de la lista es {Sample1}')
    
print (f'-' * 20)

def Ejercicio2(Lista):
    Acumulador = 0
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador += elemento
        else:
            continue
        
    return Acumulador

Sample2 = Ejercicio2(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample2 > 0):
        print (f'La suma de los numeros pares es {Sample2}')
    else:
        print (f'Error, no hay numeros pares en la lista')
        
print (f'-' * 20)

def Ejercicio3(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        
        for elemento in Lista:
            Acumulador += elemento
            
        return Acumulador

Sample3 = Ejercicio3(Lista_Ejemplo1)

if (Sample3 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de todos los elementos de la lista es {Sample3}')
    
print (f'-' * 20)

def Ejercicio4(Lista):
    Acumulador = 0
    
    for elemento in Lista[:-1]:
        Acumulador += elemento
        
    return Acumulador

Sample4 = Ejercicio4(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de los numeros menos el ultimo de la lista es {Sample4}')
    
print (f'-' * 20)

def Ejercicio5(Lista, Numero):
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

Numerito1 = 4

Sample5 = Ejercicio5(Lista_Ejemplo1, Numerito1)

if (Sample5 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample5 is True):
        print (f'El numero {Numerito1} fue encontrado en la lista')
    else:
        print (f'Error, el numero {Numerito1} no se ubico en la lista')
        
print (f'-' * 20)

Lista_Resultado = None

def Ejercicio6(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    Lista_Resultado = [Menore, Mayore]
    
    return Lista_Resultado

Sample6 = Ejercicio6(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de los numeros de la lista es {min(Sample6)}')
    print (f'El mayor de los numeros de la lista es {max(Sample6)}')
    
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
    
Numerito2 = 4

Sample7 = Ejercicio7(Lista_Ejemplo1, Numerito2)

if (Sample7 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample7 > 0):
        print (f'La cantidad de numeros en la lista mayores a {Numerito2} es {Sample7}')
    else:
        print (f'Error, no se encontro un solo numero mayor a {Numerito2} en la lista')
        
print (f'-' * 20)

def Ejercicio8(Lista):
    Lista_Pares = []
    Lista_Impares = list([])
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            Lista_Impares.extend([elemento])
            
    return Lista_Pares, Lista_Impares

Sample8 = Ejercicio8(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    Lista_Pares, Lista_Impares = Sample8
    
    print (f'Lista Original: {Lista_Ejemplo1}')
    print (f'Lista Pares: {Lista_Pares}')
    print (f'Lista Impares: {Lista_Impares}')
    
print (f'-' * 20)

def Ejercicio9(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Mult = []
        
        for elemento in Lista:
            Lista_Mult.append(elemento * 2)
            
        return Lista_Mult

Sample9 = Ejercicio9(Lista_Ejemplo1)

if (Sample9 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Ejemplo1}')
    print (f'Lista Multiplicada: {Sample9}')
    
print (f'-' * 20)

'''Lista_Promedios = list([])

Contador = 0

while (Contador < 3):
    while True:
        Numerito3 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito4 = float(Numerito3)
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
    
Promedio1 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas ingresadas es {round(Promedio1, 2)}')'''

Lista_Ejemplo2 = list([5, -6, 0, -1, -3, 0])

def Ejercicio10(Lista):
    Negativo = 0
    Positivo = 0
    Ceros = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Positivo += 1
        elif (elemento < 0):
            Negativo += 1
        else:
            Ceros += 1
            
    return Positivo, Negativo, Ceros

Sample10 = Ejercicio10(Lista_Ejemplo2)

if (len(Lista_Ejemplo2) == 0):
    print (f'Error, la lista esta vacia')
else:
    Num_Positivos, Num_Negativos, Num_Ceros = Sample10
    
    print (f'Total Numeros Positivos: {Num_Positivos}')
    print (f'Total Numeros Negativos: {Num_Negativos}')
    print (f'Total Numeros Ceros: {Num_Ceros}')
    
print (f'-' * 20)

Lista_Ejemplo3 = [
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
]

def Ejercicio11(Lista):
    Lista_Validos = []
    Lista_Invalidos = list([])
    
    import re
    
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

Sample11 = Ejercicio11(Lista_Ejemplo3)

if (Sample11 is None):
    print (f'Error, la lista esta vacia')
else:
    Lista_Correos_Validos, Lista_Correos_InValidos = Sample11
    
    print (f'Lista de correos validos: {Lista_Correos_Validos}')
    print (f'Lista de correos invalidos: {Lista_Correos_InValidos}')
    
print (f'-' * 20)

def Ejercicio12(Lista):
    Temporal1 = Lista[0]
    
    for elemento in Lista:
        if (elemento > Temporal1):
            Temporal1 = elemento
        else:
            continue
        
    return Temporal1

Sample12 = Ejercicio12(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero mayor de la lista es {Sample12}')
    
print (f'-' * 20)

def Ejercicio13(Lista):
    Temporal1 = Lista[0]
    
    for elemento in Lista:
        if (elemento < Temporal1):
            Temporal1 = elemento
        else:
            continue
        
    return Temporal1

Sample13 = Ejercicio13(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero menor de la lista es {Sample13}')
    
print (f'-' * 20)

Lista_Ejemplo4 = list([-15.5, -8, -3.2, -1, 0, -6, 7.5, 12, 19.1, 25])

def Ejercicio14(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Positivos = 0
        Negativos = 0
        Positivos_Sum = 0
        
        for elemento in Lista:
            if (elemento > 0):
                Positivos += 1
                Positivos_Sum += elemento
            else:
                Negativos += 1
                
        return Positivos_Sum, Positivos, Negativos

Sample14 = Ejercicio14(Lista_Ejemplo4)

if (Sample14 is None):
    print (f'Error, la lista esta vacia')
else:
    Sumatoria_Positivos, Num_Positivos2, Num_Negativos2 = Sample14
    
    print (f'Total Positivos: {Num_Positivos2}')
    print (f'Total Negativos: {Num_Negativos2}')
    print (f'Sumatoria Positivos: {Sumatoria_Positivos}')
    
print (f'-' * 20)

Lista_Ejemplo5 = [65, 70, 54, 80, 69, 66]

def Ejercicio15(Lista):
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

Sample15 = Ejercicio15(Lista_Ejemplo5)

if (len(Lista_Ejemplo5) == 0):
    print (f'Error, la lista esta vacia')
else:
    Sumatoria_Aprobados, Aprobados, Reprobados = Sample15
    
    print (f'Sumatoria de los aprobados: {Sumatoria_Aprobados}')
    print (f'Aprobados: {Aprobados}')
    print (f'Reprobados: {Reprobados}')
    
print (f'-' * 20)

Lista_Ejemplo6 = [15, 0, 8, 2, 0, 25, 4]

def Ejericicio16(Lista):
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

Sample16 = Ejericicio16(Lista_Ejemplo6)

if (Sample16 is None):
    print (f'Error, la lista esta vacia')
else:
    Total_Agotados, Total_Stock_Bajo, Total_Stock_Alto, Stock_Bajo_Sumatoria, Stock_Alto_Sumatoria = Sample16
    
    print (f'Total Agotados: {Total_Agotados}')
    print (f'Total Stock_Bajo: {Total_Stock_Bajo}')
    print (f'Total Stock_Alto: {Total_Stock_Alto}')
    print (f'Total Stock_Bajo_Sumatoria: {Stock_Bajo_Sumatoria}')
    print (f'Total Stock_Alto_Sumatoria: {Stock_Alto_Sumatoria}')
    
print (f'-' * 20)

Lista_Ejemplo7 = [12, 8, 5, 1, 7, 3, 10]

def Ejercicio17(Lista):
    Posicion = 0
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] == 0):
            Posicion = Contador
            return Posicion
        else:
            Contador+= 1
            continue
        
    return None

Sample17 = Ejercicio17(Lista_Ejemplo7)

if (len(Lista_Ejemplo7) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample17 is None):
        print (f'No hay ningun producto agotado actualmente')
    else:
        print (f'El primer producto agotado de la lista aparece en la posicion {Sample17}')
        
print (f'-' * 20)

Lista_Ejemplo8 = list([120, 350, 80, 600, 150, 700])

def Ejercicio18(Lista, Numero):
    Posicion = 0
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] > Numero):
            Posicion = Contador
            return Posicion
        else:
            Contador += 1
            continue
        
    return None

Monto1 = 200

Sample18 = Ejercicio18(Lista_Ejemplo8, Monto1)

if (len(Lista_Ejemplo8) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample18 is None):
        print (f'No hay un numero mayor al monto {Monto1} en la lista')
    else:
        print (f'El primero numero mayor a {Monto1} de la lista aparece en la posicion {Sample18} - ({Lista_Ejemplo8[Sample18]})')
        
print (f'-' * 20)

Lista_Ejemplo9 = list([10, 1, 3, 4, 2, 5, 6])

def Ejercicio19(Lista):
    Igualdad = 0
    
    for i in range(len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                Igualdad = Lista[i]
                return Igualdad
            else:
                continue
            
    if (Igualdad == 0):
        return None
    else:
        return Igualdad

Sample19 = Ejercicio19(Lista_Ejemplo9)

if (len(Lista_Ejemplo9) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample19 is None):
        print (f'No hay numeros repetidos en la lista')
    else:
        print (f'El primer numero repetido de la lista es {Sample19}')
        
print (f'-' * 20)

def Ejercicio20(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            continue
        
    return None

Sample20 = Ejercicio20(Lista_Ejemplo9)

if (len(Lista_Ejemplo9) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample20 is None):
        print (f'No hay numeros repetidos')
    else:
        print (f'El primer numero repetido de la lista es {Sample20}')
        
print (f'-' * 20)

Lista_Ejemplo10 = [90, 89, 79, 70]

def Ejercicio21(Lista):
    
    for indice in range(0 + 1, len(Lista)):
        if (Lista[indice - 1] < Lista[indice]):
            return indice
        else:
            continue
        
    return None

Sample21 = Ejercicio21(Lista_Ejemplo10)

if (len(Lista_Ejemplo10) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample21 is None):
        print (f'No hay un numero que cumpla esta condicion')
    else:
        print (f'El primer aumento en ventas en comparacion con el dia anterior pasa en la posicion {Sample21}')
        
print (f'-' * 20)

Lista_Ejemplo11 = list([100, 97, 95, 80, 78])

def Ejercicio22(Lista, Numero):
    for elemento in range(0 + 1, len(Lista)):
        if (Lista[elemento - 1] - Lista[elemento] >= Numero):
            return Lista[elemento], elemento
        else:
            continue
        
    return None

Caida = 10

Sample22 = Ejercicio22(Lista_Ejemplo11, Caida)

if (len(Lista_Ejemplo11) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample22 is None):
        print (f'Todo en orden, no han habido caidas de temperatura en la ultima hora')
    else:
        Grados, Posicion = Sample22
        print (f'Alerta! la primer caida de temperatura de {Caida} grados sucede en la posicion {Posicion}')
        print (f'La temperatura en esa hora fue {Grados} grados')
        
print (f'-' * 20)

Lista_Ejemplo12 = [1, 4, 2, 0, 3]

def Ejercicio23(Lista):
    for elemento in range(0 + 2, len(Lista)):
        if (Lista[elemento - 2] < Lista[elemento - 1] and Lista[elemento - 1] > Lista[elemento]):
            return elemento - 1
        else:
            continue
        
    return None

Sample23 = Ejercicio23(Lista_Ejemplo12)

if (len(Lista_Ejemplo12) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample23 is None):
        print (f'Error, no hay ningun numero con estas caracteristicas')
    else:
        print (f'El pico sucede en la posicion {Sample23} y el numero es {Lista_Ejemplo12[Sample23]}')
        
print (f'-' * 20)

# Consultar valores ✅ Consultar.

Capitales = {"Costa Rica": "San José", "México": "Ciudad de México", "Argentina": "Buenos Aires", "Italia": "Roma", "España": "Madrid"}

Encontrado1 = Capitales.get("Italia")

if (Encontrado1 is None):
    print (f'Error, Italia no esta en el diccionario')
else:
    print (f'La capital de Italia es {Encontrado1}')
    
print (f'-' * 20)

Productos1 = {"Laptop": 1200, "Mouse": 25, "Teclado": 45, "Monitor": 300}

def Ejercicio24(Diccionario, Articulo):
    Encontrado = Diccionario.get(Articulo)
    if (Encontrado is None):
        return False
    else:
        return Diccionario[Articulo]

Item1 = 'Mouse'

Sample24 = Ejercicio24(Productos1, Item1)

if (len(Productos1) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample24 == False):
        print (f'El producto {Item1} no fue encontrado')
    else:
        print (f'El producto {Item1} fue encontrado')
        print (f'El precio del producto es ${Sample24}')
        
print (f'-' * 20)

# Actualizar elementos ✅ Actualizar.

Productos2 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300
}

def Ejercicio25(Diccionario, Articulo, Precio):
    Encontrado = Diccionario.get(Articulo)
    
    if (Encontrado is None):
        return False
    else:
        Diccionario[Articulo] = Precio
        return True

Item2 = 'Escoba'
Item2_Precio = 55

Sample25 = Ejercicio25(Productos2, Item2, Item2_Precio)

if (len(Productos2) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample25 == True):
        print (f'Listo! el precio del articulo {Item2} fue actualizado a ${Item2_Precio}')
    else:
        print (f'Error el articulo no esta incluido en el diccionario')
        
print (f'-' * 20)

# Agregar elementos ✅ Agregar.

Productos3 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

Item3 = 'Teclado'
Item3_Precio = 15

def Ejercicio26(Diccionario, Articulo, Precio):
    Encontrado = Diccionario.get(Articulo)
    
    if (Encontrado is None):
        Diccionario[Articulo] = Precio
        return True
    else:
        return False

Sample26 = Ejercicio26(Productos3, Item3, Item3_Precio)

if (len(Productos3) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample26 == True):
        print (f'El producto no estaba en el diccionario, {Item3} fue agregado exitosamente')
    else:
        print (f'Error! no se pudo ingresar un producto existente')
        
print (f'-' * 20)

Productos4 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

# Eliminar elementos ✅ Eliminar.

def Ejercicio27(Diccionario, Articulo):
    Encontrado = Diccionario.get(Articulo)
    
    if (Encontrado is None):
        return False
    else:
        Diccionario.pop(Articulo)
        return True

Item4 = 'Mouse'

Sample27 = Ejercicio27(Productos4, Item4)

if (len(Productos4) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample27 == False):
        print (f'Error, el articulo {Item4} no existe')
    else:
        print (f'Listo! el producto {Item4} fue eliminado exitosamente!')
        
print (f'-' * 20)

Productos5 = {
    "Laptop": 90,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio28(Diccionario):
    Clave = next(iter(Diccionario))
    Valor = Diccionario[Clave]
    
    for indice, elemento in Diccionario.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    return Clave, Valor

Sample28 = Ejercicio28(Productos5)

if (len(Productos5) == 0):
    print (f'Error, el diccionario esta vacio')
else:
        Clave, Valor = Sample28
        print (f'Producto {Clave}')
        print (f'Precio ${Valor}')
        
print (f'-' * 20)

Lista_Eliminable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Contador = 0

while (Contador < len(Lista_Eliminable)):
    print(f'Eliminando {Lista_Eliminable[Contador]}')
    del Lista_Eliminable[Contador]
    print(f'La lista ahora tiene {len(Lista_Eliminable)} elementos')
    
print (f'-' * 20)

print (f'La lista tiene {len(Lista_Eliminable)} elementos')

'''def Ejercicio29(Numero):
    Resultado = Numero * 2 + 15
    return Resultado

Sample29 = Ejercicio29(PEPE.Flotante1)

print (f'El resultado de la operacion es {Sample29}')

print (f'-' * 20)

Resultado = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado}')

def Ejercicio30(Texto):
    Cadena = Texto.replace(' ', '')
    if (isinstance(Cadena, (str))):
        if (Cadena.isalpha()):
            print (f'Lo que ingresaste es una cadena de texto')
        else:
            print (f'Error, lo que ingresaste no es un texto')

Sample30 = Ejercicio30(PEPE.Flotante3)'''

print (f'-' * 20)

'''def Ejercicio31(Cadena):
    Lista_Cadena = Cadena.split(' ')
    
    for elemento in Lista_Cadena:
        print (f'{elemento}')
        
    print (f'La cantidad de elementos de la cadena es {len(Lista_Cadena)}')

Sample31 = Ejercicio31(PEPE.Flotante4)'''

'''Lista_Estudiantes = []

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del estudiante {elemento + 1}: ')
        Lista.append(Alumno)
        
    return Lista

Estudiantes = Colegio(Lista_Estudiantes)

print (f'La lista de estudiantes que visitaron el colegio hoy es: {Estudiantes}')'''

'''Lista_Estudiantes = []

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del estudiante {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del estudiante {elemento + 1}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda Num : Num[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes es {Menore} y su edad es {Lista[0][1]} añitos')
    print (f'El mayor de los estudiantes es {Mayore} y su edad es {Lista[-1][1]} años')

Colegio(Lista_Estudiantes)'''

class Persona():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto1 = Persona("Erick Perez")

print (f'Mi nombre es {Objeto1}')

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

print (f'Lista de colores: {Lista_Colores}')

print (f'-' * 20)

class Inventario():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto2 = Inventario()

Objeto2.Productos.append('Camiseta')
Objeto2.Productos.insert(1, 'Pantalon')
Objeto2.Productos.extend(['Calcetin'])

print (f'La lista tiene {len(Objeto2)} elementos')

print (f'-' * 20)

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
    print (f'Error, los objetos no son iguales')
    
print (f'-' * 20)

class Caja():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto5 = Caja(5)
Objeto6 = Caja(3)

print (f'La sumatoria de los objetos es {Objeto5 + Objeto6}')

print (f'-' * 20)

class Armario():
    def __init__(self):
        self.Ropa = [
            'Camiseta',
            'Abrigo',
            'Zapatos'
        ]
        
    def __getitem__(self, Indice):
        return self.Ropa[Indice]
        
Objeto7 = Armario()

print (f'El elemento 0 es {Objeto7[0]}')
print (f'El elemento 1 es {Objeto7[1]}')
print (f'El elemento 2 es {Objeto7[2]}')

print (f'-' * 20)

class Panaderia():
    def __init__(self):
        self.Panes = [
            'Baguette',
            'Croissant',
            'Rosquilla'
        ]
        
    def __iter__(self):
        return iter(self.Panes)
        
Objeto8 = Panaderia()

for elemento in Objeto8:
    print (f'El elemento es {elemento}')
    
print (f'-' * 20)

'''import requests

Diccionario_API = dict({'Nombre' : ["Pistacho", "Caramelo", "Chocomenta"], 'Posicion' : [0, 0, 0]})

Segunda1 = requests.post(f'http://127.0.0.1:8000/grupo7/', json=(Diccionario_API))
Segunda2 = Segunda1.json()

print (f'Elemento agregado: {Segunda2["Agregado"]}')

print (f'-' * 20)

Tercera1 = requests.put('http://127.0.0.1:8000/grupo7/', json=(Diccionario_API))
Tercera2 = Tercera1.json()

print (f'Elemento Reemplazado: {Tercera2["Reemplazado"]}')

print (f'-' * 20)

Cuarta1 = requests.delete('http://127.0.0.1:8000/grupo7/', json=(Diccionario_API))
Cuarta2 = Cuarta1.json()

print (f'Elemento eliminado: {Cuarta2["Eliminado"]}')

print (f'-' * 20)

Primera1 = requests.get('http://127.0.0.1:8000/grupo7/')
Primera2 = Primera1.json()

print (f'Lista de Helados: {Primera2["Helados"]}')

Lista_API = ['Pastelito']

Primera3 = requests.post('http://127.0.0.1:8000/grupo7/unidad2/', json=(Lista_API))
Primera4 = Primera3.json()

print (f'{Primera4}')'''

var1 = '3'

if (isinstance(var1, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error de formato')
    
if (var1.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error de formato')
    
try:
    Numerito3 = float(var1)
    if (Numerito3.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var2 = 3.5

if (isinstance(var2, (float))):
    print (f'Lo que ingresaste es un numero flotante')
else:
    print (f'Error de formato, esto no es un numero flotante')
    
try:
    Numerito4 = float(var2)
    if (Numerito4.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var3 = 3

if (isinstance(var3, (int, float))):
    print (f'El numero puede ser entero o decimal')
else:
    print (f'Error, de formato')
    
try:
    Numerito5 = float(var3)
    if (Numerito5.is_integer()):
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
    print (f'Error, la fecha tiene el formato incorrecto')
    exit()
    
Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Ubicada1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()]

if (Ubicada1.empty):
    print (f'No hay ventas registradas en esta fecha')
else:
    print (f'Genial! se han encontrado ventas en esta fecha')
    
    Grupo1 = Ubicada1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'En la fecha {Fech1_Formateada}, el producto que menos vendio fue {Grupo1_Min} con un total de unidades {Grupo1_Min_Cant}')
    print (f'En la fecha {Fech1_Formateada}, el producto que mas vendio fue {Grupo1_Max} con un total de unidades {Grupo1_Max_Cant}')
    
    print (f'Cantidad de clientes que compraron {Grupo1.count()}')
    
    print (f'Total de productos vendidos en esta fecha {Grupo1.sum()}')
    
    Grupo2 = Ubicada1.groupby('product')['TOTALITO'].sum()
    
    print (f'Total de dinero vendido en esta fecha ${Grupo2.sum()}')
    
    Promedio1 = Grupo2.sum() / Grupo1.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Promedio1, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue ${Grupo2.mean()}')
    
print (f'-' * 20)

SetA = {1, 2, 3, 4, 5}
SetB = {4, 5}
SetC = set({8})

print (f'{SetA.issuperset(SetB)}')
print (f'{SetA >= SetB}')

print (f'-' * 20)

print (f'{SetB.issubset(SetA)}')
print (f'{SetB <= SetA}')

print (f'-' * 20)

print (f'{SetA.isdisjoint(SetC)}')

print (f'-' * 20)

SetD = {1, 2, 3, 4}
SetE = set({3, 4, 5, 6})

print (f'{SetD.union(SetE)}')
print (f'{SetD | SetE}')

print (f'-' * 20)

print (f'{SetD.intersection(SetE)}')
print (f'{SetD & SetE}')

print (f'-' * 20)

print (f'{SetD.difference(SetE)}')
print (f'{SetD - SetE}')

print (f'-' * 20)

print (f'{SetE.difference(SetD)}')
print (f'{SetE - SetD}')

print (f'-' * 20)

print (f'{SetD.symmetric_difference(SetE)}')
print (f'{SetD ^ SetE}')

print (f'-' * 20)

'''SetD.update(SetE)

print (f'{SetD}')'''

'''SetD.intersection_update(SetE)

print (f'{SetD}')'''

'''SetD.difference_update(SetE)

print (f'{SetD}')'''

'''SetE.difference_update(SetD)

print (f'{SetE}')'''

SetD.symmetric_difference_update(SetE)

print (f'{SetD}')

print (f'-' * 20)

Set_Conjunto1 = {'Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde'}
Set_Conjunto1.add('Azul')

print (f'{Set_Conjunto1}')

Set_Conjunto2 = {'Negro'}

Set_Conjunto1.update(Set_Conjunto2)

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Red', 'Blue', 'Green'})

print (f'{Set_Conjunto1}')

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
    
class Pastel():
    def __init__(self):
        self.Favorito = Chocolate()
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Objeto9 = Pastel()

Objeto9.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Ingrediente1 = Chocolate()
Objeto10 = Pastel2(Ingrediente1)
Objeto10.Hornear()

Ingrediente2 = Vainilla()
Objeto11 = Pastel2(Ingrediente2)
Objeto11.Hornear()

Ingrediente3 = Fresa()
Objeto12 = Pastel2(Ingrediente3)
Objeto12.Hornear()

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
    print (f'El correo en la posicion {indice} es {elemento}')
    
print (f'-' * 20)

import re

Texto3 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Metodo1

Pattern2 = r'\!|\?|\.{2,}|\d{4,}\-[0-9]{1,4}'

Buscar2 = re.sub(Pattern2, '', Texto3)

print (f'{Buscar2}')

print (f'-' * 20)

# Metodo2

Texto4 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern3 = r'[^a-zA-Z0-9{3}\s]+'

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

Texto5_temp1 = Texto5

Pattern4 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos1 = re.findall(Pattern4, Texto5)

print (f'{Correos1}')

for i, email in enumerate(Correos1, start=1):
    Texto5_temp1 = Texto5_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto5_temp1}')

Pattern5 = r'\!|\?'

Texto5_temp2 = re.sub(Pattern5, '', Texto5_temp1)

print (f'{Texto5_temp2}')

for i, email in enumerate(Correos1, start=1):
    Texto5_temp2 = Texto5_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto5_temp2}')

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
        Numerito6 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito7 = float(Numerito6)
            if (Numerito7.is_integer()):
                print (f'La nota ingresada es un numero entero')
                Lista_Promedios.append(Numerito7)
                break
            else:
                print (f'La nota ingresada es un numero decimal')
                Lista_Promedios.extend([Numerito7])
                break
        except ValueError:
            print (f'Error, lo ingresado no es un numero')
    Contador += 1
    
Promedio2 = sum(Lista_Promedios) / Lista_Promedios.__len__()

print (f'El promedio de las notas ingresadas es {round(Promedio2, 2)}')
    
print (f'-' * 20)'''

from Module_Own import Pokemon1 as Poke1

Objeto13 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto14 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto13.Mostrar()

print (f'-' * 20)

Objeto14.Mostrar()

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto14 = Poke_Kid1(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto14)
Objeto14.Mostrar()

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
        
Objeto15 = Perro('Chester', 5, 2.8, 'Poodle', 'Asma de perro')

Veterinaria.Mostrar(Objeto15)
Objeto15.Mostrar()

print (f'-' * 20)

class Gato(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto16 = Gato('Messi', 1.5, 2, 'Gris', 'No')

Veterinaria.Mostrar(Objeto16)
Objeto16.Mostrar()

print (f'-' * 20)

class Pajaro(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto17 = Pajaro('Polly', 31, 0.4, 'Guacamaya', 'Si')

Veterinaria.Mostrar(Objeto17)
Objeto17.Mostrar()

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
        
Objeto18 = Paladin(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto18.Mostrar()
Atacante.Mostrar(Objeto18)
Defensor.Mostrar(Objeto18)

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
        
Objeto19 = D1()

A1.Mostrar(Objeto19)
B1.Mostrar(Objeto19)
C1.Mostrar(Objeto19)
Objeto19.Mostrar()
E1.Mostrar(Objeto19)

print (f'-' * 20)

class Efectivo():
    def Pagar(self):
        print (f'El pago se realizo en Efectivo')
        
class Tarjeta():
    def Pagar(self):
        print (f'El pago se realizo en Tarjeta')
        
class Cripto():
    def Pagar(self):
        print (f'El pago se realizo en Crito')
        
Objeto20 = Efectivo()
Objeto20.Pagar()

Objeto21 = Tarjeta()
Objeto21.Pagar()

Objeto22 = Cripto()
Objeto22.Pagar()

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
        
Objeto21 = Cuenta_Bancaria(100)
Objeto21.Depositar(25)
Objeto21.Mostrar()

print (f'Tu saldo privado que no deberia compartirse es {Objeto21.Dinero}')

Objeto21.Dinero = '50,000,000'

Objeto21.Mostrar()

print (f'Tu saldo privado que no deberia compartirse es {Objeto21.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def General(self):
        pass
    
class Sub_Plantilla(Plantilla):
    def Mostrar(self):
        print (f'Este metodo le pertenece al sub plantilla')
        
    def General(self):
        print (f'Esto es el encapsulamiento')
        
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
        print (f'El contrincante eligio un {self.Favorito.Elegir()} para la batalla')
        
Objeto23 = Battle1()

Objeto23.Batallar()

print (f'-' * 20)

class Battle2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El contrincante eligio un {self.Favorito.Elegir()} para la batalla')
        
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

import re

Texto6 = 'esto 12 no es un hola ejemplo coherente 7 pero lo hula mas baImportabnte es ver si 645 ! esto sirve hela o no'

Buscar4 = re.search(r'importante', Texto6)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\d+', Texto6)

print (f'{Buscar5}')

Buscar6 = re.fullmatch(r'esto 12 no es un hola ejemplo coherente 7 pero lo hula mas baImportabnte es ver si 645 \! esto sirve hela o no', Texto6)

print (f'{Buscar6}')

Buscar7 = re.findall(r'h.la', Texto6)

print (f'{Buscar7}')

Buscar8 = re.findall(r'[A-Z]+', Texto6)

print (f'{Buscar8}')

Buscar9 = re.findall(r'[A-Z]{1}[a-z]+', Texto6)

print (f'{Buscar9}')

Buscar10 = re.findall(r'^(esto)', Texto6)

print (f'{Buscar10}')

Buscar11 = re.findall(r'(o)$', Texto6)

print (f'{Buscar11}')

Buscar12 = re.findall(r'\d+\s\W', Texto6)

print (f'{Buscar12}')

'''
{2}
{2,}
{2,5}
\d
\D
\s
\S
\w
\W
?
*
+
'''

Buscar13 = re.findall(r'([ab]{2,})', Texto6)

print (f'{Buscar13}')

Buscar14 = re.findall(r'(\d{2,4}|hola)', Texto6)

print (f'{Buscar14}')

print (f'-' * 20)

Texto7 = 'ericksuper80@gmail.com'

# Version1

Pattern6 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.[a-z]{2,}'

Buscar15 = bool(re.match(Pattern6, Texto7))

if (Buscar15 == True):
    print (f'El correo electronico tiene el formato correcto')
else:
    print (f'Error, el correo tiene un formato incorrecto')

# Version2

Texto8 = 'ericksuper80@gmail.com'

Pattern7 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)$'

Buscar16 = bool(re.fullmatch(Pattern7, Texto8))

if (Buscar16 == True):
    print (f'El correo 2 tiene el formato valido')
else:
    print (f'Error, formato de correo 2 incorrecto')
    
print (f'-' * 20)

Texto9 = '32'

Pattern8 = r'([0[0-9]|[12][0-9]|3[01])'

Buscar17 = bool(re.fullmatch(Pattern8, Texto9))

if (Buscar17 == True):
    print (f'El numero se encuentra entre 01 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

Texto10 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern9 = r'\d{2}\/[0-9]{2,4}\/\d{3,}'

Replacement9 = 'XX/XX/XXXX'

Buscar18 = re.sub(Pattern9, Replacement9, Texto10)

print (f'{Buscar18}')

Pattern10 = r'\+\d{1}\-[0-9]{2,3}\-\d{3,}\-[0-9]{4,}'

Replacement10 = 'PHON3_NUMB3R'

Buscar19 = re.sub(Pattern10, Replacement10, Buscar18)

print (f'{Buscar19}')

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

Buscar20 = re.findall(Pattern11, Texto11)

print (f'{Buscar20}')

for indice, elemento in enumerate(Buscar20, start=1):
    print (f'Indice: {indice} -- Correo Electronico: {elemento}')
    
print (f'-' * 20)

Texto12 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Version1

Pattern12 = r'\!|\?|\.{2,}|\d{2,4}\-[0-9]{4}'

Buscar21 = re.sub(Pattern12, '', Texto12)

print (f'{Buscar21}')

print (f'-' * 20)

# Version2

Texto13 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern13 = r'[^a-zA-Z0-9\s]+'

Buscar22 = re.sub(Pattern13, '', Texto13)

print (f'{Buscar22}')

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

Exception1('3.5')

print (f'-' * 20)

def Exception2(Numero):
    try:
        Numerito = float(Numero)
        if (Numerito.is_integer()):
            print (f'Lo que ingresaste es un numero entero')
        else:
            print (f'Lo que ingresaste es un numero decimal')
    except ValueError:
        print (f'Error, lo que ingresaste no es un numero')

Exception2('3')

print (f'-' * 20)

import re

Texto14 = "   Hola!!!   mundo@@   123   "

print (f'{Texto14}')

Texto14_Version1 = Texto14.strip()

print (f'{Texto14_Version1}')

Texto14_Version2 = ' '.join(Texto14_Version1.split())

print (f'{Texto14_Version2}')

Texto14_Version3 = Texto14_Version2.lower()

print (f'{Texto14_Version3}')

Texto14_Version4 = re.sub(r'\!|\@|\d+', '', Texto14_Version3)

print (f'{Texto14_Version4}')

print (f'-' * 20)

def Exception3(Numero):
    try:
        Numerito = float(Numero)
        if (Numerito.is_integer()):
            print (f'Lo que ingresaste es un numero entero')
        else:
            print (f'Lo que ingresaste es un numero decimal')
    except ValueError:
        print (f'Error, lo que ingresaste no es un numero')

Exception3('3')

print (f'-' * 20)

def Exception4(Num1, Num2):
    try:
        Suma = Num1 + Num2
        print (f'El resultado de la suma es {Suma}')
    except (TypeError, ValueError):
        print (f'Error, ambos elementos deben ser numeros')

Exception4(14, 'Hola')

print (f'-' * 20)

def Exception5(Num1, Num2):
    try:
        Divi = Num1 / Num2
        
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser un cero')

Exception5(12, 0)

print (f'-' * 20)

Lista_Exception6 = list([
    'Erick',
    'Josue',
    'Karlita'
])

def Exception6(Indice):
    try:
        print (f'El elemento en la posicion {Indice} es {Lista_Exception6[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception6(3)

print (f'-' * 20)

Diccionario_Exception7 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception7(Clave):
    try:
        print (f'El elemento en la clave {Clave} es {Diccionario_Exception7[Clave]}')
    except KeyError:
        print (f'Error, la clave esta fuera de rango')

Exception7("Votante")

print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Durazno')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo es incorrecto 404')
    
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
    Documento_Agregar = Docu.write(f'\nUvas')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nFesa Pequeña', f'\nFesa Mediana', f'\nFesa Grande'])
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

print (f'{Data_Frame_Concatenate_Age}')

print (f'-' * 20)

print (f'El menor de los numeros es {Data_Frame_Concatenate_Age.min()}')
print (f'El mayor de los numeros es {Data_Frame_Concatenate_Age.max()}')

print (f'-' * 20)

print (f'El menor de los numeros es {Data_Frame_Concatenate_Age.idxmin()}')
print (f'El mayor de los numeros es {Data_Frame_Concatenate_Age.idxmax()}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')["Edad"].sum()
Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()
Grupo3_Min_Cant = Grupo3.min()
Grupo3_Max_Cant = Grupo3.max()

print (f'La persona menor de la lista es {Grupo3_Min} y su edad es {Grupo3_Min_Cant} años')
print (f'La persona mayor de la lista es {Grupo3_Max} y su edad es {Grupo3_Max_Cant} años')

print (f'La cantidad de personas en el dataframe es {Grupo3.count()}')

print (f'La suma de las edades es {Grupo3.sum()}')

print (f'La media de las edades es {round(Grupo3.mean(), 2)}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Unidad1 = elemento["Nombre"]
    Unidad2 = elemento["Edad"]
    
    print (f'Mi nombre es {Unidad1} y mi edad {Unidad2} años')
    
print (f'-' * 20)

'''import pandas as pd
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
Elemento2 = Data_Frame1.loc[1, 'Edad']
Elemento3 = Data_Frame1.loc[2, 'Votante']
Elemento4 = Data_Frame1.loc[: 'Edad']
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
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col="cabina")
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col="edad", usecols="E:I")
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col="edad", usecols="E:I", nrows=1)

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

Grupo4 = Cargar_Excel3_Sorted.groupby('tres')["cinco"].sum()
Grupo4_min = Grupo4.idxmin()
Grupo4_max = Grupo4.idxmax()
Grupo4_min_Cant = Grupo4.min()
Grupo4_max_Cant = Grupo4.max()

print (f'El estudiante menor es {Grupo4_min} y su edad es {Grupo4_min_Cant} años')
print (f'El estudiante mayor es {Grupo4_max} y su edad es {Grupo4_max_Cant} años')

print (f'Total de personas en el dataframe {Grupo4.count()}')

print (f'Total de la suma de las edades es {Grupo4.sum()}')

print (f'La media de la suma de las edades es {Grupo4.mean()}')

print (f'-' * 20)

Lista_Cargar_Excel = list(Cargar_Excel3_Sorted['tres'])

Key1 = [f'Key{i}' for i in range(len(Lista_Cargar_Excel))]

print (f'{Lista_Cargar_Excel}')
print (f'{Key1}')

Diccionario_Cargar_Excel = dict(zip(Key1, Lista_Cargar_Excel))

for elemento in Diccionario_Cargar_Excel:
    print (f'{Diccionario_Cargar_Excel[elemento]}')
    
print (f'-' * 20)

for elemento in Diccionario_Cargar_Excel.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario_Cargar_Excel.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario_Cargar_Excel.items():
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

print (f'{Diccionario_Cargar_Excel}')
print (f'{Diccionario_Cargar_Excel.keys()}')
print (f'{Diccionario_Cargar_Excel.values()}')
print (f'{Diccionario_Cargar_Excel.items()}')
print (f'{Diccionario_Cargar_Excel["Key0"]}')
print (f'{Diccionario_Cargar_Excel.get("Key1")}')

print (f'-' * 20)

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt}')

print (f'-' * 20)

print (f'{Cargar_Txt.head()}')

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

print (f'{Array0[1][::2]}')
print (f'{Array0[0][::3]}')
print (f'{Array0[2][:2]}')
print (f'{Array0[2][2:]}')
print (f'{Array0[1][2:3]}')
print (f'{Array0[:][1]}')
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

print (f'{Array2[1, ::2]}')
print (f'{Array2[0, ::3]}')
print (f'{Array2[0, :2]}')
print (f'{Array2[0, 2:]}')
print (f'{Array2[:, 0]}')
print (f'{Array2[1, 2:3]}')
print (f'{Array2[1, 0:None]}')
print (f'{Array2[1, :]}')
print (f'{Array2[Array2 >= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[1, 0:None])
Sumita4 = np.sum(Array2_Sorted[1, :])

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

print (f'-' * 20)

print (f'Sumita: {Sumita1}')
print (f'Sumita: {Sumita2}')
print (f'Sumita: {Sumita3}')
print (f'Sumita: {Sumita4}')

print (f'-' * 20)

Array3 = np.array([[['e', 'f', 'k'], ['o', 'm', 'h']],      [['s', 'x', 'r'], ['l', 'u', 'n']]])

print (f'{Array3}')
print (f'{Array3.ndim}') # 3
print (f'{Array3.shape}') # 2x2x3
print (f'{Array3.size}') # 12
print (f'{Array3.dtype}') # <U1
print (f'{Array3[1, 0, 2]}')

print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[0, 1, 2:3]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[1, 1, 0:None]}')
print (f'{Array3[1, 1, :]}')
print (f'{Array3[Array3 == "l"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],         [[[6, 5, 4], [9, 8, 7]], [[0, 4, 9], [3, 8, 7]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 1, 1]}')

print (f'{Array4}[1, 0, 0, ::2]')
print (f'{Array4}[1, 1, 0, ::3]')
print (f'{Array4}[0, 1, 1, :2]')
print (f'{Array4}[0, 1, 1, 2:]')
print (f'{Array4}[0, 1, :, 2]')
print (f'{Array4}[1, 0, 1, 2:3]')
print (f'{Array4}[0, 0, 0, 0:None]')
print (f'{Array4}[0, 0, 0, :]')
print (f'{Array4[Array4 >= 2]}')

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

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[1, 0]}')

print (f'{Array_Zeros[1, ::2]}')
print (f'{Array_Zeros[0, ::3]}')
print (f'{Array_Zeros[0, :2]}')
print (f'{Array_Zeros[0, 2:]}')
print (f'{Array_Zeros[:, 2]}')
print (f'{Array_Zeros[1, 2:3]}')
print (f'{Array_Zeros[0, 0:None]}')
print (f'{Array_Zeros[0, :]}')
print (f'{Array_Zeros[Array_Zeros == 0]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 1]}')

print (f'{Array_Ones[0, ::2]}')
print (f'{Array_Ones[1, ::3]}')
print (f'{Array_Ones[0, :2]}')
print (f'{Array_Ones[0, 2:]}')
print (f'{Array_Ones[:, 1]}')
print (f'{Array_Ones[1, 2:3]}')
print (f'{Array_Ones[1, 0:None]}')
print (f'{Array_Ones[1, :]}')
print (f'{Array_Ones[Array_Ones == 1]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value=f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 2]}')

print (f'{Array_Gen1[1, ::2]}')
print (f'{Array_Gen1[0, ::3]}')
print (f'{Array_Gen1[1, :2]}')
print (f'{Array_Gen1[1, 2:]}')
print (f'{Array_Gen1[:, 2]}')
print (f'{Array_Gen1[1, 2:3]}')
print (f'{Array_Gen1[0, 0:None]}')
print (f'{Array_Gen1[0, :]}')
print (f'{Array_Gen1[Array_Gen1 == "Pikachu"]}')

print (f'-' * 20)

Lista_Array1 = []

Array_Gen2 = np.full(shape=(5), fill_value=f'Fuecoco')

print (f'{Array_Gen2}')
print (f'{type(Array_Gen2)}')

for elemento in Array_Gen2:
    Lista_Array1.append(str(elemento))
   
print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value=Array4[0, 1, 1, 2:3])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[0, 1]}')

print (f'{Array_Gen3[1, ::2]}')
print (f'{Array_Gen3[0, ::3]}')
print (f'{Array_Gen3[0, :2]}')
print (f'{Array_Gen3[0, 2:]}')
print (f'{Array_Gen3[:, 2]}')
print (f'{Array_Gen3[1, 2:3]}')
print (f'{Array_Gen3[1, 0:None]}')
print (f'{Array_Gen3[1, :]}')
print (f'{Array_Gen3[Array_Gen3 == 1]}')

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
print (f'{Array_Gen4[1, 1]}')

print (f'-' * 20)

print (f'{Array_Gen5}')
print (f'{Array_Gen5.ndim}')
print (f'{Array_Gen5.shape}')
print (f'{Array_Gen5.size}')
print (f'{Array_Gen5.dtype}')
print (f'{Array_Gen5[0, 0]}')

print (f'-' * 20)

print (f'{Array_Gen6}')
print (f'{Array_Gen6.ndim}')
print (f'{Array_Gen6.shape}')
print (f'{Array_Gen6.size}')
print (f'{Array_Gen6.dtype}')
print (f'{Array_Gen6[0, 0]}')

print (f'-' * 20)

print (f'{Array_Gen6[3]}')

print (f'-' * 20)

Array_Num3 = np.arange(start=1, stop=6, step=1) #type:ignore
Array_Num4 = np.arange(start=2, stop=11, step=2) #type:ignore
Array_Num5 = np.arange(start=3, stop=31, step=3) #type:ignore
Array_Num6 = np.arange(start=10, stop=21, step=2) #type:ignore
Array_Num7 = np.arange(10) #type:ignore

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

print (f'-' * 20)

Array_Random2_Sorted = np.sort(Array_Random2)

print (f'{Array_Random2_Sorted}')

Array_Random2_Sorted_Mean = np.mean(Array_Random2_Sorted)

Array_Random2_Sorted_Sum = np.sum(Array_Random2_Sorted)

print (f'{Array_Random2_Sorted_Mean}')

print (f'{Array_Random2_Sorted_Sum}')

print (f'-' * 20)

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Suma = Arr1 + Arr2
Resta = Arr1 - Arr2
Multiplicacion = Arr1 * Arr2
Division = Arr1 // Arr2

print (f'El resultado de la operacion es {Suma}')
print (f'El resultado de la operacion es {Resta}')
print (f'El resultado de la operacion es {Multiplicacion}')
print (f'El resultado de la operacion es {Division}')

Array_Random1_Cien = Array_Random1 * 100

print (f'{Array_Random1_Cien}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(20))

print (f'{Array_Random3}')

Array_Random3_Reshape = np.reshape(Array_Random3, shape=(4, 5))

print (f'{Array_Random3_Reshape}')

Array_Random3_Reshape_Ravel = np.ravel(Array_Random3_Reshape)

print (f'{Array_Random3_Reshape_Ravel}')

print (f'-' * 20)

Lista_Array2 = ['Erick', 'Josue', 'Karlita']

print (f'{Lista_Array2}')

Array5 = np.array(Lista_Array2)

print (f'{Array5}')

print (f'-' * 20)

Array6 = np.array([1, 2, 3])
Array7 = np.arange(start=4, stop=7, step=1) #type: ignore

Array_Concatenate = np.concatenate([Array6, Array7])

print (f'{Array_Concatenate}')

print (f'-' * 20)

Array_Concatenate_Splited1 = np.split(Array_Concatenate, 1)
Array_Concatenate_Splited2 = np.split(Array_Concatenate, 2)
Array_Concatenate_Splited3 = np.split(Array_Concatenate, 3)
Array_Concatenate_Splited4 = np.split(Array_Concatenate, 6)

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

Array_Random4 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random4}')

print (f'-' * 20)

Array_Random4_Columna_Min = np.min(Array_Random4, axis=0)
Array_Random4_Columna_Max = np.max(Array_Random4, axis=0)
Array_Random4_Fila_Min = np.min(Array_Random4, axis=1)
Array_Random4_Fila_Max = np.max(Array_Random4, axis=1)

print (f'Los menores de las columnas son {Array_Random4_Columna_Min}')
print (f'Los menores de las columnas son {Array_Random4_Columna_Max}')
print (f'Los menores de las columnas son {Array_Random4_Fila_Min}')
print (f'Los menores de las columnas son {Array_Random4_Fila_Max}')

print (f'-' * 20)

Set_Conjunto_Sorteo1 = {'Erick', 'Josue'}
Set_Conjunto_Sorteo1.add('Karlita')

Set_Conjunto_Sorteo2 = set({'Carmelo', 'Susanita', 'Roxana'})

Set_Conjunto_Sorteo1.symmetric_difference_update(Set_Conjunto_Sorteo2)

print (f'{Set_Conjunto_Sorteo1}')

Lista_Sorteo = list(Set_Conjunto_Sorteo1)

Ganador1 = np.random.choice(Lista_Sorteo, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Sorteo, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Sorteo, size=(2, 3), replace=False)

print (f'-' * 20)

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
    print (f'Final del Experimento')
    
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
    print (f'Final del Experimento')
    
print (f'-' * 20)

def Generadora3():
    for elemento in range(5):
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
except StopIteration:
    print (f'Final del Experimento')
    
print (f'-' * 20)

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la operacion es {PEPE.Sumatoria1(12, 7)}')

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
        
    return Usuario_Interno('MASCULINO')

Variable_Usuario = Usuario_Externo()

if (Variable_Usuario == True):
    print (f'YOU ARE A MAN')
else:
    print (f'YOU ARE A WOMAN')
    
print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(22)}')
        Docu.close()
except FileNotFoundError:
    print (f'Error 404 archivo incorrecto')
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
print (f'-' * 20)
    
def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.5, 200, True)

print (f'{Variable_Funcion_Tupla}')
print (f'{Variable_Funcion_Tupla[2]}')
print (f'{Funcion_Tupla("Perro", 3.5, 200, True)[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.5, 200, True))}')

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

Funcion_Diccionario(Nombre = "Erick", Edad = 37, Votante = not True)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

if (PEPE.Any_Par == True):
    print (f'Los numeros pares de la lista son: {list(Anonima3)}')
    print (f'Los numeros pares de la lista son: {PEPE.Lista_Pares}')
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

print (f'-' * 20)

def Closure_Externo():
    Lista_Closure = list([])
    
    def Closure_Interno(x):
        Lista_Closure.append(x)
        
        return Lista_Closure
    
    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(37)}')
print (f'{Variable_Closure(66)}')

print (f'-' * 20)

def Closure_Crear_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y

    return Closure_Multiplicador

Multiplicador1 = Closure_Crear_Multiplicador(2)
Multiplicador2 = Closure_Crear_Multiplicador(3)

print (f'El multiplicador es {Multiplicador1(10)}')
print (f'El multiplicador es {Multiplicador2(10)}')

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

Filtrador(PEPE.Lista_Numeros)

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'Esto va antes >>>')
        Segunda()
        print (f'<<< Esto va despues')
        
    return Tercera

@Primera
def Saludar4():
    print (f'Hola Mundo')
    
Saludar4()

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 19
        
    return Tercera

@Primera
def Sumatoria3(Num1:int, Num2:int) -> int:
    return Num1 + Num2

print (f'El resultado de la operacion es {Sumatoria3(12, 7)}')

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

print (f'{Usuario2('Erick', 'Perez')}')

print (f'-' * 20)

from Module_Own import Pokemon2 as Poke2

Objeto27 = Poke2(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto28 = Poke2(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto27.Mostrar()

print (f'-' * 20)

Objeto28.Mostrar()

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto29 = Poke_Kid2(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto29)
Objeto29.Mostrar()

print (f'-' * 20)

class Camara():
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada')
        
class Reproductor():
    def Reproducir_Musica(self):
        print (f'La musica fue reproducida')
        
class Smartphone(Camara, Reproductor):
    def Encender_Smartphone(self):
        print (f'El smartphone fue encendido')
        
Objeto30 = Smartphone()

Objeto30.Encender_Smartphone()

Objeto30.Reproducir_Musica()

Objeto30.Tomar_Fotografia()

print (f'-' * 20)

class Empleado():
    def __init__(self, Nombre, Edad, Salario):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Salario = Salario

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad} años')
        print (f'Salario: ${self.Salario}')
        
class Programador(Empleado):
    def __init__(self, Nombre, Edad, Salario, Lenguaje):
        super().__init__(Nombre, Edad, Salario)
        self.Lenguaje = Lenguaje
        
    def Mostrar(self):
        print (f'Lenguaje: {self.Lenguaje}')
        
Objeto31 = Programador('Erick', 37, 2000, 'Python')

Empleado.Mostrar(Objeto31)
Objeto31.Mostrar()

print (f'-' * 20)

class Disenador(Empleado):
    def __init__(self, Nombre, Edad, Salario, Herramienta):
        super().__init__(Nombre, Edad, Salario)
        self.Herramienta = Herramienta
        
    def Mostrar(self):
        print (f'Herramienta de diseño: {self.Herramienta}')
        
Objeto32 = Disenador('Karlita', 22, 1400, 'Adobe Photoshoop')

Empleado.Mostrar(Objeto32)
Objeto32.Mostrar()

print (f'-' * 20)

class Contador(Empleado):
    def __init__(self, Nombre, Edad, Salario, Especialidad):
        super().__init__(Nombre, Edad, Salario)
        self.Especialidad = Especialidad
        
    def Mostrar(self):
        print (f'Especialidad: {self.Especialidad}')
        
Objeto33 = Contador('Carmelo', 66, 3000, 'Contador Publico')

Empleado.Mostrar(Objeto33)
Objeto33.Mostrar()

print (f'-' * 20)

class Nadador():
    def __init__(self, Velocidad_Nado):
        self.Velocidad_Nado = Velocidad_Nado
        
    def Nadar(self):
        print (f'Velocidad de nado: {self.Velocidad_Nado}km/h')
        
class Volador():
    def __init__(self, Altura_Maxima):
        self.Altura_Maxima = Altura_Maxima
        
    def Volar(self):
        print (f'Altura Maxima: {self.Altura_Maxima}mts')
        
class Pato(Nadador, Volador):
    def __init__(self, Velocidad_Nado, Altura_Maxima, Raza):
        Nadador.__init__(self, Velocidad_Nado)
        Volador.__init__(self, Altura_Maxima)
        self.Raza = Raza
        
    def Especie(self):
        print (f'La especie del pato es: {self.Raza}')
        
Objeto34 = Pato(25, 200, 'Pato Mandarin')

Objeto34.Especie()
Nadador.Nadar(Objeto34)
Volador.Volar(Objeto34)

print (f'-' * 20)

Objeto34.Especie()
Objeto34.Nadar()
Objeto34.Volar()

print (f'-' * 20)

Hija_Padre1 = issubclass(Poke_Kid2, Poke2)
Hija_Padre2 = issubclass(Poke_Kid2, Poke1)

print (f'{Hija_Padre1}')
print (f'{Hija_Padre2}')

print (f'-' * 20)

Instancia1 = isinstance(Objeto34, Pato)
Instancia2 = isinstance(Objeto34, Volador)
Instancia3 = isinstance(Objeto34, Nadador)
Instancia4 = isinstance(Objeto34, Defensor)

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
        
Objeto35 = D2()

A2.Mostrar(Objeto35)
B2.Mostrar(Objeto35)
C2.Mostrar(Objeto35)
Objeto35.Mostrar()
E2.Mostrar(Objeto35)

print (f'-' * 20)

class Bicicleta():
    def Entregar(self):
        print (f'La entrega del paquete se realizara en Bicicleta')
        
class Moto():
    def Entregar(self):
        print (f'La entrega del paquete se realizara en Moto')
        
class Camion():
    def Entregar(self):
        print (f'La entrega del paquete se realizara en Camion')
        
Objeto36 = Bicicleta()
Objeto37 = Moto()
Objeto38 = Camion()

Objeto36.Entregar()
Objeto37.Entregar()
Objeto38.Entregar()

print (f'-' * 20)

class Perfil():
    def __init__(self, Nombre, Email, Contrasena):
        self.Nombre = Nombre
        self.Email = Email
        self.__Contrasena = Contrasena
    
    @property    
    def Contra(self):
        return self.__Contrasena
    
    @Contra.setter
    def Contra(self, Nueva_Contrasena):
        self.__Contrasena = Nueva_Contrasena
        
    def Mostrar(self):
        print (f'Su contrasena temporal es {self.__Contrasena}')
        
Objeto37 = Perfil('Erick', 'ericksuper80@gmail.com', 'erick123')

Objeto37.Mostrar()

print (f'Su contrasena privada que no deberias compartir es {Objeto37.Contra}')

Objeto37.Contra = 'Terry88'

Objeto37.Mostrar()

print (f'Su contrasena privada que no deberias compartir es {Objeto37.Contra}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Personaje(ABC):
    @abstractmethod
    def Atacar(self):
        pass

class Guerrero(Personaje):
    def Defender(self):
        print (f'El Guerrero defiende con escudo')
        
    def Atacar(self):
        print (f'El Guerrero ataca con espada')
        
Objeto38 = Guerrero()

Objeto38.Defender()
Objeto38.Atacar()
        
class Mago(Personaje):
    def Defender(self):
        print (f'El Mago defiende con magia')
        
    def Atacar(self):
        print (f'El Mago ataca con baston')
        
Objeto39 = Mago()

Objeto39.Defender()
Objeto39.Atacar()
        
class Arquero(Personaje):
    def Defender(self):
        print (f'El Arquero defiende con distancia')
        
    def Atacar(self):
        print (f'El Arquero ataca con arco y flecha')
        
Objeto40 = Arquero()

Objeto40.Defender()
Objeto40.Atacar()

print (f'-' * 20)

class Madera():
    def Elegir(self):
        return f'Madera'
    
class Metal():
    def Elegir(self):
        return f'Metal'
    
class Vidrio():
    def Elegir(self):
        return f'Vidrio'
    
class Manualidad():
    def __init__(self):
        self.Favorito = Madera()
        
    def Fabricar(self):
        print (f'Hoy voy a hacer una manualidad hecha con {self.Favorito.Elegir()}')
        
Objeto41 = Manualidad()

Objeto41.Fabricar()

print (f'-' * 20)

class Manualidad2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Fabricar(self):
        print (f'Hoy voy a hacer una manualidad hecha con {self.Favorito.Elegir()}')
        
Material1 = Madera()
Objeto42 = Manualidad2(Material1)
Objeto42.Fabricar()

Material2 = Metal()
Objeto43 = Manualidad2(Material2)
Objeto43.Fabricar()

Material3 = Vidrio()
Objeto44 = Manualidad2(Material3)
Objeto44.Fabricar()

print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable6 = Lista_Uno[0]
variable7 = 'Perez'
variable8 = '''Esto
Es
Un
Long
String'''

variable9 = Objeto14.Cantidad
variable10 = PEPE.Division_Flotante
variable11, variable12 = True, Objeto13.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke["Poke3"]}')

print (f'Mi nombre completo es {Lista_Uno[0]} {variable7}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Sumatoria2(1, 2, 3)}, {Anonima2(Variable_Sumatoria)} o incluso {Objeto14.Cantidad} pokemones')

del variable10

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable8)

print (f'Erick' in Lista_Uno)
print (f'Koala' in PEPE.Lista2)
print (f'Gary' not in PEPE.Tupla_Poke)
print (f'{PEPE.Diccionario_Poke["Poke2"]}' in PEPE.Set_Conjunto_Poke1)

print (f'-' * 20)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables y declaracion snake case al mismo tiempo {snake_case2}')

print (f'La lista 1 tiene un total de {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')

print (f'La lista 1 tiene un total de {len(Lista_Uno)} elementos')

print (f'-' * 20)

Cociente, Residuo = divmod(Objeto13.Cantidad, Sumatoria2(1, 2, 3, 1))

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

print (f'-' * 20)

print (f'{Lista_Uno[2]} eso que ves ahi es un {PEPE.Lista2[2]}?')

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

print (f'-' * 20)

Lista_Uno_Copia = Lista_Uno.copy()

Lista_Uno.clear()

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'-' * 20)

print (f'{dir(PEPE)}')

Tupla1 = ('Electrico', Objeto13.Tipo, Objeto13.Tipo, Objeto13.Tipo, Objeto13.Tipo, Objeto13.Tipo,)

print (f'{Tupla1}')

Tupla1 = tuple(('Rojo', 'Verde', 'Azul'))

print (f'{Tupla1}')

print (f'{Tupla1[1]}')

Tupla2 = 'Uno', 'Dos', 'Tres',

Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')

Tupla4 = ('Uno',)
Tupla5 = 'Dos',

Tupla6 = Tupla4 + Tupla5

print (f'{Tupla6}')

Set_Conjunto_Menu1 = {'Chocolate'}
Set_Conjunto_Menu2 = set({'Vainilla'})
Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)
Set_Conjunto_Menu1.add('Fresa')

print (f'{Set_Conjunto_Menu1}')

Set_Conjunto_Menu3 = frozenset({'Caramelo', 'ChocoFresa'})

print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu4 = set({Set_Conjunto_Menu3, 'Natilla'})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu3}')
print (f'{Set_Conjunto_Menu4}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu3)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : "Erick",
    'Edad' : 37,
    'Votante' : True
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

Diccionario1['Nombre'] = Saludar_Dos()

print (f'{Diccionario1}')

Diccionario1_Copia = Diccionario1.copy()

del Diccionario1['Nombre']
Variable_Dict = Diccionario1.pop('Edad')

print (f'{Diccionario1}')

print (f'El elemento eliminado es {Variable_Dict}')

Diccionario1.clear()

print (f'{Diccionario1}')
print (f'{Diccionario1_Copia}')

print (f'-' * 20)

Diccionario1 = dict({1 : "Karlita", 2 : 6, 3 : False})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario1.get(1)} no puede votar ya que solo tiene {Diccionario2["Edad"][2]} años')

Diccionario_Vacio1 = dict.fromkeys('ABC', f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]}')

Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])

Diccionario_Vacio2["Dos"] = 'Frutilla'

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

Key2 = [f'Key_{i}' for i in range(len(Lista_Uno_Copia))]

Diccionario4 = dict(zip(Key2, Lista_Uno_Copia))

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Key_2"]}')
print (f'{Diccionario4.get("Key_3")}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv2 = 'C:\\Repo\\Store.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2}')

print (f'-' * 20)

Fecha2 = '2026-04-01'

try:
    Fech2 = datetime.strptime(Fecha2, '%Y-%m-%d').date()
    Fech2_Formateada = pd.to_datetime(Fech2)
    Cargar_Csv2['date'] = pd.to_datetime(Cargar_Csv2['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato invalido')
    exit()
    
Cargar_Csv2['TOTALITO'] = Cargar_Csv2['quantity'] * Cargar_Csv2['price']
    
Ubicada2 = Cargar_Csv2[Cargar_Csv2['date'].dt.date == Fech2_Formateada.date()]

if (Ubicada2.empty):
    print (f'No hay ventas en esta fecha')
else:
    print (f'Genial! se han encontrado ventas en esta fecha')
    
    Grupo5 = Ubicada2.groupby('product')['quantity'].sum()
    Grupo5_Min = Grupo5.idxmin()
    Grupo5_Max = Grupo5.idxmax()
    Grupo5_Min_Cant = Grupo5.min()
    Grupo5_Max_Cant = Grupo5.max()
    
    print (f'En la fecha {Fech2_Formateada} el producto {Grupo5_Min} vendio {Grupo5_Min_Cant} unidades')
    print (f'En la fecha {Fech2_Formateada} el producto {Grupo5_Max} vendio {Grupo5_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron hoy fue {Grupo5.count()}')
    
    print (f'La cantidad de productos vendidos en esta fecha fue {Grupo5.sum()}')
    
    Grupo6 = Ubicada2.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue ${Grupo6.sum()}')
    
    Promedio2 = Grupo6.sum() / Grupo5.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Promedio2, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue ${Grupo6.mean()}')
    
print (f'-' * 20)

print (f'{Cargar_Csv2}')

Lista_Csv2 = list(Cargar_Csv2['product'])

Key3 = [f'Key{i}' for i in range(len(Lista_Csv2))]

print (f'{Lista_Csv2}')
print (f'{Key3}')

Diccionario5 = dict(zip(Key3, Lista_Csv2))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key3"]}')
print (f'{Diccionario5.get("Key6")}')

print (f'-' * 20)

Division_Baja = 14 // 7
Exponente = 4**3
Modulo = 20%6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'El dato es de tipo {type(variable7)}')
print (f'El dato es de tipo {type(variable9)}')
print (f'El dato es de tipo {type(PEPE.Division_Flotante)}')
print (f'El dato es de tipo {type(variable11)}')

print (f'El dato es de tipo {type(Lista_Uno_Copia)}')
print (f'El dato es de tipo {type(Tupla1)}')
print (f'El dato es de tipo {type(Set_Conjunto_Menu1)}')
print (f'El dato es de tipo {type(Set_Conjunto_Menu2)}')

print (f'El dato es de tipo {type(Diccionario_Vacio2)}')
print (f'El dato es de tipo {type(Funcion_Diccionario)}')
print (f'El dato es de tipo {type(Objeto12)}')
print (f'El dato es de tipo {type(PEPE)}')
print (f'El dato es de tipo {type(Data_Frame_Concatenate)}')
print (f'El dato es de tipo {type(Array2_Sorted)}')

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

variable12, variable13 = 'Erick', 37

if (variable12 == 'Josue' and variable13 > 30):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumplen')
    
print (f'-' * 20)

if (variable12 == 'Erick' or variable13 > 50):
    print (f'Al menos una de las condiciones se cumplen')
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
        
Objeto45 = Entrenador(PEPE.Tupla_Poke[0], 'Kanto', Objeto13.Nombre)
Objeto46 = Entrenador(PEPE.Tupla_Poke[1], 'Alolah', Objeto14.Nombre)
Objeto47 = Entrenador(PEPE.Tupla_Poke[2], 'Paldea', Objeto15.Nombre)

Objeto45.Desplegar()
Objeto46.Desplegar()
Objeto47.Desplegar()

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
    print (f'Gracias por la informacion')
else:
    print (f'Error ingrese una cadena de texto')
    
print (f'-' * 20)

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')
    
print (f'-' * 20)
    
for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'El indice es {indice} y el valor es {elemento}')
    
print (f'-' * 20)

variable14 = 'eSteBAN'
variable14_letra = variable14[0]

print (f'{variable14}')
print (f'{variable14.lower()}')
print (f'{variable14.upper()}')
print (f'{variable14.capitalize()}')

print (f'{variable14.lower().find("t")}')
print (f'{variable14.lower().index("n")}')

print (f'La letra {variable14_letra} aparece {variable14.lower().count(variable14_letra)} veces')

print (f'{variable14.lower().startswith(variable14_letra)}')
print (f'{variable14.lower().endswith("n")}')

print (f'{variable14.lower().replace("ban", "POPOTAMO")}')

variable15 = 'esto es un texto cualquiera con el que voy a probar si esto sirve o no'

Lista_variable15 = variable15.split(' ')

for elemento in Lista_variable15:
    print (f'{elemento}')
    
print (f'El total de palabras digitadas es {len(Lista_variable15)}')

print (f'-' * 20)

var4 = 'esteban'

if (isinstance(var4, (str))):
    print (f'Lo ingresado es un texto')
else:
    print (f'Error, esto no es un texto')
    
if (var4.isalpha()):
    print (f'Lo ingresado es un texto')
else:
    print (f'Error, esto no es un texto')
    
try:
    Numerito6 = float(var4)
    if (Numerito6.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo ingresado es un texto')
    
print (f'-' * 20)

var5 = 3.5

if (isinstance(var5, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Error, lo ingresado no es un numero decimal')
    
try:
    Numerito7 = float(var5)
    if (Numerito7.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var6 = '3'

if (isinstance(var6, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
if (var6.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
try:
    Numerito8 = float(var6)
    if (Numerito8.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var7 = 3

if (isinstance(var7, (int, float))):
    print (f'Lo ingresado es numero entero o decimal')
else:
    print (f'Error, formato invalido')
    
try:
    Numerito9 = float(var7)
    if (Numerito9.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var8 = 'erick123'

if (isinstance(var8, (int, str))):
    print (f'Lo ingresado es un numero o un texto')
else:
    print (f'Error, formato invalido')
    
if (var8.isalnum()):
    print (f'Lo ingresado es un numero o un texto')
else:
    print (f'Error, formato invalido')
    
print (f'-' * 20)

var9 = '    a  '

if (var9.isspace()):
    print (f'Lo que ingresaste son solo espacios')
else:
    print (f'Error, esto tiene mucho mas que solo espacios')
    
var10 = 'eSteBAN'

if (var10.lower().islower()):
    print (f'Lo que ingresaste es texto en minuscula')
else:
    print (f'Error de formato')
    
if (var10.upper().isupper()):
    print (f'Lo que ingresaste es texto en mayuscula')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var11 = ' '

if (bool(var11) == True):
    print (f'Esto ya no esta vacio')
else:
    print (f'Esto esta vacio')
    
print (f'-' * 20)

print (f'{PEPE.Tupla_Poke[2]} aparece exactamente en la posicion {PEPE.Tupla_Poke.index("Misty")}')

Variable_Dict2 = Diccionario2.pop("Nombre")

print (f'Los elemntos eliminados son {Variable_Dict2}')

Counter = 0

while (Counter < 5):
    print (f'El contador es {Counter + 1}')
    Counter += 1
    
print (f'-' * 20)

Counter = 0

while (Counter < len(PEPE.Lista_Numeros)):
    print (f'El elemento {Counter} -- {PEPE.Lista_Numeros[Counter] * 100}')
    Counter += 1
    
print (f'-' * 20)

Lista_Animales = ['Jirafa', 'Ballena']
Lista_Animales.append('Tortuga')
Lista_Animales.insert(1, PEPE.Lista2[2])
Lista_Animales.extend(['Armadillo'])

print (f'{Lista_Animales}')

Counter = 0

while (Counter < len(Lista_Animales)):
    if (Lista_Animales[Counter] == 'Tortuga'):
        print (f'Este es mi animal favorito de todo el mundo')
        break
    else:
        Counter += 1
        continue
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Uno_Copia, Tupla1):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento1, elemento2, elemento3, elemento4 in zip(Lista_Uno_Copia, Tupla1, Set_Conjunto_Menu1, PEPE.Tupla_Poke):
    print (f'{elemento1} -- {elemento2} -- {elemento3} -- {elemento4}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'El elemento es {elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'El elemento es {elemento}')
    
print (f'-' * 20)

for elemento in range(0 + 2, len(Lista_Animales)):
    print (f'El elemento es {elemento}')
    
Lista_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'Lista Multiplicada: {Lista_Mult}')

Menor = min(Lista_Mult)
Mayor = max(Lista_Mult)

print (f'El menor de los numeros de la lista es {Menor}')
print (f'El mayor de los numeros de la lista es {Mayor}')

Redondear = round(14.458795, 2)

print (f'El redondeo del numero 14.458795 es {Redondear}')

Sumatoria4 = sum(Lista_Mult)

print (f'El resultado de la sumatoria es {Sumatoria4}')

print (f'{bool(not True)}')
print (f'{bool(False)}')
print (f'{bool("")}')
print (f'{bool(0)}')
print (f'{bool(None)}')

Todo_All = all([Lista_Animales, Set_Conjunto_Menu1, PEPE.Tupla_Poke, None])

if (Todo_All == True):
    print (f'Todos los elementos de la lista son correctos')
else:
    print (f'Hay al menos un elemento de la lista que no es correcto')
    
Uno = str(500)
Dos = int('500')
Tres = float(Uno)
Cuatro = list(PEPE.Tupla_Poke)
Cinco = set(Lista_Animales)
Seis = tuple(PEPE.Set_Conjunto_Poke1)

print (f'{type(500)} ahora es {type(Uno)}')
print (f'{type('500')} ahora es {type(Dos)}')
print (f'{type(Uno)} ahora es {type(Tres)}')
print (f'{type(PEPE.Tupla_Poke)} ahora es {type(Cuatro)}')
print (f'{type(Lista_Animales)} ahora es {type(Cinco)}')
print (f'{type(PEPE.Set_Conjunto_Poke1)} ahora es {type(Seis)}')

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
            Numerito2 = float(Numerito)
            if (Numerito2.is_integer()):
                print (f'Lo que ingresaste es un numero entero')
                break
            else:
                print (f'Lo que ingresaste es un numero decimal')
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')

Exception_Finale()'''

Ventas = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def buscar_primera_venta_mayor(Diccionario, Tope):    
    for indice, valor in Diccionario.items():
        if (valor > Tope):
            return indice, valor
        
    return None

Limite = 700

Sample29 = buscar_primera_venta_mayor(Ventas, Limite)

if (len(Ventas) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample29 is None):
        print (f'Error, no se ha encontrado un producto en el diccionario que valga mas que el limite')
    else:
        Clave, Articulo = Sample29
        print (f'{Clave} -- {Articulo}')
        
print (f'-' * 20)

Productos6 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def contar_productos_mayores(Diccionario, Tope):
    Contador = 0
    for elemento in Diccionario.values():
        if (elemento > Tope):
            Contador += 1
                
    return Contador

Limite2 = 150

Sample30 = contar_productos_mayores(Productos6, Limite2)

if (len(Productos6) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample30 == 0):
        print (f'No se encontraron articulos mas caros que el limite')
    else:
        print (f'La cantidad de articulos mas caros que ${Limite2} es {Sample30}')
        
        
class Ejemplo():
    def __init__(self, Nombre):
        self.Nombre = Nombre
    
    @property    
    def Mostrar(self):
        return self.Nombre
    
Objeto46 = Ejemplo('Erick')

print (f'Mi nombre es {Objeto46.Mostrar}')