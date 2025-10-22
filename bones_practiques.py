#!/usr/bin/env python
'''bones_practiques.py. Calcula el residuo i el quocient d'una divisio

Institut Icària

Programació - 1r Batxillerat - Curs 2025-26

El programa dona per entrada el residuo i el quocient d'una divisio, escriu la divisio,
el quocient i el residuo, dona els resultats en innt
'''
__author__ = "Valentí Bernet"
__email__ = "vbernet@instituticaria.cat"
__date__ = "2025/10/22"


dividendo = int(input("Dime el dividendo: "))
divisor = int(input("Entra el divisor: "))

cociente = dividendo // divisor
residuo = dividendo % divisor

print(f"Divisió: {dividendo}/{divisor}")
print(f"Quocient: {cociente}")
print(f"Residu: {residuo}")
