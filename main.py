import numpy as np
import matplotlib.pyplot as plt
import ODESolver as odes
import math

if __name__ == "__main__":

    # Set parameters and initial conditions
    t0 = 0.0
    tf = 4
    h = 0.1
    n = int(((tf - t0) / h ))
    y0 = np.array([1,1])
    # y0 = 1 # scalar case 

    obj = odes.ODESolver()

    #
    # Defining the ODE/system of ODEs which should be integrated
    
    # def fct(t, y): -math.sin(t)  #constant ODE

    # k = -1
    # label = "exponential growth"
    # def fct(t, y): 
    #    return k * y  # exponential growth

    # k, G = 1, 2
    # def fct(t, y): 
    #    return k * y * (G - y)

    g = -9.8
    label = "falling body"
    def fct(t, y): 
        return np.array([y[1], g])  
    
    # ODE y'' + y = 0
    # def fct(t, y):
    #    return np.array([y[1], -y[0]])

    #
    # Integrating the ODEs 
    time_array, result_euler_explicit = obj.euler_explicit(t0, y0, h, n, fct)
    time_array, result_midpointrule = obj.midpointrule(t0, y0, h, n, fct)
    time_array, result_heun = obj.heun(t0, y0, h, n, fct)
    time_array, result_rk4 = obj.ClassicalRK4(t0, y0, h, n, fct)

    #
    # Printing the solutions
    if label == "exponential growth":
        plt.plot(time_array, result_euler_explicit, label="expl Euler")
        plt.plot(time_array, result_midpointrule, label="Midpointrule")
        plt.plot(time_array, result_heun, label="Heun")
        plt.plot(time_array, result_rk4, label="RK4")
        # plt.plot(time_array, y_exact, label="Exact solution (exp)")
        
    if label == "falling body":
        plt.plot(time_array, result_euler_explicit, label=["height (expl Euler)", "velocity (expl Euler"])
        plt.plot(time_array, result_midpointrule, label=["height (Midpointrule)", "velocity (Midpointrule)"])
        plt.plot(time_array, result_heun, label=["height (Heun)", "velocity (Heun)"])
        plt.plot(time_array, result_rk4, label=["height (RK4)", "velocity (RK4)"])
        # plt.plot(time_array, y_exact, label="Exact solution (exp)")         
        # plt.plot(t, y_exact, label="Exact solution y'=-y")

    # print the figure
    # y_exact = np.zeros(n + 1, dtype = 'f')
    # for i in range(n + 1):
        # y_exact[i] = math.exp(-i * h)  #exact solution for y'=-y
        # y_exact.append(G * (1 / (1 + math.exp(-k * G * i * h) * (G / y0 - 1))))  # exact solution for y'=k*y*)G-y))

    plt.legend()
    plt.show()
