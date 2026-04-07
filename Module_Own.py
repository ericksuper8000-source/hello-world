Diccionario_Poke = dict.fromkeys(['Poke1', 'Poke2', 'Poke3'])

Set_Conjunto_Poke = set({'Pikachu'})
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

class Pokemon():
    def __init__(self, Nombre, Tipo, Ataque):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Ataque = Ataque

    def Mostrar(self):
        print (f'Nombre: {self.Nombre}')
        print (f'Tipo: {self.Tipo}')
        print (f'Ataque: {self.Ataque}')

def Primera(Segunda):
    def Tercera():
        print (f'ANTES************')
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
def Saludar2(Nombre = 'Juana La Cubana'):
    return Nombre

def Saludar3(Nombre:str) -> str:
    return Nombre

def Primera(Segunda):
    def Tercera(*args, **kwargs):
        return Segunda(*args, **kwargs) + 1

    return Tercera

@Primera
def Sumatoria1(Num1, Num2):
    return Num1 + Num2

def Primera(Segunda):
    def Tercera(*args):
        return Segunda(2)

    return Tercera

@Primera
def Par(Num):
    if (Num % 2 == 0):
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
        print (f'{Nombre}, eres una mujer')