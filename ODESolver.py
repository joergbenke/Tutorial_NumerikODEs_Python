import numpy as np

class ODESolver:
    def euler_explicit(self, t0, y0, h, n, f):
        """
        Implementation of the explicit euler algorithm
        """
        t = np.zeros(n + 1, dtype='f')
        y = np.zeros(n + 1, dtype='f')
        t[0], y[0] = t0, y0
        
        for k in range(n):
            t[k + 1] = t[k] + h
            y[k + 1] = y[k] + h * f(t, y[k])
        print(y)
        return t, y

    def midpointrule(self, t0, y0, h, n, f):
        """
        Implementation of the midpoint rule algorithm (2nd order
        Runge-Kutta agorithm)
        """

        t, y = t0, y0
        result = [(t, y)]

        for i in range(n):
            t += h
            y_tmp = y + 0.5 * h * f(t, y)
            y += h * f(t + 0.5 * h, y_tmp)
            result.append((t, y))

        return result

    def heun(self, t0, y0, h, n, f):
        """
        Implementation of the heun algorithm (2nd order Runge-Kutta agorithm)
        """

        t, y = t0, y0
        k1 = k2 = 0.0
        result = [(t, y)]

        for i in range(n):
            t += h
            k1 = f(t, y)

            y_tmp = y + h * f(t, y)
            k2 = f(t + h, y_tmp)

            y += 0.5 * h * (k1 + k2)
            result.append((t, y))

        return result

    def ClassicalRK4(self, t0, y0, h, n, f):
        """
        Implementation of the heun algorithm (2nd order Runge-Kutta agorithm)
        """

        t, y = t0, y0
        k1 = k2 = k3 = k4 = 0.0

        result = [(t, y)]

        for i in range(n):
            t += h
            k1 = f(t, y)

            y_tmp = y + 0.5 * h * k1
            k2 = f(t + 0.5 * h, y_tmp)

            y_tmp = y + 0.5 * h * k2
            k3 = f(t + 0.5 * h, y_tmp)

            y_tmp = y + 0.5 * h * k3
            k4 = f(t + h, y_tmp)

            y += h * 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
            result.append((t, y))

        return result
