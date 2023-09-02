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
        
    def midpointrule( self, t0, y0, h, n, f):
        """
        Implementation of the midpoint rule algorithm (2nd order Runge-Kutta agorithm)
        """
        
        t = t0
        y = y0
        result = [(t,y)]
        
        for i in range(n):
            t += h
            y_tmp = y + 0.5 * h * f(t, y)
            y += h * f(t + 0.5 * h, y_tmp )
            result.append((t, y))
            
        return result        
        
        
    def heun(self, t0, y0, h, n, f):
        """
        Implementation of the heun algorithm (2nd order Runge-Kutta agorithm)
        """
        
        t = t0
        y = y0
        result = [(t,y)]
        
        for i in range(n):
            t += h
            y_tmp = y + h * f(t, y)
            y += 0.5 * h * (f(t, y) + f(t + h, y_tmp))
            result.append((t, y))
            
        return result            	
    	 
