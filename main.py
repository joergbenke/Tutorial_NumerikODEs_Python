import matplotlib.pyplot as plt 
import ODESolver as odes
import math
	
if __name__ == "__main__":
    t0 = 0
    y0 = 1
    h = 0.1
    n = 40
    
    obj = odes.ODESolver()
    result_euler_explicit = obj.euler_explicit(t0, y0, h, n, lambda t, y:-math.sin(t))
    result_midpointrule = obj.midpointrule(t0, y0, h, n, lambda t, y:-math.sin(t))
    result_heun = obj.heun(t0, y0, h, n, lambda t, y:-math.sin(t))
    
    
    # print the graphic
    t = []
    y_heun = []
    y_euler_explicit = []
    y_midpointrule = []
    y_exact = []
   
    for i in range(n):
        t.append(result_heun[i][0])
        y_euler_explicit.append(result_euler_explicit[i][1])
        y_midpointrule.append(result_midpointrule[i][1])
        y_heun.append(result_heun[i][1])
        y_exact.append(math.cos(i * h))
        	    
    plt.plot(t, y_heun, label="Heun method")
    plt.plot(t, y_euler_explicit, label="Euler explicit method")    
    plt.plot(t, y_midpointrule, label="Midpoint rule")    
    plt.plot(t, y_exact, label="Exact cos")
    plt.legend()

    plt.show()
        
         
         
    
