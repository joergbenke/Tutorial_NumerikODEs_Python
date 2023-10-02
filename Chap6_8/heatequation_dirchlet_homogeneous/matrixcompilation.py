import numpy as np
from scipy.sparse import diags

def matrix_heat(nx, dx):
    "Compilation of the 1d discretized heat equation matrix A"
    
    diagonals = np.array([1.0, -2.0, 1.0])
    offsets = np.array([-1, 0, 1 ])
    A = diags(diagonals, offsets, shape=(nx-1,nx-1)).toarray()
    
    return A / dx**2
    
def rhs_homogeneous_heat(nx, dx):
    "Compilation of the rhs b"
    
    b = (-1.0) * np.ones(nx-1)
    
    return b    
    
def rhs_inhomogeneous_heat(nx, dx):
    "Compilation of the rhs b"
    
    b = (-1.0) * np.ones(nx-1)
    b[0] = b[0] - 1.0/dx**2
    
    return b     
