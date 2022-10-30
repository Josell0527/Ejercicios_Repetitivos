'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0
'''
num = []
menor = 0
mayor = 0
igual = 0 
cant = (int)("Cantidad de números que vas a introducir:\n")

for i in range(1,cant):
    numero = (int)(input("Dime un número:\n"))
    num.append(numero)

for i in num:
    if i==0:
        igual+=1
    elif i<0:
        menor+=1
    elif i>0:
        mayor+=1

print("numeros mayores que 0:",mayor, "iguales que 0:",  igual, "menores de 0", menor)
    