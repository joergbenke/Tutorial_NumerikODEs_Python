import matplotlib.pyplot as plt 
import ODESolver as odes
import math
	
if __name__ == "__main__":
    t0 = 0
    y0 = 0
    h = 0.1
    n = 10
    
    obj = odes.ODESolver()
    result = obj.euler_explicit(t0, y0, h, n, lambda t, y:-math.sin(t))
    print(result)	
    
    # print the graphic
    
