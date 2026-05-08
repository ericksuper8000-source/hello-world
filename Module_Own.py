Diccionario_Poke = dict.fromkeys(['Poke1', 'Poke2', 'Poke3'])

Set_Conjunto_Poke = {'Pikachu'}
Set_Conjunto_Poke.add('Graveler')
Set_Conjunto_Poke.add('Vaporeon')

for elemento in Set_Conjunto_Poke:
    if (elemento == 'Pikachu'):
        Diccionario_Poke['Poke1'] = elemento
    elif (elemento == 'Graveler'):
        Diccionario_Poke['Poke2'] = elemento
    elif (elemento == 'Vaporeon'):
        Diccionario_Poke['Poke3'] = elemento
    else:
        continue

print (f'{Diccionario_Poke}')

for elemento in Diccionario_Poke.keys():
    print (f'{elemento}')

print (f'-' * 20)

for elemento in Diccionario_Poke.values():
    print(f'{elemento}')

print(f'-' * 20)

for elemento in Diccionario_Poke.items():
    print(f'{elemento[0]} -- {elemento[1]}')

print(f'-' * 20)

for elemento in Diccionario_Poke:
    print (f'{Diccionario_Poke[elemento]}')

print (f'-' * 20)

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

def Primera(Segunda):
    def Tercera():
        print (f'xxxxxxxxxxxxxxxx')
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
def Saludar2(Nombre='Juliana'):
    return Nombre

def Primera(Segunda):
    def Tercera(*args):
        return Segunda('Tiranosaurio')

    return Tercera

@Primera
def Saludar3(Nombre:str) -> str:
    return Nombre

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) + 1

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
        Sexo = 'FEMENINO'
        return Segunda(Nombre, Sexo)

    return Tercera

@Primera
def Usuario(Nombre, Sexo):
    Genero = Sexo.lower()
    if (Genero == 'masculino'):
        print (f'{Nombre}, eres un hombre')
    else:
        print (f'{Nombre} eres una mujer')

def Primera(Segunda):
    def Tercera(*args):
        return Segunda(88)

    return Tercera

@Primera
def Contrasena(numero:int) -> int:
    chars = 'abcdefghij'
    numero_str = str(numero)
    numero_int = int(numero_str[0])
    c1 = numero_int - 2
    c2 = numero_int
    c3 = numero_int - 5
    password = f'{chars[c1]}{chars[c2]}{chars[c3]}{int(abs(numero * c2))}'
    return password

Tupla_Poke = 'Ash', 'Brooke', 'Misty',

Lista_Numeros = [1]
Lista_Numeros.append(3)
Lista_Numeros.insert(1, 2)
Lista_Numeros.extend([4, 5])

print (f'{Lista_Numeros}')

Variable_Funcion_Anonima1 = lambda Num1, Num2 : Num1 * Num2
Variable_Funcion_Anonima2 = lambda Num : Num * 2
Variable_Funcion_Anonima3 = filter(lambda Num : Num % 2 == 0, Lista_Numeros)

Any_Par = any(num % 2 == 0 for num in Lista_Numeros)
Lista_Par = [num for num in Lista_Numeros if num % 2 == 0]

print (f'{Any_Par}')
print (f'{Lista_Par}')

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

Lista1 = ['Erick', 'Josue', 'Perez', 'Gutierrez']
Lista2 = [Division_Flotante, 20, 'Koala', True]
Lista3 = list([1, 2, 3, 4])
Lista3.extend([5])
Lista4 = [4000, 97, 15, 300]

'''Flotante1 = int(input(f'Ingrese un numero: '))

Flotante2 = input(f'Ingrese una operacion tipo 4*3: ')

Flotante3 = input(f'Ingrese un valor: ')
Flotante3_Limpio = Flotante3.replace(' ', '')

Flotante4 = input(f'Ingrese una cadena de texto: ')'''

