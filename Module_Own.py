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
        return Segunda('Carmelo')

    return Tercera

@Primera
def Saludar2(Nombre = 'Juanita La Cubanita'):
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
        return Segunda(59)

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