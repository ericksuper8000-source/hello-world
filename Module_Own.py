Diccionario_Pokemon = dict.fromkeys(['Poke1', 'Poke2', 'Poke3'])

Set_Conjunto_Poke = {'Pikachu'}
Set_Conjunto_Poke.add('Graveler')

Set_Conjunto_Poke2 = set({'Vaporeon'})

Set_Conjunto_Poke.update(Set_Conjunto_Poke2)

for elemento in enumerate(Set_Conjunto_Poke):
    if (elemento[1] == 'Pikachu'):
        Diccionario_Pokemon['Poke1'] = elemento[1]
    elif (elemento[1] == 'Graveler'):
        Diccionario_Pokemon['Poke2'] = elemento[1]
    elif (elemento[1] == 'Vaporeon'):
        Diccionario_Pokemon['Poke3'] = elemento[1]
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
        
def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'ZZZZ')
        Segunda()
        print (f'ZZZZ')
        
    return Tercera
 
@Primera        
def Saludar1():
    print (f'Hola Mundo')
    
def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda('Carmelo')
        
    return Tercera
    
@Primera
def Saludar2(Nombre = 'Juanita La Cubanita'):
    return Nombre

def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda('DINOSAURIO')
    
    return Tercera

@Primera
def Saludar3(Nombre:str) -> str:
    return Nombre

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) + 1
        
    return Tercera

@Primera
def Sumatoria1(Num1:int, Num2:int) -> int:
    return Num1 + Num2

def Primera(Segunda): #type: ignore
    def Tercera(*arg):
        return Segunda(2)
        
    return Tercera

@Primera
def Par(Numero):
    if (Numero % 2 == 0):
        return True
    else:
        return False
    
def Primera(Segunda): #type: ignore
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
        print (f'{Nombre}, eres una mujer')
        
def Primera(Segunda):
    def Tercera(*args):
        return Segunda(96)
        
    return Tercera
        
@Primera
def Contrasena(Numero):
    chars = 'abcdefghij'
    Num_Str = str(Numero)
    Num_Int = int(Num_Str[0])
    c1 = Num_Int - 2
    c2 = Num_Int
    c3 = Num_Int - 5
    Password = f'{chars[c1]}{chars[c2]}{chars[c3]}{int(abs(c2 * Numero))}'
    return Password

Lista_Numeros = [1, 2, 3, 4, 5]

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
        self.Cantidad = 18 * 2
        self.Catched = not True

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')
        
Tupla_Poke = tuple(('Ash', 'Brooke', 'Misty'))

Division_Flotante = 14/7

Lista1 = ['Erick', 'Josue', 'Perez', 'Gutierrez']
Lista2 = [Division_Flotante, 300, 'Koala', True]
Lista3 = list([1, 2, 3, 4, 5])
Lista4 = [4000, 97, 15, 300]

'''Flotante1 = input(f'Ingrese un numero: ')

Flotante2 = int(input(f'Ingrese un numero: '))'''

'''Flotante3 = input(f'Agregue una operacion tipo 4*3: ')'''

'''Flotante4 = input(f'Ingrese un numero: ')'''

'''Flotante5 = input(f'Ingrese una cadena de texto: ')'''