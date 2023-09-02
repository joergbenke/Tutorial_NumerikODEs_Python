import numpy as np

class ODESolver:
    def euler_explicit(self, t0, y0, h, n, f):
        """
        Implementation of the explicit euler algorithm
        """
        
        t = t0
        y = y0
        result = [(t,y)]
    	
        for i in range(n):
            t += h		
            y += h * f(t,y)
            result.append((t, y))	
    	
        return result    	
    	 
