'''
Ejercicio 2
Crea una aplicación que permita adivinar un número. La aplicación genera un
número aleatorio del 1 al 100. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido,a
demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El
programa termina cuando se acierta el número (además te dice en cuantos
intentos lo has acertado), si se llega al limite de intentos te muestra el número
que había generado.
'''

import random

numero= random.randint(1,100)
num= 0
contador
while (num!= numero):
    num= (int)(input("Dime un número"))
    if (num<numero):
        print("El número es mayor")
    else:
        print("El número es mayor")

print
