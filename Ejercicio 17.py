'''Ejercicio 17
Una empresa les paga a sus empleados con base en las horas trabajadas en la
semana. Para esto, se registran los días que trabajó y las horas de cada día.
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y
además calcule cuánto pagó la empresa por los N empleados.'''

horas= 0
dias= 0
trabajadores= (int)(input("Dime el número de trabajadores que tiene la empresa: \n"))

for num in range(1,7):
    horas= int(input("Dime las horas trabajadas"))
    dias= int(input("Dime los días trabajados"))
    sueldo= trabajadores