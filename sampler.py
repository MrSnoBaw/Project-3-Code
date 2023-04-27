import numpy as np
from random import random
from math import sqrt

def sierpinski_triangle_sample(n: int):
    sqrt3 = sqrt(3)
    x, y = np.zeros(n), np.zeros(n)
  
    for ind in range(n):
        r1, r2 = random(), random()
        while r1 + r2 > 1: 
            # r1, r2 = 1 - r1, 1 - r2
            r1, r2 = random(), random()
        ptx, pty = r1 + r2 / 2, r2 * sqrt3 / 2
        
        if ind%100000 == 0: print(f"Sampling triangle {round(100 * ind/n, 2)}%")
        
        for _ in range(100):
            r = 3.0 * random()
            ptx /= 2; pty /= 2

            if   r < 1.0:   continue
            elif r < 2.0:   ptx += 0.5
            else:           ptx += 0.25; pty += sqrt3 * 0.25

        x[ind] = ptx
        y[ind] = pty
    return np.vstack((x, y)).T

def sierpinski_carpet_sample(n: int):
    x, y = np.zeros(n), np.zeros(n)
    delta_x = np.array([0.0, 1.0, 2.0, 2.0, 2.0, 1.0, 0.0, 0.0]) / 3
    delta_y = np.array([0.0, 0.0, 0.0, 1.0, 2.0, 2.0, 2.0, 1.0]) / 3

    for i in range(n):
        ptx, pty = random(), random()
        
        if i%100000 == 0: print(f"Sampling sponge {round(100 * i/n, 2)}%")
        
        for _ in range(100):
            r = int(8.0 * random()) # A value in 0, 1, 2, ..., 7 inclusive
            ptx /= 3; pty /= 3
            ptx += delta_x[r]
            pty += delta_y[r]
        x[i] = ptx
        y[i] = pty
    return np.vstack((x, y)).T

def cantor_interval_sample(n: int): 
    x, y = np.zeros(n), np.array([random() for _ in range(n)])
    threp = 1
    for i in range(n):

        if i%100000 == 0: print(f"Sampling Cantor {round(100 * i/n, 2)}%")
        
        pt = 0
        threp = 1
        for j in range(100):
            threp /= 3
            if random() > 0.5:
                pt += 2 * threp
        x[i] = pt
    return np.vstack((x, y)).T

def dragon_sample(n: int):
    x, y = np.zeros(n), np.zeros(n)
    for i in range(n):

        if i%100000 == 0: print(f"Sampling dragon {round(100 * i/n, 2)}%")

        ptx, pty = int(2*random()), 0
        for _ in range(65):
            if random() > 0.5:
                ptx, pty = 0.5*(ptx - pty), 0.5*(ptx + pty)
            else:
                ptx, pty = -0.5*(ptx + pty) + 1, 0.5*(ptx - pty)
        x[i] = ptx
        y[i] = pty
    return np.vstack((x, y)).T

def square_sample(n: int):
    x, y = np.zeros(n), np.zeros(n)
    for i in range(n):

        if i%100000 == 0: print(f"Sampling square {round(100 * i/n, 2)}%")
        
        x[i] = random()
        y[i] = random()
    return np.vstack((x, y)).T

def circle_sample(n: int):
    x, y = np.zeros(n), np.zeros(n)
    for i in range(n):

        if i%100000 == 0: print(f"Sampling square {round(100 * i/n, 2)}%")
        
        a, b = random(), random()
        while a*a + b*b > 1:
            a, b = random(), random()
        x[i] = a
        y[i] = b
    return np.vstack((x, y)).T
