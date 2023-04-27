import numpy as np
from random import random
from math import cos, sin, sqrt, pi

def sierpinski_triangle_sample(n: int):
    sqrt3 = 3 ** 0.5
    x, y = np.zeros(n), np.zeros(n)
  
    for ind in range(n):
        r1, r2 = random(), random()
        if r1 + r2 > 1: 
            r1, r2 = 1 - r1, 1 - r2
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
    a_third = 1/3
    delta_x = np.array([0.0, 1.0, 2.0, 2.0, 2.0, 1.0, 0.0, 0.0]) * a_third
    delta_y = np.array([0.0, 0.0, 0.0, 1.0, 2.0, 2.0, 2.0, 1.0]) * a_third

    for i in range(n):
        ptx, pty = random(), random()
        
        if i%100000 == 0: print(f"Sampling sponge {round(100 * i/n, 2)}%")
        
        for _ in range(100):
            r = int(8.0 * random()) # A value in 0, 1, 2, ..., 7 inclusive
            ptx *= a_third; pty *= a_third

            ptx += delta_x[r]
            pty += delta_y[r]
        x[i] = ptx
        y[i] = pty
    return np.vstack((x, y)).T


# def henon_sample(n: int, a = 1.4, b = 0.3):
#     ptx, pty = 0, 0
#     x, y = np.zeros(n + 1), np.zeros(n + 1)
#     x[0],y[0] = ptx, pty 
#     for i in range(1, n + 1):
#         ptx, pty = 1 - a * ptx * ptx + pty, b * ptx
#         x[i], y[i] = ptx, pty
#     return x, y

# def ikeda_sample(n: int, a = 1.4, b = 0.3):
#     ptx, pty, u = 10*random(), 10*random(), 0.6 + 0.4 * random()
#     print(u)
#     x, y = np.zeros(n + 1), np.zeros(n + 1)
#     x[0],y[0] = ptx, pty 
#     for i in range(1, n + 1):
#         t = 0.4 - 6/(1 + ptx*ptx + pty*pty)
#         ptx, pty = 1 + u*(ptx * cos(t) - pty * sin(t)) , u * (ptx * sin(t) + pty * cos(t))
#         x[i], y[i] = ptx, pty
#     return x, y

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

def dragon_plot(n: int):
    from matplotlib.pyplot import plot, show
    lines = [np.array([complex(0, 0), complex(1, 0)])]
    for _ in range(n):
        newlines = []
        for line in lines:
            newlines.append((0.5 + complex(0, 0.5)) * line)
            newlines.append(1 + (-0.5 + complex(0, 0.5)) * line)
        lines = newlines
        for line in lines:
            plot(line.real, line.imag, color = "black")
        show()

def dragon_sample(n: int):
    pts = np.zeros(n + 1, dtype=complex)
    for i in range(n):
        if i%100000 == 0: print(f"Sampling dragon {round(100 * i/n, 2)}%")
        pt = complex(random(), 0)
        for _ in range(300):
            if random() > 0.5:
                pt = (0.5 + complex(0, 0.5)) * pt
            else:
                pt = 1 + (-0.5 + complex(0, 0.5)) * pt
        pts[i] = pt
    return np.vstack((pts.real, pts.imag)).T

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
        r = sqrt(random())
        theta = random() * 2 * pi
        x[i] = r * cos(theta)
        y[i] = r * sin(theta)
    return np.vstack((x, y)).T