try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado no existe')
    raise

Lista_Ejemplo1 = [1, 2, 3, 4, 5]

def Ejercicio1(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        while (Contador < len(Lista)):
            Contador += 1
            
    return Contador

Exercise1 = Ejercicio1(Lista_Ejemplo1)

if (Exercise1 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La cantidad de elementos de la lista es {Exercise1}')
    
print (f'-' * 20)

def Ejercicio2(Lista):
    Acumulador = 0
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador += elemento
        else:
            continue
        
    return Acumulador

Exercise2 = Ejercicio2(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de los elementos pares de la lista es {Exercise2}')
    
print (f'-' * 20)

def Ejercicio3(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        
        for elemento in Lista:
            Acumulador += elemento
            
        return Acumulador

Exercise3 = Ejercicio3(Lista_Ejemplo1)

if (Exercise3 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El resultado de sumar todos los elementos de la lista es {Exercise3}')
    
print (f'-' * 20)

def Ejercicio4(Lista, Numero):
    Founder = False

    for elemento in Lista:
        if (elemento == Numero):
            Founder = True
            return Founder
        else:
            continue
        
    return None

Buscar1 = 4

Exercise4 = Ejercicio4(Lista_Ejemplo1, Buscar1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Exercise4 is None):
        print (f'El numero {Buscar1} no fue encontrado en la lista')
    else:
        print (f'Exito! el numero {Buscar1} fue encontradoe en la lista')
        
print (f'-' * 20)

def Ejercicio5(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Menore = min(Lista)
        Mayore = max(Lista)
        
        Lista_Resultado = [Menore, Mayore]
        return Lista_Resultado

Exercise5 = Ejercicio5(Lista_Ejemplo1)

if (Exercise5 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de los numeros de la lista es {min(Exercise5)}')
    print (f'El mayor de los numeros de la lista es {max(Exercise5)}')
    
print (f'-' * 20)

def Ejercicio6(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Menore = min(Lista)
        Mayore = max(Lista)
        
        return Menore, Mayore

Exercise6 = Ejercicio6(Lista_Ejemplo1)

if (Exercise6 is None):
    print (f'Error, la lista esta vacia')
else:
    Menor1, Mayor1 = Exercise6
    print (f'El menor de los numeros de la lista es {Menor1}')
    print (f'El mayor de los numeros de la lista es {Mayor1}')

print (f'-' * 20)

def Ejercicio7(Lista, Numero):
    Contador = 0
    
    for elemento in Lista:
        if (elemento > Numero):
            Contador += 1
        else:
            continue
        
    if (Contador > 0):
        return Contador
    else:
        return None

Numerito1 = 2

Exercise7 = Ejercicio7(Lista_Ejemplo1, Numerito1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Exercise7 is None):
        print (f'Error, no hay ningun numero mayor a {Numerito1} en la lista')
    else:
        print (f'En la lista hay {Exercise7} numeros mayores que {Numerito1}')
        
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

Exercise8 = Ejercicio8(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista de numeros pares es {Exercise8}')
    
print (f'-' * 20)

def Ejercicio9(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_ImPares = []
        
        for elemento in Lista:
            if (elemento % 2 != 0):
                Lista_ImPares.extend([elemento])
            else:
                continue
            
        return Lista_ImPares

Exercise9 = Ejercicio9(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista de numeros impares es {Exercise9}')
    
print (f'-' * 20)

def Ejercicio10(Lista):
    Lista_Mult = list([])
    
    for elemento in Lista:
        Lista_Mult.append(elemento * 2)
        
    return Lista_Mult

Exercise10 = Ejercicio10(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista original: {Lista_Ejemplo1}')
    print (f'Lista actualizada: {Exercise10}')
    
print (f'-' * 20)

'''Lista_Promedios = []

Contador = 0

while (Contador < 3):
    while True:
        Nota = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito2 = float(Nota)
            if (Numerito2.is_integer()):
                print (f'Lo que ingresaste fue un numero entero')
                Lista_Promedios.append(Numerito2)
                break
            else:
                print (f'Lo que ingresaste fue un numero decimal')
                Lista_Promedios.append(Numerito2)
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador += 1

Promedio1 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas agregadas es {round(Promedio1, 2)}')'''

def Ejercicio11(Lista):
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
                
        return Lista_Impares, Lista_Pares

Exercise11 = Ejercicio11(Lista_Ejemplo1)

if (Exercise11 is None):
    print (f'Error, la lista esta vacia')
else:
    Impares1, Pares1 = Exercise11
    
    print (f'Lista Original: {Lista_Ejemplo1}')
    print (f'Lista Impares: {Impares1}')
    print (f'Lista Pares: {Pares1}')
    
print (f'-' * 20)

Lista_Ejemplo2 = list([5, -6, 0, -1, -3, 0])

def Ejercicio12(Lista):
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

Exercise12 = Ejercicio12(Lista_Ejemplo2)

if (len(Lista_Ejemplo2) == 0):
    print (f'Error, la lista esta vacia')
else:
    Positivos1, Negativos1, Ceros1 = Exercise12
    
    print (f'Total numeros positivos: {Positivos1}')
    print (f'Total numeros Negativos: {Negativos1}')
    print (f'Total numeros ceros: {Ceros1}')
    
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

def Ejercicio13(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Correos_Validos = []
        Correos_Invalidos = list([])
        
        Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'
        
        for elemento in Lista:
            Buscar = bool(re.fullmatch(Pattern, elemento))
            
            if (Buscar == True):
                Correos_Validos.append(elemento)
            else:
                Correos_Invalidos.extend([elemento])
                
        return Correos_Validos, Correos_Invalidos

Exercise13 = Ejercicio13(Lista_Ejemplo3)

if (Exercise13 is None):
    print (f'Error, la lista esta vacia')
else:
    Lista_Correos_Validos, Lista_Correos_Invalidos = Exercise13
    
    print (f'Lista de correos validos: {Lista_Correos_Validos}')
    print (f'Lista de correos invalidos: {Lista_Correos_Invalidos}')
    
print (f'-' * 20)

def Ejercicio14(Lista):
    Mayor = Lista[0]
    
    for elemento in Lista:
        if (elemento > Mayor):
            Mayor = elemento
        else:
            continue
        
    return Mayor

Exercise14 = Ejercicio14(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El mayor de los numeros de la lista es {Exercise14}')
    
print (f'-' * 20)

def Ejercicio15(Lista):
    Menor = Lista[0]
    
    for elemento in Lista:
        if (elemento < Menor):
            Menor = elemento
        else:
            continue
        
    return Menor

Exercise15 = Ejercicio15(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de los numeros de la lista es {Exercise15}')
    
print (f'-' * 20)

Lista_Ejemplo4 = [-15.5, -8, -3.2, -1, 0, 4, 7.5, 12, 19.1, 25]

def Ejercicio16(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador_Positivos = 0
        Acumulador_Positivos = 0
        
        for elemento in Lista:
            if (elemento > 0):
                Contador_Positivos += 1
                Acumulador_Positivos += elemento
                
        return Contador_Positivos, Acumulador_Positivos

Exercise16 = Ejercicio16(Lista_Ejemplo4)

if (Exercise16 is None):
    print (f'Error, la lista esta vacia')
else:
    Total_Positivos, Suma_Positivos = Exercise16
    
    print (f'El total de numeros positivos en la lista es {Total_Positivos}')
    print (f'La suma de estos numeros positivos es {Suma_Positivos}')
    
print (f'-' * 20)

Lista_Ejemplo5 = [65, 70, 54, 80, 69, 66]

def Ejercicio17(Lista):
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

Exercise17 = Ejercicio17(Lista_Ejemplo5)

if (len(Lista_Ejemplo5) == 0):
    print (f'Error, la lista esta vacia')
else:
    Aprobados1, Suma_Aprobados1, Reprobados1 = Exercise17
    
    print (f'La cantidad de estudiantes aprobados es {Aprobados1}')
    print (f'La cantidad de estudiantes reprobados es {Reprobados1}')
    print (f'La suma de las notas de los estudiantes aprobados es {Suma_Aprobados1}')
    
print (f'-' * 20)

Lista_Ejemplo6 = list([15, 0, 8, 2, 0, 25, 4])

def Ejercicio18(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Agotado = 0
        Stock_Bajo = 0
        Stock_Alto = 0
        Stock_Bajo_Sum = 0
        Stock_Alto_Sum = 0
        
        for elemento in Lista:
            if (elemento <= 0):
                Agotado += 1
            elif (elemento >= 1 and elemento <= 5):
                Stock_Bajo += 1
                Stock_Bajo_Sum += elemento
            else:
                Stock_Alto += 1
                Stock_Alto_Sum += elemento
                
        return Stock_Bajo_Sum, Stock_Bajo, Stock_Alto_Sum, Stock_Alto, Agotado

Exercise18 = Ejercicio18(Lista_Ejemplo6)

if (Exercise18 is None):
    print (f'Error, la lista esta vacia')
else:
    Prod_Stock_Bajo_Sum, Prod_Stock_Bajo, Prod_Stock_Alto_Sum, Prod_Stock_Alto, Prod_Agotado = Exercise18
    
    print (f'Cantidad productos agotados: {Prod_Agotado}')
    print (f'Cantidad productos stock bajo: {Prod_Stock_Bajo}')
    print (f'Sumatoria de productos stock bajo: {Prod_Stock_Bajo_Sum}')
    print (f'Cantidad productos stock alto: {Prod_Stock_Alto}')
    print (f'Sumatoria de productos stock alto: {Prod_Stock_Alto_Sum}')
    
    print (f'La suma de todos los productos que tienen stock es {Prod_Stock_Bajo_Sum + Prod_Stock_Alto_Sum}')
    
print (f'-' * 20)

Lista_Ejemplo7 = [12, 8, 5, 2, 7, 0, 10]

def Ejercicio19(Lista):
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

Exercise19 = Ejercicio19(Lista_Ejemplo7)

if (len(Lista_Ejemplo7) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Exercise19 is None):
        print (f'Por el momento no hay ningun producto agotado')
    else:
        print (f'El primer producto agotado del inventario esta en la posicion {Exercise19}')
        
print (f'-' * 20)

Lista_Ejemplo8 = [120, 350, 80, 600, 150, 700]

def Ejercicio20(Lista, Numero):
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

Monto = 200

Exercise20 = Ejercicio20(Lista_Ejemplo8, Monto)

if (len(Lista_Ejemplo8) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Exercise20 is None):
        print (f'En la lista no hay una venta superior al monto ingresado')
    else:
        print (f'La venta superior al monto ${Monto} aparece en la posicion {Exercise20} y la venta es ${Lista_Ejemplo8[Exercise20]}')
        
print (f'-' * 20)
        
Lista_Ejemplo9 = [10, 5, 2, 4, 3, 1, 6]

def Ejercicio21(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            
    return None

Exercise21 = Ejercicio21(Lista_Ejemplo9)

if (len(Lista_Ejemplo9) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Exercise21 is None):
        print (f'No hay dos numeros iguales en la lista')
    else:
        print (f'El primer numero de la lista igual es {Exercise21}')
        
print (f'-' * 20)
        
Lista_Ejemplo9 = [10, 1, 2, 4, 3, 5, 6]

def Ejercicio22(Lista):
    for i in range(0, len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                return Lista[i]
            else:
                continue
            
    return None

Exercise22 = Ejercicio22(Lista_Ejemplo9)

if (len(Lista_Ejemplo9) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Exercise22 is None):
        print (f'No hay dos numeros iguales en la lista')
    else:
        print (f'El primer numero de la lista igual es {Exercise22}')
        
print (f'-' * 20)

Lista_Ejemplo10 = [90, 91, 79, 82]

def Ejercicio23(Lista):
    Posicion = 0
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] < Lista[i]):
            Posicion = i
            return Posicion
        else:
            continue
        
    return None

Exercise23 = Ejercicio23(Lista_Ejemplo10)

if (len(Lista_Ejemplo10) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Exercise23 is None):
        print (f'En la lista nunca sucede un aumento de ventas con respecto al dia anterior')
    else:
        print (f'El aumento de ventas sucede en la posicion {Exercise23}')
        
print (f'-' * 20)

Lista_Ejemplo11 = [100, 97, 95, 80, 78]

def Ejercicio24(Lista, Fall):
    Posicion = 0
    Grados = 0
    
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] - Lista[i] >= Fall):
            Grados = Lista[i - 1] - Lista[i]
            Posicion = i
            return Grados, Posicion
        else:
            pass

    return None

Caida = 5

Exercise24 = Ejercicio24(Lista_Ejemplo11, Caida)

if (len(Lista_Ejemplo11) == 0):
    print (f'Error la lista esta vacia')
else:
    if (Exercise24 is None):
        print (f'Maquina estable, no hay caidas bruscas de temperatura')
    else:
        Grados, Posicion = Exercise24
        print (f'Hubo una caida de {Grados} grados en la posicion {Posicion}')
        
print (f'-' * 20)

Lista_Ejemplo12 = [1, 1, 2, 1, 3]

def Ejercicio25(Lista):
    for i in range(0 + 2, len(Lista)):
        if (Lista[i - 2] < Lista[i - 1] and Lista[i - 1] > Lista[i]):
            return Lista[i - 1]
        else:
            continue
        
    return None

Exercise25 = Ejercicio25(Lista_Ejemplo12)

if (len(Lista_Ejemplo12) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Exercise25 is None):
        print (f'No hay un numero que cumpla las caracteristicas de un Pico')
    else:
        print (f'El numero que genera un pico es {Exercise25}')
        
print (f'-' * 20)

# Consultar valores ✅ Consultar.

Capitales1 = {"Costa Rica": "San José", "México": "Ciudad de México", "Argentina": "Buenos Aires", "Italia": "Roma", "España": "Madrid"}

Ubicado1 = Capitales1.get("Italia")

if (Ubicado1 is None):
    print (f'Error, la ciudad elegida no existe')
else:
    print (f'La capital de Italia es {Ubicado1}')
    
print (f'-' * 20)

# Consultar valores ✅ Consultar.

Productos1 = {"Laptop": 1200, "Mouse": 25, "Teclado": 45, "Monitor": 300}

def Ejercicio26(Diccionario, Cosa):
    Ubicado2 = Diccionario.get(Cosa)
    if (Ubicado2 is None):
        return None
    else:
        return Ubicado2
    
Item1 = 'Cajon'

Exercise26 = Ejercicio26(Productos1, Item1)

if (len(Productos1) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Exercise26 is None):
        print (f'No se ubico el producto {Item1} en el diccionario')
    else:
        print (f'El precio del producto {Item1} es ${Exercise26}')
        
print (f'-' * 20)

# Actualizar elementos ✅ Actualizar.

Productos2 = {
	"Laptop": 1200,
	"Mouse": 25,
	"Teclado": 45,
	"Monitor": 300
}

Item2 = 'Teclado'
Item2_Precio = 55

def Ejercicio27(Diccionario, Cosa, Precio):
    Ubicado2 = Diccionario.get(Cosa)
    if (Ubicado2 is None):
        return False
    else:
        Diccionario[Cosa] = Precio
        return True

Exercise27 = Ejercicio27(Productos2, Item2, Item2_Precio)

if (len(Productos2) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Exercise27 == True):
        print (f'Listo! el precio del producto {Item2} fue actualizado')
    else:
        print (f'Error, el producto no existe, no se puede actualizar el precio')
        
print (f'-' * 20)

# Agregar elementos ✅ Agregar.

Productos3 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio28(Diccionario, Cosa, Precio):
    Ubicado2 = Diccionario.get(Cosa)
    
    if (Ubicado2 is None):
        Diccionario[Cosa] = Precio
        return False
    else:
        return True

Item3 = 'Teclado'
Item3_Precio = 300

Exercise28 = Ejercicio28(Productos3, Item3, Item3_Precio)

if (len(Productos3) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Exercise28 == True):
        print (f'Error, el producto ya existe en inventario, no es necesario agregarlo nuevamente')
    else:
        print (f'Listo! el producto {Item3} fue incluido en el inventario')
        
print (f'-' * 20)

# Eliminar elementos ✅ Eliminar.

Productos4 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio29(Diccinario, Cosa):
    Ubicado2 = Diccinario.get(Cosa)
    if (Ubicado2 is None):
        return False
    else:
        Diccinario.pop(Cosa)
        return True

Item4 = 'Laptop'

Exercise29 = Ejercicio29(Productos4, Item4)

if (len(Productos4) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Exercise29 == False):
        print (f'Error el producto no existe, no se puede eliminar')
    else:
        print (f'Listo! el producto {Item4} fue eliminado del inventario')
        
print (f'-' * 20)

Productos5 = {
    "Laptop": 99,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 100,
    "Impresora": 180
}

def Ejercicio30(Diccionario):
    Nombre = next(iter(Diccionario))
    Precio = Diccionario[Nombre]
    
    for indice, elemento in Diccionario.items():
        if (Precio < elemento):
            Nombre = indice
            Precio = elemento
        else:
            continue
        
    return Nombre, Precio

Exercise30 = Ejercicio30(Productos5)

if (len(Productos5) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Nombre, Precio = Exercise30
    
    print (f'Nombre Producto: {Nombre}')
    print (f'Precio Producto: {Precio}')
    
print (f'-' * 20)

'''def Floating1(Numero):
    Resultado = Numero * 12 + 150
    return Resultado

print (f'El resultado de la operacion es {Floating1(PEPE.Flotante1)}')

print (f'-' * 20)

Floating2 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Floating2}')

print (f'-' * 20)

def Floating3(Cadena):
    Nombre = Cadena.replace(' ', '')
    if (isinstance(Nombre, (str))):
        if (Nombre.isalpha()):
            print (f'Lo que ingresaste es un texto')
        else:
            print (f'Error, lo que ingresaste no es un texto')

Floating3(PEPE.Flotante3)

print (f'-' * 20)

def Floating4(Cadena):
    Lista_Cadena = Cadena.split(' ')
    
    for elemento in enumerate(Lista_Cadena):
        print (f'{elemento[0]} -- {elemento[1]}')
        
    print (f'El numero de palabras digitadas es {Lista_Cadena.__len__()}')

Floating4(PEPE.Flotante4)'''

'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese el numero de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Lista.append(Alumno)
        
    return Lista

print (f'La lista de alumnos ingresados es: {Colegio(Lista_Alumnos)}')'''

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
    
    print (f'El menor de los alumnos de la lista es {Menore} con una edad de {Lista[0][1]} años')
    print (f'El mayor de los alumnos de la lista es {Mayore} con una edad de {Lista[-1][1]} años')

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
    
    def __len__(self):
        return len(self.Nombre)
        
Lista_Colores = [
    Colores('Rojo'),
    Colores('Azul'),
    Colores('Verde')
]

print (f'La lista de colores es {Lista_Colores}')
print (f'La cantidad de elementos en la lista es {len(Lista_Colores)}')

print (f'-' * 20)

class Inventario():
    def __init__(self):
        self.Producto = []
        
    def __len__(self):
        return len(self.Producto)
        
Objeto2 = Inventario()

Objeto2.Producto.append('Casa')
Objeto2.Producto.insert(1, 'Carro')
Objeto2.Producto.extend(['Piscina'])

print (f'La cantidad de elementos del inventario es {len(Objeto2)}')

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

print (f'El resultado de la sumatoria es {Objeto5 + Objeto6}')

print (f'-' * 20)

class Caja2():
    def __init__(self):
        self.Productos = ['Lapiz', 'Borrador', 'Cuaderno']
        
    def __getitem__(self, Indice):
        return self.Productos[Indice]
        
Objeto7 = Caja2()

print (f'El producto en la posicion 0 es {Objeto7[0]}')
print (f'El producto en la posicion 1 es {Objeto7[1]}')
print (f'El producto en la posicion 2 es {Objeto7[2]}')

print (f'-' * 20)

class Panaderia():
    def __init__(self):
        self.Panes = list([
            'Baguette',
            'Croissant',
            'Pan Dulce'
        ])
        
    def __iter__(self):
        return iter(self.Panes)
        
Objeto8 = Panaderia()

for elemento in enumerate(Objeto8):
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

'''import requests

Sabore1 = 'Mora'

Agregar1 = requests.post(f'http://127.0.0.1:8015/grupo1/{Sabore1}')
Agregar2 = Agregar1.json()

print (f'{Agregar2}')

Obtener1 = requests.get('http://127.0.0.1:8015/grupo1/')
Obtener2 = Obtener1.json()

print (f'Lista de helados: {Obtener2["Helados"]}')'''

var1 = '3'

if (isinstance(var1, (int))):
    print (f'Esto es un numero entero')
else:
    print (f'Esto no es un numero entero')
    
if (var1.isnumeric()):
    print (f'Esto es un numero entero')
else:
    print (f'Esto no es un numero entero')
    
try:
    Numerito2 = float(var1)
    if (Numerito2.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var2 = 3.5

if (isinstance(var2, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Esto no es un numero decimal')
    
try:
    Numerito3 = float(var2)
    if (Numerito3.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var3 = 3.5

if (isinstance(var3, (int, float))):
    print (f'Lo que ingresaste puede ser un numero entero o decimal')
else:
    print (f'Error de formato')
    
try:
    Numerito4 = float(var3)
    if (Numerito4.is_integer()):
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

Pattern1 = r'\!|\@|\d+'

Texto1_Version4 = re.sub(Pattern1, '', Texto1_Version3)

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
    
    print (f'El producto con menos unidades en inventario es {Grupo1_Min}, cantidad en inventario {Grupo1_Min_Cant}')
    print (f'El producto con mas unidades en inventario es {Grupo1_Max}, cantidad en inventario {Grupo1_Max_Cant}')
    
    print (f'La cantidad de productos vendidos en esta fecha fue {Grupo1.sum()}')
    print (f'La cantidad de clientes que nos compraron en esta fecha fue {Grupo1.count()}')
    
    Grupo2 = Encontrado1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue ${Grupo2.sum()}')
    
    Promedio1 = Grupo2.sum() / Grupo1.count()
    
    print (f'El promedio de venta en esta fecha fue de ${round(Promedio1, 2)}')
    print (f'El promedio de venta en esta fecha fue de ${Grupo2.mean()}')
    
print (f'-' * 20)

print (f'{Cargar_Csv1}')

Set_Conjunto_Csv1 = set(Cargar_Csv1['product'])

print (f'{Set_Conjunto_Csv1}')

Lista_Csv1 = list(Set_Conjunto_Csv1)

Key1 = [f'Key{i}' for i in range(len(Lista_Csv1))]

Diccionario1 = dict(zip(Key1, Lista_Csv1))

print (f'-' * 20)

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1["Key3"]}')
print (f'{Diccionario1.get("Key6")}')

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

Pattern2 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.[a-z]{2,}'

Buscar2 = re.findall(Pattern2, Texto2)

print (f'{Buscar2}')

print (f'-' * 20)

Pattern3 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar3 = re.findall(Pattern3, Texto2)

print (f'{Buscar3}')

for elemento in Buscar3:
    print (f'{elemento}')
    
print (f'-' * 20)

import re

Texto3 = '28'

Pattern4 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar4 = bool(re.match(Pattern4, Texto3))

if (Buscar4 == True):
    print (f'El numero esta entre 01 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

import re

Texto4 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern5 = r'\d{2}\/[0-9]{2,}\/\d{3,4}'

Replacement5 = 'XX/XX/XXXX'

Buscar5 = re.sub(Pattern5, Replacement5, Texto4)

print (f'{Buscar5}')

Pattern6 = r'\+\d{1}\-[0-9]{3}\-\d{2,}\-[0-9]{4,10}'

Replacement6 = 'Ph0n3Numb3r'

Buscar6 = re.sub(Pattern6, Replacement6, Buscar5)

print (f'{Buscar6}')

print (f'-' * 20)

import re

Texto5 = """
Contactos:
- juan.perez@gmail.com
- maria_123@hotmail.net
- usuario-invalido@com
- pedro.lopez@yahoo.org
- test@empresa
- ana+test@gmail.com
"""

Pattern7 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar7 = re.findall(Pattern7, Texto5)

print (f'{Buscar7}')

for indice, elemento in enumerate(Buscar7, start=1):
    print (f'{indice} -- {elemento}')
    
print (f'-' * 20)

import re

Texto6 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Metodo 1

Pattern8 = r'\!|\?|\.{2,}|\d{4}\-[0-9]{4,}'

Buscar8 = re.sub(Pattern8, '', Texto6)

print (f'{Buscar8}')

# Metodo 2

Pattern9 = r'[^a-zA-Z0-9\s\d{1,3}]'

Buscar9 = re.sub(Pattern9, '', Texto6)

print (f'{Buscar9}')

print (f'-' * 20)

import re

Texto7 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Pattern10 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correo = re.findall(Pattern10, Texto7)

print (f'{Correo}')

Texto7_temp1 = Texto7

for i, email in enumerate(Correo, start=1):
    Texto7_temp1 = Texto7_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto7_temp1}')

Pattern11 = r'\!|\?'

Texto7_temp2 = re.sub(Pattern11, '', Texto7_temp1)

print (f'{Texto7_temp2}')

for i, email in enumerate(Correo, start=1):
    Texto7_temp2 = Texto7_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto7_temp2}')

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
        Nota = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito5 = float(Nota)
            if (Numerito5.is_integer()):
                print (f'Lo que ingresaste es un numero entero')
                Lista_Promedios.append(Numerito5)
                break
            else:
                print (f'Lo que ingresaste es un numero decimal')
                Lista_Promedios.extend([Numerito5])
                break
        except ValueError:
            print (f'Error, ingrese un numero')
    Contador+= 1
    
Promedio2 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas elegidas es {round(Promedio2, 2)}')'''

from Module_Own import Pokemon1 as Poke1

Objeto9 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Impact Trueno', 'Electrico')
Objeto10 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Sismo', 'Roca')

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
        
Objeto12 = Perro('Chester', 5, 2.8, 'Poodle', 'Hiper-Tension')

Veterinaria.Mostrar(Objeto12)
Objeto12.Mostrar()

print (f'-' * 20)

class Gato(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente = Paciente

    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto13 = Gato('Messi', 1.8, 1.5, 'Gris', 'No')

Veterinaria.Mostrar(Objeto13)
Objeto13.Mostrar()

print (f'-' * 20)

class Pajaro(Veterinaria):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto14 = Pajaro('Polly', 31, 0.4, 'Cacatua Amarilla', 'Si')

Veterinaria.Mostrar(Objeto14)
Objeto14.Mostrar()

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
        
Objeto15 = Paladin(25, 'Battle Axe', 15, 'Dark Crystal', 200, 'Ghost Knight')

Objeto15.Mostrar()
Atacante.Mostrar(Objeto15)
Defensor.Mostrar(Objeto15)

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
        
Objeto16 = D1()

A1.Mostrar(Objeto16)
B1.Mostrar(Objeto16)
C1.Mostrar(Objeto16)
Objeto16.Mostrar()
E1.Mostrar(Objeto16)

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
        
Objeto17 = Cripto()
Objeto18 = Efectivo()
Objeto19 = Tarjeta()

Objeto17.Pagar()
Objeto18.Pagar()
Objeto19.Pagar()

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
        
Objeto18 = Cuenta_Bancaria(125)
Objeto18.Depositar(25)
Objeto18.Mostrar()

print (f'Su saldo privado que no deberia ser publicado nunca es {Objeto18.Dinero}')

Objeto18.Dinero = '50,000,000'

Objeto18.Mostrar()

print (f'Su saldo privado que no deberia ser publicado nunca es {Objeto18.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla(Plantilla):
    def Mostrar(self):
        print (f'Este es el metodo de la sub plantilla')
        
    def General(self):
        print (f'Este es el metodo de la plantilla principal mandatorio')
        
Objeto19 = Sub_Plantilla()

Objeto19.Mostrar()
Objeto19.General()

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
        
Objeto20 = Pastel1()

Objeto20.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Ingrediente1 = Chocolate()
Objeto21 = Pastel2(Ingrediente1)
Objeto21.Hornear()

Ingrediente2 = Vainilla()
Objeto22 = Pastel2(Ingrediente2)
Objeto22.Hornear()

Ingrediente3 = Fresa()
Objeto23 = Pastel2(Ingrediente3)
Objeto23.Hornear()

print (f'-' * 20)

import re

Texto8 = 'esto es 12! un texto que hola yo deberia 80 ser el - primero inicial hela pero aquel 250 @ que yo tendria es mi hila casa'

Buscar10 = re.search(r'inicial', Texto8)

print (f'{Buscar10}')

Buscar11 = re.findall(r'\d+', Texto8)

print (f'{Buscar11}')

Buscar12 = bool(re.fullmatch(r'esto es 12\! un texto que hola yo deberia 80 ser el \- primero inicial hela pero aquel 250 \@ que yo tendria es mi hila casa', Texto8))

if (Buscar12 == True):
    print (f'Ambos textos son iguales')
else:
    print (f'Error, los textos no son iguales')
    
print (f'-' * 20)

'''
{4}
{2,}
{4,10}
? [0 o 1]
+ [1 o mas]
* [0 o mas]
'''

Buscar13 = re.findall(r'h.la', Texto8)

print (f'{Buscar13}')

Buscar14 = re.findall(r'^esto', Texto8)

print (f'{Buscar14}')

Buscar15 = re.findall(r'a$', Texto8)

print (f'{Buscar15}')

Buscar16 = re.findall(r'\d{3}\s\W', Texto8)

print (f'{Buscar16}')

Buscar17 = re.findall(r'([ab]+)', Texto8)

print (f'{Buscar17}')

Buscar18 = re.findall(r'[ab]+', Texto8)

print (f'{Buscar18}')

print (f'-' * 20)

Texto9 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern12 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correo2 = re.findall(Pattern12, Texto9)

Texto9_temp1 = Texto9

for i, email in enumerate(Correo2, start=1):
    Texto9_temp1 = Texto9_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto9_temp1}')

Pattern13 = r'\!|\?|\.{2,}|\d{4}\-[0-9]{4,10}'

Texto9_temp2 = re.sub(Pattern13, '', Texto9_temp1)

print (f'{Texto9_temp2}')

for i, email in enumerate(Correo2, start=1):
    Texto9_temp2 = Texto9_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto9_temp2}')

print (f'-' * 20)

var4 = 3.5

if (isinstance(var4, (float))):
    print (f'El numero es decimal')
else:
    print (f'Esto no es un numero decimal')
    
try:
    Numerito5 = float(var4)
    if (Numerito5.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var5 = '3'

if (isinstance(var5, (int))):
    print (f'Esto es un numero entero')
else:
    print (f'Esto no es un numero entero')
    
if (var5.isnumeric()):
    print (f'Esto es un numero entero')
else:
    print (f'Esto no es un numero entero')
    
try:
    Numerito6 = float(var5)
    if (Numerito6.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

import re

Texto10 = "   Hola!!!   mundo@@   123   "

print (f'{Texto10}')

Texto10_Version1 = Texto10.strip()

print (f'{Texto10_Version1}')

Texto10_Version2 = ' '.join(Texto10_Version1.split())

print (f'{Texto10_Version2}')

Texto10_Version3 = Texto10_Version2.lower()

print (f'{Texto10_Version3}')

Pattern14 = r'\!|\@|\d{3,}'

Texto10_Version4 = re.sub(Pattern14, '', Texto10_Version3)

print (f'{Texto10_Version4}')

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

def Exception2(Num1, Num2):
    try:
        Resultado = Num1 + Num2
        print (f'El resultado de la operacion es {Resultado}')
    except (ValueError, TypeError):
        print (f'Error, ambos elementos deben ser numeros')

Exception2(12, 'hola')

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        Division = Num1 / Num2
        
        print (f'El resultado de la division es {round(Division, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

Exception3(12, 0)

print (f'-' * 20)

Lista_Exception4 = list(['Erick'])
Lista_Exception4.append('Josue')
Lista_Exception4.insert(1, 'Karlita')
Lista_Exception4.extend(['Roberta'])

def Exception4(Indice):
    try:
        print (f'El texto en el indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(4)

print (f'-' * 20)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : 37})

def Exception5(Llave):
    try:
        print (f'El texto en la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception5("Votante")

print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Hiena')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo txt no existe')
    
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
    Documento_Agregar = Docu.write(f'\nPanda Rojo')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nPato Amarilo', f'\nPato Rojo', f'\nPato Verde'])
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

print (f'La menor de las edades del dataframe es {Data_Frame_Concatenate_Age.min()}')
print (f'La mayor de las edades del dataframe es {Data_Frame_Concatenate_Age.max()}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate}')

Grupo3 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()
Grupo3_Min_Cant = Grupo3.min()
Grupo3_Max_Cant = Grupo3.max()

print (f'Del dataframe el sadico con menor edad es {Grupo3_Min} y su edad es {Grupo3_Min_Cant} años')
print (f'Del dataframe el sadico con menor edad es {Grupo3_Max} y su edad es {Grupo3_Max_Cant} años')

print (f'La suma total de todas las edades es {Grupo3.sum()}')

print (f'El datafarme esta compuesto por {Grupo3.count()} personas')

print (f'El promedio de las edades del dataframe es {round(Grupo3.mean(), 2)}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Unidad1 = elemento['Nombre']
    Unidad2 = elemento['Edad']
    
    print (f'Hola, mi nombre es {Unidad1} y mi edad es {Unidad2} años')
    
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

Elemento1 = Data_Frame1.loc[0, "Nombre"]
Elemento2 = Data_Frame1.loc[1, "Edad"]
Elemento3 = Data_Frame1.loc[2, "Votante"]
Elemento4 = Data_Frame1.loc[:, "Nombre"]
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
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col="tarifa")
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col="tarifa", usecols="E:K")
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col="tarifa", usecols="E:K", nrows=1)

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

Cargar_Excel3_Sorted = Cargar_Excel3.sort_values(by = 'cinco', ascending=True)

print (f'{Cargar_Excel3_Sorted}')

print (f'-' * 20)

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by = 'cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

print (f'-' * 20)

import pandas as pd

Ruta_Txt = 'C:\\Repo\\HolaMundo.txt'

Cargar_Txt = pd.read_csv(Ruta_Txt)

print (f'{Cargar_Txt.head()}')

print (f'-' * 20)

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

print (f'{Cargar_Html[2].head()}')

print (f'-' * 20)

Array0 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print (f'{Array0}')
print (f'{Array0[2][::2]}')
print (f'{Array0[1][::3]}')
print (f'{Array0[0][:2]}')
print (f'{Array0[0][2:]}')
print (f'{Array0[2][2:3]}')
print (f'{Array0[1][0:None]}')
print (f'{Array0[1][:]}')
print (f'{Array0[:][2]}')

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

print (f'{Array2[0, ::2]}')
print (f'{Array2[1, ::3]}')
print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[:, 2]}')
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

print (f'-' * 20)

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {Array2_Sorted_Mean}')
print (f'Sumatoria: {Array2_Sorted_Sum}')

print (f'Sumita: {Sumita1}')
print (f'Sumita: {Sumita2}')
print (f'Sumita: {Sumita3}')
print (f'Sumita: {Sumita4}')

print (f'-' * 20)

Array3 = np.array([[['e', 'j', 'm'], ['o', 'l', 'f']],         [['s', 'k', 'n'], ['w', 'd', 'a']]])

print (f'{Array3}')
print (f'{Array3.ndim}')
print (f'{Array3.shape}')
print (f'{Array3.size}')
print (f'{Array3.dtype}')
print (f'{Array3[0, 1, 2]}')

print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[1, 0, :2]}')
print (f'{Array3[1, 0, 2:]}')
print (f'{Array3[1, :, 0]}')
print (f'{Array3[1, 1, 2:3]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "m"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],            [[[5, 6, 4], [9, 8, 7]], [[0, 4, 2], [3, 8, 2]]]])

print (f'{Array4}')
print (f'{Array4.ndim}')
print (f'{Array4.shape}')
print (f'{Array4.size}')
print (f'{Array4.dtype}')
print (f'{Array4[1, 0, 0, 2]}')

print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[0, 1, 1, ::3]}')
print (f'{Array4[1, 0, 0, :2]}')
print (f'{Array4[1, 0, 0, 2:]}')
print (f'{Array4[0, 1, :, 2]}')
print (f'{Array4[0, 1, 1, 2:3]}')
print (f'{Array4[1, 0, 1, 0:None]}')
print (f'{Array4[1, 0, 1, :]}')
print (f'{Array4[Array4 >= 2]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[0, 1, 1, 0:None])
Sumita8 = np.sum(Array4_Sorted[0, 1, 1, :])

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

print (f'Sumita: {Sumita5}')
print (f'Sumita: {Sumita6}')
print (f'Sumita: {Sumita7}')
print (f'Sumita: {Sumita8}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1) #type: ignore

print (f'{Array_Num1}')

print (f'El mas pequeño de los numeros del array es {np.min(Array_Num1)}')
print (f'El mas grande de los numeros del array es {np.max(Array_Num1)}')

print (f'-' * 20)

Array_Num2 = np.arange(start=1, stop=26, step=1) #type: ignore

print (f'{Array_Num2}')

Array_Num2_Reshape = np.reshape(Array_Num2, shape=(5, 5))

print (f'{Array_Num2_Reshape}')

print (f'-' * 20)

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
print (f'{Array_Zeros[1, 1]}')

print (f'{Array_Zeros[0, ::2]}')
print (f'{Array_Zeros[1, ::3]}')
print (f'{Array_Zeros[1, :2]}')
print (f'{Array_Zeros[1, 2:]}')
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
print (f'{Array_Ones[1, 0]}')

print (f'{Array_Ones[1, ::2]}')
print (f'{Array_Ones[0, ::3]}')
print (f'{Array_Ones[1, :2]}')
print (f'{Array_Ones[1, 2:]}')
print (f'{Array_Ones[:, 0]}')
print (f'{Array_Ones[1, 2:3]}')
print (f'{Array_Ones[0, 0:None]}')
print (f'{Array_Ones[0, :]}')
print (f'{Array_Ones[Array_Ones == 1]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value=f'{PEPE.Diccionario_Poke["Poke1"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[0, 0]}')

print (f'{Array_Gen1[0, ::2]}')
print (f'{Array_Gen1[1, ::3]}')
print (f'{Array_Gen1[1, :2]}')
print (f'{Array_Gen1[1, 2:]}')
print (f'{Array_Gen1[:, 1]}')
print (f'{Array_Gen1[1, 2:3]}')
print (f'{Array_Gen1[0, 0:None]}')
print (f'{Array_Gen1[0, :]}')

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

Array_Gen3 = np.full(shape=(2, 3), fill_value=Array4[0, 1, 0, 2])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 2]}')

print (f'{Array_Gen3[0, ::2]}')
print (f'{Array_Gen3[1, ::3]}')
print (f'{Array_Gen3[1, :2]}')
print (f'{Array_Gen3[1, 2:]}')
print (f'{Array_Gen3[:, 2]}')
print (f'{Array_Gen3[1, 2:3]}')
print (f'{Array_Gen3[1, 0:None]}')
print (f'{Array_Gen3[1, :]}')

print (f'-' * 20)

Set_Conjunto_Array = set({1, 2, 3})
Tupla_Array = tuple(('Uno', 'Dos'))
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Num3 = np.full(shape=(2, 1), fill_value=Set_Conjunto_Array)
Array_Num4 = np.full(shape=(3, 2), fill_value=Tupla_Array)
Array_Num5 = np.full(shape=(4, 1), fill_value=Diccionario_Array["Nombre"][2])

print (f'-' * 20)

print (f'{Array_Num3}')
print (f'{Array_Num3.ndim}')
print (f'{Array_Num3.shape}')
print (f'{Array_Num3.size}')
print (f'{Array_Num3.dtype}')

print (f'-' * 20)

print (f'{Array_Num4}')
print (f'{Array_Num4.ndim}')
print (f'{Array_Num4.shape}')
print (f'{Array_Num4.size}')
print (f'{Array_Num4.dtype}')
print (f'{Array_Num4[2, 0]}')

print (f'-' * 20)

print (f'{Array_Num5}')
print (f'{Array_Num5.ndim}')
print (f'{Array_Num5.shape}')
print (f'{Array_Num5.size}')
print (f'{Array_Num5.dtype}')
print (f'{Array_Num5[3, 0]}')

print (f'-' * 20)

print (f'{Array_Num5[3]}')

print (f'-' * 20)

Array_Num6 = np.arange(start=1, stop=6, step=1) #type: ignore
Array_Num7 = np.arange(start=2, stop=11, step=2) #type: ignore
Array_Num8 = np.arange(start=3, stop=31, step=3) #type: ignore
Array_Num9 = np.arange(start=10, stop=21, step=2) #type: ignore
Array_Num10 = np.arange(10) #type: ignore

print (f'{Array_Num6}')
print (f'{Array_Num7}')
print (f'{Array_Num8}')
print (f'{Array_Num9}')
print (f'{Array_Num10}')

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

print (f'Sumita: {Sumita9}')
print (f'Sumita: {Sumita10}')
print (f'Sumita: {Sumita11}')
print (f'Sumita: {Sumita12}')

print (f'-' * 20)

Arr1 = np.array([8, 9, 14])
Arr2 = np.array([2, 3, 7])

Sum = Arr1 + Arr2
Rest = Arr1 - Arr2
Mult = Arr1 * Arr2
Div = Arr1 / Arr2
Array_Random1_Cien = Array_Random1 + 100

print (f'Resultado: {Sum}')
print (f'Resultado: {Rest}')
print (f'Resultado: {Mult}')
print (f'Resultado: {Div}')
print (f'Resultado: {Array_Random1_Cien}')

print (f'-' * 20)

Array_Random3 = np.random.randint(low=1, high=10, size=(20))

print (f'{Array_Random3}')

print (f'-' * 20)

Array_Random3_Reshape = np.reshape(Array_Random3, shape=(4, 5))

print (f'{Array_Random3_Reshape}')

print (f'-' * 20)

Array_Random3_Reshape_Ravel = np.ravel(Array_Random3_Reshape)

print (f'{Array_Random3_Reshape_Ravel}')

print (f'-' * 20)

Array_Num11 = np.arange(start=1, stop=11, step=1) #type: ignore

print (f'{Array_Num11}')

print (f'-' * 20)

Lista_Array = [1, 2, 3, 4, 5]

Array_Num12 = np.array(Lista_Array)

print (f'{Lista_Array}')
print (f'{type(Lista_Array)}')
print (f'{Array_Num12}')
print (f'{type(Array_Num12)}')

print (f'-' * 20)

Array5 = np.array([1, 2, 3])
Array6 = np.arange(start=4, stop=7, step=1) #type: ignore

Array_Concatenate = np.concatenate([Array5, Array6])

print (f'{Array_Concatenate}')

print (f'-' * 20)

Array_Concatenate_splitted1 = np.split(Array_Concatenate, 1)
Array_Concatenate_splitted2 = np.split(Array_Concatenate, 2)
Array_Concatenate_splitted3 = np.split(Array_Concatenate, 3)
Array_Concatenate_splitted4 = np.split(Array_Concatenate, 6)

print (f'{Array_Concatenate_splitted1[0]}')

print (f'-' * 20)

print (f'{Array_Concatenate_splitted2[0]}')
print (f'{Array_Concatenate_splitted2[1]}')

print (f'-' * 20)

print (f'{Array_Concatenate_splitted3[0]}')
print (f'{Array_Concatenate_splitted3[1]}')
print (f'{Array_Concatenate_splitted3[2]}')

print (f'-' * 20)

print (f'{Array_Concatenate_splitted4[0]}')
print (f'{Array_Concatenate_splitted4[1]}')
print (f'{Array_Concatenate_splitted4[2]}')
print (f'{Array_Concatenate_splitted4[3]}')
print (f'{Array_Concatenate_splitted4[4]}')
print (f'{Array_Concatenate_splitted4[5]}')

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

Array_Random4 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random4}')

print (f'-' * 20)

Lista_Sorteo = list(['Erick', 'Josue', 'Karlita'])
Lista_Sorteo.append('Carmelo')
Lista_Sorteo.insert(1, 'Susanita')
Lista_Sorteo.extend(['Roxana'])

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
        yield f'El eleemnto es {elemento}'

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
            yield f'EL NUMERO ES PAR'
        else:
            yield f'EL NUMERO ES IMPAR'

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
    for elemento in range(5):
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
    print (f'Fin del experimento')

print (f'-' * 20)

Lista_Ejemplo13 = list([1, 2, 3, 4, 5])

def Ejercicio31(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        while (Contador < len(Lista)):
            Contador += 1
            
    return Contador

Exercise31 = Ejercicio31(Lista_Ejemplo13)

if (Exercise31 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La cantidad de numeros de la lista es {Exercise31}')
    
print (f'-' * 20)

def Ejercicio32(Lista):
    Acumulador = 0
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador += elemento
        else:
            continue
        
    if (Acumulador > 0):
        return Acumulador
    else:
        return None

Exercise32 = Ejercicio32(Lista_Ejemplo13)

if (len(Lista_Ejemplo13) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Exercise32 is None):
        print (f'No hay numeros pares en la lista')
    else:
        print (f'La suma de los numeros pares de la lista es {Exercise32}')
        
print (f'-' * 20)

def Ejercicio33(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        
        for elemento in Lista:
            Acumulador += elemento
            
        return Acumulador

Exercise33 = Ejercicio33(Lista_Ejemplo13)

if (Exercise33 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La suma de todos los numeros de la lista es {Exercise33}')
    
print (f'-' * 20)

def Ejercicio34(Lista, Numero):
    Founder = False

    for elemento in Lista:
        if (elemento == Numero):
            Founder = True
            break
        else:
            continue
        
    if (Founder == True):
        return Founder
    else:
        return None

Numerito7 = 5

Exercise34 = Ejercicio34(Lista_Ejemplo13, Numerito7)

if (len(Lista_Ejemplo13) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Exercise34 is None):
        print (f'El numero buscado no se encuentra en la lista')
    else:
        print (f'El numero {Numerito7} fue encontrado en la lista')
        
print (f'-' * 20)

def Ejercicio35(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Menore = min(Lista)
        Mayore = max(Lista)
        
        Lista_Resultado = [Menore, Mayore]
        return Lista_Resultado

Exercise35 = Ejercicio35(Lista_Ejemplo13)

if (len(Lista_Ejemplo13) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de la lista es {min(Exercise35)}') #type: ignore
    print (f'El mayor de la lista es {max(Exercise35)}') #type: ignore
    
print (f'-' * 20)

def Ejercicio36(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Menore = min(Lista)
        Mayore = max(Lista)
        
        return Menore, Mayore

Exercise36 = Ejercicio36(Lista_Ejemplo13)

if (len(Lista_Ejemplo13) == 0):
    print (f'Error, la lista esta vacia')
else:
    Menor2, Mayor2 = Exercise36 #type: ignore
    
    print (f'El menor de la lista es {Menor2}')
    print (f'El mayor de la lista es {Mayor2}')
    
print (f'-' * 20)

def Ejercicio37(Lista, Numero):
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

Numerito8 = 2

Exercise37 = Ejercicio37(Lista_Ejemplo13, Numerito8)

if (Exercise37 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Exercise37 == 0):
        print (f'Error, no hay ningun numero mayor que {Numerito8} en la lista')
    else:
        print (f'La cantidad de numeros mayores a {Numerito8} en la lista es {Exercise37}')
        
print (f'-' * 20)

def Ejercicio38(Lista):
    Lista_Pares = []
    Lista_Impares = list([])
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            Lista_Impares.extend([elemento])

    return Lista_Pares, Lista_Impares

Exercise38 = Ejercicio38(Lista_Ejemplo13)

if (len(Lista_Ejemplo13) == 0):
    print (f'Error, la lista esta vacia')
else:
    Pares2, Impares2 = Exercise38
    print (f'Lista Original: {Lista_Ejemplo13}')
    print (f'Lista Pares: {Pares2}')
    print (f'Lista Impares: {Impares2}')
    
print (f'-' * 20)

def Ejercicio39(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Mult = []
        
        for elemento in Lista:
            Lista_Mult.append(elemento * 2)
            
        return Lista_Mult

Exercise39 = Ejercicio39(Lista_Ejemplo13)

if (len(Lista_Ejemplo13) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Ejemplo13}')
    print (f'Lista Actualizada: {Exercise39}')
    
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

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\n Tu contrasena temporal es {PEPE.Contrasena(35)}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
print (f'-' * 20)
    
def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 3.5, 300, True)

print (f'{Funcion_Tupla("Perro", 3.5, 300, True)}')
print (f'{Variable_Funcion_Tupla[2]}')
print (f'{Funcion_Tupla("Perro", 3.5, 300, True)[3]}')
print (f'{type(Funcion_Tupla("Perro", 3.5, 300, True))}')

print (f'-' * 20)

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs:
        print (f'{kwargs[elemento]}')
        
    print (f'-' * 20)
    
    for elemento in kwargs.items():
        print (f'{elemento[0]} -- {elemento[1]}')
        
    print (f'-' * 20)
    
    for elemento in kwargs.keys():
        print (f'{elemento}')
        
    print (f'-' * 20)
        
    for elemento in kwargs.keys():
        print (f'{elemento}')
        
Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = 37, Votante = not True)

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la operacion es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

if (PEPE.Any_Par == True):
    print (f'Los numeros pares de la lista son {list(Anonima3)}')
    print (f'Los numeros pares de la lista son {PEPE.Lista_Par}')
else:
    print (f'Error, no hay numeros pares en la lista')
    
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
    def Interna(Apellido:str) -> str:
        return f'Mi nombre es {Nombre} {Apellido}'
    
    return Interna("PEREZ GUTIERREZ")

print (f'{Externa("ERICK JOSUE")}')

print (f'-' * 20)

def Closure_Externo():
    Lista_Closure = list([])
    def Closure_Interno(x):
        Lista_Closure.append(x)
        
        return Lista_Closure
    
    return Closure_Interno

Variable_Closure = Closure_Externo()

print (f'{Variable_Closure(12)}')
print (f'{Variable_Closure(24)}')
print (f'{Variable_Closure(39)}')

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
        Anonima = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Impares = [num for num in Lista if num % 2 != 0]
        
        print (f'Los numeros impares de la lista son {list(Anonima)}')
        print (f'Los numeros impares de la lista son {Lista_Impares}')
    else:
        print (f'Error, no hay numeros impares en la lista')

Filtrador(PEPE.Lista_Numeros)

print (f'-' * 20)

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

print (f'-' * 20)

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonathan'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)
        
    return Tercera

@Primera
def Usuario2(Nombre, Apellido):
    print (f'Mi nombre es {Nombre} {Apellido}')
    
Usuario2("Erick", "Perez")

print (f'-' * 20)

from Module_Own import Pokemon2 as Poke2

Objeto24 = Poke2(Objeto9.Nombre, 'Electrico', 'Impact Trueno')
Objeto25 = Poke2(Objeto10.Nombre, 'Roca', Objeto10.Ataque)

Objeto24.Mostrar()

print (f'-' * 20)

Objeto25.Mostrar()

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto26 = Poke_Kid2(Objeto11.Nombre, 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto26)
Objeto26.Mostrar()

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
        
Objeto27 = Smartphone()

Objeto27.Encender_Smartphone()
Objeto27.Reproducir_Musica()
Objeto27.Tomar_Fotografia()

print (f'-' * 20)

class Veterinaria2():
    def __init__(self, Nombre, Peso, Edad):
        self.Nombre = Nombre
        self.Peso = Peso
        self.Edad = Edad

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Peso: {self.Peso}kgs')
        print (f'Edad: {self.Edad} años')
        
class Perro2(Veterinaria2):
    def __init__(self, Nombre, Peso, Edad, Raza, Padecimiento):
        super().__init__(Nombre, Peso, Edad)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        
    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        
Objeto28 = Perro2('Chester', 2.8, 5, 'Poodle', 'Hipertension')

Veterinaria2.Mostrar(Objeto28)
Objeto28.Mostrar()

print (f'-' * 20)

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Peso, Edad, Color, Paciente):
        super().__init__(Nombre, Peso, Edad)
        self.Color = Color
        self.Paciente = Paciente

    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto29 = Gato2('Messi', 1.8, 1.5, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto29)
Objeto29.Mostrar()

print (f'-' * 20)

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Peso, Edad, Especie, Habla):
        super().__init__(Nombre, Peso, Edad)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto30 = Pajaro2('Polly', 0.4, 31, 'Guacamaya', 'Si')

Veterinaria2.Mostrar(Objeto30)
Objeto30.Mostrar()

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
        
Objeto31 = Paladin2(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto31.Mostrar()
Atacante2.Mostrar(Objeto31)
Defensor2.Mostrar(Objeto31)

print (f'-' * 20)

Hija_Padre1 = issubclass(Poke_Kid2, Poke2)
Hija_Padre2 = issubclass(Poke_Kid2, Poke1)

print (f'{Hija_Padre1}')
print (f'{Hija_Padre2}')

Instancia1 = isinstance(Objeto31, Paladin2)
Instancia2 = isinstance(Objeto31, Atacante2)
Instancia3 = isinstance(Objeto31, Defensor2)
Instancia4 = isinstance(Objeto31, Atacante)

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
        
Objeto32 = D2()

A2.Mostrar(Objeto32)
B2.Mostrar(Objeto32)
C2.Mostrar(Objeto32)
Objeto32.Mostrar()
E2.Mostrar(Objeto32)

print (f'-' * 20)

class Efectivo2():
    def Pagar(self):
        print (f'El pago se realizo con Efectivo')
        
class Tarjeta2():
    def Pagar(self):
        print (f'El pago se realizo con Tarjeta')
        
class Cripto2():
    def Pagar(self):
        print (f'El pago se realizo con Cripto')
        
Objeto33 = Cripto2()
Objeto34 = Tarjeta2()
Objeto35 = Efectivo2()

Objeto33.Pagar()
Objeto34.Pagar()
Objeto35.Pagar()

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
        print (f'Buenos dias, tu saldo a la fecha es de ${self.__Saldo}')
        
Objeto34 = Cuenta_Bancaria2(125)
Objeto34.Depositar(25)
Objeto34.Mostrar()

print (f'Tu saldo privado es {Objeto34.Dinero}')

Objeto34.Dinero = '50,000,000'

Objeto34.Mostrar()

print (f'Tu saldo privado es {Objeto34.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla2(Plantilla2):
    def Mostrar(self):
        print (f'Metodo interno')
        
    def General(self):
        print (f'Este metodo pertenece a la plantilla y es mandatorio')
        
Objeto35 = Sub_Plantilla2()

Objeto35.Mostrar()
Objeto35.General()

print (f'-' * 20)

class Bulbasaur():
    def Elegir(self):
        return f'Bulbasaur'
    
class Charmander():
    def Elegir(self):
        return f'Charmander'
    
class Squirtle():
    def Elegir(self):
        return f'Squirtle'
    
class Battle1():
    def __init__(self):
        self.Favorito = Bulbasaur()
        
    def Batallar(self):
        print (f'Felicidades, tu inicial es un {self.Favorito.Elegir()}')
        
Objeto36 = Battle1()

Objeto36.Batallar()

print (f'-' * 20)

class Battle2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'Felicidades, tu inicial es un {self.Favorito.Elegir()}')
        
Criatura1 = Bulbasaur()
Objeto36 = Battle2(Criatura1)
Objeto36.Batallar()

Criatura2 = Charmander()
Objeto37 = Battle2(Criatura2)
Objeto37.Batallar()

Criatura3 = Squirtle()
Objeto38 = Battle2(Criatura3)
Objeto38.Batallar()

print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un
Long
String'''

variable4 = Objeto9.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = True, Objeto11.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esta es una concatenacion simple {PEPE.Diccionario_Poke["Poke3"]}')

print (f'Mi nombre es {Lista_Uno[0]} {variable2}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Variable_Sumatoria}, {Sumatoria2(1, 2, 3, 4, 5)} o incluso {Objeto10.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Erick'in Lista_Uno)
print (f'Gary' not in PEPE.Tupla_Poke)
print (f'{PEPE.Diccionario_Poke["Poke1"]}' in PEPE.Set_Conjunto_Poke1)

print (f'-' * 20)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es un desempaquetado de variables y snake case declaracion al mismo tiempo {snake_case2}')

print (f'Mi lista 1 tiene {Lista_Uno.__len__()} elementos')

Lista_Uno.append("Coco Rayado")
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Cociente, Residuo = divmod(Objeto11.Cantidad, Sumatoria2(1, 2, 3, 1))

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

print (f'{Lista_Uno[2]} eso que esta ahi es un {PEPE.Lista2[PEPE.Lista2.index("Koala")]}?')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, 200, Anonima1(50, 2))

print (f'{Lista_Cuatro}')

del Lista_Uno[1]
Lista_Uno.remove('Coco Rayado')
Lista_Uno.pop(-2)
Lista_Uno.pop(-1)
Lista_Uno.pop(-1)

Lista_Uno_Copia = Lista_Uno.copy()

print (f'{Lista_Uno}')
print (f'La lista 1 tiene {len(Lista_Uno)} elementos')

Lista_Uno.clear()

print (f'{Lista_Uno}')
print (f'{Lista_Uno_Copia}')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'{dir(PEPE)}')

Tupla1 = ('Rojo', 'Negro', 'Negro', 'Negro', 'Negro', 'Negro', 'Negro', 'Negro', 'Negro')

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Black', 'White'))

print (f'{Tupla1}')

Tupla2 = 'Erick', 'Josue', 'Karlita',

Tupla3 = 'Erick',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Variable_Funcion_Tupla)}')

print (f'{Tupla1[1]}')

Set_Conjunto1 = {'Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde'}
Set_Conjunto1.add('Azul')

Set_Conjunto2 = set({'Amarillo'})

Set_Conjunto1.update(Set_Conjunto2)

print (f'{Set_Conjunto1}')

Set_Conjunto2 = set({'Red', 'Green', 'Blue', 'Yellow'})

print (f'{Set_Conjunto2}')

Set_Conjunto3 = {1, 2, 3, 4, 5}
Set_Conjunto4 = {4, 5}
Set_Conjunto5 = set({8})

print (f'{Set_Conjunto3.issuperset(Set_Conjunto4)}')
print (f'{Set_Conjunto3 >= Set_Conjunto4}')

print (f'{Set_Conjunto4.issubset(Set_Conjunto3)}')
print (f'{Set_Conjunto4 <= Set_Conjunto3}')

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

Set_Conjunto_Menu2 = frozenset({'Caramelo'})

Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, 'Pastel'})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario2 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Objeto9.Cantidad,
    'Votante' : Variable_Funcion_Tupla[3]
}

Diccionario3 = {
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, Anonima2(10), 6],
    'Votante' : [True, not False, False]
}

Diccionario4 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

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

Diccionario2['Nombre'] = variable1

print (f'{Diccionario2}')

Diccionario2_Copia = Diccionario2.copy()

del Diccionario2['Nombre']
Diccionario2.pop("Edad")

print (f'{Diccionario2}')

Diccionario2.clear()

print (f'{Diccionario2}')
print (f'{Diccionario2_Copia}')

print (f'-' * 20)

Diccionario2 = dict({1 : "Karlita", 2 : 6, 3 : False})

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2.values()}')
print (f'{Diccionario2.items()}')
print (f'{Diccionario2[1]}')
print (f'{Diccionario2.get(2)}')

print (f'-' * 20)

print (f'{Diccionario2.get(1)} no puede votar ya que solo tiene {Diccionario3["Edad"][2]} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', f'{PEPE.Diccionario_Poke["Poke1"]}')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2["Dos"] = Objeto11.Nombre

print (f'{Diccionario_Vacio1}')
print (f'{Diccionario_Vacio1.keys()}')
print (f'{Diccionario_Vacio1.values()}')
print (f'{Diccionario_Vacio1.items()}')
print (f'{Diccionario_Vacio1["B"]}')
print (f'{Diccionario_Vacio1.get("C")}')

print (f'-' * 20)

print (f'{Diccionario_Vacio2}')
print (f'{Diccionario_Vacio2.keys()}')
print (f'{Diccionario_Vacio2.values()}')
print (f'{Diccionario_Vacio2.items()}')
print (f'{Diccionario_Vacio2["Uno"]}')
print (f'{Diccionario_Vacio2.get("Dos")}')

print (f'-' * 20)

Key2 = [f'Key{i}' for i in range(len(Lista_Uno_Copia))]

print (f'{Key2}')

Diccionario5 = dict(zip(Key2, Lista_Uno_Copia))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key2"]}')
print (f'{Diccionario5.get("Key3")}')

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
    exit()
    
Cargar_Csv3['TOTALITO'] = Cargar_Csv3['quantity'] * Cargar_Csv3['price']
    
Encontrado3 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech3_Formateada.date()]

if (Encontrado3.empty):
    print (f'No se han encontrado ventas en esta fecha')
else:
    print (f'Genial! se han encontrado ventas en esta fecha')
    
    Grupo4 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo4_Min = Grupo4.idxmin()
    Grupo4_Max = Grupo4.idxmax()
    Grupo4_Min_Cant = Grupo4.min()
    Grupo4_Max_Cant = Grupo4.max()
    
    print (f'En esta fecha {Fech3_Formateada} el producto que vendio menos fue {Grupo4_Min} con una cantidad de {Grupo4_Min_Cant} unidades')
    print (f'En esta fecha {Fech3_Formateada} el producto que vendio mas fue {Grupo4_Max} con una cantidad de {Grupo4_Max_Cant} unidades')
    
    print (f'El total de unidades vendidas en esta fecha fue de {Grupo4.sum()}')
    print (f'La cantidad de clientes que nos compraron fue de {Grupo4.count()}')
    
    Grupo5 = Encontrado3.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue de ${Grupo5.sum()}')
    
    Promedio2 = Grupo5.sum() / Grupo4.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio2, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${Grupo5.mean()}')
    
print (f'-' * 20)

print (f'{Cargar_Csv3}')

Set_Conjunto_Csv3 = list(Cargar_Csv3['product'])

Lista_Csv3 = list(Set_Conjunto_Csv3)

Key3 = [f'Key{i}' for i in range(len(Lista_Csv3))]

Diccionario6 = dict(zip(Key3, Lista_Csv3))

print (f'-' * 20)

print (f'{Diccionario6}')
print (f'{Diccionario6.keys()}')
print (f'{Diccionario6.values()}')
print (f'{Diccionario6.items()}')
print (f'{Diccionario6["Key2"]}')
print (f'{Diccionario6.get("Key3")}')

print (f'-' * 20)

Division_Baja = 14 // 7
Exponente = 2 ** 3
Modulo = 20 % 6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'-' * 20)

print (f'El tipo de la variable es {type(variable1)}')
print (f'El tipo de la variable es {type(variable4)}')
print (f'El tipo de la variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de la variable es {type(variable6)}')
print (f'El tipo de la variable es {type(Lista_Ejemplo10)}')
print (f'El tipo de la variable es {type(Tupla3)}')
print (f'El tipo de la variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de la variable es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de la variable es {type(Diccionario_Vacio1)}')
print (f'El tipo de la variable es {type(Objeto11)}')
print (f'El tipo de la variable es {type(Funcion_Diccionario)}')
print (f'El tipo de la variable es {type(Data_Frame_Concatenate)}')
print (f'El tipo de la variable es {type(Array0)}')
print (f'El tipo de la variable es {type(PEPE)}')

if (Diccionario4['Ingresos'] > 500): #type: ignore
    if (Diccionario4['Gastos'] < 200): #type: ignore
        print (f'Ingresos Altos, Gastos Bajos')
    elif (Diccionario4['Gastos'] == 200): #type: ignore
        print (f'Ingresos Altos, Gastos Al Limite')
    elif (Diccionario4['Gastos'] > 200): #type: ignore
        print (f'Ingresos Altos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario4['Ingresos'] == 500): #type: ignore
    if (Diccionario4['Gastos'] < 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Bajos')
    elif (Diccionario4['Gastos'] == 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Al Limite')
    elif (Diccionario4['Gastos'] > 200): #type: ignore
        print (f'Ingresos Minimos, Gastos Altos')
    else:
        print (f'Error de codigo')
elif (Diccionario4['Ingresos'] < 500): #type: ignore
    if (Diccionario4['Gastos'] < 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Bajos')
    elif (Diccionario4['Gastos'] == 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Al Limite')
    elif (Diccionario4['Gastos'] > 200): #type: ignore
        print (f'Ingresos Bajos, Gastos Altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')
    
print (f'-' * 20)

variable8 = 'este es un texto cualquiera para ver si esto funciona o no'

Lista_variable8 = variable8.split(' ')

print (f'La cantidad de palabras digitadas es {len(Lista_variable8)}')

variable9, variable10 = '3', 20

if (variable9.isalpha() and variable10 > 30):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')
    
print (f'-' * 20)
    
if (variable9.isalpha() or variable10 > 30):
    print (f'Al menos una de las condiciones se cumple')
else:
    print (f'Error, ninguna de las condiciones se cumple')
    
print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Sumatoria2(1, 2, 3, 4, 5)
        self.Classified = True

    def Desplegar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')
        
Objeto39 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Ash")], 'Kanto', Objeto9.Nombre)
Objeto40 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Brooke")], 'Paldea', Objeto10.Nombre)
Objeto41 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")], 'Alolah', Objeto11.Nombre)

Objeto39.Desplegar()
Objeto40.Desplegar()
Objeto41.Desplegar()

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

if (bool(Diccionario4['Vacio'] == True)):
    print (f'Gracias por la informacion')
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
    print (f'{indice} -- {elemento}')
    
print (f'-' * 20)

variable11 = 'eSteBAN'
variable11_letra = variable11[0]

print (f'{variable11}')
print (f'{variable11.lower()}')
print (f'{variable11.upper()}')
print (f'{variable11.capitalize()}')

print (f'{variable11.lower().find("t")}')
print (f'{variable11.lower().index("n")}')

print (f'La letra {variable11_letra} aparece un total de {variable11.lower().count(variable11_letra)} veces')

print (f'{variable11.lower().startswith(variable11_letra)}')
print (f'{variable11.lower().endswith("n")}')

print (f'{variable11.lower().replace("ban", "POPOTAMO")}')

print (f'-' * 20)

var6 = 'erick'

if (isinstance(var6, (str))):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Error, lo que ingresaste no es texto')
    
if (var6.isalpha()):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Error, lo que ingresaste no es texto')
    
try:
    Numerito9 = float(var6)
    if (Numerito9.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Lo que ingresaste es texto')
    
print (f'-' * 20)

var7 = 3.5

if (isinstance(var7, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, lo que ingresaste no es un numero decimal')
    
try:
    Numerito10 = float(var7)
    if (Numerito10.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var8 = '3'

if (isinstance(var8, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')
    
if (var8.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Error, lo que ingresaste no es un numero entero')
    
try:
    Numerito11 = float(var8)
    if (Numerito11.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var9 = 3

if (isinstance(var9, (int, float))):
    print (f'Lo que ingresaste puede ser entero o decimal')
else:
    print (f'Error, lo que ingresaste no es un numero')
    
try:
    Numerito12 = float(var9)
    if (Numerito12.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

var10 = 'erick123'

if (isinstance(var10, (str, int))):
    print (f'Numero entero o cadena de caracteres')
else:
    print (f'Error de formato')
    
if (var10.isalnum()):
    print (f'Numero entero o cadena de caracteres')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var11 = '      e       '

if (var11.isspace()):
    print (f'Esta mica esta compuesta unicamente por espacios')
else:
    print (f'Error, hay mas que solo espacios en esta mica')
    
print (f'-' * 20)

var12 = 'eSteBAN'

if (var12.lower().islower()):
    print (f'Esto esta compuesto unicamente por letras en minuscula')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

if (var12.upper().isupper()):
    print (f'Esto esta compuesto unicamente por letras en mayusculas')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var13 = ' '

if (bool(var13) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error, esto esta vacio')
    
print (f'-' * 20)

print (f'En la tupla {PEPE.Tupla_Poke}, el elemento {PEPE.Tupla_Poke[1]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Brooke")}')

Eliminado = Lista_Uno_Copia.pop(-2)

print (f'El elemento eliminado fue: {Eliminado}')
print (f'Lista Actualizada: {Lista_Uno_Copia}')

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'El numero {PEPE.Lista_Numeros[Contador]} multiplicado por 100 es {PEPE.Lista_Numeros[Contador] * 100}')
    Contador += 1
    
Lista_Animales = list([PEPE.Lista2[2]])
Lista_Animales.append('Hormiga')
Lista_Animales.insert(2, 'Ballena')
Lista_Animales.extend(['Leon'])

print (f'{Lista_Animales}')

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Ballena'):
        print (f'La ballena vive en el mar')
        break
    else:
        Contador += 1
        continue
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Animales, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento1, elemento2, elemento3, elemento4 in zip(Lista_Animales, Set_Conjunto_Menu1, PEPE.Set_Conjunto_Poke1, Lista_Uno_Copia):
    print (f'{elemento1} -- {elemento2} -- {elemento3} -- {elemento4}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(len(PEPE.Set_Conjunto_Poke1)):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
Lista_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'Lista original: {PEPE.Lista_Numeros}')
print (f'Lista multiplicada: {Lista_Mult}')

Contador = 0

while (Contador < 5):
    print (f'El contador es {Contador + 1}')
    Contador += 1
    
print (f'-' * 20)

Menor3 = min(Lista_Mult)
Mayor3 = max(Lista_Mult)

Redondeo = round(14.458795, 2)

Sumatoria4 = sum(Lista_Mult)

print (f'El numero menor de la lista es {Menor3}')
print (f'El numero mayor de la lista es {Mayor3}')
print (f'El redondeo del numero 14.458795 es {Redondeo}')
print (f'La sumatoria de todos los numeros de la lista es {Sumatoria4}')

print (f'{bool(not True)}')
print (f'{bool(False)}')
print (f'{bool(0)}')
print (f'{bool(None)}')
print (f'{bool("")}')

print (f'-' * 20)

Todo_All = all([Lista_Mult, Set_Conjunto1, Diccionario2_Copia, 0])

print (f'{Todo_All}')

print (f'-' * 20)

Uno = int("500")
Dos = str(500)
Tres = float(Uno)
Cuatro = list(PEPE.Set_Conjunto_Poke1)
Cinco = set(PEPE.Tupla_Poke)
Seis = tuple(Lista_Animales)

print (f'{type("500")} -- {type(Uno)}')
print (f'{type(500)} -- {type(Dos)}')
print (f'{type(Uno)} -- {type(Tres)}')
print (f'{type(PEPE.Set_Conjunto_Poke1)} -- {type(Cuatro)}')
print (f'{type(PEPE.Tupla_Poke)} -- {type(Cinco)}')
print (f'{type(Lista_Animales)} -- {type(Seis)}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto_Poke1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

print (f'-' * 20)

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

'''print (f'-' * 20)

def Exception_Finale():
    while True:
        Numerito = input(f'Ingrese un numero: ')
        try:
            Numerito1 = float(Numerito)
            if (Numerito1.is_integer()):
                print (f'Lo que ingresaste fue un numero entero')
                break
            else:
                print (f'Lo que ingresaste fue un numero decimal')
                break
        except ValueError:
            print (f'Error, necesito que lo que ingreses sea un numero')

Exception_Finale()'''

print (f'-' * 20)

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

Texto10 = 'ericksuper80@hotmail.com'

Pattern15 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|org|net)$'

Buscar19 = bool(re.fullmatch(Pattern15, Texto10))

if (Buscar19 == True):
    print (f'El correo electronico tiene el formato correcto')
else:
    print (f'Error, el correo tiene un formato invalido')
    
print (f'-' * 20)

Texto11 = '32'

import re

Pattern15 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar20 = bool(re.match(Pattern15, Texto11))

if (Buscar20 == True):
    print (f'El numero se encuentra entre 01 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

class Persona2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
        
Objeto42 = Persona2("Erick Perez")

print (f'Hola, mi nombre es {Objeto42}')

print (f'-' * 20)

class Colores2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Colores2 = [
    Colores2('Rojo'),
    Colores2('Azul'),
    Colores2('Verde')
]

print (f'Lista de colores: {Lista_Colores2}')

print (f'-' * 20)

class Inventario2():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto43 = Inventario2()

Objeto43.Productos.append('Guanabana')
Objeto43.Productos.insert(1, 'Fresa')
Objeto43.Productos.extend(['Manzana'])

print (f'Mi lista tiene {len(Objeto43)} elementos')

print (f'-' * 20)

class Igualdad2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto44 = Igualdad2("Panda Rojo")
Objeto45 = Igualdad2("Panda Rojo")

if (Objeto44 == Objeto45):
    print (f'Ambos objetos son iguales')
else:
    print (f'Erorr, los objetos no son iguales')
    
print (f'-' * 20)

class Caja3():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso

Objeto46 = Caja3(5)
Objeto47 = Caja3(3)

print (f'El resultado de la operacion es {Objeto46 + Objeto47}')

print (f'-' * 20)

class Armario():
    def __init__(self):
        self.Ropa = list([
            'Camisa',
            'Medias',
            'Pantalon',
            'Abrigo'
        ])
        
    def __getitem__(self, Indice):
        return self.Ropa[Indice]
        
Objeto48 = Armario()

print (f'El elemento en la posicion 0 es {Objeto48[0]}')
print (f'El elemento en la posicion 1 es {Objeto48[1]}')
print (f'El elemento en la posicion 2 es {Objeto48[2]}')
print (f'El elemento en la posicion 3 es {Objeto48[3]}')

print (f'-' * 20)

class Panaderia2():
    def __init__(self):
        self.Panes = [
            'Baguette',
            'Croissant',
            'Pan Dulce'
        ]
        
    def __iter__(self):
        return iter(self.Panes)
        
Objeto49 = Panaderia2()

for elemento in Objeto49:
    print (f'{elemento}')
    
print (f'-' * 20)

Productos6 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def buscar_producto_mas_barato(Diccionario):
    if (len(Diccionario) == 0):
        return None
    else:
        Nombre = next(iter(Diccionario))
        Precio = Diccionario[Nombre]
        
        for indice, elemento in Diccionario.items():
            if (elemento < Precio):
                Nombre = indice
                Precio = elemento
            else:
                continue
            
        return Nombre, Precio

Exercise40 = buscar_producto_mas_barato(Productos6)

if (Exercise40 is None):
    print (f'Error, el diccionario esta vacio')
else:
    Nombre_Prod, Precio_Prod = Exercise40
    
    print (f'Nombre del producto: {Nombre_Prod}')
    print (f'Precio del producto: ${Precio_Prod}')