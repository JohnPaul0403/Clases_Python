#como funcionan los loops

cart = ["Gaming laptop", "Keyboard", "Gaming mouse", "29 inch Monitor", "Laptop stand", "Ipad pro 11 inch", "Laptop carry bag", "Ipad Case"]
#Lo que podrias hacer para imprimir cada uno de estos elementos

print(cart[0])
print(cart[1])
print(cart[2])
print(cart[3])
print(cart[4])

#Otra opcion mas corta con el metodo While

x = 0

while x < len(cart):
    if cart[x] == "Gaming laptop":
        break
    print(cart[x])
    x += 1

#Otra forma mas efectiva con el bucle for

for n in cart:
    if n == "Keyboard":
        print("You need to buy a " + n)
        #break, termina el bucle
        continue#Omite la data que en esta parte del bucle
    print(n)

for n in range(1, 11):
    print(n)

for letter in "Gaming Laptop":
    print(letter)