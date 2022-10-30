'''
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ 
en caso contrario, el programa termina cuando se introduce un espacio.
'''

letra = (str)(input("Dime una letra: |pulsa espacio para salir| \n")).lower()
num = 0
while letra != " ":
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("Tu letra es una vocal")
    else:
        print("Tu letra no es una vocal")
    letra = (str)(input("Dime una letra: |pulsa espacio para salir| \n"))
print("*********")