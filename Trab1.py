from scipy.optimize import differential_evolution as de;
from math import sin

files = [
    "Caso_13geradores_econ_ponto_valvula.txt",
    "Caso_13geradores_econ_ponto_valvula2.txt",
    "Caso_40geradores_econ_ponto_valvula.txt"
]
generators = 0
potency = 0
p_min = []
p_max = []
a = []
b = [] 
c = []
d = []
e = []
f = []

def obj_func(p):
    summation = 0
    for i in range(0, len(p)):
        summation += a[i] * p[i] ** 2 + b[i] * p[i] + c[i] + abs(d[i] * sin(e[i] *(p_min[i] - p_max[i])))
    return summation

file = open(files[0], 'r')

with file as opened_file:
    try:
        number_of_generators = int(opened_file.readline())
        demanded_potency = int(opened_file.readline())
        for _ in range(0, number_of_generators):
            p_min.append(float(opened_file.readline()))
        for _ in range(0, number_of_generators):
            p_max.append(float(opened_file.readline()))
        for _ in range(0, number_of_generators):
            a.append(float(opened_file.readline()))
        for _ in range(0, number_of_generators):
            b.append(float(opened_file.readline()))
        for _ in range(0, number_of_generators):
            c.append(float(opened_file.readline()))
        for _ in range(0, number_of_generators):
            d.append(float(opened_file.readline()))
        for _ in range(0, number_of_generators):
            e.append(float(opened_file.readline()))
    finally:
        opened_file.close()

print(f)

