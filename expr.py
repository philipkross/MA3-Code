import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
import numpy as np
from statistics import mean 
from time import perf_counter as pc
from numba import njit





def sphere_volume(n, d): 
    points = np.random.uniform(-1, 1, (n, d))

    distances = [sum(x**2 for x in point) for point in points]

    inside = list(filter(lambda dist: dist < 1, distances))

    return len(inside) / n * 2**d

    

#Exc2, real value
def hypersphere_exact(n, d):

    approx = sphere_volume(n,d)
    exact = m.pi**(d/2) / m.gamma(d/2+1)
    print(approx-exact)

    
    return



@njit
def sphere_volume_numba(n:int, d:int)->float:
    points = np.random.uniform(-1, 1, (n, d))

    inside = 0

    for i in range(n):
        dist = 0.0

        for j in range(d):
            dist += points[i, j]**2

        if dist < 1:
            inside += 1

    return inside / n * 2**d

times = []
for i in range(3):
    start = pc()

    result = sphere_volume_numba(10**6, 11)

    end = pc()
    times.append(end-start)

print(times)