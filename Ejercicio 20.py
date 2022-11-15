'''Ejercicio 20
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad
de números primos que queremos mostrar.'''

def esPrimo(num):
    for i in range(2,num):
        if (num%i==0):
            return False
    return True
    

num= int(input("Dime un número: \n"))
num2= []

for i in range(1,num+1):
    if esPrimo(num)==True:
        num2.append(i)
    
print(num2)