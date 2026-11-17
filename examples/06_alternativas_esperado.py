import math

n = 0
n = int(input())
if n > 0:
    print('Positivo', sep='', end='\n')
else:
    if n < 0:
        print('Negativo', sep='', end='\n')
    else:
        print('Cero', sep='', end='\n')
