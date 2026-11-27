try:
    import Module_Own as PEPE
except (ImportError, ModuleNotFoundError):
    print (f'Error, el modulo es incorrecto')
    raise

Diccionario_Numeral1 = dict({
    'Num1' : 5,
    'Num2' : 1,
    'Num3' : 6,
    'Num4' : 2,
    'Num5' : 3
})

print (f'{Diccionario_Numeral1}')

Diccionario_Numeral1_Sorted = dict(sorted(Diccionario_Numeral1.items(), key=lambda item : item[1]))
Diccionario_Numeral1_Sorted_Min = min(Diccionario_Numeral1_Sorted.items(), key=lambda item : item[1])
Diccionario_Numeral1_Sorted_Max = max(Diccionario_Numeral1_Sorted.items(), key=lambda item : item[1])

print (f'{Diccionario_Numeral1}')
print (f'{Diccionario_Numeral1_Sorted}')
print (f'{Diccionario_Numeral1_Sorted_Min}')
print (f'{Diccionario_Numeral1_Sorted_Max}')

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
    print (f'Error, la fecha es incorrecta')
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
    
    print (f'En esta fecha nos compraron {Grupo1.count()} clientes')
    
    print (f'La cantidad de productos vendidos en esta fecha fue de {Grupo1.sum()}')
    
    Grupo2 = Encontrado1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue de ${Grupo2.sum()}')
    
    Promedio1 = Grupo2.sum() / Grupo2.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio1, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Grupo2.mean(), 2)}')
    
print (f'-' * 20)

Diccionario1X = {
    'Nombre' : "Erick"
}

print (f'{Diccionario1X}')
print (f'{Diccionario1X.keys()}')
print (f'{Diccionario1X.values()}')
print (f'{Diccionario1X.items()}')
print (f'{Diccionario1X["Nombre"]}')
print (f'{Diccionario1X.get("Nombre")}')

for indice, elemento in Diccionario1X.items():
    print (f'{indice} : {elemento}')

print (f'-' * 20)

Diccionario2X = {
    'Nombre' : ["Erick"]
}

print (f'{Diccionario2X}')
print (f'{Diccionario2X.keys()}')
print (f'{Diccionario2X.values()}')
print (f'{Diccionario2X.items()}')
print (f'{Diccionario2X["Nombre"][0]}')
print (f'{Diccionario2X.get("Nombre")[0]}') #type: ignore

for indice, elemento in Diccionario2X.items():
    for indice, elemento_Finale in enumerate(elemento[:], start=1):
        print (f'{indice} : {elemento_Finale}')

print (f'-' * 20)

Diccionario3X = {
    'Usuario1' : {
        'Nombre' : "Erick"
    }
}

print (f'{Diccionario3X}')
print (f'{Diccionario3X.keys()}')
print (f'{Diccionario3X.values()}')
print (f'{Diccionario3X.items()}')
print (f'{Diccionario3X["Usuario1"]["Nombre"]}')
print (f'{Diccionario3X.get("Usuario1")["Nombre"]}') #type: ignore

for indice1, elemento1 in Diccionario3X.items():
    for indice2, elemento2 in elemento1.items():
        print (f'{indice2} : {elemento2}')

print (f'-' * 20)

Diccionario4X = {
    'Usuario1' : {
        'Nombre' : ["Erick"]
    }
}

print (f'{Diccionario4X}')
print (f'{Diccionario4X.keys()}')
print (f'{Diccionario4X.values()}')
print (f'{Diccionario4X.items()}')
print (f'{Diccionario4X["Usuario1"]["Nombre"][0]}')
print (f'{Diccionario4X.get("Usuario1")["Nombre"][0]}') #type: ignore

for indice1, elemento1 in Diccionario4X.items():
    for indice2, elemento2 in elemento1.items():
        for indice3, elemento3 in enumerate(elemento2, start=1):
            print (f'{indice3} : {elemento3}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv2 = 'C:\\Repo\\Store.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2.head()}')

Lista_Csv1 = list(Cargar_Csv2['product'])
Key1 = [f'Key{i}' for i in range(len(Lista_Csv1))]

Diccionario_Csv1 = dict(zip(Key1, Lista_Csv1))

print (f'{Diccionario_Csv1}')
print (f'{Diccionario_Csv1.keys()}')
print (f'{Diccionario_Csv1.values()}')
print (f'{Diccionario_Csv1.items()}')
print (f'{Diccionario_Csv1["Key1"]}')
print (f'{Diccionario_Csv1.get("Key3")}')

print (f'-' * 20)

Diccionario_Vacio1 = dict({})

for elemento1 in Key1:
    if (elemento1 not in Diccionario_Vacio1):
        Diccionario_Vacio1[elemento1] = []
        for elemento2 in Lista_Csv1[0:None]:
            if (elemento2 == "Desk Lamp"):
                Diccionario_Vacio1[elemento1].append(elemento2)
                break
            elif (elemento2 == "Office Chair"):
                Diccionario_Vacio1[elemento1].append(elemento2)
                break
            else:
                Diccionario_Vacio1[elemento1].append(elemento2)
                break
    else:
        continue
    
print (f'{Diccionario_Vacio1}')

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

DataFrame_Concatenate_Age = DataFrame_Concatenate['Edad']

print (f'{DataFrame_Concatenate_Age}')

print (f'{DataFrame_Concatenate.info}')

print (f'-' * 20)

DataFrame_Concatenate_Min = DataFrame_Concatenate_Age.min()
DataFrame_Concatenate_Max = DataFrame_Concatenate_Age.max()

print (f'El menor de los perritos es {DataFrame_Concatenate_Min}')
print (f'El menor de los perritos es {DataFrame_Concatenate_Max}')

Grupo3 = DataFrame_Concatenate.groupby('Nombre')['Edad'].sum()

Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()

print (f'El menor de los perritos es {Grupo3_Min} y su edad es {DataFrame_Concatenate_Min} años')
print (f'El mayor de los perritos es {Grupo3_Max} y su edad es {DataFrame_Concatenate_Max} años')

print (f'-' * 20)

for indice, elemento in DataFrame_Concatenate.iterrows():
    Elemental1 = elemento['Nombre']
    Elemental2 = elemento['Edad']
    
    print (f'Mi nombre es {Elemental1} y mi edad es {Elemental2} años')
    
print (f'-' * 20)

Datos1 = {"ana": {"edad": 25, "ciudad": "Quito"}}

def Ejercicio1(Diccionario, User, Field, New_Value):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        Diccionario[User] = {}
        Diccionario[User][Field] = New_Value
        return (False, f'Error, el usuario no existia, fue creado, {Diccionario}')
    else:
        Ubicado2 = Ubicado1.get(Field)
        if (Ubicado2 is None):
            Diccionario[User][Field] = New_Value
            return (False, f'Error, el campo no existia, fue creado, {Diccionario}')
        else:
            Diccionario[User][Field] = New_Value
            return (True, f'Exito, {Diccionario}')

Usuario1 = 'ana'
Campo1 = 'ciudad'
Nuevo_Valor1 = 'San Jose'

Sample1 = Ejercicio1(Datos1, Usuario1, Campo1, Nuevo_Valor1)

if (len(Datos1) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample1[0] == False):
        print (f'{Sample1[1]}')
    else:
        print (f'{Sample1[1]}')
        
print (f'-' * 20)

Diccionario_Lenguajes1 = {
    "python": 2,
    "java": 2,
    "c++": 3,
    "go": 1
}

def Ejercicio2(Diccionario):
    
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
                Lista_Repetidos.extend([indice])
            else:
                continue
            
        if (len(Lista_Repetidos) > 1):
            return Lista_Repetidos
        else:
            return Clave
        
Sample2 = Ejercicio2(Diccionario_Lenguajes1)

if (Sample2 is None):
    print (f'Error, este diccionario esta vacio')
else:
    print (f'El lenguaje o los lenguajes con mayor cantidad de alumnos son: {Sample2}')
    
print (f'-' * 20)

def Ejercicio3(Limite):
    Lista_Fibonacci = [0, 1]
    
    while (len(Lista_Fibonacci) < Limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

Sample3 = Ejercicio3(10)

print (f'La lista Fibonacci es: {Sample3}')

print (f'-' * 20)

# Metodo Num 1

Lista_Ejemplo1 = [10, 1, 2, 4, 3, 5, 6]

def Ejercicio4(Lista):
    if (len(Lista) == 0):
        return None
    else:
        for i in range(len(Lista)):
            for j in range(i + 1, len(Lista)):
                if (Lista[i] == Lista[j]):
                    return i
                else:
                    continue
                
        return False

Sample4 = Ejercicio4(Lista_Ejemplo1)

if (Sample4 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample4 == False):
        print (f'No se han encontrado numeros repetidos en la lista')
    else:
        print (f'El primer numero repetido de la lista aparece en la posicion {Sample4} y el numero es {Lista_Ejemplo1[Sample4]}')

print (f'-' * 20)

# Metodo Num 2

Lista_Ejemplo2 = [10, 5, 1, 4, 3, 5, 6]

def Ejercicio5(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista[:]:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            
    return None

Sample5 = Ejercicio5(Lista_Ejemplo2)

if (len(Lista_Ejemplo2) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample5 is None):
        print (f'No se han encontrado numeros repetidos en la lista')
    else:
        print (f'El primer numero repetido de la lista es {Sample5}')
        
print (f'-' * 20)

Lista_Ejemplo3 = list([90, 91, 79, 78])

def Ejercicio6(Lista):
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] < Lista[i]):
            return i
        else:
            continue
        
    return None

Sample6 = Ejercicio6(Lista_Ejemplo3)

if (Lista_Ejemplo3):
    if (Sample6 is None):
        print (f'No encontramos un aumento consecutivo en toda la lista')
    else:
        print (f'El primer aumento consecutivo sucede en la posicion {Sample6} con el numero {Lista_Ejemplo3[Sample6]}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejemplo4 = [100, 97, 95, 80, 78]

def Ejercicio7(Lista, Limit):
    if (len(Lista) == 0):
        return False
    else:
        for i in range(0 + 1, len(Lista)):
            if (Lista[i - 1] - Lista[i] >= Limit):
                Caida = Lista[i - 1] - Lista[i]
                Posicion = i
                return Posicion, Caida
            else:
                continue
            
        return None
    
Limite1 = 30

Sample7 = Ejercicio7(Lista_Ejemplo4, Limite1)

if (Sample7 is False):
    print (f'Error la lista esta vacia')
else:
    if (Sample7 is None):
        print (f'No se ha reportado una caida de temperatura drastica en la ultima hora')
    else:
        Posicion1, Caida1 = Sample7
        print (f'Alerta!, se ha reportado una caida de temperatura')
        print (f'Posicion de la caida: {Posicion1}')
        print (f'Caida en grados: {Caida1} grados')
        print (f'Temperatura actual: {Lista_Ejemplo4[Posicion1]} grados')
        
print (f'-' * 20)

Lista_Ejemplo5 = list([1, 1, 2, 1, 3])

def Ejercicio8(Lista):
    for i in range(0 + 2, len(Lista)):
        if (Lista[i - 2] < Lista[i - 1] > Lista[i]):
            return i - 1
        else:
            continue

    return None

Sample8 = Ejercicio8(Lista_Ejemplo5)

if (Lista_Ejemplo5):
    if (Sample8 is None):
        print (f'No hay ningun pico en esta lista')
    else:
        print (f'El pico sucede en la posicion {Sample8} con el numero {Lista_Ejemplo5[Sample8]}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejemplo6 = list(["python", "java", "python", "c++", "java", "python", "go", "c++", "python"])

def Ejercicio9(Lista):
    Diccionario_Vacio = dict({})
    
    for elemento in Lista[:]:
        if (elemento not in Diccionario_Vacio):
            Diccionario_Vacio[elemento] = 0
            Diccionario_Vacio[elemento] += 1
        else:
            Diccionario_Vacio[elemento] += 1
            
    return Diccionario_Vacio

Sample9 = Ejercicio9(Lista_Ejemplo6)

if (len(Lista_Ejemplo6) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample9):
        for indice, elemento in Sample9.items():
            print (f'{indice} : {elemento}')
    else:
        print (f'Error, el diccionario nunca se actualizo')
        
print (f'-' * 20)

'''Lista_Estudiantes = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'El nombre del alumno {elemento + 1} es: ')
        Alumno_Edad = int(input(f'La edad del alumno {elemento + 1} es: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda item : item[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes es {Menore} y su edad es {Lista[0][1]} años')
    print (f'El mayor de los estudiantes es {Mayore} y su edad es {Lista[-1][1]} años')

Colegio(Lista_Estudiantes)'''

class Persona1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def Mostrar1(self):
        return self.Nombre
    
    @property
    def Mostrar2(self):
        return self.Nombre
        
    def __str__(self):
        return self.Nombre
    
Objeto1 = Persona1("Erick Josue")

print (f'Mi nombre es {Objeto1.Mostrar1()}')
print (f'Mi nombre es {Objeto1.Mostrar2}')
print (f'Mi nombre es {Objeto1}')

class Colores1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre
    
Lista_Colores1 = [
    Colores1('Rojo'),
    Colores1('Azul'),
    Colores1('Verde')
]

print (f'La lista de colores es {Lista_Colores1}')

class Inventario1():
    def __init__(self):
        self.Comida = []
        
    def __len__(self):
        return len(self.Comida)
    
Objeto2 = Inventario1()

Objeto2.Comida.append('Empanada')
Objeto2.Comida.insert(1, 'Rosquilla')
Objeto2.Comida.extend(['Hamburguesa'])

print (f'La lista tiene actualmente {len(Objeto2)} elementos')

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
    
class Caja1():
    def __init__(self, Peso):
        self.Peso = Peso

    def __add__(self, Otro):
        return self.Peso + Otro.Peso
    
Objeto5 = Caja1(5)
Objeto6 = Caja1(3)

print (f'El resultado de la sumatoria es {Objeto5 + Objeto6}')

class Armario1():
    def __init__(self):
        self.Guardaropa = [
            'Camiseta',
            'Pantalones',
            'Medias'
        ]
        
    def __getitem__(self, Indice):
        return self.Guardaropa[Indice]
    
Objeto7 = Armario1()

print (f'La prenda en la posicion 0 es {Objeto7[0]}')
print (f'La prenda en la posicion 1 es {Objeto7[1]}')
print (f'La prenda en la posicion 2 es {Objeto7[2]}')

class Panaderia1():
    def __init__(self):
        self.Panes = list([
            'Baguette',
            'Donas',
            'Croissant'
        ])
        
    def __iter__(self):
        return iter(self.Panes)
    
Objeto8 = Panaderia1()

for indice, elemento in enumerate(Objeto8, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

from Module_Own import Pokemon1 as Poke1

Objeto9 = Poke1(PEPE.Diccionario_Pokemon['Poke1'], 'Electrico', 'Impact Trueno')
Objeto10 = Poke1(PEPE.Diccionario_Pokemon['Poke2'], 'Roca', 'Mega-Sismo')

Objeto9.Mostrar1()

print (f'El tipo de este pokemon es {Objeto9.Tipo}')
print (f'El nombre es {Objeto9.Mostrar2}')
print (f'El nombre es {Objeto9}')
print (f'El tipo de este pokemon es {Objeto9.Tipo}')

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar1(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto11 = Poke_Kid1(PEPE.Diccionario_Pokemon['Poke3'], 'Agua', 'HidroChorro', 'Acero')

Poke1.Mostrar1(Objeto11)
Objeto11.Mostrar1()

print (f'-' * 20)

class Camara1():
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada')
        
class Reproductor1():
    def Reproducir_Musica(self):
        print (f'La musica ha sido reproducida')
        
class Celular1(Camara1, Reproductor1):
    def Encender_Celular(self):
        print (f'El celular fue encendido')
        
Objeto12 = Celular1()

Objeto12.Encender_Celular()
Objeto12.Reproducir_Musica()
Objeto12.Tomar_Fotografia()

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
        
Objeto13 = Perro1('Terry', 3.5, 8, 'Dobberman', 'Obesidad')

Veterinaria1.Mostrar(Objeto13)
Objeto13.Mostrar()

print (f'-' * 20)

class Gato1(Veterinaria1):
    def __init__(self, Nombre, Peso, Edad, Color, Paciente):
        super().__init__(Nombre, Peso, Edad)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto14 = Gato1('Messi', 1.8, 2, 'Gris', 'No')

Veterinaria1.Mostrar(Objeto14)
Objeto14.Mostrar()

print (f'-' * 20)

class Pajaro1(Veterinaria1):
    def __init__(self, Nombre, Peso, Edad, Especie, Habla):
        super().__init__(Nombre, Peso, Edad)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto15 = Pajaro1('Polly', 0.4, 31, 'Cacatua', 'Si')

Veterinaria1.Mostrar(Objeto15)
Objeto15.Mostrar()

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
        
Objeto16 = Paladin1(65, 'Battle Axe', 25, 'Dark Crystal', 200, 'Ghost Knight')

Objeto16.Mostrar()
Atacante1.Mostrar(Objeto16)
Defensor1.Mostrar(Objeto16)

print (f'-' * 20)

Padre_Hija1 = issubclass(Poke_Kid1, Poke1)
Instancia1 = isinstance(Objeto16, Paladin1)
Instancia2 = isinstance(Objeto16, Defensor1)
Instancia3 = isinstance(Objeto16, Atacante1)

print (f'{Padre_Hija1}')
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

class Efectivo1():
    def Pagar(self):
        print (f'El pago se realizo en Efectivo')
        
class Cripto1():
    def Pagar(self):
        print (f'El pago se realizo en Cripto')
        
class Tarjeta1():
    def Pagar(self):
        print (f'El pago se realizo en Tarjeta')
        
Objeto18 = Efectivo1()
Objeto19 = Cripto1()
Objeto20 = Tarjeta1()

Objeto18.Pagar()
Objeto19.Pagar()
Objeto20.Pagar()

print (f'-' * 20)

class Cuenta_Bancaria1():
    def __init__(self, Dinero):
        self.Dinero = Dinero

    def Depositar(self, Saldo):
        self.Dinero += Saldo
        
    @property
    def Privado(self):
        return self.Dinero
    
    @Privado.setter
    def Privado(self, Nuevo_Saldo):
        self.Dinero = Nuevo_Saldo
        
    def Mostrar(self):
        print (f'Su saldo a la fecha es de ${self.Dinero}')
        
Objeto21 = Cuenta_Bancaria1(100)
Objeto21.Depositar(25)
Objeto21.Mostrar()

print (f'Usted tiene un saldo privado que nunca deberia de mostrarse, y este es {Objeto21.Privado}')

Objeto21.Privado = '50,000,000'

Objeto21.Mostrar()

print (f'Usted tiene un saldo privado que nunca deberia de mostrarse, y este es {Objeto21.Privado}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla1(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla1(Plantilla1):
    def Metodo(self):
        print (f'Esto le pertenece a la subplantilla')
        
    def General(self):
        print (f'Este es el metodo abstracto de la plantilla original')
        
Objeto22 = Sub_Plantilla1()

Objeto22.Metodo()

print (f'-' * 20)

class Chocolate1():
    def Elegir(self):
        return f'Chocolate'
    
class Vainilla1():
    def Elegir(self):
        return f'Vainilla'
    
class Fresa1():
    def Elegir(self):
        return f'Fresa'
    
class Pastel1():
    def __init__(self):
        self.Ingrediente = Chocolate1()
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Ingrediente.Elegir()}')
        
Objeto23 = Pastel1()

Objeto23.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Ingrediente):
        self.Ingrediente = Ingrediente
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Ingrediente.Elegir()}')
        
Ingrediente1 = Chocolate1()

Objeto24 = Pastel2(Ingrediente1)
Objeto24.Hornear()

Ingrediente2 = Vainilla1()

Objeto25 = Pastel2(Ingrediente2)
Objeto25.Hornear()

Ingrediente3 = Fresa1()

Objeto26 = Pastel2(Ingrediente3)
Objeto26.Hornear()

print (f'-' * 20)

class Persona2():
    def __init__(self, Nombre, Apellido):
        self.Nombre = Nombre
        self.Apellido = Apellido

    def Mostrar1(self):
        return self.Nombre
    
    @property
    def Mostrar2(self):
        return self.Nombre
    
    def __str__(self):
        return self.Nombre
    
    def __repr__(self):
        return self.Apellido
    
Objeto27 = Persona2('Erick', 'Perez')

print (f'{Objeto27.Mostrar1()}')
print (f'{Objeto27.Mostrar2}')
print (f'{Objeto27}')
print (f'{Objeto27.Apellido}')

print (f'-' * 20)

Dict_Ventas = {"ana": ["manzana", "pera"], "luis": ["zanahoria", "manzana"]}

def Ejercicio10(Diccionario, Texto):
    for indice, elemento in Diccionario.items():
        for elemento_Finale in elemento[:]:
            if (elemento_Finale == Texto):
                return (f'El producto {elemento_Finale} le pertenece al vendedor {indice}')
            else:
                continue

    return None

Frutita1 = 'berenjena'

Sample10 = Ejercicio10(Dict_Ventas, Frutita1)

if (len(Dict_Ventas) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample10 is None):
        print (f'El producto {Frutita1} no se encontro en ninguno de los vendedores')
    else:
        print (f'{Sample10}')
        
print (f'-' * 20)

Datos2 = {"ana": {"edad": 25, "ciudad": "Quito"}}

def Ejercicio11(Diccionario, User, Field, New_Value):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        Diccionario[User] = {}
        Diccionario[User][Field] = New_Value
        return (False, f'Error, el usuario no existia, fue creado {Diccionario}')
    else:
        Ubicado2 = Ubicado1.get(Field)
        if (Ubicado2 is None):
            Diccionario[User][Field] = New_Value
            return (False, f'Error, el usuario si existe, pero el campo no existia, fue creado {Diccionario}')
        else:
            Diccionario[User][Field] = New_Value
            return (True, f'Exito, tanto el usuario como el campo existian, fue actualizado {Diccionario}')

Usuario2 = 'roberto'
Campo2 = 'telefono'
Nuevo_Valor2 = 123456789

Sample11 = Ejercicio11(Datos2, Usuario2, Campo2, Nuevo_Valor2)

if (Datos2):
    if (Sample11[0] == True):
        print (f'{Sample11[1]}')
    else:
        print (f'{Sample11[1]}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Diccionario5X = {
    'Nombre' : "Erick"
}

print (f'{Diccionario5X}')
print (f'{Diccionario5X.keys()}')
print (f'{Diccionario5X.values()}')
print (f'{Diccionario5X.items()}')
print (f'{Diccionario5X["Nombre"]}')
print (f'{Diccionario5X.get("Nombre")}')

for indice, elemento in Diccionario5X.items():
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

Diccionario6X = {
    'Nombre' : ["Erick"]
}

print (f'{Diccionario6X}')
print (f'{Diccionario6X.keys()}')
print (f'{Diccionario6X.values()}')
print (f'{Diccionario6X.items()}')
print (f'{Diccionario6X["Nombre"][0]}')
print (f'{Diccionario6X.get("Nombre")[0]}') #type: ignore

for indice, elemento in Diccionario6X.items():
    for elemento_Finale in enumerate(elemento[0:None]):
        print (f'{elemento_Finale[0]} : {elemento_Finale[1]}')
        
print (f'-' * 20)

Diccionario7X = {
    'Usuario1' : {
        'Nombre' : "Erick"
    }
}

print (f'{Diccionario7X}')
print (f'{Diccionario7X.keys()}')
print (f'{Diccionario7X.values()}')
print (f'{Diccionario7X.items()}')
print (f'{Diccionario7X["Usuario1"]["Nombre"]}')
print (f'{Diccionario7X.get("Usuario1")["Nombre"]}') #type: ignore

for nivel1_indice, nivel1_valor in Diccionario7X.items():
    for nivel2_indice, nivel2_valor in nivel1_valor.items():
        print (f'{nivel2_indice} : {nivel2_valor}')
        
print (f'-' * 20)

Diccionario8X = {
    'Usuario1' : {
        'Nombre' : ["Erick"]
    }
}

print (f'{Diccionario8X}')
print (f'{Diccionario8X.keys()}')
print (f'{Diccionario8X.values()}')
print (f'{Diccionario8X.items()}')
print (f'{Diccionario8X["Usuario1"]["Nombre"][0]}')
print (f'{Diccionario8X.get("Usuario1")["Nombre"][0]}') #type: ignore

for nivel1_indice, nivel1_valor in Diccionario8X.items():
    for nivel2_indice, nivel2_valor in nivel1_valor.items():
        for indice, elemento in enumerate(nivel2_valor[:], start=1):
            print (f'{indice} : {elemento}')
            
print (f'-' * 20)

Diccionario_Personas = {
    "ana": {"edad": 25, "ciudad": "Quito"},
    "luis": {"edad": 30, "ciudad": "Guayaquil"}
}

def Ejercicio12(Diccionario, User, Field):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        return (False, f'Error, el usuario no se encontro')
    else:
        Ubicado2 = Ubicado1.get(Field)
        if (Ubicado2 is None):
            return (False, f'Error, el usuario si existe, pero el campo no')
        else:
            return (True, f'Ambos Usuario y Campo existen')

Usuario3 = 'ana'
Campo3 = 'telefono'

Sample12 = Ejercicio12(Diccionario_Personas, Usuario3, Campo3)

if (len(Diccionario_Personas) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample12[0] == True):
        print (f'{Sample12[1]}')
    else:
        print (f'{Sample12[1]}')
        
print (f'-' * 20)

Diccionario_Lenguajes2 = dict({"python": 2, "java": 2, "c++": 2, "go": 1})

def Ejercicio13(Diccionario):
    
    Lista_Repetidos = list([])
    
    clave = next(iter(Diccionario))
    valor = Diccionario[clave]
    
    for indice, elemento in Diccionario.items():
        if (elemento > valor):
            clave = indice
            valor = elemento
        else:
            continue
        
    for indice, elemento in Diccionario.items():
        if (elemento == valor):
            Lista_Repetidos.append(indice)
        else:
            continue
        
    if (len(Lista_Repetidos) > 1):
        return Lista_Repetidos
    else:
        return clave

Sample13 = Ejercicio13(Diccionario_Lenguajes2)

if (Diccionario_Lenguajes2):
    if (Sample13):
        print (f'El curso al que mas personas se inscribieron este verano fue {Sample13}')
    else:
        print (f'Error, nadie se inscribio en ningun curso este verano')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Lista_Productos = ["manzana", "zanahoria", "kiwi", "pera", "tomate"]

Canastas = {
    "frutas": [],     # se llenará con frutas
    "verduras": [],   # se llenará con verduras
    "otros": []       # se llenará con lo que no sea fruta ni verdura
}

def Ejercicio14(Lista, Diccionario):
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

Sample14 = Ejercicio14(Lista_Productos, Canastas)

if (Lista_Productos and Canastas):
    for indice, elemento in Sample14.items():
        print (f'{indice} : {elemento}')
else:
    print (f'Error, al menos uno de los contenedores esta vacio')
    
print (f'-' * 20)

Lista_Agrupar = [("fruta","manzana"), ("verdura","zanahoria"), ("fruta","pera"), ("fruta","banana"), ("verdura","tomate")]

def Ejercicio15(Lista):
    Diccionario_Vacio2 = dict({})
    
    for indice, elemento in Lista:
        if (indice not in Diccionario_Vacio2):
            Diccionario_Vacio2[indice] = []
            Diccionario_Vacio2[indice].append(elemento)
        else:
            Diccionario_Vacio2[indice].append(elemento)
            
    return Diccionario_Vacio2

Sample15 = Ejercicio15(Lista_Agrupar)

if (len(Lista_Agrupar) == 0):
    print (f'Error, la lista esta vacia')
else:
    for indice, elemento in Sample15.items():
        print (f'{indice} : {elemento}')
        
print (f'-' * 20)

Datos3 = {
    "ana":  {"edad": 25, "ciudad": "Quito"},
    "luis": {"edad": 30, "ciudad": "Guayaquil"}
    }

def Ejercicio16(Diccionario, User, Field, New_Value):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        return (False, f'Error, el usuario no existe')
    else:
        Ubicado2 = Ubicado1.get(Field)
        if (Ubicado2 is None):
            return (False, f'Error, el usuario existe, pero el campo no')
        else:
            Diccionario[User][Field] = New_Value
            return (True, f'El campo fue actualizado correctamente -> {Diccionario}')

Usuario4 = 'luis'
Campo4 = 'telefono'
Nuevo_Valor4 = 'Santa Barbara'

Sample16 = Ejercicio16(Datos3, Usuario4, Campo4, Nuevo_Valor4)

if (Datos3):
    if (Sample16[0] == True):
        print (f'{Sample16[1]}')
    else:
        print (f'{Sample16[1]}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

def Funcion_Suma(Num1):
    return Num1 + 10

def Funcion_Multiplicacion(Num1):
    return Num1 * 10

def Funcion_Superior1(Funcion, Numero):
    return Funcion(Numero)

print (f'El resultado de la operacion es {Funcion_Superior1(Funcion_Suma, 5)}')
print (f'El resultado de la operacion es {Funcion_Superior1(Funcion_Multiplicacion, 5)}')

print (f'-' * 20)

Lista_Nombres1 = ['Erick', 'Josue', 'Karlita']
Lista_Nombres2 = list(['Carmelo', 'Susanita', 'Roxana'])

def Enlistado1(Lista):
    for indice, elemento in enumerate(Lista, start=1):
        print (f'{indice} : {elemento}')
        
def Enlistado2(Lista):
    for indice, elemento in enumerate(Lista, start=1):
        print (f'{indice} : {elemento}')
        
def Funcion_Elegir_Lista(Funcion, Lista):
    return Funcion(Lista)

Funcion_Elegir_Lista(Enlistado1, Lista_Nombres1)

print (f'-' * 20)

Funcion_Elegir_Lista(Enlistado2, Lista_Nombres2)

print (f'-' * 20)

def Funcion_Suma2(Numero, *args, **kwargs):
    Acumulador = 0
    
    for elemento in kwargs.values():
        Acumulador += elemento
        
    return Numero + sum(args) + Acumulador

def Funcion_Multiplicacion2(Numero, *args, **kwargs):
    Acumulador = 0
    
    for elemento in kwargs.values():
        Acumulador += elemento
        
    return Numero * sum(args) * Acumulador

def Funcion_Superior2(Funcion, Numero, *Numeros, **Numeross):
    return Funcion(Numero, *Numeros, **Numeross)

print (f'El resultado de la operacion es {Funcion_Superior2(Funcion_Suma2, 1, 1, 2, 3, Num1 = 10, Num2 = 20, Num3 = 30)}')
print (f'El resultado de la operacion es {Funcion_Superior2(Funcion_Multiplicacion2, 1, 1, 2, 3, Num1 = 10, Num2 = 20, Num3 = 30)}')

print (f'-' * 20)

Diccionario_Numeral2 = dict({
    'Num1' : 5,
    'Num2' : 1,
    'Num3' : 6,
    'Num4' : 2,
    'Num5' : 3
})

def Elegir_Pares(Diccionario):
    Lista_Pares = []
    
    for indice, elemento in Diccionario.items():
        if (elemento % 2 == 0):
            Lista_Pares.append(indice)
        else:
            continue
        
    return Lista_Pares

def Elegir_ImPares(Diccionario):
    Lista_ImPares = []
    
    for indice, elemento in Diccionario.items():
        if (elemento % 2 != 0):
            Lista_ImPares.extend([indice])
        else:
            continue
        
    return Lista_ImPares

def Funcion_Superior3(Funcion, Diccionario):
    return Funcion(Diccionario)

print (f'Los numeros pares del diccionario son {Funcion_Superior3(Elegir_Pares, Diccionario_Numeral2)}')
print (f'Los numeros impares del diccionario son {Funcion_Superior3(Elegir_ImPares, Diccionario_Numeral2)}')

print (f'-' * 20)

Lista_Animales1 = ['Ornitorrinco']
Lista_Animales2 = list(['Perro'])
Lista_Animales1.append('Avestruz')
Lista_Animales1.insert(1, 'Caballo')
Lista_Animales1.extend(['Pez'])

Lista_Animales3 = Lista_Animales1 + Lista_Animales2

def Ejercicio17(Lista):
    if (len(Lista) == 0):
        return None
    else:
        while (Lista):
            print (f'{Lista}')
            del Lista[-1]

Sample17 = Ejercicio17(Lista_Animales3)

if (Sample17 is None):
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio18(Num1:int, Num2:int, Num3:int) -> int:
    '''Esto es un docstring, se devuelve la suma de los argumentos'''
    return Num1 + Num2 + Num3

print (f'El resultado de la operacion es {Ejercicio18(1, 2, 3)}')

print (f'{help(Ejercicio18)}')

def Ejercicio19(Texto = 'Nada declarado aun'):
    return Texto

print (f'{Ejercicio19()}')

print (f'-' * 20)

def Ejercicio20(Num1, Num2, Num3):
    return Num1 + Num2 + Num3

print (f'El resultado de la operacion es {Ejercicio20(1, 2, 3)}')

print (f'-' * 20)

def Ejercicio21(Num1=1, Num2=2, Num3=3):
    return Num1 + Num2 + Num3

print (f'El resultado de la operacion es {Ejercicio21()}')

print (f'-' * 20)

def Ejercicio22(Num1=1, Num2=2, Num3=3):
    return Num1 + Num2 + Num3

print (f'El resultado de la operacion es {Ejercicio22(10, 20, 30)}')

print (f'-' * 20)

def Ejercicio23(Num1, Num2, Num3=3):
    return Num1 + Num2 + Num3

print (f'El resultado de la operacion es {Ejercicio23(5, 2)}')


def Ejercicio24(*args):
    Promedio = sum(args) / len(args)
    return round(Promedio, 2)

Sample24 = Ejercicio24(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print (f'El promedio de los numeros elegidos es {Sample24}')

def Ejercicio25(**kwargs):
    Acumulador = 0
    
    for _, elemento in kwargs.items():
        Acumulador += elemento
        
    return Acumulador

Sample25 = Ejercicio25(
    Numero1 = 4,
    Numero2 = 6,
    Numero3 = 7
)

print (f'El resultado de la operacion es {Sample25}')

def Ejercicio26(Num1, *nombres, **detalles):
    print (f'Mi numero favorito es {Num1}')
    
    print (f'Nombres: ')
    for indice, elemento in enumerate(nombres, start=1):
        print (f'{indice} : {elemento}')
        
    print (f'-' * 20)
    
    print (f'Detalles del evento: ')
    for indice, elemento in detalles.items():
        print (f'{indice} : {elemento}')

Sample26 = Ejercicio26(
    8,
    'erick', 'josue', 'karlita', 'carmelo', 'roxana',
    fecha = 'domingo',
    lugar = 'Igleasia de Santa Ana',
    tema = 'Gran Bingo Mensual'
)

print (f'-' * 20)

def Ejercicio27(Limite):
    Lista_Fibonacci = [0, 1]
    
    while (len(Lista_Fibonacci) < Limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

Sample27 = Ejercicio27(10)

print (f'La lista Fibonacci es {Sample27}')

print (f'-' * 20)

Lista_Primera = [7, 5]
Lista_Segunda = [6, 9]

def Ejercicio28(Lista1, Lista2):
    if (Lista1 and Lista2):
        Lista_Tercera = list([])
        Set_Conjunto = set({})
        
        for elemento in Lista1[:]:
            if (elemento in Lista2):
                Set_Conjunto.add(elemento)
            else:
                continue
            
        Lista_Tercera = list(Set_Conjunto)
        
        return Lista_Tercera
    else:
        return None

Sample28 = Ejercicio28(Lista_Primera, Lista_Segunda)

if (Sample28 is None):
    print (f'Error, alguna de las dos listas esta vacia')
else:
    if (Sample28):
        print (f'La lista que cumple ambas condiciones es {Sample28}')
    else:
        print (f'No hay ningun numero en las listas que cumpla ambas condiciones')
        
print (f'-' * 20)

Diccionario_Vacio2 = dict.fromkeys('ABC', 'Carrito')

print (f'{Diccionario_Vacio2}')

Diccionario_Vacio3 = dict.fromkeys(['Uno', 'Dos', 'Tres'], 'Hola')

print (f'{Diccionario_Vacio3}')

Diccionario_Vacio4 = dict.fromkeys(['Uno', 'Dos', 'Tres'])

print (f'{Diccionario_Vacio4}')

print (f'-' * 20)

var0 = 25

print (f'{type(var0)}')

var0 += 3.5 # Esto es un casteo implicito, se hace una operacion que cambia el tipo de la variable

print (f'{type(var0)}')

var0 = '50'

print (f'{type(var0)}')

var0 = int(var0) # Esto es un casteo explicito, deliberadamente cambie el tipo de la variable

print (f'{type(var0)}')

print (f'-' * 20)

Lista_Nombres3 = ['Erick']
Lista_Nombres4 = list(['Josue'])

print (f'Una suma de listas las concatena: {Lista_Nombres3 + Lista_Nombres4}')

Tupla_Nombres3 = ('Erick',)
Tupla_Nombres4 = tuple(('Josue',))

print (f'Una suma de tuplas las concatena: {Tupla_Nombres3 + Tupla_Nombres4}')

print (f'-' * 20)

var1 = 0

if (var1):
    print (f'Correcto, se permite numero entero, decimal y negativo')
else:
    print (f'Error, no se permite cero')
    
var2 = ''

if (var2):
    print (f'Correcto, se permite una cadena de texto')
else:
    print (f'Error, esto esta vacio')
    
var3 = list([])

if (var3):
    print (f'Esta lista tiene contenido')
else:
    print (f'Error, esta lista esta vacia')
    
var4 = tuple(('Erick',))

if (var4):
    print (f'Esta tupla tiene contenido')
else:
    print (f'Error, esta tupla esta vacia')
    
var5 = set({1})

if (var5):
    print (f'Este set tiene contenido')
else:
    print (f'Error, este set esta vacio')
    
var6 = dict({
})

if (var6):
    print (f'El diccionario tiene contenido')
else:
    print (f'Error, el diccionario esta vacio')
    
var7 = None

if (var7):
    print (f'Esto tiene asignacion')
else:
    print (f'Error, esto no tiene nada asignado')
    
var8 = not None

if (var8):
    print (f'Esto tiene asignacion')
else:
    print (f'Error, esto no tiene nada asignado')
    
print (f'-' * 20)

Lista_Ejemplo7 = [1, 2, 3, 4, 5]

def Ejercicio29(Lista):
    Contador = 0
    
    while (Contador < len(Lista)):
        Contador += 1
        
    return Contador

Sample29 = Ejercicio29(Lista_Ejemplo7)

if (Sample29):
    print (f'La lista tiene {Sample29} elementos')
else:
    print (f'Error del contador')
    
print (f'-' * 20)

def Ejercicio30(Lista):
    Contador_Pares = 0
    Contador_Impares = 0
    
    for elemento in Lista[0:None]:
        if (elemento % 2 == 0):
            Contador_Pares += elemento
        else:
            Contador_Impares += elemento
            
    return Contador_Pares, Contador_Impares

Sample30 = Ejercicio30(Lista_Ejemplo7)

try:
    Pares1, Impares1 = Sample30
    
    print (f'La suma de los numeros pares es {Pares1}')
    print (f'La suma de los numeros impares es {Impares1}')
except ValueError as Errore1:
    print (f'Error, la declaracion multiple es incorrecto -> {Errore1}')
    
print (f'-' * 20)

def Ejercicio31(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Acumulador = 0
        
        for i in range(0, len(Lista)):
            Acumulador += Lista[i]
            
        return Acumulador

Sample31 = Ejercicio31(Lista_Ejemplo7)

if (Sample31 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample31):
        print (f'La suma de todos los numeros de la lista es {Sample31}')
    else:
        print (f'Tuvimos un error con el acumulador')
        
print (f'-' * 20)

def Ejercicio32(Lista):
    for elemento in Lista[:]:
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    for elemento in Lista[:-1]:
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    for elemento in Lista[:-2]:
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    for elemento in Lista[:-3]:
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    for elemento in Lista[:-4]:
        print (f'{elemento}')
        
    print (f'-' * 20)

if (len(Lista_Ejemplo7) == 0):
    print (f'Error, la lista esta vacia')
else:
    Sample32 = Ejercicio32(Lista_Ejemplo7)
    
print (f'-' * 20)

def Ejercicio33(Lista, Num):
    for elemento in Lista[0:None]:
        if (elemento == Num):
            return elemento
        else:
            continue
        
    return None

Numero1 = 3

if (Lista_Ejemplo7):
    Sample33 = Ejercicio33(Lista_Ejemplo7, Numero1)
    
    if (Sample33 is None):
        print (f'Error, el numero {Numero1} fue encontrado')
    else:
        print (f'El numero {Sample33} fue encontrado en la lista')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio34(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Min = min(Lista)
        Max = max(Lista)
        Lista_Resultados = list([Min, Max])
        
        return Lista_Resultados

Sample34 = Ejercicio34(Lista_Ejemplo7)

if (Sample34 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El menor de los numeros de la lista es {min(Sample34)}')
    print (f'El mayor de los numeros de la lista es {max(Sample34)}')
    
print (f'-' * 20)

def Ejercicio35(Lista, Num):
    Contador = 0
    
    for i in range(0, len(Lista)):
        if (Lista[i] > Num):
            Contador += 1
        else:
            continue
        
    return Contador

Numero2 = 2

Sample35 = Ejercicio35(Lista_Ejemplo7, Numero2)

if (len(Lista_Ejemplo7) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample35):
        print (f'La cantidad de numeros mayores que {Numero2} es {Sample35}')
    else:
        print (f'Error, no hay ningun numero mayor que {Numero2}')
        
print (f'-' * 20)

def Ejercicio36(Lista):
    Lista_Pares = []
    Lista_Impares = list([])
    
    if (len(Lista) == 0):
        return None
    else:
        for elemento in Lista[0:None]:
            if (elemento % 2 == 0):
                Lista_Pares.append(elemento)
            else:
                Lista_Impares.extend([elemento])
                
        return Lista_Pares, Lista_Impares

Sample36 = Ejercicio36(Lista_Ejemplo7)

if (Sample36 is None):
    print (f'Error, la lista esta vacia')
else:
    try:
        Lista_Par, Lista_Impar = Sample36
        
        print (f'Los elementos pares de la lista son {Lista_Par}')
        print (f'Los elementos impares de la lista son {Lista_Impar}')
    except (ValueError, Exception):
        print (f'Error, este desempaquetado de variables es incorrecto')
        
Any_Par1 = any(num % 2 == 0 for num in Lista_Ejemplo7)
Anonima1 = filter(lambda item : item % 2 == 0, Lista_Ejemplo7)
Lista_Par2 = [num for num in Lista_Ejemplo7 if num % 2 == 0]

print (f'{Any_Par1}')
print (f'{list(Anonima1)}')
print (f'{Lista_Par2}')

print (f'-' * 20)

def Ejercicio37(Lista):
    Lista_Mult = []
    
    for elemento in Lista[:]:
        Lista_Mult.append(elemento * 10)
        
    return Lista_Mult

Sample37 = Ejercicio37(Lista_Ejemplo7)

if (Lista_Ejemplo7):
    print (f'Lista Original: {Lista_Ejemplo7}')
    print (f'Lista Multiplicada: {Sample37}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

'''Lista_Promedios = list([])

Limite2 = int(input(f'Ingrese la cantidad de numeros: '))

def Ejercicio38(Lista):
    Contador = 0
    while (Contador < Limite2):
        while (True):
            Numero3 = input(f'Ingrese la nota {Contador + 1}: ')
            try:
                Numero4 = float(Numero3)
                if (Numero4.is_integer()):
                    Lista.append(Numero4)
                    print (f'El numero {Contador + 1} es entero')
                    break
                else:
                    Lista.append(Numero4)
                    print (f'El numero {Contador + 1} es decimal')
                    break
            except ValueError:
                print (f'Error, lo que ingresaste no es un numero')
        Contador += 1
        
    return Lista

Sample38 = Ejercicio38(Lista_Promedios)

Promedio2 = sum(Sample38) / Sample38.__len__()

print (f'El promedio de las notas agregadas es {round(Promedio2, 2)}')'''

Lista_Ejemplo8 = list([5, -6, 0, -8, -3, 0])

def Ejercicio38(Lista):
    Positivos = 0
    Negativos = 0
    Ceros = 0
    
    Contador = 0
    
    while (Contador < len(Lista)):
        if (Lista[Contador] > 0):
            Positivos += 1
        elif (Lista[Contador] < 0):
            Negativos += 1
        else:
            Ceros += 1
            
        Contador += 1
        
    return Positivos, Negativos, Ceros

Sample38 = Ejercicio38(Lista_Ejemplo8)

if (len(Lista_Ejemplo8) == 0):
    print (f'Error, la lista esta vacia')
else:
    Num_Positivos, Num_Negativos, Num_Ceros = Sample38
    
    print (f'Numeros positivos detectados: {Num_Positivos}')
    print (f'Numeros negativos detectados: {Num_Negativos}')
    print (f'Numeros ceros detectados: {Num_Ceros}')
    
print (f'-' * 20)

import pandas as pd
import re

Lista_Ejemplo9 = [
    "juan@gmail.com",
    "hola",
    "maria@hotmail.net",
    "python.org",
    "ana+test@yahoo.org",
    "correo@empresa",
    "pedro123@gmail.com"
]

def Ejercicio39(Lista):
    Lista_Validos = []
    Lista_Invalidos = []
    
    Pattern = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'
    
    for elemento in Lista:
        Buscar = bool(re.fullmatch(Pattern, elemento))
        if (Buscar == True):
            Lista_Validos.append(elemento)
        else:
            Lista_Invalidos.extend([elemento])
            
    return Lista_Validos, Lista_Invalidos

Sample39 = Ejercicio39(Lista_Ejemplo9)

if (Lista_Ejemplo9):
    Correos_Validos, Correos_Invalidos = Sample39
    
    print (f'Lista original: {Lista_Ejemplo9}')
    print (f'Lista correos validos: {Correos_Validos}')
    print (f'Lista correos invalidos: {Correos_Invalidos}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio40(Lista):
    Temporal = Lista[0]
    if (len(Lista) == 0):
        return None
    else:
        for elemento in Lista[0:None]:
            if (elemento > Temporal):
                Temporal = elemento
            else:
                continue
            
        return Temporal

Sample40 = Ejercicio40(Lista_Ejemplo7)

if (Sample40 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero mayor de la lista es {Sample40}')
    
print (f'-' * 20)

def Ejercicio41(Lista):
    Temporal = Lista[0]
    if (len(Lista) == 0):
        return None
    else:
        for elemento in Lista[:]:
            if (elemento < Temporal):
                Temporal = elemento
            else:
                continue
            
        return Temporal

Sample41 = Ejercicio41(Lista_Ejemplo7)

if (Sample41 is None):
    print (f'Error, la lista esta vacia')
else:
    print (f'El numero menor de la lista es {Sample41}')
    
print (f'-' * 20)

Lista_Ejemplo10 = [-15.5, -8, -3.2, -1, 0, 4, 7.5, 12, 19.1, 25]

def Ejercicio42(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Positivos = 0
        Positivos_Sum = 0
        
        for elemento in Lista:
            if (elemento > 0):
                Positivos += 1
                Positivos_Sum += elemento
            else:
                continue
            
        return Positivos, Positivos_Sum
        
Sample42 = Ejercicio42(Lista_Ejemplo10)

if (Sample42 is None):
    print (f'Error, la lista esta vacia')
else:
    try:
        Positivos1, Positivos1_Num = Sample42
        
        print (f'Cantidad de numeros positivos: {Positivos1}')
        print (f'Suma de estos numeros positivos: {Positivos1_Num}')
    except ValueError:
        print (f'Error, este desempaquetado es un asco')
        
print (f'-' * 20)
        
Lista_Ejemplo11 = list([65, 70, 54, 80, 69, 66])

def Ejercicio43(Lista):
    Aprobado = 0
    Reprobado = 0
    Aprobado_Sum = 0
    
    for elemento in Lista[:]:
        if (elemento >= 70):
            Aprobado += 1
            Aprobado_Sum += elemento
        else:
            Reprobado += 1
            
    return Aprobado, Reprobado, Aprobado_Sum

Sample43 = Ejercicio43(Lista_Ejemplo11)

if (len(Lista_Ejemplo11) == 0):
    print (f'Error, la lista esta vacia')
else:
    try:
        Est_Aprobados, Est_Reprobados, Est_Aprobados_Sum = Sample43
        print (f'Estudiantes que aprobaron el curso: {Est_Aprobados}')
        print (f'Estudiantes que aprobaron el curso: {Est_Reprobados}')
        print (f'Suma de todas las notas aprobadas: {Est_Aprobados_Sum}')
    except ValueError as Errore2:
        print (f'Este desempaquetado de variables es incorecto -> {Errore2}')
        
print (f'-' * 20)

Lista_Ejemplo12 = [15, 0, 8, 2, 0, 25, 4]

def Ejercicio44(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Agotado = 0
        Stock_Bajo = 0
        Stock_Alto = 0
        Stock_Bajo_Sum = 0
        Stock_Alto_Sum = 0
        
        for i in range(0, len(Lista)):
            if (Lista[i] == 0):
                Agotado += 1
            elif (Lista[i] >= 1 and Lista[i] <= 5):
                Stock_Bajo += 1
                Stock_Bajo_Sum += Lista[i]
            else:
                Stock_Alto += 1
                Stock_Alto_Sum += Lista[i]
                
        return Agotado, Stock_Bajo, Stock_Alto, Stock_Bajo_Sum, Stock_Alto_Sum

Sample44 = Ejercicio44(Lista_Ejemplo12)

if (Sample44 is None):
    print (f'Error, la lista esta vacia')
else:
    Prod_Agotado, Prod_Stock_Bajo, Prod_Stock_Alto, Prod_Stock_Bajo_Sum, Prod_Stock_Alto_Sum = Sample44
    
    print (f'Productos Agotados del inventario: {Prod_Agotado}')
    print (f'Productos Stock_Bajo del inventario: {Prod_Stock_Bajo}')
    print (f'Productos Stock_Alto del inventario: {Prod_Stock_Alto}')
    print (f'Suma productos con Stock_Bajo: {Prod_Stock_Bajo_Sum}')
    print (f'Suma productos con Stock_Alto: {Prod_Stock_Alto_Sum}')
    print (f'Suma productos con Stock: {Prod_Stock_Bajo_Sum + Prod_Stock_Alto_Sum}')
    
print (f'-' * 20)

Lista_Ejemplo13 = list([12, 8, 5, 1, 7, 2, 10])

def Ejercicio45(Lista):
    for i in range(0, len(Lista)):
        if (Lista[i] == 0):
            return i
        else:
            continue
        
    return None

Sample45 = Ejercicio45(Lista_Ejemplo13)

if (Lista_Ejemplo13):
    if (Sample45 is None):
        print (f'No se han encontrado productos agotados en el inventario')
    else:
        print (f'El primer producto agotado del inventario aparece en la posicion {Sample45}')
else:
    print (f'Error la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejemplo14 = [120, 350, 80, 600, 150, 700]

def Ejercicio46(Lista, Num):
    Lista.sort()
    Lista.sort(reverse = True)
    Lista.reverse()
    for elemento in Lista:
        if (elemento > Num):
            return elemento
        else:
            continue
        
    return None

Limite2 = 70

if (len(Lista_Ejemplo14) == 0):
    print (f'Error, la lista esta vacia')
else:
    Sample46 = Ejercicio46(Lista_Ejemplo14, Limite2)
    if (Sample46 is None):
        print (f'Error, no hay un numero mayor que {Limite2}')
    else:
        print (f'El primer numero mayor que {Limite2} es {Sample46}')
        
print (f'-' * 20)

# Para esto tenemos dos maneras de hacerlo, con dos ciclos for o por medio de un set conjunto

# Metodo 1 con dos ciclos for

Lista_Ejemplo15 = list([10, 1, 2, 4, 3, 5, 6])

def Ejercicio47(Lista):
    for i in range(0, len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                return i
            else:
                continue
            
    return None

Sample47 = Ejercicio47(Lista_Ejemplo15)

if (Lista_Ejemplo15):
    if (Sample47 is None):
        print (f'Error, no hay dos numeros repetidos en la lista')
    else:
        print (f'El primer numero repetido se encontro en la posicion {Sample47} y el numero es {Lista_Ejemplo15[Sample47]}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

# Este es el segundo metodo y aqui usamos un set para evitar repetidos

Lista_Ejemplo16 = list([10, 2, 1, 4, 3, 5, 6])

def Ejercicio48(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista[0:None]:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            
    return None

Sample47 = Ejercicio48(Lista_Ejemplo16)

if (Lista_Ejemplo16):
    if (Sample47 is None):
        print (f'Error, no hay dos numeros repetidos en la lista')
    else:
        print (f'El primer numero repetido de la lista es {Sample47}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejemplo16 = [90, 80, 79, 82]

def Ejercicio49(Lista):
    pass

Sample49 = Ejercicio49(Lista_Ejemplo16)