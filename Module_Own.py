Diccionario_Poke = dict.fromkeys(['Poke1', 'Poke2', 'Poke3'])

Set_Conjunto_Poke = set({'Pikachu'})
Set_Conjunto_Poke.add('Graveler')
Set_Conjunto_Poke.add('Vaporeon')

for indice, elemento in enumerate(Set_Conjunto_Poke, start=1):
    if (elemento == 'Pikachu'):
        Diccionario_Poke['Poke1'] = elemento
    elif (elemento == 'Graveler'):
        Diccionario_Poke['Poke2'] = elemento
    elif (elemento == 'Vaporeon'):
        Diccionario_Poke['Poke3'] = elemento
    else:
        continue

print (f'{Diccionario_Poke}')

class Pokemon():
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
        print (f'ANTES')
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
def Saludar2(Nombre = 'Juanita'):
    return Nombre

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
        Sexo = 'FemeNINO'
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
        return Segunda(88)

    return Tercera

@Primera
def Contrasena(Numero:int) -> int:
    chars = 'abcefghij'
    Numero_Str = str(Numero)
    Numero_Int = int(Numero_Str[0])
    c1 = Numero_Int - 2
    c2 = Numero_Int
    c3 = Numero_Int - 5
    Password = f'{chars[c1]}{chars[c2]}{chars[c3]}{int(abs(c2 * Numero))}'
    return Password

Lista_Numeros = []
Lista_Numeros.append(1)
Lista_Numeros.insert(1, 2)
Lista_Numeros.extend([3, 4, 5])

print (f'{Lista_Numeros}')

Tupla_Poke = ('Ash', 'Brooke', 'Misty')

Variable_Funcion_Anonima1 = lambda Num1, Num2 : Num1 * Num2
Variable_Funcion_Anonima2 = lambda Num : Num  * 2
Variable_Funcion_Anonima3 = filter(lambda Num : Num % 2 == 0, Lista_Numeros)

Any_Par = any(num % 2 == 0 for num in Lista_Numeros)
Lista_Par = [num for num in Lista_Numeros if num % 2 == 0]

print (f'{Any_Par}')
print (f'{Lista_Par}')

Global = 30

class A():
    def Mostrar(self):
        print (f'Hola A')

class E():
    def Mostrar(self):
        print (f'Hola E')

class B(E):
    def Mostrar(self):
        print (f'Hola B')

class C(A):
    def Mostrar(self):
        print (f'Hola C')

class D(B,C):
    def Mostrar(self):
        print (f'Hola D')

Objeto17 = D()

A.Mostrar(Objeto17)
B.Mostrar(Objeto17)
C.Mostrar(Objeto17)
Objeto17.Mostrar()
E.Mostrar(Objeto17)

print (f'------------')

Division_Flotante = 14/7

Lista1 = ['Erick', 'Josue', 'Perez', 'Gutierrez']
Lista2 = [Division_Flotante, 250, 'Koala', True]
Lista3 = list([1, 2, 3, 4, 5])
Lista4 = [4000, 97, 15, 200]
'''
Flotante1 = int(input(f'Ingrese un numero: '))

Flotante2 = input(f'Ingrese una operacion tipo 4*3: ')

Flotante3 = input(f'Ingrese una cadena de texto: ')'''