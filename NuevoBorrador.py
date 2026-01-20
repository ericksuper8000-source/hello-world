def Saludar1():
    print (f'Hola Mundo')

Saludar1()

def Saludar2(Nombre = 'Juanita'):
    return Nombre

print (f'Hola {Saludar2()}')

def Saludar3(Nombre:str) -> str:
    return Nombre

print (f'Hola nuevamente {Saludar3(Saludar2())}')