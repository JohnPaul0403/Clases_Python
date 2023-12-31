#Todas las funciones de los arreglos

cosas = [10,"Hello", 10.0, [10, 23]]
colors = ["Red", "Green", "Blue"]

print(dir(colors))
print(colors.sort(reverse=True))

#funciones de las listas

nums = list(colors)
print(nums)

nums = list({10,20,30})#La tupla crea una lista como si fuera un solo elemento
print(nums)
print(type(nums))

list = list(range(1, 10))
print(list)

print(len(list))

number = [3,2,5,1,3,5]

print(number[2])
print(5 in number)#Busca un dato

number[2] = 4
print(number)

number.append(7)
number.extend({20,34})
number.insert(1, 20)
number.insert(len(number), 32)
number.pop()
number.remove(5)
number.pop(0)
number.sort()
print(number)

print(number.index(20))
print(number.count(20))

number.clear()
print(number)
