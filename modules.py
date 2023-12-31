#Como utilizar y maximizar el uso de modulos
import datetime 
from datetime import timedelta, date
import math_module #o
from math_module import lineal_regrasion
from colorama import Fore, Style

print(datetime.date.today())
print(datetime.timedelta(minutes=90))

#Otra opcion de importar


print(timedelta(minutes=123.4))
print(Fore.RED + str(date.today()))

print(math_module.lineal_regrasion(10))
print(lineal_regrasion(1))