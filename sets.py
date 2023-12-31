#Funciones de los sets
set = {"Rgb", "Yellow", "Purple"}

print(type(set))
print(dir(set))

print("Rgb" in set)#Busca el dato
set.add("Guy")

print(set)
set.remove("Purple")

print(set)

set.clear()
print(set)

del(set)