'''Ejercicio 15
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó
10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo
para determinar cuánto debe pagar mensualmente y el total de
lo que pagó después de los 20 meses.'''

producto= 10
contador = 0
num= 0
suma= 0

for num in range(0,20):
    contador= contador+1
    print("El", contador, "mes, paga:", producto, "€")
    producto*=2
    suma= suma+producto
print("Total:",suma, "€")
