import numpy as np
import matplotlib.pyplot as plt
import ODESolver as odes
#from Visualization import visualization_fct
import math

def visualization_fct(time_array, result_array, label): 
    """ Printing the solutions """
    plt.plot(time_array, result_array, label=label)
    plt.plot(time_array, result_array, label=label)
    plt.plot(time_array, result_array, label=label)
    plt.plot(time_array, result_array, label=label)
    
    plt.legend()
    plt.show()

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

    # g = -9.8
    # label = "falling body"
    # def fct(t, y): 
    #    return np.array([y[1], g])  
    
    # ODE y'' + y = 0
    label = "y'' + y = 0"
    def fct(t, y):
        return np.array([y[1], -y[0]])

    #
    # Integrating the ODEs 
    time_array, result_euler_explicit = obj.euler_explicit(t0, y0, h, n, fct)
    time_array, result_midpointrule = obj.midpointrule(t0, y0, h, n, fct)
    time_array, result_heun = obj.heun(t0, y0, h, n, fct)
    time_array, result_rk4 = obj.ClassicalRK4(t0, y0, h, n, fct)

    #
    # Printing the solutions
    visualization_fct( time_array, result_euler_explicit, label='expl Euler') 
    # !!!!evtl mit kwargs versuchen !!!!!!!
    # vis.visualization_fct( time_array, result_midpointrule, label="Midpointrule")
    # vis.visualization_fct( time_array, result_heun, label="Heun")
    # vis.visualization_fct( time_array, result_rk4, label="RK4")
    

  
    # print the figure
    # y_exact = np.zeros(n + 1, dtype = 'f')
    # for i in range(n + 1):
        # y_exact[i] = math.exp(-i * h)  #exact solution for y'=-y
        # y_exact.append(G * (1 / (1 + math.exp(-k * G * i * h) * (G / y0 - 1))))  # exact solution for y'=k*y*)G-y))

   

