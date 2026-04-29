Diccionario_Poke = dict.fromkeys(['Poke1', 'Poke2', 'Poke3'])

Set_Conjunto_Poke = {'Pikachu'}
Set_Conjunto_Poke.add('Graveler')
Set_Conjunto_Poke.add('Vaporeon')

for elemento in enumerate(Set_Conjunto_Poke):
    if (elemento[1] == 'Pikachu'):
        Diccionario_Poke['Poke1'] = elemento[1]
    elif (elemento[1] == 'Graveler'):
        Diccionario_Poke['Poke2'] = elemento[1]
    elif (elemento[1] == 'Vaporeon'):
        Diccionario_Poke['Poke3'] = elemento[1]
    else:
        continue

print (f'{Diccionario_Poke}')

class Pokemon1():
    def __init__(self, Nombre, Tipo, Ataque):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque
        self.Cantidad = 18 * 2
        self.Catched = not True

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')

def Parametros(Lista):
    Numero_Menor = min(Lista)

    import numpy as np

    Numero_Mayor = np.max(Lista)
    Resultado_Lista = [Numero_Menor, int(Numero_Mayor)]
    return Resultado_Lista

Lista_Parametros = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print (f'El resultado de la operacion es {Parametros(Lista_Parametros)}')

def Primera(Segunda):
    def Tercera():
        print (f'XXXXXXXXXXX')
        Segunda()

    return Tercera

@Primera
def Saludar1():
    print (f'Hola Mundo')

def Primera(Segunda):
    def Tercera(*args):
        return Segunda('Carmelo')

    return Tercera

@Primera
def Saludar2(Nombre = 'Juana La Cubana'):
    return Nombre

def Saludar3(Nombre:str) -> str:
    return Nombre

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 11

    return Tercera

@Primera
def Sumatoria1(Num1:int, Num2:int) -> int:
    return Num1 + Num2

def Primera(Segunda):
    def Tercera(*args):
        return Segunda(2)

    return Tercera

@Primera
def Par(Numero):
    if (Numero % 2 == 0):
        return True
    else:
        return False

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        Nombre = 'Juana La Cubana'
        Sexo = 'Femenino'
        return Segunda(Nombre, Sexo)

    return Tercera

@Primera
def Usuario(Nombre, Sexo):
    Genero = Sexo.lower()
    if (Genero == 'masculino'):
        print (f'{Nombre}, eres un hombre')
    else:
        print (f'{Nombre}, eres una mujer')

def Primera(Segunda):
    def Tercera(*args):
        return Segunda(35)

    return Tercera

@Primera
def Contrasena(Numero:int) -> int:
    chars = 'abcdefghij'
    Numero_Str = str(Numero)
    Numero_Int = int(Numero_Str[0])
    c1 = Numero_Int - 2
    c2 = Numero_Int
    c3 = Numero_Int - 5
    Password = f'{chars[c1]}{chars[c2]}{chars[c3]}{int(abs(c2 * Numero))}'
    return Password

Lista_Numeros = []
Lista_Numeros.extend([1, 2])
Lista_Numeros.insert(2, 3)
Lista_Numeros.insert(3, 4)
Lista_Numeros.append(5)

print (f'{Lista_Numeros}')

Variable_Funcion_Anonima1 = lambda Num1, Num2 : Num1 * Num2
Variable_Funcion_Anonima2 = lambda Num : Num * 2
Variable_Funcion_Anonima3 = filter(lambda Num : Num % 2 == 0, Lista_Numeros)

Any_Pares = any(num % 2 == 0 for num in Lista_Numeros)
Lista_Pares = [num for num in Lista_Numeros if num % 2 == 0]

print (f'{Any_Pares}')
print (f'{Lista_Pares}')

GLOBAL = 30

class Pokemon2():
    def __init__(self, Nombre, Tipo, Ataque):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque
        self.Cantidad = 18 * 2
        self.Catched = not True

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')

Division_Flotante = 14/7

Tupla_Poke = 'Ash', 'Misty', 'Brooke',

print (f'{type(Tupla_Poke)}')

Lista1 = ['Erick', 'Josue', 'Perez', 'Gutierrez']
Lista2 = [Division_Flotante, 200, 'Koala', not True]
Lista3 = list([1, 2, 3, 4])
Lista3.append(5)
Lista4 = [4000, 97, 15, 300]