#Como funcionan las funciones

def function(x="guy"):#En caso que sea texto en blanco
    print("Hello " + x + "!")

name = input("Che dime tu nombre ")
function(name)
function()

def calculator(x, y):
    return x + y

z = calculator(1, 2)#La funcion se va a volver el numero tres
print(z)

def lineal_regrasion(x):
    return 10 + 3*x

x = 0

while x <= 10:
    print(lineal_regrasion(x), x)
    x += 1

#Funcion escrita en una sola linea

add = lambda x, y: x+y

z = add(10, 30)
print(z)