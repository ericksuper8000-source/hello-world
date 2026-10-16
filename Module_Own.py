Diccionario_Poke = dict.fromkeys(['Poke1', 'Poke2', 'Poke3'])

Set_Conjunto_Poke1 = {'Pikachu'}
Set_Conjunto_Poke1.add("Graveler")

Set_Conjunto_Poke2 = set({'Vaporeon'})

Set_Conjunto_Poke1.update(Set_Conjunto_Poke2)

for elemento in Set_Conjunto_Poke1:
    if (elemento == 'Pikachu'):
        Diccionario_Poke['Poke1'] = elemento
    elif (elemento == 'Graveler'):
        Diccionario_Poke['Poke2'] = elemento
    elif (elemento == 'Vaporeon'):
        Diccionario_Poke['Poke3'] = elemento
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
        print (f'Cantidad: {self.Cantidad}')
        print (f'Catched: {self.Catched}')
        
    def __str__(self):
        return self.Nombre
    
'''Flotante1 = int(input(f'Ingrese un numero cualquiera: '))

Flotante2 = input(f'Ingrese una operacion tipo 4*3: ')

Flotante3 = input(f'Ingrese su nombre completo: ')

Flotante4 = input(f'Ingrese una cadena de texto: ')'''

def Saludar1():
    print (f'Hola Mundo')
    
def Saludar2(Nombre = 'Carmelo'):
    return Nombre

def Saludar3(Nombre : str) -> str:
    return Nombre

def Primera(Segunda): #type: ignore
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) - 18
        
    return Tercera

@Primera
def Sumatoria1(Num1:int, Num2:int) -> int:
    return Num1 + Num2

def Primera(Segunda): #type: ignore
    def Tercera(*args):
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
        print (f'{Nombre}, tu eres un hombre')
    else:
        print (f'{Nombre}, tu eres una mujer')
        
def Primera(Segunda):
    def Tercera(*args):
        return Segunda(69)
        
    return Tercera
        
@Primera
def Contrasena(Numero):
    chars = 'abcdefghij'
    Numero_Str = str(Numero)
    Numero_Int = int(Numero_Str[0])
    c1 = Numero_Int - 2
    c2 = Numero_Int
    c3 = Numero_Int - 5
    Password = f'{chars[c1]}{chars[c2]}{chars[c3]}{Numero * c2}'
    return Password

Lista_Numeros1 = list([1, 2])
Lista_Numeros1.append(3)
Lista_Numeros1.insert(4, 4)
Lista_Numeros1.extend([5])

Variable_Funcion_Anonima1 = lambda Num1, Num2 : Num1 * Num2
Variable_Funcion_Anonima2 = lambda Num : Num * 2
Variable_Funcion_Anonima3 = filter(lambda Num : Num % 2 == 0, Lista_Numeros1)

Anonima_Par = any(Num % 2 == 0 for Num in Lista_Numeros1)
Lista_Par = [num for num in Lista_Numeros1 if num % 2 == 0]

GLOBAL = 30

Division_Flotante = 14 // 7

Lista1 = ['Erick', 'Josue', 'Perez', 'Gutierrez']
Lista2 = [Division_Flotante, 300, 'Koala', not False]
Lista3 = list(Lista_Numeros1)
Lista4 = list([4000, 97, 15, 300])

Tupla_Poke = ('Ash', 'Brooke', 'Misty',)