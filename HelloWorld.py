def Exception1(Elemento):
    try:
        Numerito = int(Elemento)
        return f'Tu numero es {Numerito}'
    except ValueError:
        return f'Error, necesito que ingreses un numero'

print (f'{Exception1(26)}')

def Exception2(Num1, Num2):
    try:
        Sum = Num1 + Num2
        return f'El resultado de la sumatoria es {Sum}'
    except TypeError:
        return f'Error, ambos elementos deben ser numeros'

print (f'{Exception2(12, "Hola")}')

def Exception3(Num1, Num2):
    try:
        Div = Num1 / Num2
        return f'El resultado de la division es {round(Div, 2)}'
    except ZeroDivisionError:
        return f'Error, el divisor no puede ser un cero'

print (f'{Exception3(12, 0)}')

Lista_Exception4 = list(['Erick', 'Josue', 'Karlita'])

def Exception4(Indice):
    try:
        print (f'El elemento en el indice {Indice} es {Lista_Exception4[Indice]}')
    except IndexError:
        print (f'Error, el indice esta fuera de rango')

Exception4(3)

Diccionario_Exception5 = dict({'Nombre' : "Karlita", 'Edad' : 6})

def Exception5(Llave):
    try:
        print (f'El elemento en la llave {Llave} es {Diccionario_Exception5[Llave]}')
    except KeyError:
        print (f'Error, la llave esta fuera de rango')

Exception5('Votante')

try:
    with open ('C:\\Repo\\HolaMundo.txt', 'w', encoding='UTF-8') as Docu:
        Documento_SobreEscribir = Docu.write(f'Durazno')
        Docu.close()
except FileNotFoundError:
    print (f'Error, el archivo no fue encontrado')

with open ('C:\\Repo\\HolaMundo.txt', encoding='UTF-8') as Docu:
    Documento_Linea = Docu.readline()
    print (f'{Documento_Linea}')
    Docu.close()