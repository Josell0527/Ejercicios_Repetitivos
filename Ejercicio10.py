'''Ejercicio 10. Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.'''

def multiplicar():
    num= 0
    i= 0
    while (i<=10):
            print(num, "*", i, "=", num*i )
            i= i+1

for i in range(1,5+1):
    print (multiplicar)