#Escribir un programa que solicite al usuario dos numeros enteros y calcular la suma desde el numero 1 hasta
#el numero 2. Imprimir el resultado de la suma.

num1 = int(input("Dame un numero:\n"))
num2 = int(input("Dame otro numero:\n"))

suma = 0

for num in range (num1,num2+1):
    suma = suma + num

print (suma)
    