import numpy as np
from scipy.linalg import inv
import matplotlib.pyplot as plt

# from matrixcompilation import matrix_heat, rhs_constant_heat
from matrixcompilation import matrix_heat_neumann, rhs_constant_heat_neumann

from visualization import plot_solution

if __name__ == "__main__":
    # Test of the solution of the heat equation
    
    # definitions of parameters
    l_start, l_end = 0.0, 2.0
    dx = 0.1
    nx = int((l_end - l_start) / dx)
    
    """
    #
    # Solve homogeneous Dirichlet heat equation
    
    # create mesh
    x = np.linspace(l_start, l_end, nx + 1, dtype="float")
    
    # create lhs A
    A = matrix_heat(nx, dx)
    
    # create rhs b (inhomogeneous)
    b = rhs_constant_heat(nx, 0)
    
    # 
    # numerical and exact solution of the system
    T = np.zeros(nx + 1) 
    T[1 : -1] = np.dot(inv(A), b)
    T[0], T[-1] = 0, 0
    print(T)

    T_exact = 0.5 * (x - l_start) * (l_end - x) # general form 
    print(T_exact)
    print(np.subtract(T, T_exact))
    
    # Visulalization of the numerical and exact solution 
    plot_solution(x, T, T_exact, 'Heat equation - Homogeneous Dirichlet boundary conditions')
    """  
    
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
    plot_solution(x, T, T_exact, 'Heat equation - Inhomogeneous Dirichlet boundary conditions')
    """
    
    #
    # Solve neumann conditions (heat equation)
    
    # create mesh
    x = np.linspace(l_start, l_end, nx + 1, dtype="float")
    
    # create lhs A
    A = matrix_heat_neumann(nx, dx)
    print(A)
      
    # create rhs b (inhomogeneous)
    b = rhs_constant_heat_neumann(nx, dx)
    
    # 
    # numerical and exact solution of the system
    T = np.zeros(nx + 1) 
    T[1 : -1] = np.dot(inv(A), b)
    T[0] = 4./3.*T[1] - 1./3.*T[2] - 4./3.*dx 
    T[-1] = 1
    print(T)

    T_exact = -0.5 * (x**2 - 4 * x + (l_end - l_start)) # general form für l_end = 1, 2; nicht mehr gueltig für > 2
    print(T_exact)
    print(np.subtract(T, T_exact))
    
    # Visulalization of the numerical and exact solution 
    plot_solution(x, T, T_exact, 'Heat equation - Homogeneous Dirichlet boundary conditions')
