import numpy as np
import matplotlib.pyplot as plt
import ODESolver as odes
import math

if __name__ == "__main__":
    t0 = 0.0
    y0 = 1
    h = 0.1
    n = 4
    dim = 2

    obj = odes.ODESolver()

    # Defining the ODE which should be integrated
    # def fct(t, y): -math.sin(t)  #constant ODE

    k = -1
    def fct(t, y): 
        return k * y  # exponential growth

    # k, G = 1, 2
    # def fct(t, y): return k * y * (G - y)

    # g = -9.8
    # v = 0.0
    # def fct(t, y): return np.array([y[1], -g])  

    time_array, result_euler_explicit = obj.euler_explicit(t0, y0, h, n, fct)
    #result_midpointrule = obj.midpointrule(t0, y0, h, n, fct)
    #result_heun = obj.heun(t0, y0, h, n, fct)
    #result_rk4 = obj.ClassicalRK4(t0, y0, h, n, fct)

    # print the figure
    y_exact = np.zeros(n + 1, dtype = 'f')
    for i in range(n + 1):
        y_exact[i] = math.exp(-i * h)  #exact solution for y'=-y
        # y_exact.append(G * (1 / (1 + math.exp(-k * G * i * h) * (G / y0 - 1))))  # exact solution for y'=k*y*)G-y))

    # plt.plot(t, y_heun, label="Heun method")
    plt.plot(time_array, result_euler_explicit, label="Euler explicit method")
    # plt.plot(t, y_midpointrule, label="Midpoint rule")
    # plt.plot(t, y_rk4, label="Classic RK4")
    plt.plot(time_array, y_exact, label="Exact solution (exp)")

    # plt.plot(t, y_exact, label="Exact solution y'=-y")
    plt.legend()
    plt.show()
