def Excepcion1(Num):
    Numero = Num
    try:
        Numerito = int(Numero)
        print (f'Gracias, tu numerito es {Numerito}')
    except ValueError:
        print (f'Error, necesito que ingreses un numero par')

Excepcion1("Hola")

def Excepcion2(Num1, Num2):
    try:
        Resultado = Num1 + Num2
        return f'El resultado de la sumatoria es {Resultado}'
    except TypeError:
        return f'Error, ambos elementos deben ser numeros'

print (f'{Excepcion2(12, "Hola")}')

def Excepcion3(Num1, Num2):
    try:
        Divi = Num1 / Num2
        return f'El resultado de la division es {Divi}'
    except ZeroDivisionError:
        return f'Error, el divisor no puede ser un cero'

print (f'{Excepcion3(12, 0)}')

Lista_Excepcion4 = list(['Erick', 'Josue', 'Karlita'])

def Excepcion4(Indice):
    try:
        print (f'El elemento en la posicion {Indice} es {Lista_Excepcion4[Indice]}')
    except IndexError:
        print (f'El indice elegido esta fuera de rango')

Excepcion4(3)

Diccionario_Excepcion5 = dict({'Nombre' : "Erick", 'Edad' : 37, 'Votante' : True})

def Excepcion5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Excepcion5[Llave]}')
    except KeyError:
        print (f'Error, la llave seleccionada esta fuera de rango')

Excepcion5('Hola')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Hiena')
        Docu.close()
except FileNotFoundError:
    print (f'El archivo seleccionado no existe')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()

try:
    import Module_Own as PEPE
except ImportError:
    print (f'Error, el modulo seleccionado no existe')