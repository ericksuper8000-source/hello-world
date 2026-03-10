import re

Nombre = input(f'Ingrese su nombre: ')

Pattern1 = r'[a-zA-Z]+'

Buscar1 = bool(re.match(Pattern1, Nombre))

if (Buscar1 == True):
    print (f'Hola {Nombre}!')
    print (f'El tipo de dato es - {type(Nombre)}')
else:
    print (f'Error, su nombre solo puede llevar texto')

Edad = input(f'Ingrese su edad: ')

Pattern2 = r'^\d+'

Buscar2 = bool(re.match(Pattern2, Edad))

if (Buscar2 == True):
    if (int(Edad) > 105):
        print (f'Puede que haya digitado una edad falsa')
    else:
        print (f'Tienes {int(Edad)} años')
        print(f'El tipo de dato es - {type(int(Edad))}')
else:
    print (f'Error, necesito que ingrese un numero')

Pais = input(f'Ingrese su pais de procedencia: ')

Buscar3 = bool(re.match(Pattern1, Pais))

if (Buscar3 == True):
    print (f'Vives en {Pais}')
    print(f'El tipo de dato es - {type(Pais)}')
else:
    print (f'Error, necesito que ingrese una cadena de texto')

Altura = input(f'Ingrese su altura con formato 1.72: ')

Pattern3 = r'^[0-2]?\.\d{2}$'

Buscar4 = bool(re.match(Pattern3, Altura))

if (Buscar4 == True):
    print (f'Mides {float(Altura)} metros')
    print(f'El tipo de dato es - {type(float(Altura))}')
else:
    print (f'Formato de altura incorrecto, debe ser x.xx')

