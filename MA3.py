#!/usr/bin/env python3
""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
import numpy as np
from statistics import mean 
from time import perf_counter as pc
from numba import njit

# Exc1
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def approximate_pi(n):
    points = np.random.uniform(-1, 1, (n, 2))
    x = points[:, 0]
    y = points[:, 1]
    inside = x**2 + y**2 <= 1
    res = inside.sum()

    # Plot the generated points: inside red, outside blue
    plt.scatter(x[inside], y[inside], s=1, c="red")
    plt.scatter(x[~inside], y[~inside], s=1, c="blue")
    plt.axis("equal")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Monte Carlo approximation of pi")
    plt.savefig(f"pi_{n}.png")
    plt.close()

    pi = 4 * res / len(x)
    print(f"n = {n}, estimated pi = {pi}")
    return pi


# Exc2, approximation
def sphere_volume(n, d): 
    points = np.random.uniform(-1, 1, (n, d))

    distances = [sum(x**2 for x in point) for point in points]

    inside = list(filter(lambda dist: dist < 1, distances))

    return len(inside) / n * 2**d

    

#Exc2, real value
def hypersphere_exact(n, d):

    exact = m.pi**(d/2) / m.gamma(d/2+1)
    
    return exact

# Run times: [1.3506737910211086, 1.292310249991715, 1.287617375026457]

#Exc3: numba version
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

#Run times: [0.6266269580228254, 0.03469975001644343, 0.03460545896086842]

#Exc4: parallel code - parallelize actual computations by splitting data
import multiprocessing
import random


def count_inside(n, d=11):
    inside = 0

    for _ in range(n):
        point = [random.uniform(-1, 1) for _ in range(d)]

        if sum(x**2 for x in point) <= 1:
            inside += 1

    return inside


def sphere_volume_parallel(n, d, np=10):

    points_per_process = n // np

    p = [points_per_process] * np

    with multiprocessing.Pool(np) as ex:
        results = ex.starmap(count_inside, [(k, d) for k in p])

    points_inside = sum(results)

    return 2**d * points_inside / n
    
def main():
    # Exc1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

    # Exc2
    n = 100000
    d = 2
    print(f"Approximate volume of {d} dimentional sphere = {sphere_volume(n, d)}")
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    n = 100000
    d = 11
    print(f"Approximate volume of {d} dimentional sphere = {sphere_volume(n, d)}")
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    # Exc3
    n = 1000000
    d = 11
    for f in (sphere_volume, sphere_volume_numba):
        for call in range(1, 4):
            start = pc()
            f(n, d)
            stop = pc()
            print(f"Exc3: {f.__name__} call {call}, d={d}, n={n}: {stop-start}")

    # Exc4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"Exc4: Sequential time of {d} and {n}: {stop-start}")
    start = pc()
    sphere_volume_parallel(n, d)
    stop = pc()
    print(f"Exc4: Parallel time of {d} and {n}: {stop-start}")

    
    

if __name__ == '__main__':
	main()
