"""
Funciones definidas por el usuario 
"""

#simple 

def saludar():
    print("Hola , Python")

saludar()

# Con retorno 

def devolver_saludo():
    return "Hola, Python 2.0 "

saludo = devolver_saludo()
print(saludo)

#Con argumento



def saludo(nombre):
    print(f"Hola {nombre}, como estas ?")


saludo("David")


#Con argumentos

def suma(a,b):
    sum = a+b
    return a+b

a = 3
b = 4

print(suma(a,b))

def saludo_completo(saludo, nombre):
    bienvenida = print(F"{saludo}, {nombre}")
    return bienvenida

saludo = "Hello"
nombre = "David"

saludo_completo(saludo,nombre)

# Con argumentos predeterminados

def saludo_completo(saludo = "Holis ", nombre = "Juan"):
    bienvenida = print(F"{saludo}, {nombre}")
    return bienvenida



saludo_completo()



def saludo_completo(saludo = "Holis ", nombre = "Juan"):
    bienvenida = print(F"{saludo}, {nombre}")
    return bienvenida



saludo_completo(nombre = "Santiago" , saludo = "Hooola")

#Con argumentos y retorno 


def saludo_completo(saludo = "Holis ", nombre = "Juan"):
    
    return F"{saludo}, {nombre}"



print(saludo_completo(nombre = "Santiago" , saludo = "Hooola"))

# Con retorno de varios valores 

def multiple ():
    return "Hola" , "Python"

saludo , lenguaje = multiple()
print(saludo )
print(lenguaje)


#  Con un numero variable de argumentos 

def saludo_variable(*names):
    for name in names :
        print(f"Hola {name}")


saludo_variable("SANTI", "Andres", "Comunity")


#Con un numero variable de argumentos con palabra clave

def saludo_clavevariable(**names):
    for param, name in names.items() :
        print(f"{param} : {name} ")



saludo_clavevariable(
    Name= "Santi", 
    Lenguaje= "Python", 
    Company = "Nvidia", 
    Age= "36"
)

# Funciones  dentro de otras funciones 

def funcion_A():
    def funcion_B():
        print("Funcion Interna: Hola Python")
    funcion_B()

funcion_A()


# Funciones del lenguaje (built-in)

print(len("Hola"))  #Una funcion que escribe en la terminal , que dentro de ella tiene una funcion que cuenta la cantidad de letras dentro de la cadena de texto

print(type(32)) #imprime que tipo de variable hay 

print("Santi" .upper()) #Mayuscula

print("SANTI" .lower()) #Minuscula 

# Variables locales y globales 

global_variable = "Python" # Variable global

print(global_variable)

def hello_python():
    local_variable = "Olas" # Variable Local  dentro de la funcion 
    print(f"{local_variable} , {global_variable}")

# print(local_var) No se puede acceder 
hello_python()



## Reto 

def reto (palabra1,palabra2):
    contador = 0
    for i in range (1,101):
        
     if i % 3 == 0  and i % 5 == 0 :
        print(f" {i} = {palabra1}, {palabra2}")
     elif i % 3 == 0:
            print(f" {i} = {palabra1}")
     elif i % 5 == 0 :
        print(f" {i} = {palabra2}")
     else:
        print(i)
        contador += 1

    return contador 

print(reto("Fizz" , "Buzz"))