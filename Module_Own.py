'''Flotante1 = int(input(f'Ingrese un numero: '))'''

'''Flotante2 = input(f'Ingrese una operacion tipo 4 * 3: ')'''

'''Flotante3 = input(f'Ingrese su nombre: ')'''

'''Flotante4 = input(f'Ingrese una cadena de texto: ')'''

Diccionario_Poke = dict.fromkeys(['Poke1', 'Poke2', 'Poke3'])

Set_Conjunto_Poke1 = {'Pikachu'}
Set_Conjunto_Poke1.add('Graveler')

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
        
def Primera(Segunda): #type: ignore
    def Tercera():
        print (f'ANTES DEL SALUDO')
        Segunda()
        
    return Tercera
        
@Primera
def Saludar1():
    print (f'Hola Mundo')
    
def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda('Carmelo')
        
    return Tercera
    
@Primera
def Saludar2(Nombre = 'Juana La Cubana'):
    return Nombre

def Primera(Segunda): #type: ignore
    def Tercera(*args):
        return Segunda('Carmel')
        
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
        Sexo = 'FeMENIno'
        return Segunda(Nombre, Sexo)
        
    return Tercera
    
@Primera
def Usuario1(Nombre, Sexo):
    Genero = Sexo.lower()
    if (Genero == 'masculino'):
        print (f'{Nombre}, eres un hombre')
    else:
        print (f'{Nombre}, eres una mujer')
        
def Primera(Segunda):
    def Tercera(*args):
        return Segunda(87)
        
    return Tercera
        
@Primera
def Contrasena(Numero):
    chars = 'abcdefghij'
    Numero_Str = str(Numero)
    Numero_Int = int(Numero_Str[0])
    c1 = Numero_Int - 2
    c2 = Numero_Int
    c3 = Numero_Int - 5
    Password = f'{chars[c1]}{chars[c2]}{chars[c3]}{int(abs(c2 * Numero))}'
    return Password

Lista_Numeros = [1, 2]
Lista_Numeros.append(3)
Lista_Numeros.insert(4, 4)
Lista_Numeros.extend([5])

Tupla_Poke = tuple(('Ash', 'Brooke', 'Misty'))

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
        
    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')
        
Division_Flotante = 14/ 7 
  
Lista1 = ['Erick', 'Josue', 'Perez', 'Gutierrez']
Lista2 = [Division_Flotante, 200, 'Koala', not True]
Lista3 = list([1, 2, 3, 4, 5])
Lista4 = [4000, 15, 97, 300]