#Todas las funciones de los dictionaries
cart = {
    "Nombre": "Luna de Pluton",
    "Precio": 10,
    "Cantidad": 1000000000,
    "Descripcion": "Mi libro luna de Pluton es un exito en Rituanda"
    }

print(dir(cart))
print(type(cart))

print(cart.keys())#Solo las llaves
print(cart.items())#Muestra los items 
cart.clear()
print(cart)
del cart

cart = {
    "First": {
        "Nombre": "Dell xps 13 9310",
        "Precio": 949.99,
        "cantidad": 1
    },
    "Second": {
        "Nombre": "Usb-c dongle",
        "Precio": 17.99,
        "Cantidad": 1
    },
    "Third": {
        "Nombre": "Laptop stand",
        "Precio": 10.99,
        "Cantidad": 1
    }
}

print(cart)