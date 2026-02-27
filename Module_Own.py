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
        Nombre = 'Carmelo'
        return Segunda(Nombre)

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
        Nombre = 'Juanita La Cubanita'
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
        return Segunda(77)

    return Tercera

@Primera
def Contrasena(Numero:int) -> int:
    chars = 'abcdefghij'
    Num_Str = str(Numero)
    Num_Int = int(Num_Str[0])
    c1 = Num_Int - 2
    c2 = Num_Int
    c3 = Num_Int - 5
    Password = f'{chars[c1]}{chars[c2]}{chars[c3]}{int(abs(c2 * Numero))}'
    return Password

Tupla_Poke = ('Ash', 'Brooke', 'Misty')

Lista_Numeros = [1, 2, 3, 4, 5]

Variable_Funcion_Anonima1 = lambda Num1, Num2 : Num1 * Num2
Variable_Funcion_Anonima2 = lambda Num :  Num * 2
Variable_Funcion_Anonima3 = filter(lambda Num : Num % 2 == 0, Lista_Numeros)

Any_Par = any(num % 2 == 0 for num in Lista_Numeros)
Lista_Pares = [num for num in Lista_Numeros if num % 2 == 0]

print (f'{Any_Par}')
print (f'{Lista_Pares}')

Global = 30

class Pokemon:
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


class Poke2(Pokemon):
    def __init__(self, Nombre, Tipo, Ataque, Habitat, Sub_Tipo):
        super().__init__(Nombre, Tipo, Ataque)
        self.Habitat = Habitat
        self.Sub_Tipo = Sub_Tipo

    def Desplegar(self):
        print (f'{self.Nombre} vive en {self.Habitat} y es de tipos {self.Tipo} / {self.Sub_Tipo}')

Objeto4 = Poke2('Gyarados', 'Agua', 'Aliento Dragon', 'Mares', 'Acero')

Objeto4.Desplegar()