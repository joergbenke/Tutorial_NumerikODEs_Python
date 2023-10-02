import numpy as np
from scipy.linalg import inv
import matplotlib.pyplot as plt

from matrixcompilation import matrix_heat, rhs_inhomogeneous_heat

if __name__ == "__main__":
    """ Test of the solution of the heat equation"""
    
    # definitions of parameters
    l_start, l_end = 0.0, 1.0
    dx = 0.1
    nx = int((l_end - l_start) / dx)
    
    """
    #
    # Solve homogeneous Dirichlet heat equation
    
    # create mesh
    x = np.linspace(0, 1, nx + 1, dtype="float")
    
    # create lhs A
    A = matrix_heat(nx, dx)
    
    # create rhs b (homogeneous)
    # b = rhs_homogeneous_heat(nx, dx)
    
    # create rhs b (inhomogeneous)
    b = rhs_inhomogeneous_heat(nx, dx)
    
    # 
    # numerical and exact solution of the system
    T = np.zeros(nx + 1) 
    T[1 : -1] = np.dot(inv(A), b)
    T[0], T[-1] = 0, 0
    print(T)

    T_exact = 0.5 * x * (1 - x) # notice how we multiply numpy arrays pointwise.
    print(T_exact)
    print(np.subtract(T, T_exact))
    
    # Visulalization of the numerical and exact solution 
    fig, ax = plt.subplots(figsize=(10, 7))

    ax.plot(x, T_exact, label='Exact solution')
    ax.plot(x, T, '^g', label='Approximate solution')

    ax.set_xlabel('$x$')
    ax.set_ylabel('$T$')
    ax.set_title('Heat equation - Homogeneous Dirichlet boundary conditions')
    ax.legend();
    
    plt.show()
    """    
    
    #
    # Solve homogeneous Dirichlet heat equation
 
    # create mesh
    x = np.linspace(0, 1, nx + 1, dtype="float")
    
    # create lhs A
    A = matrix_heat(nx, dx)
    print(A)
    
    # create rhs b (inhomogeneous)
    b = rhs_inhomogeneous_heat(nx, dx)
    print(b)
    
    # 
    # numerical and exact solution of the system
    T = np.zeros(nx + 1) 
    T[1 : -1] = np.dot(inv(A), b)
    T[0], T[-1] = 1, 0
    print(T)

    T_exact = 0.5 * (x + 2) * (1 - x) # notice how we multiply numpy arrays pointwise.
    print(T_exact)
    print(np.subtract(T, T_exact))
    
    # Visulalization of the numerical and exact solution 
    fig, ax = plt.subplots(figsize=(10, 7))

    ax.plot(x, T_exact, label='Exact solution')
    ax.plot(x, T, '^g', label='Approximate solution')

    ax.set_xlabel('$x$')
    ax.set_ylabel('$T$')
    ax.set_title('Heat equation - Homogeneous Dirichlet boundary conditions')
    ax.legend();
    
    plt.show()
