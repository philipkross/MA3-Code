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
from statistics import mean 
from time import perf_counter as pc

# Exc1
def approximate_pi(n):
    # n is the number of points

    # Write your code here
    return

# Exc2, approximation
def sphere_volume(n, d): 
    # n is the number of points

    # d is the number of dimensions of the sphere 

    return 

#Exc2, real value
def hypersphere_exact(n, d):
    # n is the number of points

    # d is the number of dimensions of the sphere 
    return

#Exc3: numba version
def sphere_volume_numba(n:int, d:int)->float:
    # n is the number of points

    # d is the number of dimensions of the sphere
    #np is the number of processes
    return

#Exc4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n, d, np=10):
    # n is the number of points
    # d is the number of dimensions of the sphere
    # np is the number of processes
    return 
    
def main():
    # Exc1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

    # Exc2
    n = 100000
    d = 2
    sphere_volume(n, d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    n = 100000
    d = 11
    sphere_volume(n, d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    # Exc3
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"Exc3: Sequential time of {d} and {n}: {stop-start}")
    print("What is numba time?")

    # Exc4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"Exc4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    
    

if __name__ == '__main__':
	main()
