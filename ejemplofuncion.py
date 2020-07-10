#Escribir un programa que pida al usuario un texto y un numero entero, mandar a imprimir en pantalla el texto 
#repetido el numero de veces indicado por el numero. Nota: Hacer el programa usando una funcion


#Declarar funcion

def repetidor(texto,num):
    texto+="\n"
    print(texto*num)

#Codigo

texto = input("Escribe un texto:\n")
num = int(input("Ingresa un numero:\n"))

repetidor(texto,num)
