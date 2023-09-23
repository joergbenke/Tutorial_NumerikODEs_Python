import numpy as np

class ODESolver:
    def euler_explicit(self, t0, y0, h, n, f):
        """
        Implementation of the explicit euler algorithm
        """
        t = np.zeros(n + 1, dtype='f')
        neq = 1
               
        if isinstance(y0, (int, float)):
            y = np.zeros(n + 1, dtype='f')
            y[0] = y0
        else:
            neq = len(y0)
            y = np.zeros((n + 1, neq), dtype='f')
            y[0,:] = y0
                
        t[0] = t0
        if neq > 1:
            for k in range(n):
                t[k + 1] = t[k] + h
                y[k + 1, :] = y[k, :] + h * f(t[k], y[k, :])
                print(t[k+1], y[k + 1, :])
        else:
            for k in range(n):
                t[k + 1] = t[k] + h
                y[k + 1] = y[k] + h * f(t[k], y[k])
                print(t[k+1], y[k + 1])      
        return t, y

    def midpointrule(self, t0, y0, h, n, f):
        """
        Implementation of the midpoint rule algorithm (2nd order
        Runge-Kutta agorithm)
        """
        t = np.zeros(n + 1, dtype='f')
        neq = 1
        
        if isinstance(y0, (int, float)):
            y = np.zeros(n + 1, dtype='f')
            y[0] = y0
        else:
            neq = len(y0)
            y = np.zeros((n + 1, neq), dtype='f')
            y[0,:] = y0            
                
        t[0] = t0
        if neq > 1:
            for k in range(n):
                t[k + 1] = t[k] + h
                y[k + 1, :] = y[k, :] + h * f(t[k] + 0.5 * h, y[k, :] + 0.5 * h * f(t[k], y[k, :]))
        else:
            for k in range(n):
                t[k + 1] = t[k] + h
                y[k + 1] = y[k] + h * f(t[k] + 0.5 * h, y[k] + 0.5 * h * f(t[k], y[k]))            
        print(y)
        return t, y
            

    def heun(self, t0, y0, h, n, f):
        """
        Implementation of the heun algorithm (2nd order Runge-Kutta agorithm)
        """
        t = np.zeros(n + 1, dtype='f')
        neq = 1
               
        if isinstance(y0, (int, float)):
            y = np.zeros(n + 1, dtype='f')
            y[0] = y0
        else:
            neq = len(y0)
            y = np.zeros((n + 1, neq), dtype='f')
            y[0,:] = y0            
                
        t[0] = t0
        if neq > 1:
            for k in range(n):
                t[k + 1] = t[k] + h 
                k1 = f(t[k], y[k, :])
            
                y_tmp = y[k, :] + h * f(t[k + 1], y[k + 1, :])
                k2 = f(t[k + 1], y_tmp)
             
                y[k + 1, :] = y[k, :] + h * 0.5 * (k1 + k2)
        else:
            for k in range(n):
                t[k + 1] = t[k] + h 
                k1 = f(t[k], y[k])
            
                y_tmp = y[k] + h * f(t[k + 1], y[k + 1])
                k2 = f(t[k + 1], y_tmp)
             
                y[k + 1] = y[k] + h * 0.5 * (k1 + k2)
                
        print(y)
        return t, y
           

    def ClassicalRK4(self, t0, y0, h, n, f):
        """
        Implementation of the heun algorithm (2nd order Runge-Kutta agorithm)
        """
        t = np.zeros(n + 1, dtype='f')
        neq = 1
               
        if isinstance(y0, (int, float)):
            y = np.zeros(n + 1, dtype='f')
            y[0] = y0
        else:
            neq = len(y0)
            y = np.zeros((n + 1, neq), dtype='f')
            y[0,:] = y0     

        t[0] = t0
        if neq > 1:
            for k in range(n):
                t[k + 1] = t[k] + h
                k1 = f(t[k], y[k, :])

                y_tmp = y[k, :] + 0.5 * h * k1
                k2 = f(t[k] + 0.5 * h, y_tmp)

                y_tmp = y[k, :] + 0.5 * h * k2
                k3 = f(t[k] + 0.5 * h, y_tmp)

                y_tmp = y[k, :] + 0.5 * h * k3
                k4 = f(t[k + 1], y_tmp)

                y[k + 1, :] = y[k, :] + h * 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
        else:
            for k in range(n):
                t[k + 1] = t[k] + h
                k1 = f(t[k], y[k])

                y_tmp = y[k] + 0.5 * h * k1
                k2 = f(t[k] + 0.5 * h, y_tmp)

                y_tmp = y[k] + 0.5 * h * k2
                k3 = f(t[k] + 0.5 * h, y_tmp)

                y_tmp = y[k] + 0.5 * h * k3
                k4 = f(t[k + 1], y_tmp)

                y[k + 1] = y[k] + h * 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)

        print(y)
        return t, y
