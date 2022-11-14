'''Ejercicio 17
Una empresa les paga a sus empleados con base en las horas trabajadas en la
semana. Para esto, se registran los días que trabajó y las horas de cada día.
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y
además calcule cuánto pagó la empresa por los N empleados.'''

horas= 0
trabajadores= (int)(input("Dime el número de trabajadores que tiene la empresa: \n"))
num= 0
semanas=4
horastotal= 0
sueldosemanal= 0
gastototal= 0
eurohora= (int)(input("Dime el salario de la hora: \n"))

for tra in range (1,trabajadores+1):
    dias= int(input(f"Dime los días trabajados del empleado {tra}: \n"))
    horastotal= 0
    for num in range (1,dias+1):
        horastrabajadas= int(input(f"Dime las horas trabajadas el día {num}: \n"))
        horastotal += horastrabajadas


    sueldosemanal = horastotal*eurohora
    gastototal += sueldosemanal

print("Total semana:", sueldosemanal)
print("Total de todos los trabajadores:", (gastototal))
