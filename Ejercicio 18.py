'''Ejercicio 18
Hacer un programa que muestre un cronometro, indicando las horas, minutos y
segundos.'''
import time 
horas = 0
minutos = 0
segundos= 0
for hora in range (0,24):
    for min in range (0,60):
        for seg in range (0,60):
            print(f"{hora}:{min}:{seg}")
            for i in range (0,7):
                print()
            time.sleep(1)