"""
Operadores 

"""

#Operadores aritmeticos 

print(f"suma 10 + 3 : {10+3} ")
print(f"Resta 10 - 3 : {10-3}")
print(f"Multiplicacion  10 * 3: {10*3}")
print(f"Division 10 / 3: {10/3}")
print(f"Modulo 10 % 3 : {10%3}")
print(f"Exponenet 10 ** 3 : {10**3}")
print(f"Divison entera 10//3 : {10//3}")

#Operadores de comparacion
print(f"Igualdad: 10 == 3 es {10==3}")
print(f"Desigualdad: 10 != 3 es {10!=3}")
print(f"Mayor que : 10 > 3 es {10 > 3}")
print(f"Menor que : 10 < 3 es {10<3}")
print(f"Mayor o igual que : 10 >= 10 es {10 >= 3}")
print(f"Menor o igual que : 10 <= 5 es {10<= 3}")

#Operadores lógicos

print(f"AND &&: 10 + 3 == 13 and  5 -1 == 4 es : {10 + 3 == 13 and  5 -1 == 4 } ")
print(f"OR ||: 10 + 3 == 13 or  5 -1 == 4 es : {10 + 3 == 12 or  5 -1 == 4 } ")
print(f"NOT !: not 10 + 3 = es : {not 10 + 3 == 13} ")

#Operadores de asignación 

my_number = 11 
print(my_number) # Asignacion
my_number += 1 
print(my_number) # Asignacion y suma 
my_number -= 1 
print(my_number) # Asignacion y Resta
my_number *= 2
print(my_number) # Asignacion y Multiplicacion
my_number /= 2
print(my_number) # Asignacion y Division
my_number %= 2
print(my_number)

# Operadores de identidad
my_new_number = my_number

print(f"my_number is my_new_number es : {my_number is my_new_number}")
print(f"my_number is not my_new_number es : {my_number is not my_new_number}")

#Operadores de pertenecia

print(f"'a' in brais : {'a' in 'brais'} ")
print(f"'b' not in brais : {'a' in 'brais'} ")

#Operadores de bit 
a = 10 # 1010
b = 3 # 0011
print(f"AND : 10 & 3 = {10 & 3} ") #0010
print(f"OR : 10 | 3 = {10  | 3} ") #1011
print(f"XOR : 10 ^ 3 = {10 ^ 3} ") #1001
print(f"NOT : 10 ^ 3 = {~3} ") #1100
print(f"Dezplazamiento a la derecha 10 >> 2 =  {10 >> 2} ") #0010
print(f"Dezplazamiento a la Izquierda 10 << 2 =  {10 << 2} ") #101000

"""
 Estructuras de control
"""

#Condicional

nombre = "david"

if nombre == "david":
    print("nombre es 'david'")
elif nombre == "Juan":
    print("nombre es Juan")
else:
    print("el nombre no es david")

#Iterativas 

for i in range(1,11):
    print(i)

i = 0 

while  i <= 10:
    print( "Valor ",i)
    i += 1

#Manejo de expeciones
try: #Intenta esto
    print(10/0)
except ZeroDivisionError: #Si pasa esto haz esto
    print("Se ha producido un Error")
finally: # Ultima instruccion siempre que se produzca o no el error
    print("Ha finalizado el manejo de excepciones")


# Reto

for i in range (10,56):
    if i % 2 == 0 and i != 16 and (i % 3 != 0):
        print(f"Numero : {i}")



   