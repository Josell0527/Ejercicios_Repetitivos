'''
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el
límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:
- La suma de los números que están dentro del intervalo (intervalo abierto).
- Cuantos números están fuera del intervalo.
- He informa si hemos introducido algún número igual a los límites del intervalo.
'''
inferior= 0
superior= 0
inferior= (int)(input("Dime el intervalo inferior: \n"))
superior= (int)(input("Dime el intervalo superior: \n"))

while inferior>superior:
     inferior= (int)(input("Dime el intervalo inferior: \n"))

num= (int)(input("Dime un número \n"))
while (num!=0):
    num= 1
    vNumeros=[]
    vNumeros.append(num)
    num= (int)(input("Dime un número \n"))

for Vnumeros in range(inferior, superior):
     print(vNumeros)
