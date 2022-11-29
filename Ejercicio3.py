'''
Ejercicio 3. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos
'''
contador= 0
suma= 0
num= (int)(input("Dime un número: \n"))
while (num!=0):
    contador= contador+1
    suma= suma+num
    num= (int)(input("Dime un número: \n"))
print("La suma total es:", suma, "y la media", (suma/contador))

#Muy bien!