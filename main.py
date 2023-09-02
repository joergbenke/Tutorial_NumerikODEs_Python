import matplotlib.pyplot as plt 
import ODESolver as odes
import math
	
if __name__ == "__main__":
    t0 = 0
    y0 = 1
    h = 0.4
    n = 10
    
    obj = odes.ODESolver()
    result = obj.euler_explicit(t0, y0, h, n, lambda t, y:-math.sin(t))
    print(result)	
    
    # print the graphic
    t = []
    y = []
    z = []
   
    for i in range(n):
        t.append(result[i][0])
        y.append(result[i][1])
        z.append(math.cos(i * h))
        	    
    plt.plot(t, y)    
    plt.plot(t, z)
    plt.show()
        
         
    
