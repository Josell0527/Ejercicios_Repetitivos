'''
Realizar una algoritmo que muestre la tabla de multiplicar de un número
introducido por teclado
'''
print("Tabla de Multiplicar")
num= (int)(input("Dime un número: \n"))

for numero in range (0,11):
    print (num*numero)
