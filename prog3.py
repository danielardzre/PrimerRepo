#Escribir un programa que muestre al usuario el siguiente menu: 
#Operaciones; S=Suma, R=Resta, M=Multiplicacion,D=Division,A=Salir.

menu= True

while menu == True:
    print("""
    MENU:
    S: Suma
    R: Resta
    M: Multiplicacion
    D: Division
    A: Salir""")
    opcion= input("Bienvenido a mi programa, seleccione una opcion del menu:\n")    
    

    if opcion.upper()== "S":
        num1= int(input("Escribe un numero:\n"))
        num2= int(input("Escribe otro numero:\n"))
        resul= num1 + num2
        print(f'El resultado de la operacion es {resul}')

    elif opcion.upper()== "R":
        num1= int(input("Escribe un numero:\n"))
        num2= int(input("Escribe otro numero:\n"))
        resul= num1 - num2
        print(f'El resultado de la operacion es {resul}')

    elif opcion.upper()== "M":
        num1= int(input("Escribe un numero:\n"))
        num2= int(input("Escribe otro numero:\n"))
        resul= num1 * num2
        print(f'El resultado de la operacion es {resul}')

    elif opcion.upper()== "D":
        num1= int(input("Escribe un numero:\n"))
        num2= int(input("Escribe otro numero:\n"))
        resul= num1 / num2
        print(f'El resultado de la operacion es {resul}')

    elif opcion.upper()=="A":
        menu = False
        print("Gracias por usar el programa.")          

    else:
        print ("Ingrese una opcion valida contenida en el menu")





