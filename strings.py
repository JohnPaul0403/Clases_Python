#Todas las funciones de los strings

my_str = "Hello world!"

#Dir nos da todas las funcionalidades del tipo de dato
print(dir(my_str))

print(len(my_str))#Nos devuelva la longitud de la cadena

print(my_str.upper())#Pone toda la cadena en mayusculas
print(my_str.lower())#Pone toda la en minusculas
print(my_str.swapcase())#Pone toda la cadena al inversa de minusculas y mayusculas
print(my_str.replace("Hello", "New").upper())#Reemplaza una parte del texto por otra
print(my_str.count("l"))

print(my_str.startswith("Hello"))#Sale true
print(my_str.endswith("world"))#Sale false

print(my_str.split())#Convierte cada palabra en un dato distinto
st = my_str.split()

print(st[0])

print(my_str.find("l"))#Buscador de letras o palabras, muestra la posicion de la letra

print(my_str.index("e"))#Nos devuelve la posicion de la cadena

print(my_str[4])#Devuelve solo la que esta en la posicion n

print(my_str[-1])#Empieza a la inversa

#formas de concatenar
name = "John"

print("My name is " + name)
print(f"My name is {name}")
print("My name is {0}".format(name))