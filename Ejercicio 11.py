'''Ejercicio 11
Escribe un programa que diga si un número introducido por teclado es o no
primo. Un número primo es aquel que sólo es divisible entre él mismo y la
unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si
es divisible por algún otro número.'''

def esPrimo(num):
    for i in range(2,num):
        if (num%i==0):
            return False
    return True
    

num= int(input("Dime un número: \n"))

if esPrimo(num)== True :
    print("El número es Primo")
else:
    print("El número No es primo")