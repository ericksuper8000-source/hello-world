try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado es incorrecto')
    raise

Lista_Elementos1 = list([1, 2, 3, 4, 5])

def Ejercicio1(Lista):
    Contador = 0
    
    while (Contador < len(Lista)):
        Contador += 1
        
    return Contador

if (len(Lista_Elementos1) == 0):
    print (f'Error, la lista seleccionada esta vacia')
else:
    Resultado1 = Ejercicio1(Lista_Elementos1)
    
    print (f'La lista 1 tiene {Resultado1} elementos')
    
print (f'-' * 20)

def Ejercicio2(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        
        for elemento in Lista:
            if (elemento % 2 == 0):
                Contador += 1
            else:
                continue
            
    return Contador

Resultado2 = Ejercicio2(Lista_Elementos1)

if (Resultado2 is None):
    print (f'Error, la lista esta vacia')
else:
    Contador_Pares = Resultado2
    
    print (f'La cantidad de numeros pares en la lista es {Contador_Pares}')
    
print (f'-' * 20)

def Ejercicio3(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        
        for elemento in Lista:
            Acumulador += elemento
            
    return Acumulador

Resultado3 = Ejercicio3(Lista_Elementos1)

if (Resultado3 is None):
    print (f'Error, la lista esta vacia')
else:
    Total = Resultado3
    
    print (f'El resultado de la sumatoria de los elementos de la lista es {Total}')
    
print (f'-' * 20)

def Ejercicio4(Lista, Numero):
    Founder = False

    for elemento in Lista:
        if (elemento == Numero):
            Founder = True
            break
        else:
            continue
        
    return Founder

Resultado4 = Ejercicio4(Lista_Elementos1, 4)

if (len(Lista_Elementos1) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado4 == True):
        print (f'El numero fue encontrado')
    else:
        print (f'Error, el numero no aparece en la lista')
        
print (f'-' * 20)

def Ejercicio5(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Menore = min(Lista)
        Mayore = max(Lista)
        
    return Menore, Mayore

Resultado4 = Ejercicio5(Lista_Elementos1)

if (Resultado4 is None):
    print (f'Error, la lista esta vacia')
else:
    Min, Max = Resultado4
    
    print (f'El menor de los numeros es {Min}')
    print (f'El mayor de los numeros es {Max}')
    
print (f'-' * 20)

def Ejercicio6(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    Lista_Resultado = [Menore, Mayore]
    
    return Lista_Resultado

Ejercicio6([1, 2, 3, 4, 5])

if (len([1, 2, 3, 4, 5]) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de los numeros de la lista es {min(Ejercicio6([1, 2, 3, 4, 5]))}')
    print (f'El menor de los numeros de la lista es {max(Ejercicio6([1, 2, 3, 4, 5]))}')
    
print (f'-' * 20)

def Ejercicio7(Lista, Numero):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        
        for elemento in Lista:
            if (elemento > Numero):
                Contador += 1
                
    return Contador

Resultado5 = Ejercicio7(Lista_Elementos1, 3)

if (Resultado5 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La cantidad de numeros en la lista mayores a 3 es {Resultado5}')

print (f'-' * 20)

def Ejercicio8(Lista):
    Lista_Pares = list([])
    
    for elemento in Lista:
        if (elemento % 2 == 0):
            Lista_Pares.append(elemento)
        else:
            continue
        
    return Lista_Pares

Resultado6 = Ejercicio8([1, 2, 3, 4, 5])

if (len([1, 2, 3, 4, 5]) == 0):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista de numeros pares es {Resultado6}')
    
print (f'-' * 20)

def Ejercicio9(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Impares = []
        for elemento in Lista:
            if (elemento % 2 != 0):
                Lista_Impares.extend([elemento])
            else:
                continue
            
    return Lista_Impares

Resultado7 = Ejercicio9(Lista_Elementos1)

if (Resultado7 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista de numeros impares es {Resultado7}')
    
print (f'-' * 20)

def Ejercicio10(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Mult = []
        for elemento in Lista:
            Lista_Mult.append(elemento * 2)
            
    return Lista_Mult

Resultado8 = Ejercicio10(Lista_Elementos1)

if (Resultado8 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'La lista original es {Lista_Elementos1}')
    print (f'La lista actualizada es {Resultado8}')
    
print (f'-' * 20)

'''Contador = 0

Lista_Promedios = list([])

while (Contador < 3):
    while True:
        Numerito1 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito2 = float(Numerito1)
            if (Numerito2.is_integer()):
                Lista_Promedios.append(Numerito2)
                break
            else:
                Lista_Promedios.append(Numerito2)
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador += 1
    
Promedio1 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas elegidas es {round(Promedio1, 2)}')'''

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
                
    return Lista_Pares, Lista_Impares

Resultado9 = Ejercicio11(Lista_Elementos1)

if (Resultado9 is None):
    print (f'Erro, la lista esta vacia')
else:
    Pares1, Impares1 = Resultado9
    
    print (f'Lista de Pares: {Pares1}')
    print (f'Lista de ImPares: {Impares1}')
    
print (f'-' * 20)

def Ejercicio12(Lista):
    if (len(Lista) == 0):
        return None
    else:
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

Resultado10 = Ejercicio12([5, -6, 0, -1, -3, 0])

if (Resultado10 is None):
    print (f'Error, la lista esta vacia')
else:
    Contador_Positivos, Contador_Negativos, Contador_Ceros = Resultado10
    
    print (f'Cantidad Positivos: {Contador_Positivos}')
    print (f'Cantidad Negativos: {Contador_Negativos}')
    print (f'Cantidad Ceros: {Contador_Ceros}')
    
print (f'-' * 20)

import re

Lista_Elementos2 = [
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
]

def Ejercicio13(Lista):
    Lista_Validos = []
    Lista_Invalidos = list([])
    
    Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|net|org)'
    
    for elemento in Lista:
        Buscar = bool(re.fullmatch(Pattern, elemento))
        if (Buscar == True):
            Lista_Validos.append(elemento)
        else:
            Lista_Invalidos.extend([elemento])
            
    return Lista_Validos, Lista_Invalidos

Resultado11 = Ejercicio13(Lista_Elementos2)

if (len(Lista_Elementos2) == 0):
    print (f'Error, la lista esta vacia')
else:
    Validos, Invalidos = Resultado11
    
    print (f'Correos que pasaron la validacion: {Validos}')
    print (f'Correos que no pasaron la validacion: {Invalidos}')
    
print (f'-' * 20)

def Ejercicio14(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Temporal = Lista[0]
        
        for elemento in Lista:
            if (Temporal < elemento):
                Temporal = elemento
            else:
                continue
            
    return Temporal

Resultado12 = Ejercicio14(Lista_Elementos1)

if (Resultado12 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El mayor de los numeros de la lista es {Resultado12}')
    
    
def Ejercicio15(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Temporal = Lista[0]
        
        for elemento in Lista:
            if (Temporal > elemento):
                Temporal = elemento
            else:
                continue
            
    return Temporal

Resultado13 = Ejercicio15(Lista_Elementos1)

if (Resultado13 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de los numeros de la lista es {Resultado13}')
    
print (f'-' * 20)

Lista_Elementos3 = [-15, -8, -3, -1, 0, 4, 7, 12, 19, 25]

def Ejercicio16(Lista):
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

Resultado14 = Ejercicio16(Lista_Elementos3)

if (Resultado14 is None):
    print (f'Error, la lista esta vacia')
else:
    Total_Positivos, Sumatoria_Positivos = Resultado14
    
    print (f'Total Numeros Positivos: {Total_Positivos}')
    print (f'Sumatoria Positivos: {Sumatoria_Positivos}')
    
print (f'-' * 20)

Lista_Elementos4 = [65, 70, 54, 80, 69, 66]

def Ejercicio17(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Aprobados = 0
        Reprobados = 0
        Total_Aprobados = 0
        
        for elemento in Lista:
            if (elemento >= 70):
                Aprobados += 1
                Total_Aprobados += elemento
            else:
                Reprobados += 1
                
    return Aprobados, Reprobados, Total_Aprobados

Resultado15 = Ejercicio17(Lista_Elementos4)

if (Resultado15 is None):
    print (f'Error, la lista esta vacia')
else:
    Contador_Aprobados, Contador_Reprobados, Total2 = Resultado15
    
    print (f'Estudiantes Aprobados: {Contador_Aprobados}')
    print (f'Estudiantes Reprobados: {Contador_Reprobados}')
    print (f'Sumatoria notas aprobadas: {Total2}')
    
print (f'-' * 20)

Lista_Elementos5 = [120, 0, 350, 80, 0, 40, 600]

def Ejercicio18(Lista):
    Ventas = 0
    No_Ventas = 0
    Total_Ventas = 0
    
    for elemento in Lista:
        if (elemento > 0):
            Ventas += 1
            Total_Ventas += elemento
        else:
            No_Ventas += 1
        
    return Ventas, No_Ventas, Total_Ventas

Resultado16 = Ejercicio18(Lista_Elementos5)

if (len(Lista_Elementos5) == 0):
    print (f'Error, la lista esta vacia')
else:
    Ventas_Registradas, Ventas_No_Registradas, Suma_Ventas = Resultado16
    
    print (f'Ventas registradas: {Ventas_Registradas}')
    print (f'Clientes que no compraron: {Ventas_No_Registradas}')
    print (f'Total Vendido: {Suma_Ventas}')
    
print (f'-' * 20)

Lista_Elementos6 = [28, 19, 33, 35, 30, 29, 33]

def Ejercicio19(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Mayor_Treinta = 0
        Suma_Mayor_Treinta = 0
        for elemento in Lista:
            if (elemento >= 30):
                Mayor_Treinta += 1
                Suma_Mayor_Treinta += elemento
                
    return Mayor_Treinta, Suma_Mayor_Treinta

Resultado17 = Ejercicio19(Lista_Elementos6)

if (Resultado17 is None):
    print (f'Error, la lista esta vacia')
else:
    Temperatura_Mayor_Treinta, Suma_Temperatura1 = Resultado17
    if (Temperatura_Mayor_Treinta >= 4):
        print (f'Días calurosos: {Temperatura_Mayor_Treinta}')
        print (f'Suma temperaturas: {Suma_Temperatura1}')
        print (f'Semana Calurosa, hubieron exactamente {Temperatura_Mayor_Treinta} dias con temperatura mayor a 30 grados')
    else:
        print (f'Días calurosos: {Temperatura_Mayor_Treinta}')
        print (f'Suma temperaturas: {Suma_Temperatura1}')
        print (f'Semana normal, la temperatura no estuvo muy alta')
        
print (f'-' * 20)

Lista_Elementos7 = [15, 0, 8, 2, 0, 25, 4]

def Ejercicio20(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Agotados = 0
        Low_Stock = 0
        High_Stock = 0
        Sum_Low_Stock = 0
        Sum_High_Stock = 0
        
        for elemento in Lista:
            if (elemento == 0):
                Agotados += 1
            elif (elemento >= 1 and elemento <= 5):
                Low_Stock += 1
                Sum_Low_Stock += elemento
            else:
                High_Stock += 1
                Sum_High_Stock += elemento
                
    return Agotados, Low_Stock, High_Stock, Sum_Low_Stock, Sum_High_Stock

Resultado18 = Ejercicio20(Lista_Elementos7)

if (Resultado18 is None):
    print (f'Error, la lista esta vacia')
else:
    Agotados, Stock_Bajo, Stock_Alto, Suma_Stock_Bajo, Suma_Stock_Alto = Resultado18
    
    print (f'Productos agotados en el inventario: {Agotados}')
    print (f'Productos con stock bajo: {Stock_Bajo}')
    print (f'Productos con stock alto: {Stock_Alto}')
    print (f'Total Prod Stock Bajo: {Suma_Stock_Bajo}')
    print (f'Total Prod Stock Alto: {Suma_Stock_Alto}')

print (f'-' * 20)

Lista_Elementos8 = [1200, 1001, 1500, 950, 2000, 700]

def Ejercicio21(Lista):
    Mas_Mil = 0
    Menos_Mil = 0
    Sumatoria = 0
    
    for elemento in Lista:
        if (elemento >= 1000):
            Mas_Mil += 1
            Sumatoria += elemento
        else:
            Menos_Mil += 1
        
    return Mas_Mil, Menos_Mil, Sumatoria

Resultado19 = Ejercicio21(Lista_Elementos8)

if (len(Lista_Elementos8) == 0):
    print (f'Error, la lista esta vacia')
else:
    Ganar_Mas_Mil, Ganar_Menos_Mil, Total_Mas_Mil = Resultado19
    
    print (f'Cantidad empleados que ganan mas de $1000: {Ganar_Mas_Mil}')
    print (f'Cantidad empleados que ganan menos de $1000: {Ganar_Menos_Mil}')
    print (f'Total de dinero que ganan los empleados que ganan mas de $1000: ${Total_Mas_Mil}')

print (f'-' * 20)

Lista_Elementos9 = [12, 8, 5, 0, 7, 0, 10]

def Ejercicio22(Lista):
    Indice = 0
    Contador = 0
    Founder = False
    
    while (Contador < len(Lista)):
        if (Lista[Contador] == 0):
            Indice = Contador
            Founder = True
            break
        else:
            Contador += 1
            continue
        
    if (Founder == True):
        return Indice
    else:
        return None

Resultado20 = Ejercicio22(Lista_Elementos9)

if (len(Lista_Elementos9) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Resultado20 is None):
        print (f'No hay ningun producto agotado')
    else:
        Indice = Resultado20
        print (f'El producto Agotado {Lista_Elementos9[Indice]} se encuentra en la posicion {Indice} de la lista')
        
print (f'-' * 20)

'''def Ejercicio23(Numero):
    Resultado = 38 * 12 + Numero
    print (f'El resultado de la operacion es {Resultado}')

Ejercicio23(PEPE.Flotante1)'''

'''Resultado21 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado21}')'''

'''def Ejercicio23(Cadena):
    Nombre = Cadena.replace(' ', '')
    if (isinstance(Nombre, (str))):
        print (f'Lo ingresado es un texto')
    else:
        print (f'Error, lo ingresado no es un texto')
        
    if (Nombre.isalpha()):
        print (f'Lo ingresado es un texto')
    else:
        print (f'Error, lo ingresado no es un texto')
        
    try:
        Numerito = float(Nombre)
        if (Numerito.is_integer()):
            print (f'Lo que ingresaste es un numero entero')
        else:
            print (f'Lo que ingresaste es un numero decimal')
    except ValueError:
        print (f'Lo que ingresaste es un texto')

Ejercicio23(PEPE.Flotante3)

print (f'-' * 20)'''

'''def Ejercicio24(Cadena):
    Lista_Cadena = Cadena.split(' ')
    
    for elemento in Lista_Cadena:
        print (f'{elemento}')
        
    print (f'La cantidad de palabras digitadas es {len(Lista_Cadena)}')

Ejercicio24(PEPE.Flotante4)'''

'''Lista_Alumnos = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
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
        
    Lista.sort(key = lambda Num : Num[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes de la lista es {Menore} ({Lista[0][1]})')
    print (f'El mayor de los estudiantes de la lista es {Mayore} ({Lista[-1][1]})')

Colegio(Lista_Alumnos)'''

class Persona1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre

Objeto1 = Persona1('Erick Perez')

print (f'Hola {Objeto1}')

print (f'-' * 20)

class Colores1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Colores = [
    Colores1('Rosa'),
    Colores1('Amarillo'),
    Colores1('Cafe')
]

print (f'La lista de colores es {Lista_Colores}')

print (f'-' * 20)

class Inventario1():
    def __init__(self):
        self.Productos = []
        
    def __len__(self):
        return len(self.Productos)
        
Objeto2 = Inventario1()

Objeto2.Productos.append('Sandia')
Objeto2.Productos.insert(1, 'Cas')
Objeto2.Productos.extend(['Maiz'])

print (f'La cantidad de elementos de la lista es {len(Objeto2)}')

print (f'-' * 20)

class Igualdad1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre

Objeto3 = Igualdad1('Panda Rojo')
Objeto4 = Igualdad1('Panda Rojo')

if (Objeto3 == Objeto4):
    print (f'Ambos objetos son iguales')
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

'''import requests

Saborcito = 'Mango Maduro'

URL = 'http://127.0.0.1:8002/grupo1/elemento2/'

Agregado1 = requests.post(URL, params={'Elemento' : Saborcito})
Agregado2 = Agregado1.json()

print (f'{Agregado2}')

Unidad1 = requests.get('http://127.0.0.1:8002/grupo1/')
Unidad2 = Unidad1.json()

print (f'Los sabores de helado son {Unidad2["Helados"]}: ')

print (f'-' * 20)

Indice = 3
Nuevo_Saborcito = 'Perro Mojado'

URL2 = 'http://127.0.0.1:8002/grupo1/elemento3/'

Reemplazado1 = requests.put(URL2, params={"Indice": Indice}, json=Nuevo_Saborcito)
Reemplazado2 = Reemplazado1.json()

print (f'{Reemplazado2}')

Unidad1 = requests.get('http://127.0.0.1:8002/grupo1/')
Unidad2 = Unidad1.json()

print (f'Los sabores de helado son {Unidad2["Helados"]}: ')'''

var1 = '3'

if (isinstance(var1, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
if (var1.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
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
    print (f'Error, lo ingresado no es un numero decimal')
    
try:
    Numerito2 = float(var2)
    if (Numerito2.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var3 = 5

if (isinstance(var3, (int, float))):
    print (f'Lo ingresado es un numero entero o decimal')
else:
    print (f'Error, lo ingresado no es un numero')
    
try:
    Numerito3 = float(var3)
    if (Numerito3.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var4 = 'erick123'

if (var4, (str, int)):
    print (f'Lo ingresado es texto o numero entero')
else:
    print (f'Error de formato')
    
if (var4.isalnum()):
    print (f'Lo ingresado es texto o numero entero')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var5 = 'texto'

if (var5.isalpha()):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Error, lo que ingresaste no es texto')
    
if (isinstance(var5, (str))):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Error, lo que ingresaste no es texto')
    
try:
    Numerito4 = float(var5)
    if (Numerito4.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Lo que ingresaste es texto')
    
print (f'-' * 20)

var6 = '    s      '

if (var6.isspace()):
    print (f'Lo que ingresaste esta compuesto por espacios nada mas')
else:
    print (f'Error, lo que ingresaste tiene mas que solo espacios')
    
print (f'-' * 20)

var7 = ' '

if (bool(var7) == True):
    print (f'Esta variable tiene contenido')
else:
    print (f'Error, esta variable esta vacia')
    
print (f'-' * 20)

var8 = 'eSteBAN'

if (var8.lower().islower()):
    print (f'Este texto esta compuesto por minusculas nada mas')
    
if (var8.upper().isupper()):
    print (f'Este texto esta compuesto por mayusculas nada mas')
    
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
    
Encontrada1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateada.date()]

if (Encontrada1.empty):
    print (f'No se encontraron ventas en esta fecha')
else:
    print (f'Genial! Se encontraron ventas en esta fecha')
    
    Grupo1 = Encontrada1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'En la fecha {Fech1_Formateada}, el producto {Grupo1_Min} vendio un total de {Grupo1_Min_Cant} unidades')
    print (f'En la fecha {Fech1_Formateada}, el producto {Grupo1_Max} vendio un total de {Grupo1_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que nos compraron en esta fecha fue de {Grupo1.count()}')
    print (f'La cantidad de productos comprados en esta fecha fue de {Grupo1.sum()}')
    
    Grupo2 = Encontrada1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue de ${Grupo2.sum()}')
    
    Promedio1 = Grupo2.sum() / Grupo1.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio1, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${Grupo2.mean()}')
    
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

# Version1

Pattern1 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Buscar1 = re.findall(Pattern1, Texto2)

print (f'{Buscar1}')

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

# Version1

Pattern2 = r'\!|\?|\.{2,}|[0-9]{4}\-\d{3,4}'

Buscar2 = re.sub(Pattern2, '', Texto3)

print (f'{Buscar2}')

print (f'-' * 20)

# Version2

Pattern3 = r'[^a-zA-Z0-9\s]'

Buscar3 = re.sub(Pattern3, '', Texto3)

print (f'{Buscar3}')

Buscar4 = re.sub(r'\d{5,}', '', Buscar3)

print (f'{Buscar4}')

print (f'-' * 20)

# Version3

import re

Texto3_temp1 = Texto3

Pattern4 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Correos1 = re.findall(Pattern4, Texto3)

print (f'{Correos1}')

for i, email in enumerate(Correos1, start=1):
    Texto3_temp1 = Texto3_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto3_temp1}')

Pattern5 = r'\!|\?|\.{2,}'

Texto3_temp2 = re.sub(Pattern5, '', Texto3_temp1)

print (f'{Texto3_temp2}')

Texto3_temp3 = re.sub(r'\d{4}\-[0-9]{2,4}', '', Texto3_temp2)

print (f'{Texto3_temp3}')

for i, email in enumerate(Correos1, start=1):
    Texto3_temp3 = Texto3_temp3.replace(f'SAMPLE{i}', email)
    
print (f'{Texto3_temp3}')

print (f'-' * 20)

import re

Texto4 = """
Hola!!! Contacta a juan.perez@gmail.com!!!
También a maria_123@hotmail.net???
Otro válido: ana+test@yahoo.org!!!
Fin!!!
"""

Pattern6 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Texto4_temp1 = Texto4

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

'''Lista_Promedios = []

Contador = 0

while (Contador < 3):
    while True:
        Numerito5 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numerito6 = float(Numerito5)
            if (Numerito6.is_integer()):
                print (f'El numero ingresado es entero')
                Lista_Promedios.append(Numerito6)
                break
            else:
                print (f'El numero ingresado es decimal')
                Lista_Promedios.append(Numerito6)
                break
        except ValueError:
            print (f'Error, lo ingresado no es un numero')
    Contador += 1
    
Promedio2 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas ingresadas es {round(Promedio2, 2)}')'''

from Module_Own import Pokemon1 as Poke1

Objeto7 = Poke1(PEPE.Diccionario_Poke['Poke1'], 'Electrico', 'Impact Trueno')
Objeto8 = Poke1(PEPE.Diccionario_Poke['Poke2'], 'Roca', 'Sismo')

Objeto7.Mostrar()

print (f'-' * 20)

Objeto8.Mostrar()

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto9 = Poke_Kid1(PEPE.Diccionario_Poke['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto9)
Objeto9.Mostrar()

print (f'-' * 20)

class Veterinaria1():
    def __init__(self, Nombre, Peso, Edad):
        self.Nombre = Nombre
        self.Peso = Peso
        self.Edad = Edad

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Peso: {self.Peso}kgs')
        print (f'Edad: {self.Edad} años')
        
class Perro1(Veterinaria1):
    def __init__(self, Nombre, Peso, Edad, Raza, Padecimiento):
        super().__init__(Nombre, Peso, Edad)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        
    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        
Objeto10 = Perro1('Chester', 2.8, 5, 'Poddle', 'Asma De Perro')

Veterinaria1.Mostrar(Objeto10)
Objeto10.Mostrar()

print (f'-' * 20)

class Gato1(Veterinaria1):
    def __init__(self, Nombre, Peso, Edad, Color, Paciente):
        super().__init__(Nombre, Peso, Edad)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto11 = Gato1('Messi', 1.8, 1.5, 'Gris', 'No')

Veterinaria1.Mostrar(Objeto11)
Objeto11.Mostrar()

print (f'-' * 20)

class Pajaro1(Veterinaria1):
    def __init__(self, Nombre, Peso, Edad, Especie, Habla):
        super().__init__(Nombre, Peso, Edad)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto12 = Pajaro1('Polly', 0.4, 31, 'Cacatua', 'Si')

Veterinaria1.Mostrar(Objeto12)
Objeto12.Mostrar()

print (f'-' * 20)

class Atacante1():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon
        
    def Mostrar(self):
        print (f'Damage: {self.Damage}pts')
        print (f'Weapon: {self.Weapon}')
        
class Defensor1():
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life
        
    def Mostrar(self):
        print (f'Healing: {self.Healing}pts')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}pts')
        
class Paladin1(Atacante1, Defensor1):
    def __init__(self, Damage, Weapon, Healing, Potion, Life, Name):
        Atacante1.__init__(self, Damage, Weapon)
        Defensor1.__init__(self, Healing, Potion, Life)
        self.Name = Name
        
    def Mostrar(self):
        print (f'Name: {self.Name}')
        
Objeto13 = Paladin1(75, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto13.Mostrar()
Atacante1.Mostrar(Objeto13)
Defensor1.Mostrar(Objeto13)

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
        
Objeto14 = D1()

A1.Mostrar(Objeto14)
B1.Mostrar(Objeto14)
C1.Mostrar(Objeto14)
Objeto14.Mostrar()
E1.Mostrar(Objeto14)

print (f'-' * 20)

class Efectivo1():
    def Pagar(self):
        print (f'El pago se realizo en Efectivo')
        
class Tarjeta1():
    def Pagar(self):
        print (f'El pago se realizo en Tarjeta')
        
class Cripto1():
    def Pagar(self):
        print (f'El pago se realizo en Cripto')
        
Objeto15 = Cripto1()
Objeto16 = Tarjeta1()
Objeto17 = Efectivo1()

Objeto15.Pagar()
Objeto16.Pagar()
Objeto17.Pagar()

print (f'-' * 20)

class Cuenta_Bancaria1():
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
        print (f'Tu saldo a la fecha es de ${self.__Saldo}')
        
Objeto18 = Cuenta_Bancaria1(100)
Objeto18.Depositar(25)
Objeto18.Mostrar()

print (f'Existe un saldo que es privado y no deberia ser publico, este es {Objeto18.Dinero}')

Objeto18.Dinero = '50,000,000'

Objeto18.Mostrar()

print (f'Existe un saldo que es privado y no deberia ser publico, este es {Objeto18.Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla1(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla1(Plantilla1):
    def Mostrar(self):
        print (f'Este es el metodo interno')
        
    def General(self):
        print (f'Este es el metodo de la plantilla y es mandatorio')
        
Objeto19 = Sub_Plantilla1()

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
        print (f'El retador ha elegido un {self.Favorito.Elegir()} para la batalla!!!')
        
Objeto20 = Battle1()

Objeto20.Batallar()

print (f'-' * 20)

class Battle2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El retador ha elegido un {self.Favorito.Elegir()} para la batalla!!!')
        
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

Texto5 = 'esto hola es 125 - un texto ! en hela el que voy 6 a probar si @ esto realmente sirve hala 88 o no'

Buscar4 = re.search(r'voy', Texto5)

print (f'{Buscar4}')

Buscar5 = re.findall(r'\d+', Texto5)

print (f'{Buscar5}')

Buscar6 = bool(re.fullmatch(r'esto hola es 125 \- un texto \! en hela el que voy 6 a probar si \@ esto realmente sirve hala 88 o no', Texto5))

if (Buscar6 == True):
    print (f'El texto es exactamente igual')
else:
    print (f'Error, el texto no es igual')

Buscar7 = re.findall(r'h.la', Texto5)

print (f'{Buscar7}')

Buscar8 = re.search(r'^esto', Texto5)
Buscar9 = re.search(r'no$', Texto5)

print (f'{Buscar8}')
print (f'{Buscar9}')

Buscar10 = bool(re.match(r'^esto', Texto5))
Buscar11 = bool(re.match(r'o$', Texto5))

print (f'{Buscar10}')
print (f'{Buscar11}')

print (f'-' * 20)

import re

Texto6 = 'ericksuper80@gmail.com'

Pattern8 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@[a-zA-Z]+\.[a-z]{2,}$'

Buscar12 = bool(re.fullmatch(Pattern8, Texto6))

if (Buscar12 == True):
    print (f'El correo electronico tiene el formato correcto')
else:
    print (f'Error, el formato del correo electronico es incorrecto')
    
print (f'-' * 20)

import re

Texto7 = 'ericksuper80@gmail.com'

Pattern9 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)$'

Buscar13 = bool(re.match(Pattern9, Texto7))

if (Buscar13):
    print (f'El correo electronico 2 tiene el formato correcto')
else:
    print (f'Error, el formato del correo electronico 2 es incorrecto')
    
print (f'-' * 20)

import re

Texto8 = '32'

Pattern10 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar14 = bool(re.fullmatch(Pattern10, Texto8))

if (Buscar14 == True):
    print (f'El numero esta entre 01 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

import re

Texto9 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern11 = r'\d{2}\/[0-9]{2,4}\/\d{4,}'

Replacement11 = 'XX/XX/XXXX'

Buscar15 = re.sub(Pattern11, Replacement11, Texto9)

print (f'{Buscar15}')

Pattern12 = r'\+\d{1}\-[0-9]{3,4}\-\d{3}\-[0-9]{3,}'

Replacement12 = 'PhoneNumber'

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

Pattern13 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Buscar17 = re.findall(Pattern13, Texto10)

print (f'{Buscar17}')

for indice, elemento in enumerate(Buscar17, start=1):
    print (f'{indice} -- {elemento}')
    
print (f'-' * 20)

import re

Texto11 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Version1

Pattern14 = r'\!|\?|\.{2,}|[0-9]{3,4}\-\d{4,}'

Buscar18 = re.sub(Pattern14, '', Texto11)

print (f'{Buscar18}')

# Version2

import re

Texto12 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern15 = r'[^a-zA-Z0-9\s]+'

Buscar19 = re.sub(Pattern15, '', Texto12)

print (f'{Buscar19}')

Buscar20 = re.sub(r'\d{5,}', '', Buscar19)

print (f'{Buscar20}')

# Version3

import re

Texto13 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

Pattern16 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|yahoo|hotmail)\.(?:com|net|org)'

Correos3 = re.findall(Pattern16, Texto13)

print (f'{Correos3}')

Texto13_temp1 = Texto13

for i, email in enumerate(Correos3, start=1):
    Texto13_temp1 = Texto13_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto13_temp1}')

Pattern17 = r'\!|\?|\.{2,}|[0-9]{4}\-\d{3,}'

Texto13_temp2 = re.sub(Pattern17, '', Texto13_temp1)

print (f'{Texto13_temp2}')

for i, email in enumerate(Correos3, start=1):
    Texto13_temp2 = Texto13_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto13_temp2}')

print (f'-' * 20)

var9 = 3.5

if (isinstance(var9, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Error, lo ingresado no es un numero decimal')
    
try:
    Numerito5 = float(var9)
    if (Numerito5.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
print (f'-' * 20)

var10 = '3'

if (isinstance(var10, (int))):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
if (var10.isnumeric()):
    print (f'Lo ingresado es un numero entero')
else:
    print (f'Error, lo ingresado no es un numero entero')
    
try:
    Numerito6 = float(var10)
    if (Numerito6.is_integer()):
        print (f'Lo ingresado es un numero entero')
    else:
        print (f'Lo ingresado es un numero decimal')
except ValueError:
    print (f'Error, lo ingresado no es un numero')
    
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

def Exception1(Numero):
    try:
        Numerito = float(Numero)
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
    except (TypeError, ValueError):
        print (f'Error, ambos elementos deben ser numeros enteros')

Exception2(12, 7)

print (f'-' * 20)

def Exception3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        print (f'El resultado de la division es {round(Divi, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')

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
        print (f'Error, el indice elegido esta fuera de rango')

Exception4(3)

print (f'-' * 20)

Diccionario_Exception5 = dict({'Nombre' : "Erick", 'Edad' : Objeto8.Cantidad})

def Exception5(Llave):
    try:
        print (f'El elemento con llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave seleccionada esta fuera de rango')

Exception5("Votante")

print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Guanabana')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo seleccionado es incorrecto')
    
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
    Documento_Agregar = Docu.write(f'\nDurazno')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nFresa Pequeña', f'\nFresa Pequeña', f'\nFresa Pequeña'])
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke1"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke2"]}')
    Documento_Agregar = Docu.write(f'\n{PEPE.Diccionario_Poke["Poke3"]}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Diccionario_Poke)])
    Docu.close()
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Leer = Docu.read()
    print (f'{Documento_Leer}')
    Docu.close()
    
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

DataFrame_Concatenate = pd.concat([DataFrame1, DataFrame2])

print (f'{DataFrame_Concatenate}')

print (f'-' * 20)

DataFrame_Concatenate_Age = DataFrame_Concatenate['Edad']

print (f'{DataFrame_Concatenate_Age}')

print (f'-' * 20)

print (f'{DataFrame_Concatenate.info()}')

print (f'-' * 20)

print (f'La menor de las edades es {DataFrame_Concatenate_Age.min()}')
print (f'La mayor de las edades es {DataFrame_Concatenate_Age.max()}')

print (f'-' * 20)

for indice, elemento in DataFrame_Concatenate.iterrows():
    Sample1 = elemento['Nombre']
    Sample2 = elemento['Edad']
    
    print (f'Hola, mi nombre es {Sample1} y mi edad es {Sample2} años')
    
print (f'-' * 20)

Grupo3 = DataFrame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()
Grupo3_Min_Cant = Grupo3.min()
Grupo3_Max_Cant = Grupo3.max()

print (f'El menor de los numeros de la lista es {Grupo3_Min}')
print (f'El mayor de los numeros de la lista es {Grupo3_Max}')
print (f'La persona menor de la lista es {Grupo3_Min} con una edad de {Grupo3_Min_Cant} años')
print (f'La persona mayor de la lista es {Grupo3_Max} con una edad de {Grupo3_Max_Cant} años')

'''print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'Nombre', y = 'Edad', data=DataFrame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x = 'Nombre', y = 'Edad', data=DataFrame_Concatenate)

plt.show()

print (f'-' * 20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = 'Nombre', y = 'Edad', data=DataFrame_Concatenate)

plt.show()'''

print (f'{DataFrame_Concatenate.head(1)}')

print (f'-' * 20)

print (f'{DataFrame_Concatenate.head(3)}')

print (f'-' * 20)

print (f'{DataFrame_Concatenate.tail(1)}')

print (f'-' * 20)

Filas, Columnas = DataFrame_Concatenate.shape

print (f'La cantidad de Filas es {Filas}')
print (f'La cantidad de Columnas es {Columnas}')

Elemento1 = DataFrame1.loc[0, 'Nombre']
Elemento2 = DataFrame1.loc[0, 'Edad']
Elemento3 = DataFrame1.loc[0, 'Votante']
Elemento4 = DataFrame1.loc[0, :]
Elemento5 = DataFrame1.loc[:, 'Edad']

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')
print (f'{Elemento4}')
print (f'{Elemento5}')

print (f'-' * 20)

Elemento6 = DataFrame2.iloc[0, 0]
Elemento7 = DataFrame2.iloc[1, 1]
Elemento8 = DataFrame2.iloc[2, 2]
Elemento9 = DataFrame2.iloc[0, :]
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

print (f'{Cargar_Excel}')

Cargar_Excel1 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=1)
Cargar_Excel2 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0)
Cargar_Excel3 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, names=['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nuevo', 'diez'])
Cargar_Excel4 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tiquete')
Cargar_Excel5 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tiquete', usecols='E:I')
Cargar_Excel6 = pd.read_excel(Ruta_Excel, engine='openpyxl', sheet_name=0, header=0, index_col='tiquete', usecols='E:I', nrows=1)

print (f'-' * 20)

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

Cargar_Excel3_Sorted_Descending = Cargar_Excel3.sort_values(by='cinco', ascending=False)

print (f'{Cargar_Excel3_Sorted_Descending}')

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
print (f'{Array1.ndim}')
print (f'{Array1.shape}')
print (f'{Array1.size}')
print (f'{Array1.dtype}')
print (f'{Array1[1]}')

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
print (f'Mediado: {round(Array2_Sorted_Mean, 2)}')
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

Array3 = np.array([[['x', 'e', 'u'], ['l', 'm', 'i']],    [['w', 'z', 'v'], ['n', 's', 'r']]])

print (f'{Array3}')
print (f'{Array3.ndim}')
print (f'{Array3.shape}')
print (f'{Array3.size}')
print (f'{Array3.dtype}')
print (f'{Array3[1, 0, 0]}')

print (f'{Array3[0, 1, ::2]}')
print (f'{Array3[0, 0, ::3]}')
print (f'{Array3[0, 1, :2]}')
print (f'{Array3[0, 1, 2:]}')
print (f'{Array3[1, :, 2]}')
print (f'{Array3[0, 1, 2:3]}')
print (f'{Array3[1, 1, 0:None]}')
print (f'{Array3[1, 1, :]}')
print (f'{Array3[Array3 == "v"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],      [[[6, 5, 4], [9, 8, 7]], [[7, 5, 3], [3, 6, 9]]]])

print (f'{Array4}')
print (f'{Array4.ndim}')
print (f'{Array4.shape}')
print (f'{Array4.size}')
print (f'{Array4.dtype}')
print (f'{Array4[0, 1, 1, 0]}')

print (f'{Array4[1, 0, 0, ::2]}')
print (f'{Array4[1, 0, 1, ::3]}')
print (f'{Array4[0, 1, 0, :2]}')
print (f'{Array4[0, 1, 0, 2:]}')
print (f'{Array4[1, 0, :, 0]}')
print (f'{Array4[0, 0, 1, 2:3]}')
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
Sumita7 = np.sum(Array4_Sorted[0, 1, 1, 0:None])
Sumita8 = np.sum(Array4_Sorted[0, 1, 1, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=6, step=1) #type: ignore

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

print (f'Los menores de las columnas son: {Array_Num2_Reshape_Column_Min}')
print (f'Los mayores de las columnas son: {Array_Num2_Reshape_Column_Max}')
print (f'Los menores de las columnas son: {Array_Num2_Reshape_Row_Min}')
print (f'Los mayores de las columnas son: {Array_Num2_Reshape_Row_Max}')

print (f'-' * 20)

Array_Zeros = np.zeros(shape=(2, 3))

print (f'{Array_Zeros}')
print (f'{Array_Zeros.ndim}')
print (f'{Array_Zeros.shape}')
print (f'{Array_Zeros.size}')
print (f'{Array_Zeros.dtype}')
print (f'{Array_Zeros[0, 1]}')

print (f'{Array_Zeros[0, ::2]}')
print (f'{Array_Zeros[1, ::3]}')
print (f'{Array_Zeros[0, :2]}')
print (f'{Array_Zeros[1, 2:]}')
print (f'{Array_Zeros[:, 1]}')
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
print (f'{Array_Ones[0, 1]}')

print (f'{Array_Ones[0, ::2]}')
print (f'{Array_Ones[1, ::3]}')
print (f'{Array_Ones[0, :2]}')
print (f'{Array_Ones[0, 2:]}')
print (f'{Array_Ones[:, 2]}')
print (f'{Array_Ones[1, 2:3]}')
print (f'{Array_Ones[1, 0:None]}')
print (f'{Array_Ones[1, :]}')
print (f'{Array_Ones[Array_Ones == 1]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value=f'{PEPE.Diccionario_Poke["Poke3"]}')

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 0]}')

print (f'{Array_Gen1[0, ::2]}')
print (f'{Array_Gen1[1, ::3]}')
print (f'{Array_Gen1[1, :2]}')
print (f'{Array_Gen1[1, 2:]}')
print (f'{Array_Gen1[:, 1]}')
print (f'{Array_Gen1[0, 1:2]}')
print (f'{Array_Gen1[1, 0:None]}')
print (f'{Array_Gen1[1, :]}')
print (f'{Array_Gen1[Array_Gen1 == "Vaporeon"]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(5), fill_value=f'Fuecoco')

Lista_Array_Gen2 = list([])

for elemento in Array_Gen2:
    Lista_Array_Gen2.extend([str(elemento)])

print (f'{Array_Gen2}')
print (f'{type(Array_Gen2)}')
print (f'{Lista_Array_Gen2}')
print (f'{type(Lista_Array_Gen2)}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value=Array4[0, 1, 0, 2])

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3}')

print (f'-' * 20)

Tupla_Array = ('Rojo', 'Verde', 'Azul')
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = {'Nombre' : ["Erick", "Josue", "Karlita"]}

Array_Gen4 = np.full(shape=(2, 3), fill_value=Tupla_Array)
Array_Gen5 = np.full(shape=(1, 2), fill_value=Set_Conjunto_Array)
Array_Gen6 = np.full(shape=(4, 1), fill_value=Diccionario_Array["Nombre"][1])

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
print (f'{Array_Random1.ndim}')
print (f'{Array_Random1.shape}')
print (f'{Array_Random1.size}')
print (f'{Array_Random1.dtype}')
print (f'{Array_Random1[3]}')

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

print (f'El resultado es {Suma}')
print (f'El resultado es {Resta}')
print (f'El resultado es {Multiplicacion}')
print (f'El resultado es {Division}')
print (f'El resultado es {Array_Random1_Cien}')

print (f'-' * 20)

Array_Num8 = np.arange(start=1, stop=21, step=1) #type: ignore

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

print (f'-' * 20)

Lista_Array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Array5 = np.array(Lista_Array1)

print (f'{Array5}')
print (f'{Array5.ndim}')
print (f'{Array5.shape}')
print (f'{Array5.size}')
print (f'{Array5.dtype}')
print (f'{Array5[8]}')

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

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')
print (f'{Array_Random3.ndim}')
print (f'{Array_Random3.shape}')
print (f'{Array_Random3.size}')
print (f'{Array_Random3.dtype}')
print (f'{Array_Random3[0, 1, 2]}')

Array_Random3_sorted = np.sort(Array_Random3)
Array_Random3_sorted_Mean = np.mean(Array_Random3_sorted)
Array_Random3_sorted_Sum = np.sum(Array_Random3_sorted)

print (f'Acomodado: {Array_Random3_sorted}')
print (f'Media: {round(Array_Random3_sorted_Mean, 2)}')
print (f'Sumatoria: {Array_Random3_sorted_Sum}')

Array_Random3_sorted_Column_Min = np.min(Array_Random3_sorted, axis=0)
Array_Random3_sorted_Column_Max = np.min(Array_Random3_sorted, axis=0)
Array_Random3_sorted_Row_Min = np.max(Array_Random3_sorted, axis=1)
Array_Random3_sorted_Row_Max = np.max(Array_Random3_sorted, axis=1)

print (f'Los menores de las columnas son {Array_Random3_sorted_Column_Min}')
print (f'Los menores de las columnas son {Array_Random3_sorted_Column_Max}')
print (f'Los menores de las columnas son {Array_Random3_sorted_Row_Min}')
print (f'Los menores de las columnas son {Array_Random3_sorted_Row_Max}')

print (f'-' * 20)

Set_Conjunto_Sorteo1 = {'Erick', 'Josue'}
Set_Conjunto_Sorteo1.add('Karlita')
Set_Conjunto_Sorteo2 = set({'Carmelo', 'Susanita', 'Roxana'})
Set_Conjunto_Sorteo1.update(Set_Conjunto_Sorteo2)

Lista_Sorteo = list(Set_Conjunto_Sorteo1)

Ganador1 = np.random.choice(Lista_Sorteo, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Sorteo, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Sorteo, size=(2, 3), replace=False)

print (f'El ganador del sorteo es {Ganador1}')
print (f'El ganador del sorteo es {Ganador2}')
print (f'El ganador del sorteo es {Ganador3}')

print (f'-' * 20)

Array_Linspace = np.linspace(start=1, stop=1, num=3)

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
    print (f'Error, el experimento termina aqui')
    
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
    print (f'Error, el experimento termina aqui')
    
print (f'-' * 20)

def Generadora3():
    for elemento in range(0, 5):
        if (elemento == 0):
            yield f'Number Zero'
        elif (elemento == 1):
            yield f'Number One'
        elif (elemento == 2):
            yield f'Number Two'
        elif (elemento == 3):
            yield f'Number Three'
        elif (elemento == 4):
            yield f'Number Four'
        else:
            yield f'Error de codigo'

Gen3 = Generadora3()

try:
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
    print (f'{next(Gen3)}')
except StopIteration:
    print (f'Error, el experimento termina aqui')
    
print (f'-' * 20)

Lista_Elementos10 = [1, 2, 3, 4, 5]

def Ejercicio23(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Contador = 0
        
        while (Contador < len(Lista)):
            Contador += 1
            
    return Contador

Resultado21 = Ejercicio23(Lista_Elementos10)

if (Resultado21 is None):
    print (f'Error, la lista esta vacia')
else:
    Total3 = Resultado21
    
    print (f'La lista tiene un total de {Total3} elementos')
    
print (f'-' * 20)

def Ejercicio24(Lista):
    Acumulador = 0
    for elemento in Lista:
        if (elemento % 2 == 0):
            Acumulador += elemento
            
    return Acumulador

Resultado22 = Ejercicio24(Lista_Elementos10)

if (len(Lista_Elementos10) == 0):
    print (f'Error, la lista esta vacia')
else:
    Acumulante = Resultado22
    print (f'Si sumo solo los elementos pares me da el numero {Acumulante}')
    
print (f'-' * 20)

def Ejercicio25(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        for elemento in Lista:
            Acumulador += elemento
            
    return Acumulador

Resultado23 = Ejercicio25(Lista_Elementos10)

if (Resultado23 is None):
    print (f'Error, la lista esta vacia')
else:
    Acumulante2 = Resultado23
    print (f'La suma de todos los elementos de la lista es {Acumulante2}')
    
Lista_Elementos11 = list([1, 2, 3, 4, 5])
    
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

Resultado24 = Ejercicio26(Lista_Elementos11, 2)

if (Lista_Elementos11.__len__() == 0):
    print (f'Error, la lista esta vacia')
else:
    Founder1 = Resultado24
    if (Founder1 == True):
        print (f'El numero fue encontrado')
    else:
        print (f'Error, el numero no fue encontrado en la lista')
        
print (f'-' * 20)

def Ejercicio27(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Menore = min(Lista)
        Mayore = max(Lista)
        
    Lista_Resultado = [Menore, Mayore]
    return Lista_Resultado

Resultado25 = Ejercicio27(Lista_Elementos11)

if (Resultado25 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de los numeros de la lista es {min(Resultado25)}')
    print (f'El mayor de los numeros de la lista es {max(Resultado25)}')

print (f'-' * 20)

def Ejercicio28(Lista):
    Menore = min(Lista)
    Mayore = max(Lista)
    
    return Menore, Mayore

Resultado25 = Ejercicio28(Lista_Elementos11)

if (len(Lista_Elementos11) == 0):
    print (f'Error, la lista esta vacia')
else:
    Menore1, Mayore1 = Resultado25
    print (f'El menor de los numeros de la lista es {Menore1}')
    print (f'El mayor de los numeros de la lista es {Mayore1}')
    
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

Resultado26 = Ejercicio29(Lista_Elementos11, 2)

if (Resultado26 is None):
    print (f'Error, la lista esta vacia')
else:
    Counter1 = Resultado26
    print (f'La cantidad de numeros que son mayores a 2 son {Counter1}')
    
print (f'-' * 20)

def Ejercicio30(Lista):
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

Resultado27 = Ejercicio30(Lista_Elementos11)

if (Resultado27 is None):
    print (f'Error, la lista esta vacia')
else:
    Pares2 = Resultado27
    print (f'La lista de solo numeros pares es {Pares2}')
    
print (f'-' * 20)

def Ejercicio31(Lista):
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

Resultado28 = Ejercicio31(Lista_Elementos11)

if (Resultado28 is None):
    print (f'Error, la lista esta vacia')
else:
    Impares2 = Resultado28
    print (f'La lista de solo numeros impares es {Impares2}')
    
print (f'-' * 20)

def Ejercicio32(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Mult = list([])
        
        for elemento in Lista:
            Lista_Mult.append(elemento * 2)
            
    return Lista_Mult

Resultado29 = Ejercicio32(Lista_Elementos11)

if (Resultado29 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'Lista Original: {Lista_Elementos11}')
    print (f'Lista Actualizada: {Resultado29}')
    
print (f'-' * 20)

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'El resultado de la sumatoria 1 es {PEPE.Sumatoria1(12, 7)}')

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
    
PEPE.Usuario1(Saludar_Dos(), 'MASCULINO')

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
    print (f'YOU ARE A MAN CATALOGED AS MALE')
else:
    print (f'YOU ARE A WOMAN CATALOGED AS FEMALE')
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
        Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(22)}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo seleccionado no existe')
    
with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Lineas = Docu.readlines()
    print (f'{Documento_Lineas}')
    Docu.close()
    
print (f'-' * 20)
    
def Funcion_Tupla(*args):
    return args

Variable_Funcion_Tupla = Funcion_Tupla("Perro", 200, 3.5, True)

print (f'{Funcion_Tupla("Perro", 200, 3.5, True)}')
print (f'{Variable_Funcion_Tupla[2]}')
print (f'{Funcion_Tupla("Perro", 200, 3.5, True)[3]}')
print (f'{type(Funcion_Tupla("Perro", 200, 3.5, True))}')

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
        
    for elemento in kwargs.values():
        print (f'{elemento}')
        
Funcion_Diccionario(Nombre = Saludar_Dos(), Edad = Objeto7.Cantidad, Votante = not True)

print (f'-' * 20)

def Sumatoria2(*args):
    return sum(args)

print (f'El resultado de la sumatoria es {Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

def Sumatoria_Dos(Nombre, *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria_Dos("Erick", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

if (PEPE.Any_Par == True):
    print (f'Los numeros pares de la lista son {PEPE.Lista_Par}')
    print (f'Los numeros pares de la lista son {list(Anonima3)}')
else:
    print (f'Error, no hay numeros pares en la lista')
    
print (f'El resultado de la multiplicacion es {Anonima1(150, 2)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

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
        return Nombre + Apellido
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
print (f'{Variable_Closure(38)}')

def Closure_Crear_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y

    return Closure_Multiplicador

Mult1 = Closure_Crear_Multiplicador(2)
Mult2 = Closure_Crear_Multiplicador(3)

print (f'El multiplicador 1 es {Mult1(10)}')
print (f'El multiplicador 2 es {Mult2(10)}')

def Filtro(Lista):
    Any_Impar = any(num % 2 != 0 for num in Lista)
    Lista_Impar = [num for num in Lista if num % 2 != 0]
    Anonima = filter(lambda Num : Num % 2 != 0, Lista)
    
    if (Any_Impar == True):
        print (f'Los numeros impares de la lista son {Lista_Impar}')
        print (f'Los numeros impares de la lista son {list(Anonima)}')
    else:
        print (f'Error, no hay elementos impares en la lista')

Filtro(PEPE.Lista_Numeros)

print (f'-' * 20)

def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'ANTES')
        Segunda()
        print (f'DESPUES')
        
    return Tercera

@Primera
def Saludar3():
    print (f'Hola Mundo')

Saludar3()

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 19
        
    return Tercera

@Primera
def Sumatoria3(Num1, Num2):
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
    return f'Mi nombre es {Nombre} {Apellido}'

print (f'{Usuario2("Erick", "Perez")}')

from Module_Own import Pokemon2 as Poke2

Objeto24 = Poke2(PEPE.Diccionario_Poke["Poke1"], 'Electricidad', 'Impact Trueno')
Objeto25 = Poke2(PEPE.Diccionario_Poke["Poke2"], 'Roca', 'Sismo')

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
        
Objeto26 = Poke_Kid2(PEPE.Diccionario_Poke["Poke3"], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto26)
Objeto26.Mostrar()

print (f'-' * 20)

class Camara():
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada')
        
class Reproductor_Musica():
    def Reproducir_Musica(self):
        print (f'La musica fue reproducida')
        
class Smartphone(Camara, Reproductor_Musica):
    def Encender_Smartphone(self):
        print (f'Smartphone fue encendido')
        
Objeto27 = Smartphone()

Objeto27.Encender_Smartphone()
Objeto27.Reproducir_Musica()
Objeto27.Tomar_Fotografia()

print (f'-' * 20)

class Veterinaria2():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad} años')
        print (f'Peso: {self.Peso}')
        
class Perro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        
    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        
Objeto28 = Perro2('Chester', 2.8, 5, 'Poodle', 'Asma De Perro')

Veterinaria2.Mostrar(Objeto28)
Objeto28.Mostrar()

print (f'-' * 20)

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto29 = Gato2('Messi', 1.5, 2, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto29)
Objeto29.Mostrar()

print (f'-' * 20)

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla

    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto30 = Pajaro2('Polly', 31, 0.4, 'Guacamaya', 'Si')

Veterinaria2.Mostrar(Objeto30)
Objeto30.Mostrar()

print (f'-' * 20)

class Atacante2():
    def __init__(self, Damage, Weapon):
        self.Damage = Damage
        self.Weapon = Weapon
        
    def Mostrar(self):
        print (f'Damage: {self.Damage}')
        print (f'Weapon: {self.Weapon}')
        
class Defensor2():
    def __init__(self, Healing, Potion, Life):
        self.Healing = Healing
        self.Potion = Potion
        self.Life = Life
        
    def Mostrar(self):
        print (f'Healing: {self.Healing}')
        print (f'Potion: {self.Potion}')
        print (f'Life: {self.Life}')
        
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

Hija_Padre = issubclass(Poke_Kid2, Poke2)

print (f'{Hija_Padre}')

Instancia1 = isinstance(Objeto31, Paladin2)
Instancia2 = isinstance(Objeto31, Defensor2)
Instancia3 = isinstance(Objeto31, Atacante2)
Instancia4 = isinstance(Objeto31, Defensor1)

print (f'{Instancia1}')
print (f'{Instancia2}')
print (f'{Instancia3}')
print (f'{Instancia4}')

print (f'-' * 20)

class A2():
    def Mostrar(self):
        print (f'Hola A2')
        
class E2():
    def Mostrar(self):
        print (f'Hola E2')
        
class B2(E2):
    def Mostrar(self):
        print (f'Hola B2')
        
class C2(A2):
    def Mostrar(self):
        print (f'Hola C2')
        
class D2(B2, C2):
    def Mostrar(self):
        print (f'Hola D2')
        
Objeto32 = D2()

A2.Mostrar(Objeto32)
B2.Mostrar(Objeto32)
C2.Mostrar(Objeto32)
Objeto32.Mostrar()
E2.Mostrar(Objeto32)

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
        print (f'Tu saldo a la fecha es de ${self.__Saldo}')
        
Objeto33 = Cuenta_Bancaria2(100)
Objeto33.Depositar(25)
Objeto33.Mostrar()

print (f'Tu saldo privado que no deberia exponerse es {Objeto33.Dinero}')

Objeto33.Dinero = '50,000,000'

Objeto33.Mostrar()

print (f'Tu saldo privado que no deberia exponerse es {Objeto33.Dinero}')

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
        
Objeto34 = Efectivo2()
Objeto35 = Tarjeta2()
Objeto36 = Cripto2()

Objeto34.Pagar()
Objeto35.Pagar()
Objeto36.Pagar()

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla2(ABC):
    @abstractmethod
    def General():
        pass
    
class Sub_Plantilla2(Plantilla2):
    def Mostrar(self):
        print (f'Este es el metodo interno')
        
    def General(self):
        print (f'Metodo obligatorio de la Plantilla2')
        
Objeto37 = Sub_Plantilla2()

Objeto37.Mostrar()
Objeto37.General()

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
        
Objeto38 = Pastel1()

Objeto38.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Ingrediente1 = Chocolate()
Objeto39 = Pastel2(Ingrediente1)
Objeto39.Hornear()

Ingrediente2 = Vainilla()
Objeto40 = Pastel2(Ingrediente2)
Objeto40.Hornear()

Ingrediente3 = Fresa()
Objeto41 = Pastel2(Ingrediente3)
Objeto41.Hornear()

print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esto
Es
Un
Long
String'''

variable4 = Objeto8.Cantidad
variable5 = PEPE.Division_Flotante
variable6, variable7 = True, Objeto9.Catched

# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Mi nombre completo es {Lista_Uno[0]} {variable2}')

print (f'Concatenacion simple {PEPE.Diccionario_Poke["Poke3"]}')

print (f'{PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")]} tiene {Objeto8.Cantidad} {PEPE.Diccionario_Poke["Poke3"]}s')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Josue' in PEPE.Lista1)
print (f'Misty' not in PEPE.Tupla_Poke)
print (f'{PEPE.Diccionario_Poke["Poke1"]}' in PEPE.Set_Conjunto_Poke1)

snake_case1, snake_case2, snake_case3 = PEPE.Tupla_Poke

print (f'Esto es una declaracion snake case y al mismo tiempo desempaquetado de variable {snake_case2}')

print (f'La cantidad de elementos de la lista 1 es {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La cantidad de elementos de la lista 1 es {len(Lista_Uno)}')

Cociente, Residuo = divmod(Objeto8.Cantidad, Sumatoria2(1, 2, 1, 1))

print (f'Cociente: {Cociente}')
print (f'Residuo: {Residuo}')

print (f'{Lista_Uno[::2]}')
print (f'{Lista_Uno[::3]}')
print (f'{Lista_Uno[:2]}')
print (f'{Lista_Uno[2:]}')
print (f'{Lista_Uno[2:3]}')
print (f'{Lista_Uno[0:None]}')
print (f'{Lista_Uno[:]}')

print (f'{Lista_Uno[2:3]} eso que ves ahi es un {PEPE.Lista2[PEPE.Lista2.index("Koala")]}?')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), 150, 50, 200, 100)

print (f'{Lista_Cuatro}')

del Lista_Uno[1]
Lista_Uno.remove("Coco Rayado")
Lista_Uno.pop(-2)
Lista_Uno.pop(-1)
Lista_Uno.pop(-1)

print (f'{Lista_Uno}')
print (f'La cantidad de elementos de la lista 1 es {len(Lista_Uno)}')

Lista_Uno_Copia = Lista_Uno.copy()

Lista_Uno.clear()

print (f'{Lista_Uno}')
print (f'La cantidad de elementos de la lista 1 es {len(Lista_Uno)}')

print (f'{Lista_Uno_Copia}')
print (f'La cantidad de elementos de la lista 1 es {len(Lista_Uno_Copia)}')

print (f'{Lista_Cuatro}')
Lista_Cuatro.sort()
print (f'{Lista_Cuatro}')
Lista_Cuatro.sort(reverse = True)
print (f'{Lista_Cuatro}')
Lista_Cuatro.reverse()
print (f'{Lista_Cuatro}')

print (f'{PEPE.__dir__()}') #type: ignore

Tupla1 = ('Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde')

print (f'{Tupla1}')

Tupla1 = tuple(('Red', 'Blue', 'Green'))

print (f'{Tupla1}')

Tupla2 = 'Rojo', 'Verde', 'Azul',

Tupla3 = 'Rojo',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(Variable_Funcion_Tupla)}')

Set_Conjunto1 = {'Electrico', Objeto8.Tipo, Objeto8.Tipo, Objeto8.Tipo, Objeto8.Tipo}
Set_Conjunto1.add(f'Hada')

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Electricity', 'Rock', 'Fairy'})

print (f'{Set_Conjunto1}')

Set_Conjunto_A = {1, 2, 3, 4, 5}
Set_Conjunto_B = {4, 5}
Set_Conjunto_C = set({8})

print (f'{Set_Conjunto_A.issuperset(Set_Conjunto_B)}')
print (f'{Set_Conjunto_A >= Set_Conjunto_B}')
print (f'-' * 20)
print (f'{Set_Conjunto_B.issubset(Set_Conjunto_A)}')
print (f'{Set_Conjunto_B <= Set_Conjunto_A}')
print (f'-' * 20)
print (f'{Set_Conjunto_A.isdisjoint(Set_Conjunto_C)}')

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

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, 'ChocoMani'})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : Saludar_Dos(),
    'Edad' : Objeto7.Cantidad,
    'Votante' : Variable_Funcion_Tupla[3]
}

Diccionario2 = {
    'Nombre' : ['Erick', 'Josue', 'Karlita'],
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

Diccionario1_copia = Diccionario1.copy()

del Diccionario1["Nombre"]
Diccionario1.pop("Edad")

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')
print (f'{Diccionario1_copia}')

Diccionario1 = dict({1 : "Karlita", 2 : 6, 3 : not True})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario1.get(1)} no puede votar ya que solo tiene {Diccionario2["Edad"][2]} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'Dragon')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = PEPE.Diccionario_Poke['Poke1']

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

Diccionario_Vacio3 = dict.fromkeys(['Uno', 'Dos', 'Tres', 'Cuatro'])

for indice, elemento in enumerate(Diccionario_Vacio3, start=1):
    if (elemento == 'Uno'):
        Diccionario_Vacio3[elemento] = Lista_Uno_Copia[0]
    elif (elemento == 'Dos'):
        Diccionario_Vacio3[elemento] = Lista_Uno_Copia[1]
    elif (elemento == 'Tres'):
        Diccionario_Vacio3[elemento] = Lista_Uno_Copia[2]
    elif (elemento == 'Cuatro'):
        Diccionario_Vacio3[elemento] = Lista_Uno_Copia[3]
    else:
        continue
    
print (f'{Diccionario_Vacio3}')
print (f'{Diccionario_Vacio3.keys()}')
print (f'{Diccionario_Vacio3.values()}')
print (f'{Diccionario_Vacio3.items()}')
print (f'{Diccionario_Vacio3["Uno"]}')
print (f'{Diccionario_Vacio3.get("Dos")}')

print (f'-' * 20)

Key1 = [f'Key{i}' for i in range(len(Lista_Uno_Copia))]

print (f'{Key1}')

Diccionario4 = dict(zip(Key1, Lista_Uno_Copia))

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Key1"]}')
print (f'{Diccionario4.get("Key2")}')

print (f'-' * 20)

for elemento in Diccionario1_copia:
    print (f'{Diccionario1_copia[elemento]}')
    
print (f'-' * 20)

for elemento in Diccionario1_copia.keys():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario1_copia.values():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario1_copia.items():
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
    print (f'Error, el formato de la fecha es incorrecto')
    exit()
    
Cargar_Csv3['TOTALITO'] = Cargar_Csv3['quantity'] * Cargar_Csv3['price']
    
Encontrada3 = Cargar_Csv3[Cargar_Csv3['date'].dt.date == Fech3_Formateada.date()]

if (Encontrada3.empty):
    print (f'No hay ventas en esta fecha')
else:
    print (f'Genial! Encontramos ventas en esta fecha')
    
    Grupo4 = Encontrada3.groupby('product')['quantity'].sum()
    Grupo4_Min = Grupo4.idxmin()
    Grupo4_Max = Grupo4.idxmax()
    Grupo4_Min_Cant = Grupo4.min()
    Grupo4_Max_Cant = Grupo4.max()
    
    print (f'En la fecha {Fech3_Formateada}, el producto {Grupo4_Min} vendio un total de {Grupo4_Min_Cant} unidades')
    print (f'En la fecha {Fech3_Formateada}, el producto {Grupo4_Max} vendio un total de {Grupo4_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que nos compraron en esta fecha fue de {Grupo4.count()}')
    print (f'La cantidad de unidades vendidas en esta fecha fue de {Grupo4.sum()}')
    
    Grupo5 = Encontrada3.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero que se vendio en esta fecha fue de ${Grupo5.sum()}')
    
    Promedio2 = Grupo5.sum() / Grupo4.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio2, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${Grupo5.mean()}')
    
print (f'-' * 20)

Set_Conjunto_Productos = set(Cargar_Csv3['product'])

print (f'{Set_Conjunto_Productos}')

Lista_Productos = list(Set_Conjunto_Productos)

print (f'{Lista_Productos}')

Key2 = [f'Key_{i}' for i in range(len(Lista_Productos))]

Diccionario5 = dict(zip(Key2, Lista_Productos))

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Key_2"]}')
print (f'{Diccionario5.get("Key_5")}')

print (f'-' * 20)

Division_Baja = 14//7
Exponente = 4**3
Modulo = 20 % 6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {int(abs(Division_Baja))}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')

print (f'El tipo de dato de la variable es {type(variable1)}')
print (f'El tipo de dato de la variable es {type(variable3)}')
print (f'El tipo de dato de la variable es {type(PEPE.Division_Flotante)}')
print (f'El tipo de dato de la variable es {type(variable6)}')
print (f'El tipo de dato de la variable es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato de la variable es {type(Tupla1)}')
print (f'El tipo de dato de la variable es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de dato de la variable es {type(Diccionario1_copia)}')
print (f'El tipo de dato de la variable es {type(Funcion_Diccionario)}')
print (f'El tipo de dato de la variable es {type(Array2_Sorted)}')
print (f'El tipo de dato de la variable es {type(DataFrame1)}')
print (f'El tipo de dato de la variable es {type(Objeto10)}')

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
    
variable8 = 'Josue'
variable9 = 29

if (variable8 == 'Erick' and variable9 > 30):
    print (f'Ambas condiciones se cumplen')
else:
    print (f'Error, al menos una de las condiciones no se cumple')
    
print (f'-' * 20)

if (variable8 == 'Erick' or variable9 > 30):
    print (f'Al menos una de las condiciones se cumple')
else:
    print (f'Error, ninguna condicion se cumple')
    
class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        
    def Desplegar(self):
        print (f'Trainer: {self.Trainer}')
        print (f'City: {self.City}')
        print (f'Favorite: {self.Favorite}')
        
    def Mostrar(self):
        print (f'{self.Trainer} just catched a {self.Favorite} while visiting {self.City}')
        
Objeto42 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Ash")], 'Kanto', Objeto7.Nombre)
Objeto43 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Brooke")], 'Alolah', Objeto8.Nombre)
Objeto44 = Entrenador(PEPE.Tupla_Poke[PEPE.Tupla_Poke.index("Misty")], 'Paldea', Objeto9.Nombre)

Objeto42.Desplegar()
Objeto42.Mostrar()

print (f'-' * 20)

Objeto43.Desplegar()
Objeto43.Mostrar()

print (f'-' * 20)

Objeto44.Desplegar()
Objeto44.Mostrar()

print (f'-' * 20)

Negativo = -5

print (f'{int(abs(Negativo))}')

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
    print (f'Error, esto esta vacio')
    
print (f'-' * 20)

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} -- {elemento[1]}')
    
print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'{indice} ------- {elemento}')
    
print (f'-' * 20)

variable10 = 'eSteBAN'
variable10_letra = variable10[0]

print (f'{variable10}')
print (f'{variable10.lower()}')
print (f'{variable10.upper()}')
print (f'{variable10.capitalize()}')

print (f'{variable10.lower().find("b")}')
print (f'{variable10.lower().index("n")}')

print (f'La letra {variable10_letra} aparece un total de {variable10.lower().count(variable10_letra)} veces')

print (f'{variable10.lower().startswith(variable10_letra)}')
print (f'{variable10.lower().endswith("n")}')

print (f'{variable10.lower().replace("ban", "POPOTAMO")}')

variable11 = 'esto es un texto cualquiera, pero lo mas importante es saber si esto sirve o no'
variable11_lista = variable11.split(' ')

for elemento in variable11_lista:
    print (f'{elemento}')
    
print (f'La cantidad de elementos de la lista es {len(variable11_lista)}')

var11 = 'hola'

if (isinstance(var11, (str))):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Lo que ingresaste no es texto')
    
if (var11.isalpha()):
    print (f'Lo que ingresaste es texto')
else:
    print (f'Lo que ingresaste no es texto')
    
try:
    Numerito7 = float(var11)
    if (Numerito7.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Lo ingresado es texto')
    
print (f'-' * 20)

var12 = 3.5

if (isinstance(var12, (float))):
    print (f'Lo ingresado es un numero decimal')
else:
    print (f'Lo ingresado no es un numero decimal')
    
try:
    Numerito8 = float(var12)
    if (Numerito8.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Lo ingresado es texto')
    
print (f'-' * 20)

var13 = '3'

if (isinstance(var13, (int))):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Lo que ingresaste no es un numero entero')
    
if (var13.isnumeric()):
    print (f'Lo que ingresaste es un numero entero')
else:
    print (f'Lo que ingresaste no es un numero entero')
    
try:
    Numerito9 = float(var13)
    if (Numerito9.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Lo ingresado es texto')
    
print (f'-' * 20)

var14 = 'erick'

if (isinstance(var14, (float, str))):
    print (f'Esto es texto o numeros')
else:
    print (f'Error de formato')
    
if (var14.isalnum()):
    print (f'Esto es texto o numeros')
else:
    print (f'Error de formato')
    
print (f'-' * 20)

var15 = '       r        '

if (var15.isspace()):
    print (f'Esto es solo espacios')
else:
    print (f'Error, esto tiene mas que solo espacios')
    
var16 = ' '

if (bool(var16) == True):
    print (f'Gracias por la informacion')
else:
    print (f'Error ingrese una cadena')
    
print (f'-' * 20)

var17 = 'eSteBAN'

if (var17.lower().islower()):
    print (f'Lo ingresado esta completamente en minuscula')
else:
    print (f'Error, esto no esta solo en minuscula')
    
if (var17.upper().isupper()):
    print (f'Lo ingresado esta completamente en mayuscula')
else:
    print (f'Error, esto no esta solo en mayuscula')
    
print (f'-' * 20)

print (f'{PEPE.Tupla_Poke[2]} se encuentra en la posicion {PEPE.Tupla_Poke.index("Misty")}')

Contador = 0

while (Contador <= 5):
    print (f'El contador es {Contador}')
    Contador += 1
    
print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'El elemento es {PEPE.Lista_Numeros[Contador] * 100}')
    Contador+= 1
    
print (f'-' * 20)

Lista_Animales = ['Lagartija']
Lista_Animales.append(PEPE.Lista2[2])
Lista_Animales.insert(1, 'Leon')
Lista_Animales.extend(['Tortuga'])

print (f'{Lista_Animales}')

Contador = 0

while (Contador < len(Lista_Animales)):
    if (Lista_Animales[Contador] == 'Koala'):
        print (f'El animalillo viene de Australia')
        break
    else:
        Contador+= 1
        continue
    
for elemento1, elemento2 in zip(Lista_Animales, PEPE.Tupla_Poke):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento1, elemento2, elemento3, elemento4 in zip(Lista_Animales, Lista_Uno_Copia, PEPE.Set_Conjunto_Poke1, PEPE.Tupla_Poke):
    print (f'{elemento1} -- {elemento2} -- {elemento3} -- {elemento4}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
Lista_Mult = [num * 100 for num in PEPE.Lista_Numeros]
    
Menore2 = min(Lista_Mult)
Mayore2 = max(Lista_Mult)

print (f'El menor de los numeros de la lista es {Menore2}')
print (f'El mayor de los numeros de la lista es {Mayore2}')

Redondeado = round(14.458795, 2)

print (f'El numero redondeado de 14.458795 es {round(Redondeado, 2)}')

print (f'{bool(not True)}')
print (f'{bool(False)}')
print (f'{bool(None)}')
print (f'{bool(0)}')
print (f'{bool("")}')

Todo_All = all([Lista_Uno_Copia, Tupla1, Set_Conjunto_Menu1, ""])

print (f'{Todo_All}')

Sumatoria4 = sum(Lista_Mult)

print (f'El resultado de la sumatoria es {Sumatoria4}')

Set_Conjunto_Mult = {num * 100 for num in PEPE.Lista_Numeros}

print (f'{Set_Conjunto_Mult}')

print (f'-' * 20)

Uno = int('500')
Dos = str(500)
Tres = float(Uno)
Cuatro = list(Tupla1)
Cinco = tuple(Lista_Uno_Copia)
Seis = set(Tupla1)

print (f'{'500'} -- {type(Uno)}')
print (f'{500} -- {type(Dos)}')
print (f'{Uno} -- {type(Tres)}')
print (f'{Tupla1} -- {type(Cuatro)}')
print (f'{Lista_Uno_Copia} -- {type(Cinco)}')
print (f'{Tupla1} -- {type(Seis)}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto_Poke1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE2

PEPE2.Saludar5()

import Paquete.Sub_Paquete.Segundo as PEPE3

Variable_PEPE3 = PEPE3

'''def Exception_Finale():
    while True:
        Numerito = input(f'Ingrese un numero: ')
        try:
            Numerito_Finale = float(Numerito)
            if (Numerito_Finale.is_integer()):
                print (f'Lo que ingresaste es un numero entero')
                break
            else:
                print (f'Lo que ingresaste es un numero decimal')
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')

Exception_Finale()'''