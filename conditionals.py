#Como funcionan y sus funciones de las condicionales

x = int(input("Che desime tu edad loco "))

if x < 30:
    print(str(x) + " es menor a 30")
elif x == 30:
    print(str(x) + " es igual a 30")
else:
    print(str(x) + " es mayor a 30")

first_name = "John"
last_name = "Carter"

if first_name == "John" and last_name == "Carter":
    print("Bienvenido " + first_name + " " + last_name)
else:
    print("Fuera de aqui")

#En de la siguiente forma se puede utilizar para casos mas especificos

if first_name == "John":
    if last_name == "Carter":
        print("Bienvenido John Carter")
    else:
        print("John tu no eres John Carter")
else:
    print("Fuera de aqui")

edad = int(input("Decime tu edad "))

if edad <= 18 or edad >= 65:
    print("Pasajero priveligiado")
else: 
    print("Pasajero normal")