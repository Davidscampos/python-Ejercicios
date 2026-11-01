import os
"""Listas donde se pueden guardar diferentes tipos de datos recuerda que una lista se conoce por 
empezar con [ y terminar con ] """

print("Lista Original ")
my_list = ["David",2,True,"Avion",1.23]
print(my_list)
print("\n Lista con insercion  ")
my_list.append("Jose") #Inserción
my_list.append(12)
print(my_list)

print("\n Lista con Eliminación  ")

my_list.remove(True) # Eliminación 
my_list.remove(1.23)
print(my_list)


print("\n Lista con Actualización ")

my_list[0] = "Santiago"
# my_list[5] = 12  No se puede porque supera el # de elementos que hay 
my_list[4] = 21
print(my_list)

print("\n Actualizacion con for ")
for i in range(len(my_list)):
    my_list[i]= i
print(my_list)

print("\n Lista con Ordenación")

my_list=[32,21,45,1,23,4,1,87]
my_list2 = ["Hola", "Beca", "Fenomeno","Petro","Libera","Astro"]
my_list.sort() # Ordena de menor a mayor 
my_list2.sort() # Ordena de la A a la z
print(my_list)
print(my_list2)

# Tuplas son inmutables 
print("\n Tuplas ")
my_tupla = ("David","Campos","19","@gmail")
print(my_tupla[1]) #Acceso
print(my_tupla[3])
my_tupla= sorted(my_tupla)  #Nos devuelve una lista, pero todos los datos de la tupla deben ser del mismo tipo
print(type(my_tupla))

my_tupla= tuple(sorted(my_tupla))  #Se ordena porque se vuelve una lista con el sorted y luego vuelve a ser una tupla
print(my_tupla)
print(type(my_tupla))

#Sets es una estructura desordenada, no es buena para buscar datos 
print("\n Sets ")
my_set = {"David","Campos","19","@gmail"}
print(my_set)

print("\n Set Actualizado ")
my_set.add("santi@gmail.com") #Insercion 
# print(my_set[2]) No se puede imprimir ya que es una estructura desordenada
print(my_set)
my_set.add("santi@gmail.com") 
print(my_set) #Evita duplicados 

my_set.remove("19") # Elimina
print(my_set)
my_set =set(sorted(my_set)) # No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario 
print("\n Diccionarios ")

diccionario : dict ={"Name":"David", "Apellido": "Campos","Edad": "19","Correo": "@gmail"}
print(type(diccionario))
 
print(diccionario["Correo"]) #Acceso

diccionario["Email"] = "david.email@com" #Insercion
print(diccionario) 

diccionario["Edad"] = "37" #Actualizacion
print(diccionario) 

del diccionario["Apellido"] #Eliminacion
print(diccionario)

"""diccionario1 = sorted(diccionario)
print(diccionario1)
print(type(diccionario1))"""

diccionario = dict(sorted(diccionario.items())) # Ordenacion
print(diccionario)
print(type(diccionario))

## Reto Extra 
Agenda = {"Maria" : 31203065715 , "Heri" : 3212127541 , "Joshua" : 3001254290}
print("############### - Menú - ################# ")

while True: 
 
 print("\n1. Actualizar  ")
 print("2. Insertar")
 print("3. Eliminar ")
 print("4. Ver la agenda de contactos ")
 print("5. Salir del programa \n")

 opcion = int(input("Que quieres hacer? : "))


 if opcion == 1 : 
     print(Agenda)
     x = input("Que contacto vas a actualizar? (Escribe su nombre) :")
     n = int(input("Escribe el numero actualizado : "))
     Agenda[x] = n
     print(f"Agenda actualizada :  {Agenda}")
 elif opcion == 2 : 
        x =  input("Nombre del nuevo contacto : ")
        n = int(input("Numero de telefono del contacto : "))
        while len(n) >= 11:
             print("Numero invalido , escribelo de nuevo ")
             n = int(input("Numero de telefono del contacto : "))
        Agenda[x] = n
        print(f"Agenda actualizada :  {Agenda}")
 elif opcion == 3 :
      print(Agenda)
      x =  input("Nombre del contacto que vas a eliminar  : ")
      del Agenda[x] 
      print(f"Agenda actualizada :  {Agenda}")
 elif opcion == 4:
      print(f"Agenda de contactos : {Agenda}")
 elif opcion == 5:
      print("Saliendo del programa .....")
      break

 else:
        print("\n❌ Opción incorrecta. Intenta de nuevo.")
        input("\nPresiona Enter para continuar...")    



## Reto guiado 

def my_agenda ():

 Agenda= {}

 def insert_contact():
  phone = input("Escribe numero de telefono : ")
  if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
               Agenda[name] = phone 
  else :
             print(f"EL contacto {name} no existe: ")
 
 while True: 

    print("")
    print("\n1. Buscar ")
    print("2. Insertar")
    print("3. Actaulizar ")
    print("4. Eliminar")
    print("5. Salir del programa \n")

    opcion = int(input("Que quieres hacer? : "))

    match opcion:
         case 1 :
            name = input("A quien buscas ? : ")

            if name in Agenda:
                print(f"El numero de tu contacto {name} es : {Agenda[name]}")

            else:
                print(f"EL contacto {name} no existe: ")
            pass
         case 2 :

            name = input("Con que nombre lo guardaras ? : ")
            insert_contact()
            pass

         case 3 :
            x =  input("Nombre del contacto que vas a actualizar  : ")
            if x in Agenda:  
                insert_contact()      
            pass
         case 4 :
            x =  input("Nombre del contacto que vas a eliminar  : ")
            if x in Agenda:
             del Agenda[x] 
            else :
                print(f"EL contacto {name} no existe: ")
            pass
         case 5 :
              print("Saliendo del programa ....")
              break
         case _: 
              print("\n❌ Opción incorrecta. Intenta de nuevo.")
              input("\nPresiona Enter para continuar...")    
                    
            
my_agenda()