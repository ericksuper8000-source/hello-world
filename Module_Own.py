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
        
Lista_Numeros = []
Lista_Numeros.append(1)
Lista_Numeros.insert(1, 2)
Lista_Numeros.append(3)
Lista_Numeros.extend([4, 5])

def Primera(Segunda):
    def Tercera():
        print (f'ANTES')
        return Segunda()
        
    return Tercera

@Primera
def Saludar1():
    return f'Hola Mundo'

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
        return Segunda(*args, **kwargs) + 1
        
    return Tercera

@Primera
def Sumatoria1(Num1:int, Num2:int) -> int:
    return Num1 + Num2

def Primera(Segunda):
    def Tercera(*args):
        return Segunda(8)
        
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
        return f'{Nombre}, eres un hombre'
    else:
        return f'{Nombre}, eres una mujer'
    
def Primera(Segunda):
    def Tercera(*args):
        return Segunda(88)
        
    return Tercera

@Primera    
def Contrasena(Numero:int) -> int:
    chars = 'abcdefghij'
    numero_str = str(Numero)
    numero_int = int(numero_str[0])
    c1 = numero_int - 2
    c2 = numero_int
    c3 = numero_int - 5
    password = f'{chars[c1]}{chars[c2]}{chars[c3]}{int(abs(Numero * c2))}'
    return password

Variable_Funcion_Anonima1 = lambda Num1, Num2 : Num1 * Num2
Variable_Funcion_Anonima2 = lambda Num : Num * 2
Variable_Funcion_Anonima3 = filter(lambda Num : Num % 2 == 0, Lista_Numeros)

Any_Par = any(num % 2 == 0 for num in Lista_Numeros)
Lista_Par = [num for num in Lista_Numeros if num % 2 == 0]

GLOBAL = 30

class Pokemon2():
    def __init__(self, Nombre, Tipo, Ataque):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque
        self.Cantidad = 37
        self.Catched = not True

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')
        
Division_Flotante = 14/7
        
Lista1 = ['Erick', 'Josue', 'Perez', 'Gutierrez']
Lista2 = [Division_Flotante, 600, 'Koala', True]
Lista3 = list([1, 2, 3, 4])
Lista3.append(5)
Lista4 = [4000, 97, 15, 300]

Tupla_Poke = 'Ash', 'Brooke', 'Misty',

'''Flotante1 = input(f'Ingrese un numero entero: ')
Flotante2 = input(f'Ingrese una operacion tipo 4*3: ')
Flotante3 = input(f'Ingrese su nombre: ')'''