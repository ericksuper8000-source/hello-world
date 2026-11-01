try:
    import Module_Own as PEPE
except (ImportError, ModuleNotFoundError):
    print (f'Error, el modulo seleccionado no existe')
    raise

class Persona1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
    
    def Mostrar(self):
        return self.Nombre
    
    @property
    def Mostrar2(self):
        return self.Nombre

Objeto1 = Persona1('Erick')

print (f'Mi nombre es {Objeto1}')
print (f'Mi nombre es {Objeto1.Mostrar()}')
print (f'Mi nombre es {Objeto1.Mostrar2}')

print (f'-' * 20)

class Perfil1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre

Lista_Perfiles = list([Perfil1('Erick'), Perfil1('Josue'), Perfil1('Karlita')])

print (f'La lista de perfiles es {Lista_Perfiles}')

print (f'-' * 20)

class Colores1():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre
        
Lista_Colores = [
    Colores1('Rojo'),
    Colores1('Azul'),
    Colores1('Negro')
]

print (f'La lista de colores es {Lista_Colores}')

print (f'-' * 20)

class Inventario1():
    def __init__(self):
        self.Ropa = []
        
    def __len__(self):
        return len(self.Ropa)

Objeto2 = Inventario1()

Objeto2.Ropa.append('Zapatos')
Objeto2.Ropa.insert(1, 'Gorra')
Objeto2.Ropa.extend(['Camiseta'])

print (f'La lista tiene {len(Objeto2)} elementos')

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

class Cajas1():
    def __init__(self, Peso):
        self.Peso = Peso
        
    def __add__(self, Otro):
        return self.Peso + Otro.Peso
        
Objeto5 = Cajas1(5)
Objeto6 = Cajas1(3)

print (f'El resultado de la sumatoria de pesos es {Objeto5 + Objeto6}')

print (f'-' * 20)

class Armario1():
    def __init__(self):
        self.Ropa = [
            'Camiseta',
            'Chaleco',
            'Medias'
        ]
        
    def __getitem__(self, Indice):
        return self.Ropa[Indice]
        
Objeto7 = Armario1()

print (f'El elemento en la posicion 0 es {Objeto7[0]}')
print (f'El elemento en la posicion 1 es {Objeto7[1]}')
print (f'El elemento en la posicion 2 es {Objeto7[2]}')

print (f'-' * 20)

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

Objeto9 = Poke1(PEPE.Diccionario_Poke1['Poke1'], 'Electrico', 'Impact Trueno')
Objeto10 = Poke1(PEPE.Diccionario_Poke1['Poke2'], 'Roca', 'Mega Sismo')

Objeto9.Mostrar()

print (f'Mi pokemon favorito de todos los tiempos es {Objeto9}')
print (f'Mi pokemon favorito de todos los tiempos es {Objeto9.Mostrar2}')

print (f'-' * 20)

Objeto10.Mostrar()

print (f'Mi pokemon favorito de todos los tiempos es {Objeto10}')
print (f'Mi pokemon favorito de todos los tiempos es {Objeto10.Mostrar2}')

print (f'-' * 20)

class Poke_Kid1(Poke1):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto11 = Poke_Kid1(PEPE.Diccionario_Poke1['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke1.Mostrar(Objeto11)
Objeto11.Mostrar()

print (f'Mi pokemon favorito de todos los tiempos es {Objeto11.Nombre}')

print (f'-' * 20)

class Camara():
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada exitosamente')
        
class Reproductor():
    def Reproducir_Musica(self):
        print (f'La musica fue reproducida')
        
class Celular(Camara, Reproductor):
    def Encender_Celular(self):
        print (f'El celular fue encendido')
        
Objeto12 = Celular()

Objeto12.Tomar_Fotografia()
Objeto12.Reproducir_Musica()
Objeto12.Encender_Celular()

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
        
Objeto13 = Perro1('Terry', 3.5, 5, 'Dobberman', 'Asma De Perro')

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
        
Objeto14 = Gato1('Messi', 1.5, 1.8, 'Gris', 'No')

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
        
Objeto15 = Pajaro1('Polly', 0.4, 31, 'Guacamaya Esmeralda', 'Si')

Veterinaria1.Mostrar(Objeto15)
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

Atacante.Mostrar(Objeto16)
Defensor.Mostrar(Objeto16)
Objeto16.Mostrar()

print (f'-' * 20)

Hija_Padre = issubclass(Poke_Kid1, Poke1)
Instancia1 = isinstance(Objeto16, Paladin)
Instancia2 = isinstance(Objeto16, Defensor)
Instancia3 = isinstance(Objeto16, Atacante)

print (f'{Hija_Padre}')
print (f'{Instancia1}')
print (f'{Instancia2}')
print (f'{Instancia3}')

print (f'-' * 20)

class A1():
    def Mostrar(self):
        print (f'Hola yo soy A1')
        
class E1():
    def Mostrar(self):
        print (f'Hola yo soy E1')
        
class B1(E1):
    def Mostrar(self):
        print (f'Hola yo soy B1')
        
class C1(A1):
    def Mostrar(self):
        print (f'Hola yo soy C1')
        
class D1(B1, C1):
    def Mostrar(self):
        print (f'Hola yo soy D1')
        
Objeto17 = D1()

A1.Mostrar(Objeto17)
B1.Mostrar(Objeto17)
C1.Mostrar(Objeto17)
Objeto17.Mostrar()
E1.Mostrar(Objeto17)

print (f'-' * 20)

class Tarjeta():
    def Mostrar(self):
        print (f'El pago se realizo con Tarjeta')
        
class Efectivo():
    def Mostrar(self):
        print (f'El pago se realizo con Efectivo')
        
class Cripto():
    def Mostrar(self):
        print (f'El pago se realizo con Cripto')
        
Objeto18 = Cripto()
Objeto19 = Efectivo()
Objeto20 = Tarjeta()

Objeto18.Mostrar()
Objeto19.Mostrar()
Objeto20.Mostrar()

print (f'-' * 20)

class Cuenta_Bancaria():
    def __init__(self, Efectivo):
        self.Efectivo = Efectivo
        
    def Depositar(self, Dinero):
        self.Efectivo += Dinero
     
    @property   
    def Dinero(self):
        return self.Efectivo
    
    @Dinero.setter
    def Dinero(self, Nuevo_Saldo):
        self.Efectivo = Nuevo_Saldo
        
    def Mostrar(self):
        print (f'Tu saldo a la fecha es de ${self.Efectivo}')
        
Objeto19 = Cuenta_Bancaria(100)
Objeto19.Depositar(25)
Objeto19.Mostrar()

print (f'Tu saldo privado que no deberias compartir es {Objeto19.Efectivo}')

Objeto19.Efectivo = '50,000,000'

Objeto19.Mostrar()

print (f'Tu saldo privado que no deberias compartir es {Objeto19.Efectivo}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla(Plantilla):
    def Mostrar(self):
        print (f'Este es el metodo de la subplantilla')
        
    def General(self):
        print (f'Este es el encapsulamiento')
        
Objeto20 = Sub_Plantilla()

Objeto20.Mostrar()
Objeto20.General()

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
        
Objeto21 = Pastel1()

Objeto21.Hornear()

print (f'-' * 20)

class Pastel2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Ingrediente1 = Chocolate()

Objeto22 = Pastel2(Ingrediente1)
Objeto22.Hornear()

Ingrediente2 = Vainilla()

Objeto23 = Pastel2(Ingrediente2)
Objeto23.Hornear()

Ingrediente3 = Fresa()

Objeto24 = Pastel2(Ingrediente3)
Objeto24.Hornear()

print (f'-' * 20)

Ventas1 = {"ana": ["manzana", "pera"], "luis": ["zanahoria", "manzana"]}

def Ejercicio1(Diccionario, Cosa):
    for indice, elemento in Diccionario.items():
        for finale in elemento[:]:
            if (finale == Cosa):
                return (True, indice)
            else:
                continue
            
    return None

Item1 = 'manzana'

Sample1 = Ejercicio1(Ventas1, Item1)

if (len(Ventas1) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample1 is None):
        print (f'No se encontro')
    else:
        print (f'El articulo {Item1} estaba en el inventario de {Sample1[1]}')
        
print (f'-' * 20)

Datos1 = {"jose": {"edad": 25, "ciudad": "Quito"}}

def Ejercicio2(Diccionario, User, Field, Value):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        Diccionario[User] = {}
        Diccionario[User][Field] = Value
        return (False, "usuario creado")
    else:
        Ubicado2 = Ubicado1.get(Field)
        if (Ubicado2 is None):
            Diccionario[User][Field] = Value
            return (False, "campo nuevo")
        else:
            Diccionario[User][Field] = Value
            return (True, "Informacion actualizada")

Usuario = 'ana'
Campo = 'ciudad'
Nuevo_Elemento = 'San Jose'

if (Datos1):
    Sample2 = Ejercicio2(Datos1, Usuario, Campo, Nuevo_Elemento)
    if (Sample2[0] == True):
        print (f'{Sample2[1]}')
    else:
        print (f'{Sample2[1]}')
else:
    print (f'Error, el diccionario anidado esta vacio')
    
print (f'-' * 20)

Diccionario1X = {
    'Nombre' : "Erick",
    'Edad' : 37,
    'Votante' : not False
}

for indice, elemento in Diccionario1X.items():
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

Diccionario2X = {
    'Nombre' : ['Erick', 'Josue', 'Karlita'],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
}

for _, elemento1 in Diccionario2X.items():
    for indice, elemento2 in enumerate(elemento1[0:None], 2):
        print (f'{indice} : {elemento2}')
        
print (f'-' * 20)

Diccionario3X = {
    'Usuario1' : {
        'Nombre' : "Erick",
        'Edad' : 37,
        'Votante' : True
    },

    'Usuario2' : {
        'Nombre' : "Josue",
        'Edad' : 20,
        'Votante' : True
    }
}

for nivel1_clave, nivel1_valor in Diccionario3X.items():
    for nivel2_clave, nivel2_valor in nivel1_valor.items():
        print (f'{nivel2_clave} : {nivel2_valor}')
        
print (f'-' * 20)

Diccionario4X = {
    'Usuario1' : {
        'Nombre' : ["Erick", "Josue", "Karlita"],
        'Edad' : [37, 20, 6],
        'Votante' : [True, not False, False]
    },

    'Usuario2' : {
        'Nombre' : ["Carmelo", "Susanita", "Roxana"],
        'Edad' : [55, 14, 26],
        'Votante' : [True, False, not False]
    },
}

for nivel1_clave, nivel1_valor in Diccionario4X.items():
    for nivel2_clave, nivel2_valor in nivel1_valor.items():
        for finale1, finale2 in enumerate(nivel2_valor[:]):
            print (f'{finale1} : {finale2}')

print (f'-' * 20)

Diccionario5X = {
    "ana": {"edad": 25, "ciudad": "Quito"},
    "luis": {"edad": 30, "ciudad": "Guayaquil"}
}

def Ejercicio3(Diccionario, User, Field):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        return (False, f'El usuario esta incorrecto')
    else:
        Ubicado2 = Ubicado1.get(Field)
        if (Ubicado2 is not None):
            return (True, f'Tanto el usuario como el campo son correctos')
        else:
            return (False, f'El campo esta incorrecto')

Usuario2 = 'luis'
Campo2 = 'telefono'

if (len(Diccionario5X) == 0):
    print (f'Error el diccionario anidado esta vacio')
else:
    Sample3 = Ejercicio3(Diccionario5X, Usuario2, Campo2)
    if (Sample3[0] == True):
        print (f'{Sample3[1]}')
    else:
        print (f'{Sample3[1]}')
        
print (f'-' * 20)

Diccionario_Lenguaje1 = dict({"python": 2, "java": 2, "c++": 2, "go": 1})

def Ejercicio4(Diccionario):
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

Sample4 = Ejercicio4(Diccionario_Lenguaje1)

if (Sample4 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample4):
        print (f'Nombre lenguaje: {Sample4}')
    else:
        print (f'Error de asignacion de lenguaje')
        
print (f'-' * 20)

Lista_Productos = ["manzana", "zanahoria", "kiwi", "pera", "tomate"]

Canastas = {
    "frutas": [],     # se llenará con frutas
    "verduras": [],   # se llenará con verduras
    "otros": []       # se llenará con lo que no sea fruta ni verdura
}

def Ejercicio5(Lista, Diccionario):
    
    fruta = ["manzana","banana","pera"]
    verdura = ["zanahoria","lechuga","tomate"]
    
    for elemento in Lista[0:None]:
        if (elemento in fruta):
            Diccionario["frutas"].append(elemento)
        elif (elemento in verdura):
            Diccionario["verduras"].append(elemento)
        else:
            Diccionario["otros"].append(elemento)
            
    return Diccionario

if (Lista_Productos and Canastas):
    Sample5 = Ejercicio5(Lista_Productos, Canastas)
    if (Sample5):
        print (f'{Sample5}')
    else:
        print (f'Error diccionario invalido')
else:
    print (f'Error, al menos uno de estos elementos esta vacio')
    
print (f'-' * 20)

Lista_Agrupar = [("fruta","manzana"), ("verdura","zanahoria"), ("fruta","pera"), ("fruta","banana"), ("verdura","tomate")]

def Ejercicio6(Lista):
    Diccionario_Vacio = dict({})
    for elemento1, elemento2 in Lista:
        if (elemento1 not in Diccionario_Vacio):
            Diccionario_Vacio[elemento1] = []
            Diccionario_Vacio[elemento1].append(elemento2)
        else:
            Diccionario_Vacio[elemento1].append(elemento2)
            
    return Diccionario_Vacio

Sample6 = Ejercicio6(Lista_Agrupar)

if (Lista_Agrupar):
    if (Sample6):
        for valor, elemento in Sample6.items():
            for finale in elemento[:]:
                print (f'{finale}')
    else:
        print (f'Error de diccionario vacio')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Datos2 = {
    "ana":  {"edad": 25, "ciudad": "Quito"},
    "luis": {"edad": 30, "ciudad": "Guayaquil"}
    }

def Ejercicio7(Diccionario, User, Field, Value):
    Ubicado1 = Diccionario.get(User)
    if (Ubicado1 is None):
        return (False, f'Error, el usuario no existe')
    else:
        Ubicado2 = Ubicado1.get(Field)
        if (Ubicado2 is None):
            return (False, f'Error, el campo no existe')
        else:
            Diccionario[User][Field] = Value
            return (True, f'{Diccionario}')
    
Usuario3 = 'luis'
Campo3 = 'edad'
Nuevo_Elemento3 = '890'

Sample7 = Ejercicio7(Datos2, Usuario3, Campo3, Nuevo_Elemento3)

if (len(Datos2) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample7[0] == True):
        print (f'{Sample7[1]}')
    else:
        print (f'{Sample7[1]}')
        
print (f'-' * 20)

def Superior_Sumar(Num1):
    return Num1 + 10

def Superior_Multiplicar(Num1):
    return Num1 * 10

def Elegir_Operacion(Funcion, Numero):
    return Funcion(Numero)

print (f'El resultado de la operacion es {Elegir_Operacion(Superior_Sumar, 2)}')
print (f'El resultado de la operacion es {Elegir_Operacion(Superior_Multiplicar, 2)}')

print (f'-' * 20)

Lista_Nombres1 = ['Erick', 'Josue', 'Karlita']
Lista_Nombres2 = list(['Carmelo', 'Susanita', 'Roxana'])

def Listador1(Lista):
    return Lista

def Listador2(Lista):
    return Lista

def Elegir_Listador(Funcion, Lista):
    return Funcion(Lista)

print (f'Los elementos de la lista son {Elegir_Listador(Listador1, Lista_Nombres1)}')
print (f'Los elementos de la lista son {Elegir_Listador(Listador2, Lista_Nombres2)}')

print (f'-' * 20)

def Superior_Sumar2(Num, *args, **kwargs):
    Acumulador = 0
    for elemento in kwargs.values():
        Acumulador += elemento
        
    return Num + sum(args) + Acumulador

def Superior_Multiplicar2(Num, *args, **kwargs):
    Acumulador = 0
    for elemento in kwargs.values():
        Acumulador += elemento
        
    return Num * sum(args) * Acumulador

def Elegir_Operacion2(Funcion, Numero, *argumentos, **kwargumentos):
    return Funcion(Numero, *argumentos, **kwargumentos)

print (f'El resultado de la operacion es {Elegir_Operacion2(Superior_Sumar2, 1, 1, 2, 3, 4, 5, Numerito1=10, Numerito2=50)}')
print (f'El resultado de la operacion es {Elegir_Operacion2(Superior_Multiplicar2, 1, 1, 2, 3, 4, 5, Numerito1=10, Numerito2=50)}')

print (f'-' * 20)

Diccionario_Numeral1 = {
    'Num1' : 7,
    'Num2' : 1,
    'Num3' : 4,
    'Num4' : 2,
    'Num5' : 5
}

def Superior_Pares(Diccionario):
    Lista_Pares = list([])
    for indice, elemento in Diccionario.items():
        if (elemento % 2 == 0):
            Lista_Pares.append(indice)
        else:
            continue
        
    return Lista_Pares
        
def Superior_Impares(Diccionario):
    Lista_ImPares = list([])
    for indice, elemento in Diccionario.items():
        if (elemento % 2 != 0):
            Lista_ImPares.append(indice)
        else:
            continue
        
    return Lista_ImPares
        
def Elegir_Diccionario(Funcion, Diccionario):
    return Funcion(Diccionario)

print (f'Los elementos pares del diccionario son {Elegir_Diccionario(Superior_Pares, Diccionario_Numeral1)}')
print (f'Los elementos impares del diccionario son {Elegir_Diccionario(Superior_Impares, Diccionario_Numeral1)}')

print (f'-' * 20)

Lista_Animales1 = ['Jirafa', 'Perro']
Lista_Animales1.append('Colibri')
Lista_Animales1.insert(2, 'Manati')
Lista_Animales1.extend(['Leon'])

while (Lista_Animales1 ):
    print (f'{Lista_Animales1}')
    del Lista_Animales1[-1]
    
print (f'-' * 20)

def Ejercicio8(Num1:int, Num2:int) -> int:
    '''Docstring, tomamos dos argumentos, los sumamos y devolvemos el resultado'''
    return Num1 + Num2

print (f'El resultado de la operacion es {Ejercicio8(12, 4)}')

print (f'{help(Ejercicio8)}')

print (f'-' * 20)

def Ejercicio9(Texto = 'Nada que decir'):
    return Texto

print (f'{Ejercicio9()}')

def Ejercicio10(Num1, Num2):
    return Num1 + Num2

Sample10 = Ejercicio10(12, 4)

print (f'El resultado de la operacion es {Sample10}')

print (f'-' * 20)

def Ejercicio11(Num1=12, Num2=4):
    return Num1 + Num2

Sample11 = Ejercicio11()

print (f'El resultado de la operacion es {Sample11}')

print (f'-' * 20)

def Ejercicio12(Num1=12, Num2=4):
    return Num1 + Num2

Sample12 = Ejercicio12(1, 2)

print (f'El resultado de la operacion es {Sample12}')

print (f'-' * 20)

def Ejercicio13(Num1, Num2, Num3=100):
    return Num1 + Num2 + Num3

Sample13 = Ejercicio13(1, 2)

print (f'El resultado de la operacion es {Sample13}')

print (f'-' * 20)

def Ejercicio14(*args):
    Promedio = sum(args) / len(args)
    return Promedio

Sample14 = Ejercicio14(
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
)

print (f'El promedio de los numeros agregados es {round(Sample14, 2)}')

print (f'-' * 20)

def Ejercicio15(**kwargs):
    for indice, elemento in kwargs.items():
        print (f'{indice} : {elemento}')
        
Sample15 = Ejercicio15(
    Nombre = 'Erick',
    Edad = 37,
    Votante = True
)

print (f'-' * 20)

def Ejercicio16(**kwargs):
    Acumulador = 0
    for _, elemento in kwargs.items():
        Acumulador += elemento
        
    return Acumulador

Sample16 = Ejercicio16(
    Num1 = 2,
    Num2 = 6,
    Num3 = 9,
    Num4 = 1,
    Num5 = 4,
    Num6 = 7,
    Num7 = 3
)

print (f'El resultado de la operacion es {Sample16}')

print (f'-' * 20)

def Ejercicio17(*participantes, **detalles):
    print (f'Participantes: ')
    for elemento in participantes[0:None]:
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    print (f'Detalles del evento: ')
    for indice, elemento in detalles.items():
        print (f'{indice} : {elemento}')

Sample17 = Ejercicio17(
    'Jose', 'Ramiro', 'Alexandria',
    Fecha = 'Domingo',
    Lugar = 'Iglesia de Santa barbara',
    Tema = 'Gran Bingo Anual'
)

print (f'-' * 20)

def Ejercicio18(Limite):
    Lista_Fibonacci = [0, 1]
    
    while (len(Lista_Fibonacci) < Limite):
        Temporal = Lista_Fibonacci[-2] + Lista_Fibonacci[-1]
        Lista_Fibonacci.append(Temporal)
        
    return Lista_Fibonacci

Sample18 = Ejercicio18(10)

print (f'La lista Fibanacci es {Sample18}')

print (f'-' * 20)

Lista_Primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
Lista_Segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]

def Ejercicio19(Lista1, Lista2):
    Set_Conjunto3 = set({})
    Lista3 = []
    if (Lista1 and Lista2):
        for elemento in Lista1[0:None]:
            if (elemento in Lista2):
                Set_Conjunto3.add(elemento)
            else:
                continue
    else:
        return None
    
    Lista3 = list(Set_Conjunto3)
    
    return Lista3

Sample19 = Ejercicio19(Lista_Primera, Lista_Segunda)

if (Sample19 is None):
    print (f'Error, alguna de las 2 listas esta vacia')
else:
    if (Sample19):
        print (f'La lista que cumple estas condiciones es {Sample19}')
    else:
        print (f'Error, no hay ningun elemento que cumpla estas condiciones')
        
print (f'-' * 20)

var0 = 5

print (f'{type(var0)}')

var0 += 3.4

print (f'{type(var0)}')

print (f'-' * 20)

var0 = 5
print (f'{type(var0)}')

var0 = str(500)

print (f'{type(var0)}')

print (f'-' * 20)

Lista_Nombres3 = ['Erick']
Lista_Nombres4 = list(['Josue'])

Tupla_Nombres3 = ('Erick',)
Tupla_Nombres4 = 'Josue',

print (f'{Lista_Nombres3 + Lista_Nombres4}')

print (f'{Tupla_Nombres3 + Tupla_Nombres4}')

# Truthness de numero puede ser entero positivo, entero negativo, decimal positivo o decimal negativo, nunca cero

var1 = 0

if (var1):
    print (f'Truthness de numero puede ser entero positivo, entero negativo, decimal positivo o decimal negativo, nunca cero')
else:
    print (f'Error, dije que nunca puede ser cero')
    
print (f'-' * 20)

# Con esta condicion debe tener texto, nunca vacio
var2 = ''

if (var2):
    print (f'Con esta condicion debe tener texto, nunca vacio')
else:
    print (f'Error, esto no puede irse vacio')
    
print (f'-' * 20)

# La lista nunca puede estar vacia
var3 = []

if (var3):
    print (f'La lista tiene contenido')
else:
    print (f'Error, la lista no puede estar vacia')
    
print (f'-' * 20)

var4 = {}

if (var4):
    print (f'El diccionario tiene contenido')
else:
    print (f'Error, el diccionario no puede estar vacio')
    
print (f'-' * 20)

var5 = None

if (var5):
    print (f'Esto esta bonito')
else:
    print (f'Error, esto esta None')
    
print (f'-' * 20)

if not (var5):
    print (f'Esto esta bonito')
else:
    print (f'Error, esto esta None')
    
print (f'-' * 20)

Lista_Ejemplo1 = [1, 2, 3, 4, 5]

def Ejercicio20(Lista):
    if (Lista):
        Contador = 0
        
        while (Contador < len(Lista)):
            Contador += 1
    else:
        return None
    
    return Contador

Sample20 = Ejercicio20(Lista_Ejemplo1)

if (Sample20 is None):
    print (f'Error, la lista esta vacia')
else:
    if (Sample20):
        print (f'La cantidad de elementos en la lista es {Sample20}')
    else:
        print (f'Se produjo un error, la lista aparece vacia')
        
print (f'-' * 20)

def Ejercicio21(Lista):
    Acumulador1 = 0
    Acumulador2 = 0
    
    for elemento in Lista[:]:
        if (elemento % 2 == 0):
            Acumulador1 += elemento
        else:
            Acumulador2 += elemento
            
    return Acumulador1, Acumulador2

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    Sample21 = Ejercicio21(Lista_Ejemplo1)
    try:
        Total1, Total2 = Sample21
        
        print (f'La suma de los numeros pares es {Total1}')
        print (f'La suma de los numeros impares es {Total2}')
    except ValueError:
        print (f'El desempaquetado esta mal hecho')
        
print (f'-' * 20)

def Ejercicio22(Lista):
    Acumulador = 0
    for elemento in Lista:
        Acumulador += elemento
        
    return Acumulador

Sample22 = Ejercicio22(Lista_Ejemplo1)

if (Lista_Ejemplo1):
    print (f'El resultado de sumar todos los numeros de la lista es {Sample22}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio23(Lista):
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

Sample23 = Ejercicio23(Lista_Ejemplo1)

if (Sample23 is None):
    print (f'Error, la lista esta vacia')
else:
    Total1, Total2, Total3, Total4 = Sample23
    
    print (f'El resultado de sumar todos los elementos de la lista es {Total1}')
    print (f'El resultado de sumar todos los elementos de la lista es {Total2}')
    print (f'El resultado de sumar todos los elementos de la lista es {Total3}')
    print (f'El resultado de sumar todos los elementos de la lista es {Total4}')
    
print (f'-' * 20)

def Ejercicio24(Lista, Num):
    for elemento in Lista[0:None]:
        if (elemento == Num):
            return elemento
        else:
            continue
        
    return None

Numero1 = 2

Sample24 = Ejercicio24(Lista_Ejemplo1, Numero1)

if (Lista_Ejemplo1):
    if (Sample24 is None):
        print (f'El numero {Numero1} no fue encontrado en la lista')
    else:
        print (f'El numero {Sample24} fue encontrado')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio25(Lista):
    Lista_Resultado = []
    Min = min(Lista)
    Max = max(Lista)
    Lista_Resultado = [Min, Max]
    
    return Lista_Resultado

Sample25 = Ejercicio25(Lista_Ejemplo1)

if (len(Lista_Ejemplo1) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample25):
        print (f'El menor de los numeros de la lista es {min(Sample25)}')
        print (f'El mayor de los numeros de la lista es {max(Sample25)}')
        
print (f'-' * 20)

def Ejercicio26(Lista, Num):
    Contador = 0
    for elemento in Lista[:]:
        if (elemento > Num):
            Contador += 1
        else:
            continue
        
    return Contador

Numero2 = 3

Sample26 = Ejercicio26(Lista_Ejemplo1, Numero2)

if (Lista_Ejemplo1):
    if (Sample26):
        print (f'La cantidad de numeros mayores que {Numero2} es {Sample26}')
    else:
        print (f'Error, no hay numeros mayores que {Numero2}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio27(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Lista_Pares = []
        Lista_Impares = list([])
        
        Contador = 0
        while (Contador < len(Lista[0:None])):
            if (Lista[Contador] % 2 == 0):
                Lista_Pares.append(Lista[Contador])
            else:
                Lista_Impares.extend([Lista[Contador]])
            Contador += 1
            
        return Lista_Pares, Lista_Impares

Sample27 = Ejercicio27(Lista_Ejemplo1)

if (Sample27 is None):
    print (f'Error, la lista esta vacia')
else:
    Lista_Num_Pares, Lista_Num_Impares = Sample27
    
    print (f'Lista Original: {Lista_Ejemplo1}')
    print (f'Lista Pares: {Lista_Num_Pares}')
    print (f'Lista Impares: {Lista_Num_Impares}')
    
print (f'-' * 20)

def Ejercicio28(Lista):
    Lista_Mult = list([])
    
    for elemento in Lista:
        Lista_Mult.append(elemento * 100)
        
    return Lista_Mult

Sample28 = Ejercicio28(Lista_Ejemplo1)

if (Lista_Ejemplo1):
    if (len(Sample28) == 0):
        print (f'Error la lista multiplicar esta mal')
    else:
        print (f'Lista Original: {Lista_Ejemplo1}')
        print (f'Lista Actualizada: {Sample28}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

'''Lista_Promedios = []

Contador = 0

while (Contador < 3):
    while (True):
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

print (f'El promedio de las notas agregadas es {round(Promedio1, 2)}')'''

Lista_Ejemplo2 = list([5, -6, 0, -8, -3, 0])

def Ejercicio29(Lista):
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

Sample29 = Ejercicio29(Lista_Ejemplo2)

if (Sample29 is None):
    print (f'Error, la lista esta vacia')
else:
    Num_Positivos, Num_Negativos, Num_Ceros = Sample29
    
    print (f'La cantidad de numeros Positivos es {Num_Positivos}')
    print (f'La cantidad de numeros Negativos es {Num_Negativos}')
    print (f'La cantidad de numeros Ceros es {Num_Ceros}')
    
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

def Ejercicio30(Lista):
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

Sample30 = Ejercicio30(Lista_Ejemplo3)

if (len(Lista_Ejemplo3) == 0):
    print (f'Error, la lista esta vacia')
else:
    Lista_Correos_Validos, Lista_Correos_Invalidos = Sample30
    
    print (f'{Lista_Ejemplo3}')
    print (f'{Lista_Correos_Validos}')
    print (f'{Lista_Correos_Invalidos}')
    
print (f'-' * 20)

def Ejercicio31(Lista):
    Temporal = Lista[0]
    for elemento in Lista:
        if (elemento > Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

Sample31 = Ejercicio31(Lista_Ejemplo1)

if (Lista_Ejemplo1):
    print (f'El numero mayor de la lista es {Sample31}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

def Ejercicio32(Lista):
    Temporal = Lista[0]
    for elemento in Lista:
        if (elemento < Temporal):
            Temporal = elemento
        else:
            continue
        
    return Temporal

Sample32 = Ejercicio32(Lista_Ejemplo1)

if (Lista_Ejemplo1):
    print (f'El numero menor de la lista es {Sample32}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejemplo4 = [-15.5, -8, -3.2, -1]

def Ejercicio33(Lista):
    if (Lista):
        Contador = 0
        Acumulador = 0
        for elemento in Lista[:]:
            if (elemento > 0):
                Contador += 1
                Acumulador += elemento
            else:
                continue
    else:
        return None
    
    return Contador, Acumulador

Sample33 = Ejercicio33(Lista_Ejemplo4)

if (Sample33 is None):
    print (f'Error, la lista esta vacia')
else:
    Total_Positivos, Sum_Positivos = Sample33
    
    if (Total_Positivos > 0):
        print (f'El total de numeros positivos: {Total_Positivos}')
        print (f'Suma de los numeros positivos: {Sum_Positivos}')
    else:
        print (f'Error, no hay numeros positivos en la lista')
        
print (f'-' * 20)

Lista_Ejemplo5 = list([65, 70, 54, 80, 69, 66])

def Ejercicio34(Lista):
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

Sample34 = Ejercicio34(Lista_Ejemplo5)

if (len(Lista_Ejemplo5) == 0):
    print (f'Error, la lista esta vacia')
else:
    Alumnos_Aprobados, Alumnos_Reprobados, Alumnos_Aprobados_Sum = Sample34
    
    print (f'Cantidad de alumnos aprobados: {Alumnos_Aprobados}')
    print (f'Cantidad de alumnos aprobados: {Alumnos_Reprobados}')
    print (f'Suma de las notas aprobadas: {Alumnos_Aprobados_Sum}')
    
print (f'-' * 20)

Lista_Ejemplo6 = [15, 0, 8, 2, 0, 25, 4]

def Ejercicio35(Lista):
    if (len(Lista) == 0):
        return None
    else:
        Agotados = 0
        Stock_Bajo = 0
        Stock_Alto = 0
        Stock_Bajo_Sum = 0
        Stock_Alto_Sum = 0
        
        for elemento in Lista[0:None]:
            if (elemento == 0):
                Agotados += 1
            elif (elemento >= 1 and elemento <= 5):
                Stock_Bajo += 1
                Stock_Bajo_Sum += elemento
            else:
                Stock_Alto += 1
                Stock_Alto_Sum += elemento
                
        return Agotados, Stock_Bajo, Stock_Bajo_Sum, Stock_Alto, Stock_Alto_Sum

Sample35 = Ejercicio35(Lista_Ejemplo6)

if (Sample35 is None):
    print (f'Error, la lista esta vacia')
else:
    Prod_Agotados, Prod_Stock_Bajo, Prod_Stock_Alto, Prod_Stock_Bajo_Sum, Prod_Stock_Alto_Sum = Sample35
    
    print (f'Productos agotados: {Prod_Agotados}')
    print (f'Productos Stock_Bajo: {Prod_Stock_Bajo}')
    print (f'Productos Stock_Alto: {Prod_Stock_Alto}')
    print (f'Suma de productos con Stock_Bajo_Sum: {Prod_Stock_Bajo_Sum}')
    print (f'Suma de productos con Stock_Alto_Sum: {Prod_Stock_Alto_Sum}')
    print (f'Suma de todos los productos con stock: {Prod_Stock_Bajo_Sum + Prod_Stock_Alto_Sum}')
    
print (f'-' * 20)

Lista_Ejemplo7 = list([12, 8, 5, 1, 7, 2, 10])

def Ejercicio36(Lista):
    Lista.sort()
    Lista.sort(reverse = True)
    Lista.reverse()

    Contador = 0
    while (Contador < len(Lista)):
        if (Lista[Contador] == 0):
            return Contador
        else:
            Contador += 1
            continue
        
    return None

Sample36 = Ejercicio36(Lista_Ejemplo7)

if (len(Lista_Ejemplo7) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample36 is None):
        print (f'No hay ningun producto agotado en el inventario')
    else:
        print (f'El primer producto agotado de la lista aparece en la posicion {Sample36}')
        
print (f'-' * 20)

Lista_Ejemplo8 = [120, 350, 80, 600, 150, 700]

def Ejercicio37(Lista, Num):
    Lista.sort()
    Contador = 0
    while (Contador < len(Lista)):
        if (Lista[Contador] > Num):
            return Contador
        else:
            Contador += 1
            continue
        
    return None

Numero3 = 700

if (Lista_Ejemplo8):
    Sample37 = Ejercicio37(Lista_Ejemplo8, Numero3)
    if (Sample37 is None):
        print (f'No hay ninguna venta que supere el limite ${Numero3}')
    else:
        print (f'El primer numero que supera el limite esta en la posicion {Sample37} y el numero es {Lista_Ejemplo8[Sample37]}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

# Metodo numero 1 con Set_Conjunto

Lista_Ejemplo9 = list([10, 2, 1, 4, 3, 5, 6])

def Ejercicio38(Lista):
    Set_Conjunto = set({})
    
    for elemento in Lista:
        if (elemento in Set_Conjunto):
            return elemento
        else:
            Set_Conjunto.add(elemento)
            
    return None

Sample38 = Ejercicio38(Lista_Ejemplo9)

if (len(Lista_Ejemplo9) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample38 is None):
        print (f'No hay ningun numero que se repita en la lista')
    else:
        print (f'El primer numero repetido de la lista es {Sample38}')
        
print (f'-' * 20)

# Metodo dos con dos for ciclos

Lista_Ejemplo10 = list([10, 1, 2, 4, 3, 5, 6])

def Ejercicio39(Lista):
    for i in range(0, len(Lista)):
        for j in range(i + 1, len(Lista)):
            if (Lista[i] == Lista[j]):
                return i
            else:
                continue
            
    return None

Sample39 = Ejercicio39(Lista_Ejemplo10)

if (len(Lista_Ejemplo10) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample39 is None):
        print (f'Error, no hay ningun numero repetido en la lista')
    else:
        print (f'El primer numero repetido aparece en la posicion {Sample39} y es {Lista_Ejemplo10[Sample39]}')
        
print (f'-' * 20)

Lista_Ejemplo11 = [90, 89, 79, 70]

def Ejercicio40(Lista):
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] < Lista[i]):
            return i
        else:
            continue
        
    return None

if (Lista_Ejemplo11):
    Sample40 = Ejercicio40(Lista_Ejemplo11)
    if (Sample40 is None):
        print (f'Error, no hay ningun aumento de ventas')
    else:
        print (f'El primer aumento de ventas aparece en la posicion {Sample40} y el monto es ${Lista_Ejemplo11[Sample40]}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Lista_Ejemplo12 = list([100, 97, 95, 80, 78])

def Ejercicio41(Lista, Caida):
    Anterior = 0
    Actual = 0
    Grados = 0
    for i in range(0 + 1, len(Lista)):
        if (Lista[i - 1] - Lista[i] >= Caida):
            Anterior = Lista[i - 1]
            Actual = Lista[i]
            Grados = Lista[i - 1] - Lista[i]
            
            return Anterior, Actual, Grados
        else:
            continue
        
    return None

Limite1 = 30

Sample41 = Ejercicio41(Lista_Ejemplo12, Limite1)

if (len(Lista_Ejemplo12) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample41 is None):
        print (f'En la ultima hora no han habido caidas de temperatura')
    else:
        Temp_Anterior, Temp_Actual, Temp_Grados = Sample41
        
        print (f'Alerta!')
        print (f'Se ha registrado una caida de {Temp_Grados} grados en la ultima hora')
        print (f'Temperatura de la hora anterior: {Temp_Anterior}')
        print (f'Temperatura actual: {Temp_Actual}')
        
print (f'-' * 20)

Lista_Ejemplo13 = [1, 1, 2, 8, 3]

def Ejercicio42(Lista):
    for i in range(0 + 2, len(Lista)):
        if (Lista[i - 2] < Lista[i - 1] > Lista[i]):
            return i - 1
        else:
            continue
        
    return None

Sample42 = Ejercicio42(Lista_Ejemplo13)

if (Lista_Ejemplo13):
    if not (Sample42):
        print (f'No se registro un pico en ventas')
    else:
        print (f'El pico en ventas sucede en la posicion {Sample42} - ({Lista_Ejemplo13[Sample42]})')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

# Consultar valores ✅ Consultar.

Capitales = {"Costa Rica": "San José", "México": "Ciudad de México", "Argentina": "Buenos Aires", "Italia": "Roma",  "España": "Madrid"}

def Ejercicio43(Diccionario, Textico):
    if (len(Diccionario) == 0):
        return None
    else:
        Ubicado1 = Diccionario.get(Textico)
        if (Ubicado1 is not None):
            return (True, f'La capital de {Textico} es {Ubicado1}')
        else:
            return (False, f'Error, en el diccionario no aparece la capital de {Textico}')

Pais = 'Italia'

Sample43 = Ejercicio43(Capitales, Pais)

if (Sample43 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample43[0] == True):
        print (f'{Sample43[1]}')
    else:
        print (f'{Sample43[1]}')
        
print (f'-' * 20)

Productos1 = {"Laptop": 1200, "Mouse": 25, "Teclado": 45, "Monitor": 300}

def Ejercicio44(Diccionario, Articulo):
    Ubicado1 = Diccionario.get(Articulo)
    if (Ubicado1 is None):
        return (False, f'Error, el producto seleccionado no existe')
    else:
        return (True, f'{Ubicado1}')

Item2 = 'Escoba'

Sample44 = Ejercicio44(Productos1, Item2)

if (len(Productos1) == 0):
    print (f'Error el diccionario esta vacio')
else:
    if (Sample44[0] == True):
        print (f'El precio del articulo {Item2} es ${Sample44[1]}')
    else:
        print (f'{Sample44[1]}')
        
print (f'-' * 20)

# Actualizar elementos ✅ Actualizar.

Productos2 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300
}

def Ejercicio45(Diccionario, Articulo, Precio):
    Ubicado1 = Diccionario.get(Articulo)
    if (Ubicado1 is None):
        return (False, f'Error, no se puede actualizar el precio del articulo {Articulo}, ya que no existe')
    else:
        Diccionario[Articulo] = Precio
        return (True, f'{Diccionario}')

Item3 = 'Teclado'
Item3_Price = 60

if (len(Productos2) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Sample45 = Ejercicio45(Productos2, Item3, Item3_Price)
    if (Sample45[0] == True):
        print (f'{Sample45[1]}')
    else:
        print (f'{Sample45[1]}')
        
print (f'-' * 20)
        
# Agregar elementos ✅ Agregar.

Productos3 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio46(Diccionario, Articulo, Precio):
    Ubicado1 = Diccionario.get(Articulo)
    if (Ubicado1 is None):
        Diccionario[Articulo] = Precio
        return (True, f'{Diccionario}')
    else:
        return (False, f'Error, el producto ya existe no se puede volver a agregar')

Item4 = 'Teclado'
Item4_Price = 200

Sample46 = Ejercicio46(Productos3, Item4, Item4_Price)

if (len(Productos3) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample46[0] == True):
        print (f'{Sample46[1]}')
    else:
        print (f'{Sample46[1]}')
        
print (f'-' * 20)

# Eliminar elementos ✅ Eliminar.

Productos4 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45
}

def Ejercicio47(Diccionario, Articulo):
    Ubicado1 = Diccionario.get(Articulo)
    if (Ubicado1 is not None):
        del Diccionario[Articulo]
        return (True, f'Correcto, el elemento fue eliminado')
    else:
        return (False, f'No se puede eliminar {Articulo}, ya que no esta en el diccionario')

Item5 = 'Laptop'

Sample47 = Ejercicio47(Productos4, Item5)

if (Productos4):
    if (Sample47[0] == True):
        print (f'{Sample47[1]}')
    else:
        print (f'{Sample47[1]}')
else:
    print (f'Error, el diccionario esta vacio')
    
print (f'-' * 20)

Productos5 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 5000,
    "Impresora": 180
}

def Ejercicio48(Diccionario):
    Clave = next(iter(Diccionario))
    Valor = Diccionario[Clave]
    
    for indice, elemento in Diccionario.items():
        if (elemento > Valor):
            Clave = indice
            Valor = elemento
        else:
            continue
        
    return Clave, Valor

Sample48 = Ejercicio48(Productos5)

if (len(Productos5) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    Clave1, Valor1 = Sample48
    
    print (f'{Clave1} : {Valor1}')
    
print (f'-' * 20)

Ventas2 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio49(Diccionario, Num):
    if (len(Diccionario) == 0):
        return None
    else:
        Diccionario_Sorted = dict(sorted(Diccionario.items(), key=lambda item : item[1]))
        for indice, elemento in Diccionario_Sorted.items():
            if (elemento > Num):
                return indice
            else:
                continue
            
        return False
    
Limite2 = 70

Sample49 = Ejercicio49(Ventas2, Limite2)

if (Sample49 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample49 == False):
        print (f'No hay ninguna venta que supere al limite')
    else:
        print (f'La venta superior al limite sucedio el {Sample49}')
        
print (f'-' * 20)

Productos6 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio50(Diccionario, Num):
    Contador = 0
    for elemento in Diccionario.values():
        if (elemento > Num):
            Contador += 1
        else:
            continue
        
    return Contador

Limite3 = 2000

Sample50 = Ejercicio50(Productos6, Limite3)

if (Productos6):
    if (Sample50):
        print (f'La cantidad de productos cuyo precio es mayor al limite es {Sample50}')
    else:
        print (f'Error, no hay ningun producto cuyo precio sea mayor que ${Limite3}')
else:
    print (f'Error, el diccinario esta vacio')
    
print (f'-' * 20)

Ventas3 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio51(Diccionario):
    Acumulador = 0
    if (len(Diccionario) == 0):
        return None
    else:
        for elemento in Diccionario.values():
            Acumulador += elemento
            
        return Acumulador

Sample51 = Ejercicio51(Ventas3)

if (Sample51 is None):
    print (f'Error, el diccionario esta vacio')
else:
    print (f'La suma de cada elemento del diccionario es {Sample51}')
    
print (f'-' * 20)

Ventas4 = {
    "Lunes": 120,
    "Martes": 450,
    "Miércoles": 80,
    "Jueves": 600,
    "Viernes": 300
}

def Ejercicio52(Diccionario, Num):
    Acumulador = 0
    for elemento in Diccionario.values():
        if (elemento > Num):
            Acumulador += elemento
        else:
            continue
        
    return Acumulador

Limite4 = 5000

Sample52 = Ejercicio52(Ventas4, Limite4)

if (len(Ventas4) == 0):
    print (f'Error, el diccinario esta vacio')
else:
    if (Sample52):
        print (f'La suma de los numeros mayores que el limite ${Limite4} es ${Sample52}')
    else:
        print (f'Error, no hay ventas mayores que el limite ${Limite4}')
        
print (f'-' * 20)

Productos7 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio53(Diccionario, Num):
    if (len(Diccionario) == 0):
        return None
    else:
        Contador = 0
        Acumulador = 0
        for _, elemento in Diccionario.items():
            if (elemento > Num):
                Contador += 1
                Acumulador += elemento
            else:
                continue
            
        return Contador, Acumulador
    
Limite5 = 6000

Sample53 = Ejercicio53(Productos7, Limite5)

if (Sample53 is None):
    print (f'Error, el diccionario esta vacio')
else:
    Contador1, Acumulador1 = Sample53
    if (Contador1 and Acumulador1):
        print (f'Productos con precio mayor que el limite: {Contador1}')
        print (f'Suma de los precios mayores que el limite: {Acumulador1}')
    else:
        print (f'Error, no hay ninguna venta superior al limite {Limite5}')
        
print (f'-' * 20)

Productos8 = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Impresora": 180
}

def Ejercicio54(Diccionario, Num):
    Diccionario_Sorted = dict(sorted(Diccionario.items(), key=lambda item : item[1]))
    for indice, elemento in Diccionario_Sorted.items():
        if (elemento > Num):
            return indice
        else:
            continue
        
    return None

Limite6 = 5000

Sample54 = Ejercicio54(Productos8, Limite6)

if (len(Productos8) == 0):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample54 is None):
        print (f'No hay ningun producto cuyo precio sea mayor que {Limite6}')
    else:
        print (f'El primer producto cuyo precio es mayor que el limite es {Sample54}')
        
print (f'-' * 20)

Lista_Lenguaje1 = ["python", "java", "python", "c++", "java", "python", "go", "c++", "python"]

def Ejercicio55(Lista):
    Diccionario_Vacio = dict({})
    
    for elemento in Lista[:]:
        if (elemento not in Diccionario_Vacio):
            Diccionario_Vacio[elemento] = 0
            Diccionario_Vacio[elemento] += 1
        else:
            Diccionario_Vacio[elemento] += 1
            
    return Diccionario_Vacio

Sample55 = Ejercicio55(Lista_Lenguaje1)

if (len(Lista_Lenguaje1) == 0):
    print (f'Error, la lista esta vacia')
else:
    for indice, elemento in Sample55.items():
        print (f'{indice} : {elemento}')
        
print (f'-' * 20)

'''def Ejercicio56(Numero):
    try:
        Numero2 = float(Numero)
        if (Numero2.is_integer()):
            print (f'Lo que ingresaste es un numero entero {Numero2}')
        else:
            print (f'Lo que ingresaste es un numero decimal {Numero2}')
    except ValueError:
        print (f'Error, lo que ingresaste no es un numero')

Sample56 = Ejercicio56(PEPE.Flotante1)

print (f'-' * 20)

Resultado1 = eval(PEPE.Flotante2)

print (f'El resultado de la operacion es {Resultado1}')

def Ejercicio57(Cadena):
    Cadena2 = Cadena.replace(' ', '')
    if (isinstance(Cadena2, (str))):
        if (Cadena2.isalpha()):
            print (f'Lo que ingresaste es un texto: {Cadena2}')
        else:
            print (f'Error 1')
    else:
        print (f'Error 2')

Sample57 = Ejercicio57(PEPE.Flotante3)

print (f'-' * 20)

def Ejercicio58(Cadena):
    Lista_Cadena = Cadena.split(' ')
    
    for elemento in Lista_Cadena[0:None]:
        print (f'{elemento}')
        
    print (f'La cantidad de palabras ingresadas es {len(Lista_Cadena)}')

Sample58 = Ejercicio58(PEPE.Flotante4)'''

'''Lista_Alumno = list([])

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Ejercicio56(Lista):
    for elemento in range(Contador):
        Alumno = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Lista.append(Alumno)
        
    return Lista

Sample56 = Ejercicio56(Lista_Alumno)

print (f'La lista de alumnos es {Sample56}')'''

'''Lista_Alumnos = []

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
    
    print (f'El menor de los alumnos es {Menore} y su edad es {Lista[0][1]}')
    print (f'El mayor de los alumnos es {Mayore} y su edad es {Lista[-1][1]}')

Sample56 = Colegio(Lista_Alumnos)'''

Paises1 = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia"
}

def Ejercicio56(Diccionario, Code):
    if (len(Diccionario) == 0):
        return None
    else:
        Ubicado1 = Diccionario.get(Code)
        if (Ubicado1 is not None):
            return Ubicado1
        else:
            return False
    
Codigo1 = 'wt'

Sample56 = Ejercicio56(Paises1, Codigo1)

if (Sample56 is None):
    print (f'Error, el diccionario esta vacio')
else:
    if (Sample56 == False):
        print (f'Error, el pais no existe')
    else:
        print (f'Pais: {Sample56}, Codigo: {Codigo1}')
        
print (f'-' * 20)

class Persona2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __str__(self):
        return self.Nombre
        
    def Mostrar(self):
        return f'{self.Nombre}'
    
    @property
    def Mostrar2(self):
        return f'{self.Nombre}'
        
Objeto25 = Persona2('Erick Josue')

print (f'Mi nombre es {Objeto25}')
print (f'Mi nombre es {Objeto25.Mostrar()}')
print (f'Mi nombre es {Objeto25.Mostrar2}')

print (f'-' * 20)

class Colores2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __repr__(self):
        return self.Nombre
        
Lista_Colores2 = [
    Colores2('Amarilla'),
    Colores2('Rojo'),
    Colores2('Azul')
]

print (f'La lista de colores es {Lista_Colores2}')

print (f'-' * 20)

class Inventario2():
    def __init__(self):
        self.Productos = list([])
        
    def __len__(self):
        return len(self.Productos)
        
Objeto26 = Inventario2()

Objeto26.Productos.append('Cuaderno')
Objeto26.Productos.insert(1, 'Lapicero')
Objeto26.Productos.extend(['Borrador'])

print (f'Esta lista tiene {len(Objeto26)} elementos')

print (f'-' * 20)

class Igualdad2():
    def __init__(self, Nombre):
        self.Nombre = Nombre
        
    def __eq__(self, Otro):
        return self.Nombre == Otro.Nombre
        
Objeto27 = Igualdad2('Panda Rojo')
Objeto28 = Igualdad2('Panda Rojo')

if (Objeto27 == Objeto28):
    print (f'Los objetos son iguales')
else:
    print (f'Error, los objetos no son iguales')
    
print (f'-' * 20)

class Sumatoria0():
    def __init__(self, Num1):
        self.Num1 = Num1
        
    def __add__(self, Otro):
        return self.Num1 + Otro.Num1
    
Objeto29 = Sumatoria0(5)
Objeto30 = Sumatoria0(3)

print (f'El resultado de la sumita es {Objeto29 + Objeto30}')

print (f'-' * 20)

class Armario2():
    def __init__(self):
        self.Ropita = [
            'Camiseta',
            'Pantalon',
            'Zapatos'
        ]
        
    def __getitem__(self, Indice):
        return self.Ropita[Indice]
        
Objeto31 = Armario2()

print (f'El elemento en la posicion 0 es {Objeto31[0]}')
print (f'El elemento en la posicion 1 es {Objeto31[1]}')
print (f'El elemento en la posicion 2 es {Objeto31[2]}')

print (f'-' * 20)

class Panaderia2():
    def __init__(self):
        self.Panes = list([
            'Croissant',
            'Baguette',
            'Donas'
        ])
        
    def __iter__(self):
        return iter(self.Panes)
        
Objeto32 = Panaderia2()

for indice, elemento in enumerate(Objeto32, start=1):
    print (f'{indice} : {elemento}')
    
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
    Fech1_Formateado = pd.to_datetime(Fech1)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato invalido')
    exit()
    
Cargar_Csv1['TOTALITO'] = Cargar_Csv1['quantity'] * Cargar_Csv1['price']
    
Encontrado1 = Cargar_Csv1[Cargar_Csv1['date'].dt.date == Fech1_Formateado.date()]

if (Encontrado1.empty):
    print (f'No se ha encontrado ventas en esta fecha')
else:
    print (f'Genial! se han encontrado ventas en esta fecha')
    
    Grupo1 = Encontrado1.groupby('product')['quantity'].sum()
    Grupo1_Min = Grupo1.idxmin()
    Grupo1_Max = Grupo1.idxmax()
    Grupo1_Min_Cant = Grupo1.min()
    Grupo1_Max_Cant = Grupo1.max()
    
    print (f'La cantidad de productos vendidos en esta fecha fue {Grupo1.sum()}')
    print (f'En la fecha {Fech1_Formateado} el producto {Grupo1_Min} vendio {Grupo1_Min_Cant} unidades')
    print (f'En la fecha {Fech1_Formateado} el producto {Grupo1_Max} vendio {Grupo1_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron en esta fecha fue {Grupo1.count()}')
    
    Promedio1 = Grupo1.sum() / Grupo1.count()
    
    print (f'El promedio de productos vendidos fue {round(Promedio1, 2)}')
    print (f'El promedio de productos vendidos fue {round(Grupo1.mean(), 2)}')
    
    print (f'-' * 20)
    
    Grupo2 = Encontrado1.groupby('product')['TOTALITO'].sum()
    
    print (f'La cantidad de dinero vendido en esta fecha fue ${Grupo2.sum()}')
    
    Promedio2 = Grupo2.sum() / Grupo1.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Promedio2, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue ${round(Grupo2.mean(), 2)}')
    
print (f'-' * 20)

var6 = '3'

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
    var7 = float(var6)
    if (var7.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except (ValueError, Exception):
    print (f'Error, esto no es un numero')
    
print (f'-' * 20)

var7 = 3.5

if (isinstance(var7, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, esto no es un numero decimal')
    
try:
    var8 = float(var7)
    if (var8.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError as Errore1:
    print (f'Error, esto no es un numero -> {str(Errore1)}')
    
print (f'-' * 20)

var9 = 3.5

if (isinstance(var9, (int, float))):
    print (f'Lo que ingresaste es un numero entero o decimal')
else:
    print (f'Error, el formato es incorrecto')
    
try:
    var10 = float(var9)
    if (var10.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except (ValueError, TypeError, Exception):
    print (f'Error, esto no es un numero')
    
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

Texto1_Version4 = re.sub('\!|\@', '', Texto1_Version3)

print (f'{Texto1_Version4}')

Texto1_Version5 = Texto1_Version4.title()

print (f'{Texto1_Version5}')

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

Pattern1 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar1 = re.findall(Pattern1, Texto2)

print (f'{Buscar1}')

for elemento in Buscar1[0:None]:
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

Pattern2 = r'\!|\?|\.{2,}|[0-9]{3,}\-\d{1,4}'

Buscar2 = re.sub(Pattern2, '', Texto3)

print (f'{Buscar2}')

print (f'-' * 20)

# Version2

Pattern3 = r'[^a-zA-Z0-9\s]+'

Buscar3 = re.sub(Pattern3, '', Texto3)

print (f'{Buscar3}')

# Version3

Texto3_temp1 = Texto3

Pattern4 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:hotmail|yahoo|gmail)\.[a-z]{2,}'

Correos1 = re.findall(Pattern4, Texto3)

print (f'{Correos1}')

for i, email in enumerate(Correos1, start=1):
    Texto3_temp1 = Texto3_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto3_temp1}')

Pattern5 = r'\!|\?|\.{2,}|[0-9]+\-\d{4,}'

Texto3_temp2 = re.sub(Pattern5, '', Texto3_temp1)

print (f'{Texto3_temp2}')

for i, email, in enumerate(Correos1, start=1):
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

Pattern6 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}'

Correos2 = re.findall(Pattern6, Texto4)

print (f'{Correos2}')

Texto4_temp1 = Texto4

for i, email, in enumerate(Correos2, start=1):
    Texto4_temp1 = Texto4_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto4_temp1}')

Pattern7 = r'\!|\?'

Texto4_temp2 = re.sub(Pattern7, '', Texto4_temp1)

print (f'{Texto4_temp2}')

for i, email in enumerate(Correos2, start=1):
    Texto4_temp2 = Texto4_temp2.replace(f'SAMPLE{i}', email)
    
print (f'{Texto4_temp2}')

print (f'-' * 20)

for elemento in PEPE.Diccionario_Poke1.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in PEPE.Diccionario_Poke1.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for indice, elemento in PEPE.Diccionario_Poke1.items():
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

for elemento in PEPE.Diccionario_Poke1:
    print (f'{PEPE.Diccionario_Poke1[elemento]}')
    
print (f'-' * 20)

'''Lista_Promedios = []

Contador = 0

while (Contador < 3):
    while (True):
        Numero4 = input(f'Ingrese la nota {Contador + 1}: ')
        try:
            Numero5 = float(Numero4)
            if (Numero5.is_integer()):
                print (f'La nota {Contador + 1} es un numero entero')
                Lista_Promedios.append(Numero5)
                break
            else:
                print (f'La nota {Contador + 1} es un numero decimal')
                Lista_Promedios.extend([Numero5])
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')
    Contador += 1
    
Promedio3 = sum(Lista_Promedios) / len(Lista_Promedios)

print (f'El promedio de las notas ingresadas es {round(Promedio3, 2)}')'''

'''Esto
Es
Un
DocString
Comment'''

# \D palabras letras sin numeros
# \d numeros sin letras solo numeros
# \w todo menos caracteres especiales
# \W solo caracteres especiales
# \s solo espacios
# \S todo menos espacios
# [0-9]+ Solo numeros enteros del cero al nueve
# [a-z] Solo letras minusculas
# [A-Z] Solo letras mayusculas
# ? 0 o 1
# * 0 o mas elementos
# + 1 o mas elementos
# $ termina con 
# ^ inicia con
# [^] cualquiera cosa menos lo que hay en el parentesis
# h.la el punto se reemplaza por cualquier valor

import re

Texto5 = 'esto es un 15 texto cualquiera hola pero 850 lo que hela quiero 123 @ es asegurarme que! esto funciona hila bien o no'

Buscar4 = re.search(r'quiero', Texto5)

print (f'{Buscar4}')

Buscar5 = re.search(r'^esto', Texto5)

Buscar6 = re.search(r'o$', Texto5)

print (f'{Buscar5}')
print (f'{Buscar6}')

Buscar7 = re.findall(r'\d+', Texto5)

print (f'{Buscar7}')

Buscar8 = bool(re.fullmatch(r'esto es un 15 texto cualquiera pero 850 lo que quiero 123 \@ es asegurarme que\! esto funciona bien o no', Texto5))

if (Buscar8 == True):
    print (f'El texto es igual')
else:
    print (f'Error, el texto no es igual')
    
Buscar9 = re.findall(r'[0-9]+', Texto5)

print (f'{Buscar9}')

Buscar10 = re.findall(r'h.la', Texto5)

print (f'{Buscar10}')

Buscar11 = re.findall(r'\d+\s\W', Texto5)

print (f'{Buscar11}')

Texto6 = 'abestebatodoba'

Buscar12 = re.findall(r'[ab]{1,3}', Texto6)

print (f'{Buscar12}')

Buscar13 = re.findall(r'[0-9]{2,4}|h.la', Texto5)

print (f'{Buscar13}')

print (f'-' * 20)

import re

Texto7 = 'ericksuper80@hotmail.com'

Pattern8 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.[a-z]{2,}$'

Buscar14 = bool(re.fullmatch(Pattern8, Texto7))

if (Buscar14 == True):
    print (f'El correo electronico tiene un formato correcto')
else:
    print (f'Error, el correo electronico es invalido')
    
print (f'-' * 20)

import re

Pattern9 = r'^[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)$'

Buscar15 = bool(re.match(Pattern9, Texto7))

if (Buscar15 == True):
    print (f'El correo electronico 2 tiene un formato correcto')
else:
    print (f'Error, el correo electronico 2 es invalido')
    
print (f'-' * 20)

import re

Texto8 = '31'

Pattern10 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar15 = bool(re.match(Pattern10, Texto8))

if (Buscar15 == True):
    print (f'El numero se encuentra entre 1 y 31')
else:
    print (f'Error, el numero esta fuera de rango')
    
print (f'-' * 20)

import re

Texto9 = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'

Pattern11 = r'\d{2}\/[0-9]{2,}\/\d{2,4}'

Replace11 = 'XX/XX/XXXX'

Buscar16 = re.sub(Pattern11, Replace11, Texto9)

print (f'{Buscar16}')

Pattern12 = r'\+\d{1}\-[0-9]{1,3}\-\d{3,}\-[0-9]{4}'

Replace12 = 'Ph0n3_Nvmb3r'

Buscar17 = re.sub(Pattern12, Replace12, Buscar16)

print (f'{Buscar17}')

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
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

import re

Texto11 = """
Hola!!! Mi nombre es Erick123...
Mi correo es: erick.perez@gmail.com!!!
Mi número es: 8888-7777???
Gracias!!!
"""

# Version 1

Pattern14 = r'\!|\?|\.{2,}|\d{3,}\-[0-9]{4}'

Buscar18 = re.sub(Pattern14, '', Texto11)

print (f'{Buscar18}')

print (f'-' * 20)

# Version 2

Pattern15 = r'[^a-zA-Z0-9\s]+'

Buscar19 = re.sub(Pattern15, '', Texto11)

print (f'{Buscar19}')

print (f'-' * 20)

# Version 3

Texto11_temp1 = Texto11

Pattern16 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Correos3 = re.findall(Pattern16, Texto11)

print (f'{Correos3}')

for i, email in enumerate(Correos3, start=1):
    Texto11_temp1 = Texto11_temp1.replace(email, f'SAMPLE{i}')
    
print (f'{Texto11_temp1}')

Pattern17 = r'\!|\?|\.{2,}|\d{3,}\-[0-9]{1,4}'

Texto11_temp2 = re.sub(Pattern17, '', Texto11_temp1)

print (f'{Texto11_temp2}')

print (f'-' * 20)

var11 = 3.5

if (isinstance(var11, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Error, esto no es un numero decimal')
    
try:
    var12 = float(var11)
    if (var12.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, lo que ingresaste no es un numero')
    
print (f'-' * 20)

import pandas as pd
import requests
import io

Ruta_Html1 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html1, headers=headers)

Leer_Html = io.StringIO(Response.text)

Cargar_Html1 = pd.read_html(Leer_Html)

print (f'{Cargar_Html1[2].head()}')

print (f'-' * 20)

import pandas as pd

Data_Frame1 = pd.DataFrame({
    'Nombre' : ["Erick", "Josue", "Karlita"],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
})

print (f'{Data_Frame1}')

Grupo3 = Data_Frame1.groupby('Nombre')['Edad'].sum()
Grupo3_Min = Grupo3.idxmin()
Grupo3_Max = Grupo3.idxmax()
Grupo3_Min_Cant = Grupo3.min()
Grupo3_Max_Cant = Grupo3.max()

print (f'La suma de todas las edades es {Grupo3.sum()}')

print (f'La menor de las personas es {Grupo3_Min} y su edad es {Grupo3_Min_Cant} años')
print (f'La mayor de las personas es {Grupo3_Max} y su edad es {Grupo3_Max_Cant} años')

print (f'La cantidad de personas en el DataFrame es {Grupo3.count()}')

Promedio3 = Grupo3.sum() / Grupo3.count()

print (f'El promedio de las edades es {round(Promedio3, 2)}')
print (f'El promedio de las edades es {round(Grupo3.mean(), 2)}')

print (f'La menos de las edades es {Grupo3.min()}')
print (f'La mayor de las edades es {Grupo3.max()}')

print (f'-' * 20)

var13 = '3'

if (isinstance(var13, (int))):
    print (f'Lo que se ingreso es un numero entero')
else:
    print (f'Error lo que se ingreso no es un numero entero')
    
if (var13.isnumeric()):
    print (f'Lo que se ingreso es un numero entero')
else:
    print (f'Error lo que se ingreso no es un numero entero')
    
if (var13.isdecimal()):
    print (f'Lo que se ingreso es un numero entero')
else:
    print (f'Error lo que se ingreso no es un numero entero')
    
try:
    var14 = float(var13)
    if (var14.is_integer()):
        print (f'Lo que se ingreso es un numero entero')
    else:
        print (f'Lo que se ingreso es un numero decimal')
except ValueError:
    print (f'Error, lo que se ingreso no es un numero')
    
print (f'-' * 20)

import re

Texto12 = "   Hola!!!   mundo@@   123   "

print (f'{Texto12}')

Texto12_Version1 = Texto12.strip()

print (f'{Texto12_Version1}')

Texto12_Version2 = ' '.join(Texto12_Version1.split())

print (f'{Texto12_Version2}')

Texto12_Version3 = Texto12_Version2.lower()

print (f'{Texto12_Version3}')

Texto12_Version4 = re.sub(r'\!|\@|\d+', '', Texto12_Version3)

print (f'{Texto12_Version4}')

Texto12_Version5 = Texto12_Version4.title()

print (f'{Texto12_Version5}')

print (f'-' * 20)

var15 = 5
var16 = 'hola'

try:
    Resultado = var15 + var16 #type: ignore
except TypeError as Errore2:
    print (f'Error, estos datos no pueden operarse -> {str(Errore2)}')
    
var17 = ['Uno', 'Dos', 'Tres']

try:
    var17.remove('Cuatro')
except ValueError:
    print (f'Error, este elemento no puede borrarse')
    
var17 = tuple(('Uno', 'Dos',))

try:
    snake_case1, snake_case2, snake_case3 = var17
except ValueError:
    print (f'Error, Este desempaquetado esta mal')
    
import pandas as pd
from datetime import datetime
    
Fecha2 = 'hola-04-01'

try:
    Fech2 = datetime.strptime(Fecha2, '%Y-%m-%d').date()
    Fech2_Formateada = pd.to_datetime(Fech2)
    Cargar_Csv1['date'] = pd.to_datetime(Cargar_Csv1['date'])
except ValueError:
    print (f'Error, la fecha tiene un formato invalido')
    
var18 = 'hola'

try:
    print (f'{int(var18)}')
except ValueError:
    print (f'Error, esta variable no puede convertirse en otro tipo')
    
try:
    print (f'{var17.index("Tres")}')
except ValueError:
    print (f'Error, este indice no existe')
    
try:
    print (f'{int(var17)}') #type: ignore
except Exception:
    print (f'Error, este elemento no se le puede cambiar el tipo')
    
print (f'-' * 20)

var18 = dict({
    'Nombre' : "Erick"
})
    
try:
    # var17.index("Tres")
    # Resultado = var16 + var17
    # Resultado = 20 / 0
    # print (f'El elemento es {var17[2]}')
    # print (f'{var18["Edad"]}')
    '''with open ('C:\\Repo\\HolaMndo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Linea = Docu.readline()
        print (f'{Documento_Linea}')
        Docu.close()'''
    import Modul_Own as PEPE2 #type: ignore
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
except Exception:
    print (f'Error, esto es un Exception')
    
print (f'-' * 20)

var18 = 'hola'

try:
    Resultado = 1 + var18 #type: ignore
except TypeError:
    print (f'Error, esto es un texto')
    
print (f'-' * 20)

'''def Exception1():
    while (True):
        Numero4 = input(f'Ingrese un numero: ')
        try:
            Numero5 = float(Numero4)
            if (Numero5.is_integer()):
                print (f'Lo que ingresaste es un numero entero')
                break
            else:
                print (f'Lo que ingresaste es un numero decimal')
                break
        except ValueError:
            print (f'Error, lo que ingresaste no es un numero')

Exception1()'''

def Exception2(Num1, Num2):
    try:
        Resultado = Num1 + Num2
        print (f'El resultado de la operacion es {Resultado}')
    except (TypeError, Exception):
        print (f'Error, esta operacion no puede realizarse')
        
Exception2(12, 'hola')

print (f'-' * 20)

def Exception3(Num1:int, Num2:int) -> int: #type: ignore
    '''Esto Es un DocString, dos argumentos se les realiza una division'''
    try:
        Resultado = Num1 / Num2
        print (f'El resultado de la division es {round(Resultado, 2)}')
    except ZeroDivisionError:
        print (f'Error, el divisor no puede ser cero')
        
Exception3(12, 0)

print (f'{help(Exception3)}')

Lista_Exception4 = list(['Erick', 'Josue', 'Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento con indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, este indice esta fuera de rango')

Exception4(3)

print (f'-' * 20)

Diccionario_Exception5 = dict({
    'Nombre' : "Erick",
    'Edad' : 37
})

def Exception5(clave):
    try:
        print (f'El elemento con la clave {clave} es {Diccionario_Exception5[clave]}')
    except KeyError:
        print (f'Error, la clave esta fuera de rango')

Exception5('Nombre')

print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
    Documento_SobreEscribir = Docu.write(f'Hiena')
    Docu.close()

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Linea = Docu.readline()
        print (f'{Documento_Linea}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nTortuga'])
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        print (f'{Documento_Lineas}')
        Docu.close()
except FileNotFoundError as Errore3:
    print (f'Error, el archivo no fue encontrado')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write('\nCerdo')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Leer = Docu.read()
        print (f'{Documento_Leer}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines([f'\nCatarina Pequeña', f'\nCatarina Mediana', f'\nCatarina Grande'])
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Linea = Docu.readline()
        print (f'{Documento_Linea}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSerpiente')
    Documento_Agregar = Docu.write(f'\nCaballo')
    Documento_Agregar = Docu.write(f'\nPez Globo')
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        # print (f'{Documento_Lineas}')
        for elemento in Documento_Lineas[0:None]:
            if (elemento.strip() == 'Caballo'):
                print (f'The name of this animal is horse in english')
                break
            else:
                continue
        print (f'El animal no se encontro')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')
    
print (f'-' * 20)

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        # print (f'{Documento_Lineas}')
        for elemento in Documento_Lineas[:]:
            print (f'{elemento.strip().upper()}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')
    
print (f'-' * 20)

with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.writelines(f'\n')
    Documento_Agregar = Docu.writelines([f' - '.join(PEPE.Set_Conjunto_Poke1)])
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Leer = Docu.read()
        print (f'{Documento_Leer}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')
    
print (f'-' * 20)

import pandas as pd

Data_Frame2 = pd.DataFrame({
    'Nombre' : ['Erick', 'Josue', 'Karlita'],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
})

Data_Frame3 = pd.DataFrame({
    'Nombre' : ['Carmelo', 'Susanita', 'Roxana'],
    'Edad' : [55, 14, 26],
    'Votante' : [True, False, not False]
})

Data_Frame2_Age = Data_Frame2['Edad']

print (f'La menor de las edades es {Data_Frame2_Age.min()}')
print (f'La mayor de las edades es {Data_Frame2_Age.max()}')

Data_Frame_Concatenate = pd.concat([Data_Frame2, Data_Frame3])

print (f'{Data_Frame_Concatenate.shape}')

print (f'{Data_Frame_Concatenate.info()}')

print (f'-' * 20)

for indice, elemento in Data_Frame_Concatenate.iterrows():
    Unidad1 = elemento['Nombre']
    Unidad2 = elemento['Edad']
    
    print (f'Mi nombre es {Unidad1} y mi edad es {Unidad2} años')
    
Grupo4 = Data_Frame_Concatenate.groupby('Nombre')['Edad'].sum()
Grupo4_Min = Grupo4.idxmin()
Grupo4_Max = Grupo4.idxmax()
Grupo4_Min_Cant = Grupo4.min()
Grupo4_Max_Cant = Grupo4.max()

print (f'El menor de los participantes es {Grupo4_Min} y su edad es {Grupo4_Min_Cant} años')
print (f'El mayor de los participantes es {Grupo4_Max} y su edad es {Grupo4_Max_Cant} años')

print (f'La cantidad de participantes es {Grupo4.count()}')

print (f'La suma de las edades es {Grupo4.sum()}')

Data_Frame_Concatenate['TOTALITO'] = Data_Frame_Concatenate['Edad'] * 100

Grupo5 = Data_Frame_Concatenate.groupby('Nombre')['TOTALITO'].sum()

Promedio4 = Grupo5.sum() / Grupo5.count()

print (f'El promedio de las edades {round(Promedio4, 2)}')
print (f'El promedio de las edades {round(Grupo5.mean(), 2)}')

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

plt.show()
'''
print (f'-' * 20)

Elemento1 = Data_Frame2.loc[0, 'Nombre']
Elemento2 = Data_Frame2.loc[1, 'Edad']
Elemento3 = Data_Frame2.loc[2, 'Votante']
Elemento4 = Data_Frame2.loc[1, :]
Elemento5 = Data_Frame2.loc[:, 'Votante']

print (f'{Elemento1}')
print (f'{Elemento2}')
print (f'{Elemento3}')
print (f'{Elemento4}')
print (f'{Elemento5}')

print (f'-' * 20)

Elemento6 = Data_Frame3.iloc[0, 0]
Elemento7 = Data_Frame3.iloc[1, 1]
Elemento8 = Data_Frame3.iloc[2, 2]
Elemento9 = Data_Frame3.iloc[1, :]
Elemento10 = Data_Frame3.iloc[:, 2]

print (f'{Elemento6}')
print (f'{Elemento7}')
print (f'{Elemento8}')
print (f'{Elemento9}')
print (f'{Elemento10}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.head(1)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.head(3)}')

print (f'-' * 20)

print (f'{Data_Frame_Concatenate.tail(1)}')

print (f'-' * 20)

Columnas, Filas = Data_Frame_Concatenate.shape

print (f'La cantidad de Columnas es {Columnas}')
print (f'La cantidad de Filas es {Filas}')

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

import pandas as pd

Ruta_Csv2 = 'C:\\Repo\\Base_Datos.csv'

Cargar_Csv2 = pd.read_csv(Ruta_Csv2)

print (f'{Cargar_Csv2.head()}')

print (f'-' * 20)

import pandas as pd
import requests
import io

Ruta_Html2 = 'https://es.wikipedia.org/wiki/Luisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html2, headers=headers)

Leer_Html2 = io.StringIO(Response.text)

Cargar_Html2 = pd.read_html(Leer_Html2)

print (f'{Cargar_Html2[2].head()}')

print (f'-' * 20)

import numpy as np

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
    for j in range(0, len(Array0[i])):
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
print (f'{Array2[1, :2]}')
print (f'{Array2[1, 2:]}')
print (f'{Array2[:, 1]}')
print (f'{Array2[1, 2:3]}')
print (f'{Array2[0, 0:None]}')
print (f'{Array2[0, :]}')
print (f'{Array2[Array2 >= 2]}')

Array2_Sorted = np.sort(Array2)
Array2_Sorted_Mean = np.mean(Array2_Sorted)
Array2_Sorted_Sum = np.sum(Array2_Sorted)

print (f'Acomodado: {Array2_Sorted}')
print (f'Media: {round(Array2_Sorted_Mean, 2)}')
print (f'Sumita: {Array2_Sorted_Sum}')

Sumita1 = np.sum(Array2_Sorted, axis=0)
Sumita2 = np.sum(Array2_Sorted, axis=1)
Sumita3 = np.sum(Array2_Sorted[0, 0:None])
Sumita4 = np.sum(Array2_Sorted[0, :])

print (f'La sumita es {Sumita1}')
print (f'La sumita es {Sumita2}')
print (f'La sumita es {Sumita3}')
print (f'La sumita es {Sumita4}')

print (f'-' * 20)

Array3 = np.array([[['a', 't', 'o'], ['d', 'b', 'c']],          [['e', 'f', 'g'], ['h', 'i', 'j']]])

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
print (f'{Array3[0, :, 0]}')
print (f'{Array3[1, 0, 2:3]}')
print (f'{Array3[0, 1, 0:None]}')
print (f'{Array3[0, 1, :]}')
print (f'{Array3[Array3 == "f"]}')

print (f'-' * 20)

Array4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 2, 1]]],         [[[5, 4, 3], [9, 8, 7]], [[4, 5, 6], [3, 8, 6]]]])

print (f'{Array4}')
print (f'{Array4.ndim}') # 4
print (f'{Array4.shape}') # 2x2x2x3
print (f'{Array4.size}') # 24
print (f'{Array4.dtype}') # int64
print (f'{Array4[1, 0, 0, 2]}')

print (f'{Array4[0, 1, 0, ::2]}')
print (f'{Array4[0, 0, 1, ::3]}')
print (f'{Array4[1, 0, 1, :2]}')
print (f'{Array4[1, 0, 1, 2:]}')
print (f'{Array4[0, 1, :, 2]}')
print (f'{Array4[1, 1, 0, 2:3]}')
print (f'{Array4[1, 0, 1, 0:None]}')
print (f'{Array4[1, 0, 1, :]}')
print (f'{Array4[Array4 >= 5]}')

Array4_Sorted = np.sort(Array4)
Array4_Sorted_Mean = np.mean(Array4_Sorted)
Array4_Sorted_Sum = np.sum(Array4_Sorted)

print (f'Acomodado: {Array4_Sorted}')
print (f'Media: {round(Array4_Sorted_Mean, 2)}')
print (f'Sumatoria: {Array4_Sorted_Sum}')

Sumita5 = np.sum(Array4_Sorted, axis=0)
Sumita6 = np.sum(Array4_Sorted, axis=1)
Sumita7 = np.sum(Array4_Sorted[1, 0, 0, 0:None])
Sumita8 = np.sum(Array4_Sorted[1, 0, 0, :])

print (f'El resultado de la sumita es {Sumita5}')
print (f'El resultado de la sumita es {Sumita6}')
print (f'El resultado de la sumita es {Sumita7}')
print (f'El resultado de la sumita es {Sumita8}')

print (f'-' * 20)

Array_Num1 = np.arange(start=1, stop=11, step=1) #type: ignore

print (f'{Array_Num1}')

Array_Num1_Min = np.min(Array_Num1)
Array_Num1_Max = np.max(Array_Num1)

print (f'El numero menor es {Array_Num1_Min}')
print (f'El numero mayor es {Array_Num1_Max}')

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
print (f'{Array_Zeros[0, 2]}')

print (f'{Array_Zeros[1, ::2]}')
print (f'{Array_Zeros[0, ::3]}')
print (f'{Array_Zeros[:, 1]}')
print (f'{Array_Zeros[1, :2]}')
print (f'{Array_Zeros[1, 2:]}')
print (f'{Array_Zeros[0, 2:3]}')
print (f'{Array_Zeros[1, 0:None]}')
print (f'{Array_Zeros[1, :]}')
print (f'{Array_Zeros[Array_Zeros >= 0]}')

print (f'-' * 20)

Array_Ones = np.ones(shape=(2, 3))

print (f'{Array_Ones}')
print (f'{Array_Ones.ndim}')
print (f'{Array_Ones.shape}')
print (f'{Array_Ones.size}')
print (f'{Array_Ones.dtype}')
print (f'{Array_Ones[0, 1]}')

print (f'{Array_Ones[1, ::2]}')
print (f'{Array_Ones[0, ::3]}')
print (f'{Array_Ones[1, :2]}')
print (f'{Array_Ones[1, 2:]}')
print (f'{Array_Ones[:, 1]}')
print (f'{Array_Ones[0, 2:3]}')
print (f'{Array_Ones[1, 0:None]}')
print (f'{Array_Ones[1, :]}')
print (f'{Array_Ones[Array_Ones >= 1]}')

print (f'-' * 20)

Array_Gen1 = np.full(shape=(2, 3), fill_value=(f'{PEPE.Diccionario_Poke1["Poke2"]}'))

print (f'{Array_Gen1}')
print (f'{Array_Gen1.ndim}')
print (f'{Array_Gen1.shape}')
print (f'{Array_Gen1.size}')
print (f'{Array_Gen1.dtype}')
print (f'{Array_Gen1[1, 2]}')

print (f'-' * 20)

Array_Gen2 = np.full(shape=(10), fill_value=(f'Fuecoco'))

print (f'{Array_Gen2}')
print (f'{Array_Gen2.ndim}')
print (f'{Array_Gen2.shape}')
print (f'{Array_Gen2.size}')
print (f'{Array_Gen2.dtype}')
print (f'{Array_Gen2[8]}')

print (f'-' * 20)

Array_Gen3 = np.full(shape=(2, 3), fill_value=(Array4[1, 0, 0, 2]))

print (f'{Array_Gen3}')
print (f'{Array_Gen3.ndim}')
print (f'{Array_Gen3.shape}')
print (f'{Array_Gen3.size}')
print (f'{Array_Gen3.dtype}')
print (f'{Array_Gen3[1, 2]}')

print (f'-' * 20)

Tupla_Array = tuple(('Uno', 'Dos', 'Tres',))
Set_Conjunto_Array = set({1, 2, 3})
Diccionario_Array = dict({'Nombre' : ["Erick", "Josue", "Karlita"]})

Array_Gen4 = np.full(shape=(2, 3), fill_value=(Tupla_Array))
Array_Gen5 = np.full(shape=(1, 2), fill_value=(Set_Conjunto_Array))
Array_Gen6 = np.full(shape=(4, 1), fill_value=(Diccionario_Array['Nombre'][1]))

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
print (f'{Array_Gen5[0, 1]}')

print (f'-' * 20)

print (f'{Array_Gen6}')
print (f'{Array_Gen6.ndim}')
print (f'{Array_Gen6.shape}')
print (f'{Array_Gen6.size}')
print (f'{Array_Gen6.dtype}')
print (f'{Array_Gen6[3, 0]}')

print (f'-' * 20)

print (f'{Array_Gen6[2]}')

print (f'-' * 20)

Array_Num3 = np.arange(start=1, stop=6, step=1) #type: ignore
Array_Num4 = np.arange(start=2, stop=11, step=2) #type: ignore
Array_Num5 = np.arange(start=10, stop=21, step=2) #type: ignore
Array_Num6 = np.arange(start=3, stop=31, step=3) #type: ignore
Array_Num7 = np.arange(10) #type: ignore

print (f'Los elementos son {Array_Num3}')
print (f'Los elementos son {Array_Num4}')
print (f'Los elementos son {Array_Num5}')
print (f'Los elementos son {Array_Num6}')
print (f'Los elementos son {Array_Num7}')

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

print (f'{Array_Random2[1, ::2]}')
print (f'{Array_Random2[0, ::3]}')
print (f'{Array_Random2[0, :2]}')
print (f'{Array_Random2[0, 2:]}')
print (f'{Array_Random2[:, 1]}')
print (f'{Array_Random2[1, 2:3]}')
print (f'{Array_Random2[0, 0:None]}')
print (f'{Array_Random2[0, :]}')
print (f'{Array_Random2[Array_Random2 >= 5]}')

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

print (f'El resultado de la sumatoria es {Sumita9}')
print (f'El resultado de la sumatoria es {Sumita10}')
print (f'El resultado de la sumatoria es {Sumita11}')
print (f'El resultado de la sumatoria es {Sumita12}')

print (f'-' * 20)

Array_Matriz1 = np.array([8, 9, 14])
Array_Matriz2 = np.array([2, 3, 7])

Suma = Array_Matriz1 + Array_Matriz2
Resta = Array_Matriz1 - Array_Matriz2
Multiplicacion = Array_Matriz1 * Array_Matriz2
Division_Flotante = Array_Matriz1 / Array_Matriz2
Division_Baja = Array_Matriz1 // Array_Matriz2
Exponente = Array_Matriz1 ** Array_Matriz2
Modulo = Array_Matriz1 % Array_Matriz2

Array_Random1_Cien = Array_Random1 + 100

print (f'El resultado de la operacion es {Suma}')
print (f'El resultado de la operacion es {Resta}')
print (f'El resultado de la operacion es {Multiplicacion}')
print (f'El resultado de la operacion es {Division_Flotante}')
print (f'El resultado de la operacion es {Division_Baja}')
print (f'El resultado de la operacion es {Exponente}')
print (f'El resultado de la operacion es {Modulo}')
print (f'El resultado de la operacion es {Array_Random1_Cien}')

print (f'-' * 20)

Array_Num8 = np.arange(start=1, stop=21, step=1) #type: ignore

print (f'{Array_Num8}')

Array_Num8_Reshape = np.reshape(Array_Num8, shape=(4, 5))

print (f'{Array_Num8_Reshape}')

Array_Num8_Reshape_Column_Min = np.min(Array_Num8_Reshape, axis=0)
Array_Num8_Reshape_Column_Max = np.max(Array_Num8_Reshape, axis=0)
Array_Num8_Reshape_Row_Min = np.min(Array_Num8_Reshape, axis=1)
Array_Num8_Reshape_Row_Max = np.max(Array_Num8_Reshape, axis=1)

print (f'De la columna los menores son {Array_Num8_Reshape_Column_Min}')
print (f'De la columna los mayores son {Array_Num8_Reshape_Column_Max}')
print (f'De la fila los menores son {Array_Num8_Reshape_Row_Min}')
print (f'De la fila los mayores son {Array_Num8_Reshape_Row_Max}')

print (f'-' * 20)

Array_Num8_Reshape_Ravel = np.ravel(Array_Num8_Reshape)

print (f'{Array_Num8_Reshape_Ravel}')

print (f'-' * 20)

Lista_Array1 = list([])

Array5 = np.array(['Erick', 'Josue', 'Karlita'])

for elemento in Array5:
    Lista_Array1.append(str(elemento))
    
print (f'{Lista_Array1}')
print (f'{type(Lista_Array1)}')
print (f'{Array5}')
print (f'{type(Array5)}')

print (f'-' * 20)

Lista_Array2 = ['Erick', 'Josue', 'Karlita']

Array6 = np.array(Lista_Array2)

print (f'-' * 20)

Array7 = np.array([1, 2, 3])
Array8 = np.array([4, 5, 6])

Array_Concatenate = np.concatenate([Array7, Array8])

print (f'{Array_Concatenate}')

print (f'-' * 20)

Array_Concatenate_Split1 = np.split(Array_Concatenate, 1)
Array_Concatenate_Split2 = np.split(Array_Concatenate, 2)
Array_Concatenate_Split3 = np.split(Array_Concatenate, 3)
Array_Concatenate_Split4 = np.split(Array_Concatenate, 6)

print (f'-' * 20)

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

Array_Random3 = np.random.randint(low=1, high=10, size=(2, 2, 3))

print (f'{Array_Random3}')

Array_Random3_Column_Min = np.min(Array_Random3, axis=0)
Array_Random3_Column_Max = np.max(Array_Random3, axis=0)
Array_Random3_Row_Min = np.min(Array_Random3, axis=1)
Array_Random3_Row_Max = np.max(Array_Random3, axis=1)

print (f'Los menores de las columnas son {Array_Random3_Column_Min}')
print (f'Los mayores de las columnas son {Array_Random3_Column_Max}')
print (f'Los menores de las filas son {Array_Random3_Row_Min}')
print (f'Los mayores de las filas son {Array_Random3_Row_Max}')

print (f'-' * 20)

Lista_Ganadores1 = ['Erick', 'Josue', 'Karlita']
Lista_Ganadores2 = ['Carmelo', 'Susanita', 'Roxana']

Lista_Ganadores3 = Lista_Ganadores1 + Lista_Ganadores2

Ganador1 = np.random.choice(Lista_Ganadores3, size=(1), replace=False)
Ganador2 = np.random.choice(Lista_Ganadores3, size=(2), replace=False)
Ganador3 = np.random.choice(Lista_Ganadores3, size=(2, 3), replace=False)

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
    print (f'Error, el experimento termina aqui')
    
print (f'-' * 20)

def Generadora2():
    for elemento in range(5):
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
    print (f'Error, el experimento termina aqui')
    
print (f'-' * 20)

def Generadora3(Lista):
    for elemento in Lista[0:None]:
        if (elemento == 1):
            yield f'El numero es uno'
        elif (elemento == 2):
            yield f'El numero es dos'
        elif (elemento == 3):
            yield f'El numero es tres'
        elif (elemento == 4):
            yield f'El numero es cuatro'
        elif (elemento == 5):
            yield f'El numero es cinco'
        else:
            yield f'Error de codigo'
        

Gen3 = Generadora3([1, 2, 3, 4, 5])

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

PEPE.Saludar1()

from Module_Own import Saludar2 as Saludar_Dos

print (f'Hola {Saludar_Dos()}')

print (f'Hola nuevamente {PEPE.Saludar3(Saludar_Dos())}')

print (f'{help(PEPE.Saludar3)}')

print (f'El resultado de la sumatoria es {PEPE.Sumatoria1(12, 4)}')

def Sumatoria_Externa(Num1):
    def Sumatoria_Interna(Num2:int) -> int:
        return Num1 + Num2
    
    return Sumatoria_Interna(4)

Variable_Sumatoria = Sumatoria_Externa(3)

print (f'El resultado de la suma es {Variable_Sumatoria}')

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
    
with open ('C:\\Repo\\HolaMundo.txt', 'a', encoding='UTF-8') as Docu:
    Documento_Agregar = Docu.write(f'\nSu contrasena temporal es {PEPE.Contrasena(44)}')
    Docu.close()
    
try:
    with open ('C:\\Repo\\HolaMundo.txt', 'r', encoding='UTF-8') as Docu:
        Documento_Lineas = Docu.readlines()
        print (f'{Documento_Lineas}')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo seleccionado es incorrecto')
    
def Funcion_Tupla(*args):
    return args
        
Variable_Funcion_Tupla = Funcion_Tupla(36, 3.5, True, 'Koala')

print (f'{Funcion_Tupla(36, 3.5, True, 'Koala')}')
print (f'{Funcion_Tupla(36, 3.5, True, 'Koala')[2]}')
print (f'{Variable_Funcion_Tupla[3]}')
print (f'{type(Funcion_Tupla(36, 3.5, True, 'Koala'))}')

def Funcion_Diccionario(**kwargs):
    for elemento in kwargs:
        print (f'{kwargs[elemento]}')
        
    print (f'-' * 20)
    
    for indice, elemento in kwargs.items():
        print (f'{indice} : {elemento}')
        
    print (f'-' * 20)
        
    for elemento in kwargs.keys():
        print (f'{elemento}')
        
    print (f'-' * 20)
    
    for elemento in kwargs.values():
        print (f'{elemento}')
        
    print (f'-' * 20)
    
Variable_Funcion_Diccionario = Funcion_Diccionario(
    Nombre = "Erick",
    Edad = 37,
    Votante = True
)

def Sumatoria2(*args):
    return sum(args)

Sum3 = Sumatoria2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print (f'El resultado de la sumatoria es {Sum3}')

print (f'-' * 20)

def Sumatoria3(Nombre = Saludar_Dos(), *args):
    return f'{Nombre}, tu numero favorito es {sum(args)}'

print (f'{Sumatoria3("Susanita", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print (f'-' * 20)

from Module_Own import Variable_Funcion_Anonima1 as Anonima1, Variable_Funcion_Anonima2 as Anonima2, Variable_Funcion_Anonima3 as Anonima3

print (f'El resultado de la multiplicacion es {Anonima1(150, 3)}')

print (f'El doble del numero {Variable_Sumatoria} es {Anonima2(Variable_Sumatoria)}')

print (f'Los numeros pares de la lista son {list(Anonima3)}')

print (f'{PEPE.Any_Par}')

print (f'{PEPE.Lista_Par}')

Diccionario_Numeral2 = {
    'Num1' : 7,
    'Num2' : 1,
    'Num3' : 4,
    'Num4' : 2,
    'Num5' : 5
}

Diccionario_Numeral2_Sorted = dict(sorted(Diccionario_Numeral2.items(), key= lambda item : item[1]))

print (f'{Diccionario_Numeral2}')
print (f'{Diccionario_Numeral2_Sorted}')

Diccionario_Numeral2_Sorted_Min = min(Diccionario_Numeral2_Sorted.items(), key=lambda item : item[1])
Diccionario_Numeral2_Sorted_Max = max(Diccionario_Numeral2_Sorted.items(), key=lambda item : item[1])

print (f'{Diccionario_Numeral2_Sorted_Min}')
print (f'{Diccionario_Numeral2_Sorted_Max}')

'''Lista_Alumnos = list([])

Contador = int(input(f'Ingrese la cantidad de estudiantes: '))

def Colegio(Lista):
    for elemento in range(0, Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.append(Estudiante)
        
    Lista.sort(key = lambda item : item[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes es {Menore} y su edad es {Lista[0][1]} años')
    print (f'El mayor de los estudiantes es {Mayore} y su edad es {Lista[-1][1]} años')

Sample57 = Colegio(Lista_Alumnos)'''

def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda(*args) - 42
        
    return Tercera

@Primera
def Operacion(Num:int) -> int:
    '''Esto es un docstring, el argumento Num se suma y luego se devuelve el resultado'''
    Local = PEPE.GLOBAL + Num
    return Local

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
print (f'{Variable_Closure(35)}')
print (f'{Variable_Closure(78)}')

def Closure_Crear_Multiplicador(x):
    def Closure_Multiplicador(y):
        return x * y
    
    return Closure_Multiplicador

Mult1 = Closure_Crear_Multiplicador(2)
Mult2 = Closure_Crear_Multiplicador(3)

print (f'El multiplicador es {Mult1(10)}')
print (f'El multiplicador es {Mult2(10)}')

def Filtrador(Lista):
    Any_Iterable = any(num % 2 != 0 for num in Lista)
    if (Any_Iterable == True):
        Anonima4 = filter(lambda Num : Num % 2 != 0, Lista)
        Lista_Iterable = [num for num in Lista if num % 2 != 0]
        print (f'Los numeros impares de la lista son {list(Anonima4)}')
        print (f'Los numeros impares de la lista son {Lista_Iterable}')
    else:
        print (f'Error, no hay numero impares en la lista')

Filtrador(PEPE.Lista_Numeros)

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
        return Segunda(*args, **kwargs) - 19
        
    return Tercera

@Primera
def Sumatoria4(Num1, Num2):
    return Num1 + Num2

print (f'El resultado de la sumatoria es {Sumatoria4(12, 7)}')

print (f'-' * 20)

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Jonathan'
        Apellido = 'Smith'
        return Segunda(Nombre, Apellido)
        
    return Tercera

@Primera
def Usuario4(Nombre, Apellido):
    return f'Mi nombre es {Nombre} {Apellido}'

print (f'{Usuario4("Erick", "Perez")}')

print (f'-' * 20)

from Module_Own import Pokemon2 as Poke2

Objeto33 = Poke2(PEPE.Diccionario_Poke1['Poke1'], 'Electrico', 'Impact Trueno')

Objeto33.Mostrar()
print (f'{Objeto33.Mostrar2}')
print (f'{Objeto33}')

print (f'-' * 20)

Objeto34 = Poke2(PEPE.Diccionario_Poke1['Poke2'], 'Roca', 'Mega Sismo')

Objeto34.Mostrar()
print (f'{Objeto34.Mostrar2}')
print (f'{Objeto34}')

print (f'-' * 20)

class Poke_Kid2(Poke2):
    def __init__(self, Nombre, Tipo, Ataque, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Sub_Tipo = Sub_Tipo
        
    def Mostrar(self):
        print (f'Sub_Tipo: {self.Sub_Tipo}')
        
Objeto35 = Poke_Kid2(PEPE.Diccionario_Poke1['Poke3'], 'Agua', 'Hidro-Chorro', 'Acero')

Poke2.Mostrar(Objeto35)
Objeto35.Mostrar()

print (f'{Objeto35.Mostrar2}')
print (f'{Objeto35}')

print (f'-' * 20)

class Camara2():
    def Tomar_Fotografia(self):
        print (f'La fotografia fue tomada')
        
class Reproductor_Musica2():
    def Reproducir_Musica(self):
        print (f'La musica fue reproducida')
        
class Smartphone2(Camara2, Reproductor_Musica2):
    def Encender_Smartphone(self):
        print (f'El smartphone fue encendido')
        
Objeto36 = Smartphone2()

Objeto36.Tomar_Fotografia()
Objeto36.Reproducir_Musica()
Objeto36.Encender_Smartphone()

print (f'-' * 20)

class Veterinaria2():
    def __init__(self, Nombre, Edad, Peso):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Peso = Peso

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Edad: {self.Edad} años')
        print (f'Peso: {self.Peso}kgs')
        
class Perro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Raza, Padecimiento):
        super().__init__(Nombre, Edad, Peso)
        self.Raza = Raza
        self.Padecimiento = Padecimiento
        
    def Mostrar(self):
        print (f'Raza: {self.Raza}')
        print (f'Padecimiento: {self.Padecimiento}')
        
Objeto37 = Perro2('Terry', 3, 5.1, 'Dobberman', 'Obesidad')

Veterinaria2.Mostrar(Objeto37)
Objeto37.Mostrar()

print (f'-' * 20)

class Gato2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Color, Paciente):
        super().__init__(Nombre, Edad, Peso)
        self.Color = Color
        self.Paciente = Paciente
        
    def Mostrar(self):
        print (f'Color: {self.Color}')
        print (f'Paciente: {self.Paciente}')
        
Objeto38 = Gato2('Messi', 1.5, 2, 'Gris', 'No')

Veterinaria2.Mostrar(Objeto38)
Objeto38.Mostrar()

print (f'-' * 20)

class Pajaro2(Veterinaria2):
    def __init__(self, Nombre, Edad, Peso, Especie, Habla):
        super().__init__(Nombre, Edad, Peso)
        self.Especie = Especie
        self.Habla = Habla
        
    def Mostrar(self):
        print (f'Especie: {self.Especie}')
        print (f'Habla: {self.Habla}')
        
Objeto39 = Pajaro2('Polly', 31, 0.4, 'Papagayo', 'Si')

Veterinaria2.Mostrar(Objeto39)
Objeto39.Mostrar()

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
        
Objeto40 = Paladin2(25, 'Battle Axe', 75, 'Dark Crystal', 200, 'Ghost Knight')

Objeto40.Mostrar()
Atacante2.Mostrar(Objeto40)
Defensor2.Mostrar(Objeto40)

print (f'-' * 20)

Hija_Padre2 = issubclass(Poke_Kid2, Poke2)
Hija_Padre3 = issubclass(Poke_Kid2, Poke1)

print (f'{Hija_Padre2}')
print (f'{Hija_Padre3}')

Instancia4 = isinstance(Objeto40, Paladin2)
Instancia5 = isinstance(Objeto40, Atacante2)
Instancia6 = isinstance(Objeto40, Defensor2)
Instancia7 = isinstance(Objeto40, Paladin)

print (f'{Instancia4}')
print (f'{Instancia5}')
print (f'{Instancia6}')
print (f'{Instancia7}')

print (f'-' * 20)

class A2():
    def Mostrar(self):
        print (f'Muy buenas tardes A2')
        
class E2():
    def Mostrar(self):
        print (f'Muy buenas tardes E2')
        
class B2(E2):
    def Mostrar(self):
        print (f'Muy buenas tardes B2')
        
class C2(A2):
    def Mostrar(self):
        print (f'Muy buenas tardes C2')
        
class D2(B2, C2):
    def Mostrar(self):
        print (f'Muy buenas tardes D2')
        
Objeto41 = D2()

A2.Mostrar(Objeto41)
B2.Mostrar(Objeto41)
C2.Mostrar(Objeto41)
Objeto41.Mostrar()
E2.Mostrar(Objeto41)

print (f'-' * 20)

class Efectivo2():
    def Pagar(self):
        print (f'El pago se realizo en Efectivo')
        
class Tarjeta2():
    def Pagar(self):
        print (f'El pago se realizo en Tarjeta')
        
class CriptoMoneda2():
    def Pagar(self):
        print (f'El pago se realizo en CriptoMoneda')
        
Objeto42 = Efectivo2()
Objeto42.Pagar()

Objeto43 = Tarjeta2()
Objeto43.Pagar()

Objeto44 = CriptoMoneda2()
Objeto44.Pagar()

print (f'-' * 20)

class Cuenta_Bancaria2():
    def __init__(self, Dinero):
        self._Dinero = Dinero

    def Depositar(self, Deposito):
        self._Dinero += Deposito
    
    @property    
    def Dinero(self):
        self._Dinero
    
    @Dinero.setter
    def Dinero(self, Nuevo_Dinero):
        self._Dinero = Nuevo_Dinero
        
    def Mostrar(self):
        print (f'Tu saldo a la fecha es de ${self._Dinero}')
        
Objeto45 = Cuenta_Bancaria2(25)
Objeto45.Depositar(100)

Objeto45.Mostrar()

print (f'Tu dinero privado es {Objeto45._Dinero}')

Objeto45._Dinero = '50,000,000'

Objeto45.Mostrar()

print (f'Tu dinero privado es {Objeto45._Dinero}')

print (f'-' * 20)

from abc import ABC, abstractmethod

class Plantilla3(ABC):
    @abstractmethod
    def General(self):
        pass

class Sub_Plantilla3(Plantilla3):
    def Mostrar(self):
        print (f'Esto es un metodo de la sub plantilla')
        
    def General(self):
        print (f'Esto es un metodo de la abstraccion')
        
Objeto46 = Sub_Plantilla3()

Objeto46.Mostrar()
Objeto46.General()

print (f'-' * 20)

from abc import ABC

class Comida(ABC):
    @abstractmethod
    def Cocinar(self):
        pass

class Pizza(Comida):
    def Amasar(self):
        print (f'En este paso vamos a amasar la masa de la pizza')
        
    def Cocinar(self):
        print (f'En este paso vamos a hornear la pizza')
        
Objeto47 = Pizza()

Objeto47.Amasar()
Objeto47.Cocinar()

print (f'-' * 20)

class Chocolate2():
    def Elegir(self):
        return f'Chocolate'
    
class Fresa2():
    def Elegir(self):
        return f'Fresa'
    
class Vainilla2():
    def Elegir(self):
        return f'Vainilla'
    
class Pastel3():
    def __init__(self):
        self.Favorito = Chocolate2()
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Objeto48 = Pastel3()

Objeto48.Hornear()

print (f'-' * 20)

class Pastel4():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Hornear(self):
        print (f'Hoy vamos a hornear un pastel de {self.Favorito.Elegir()}')
        
Ingrediente4 = Chocolate2()
Objeto49 = Pastel4(Ingrediente4)
Objeto49.Hornear()

Ingrediente5 = Fresa2()
Objeto50 = Pastel4(Ingrediente5)
Objeto50.Hornear()

Ingrediente6 = Vainilla2()
Objeto51 = Pastel4(Ingrediente6)
Objeto51.Hornear()

print (f'-' * 20)

class Bulbasaur2():
    def Elegir(self):
        return f'Bulbasaur'
    
class Chikorita2():
    def Elegir(self):
        return f'Chikorita'
    
class Treekoo2():
    def Elegir(self):
        return f'Treekoo'
    
class Batalla1():
    def __init__(self):
        self.Favorito = Bulbasaur2()
        
    def Batallar(self):
        print (f'El entrenador {PEPE.Tupla_Pokemon[PEPE.Tupla_Pokemon.index("Ash")]} ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Objeto52 = Batalla1()
Objeto52.Batallar()

print (f'-' * 20)

class Batalla2():
    def __init__(self, Favorito):
        self.Favorito = Favorito
        
    def Batallar(self):
        print (f'El entrenador {PEPE.Tupla_Pokemon[PEPE.Tupla_Pokemon.index("Misty")]} ha elegido un {self.Favorito.Elegir()} para la batalla')
        
Criatura1 = Bulbasaur2()
Objeto53 = Batalla2(Criatura1)
Objeto53.Batallar()

Criatura2 = Chikorita2()
Objeto54 = Batalla2(Criatura2)
Objeto54.Batallar()

Criatura3 = Treekoo2()
Objeto55 = Batalla2(Criatura3)
Objeto55.Batallar()

print (f'-' * 20)

class Persona3():
    def __init__(self, Nombre):
        self._Nombre = Nombre
        
    def Mostrar(self):
        return self._Nombre
    
    @property
    def Mostrar2(self):
        return self._Nombre
    
    def __str__(self):
        return self._Nombre
    
Objeto56 = Persona3('Erick Josue Perez Gutierrez')

print (f'{Objeto56.Mostrar()}')
print (f'{Objeto56.Mostrar2}')
print (f'{Objeto56}')

print (f'-' * 20)

var19 = 2

var19 += 8

print (f'El resultado de la operacion es {var19}')

var19 -= 1

print (f'El resultado de la operacion es {var19}')

var19 *= 2

print (f'El resultado de la operacion es {var19}')

var19 //= 2

print (f'El resultado de la operacion es {var19}')

var19 /= 2

print (f'El resultado de la operacion es {var19}')

var19 **= 2

print (f'El resultado de la operacion es {var19}')

var19 %= 2

print (f'El resultado de la operacion es {var19}')

print (f'-' * 20)

print (f'Hola mi nombre es {(var20 := "Erick Josue Perez Gutierrez")}')

print (f'-' * 20)

for indice, elemento in enumerate((Lista_Walrus1 := ["Erick", "Josue", "karlita"]), start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)
    
for indice, elemento in ((Diccionario_Walrus := {'Nombre' : "Erick", 'Edad' : 37, 'Votante' : True}).items()):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

for elemento in range(0, len((Lista_Walrus2 := [1, 2, 3, 4, 5]))):
    print (f'{elemento}')
    
print (f'-' * 20)

Contador = 0

while (Contador < (Numero_Walrus := 5)):
    print (f'El contador es {Contador + 1}')
    Contador += 1
    
print (f'-' * 20)

from Module_Own import Lista1 as Lista_Uno, Lista4 as Lista_Cuatro

variable1 = Lista_Uno[0]
variable2 = 'Perez'
variable3 = '''Esta
Es
Una
Variable
Long
String o Docstring'''

variable4 = Objeto34.Cantidad
variable5 = PEPE.Division_Flotante

try:
    variable6, variable7 = True, Objeto35.Catched  # Esta vara se llama desempaquetado de variables
except ValueError as Errore4:
    print (f'Error, este desempaquetado de variable es incorrecto -> {str(Errore4)}')
    
# Esto es un comentario simple

'''Esto
Es
Un
Comentario
Compuesto'''

print (f'Esto es una concatenacion simple {PEPE.Diccionario_Poke1["Poke2"]}')

class Nombrecito():
    def Elegir(self):
        return f'{PEPE.Lista1[1]}'

class Persona4():
    def __init__(self):
        self.Nombrecito = Nombrecito()
        
    def Mostrar(self):
        return self.Nombrecito.Elegir()
    
Objeto57 = Persona4()

print (f'Hola, mi nombre es {Lista_Uno[0]} {Objeto57.Mostrar()}')

print (f'{PEPE.Tupla_Pokemon[2]} tiene {Variable_Sumatoria} o {Sumatoria2(1, 2, 3, 4, 5)} o incluso {Objeto34.Cantidad} pokemones')

del variable5

print (f'melo' in Saludar_Dos())
print (f'Long' not in variable3)

print (f'Perez' in Lista_Uno)
print (f'Gary' not in PEPE.Tupla_Pokemon)
print (f'{PEPE.Diccionario_Poke1["Poke3"] in PEPE.Set_Conjunto_Poke1}')

snake_case4, snake_case5, snake_case6 = PEPE.Tupla_Pokemon

print (f'Esto es un desempaquetado de variables declarado como snake case {snake_case5}')

print (f'La lista {Lista_Uno} tiene actualmente {Lista_Uno.__len__()} elementos')

Lista_Uno.append('Coco Rayado')
Lista_Uno.insert(1, 'Juana La Cubana')
Lista_Uno.extend(['Finale1', 'Finale2', 'Finale3'])

print (f'{Lista_Uno}')
print (f'La lista {Lista_Uno} tiene actualmente {len(Lista_Uno)} elementos')

def Ejercicio57(Lista):
    Anonima4 = filter(lambda num : num % 2 == 0, Lista)
    return Anonima4

Sample57 = Ejercicio57(PEPE.Lista3)

if (len(PEPE.Lista3) == 0):
    print (f'Error, la lista esta vacia')
else:
    if (Sample57):
        print (f'La lista de solo numeros pares es {list(Sample57)}')
    else:
        print (f'Error, no hay numero pares en la lista')
        
print (f'-' * 20)

print (f'{PEPE.Lista3}')
print (f'{PEPE.Lista3[::2]}')
print (f'{PEPE.Lista3[::3]}')
print (f'{PEPE.Lista3[:2]}')
print (f'{PEPE.Lista3[2:]}')
print (f'{PEPE.Lista3[2:3]}')
print (f'{PEPE.Lista3[0:None]}')
print (f'{PEPE.Lista3[:]}')

print (f'-' * 20)

print (f'Oiga mae {Lista_Uno[0]} eso que esta ahi es un {PEPE.Lista2[2]}?')

print (f'{Lista_Cuatro}')

Lista_Cuatro[0] = Sumatoria2(Anonima2(250), Anonima1(50, 3), 50, 150 * 2)

print (f'{Lista_Cuatro}')

del Lista_Uno[1]
Lista_Uno.remove('Coco Rayado')
Lista_Uno.pop(-2)
Lista_Uno.pop(-1)
Lista_Uno.pop(-1)

print (f'{Lista_Uno}')
print (f'La lista {Lista_Uno} tiene actualmente {len(Lista_Uno)} elementos')

Lista_Uno_Copia = Lista_Uno.copy()

Lista_Uno.clear()

print (f'{Lista_Uno}')
print (f'La lista {Lista_Uno} tiene actualmente {len(Lista_Uno)} elementos')

print (f'{Lista_Uno_Copia}')
print (f'La lista {Lista_Uno_Copia} tiene actualmente {len(Lista_Uno_Copia)} elementos')

print (f'{Lista_Cuatro}')

Lista_Cuatro.sort()

print (f'{Lista_Cuatro}')

Lista_Cuatro.sort(reverse = True)

print (f'{Lista_Cuatro}')

Lista_Cuatro.reverse()

print (f'{Lista_Cuatro}')

Diccionario_Numeral3 = {
    'Num1' : 7,
    'Num2' : 1,
    'Num3' : 4,
    'Num4' : 2,
    'Num5' : 5
}

Diccionario_Numeral3_Sorted = dict(sorted(Diccionario_Numeral3.items(), key=lambda num : num[1]))

Diccionario_Numeral3_Sorted_Min = min(Diccionario_Numeral3_Sorted.items(), key=lambda num : num[1])
Diccionario_Numeral3_Sorted_Max = max(Diccionario_Numeral3_Sorted.items(), key=lambda num : num[1])

print (f'{Diccionario_Numeral3}')
print (f'{Diccionario_Numeral3_Sorted}')
print (f'{Diccionario_Numeral3_Sorted_Min}')
print (f'{Diccionario_Numeral3_Sorted_Max}')

print (f'-' * 20)

import pandas as pd
from datetime import datetime

Ruta_Csv3 = 'C:\\Repo\\Store.csv'

Cargar_Csv3 = pd.read_csv(Ruta_Csv3)

print (f'{Cargar_Csv3.head()}')

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
    print (f'No se registraron ventas en esta fecha')
else:
    print (f'GENIAL! Encontramos ventas en esta fecha')
    
    Grupo6 = Encontrado3.groupby('product')['quantity'].sum()
    Grupo6_Min = Grupo6.idxmin()
    Grupo6_Max = Grupo6.idxmax()
    Grupo6_Min_Cant = Grupo6.min()
    Grupo6_Max_Cant = Grupo6.max()
    
    print (f'En la fecha {Fech3_Formateada}, el producto {Grupo6_Min} vendio {Grupo6_Min_Cant} unidades')
    print (f'En la fecha {Fech3_Formateada}, el producto {Grupo6_Max} vendio {Grupo6_Max_Cant} unidades')
    
    print (f'La cantidad de clientes que compraron en esta fecha fue {Grupo6.count()}')
    
    print (f'La suma de las ventas realizadas en esta fecha fue de {Grupo6.sum()}')
    
    Promedio5 = Grupo6.sum() / Grupo6.count()
    
    print (f'El promedio de ventas es {round(Promedio5, 2)}')
    print (f'El promedio de ventas es {round(Grupo6.mean(), 2)}')
    
    Grupo7 = Encontrado3.groupby('product')['TOTALITO'].sum()
    
    print (f'La suma de dinero vendido en esta fecha fue de ${Grupo7.sum()}')
    
    Promedio6 = Grupo7.sum() / Grupo7.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio6, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Grupo7.mean(), 2)}')
    
print (f'-' * 20)

print (f'{dir(PEPE)}')

Tupla1 = ('Uno', 'Dos', 'Dos', 'Dos', 'Dos', 'Dos',)

print (f'{Tupla1}')

# del Tupla1[0]

# Tupla1[1] = Objeto34.Nombre

Tupla1 = tuple(('One', 'Two', 'Three',))

print (f'{Tupla1}')

# Esto es una tupla, las tuplas muestran elementos repetidos, pero son inmutables, no se les puede eliminar elementos o cambiar el valor de un elemento, solo se permite reconstruirlas

Tupla2 = 'Uno', 'Dos', 'Tres'

Tupla3 = 'Uno',

print (f'{type(Tupla1)}')
print (f'{type(Tupla2)}')
print (f'{type(Tupla3)}')
print (f'{type(PEPE.Tupla_Pokemon)}')
print (f'{type(Variable_Funcion_Tupla)}')

print (f'-' * 20)

Set_Conjunto1 = {'Electrico', Objeto33.Tipo}
Set_Conjunto2 = set({PEPE.Diccionario_Poke1['Poke1']})
Set_Conjunto1.add('Globito')
Set_Conjunto1.update(Set_Conjunto2) #type: ignore

print (f'{Set_Conjunto1}')

Set_Conjunto1 = set({'Rojo', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde'})

print (f'{Set_Conjunto1}')

# Un set o conjunto es una lista que no puede inmutarse, pero los elementos repetidos no los muestra, lo unico que permite es reconstruccion

Set_Conjunto3 = {1, 2, 3, 4, 5}
Set_Conjunto4 = {4, 5}
Set_Conjunto5 = set({8})

print (f'{Set_Conjunto3.issuperset(Set_Conjunto4)}')
print (f'{Set_Conjunto3 >= Set_Conjunto4}')

print (f'-' * 20)

print (f'{Set_Conjunto4.issubset(Set_Conjunto3)}')
print (f'{Set_Conjunto4 <= Set_Conjunto3}')

print (f'-' * 20)

print (f'{Set_Conjunto3.isdisjoint(Set_Conjunto5)}')

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

# SetA1.update(SetB1)
# SetA1.intersection_update(SetB1)
# SetA1.difference_update(SetB1)
# SetB1.difference_update(SetA1)
SetA1.symmetric_difference_update(SetB1)

print (f'{SetA1}')

print (f'-' * 20)

Set_Conjunto_Menu1 = {'Chocolate', 'Vainilla'}
Set_Conjunto_Menu1.add('Fresa')

Set_Conjunto_Menu2 = frozenset({'Caramelo'})
Set_Conjunto_Menu3 = set({Set_Conjunto_Menu2, 'Pistacho'})

print (f'{Set_Conjunto_Menu1}')
print (f'{Set_Conjunto_Menu2}')
print (f'{Set_Conjunto_Menu3}')

Set_Conjunto_Menu1.update(Set_Conjunto_Menu2)

print (f'{Set_Conjunto_Menu1}')

print (f'-' * 20)

Diccionario1 = {
    'Nombre' : "Erick",
    'Edad' : 37,
    'Votante' : True
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

Diccionario2 = {
    'Nombre' : ['Erick', 'Josue', 'Karlita'],
    'Edad' : [37, 20, 6],
    'Votante' : [True, not False, False]
}

print (f'{Diccionario2}')
print (f'{Diccionario2.keys()}')
print (f'{Diccionario2.values()}')
print (f'{Diccionario2.items()}')
print (f'{Diccionario2["Nombre"][0]}')
print (f'{Diccionario2.get("Edad")[0]}') #type: ignore

for indice, elemento in Diccionario2.items():
    for finale in elemento[0:None]:
        print (f'{finale}')
    
print (f'-' * 20)

Diccionario3 = dict({'Ingresos' : 501, 'Gastos' : 199, 'Vacio' : "q"})

print (f'{Diccionario3}')
print (f'{Diccionario3.keys()}')
print (f'{Diccionario3.values()}')
print (f'{Diccionario3.items()}')
print (f'{Diccionario3["Ingresos"]}')
print (f'{Diccionario3.get("Gastos")}')

for elemento in Diccionario3:
    print (f'{Diccionario3[elemento]}')
    
print (f'-' * 20)

Diccionario4 = {
    'Usuario1' : {
        'Nombre' : "Erick",
        'Edad' : 37,
        'Votante' : True
    },
    
    'Usuario2' : {
        'Nombre' : "Karlita",
        'Edad' : 6,
        'Votante' : False
    }
}

print (f'{Diccionario4}')
print (f'{Diccionario4.keys()}')
print (f'{Diccionario4.values()}')
print (f'{Diccionario4.items()}')
print (f'{Diccionario4["Usuario1"]["Nombre"]}')
print (f'{Diccionario4.get("Usuario2")["Nombre"]}') #type: ignore

for nivel1_indice, nivel1_elemento in Diccionario4.items():
    for nivel2_indice, nivel2_elemento in nivel1_elemento.items():
        print (f'{nivel2_indice} : {nivel2_elemento}')
        
print (f'-' * 20)

Diccionario5 = {
    'Usuario1' : {
        'Nombre' : ["Erick", "Josue", "Karlita"],
        'Edad' : [37, 20, 6],
        'Votante' : [True, True, False]
    },
    
    'Usuario2' : {
        'Nombre' : ["Carmelo", "Susanita", "Roxana"],
        'Edad' : [55, 14, 26],
        'Votante' : [True, False, not False]
    }
}

print (f'{Diccionario5}')
print (f'{Diccionario5.keys()}')
print (f'{Diccionario5.values()}')
print (f'{Diccionario5.items()}')
print (f'{Diccionario5["Usuario1"]["Nombre"][1]}')
print (f'{Diccionario5.get("Usuario2")["Nombre"][1]}') #type: ignore

for nivel1_indice, nivel1_elemento in Diccionario5.items():
    for nivel2_indice, nivel2_elemento in nivel1_elemento.items():
        for finale in nivel2_elemento[:]:
            print (f'{finale}')
            
print (f'-' * 20)

Diccionario1['Nombre'] = Saludar_Dos()

print (f'{Diccionario1}')

Diccionario1_Copia = Diccionario1.copy()

del Diccionario1['Nombre']
Diccionario1.pop('Edad')

print (f'{Diccionario1}')

Diccionario1.clear()

print (f'{Diccionario1}')

Diccionario1 = dict({1 : "Karlita", 2 : Sumatoria2(1, 2, 3), 3 : False})

print (f'{Diccionario1}')
print (f'{Diccionario1.keys()}')
print (f'{Diccionario1.values()}')
print (f'{Diccionario1.items()}')
print (f'{Diccionario1[1]}')
print (f'{Diccionario1.get(2)}')

print (f'-' * 20)

print (f'{Diccionario2["Nombre"][2]} no puede votar todavia ya que solo tiene {Diccionario1.get(2)} añitos')

Diccionario_Vacio1 = dict.fromkeys('ABC', 'Hola')
Diccionario_Vacio2 = dict.fromkeys(['Uno', 'Dos', 'Tres'])
Diccionario_Vacio2['Dos'] = PEPE.Diccionario_Poke1['Poke3']

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

Lista_Csv1 = list(Cargar_Csv3['product'])

print (f'{Lista_Csv1}')

Key1 = [f'Key{i}' for i in range(0, len(Lista_Csv1))]

print (f'{Key1}')

Diccionario6 = dict(zip(Key1, Lista_Csv1))

print (f'{Diccionario6}')
print (f'{Diccionario6.keys()}')
print (f'{Diccionario6.values()}')
print (f'{Diccionario6.items()}')
print (f'{Diccionario6["Key0"]}')
print (f'{Diccionario6.get("Key2")}')

print (f'-' * 20)

Lista_Ejemplo14 = list(['Manzana', 'Rabano', 'Pepino', 'Tomate'])

def Ejercicio58(Lista): #type: ignore
    Diccionario_Vacio = dict({})
    
    Frutas = ['Manzana', 'Pera', 'Uvas']
    Vegetales = list(['Rabano', 'Pepino', 'Tomate'])
    
    for elemento in Lista:
        if (elemento in Frutas):
            Diccionario_Vacio['Frutas'] = []
            Diccionario_Vacio['Frutas'].append(elemento)
        elif (elemento in Vegetales):
            Diccionario_Vacio['Vegetales'] = []
            Diccionario_Vacio['Vegetales'].append(elemento)
        else:
            continue
            
    return Diccionario_Vacio

if (Lista_Ejemplo14):
    Sample58 = Ejercicio58(Lista_Ejemplo14)
    for indice, elemento in Sample58.items():
        print (f'{indice} : {elemento}')
else:
    print (f'Error, la lista esta vacia')
    
print (f'-' * 20)

Key2 = [f'Key{i}' for i in range(len(Lista_Uno_Copia))]

Diccionario7 = dict(zip(Key2, Lista_Uno_Copia))

print (f'{Diccionario7}')
print (f'{Diccionario7.keys()}')
print (f'{Diccionario7.values()}')
print (f'{Diccionario7.items()}')
print (f'{Diccionario7['Key2']}')
print (f'{Diccionario7.get("Key1")}')

print (f'-' * 20)

Diccionario_Numeral4 = {
    'Num1' : 7,
    'Num2' : 1,
    'Num3' : 4,
    'Num4' : 2,
    'Num5' : 5
}

Diccionario_Numeral4_Sorted = dict(sorted(Diccionario_Numeral4.items(), key=lambda num : num[1]))
Diccionario_Numeral4_Sorted_Min = min(Diccionario_Numeral4_Sorted.items(), key=lambda num : num[1])
Diccionario_Numeral4_Sorted_Max = max(Diccionario_Numeral4_Sorted.items(), key=lambda num : num[1])

print (f'{Diccionario_Numeral4}')
print (f'{Diccionario_Numeral4_Sorted}')
print (f'{Diccionario_Numeral4_Sorted_Min}')
print (f'{Diccionario_Numeral4_Sorted_Max}')

print (f'-' * 20)

Division_Baja = 14 // 7
Exponente2 = 4**3
Modulo2 = 20 % 6

print (f'El resultado de la operacion es {PEPE.Division_Flotante}')
print (f'El resultado de la operacion es {round(Division_Baja, 2)}')
print (f'El resultado de la operacion es {Exponente2}')
print (f'El resultado de la operacion es {Modulo2}')

print (f'-' * 20)

print (f'El tipo de dato es {type(variable1)}')
print (f'El tipo de dato es {type(variable4)}')
print (f'El tipo de dato es {type(PEPE.Division_Flotante)}')
print (f'El tipo de dato es {type(Lista_Uno_Copia)}')
print (f'El tipo de dato es {type(Tupla_Nombres3)}')
print (f'El tipo de dato es {type(Set_Conjunto_Menu1)}')
print (f'El tipo de dato es {type(Set_Conjunto_Menu2)}')
print (f'El tipo de dato es {type(Diccionario5)}')
print (f'El tipo de dato es {type(Funcion_Diccionario)}')
print (f'El tipo de dato es {type(Objeto57)}')
print (f'El tipo de dato es {type(PEPE)}')
print (f'El tipo de dato es {type(Array2)}')
print (f'El tipo de dato es {type(Data_Frame2)}')

print (f'-' * 20)

if (Diccionario3['Ingresos'] > 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Los ingresos son altos, Los gastos son bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Los ingresos son altos, Los gastos estas al limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Los ingresos son altos, Los gastos son altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] == 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Los ingresos son minimos, Los gastos son bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Los ingresos son minimos, Los gastos estas al limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Los ingresos son minimos, Los gastos son altos')
    else:
        print (f'Error de codigo')
elif (Diccionario3['Ingresos'] < 500): #type: ignore
    if (Diccionario3['Gastos'] < 200): #type: ignore
        print (f'Los ingresos son bajos, Los gastos son bajos')
    elif (Diccionario3['Gastos'] == 200): #type: ignore
        print (f'Los ingresos son bajos, Los gastos estas al limite')
    elif (Diccionario3['Gastos'] > 200): #type: ignore
        print (f'Los ingresos son bajos, Los gastos son altos')
    else:
        print (f'Error de codigo')
else:
    print (f'Error de codigo')
    
print (f'-' * 20)

var21 = 'Josue'
var22 = Variable_Sumatoria

if (var21 == variable1 and var22 >= 30):
    print (f'Correcto, ambas variables cumplen la condicion')
else:
    print (f'Error, al menos una de las variables no cumple la condicion')
    
if (var21 == variable1 or var22 >= 30):
    print (f'Correcto, al menos una de las variables cumple la condicion')
else:
    print (f'Error, ninguna de las variables cumple la condicion')
    
print (f'-' * 20)

print (f'{dir(PEPE)}')

def Ejercicio58(Num1:int, Num2:int) -> int:
    '''Esto es un docstring, tenemos dos argumentos y la funcion devuelve la sumatoria de dichos argumentos'''
    return Num1 + Num2

Sample58 = Ejercicio58(12, 4)

print (f'El resultado de la sumatoria es {Sample58}')

print (f'{help(Ejercicio58)}')

print (f'-' * 20)

class Entrenador():
    def __init__(self, Trainer, City, Favorite):
        self.Trainer = Trainer
        self.City = City
        self.Favorite = Favorite
        self.Pokedex = Sumatoria2(1, 2, 3, 4, 5)
        self.Classified = variable7
        self.Mine = [
            f'{PEPE.Diccionario_Poke1["Poke1"]}',
            f'{PEPE.Diccionario_Poke1["Poke2"]}',
            f'{PEPE.Diccionario_Poke1["Poke3"]}'
        ]
        self.Pokedex2 = 1000
        
    def Desplegar1(self):
        print (f'Trainer: {self.Trainer}')
        print (f'City: {self.City}')
        print (f'Favorite: {self.Favorite}')
        
    @property
    def Desplegar2(self):
        return self.Trainer
    
    def __repr__(self):
        return self.Trainer
    
    def __len__(self):
        return len(self.City)
    
    def __add__(self, Otro):
        return self.Pokedex + Otro.Pokedex2
    
    def __getitem__(self, Indice):
        return self.Mine[Indice]
    
    def __iter__(self):
        return iter(self.Mine)
    
Objeto58 = Entrenador(PEPE.Tupla_Pokemon[PEPE.Tupla_Pokemon.index("Ash")], 'Kanto', f'{PEPE.Diccionario_Poke1["Poke1"]}')
Objeto59 = Entrenador(PEPE.Tupla_Pokemon[PEPE.Tupla_Pokemon.index("Brooke")], 'Alolah', f'{PEPE.Diccionario_Poke1["Poke2"]}')
Objeto60 = Entrenador(PEPE.Tupla_Pokemon[PEPE.Tupla_Pokemon.index("Misty")], 'Paldea', f'{PEPE.Diccionario_Poke1["Poke3"]}')

Objeto58.Desplegar1()
print (f'El nombre del entrenador es {Objeto58.Desplegar2}')
print (f'El nombre del entrenador es {Objeto58}')
    
print (f'El numero de letras que tiene la ciudad {Objeto58.City} es {len(Objeto58)}')

print (f'El pokemon en la posicion 0 es {Objeto58[0]}')
print (f'El pokemon en la posicion 1 es {Objeto58[1]}')
print (f'El pokemon en la posicion 2 es {Objeto58[2]}')

for indice, elemento in enumerate(Objeto58, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

Objeto59.Desplegar1()
print (f'El nombre del entrenador es {Objeto59.Desplegar2}')
print (f'El nombre del entrenador es {Objeto59}')
    
print (f'El numero de letras que tiene la ciudad {Objeto59.City} es {len(Objeto59)}')

print (f'El pokemon en la posicion 0 es {Objeto59[0]}')
print (f'El pokemon en la posicion 1 es {Objeto59[1]}')
print (f'El pokemon en la posicion 2 es {Objeto59[2]}')

for indice, elemento in enumerate(Objeto59, start=1):
    print (f'{indice} : {elemento}')

print (f'-' * 20)

Objeto60.Desplegar1()
print (f'El nombre del entrenador es {Objeto60.Desplegar2}')
print (f'El nombre del entrenador es {Objeto60}')
    
print (f'El numero de letras que tiene la ciudad {Objeto60.City} es {len(Objeto60)}')

print (f'El pokemon en la posicion 0 es {Objeto60[0]}')
print (f'El pokemon en la posicion 1 es {Objeto60[1]}')
print (f'El pokemon en la posicion 2 es {Objeto60[2]}')

for indice, elemento in enumerate(Objeto60, start=1):
    print (f'{indice} : {elemento}')

print (f'-' * 20)

Negativo = -5

print (f'El numero negativo ahora se volvio positivo {int(abs(Negativo))}')

Any_Iterable = any(num % 2 == 0 for num in PEPE.Lista_Numeros)
Anonima4 = filter(lambda Num : Num % 2 == 0, PEPE.Lista_Numeros)
Lista_Iterable = [Num for Num in PEPE.Lista_Numeros if Num % 2 == 0]

Diccionario_Numeral5 = {
    'Num1' : 7,
    'Num2' : 1,
    'Num3' : 4,
    'Num4' : 2,
    'Num5' : 5
}

Diccionario_Numeral5_Sorted = dict(sorted(Diccionario_Numeral5.items(), key= lambda item : item[1]))
Diccionario_Numeral5_Sorted_Min = min(Diccionario_Numeral5_Sorted.items(), key= lambda item : item[1])
Diccionario_Numeral5_Sorted_Max = max(Diccionario_Numeral5_Sorted.items(), key= lambda item : item[1])

print (f'{Any_Iterable}')
print (f'{list(Anonima4)}')
print (f'{Lista_Iterable}')
print (f'{Diccionario_Numeral5}')
print (f'{Diccionario_Numeral5_Sorted}')
print (f'{Diccionario_Numeral5_Sorted_Min}')
print (f'{Diccionario_Numeral5_Sorted_Max}')

'''Lista_Colegio = []

Contador = int(input(f'Ingrese la cantidad de alumnos: '))

def Colegio(Lista):
    for elemento in range(Contador):
        Alumno_Nombre = input(f'Ingrese el nombre del alumno {elemento + 1}: ')
        Alumno_Edad = int(input(f'Ingrese la edad del alumno {elemento + 1}: '))
        Estudiante = [Alumno_Nombre, Alumno_Edad]
        Lista.extend([Estudiante])
        
    Lista.sort(key = lambda item : item[1])
    
    Menore = Lista[0][0]
    Mayore = Lista[-1][0]
    
    print (f'El menor de los estudiantes es {Menore} y su edad es {Lista[0][1]} años')
    print (f'El mayor de los estudiantes es {Mayore} y su edad es {Lista[-1][1]} años')

Colegio(Lista_Colegio)

print (f'-' * 20)'''

print (f'El binario del numero {Variable_Sumatoria} es {bin(Variable_Sumatoria)}')

if (bool(Diccionario3['Vacio']) == True):
    print (f'Gracias por ingresar la informacion')
else:
    print (f'Error, necesitas ingresar una cadena de texto')
    
Cociente, Residuo = divmod(158, 6)

print (f'El Cociente de la operacion es {Cociente}')
print (f'El Residuo de la operacion es {Residuo}')

print (f'-' * 20)

for elemento in Lista_Uno_Copia:
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Lista_Uno_Copia[:]:
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Lista_Uno_Copia[0:None]:
    print (f'{elemento}')
    
print (f'-' * 20)

for indice, elemento in enumerate(Lista_Uno_Copia, start=1):
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

for elemento in enumerate(Lista_Uno_Copia):
    print (f'{elemento[0]} : {elemento[1]}')
    
print (f'-' * 20)

var23 = 'eSteBAN'
var23_letra = var23[0]

print (f'{var23}')
print (f'{var23.lower()}')
print (f'{var23.upper()}')
print (f'{var23.capitalize()}')
print (f'{var23.title()}')

Lista_Nombres5 = ['juan salvo', 'henry courtney', 'elizabeth bennet', 'marge simpson']
Lista_Nombres5_Actualizado = list([])

for indice, elemento in enumerate(Lista_Nombres5[:]):
    print (f'{indice} : {elemento.title()}')
    Lista_Nombres5_Actualizado.append(elemento.title())
    
print (f'-' * 20)

print (f'{Lista_Nombres5_Actualizado}')

print (f'{var23.lower().find("t")}')
print (f'{var23.lower().index("b")}')

print (f'La letra {var23_letra} aparece un total de {var23.lower().count(var23_letra)} veces')

print (f'{var23.lower().startswith(var23_letra)}')
print (f'{var23.lower().endswith("n")}')

print (f'{var23.lower().replace("ban", "POPOTAMO")}')

var24 = '          Lautar5@o'

print (f'{var24}')
print (f'{var24.strip()}')
print (f'{var24.strip().strip("5@")}')
print (f'{" ".join(var24.split()).strip("5")}')

var25 = '----hola mundo***'

import re

Buscar20 = re.sub(r'\d\W', '', var24)

print (f'{Buscar20.strip()}')

print (f'-' * 20)

var26 = 'esto es un texto cualquiera, lo que deseamos es ver si esta cosa realmente sirve o no'

Lista_var26 = var26.split(' ')

for elemento in Lista_var26:
    print (f'{elemento}')
    
print (f'La cantidad de palabras digitadas es {len(Lista_var26)}')

print (f'-' * 20)

var27 = 'texto'

if (isinstance(var27, (str))):
    print (f'Lo que ingresaste es solo texto')
else:
    print (f'Error, esto no es texto')
    
if (var27.isalpha()):
    print (f'Lo que ingresaste es solo texto')
else:
    print (f'Error, esto no es texto')
    
try:
    Numerito = float(var27)
    if (Numerito.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Lo que ingresaste es texto')
    
print (f'-' * 20)

var28 = 3.5

if (isinstance(var28, (float))):
    print (f'Lo que ingresaste es un numero decimal')
else:
    print (f'Lo que ingresaste no es un numero decimal')
    
try:
    Numerito1 = float(var28)
    if (Numerito1.is_integer()):
        print (f'Lo que ingresaste es un numero entero')
    else:
        print (f'Lo que ingresaste es un numero decimal')
except ValueError:
    print (f'Error, esto no es un numero')
    
print (f'-' * 20)

var29 = '3'

if (isinstance(var29, (int))):
    print (f'Esto es un numero entero')
else:
    print (f'Error esto no es un numero entero')
    
if (var29.isnumeric()):
    print (f'Esto es un numero entero')
else:
    print (f'Error esto no es un numero entero')

if (var29.isdecimal()):
    print (f'Esto es un numero entero')
else:
    print (f'Error esto no es un numero entero')
    
try:
    Numerito2 = float(var29)
    if (Numerito2.is_integer()):
        print (f'Esto es un numero entero')
    else:
        print (f'Esto es un numero decimal')
except ValueError:
    print (f'Error, esto no es un nu texto')
    
print (f'-' * 20)

var30 = 3

if (isinstance(var30, (int, float))):
    print (f'Esto es un numero entero o decimal')
else:
    print (f'Error de formato')
    
try:
    Numerito3 = float(var30)
    if (Numerito3.is_integer()):
        print (f'Esto es un numero entero')
    else:
        print (f'Esto es un numero decimal')
except ValueError:
    print (f'Error, esto no es un numero')
    
print (f'-' * 20)

var31 = 'erick123'

if (isinstance(var31, (int, str))):
    print (f'Esto tiene numeros o letras, o ambos')
else:
    print (f'Error de formato')
    
if (var31.isalnum):
    print (f'Esto tiene numeros o letras, o ambos')
else:
    print (f'Error de formato')
    
try:
    Numerito4 = float(var31)
    if (Numerito4.is_integer()):
        print (f'Esto esta compuesto por numeros enteros')
    else:
        print (f'Esto esta compuesto por numeros decimales')
except ValueError:
    print (f'Esto esta compuesto por texto')
    
print (f'-' * 20)

var32 = '   a    '

if (var32.isspace()):
    print (f'Esto esta compuesto unicamente por espacios')
else:
    print (f'Error, esto tiene mucho mas que solo espacios')

print (f'-' * 20)

var33 = 'eSteBAN'

if (var33.lower().islower()):
    print (f'Esto esta compuesto unicamente por letras minusculas')
else:
    print (f'Error esto no esta en minuscula')
    
if (var33.upper().isupper()):
    print (f'Esto esta compuesto unicamente por letras mayusculas')
else:
    print (f'Error esto no esta en mayusculas')
    
if (var33.title().istitle()):
    print (f'Esto esta compuesto unicamente por letras camel case')
else:
    print (f'Error esto no esta en camel case')
    
print (f'-' * 20)

var34 = ' '

if (bool(var34) == True):
    print (f'Esto tiene contenido')
else:
    print (f'Esto esta completamente vacio')
    
print (f'-' * 20)

print (f'{Lista_Uno_Copia[1]} se encuentra en la posicion {Lista_Uno_Copia.index("Josue")} de la lista')

Lista_Nombres5_Copia = Lista_Nombres5.copy()

print (f'{Lista_Nombres5}')
print (f'{Lista_Nombres5_Copia}')

print (f'{Diccionario1_Copia}')

Diccionario1_Copia.clear()

print (f'{Diccionario1_Copia}')

Diccionario_Eliminado = Diccionario2.pop("Nombre")

print (f'Elemento eliminado: {Diccionario_Eliminado}')

print (f'-' * 20)

for elemento in Diccionario1X:
    print (f'{Diccionario1X[elemento]}')
    
print (f'-' * 20)

for elemento in Diccionario1X.keys():
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in Diccionario1X.values():
    print (f'{elemento}')
    
print (f'-' * 20)

for indice, elemento in Diccionario1X.items():
    print (f'{indice} : {elemento}')
    
print (f'-' * 20)

try:
    snake_case7, snake_case8, snake_case9, snake_case10 = Lista_Uno_Copia
    print (f'Correcto el desempaquetado')
except ValueError:
    print (f'Error, este desempaquetado esta mal')
    
print (f'{Lista_Uno_Copia}')
    
print (f'-' * 20)

Contador = 0

while (Contador < 5):
    print (f'El contador es {Contador + 1}')
    Contador += 1
    
print (f'-' * 20)

Contador = 0

while (Contador < len(PEPE.Lista_Numeros)):
    print (f'Numero {PEPE.Lista_Numeros[Contador]} multiplicado seria {PEPE.Lista_Numeros[Contador] * 100}')
    Contador += 1
    
print (f'-' * 20)

Lista_Animales2 = []
Lista_Animales2.append('Avestruz')
Lista_Animales2.insert(1, 'Cocodrilo')
Lista_Animales2.extend([f'{PEPE.Lista2[2]}'])

print (f'{Lista_Animales2}')

Contador = 0

while (Contador < len(Lista_Animales2)):
    if (Lista_Animales2[Contador] == PEPE.Lista2[PEPE.Lista2.index("Koala")]):
        print (f'Este animal viene de Australia y es el favorito de millones')
        break
    else:
        Contador += 1
        continue
    
print (f'-' * 20)

for elemento1 in zip(Tupla1):
    print (f'{elemento1}')
    
print (f'-' * 20)

for elemento1, elemento2 in zip(Lista_Uno_Copia, Tupla1):
    print (f'{elemento1} -- {elemento2}')
    
print (f'-' * 20)

for elemento1, elemento2, elemento3, elemento4 in zip(Lista_Uno_Copia, Tupla1, PEPE.Tupla_Pokemon, Set_Conjunto_Menu1):
    print (f'{elemento1} -- {elemento2} -- {elemento3} -- {elemento4}')
    
print (f'-' * 20)

for elemento in range(5):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(995, 1000):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(0 + 2, len(Lista_Uno_Copia[0:None])):
    print (f'{elemento}')
    
print (f'-' * 20)

for elemento in range(0, len(Lista_Walrus3 := [1, 2, 3, 4, 5])):
    print (f'{elemento}')
    
print (f'-' * 20)

Lista_Numeros_Mult = [num * 100 for num in PEPE.Lista_Numeros]

print (f'{Lista_Numeros_Mult}')

print (f'-' * 20)

Menor = min(Lista_Numeros_Mult)
Mayor = max(Lista_Numeros_Mult)

print (f'El Menor de los numeros es {Menor}')
print (f'El Mayor de los numeros es {Mayor}')

Redondeado = round(14.458795, 2)

print (f'{Redondeado}')

print (f'{bool("")}')
print (f'{bool(None)}')
print (f'{bool(False)}')
print (f'{bool(not True)}')
print (f'{bool(0)}')

print (f'-' * 20)

Todo_All = all([Lista_Uno_Copia, Set_Conjunto_Menu1, PEPE.Tupla_Pokemon, None])

print (f'{Todo_All}')

Sumatoria5 = sum(Lista_Numeros_Mult)

print (f'{Sumatoria5}')

var35 = list(Set_Conjunto_Menu1)
var36 = set(PEPE.Set_Conjunto_Poke1)
var37 = tuple(Lista_Animales1)
var38 = str(500)
var39 = int('500')
var40 = float(var38)

print (f'{type(Set_Conjunto_Menu1)} se convirtio en {type(var35)}')
print (f'{type(PEPE.Set_Conjunto_Poke1)} se convirtio en {type(var36)}')
print (f'{type(Lista_Animales1)} se convirtio en {type(var37)}')
print (f'{type(500)} se convirtio en {type(var38)}')
print (f'{type('500')} se convirtio en {type(var39)}')
print (f'{type(var38)} se convirtio en {type(var40)}')

print (f'-' * 20)

print (f' - '.join(PEPE.Set_Conjunto_Poke1))

import Nueva.Nueva2.Nueva3.Modulo_Propio2 as PEPE3

PEPE3.Saludar5()

print (f'-' * 20)

from Paquete.Sub_Paquete import Segundo as PEPE4

Variable_PEPE4 = PEPE4

'''def Ejercicio59():
    while (True):
        Numero = input(f'Ingrese un numero: ')
        try:
            Numerito5 = float(Numero)
            if (Numerito5.is_integer()):
                print (f'Lo que ingresaste es un numero entero')
                break
            else:
                print (f'Lo que ingresaste es un numero decimal')
                break
        except ValueError:
            print (f'Error, lo que ingresaste no un numero')

Ejercicio59()'''

print (f'-' * 20)

import pandas as pd
import requests
import io

Ruta_Html3 = 'https://en.wikipedia.org/wiki/Louisiana'

headers = {'User-Agent' : 'Mozilla/5.0'}

Response = requests.get(Ruta_Html3, headers=headers)

Leer_Html3 = io.StringIO(Response.text)

Cargar_Html3 = pd.read_html(Leer_Html3)

print (f'{Cargar_Html3[2].head()}')

print (f'-' * 20)

import re

Texto13 = 'ericksuper80@hotmail.com'

Pattern18 = r'[a-zA-Z0-9\.\/\*\-\+\_]+\@(?:gmail|hotmail|yahoo)\.(?:com|net|org)'

Buscar21 = bool(re.fullmatch(Pattern18, Texto13))

if (Buscar21 == True):
    print (f'Este correo electronico tiene un formato correcto')
else:
    print (f'Error, el formato del correo es invalido')
    
print (f'-' * 20)

import re

Texto14 = '32'

Pattern19 = r'(0[0-9]|[12][0-9]|3[01])'

Buscar22 = bool(re.match(Pattern19, Texto14))

if (Buscar22 == True):
    print (f'El numero se encuentra entre 01 y 31')
else:
    print (f'Error, este numero esta fuera de rango')
    
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
    print (f'Genial! hemos encontrado ventas en esta fecha')
    
    Grupo8 = Encontrado4.groupby('product')['quantity'].sum()
    Grupo8_Min = Grupo8.idxmin()
    Grupo8_Max = Grupo8.idxmax()
    Grupo8_Min_Cant = Grupo8.min()
    Grupo8_Max_Cant = Grupo8.max()
    
    print (f'El producto que vendio menos fue {Grupo8_Min} y la cantidad vendida fue {Grupo8_Min_Cant}')
    print (f'El producto que vendio mas fue {Grupo8_Max} y la cantidad vendida fue {Grupo8_Max_Cant}')
    
    print (f'La cantidad de clientes que compraron fue {Grupo8.count()}')
    
    print (f'La cantidad de productos vendidos fue {Grupo8.sum()}')
    
    Grupo9 = Encontrado4.groupby('product')['TOTALITO'].sum()
    
    print (f'Total de dinero vendido ${Grupo9.sum()}')
    
    Promedio7 = Grupo9.sum() / Grupo9.count()
    
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Promedio7, 2)}')
    print (f'El promedio de dinero vendido en esta fecha fue de ${round(Grupo9.sum(), 2)}')
    
print (f'-' * 20)

import requests

Lista_Api1 = list([
    'Caramelo',
    'Pastel',
    'Chicle'
])

Api3 = requests.post('http://127.0.0.1:8000/grupo1/unidad1/', json=(Lista_Api1))
Api4 = Api3.json()

print (f'{Api3.status_code}')
print (f'{Api4}')

print (f'-' * 20)

Api1 = requests.get('http://127.0.0.1:8000/grupo1/')
Api2 = Api1.json()

print (f'{Api1.status_code}')
print (f'{Api2}')

print (f'-' * 20)