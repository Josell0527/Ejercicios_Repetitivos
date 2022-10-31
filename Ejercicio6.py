'''Escribir un programa que imprima todos los números pares entre dos números
que se le pidan al usuario.
'''
num1= 0
num2= 0

num1= (int)(input("Dime un número: \n"))
num2= (int)(input("Dime otro número: \n"))

for num in range (num1,num2):
    if (num%2==0):
        print(num)