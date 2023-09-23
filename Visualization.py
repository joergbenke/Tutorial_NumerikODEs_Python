import matplotlib.pyplot as plt

def visualization_fct(time_array, result_array, label_array): 
    """ Printing the solutions """
    print( label_array)
    plt.plot(time_array, result_array, label=label_array)
    plt.plot(time_array, result_array, label=label_array)
    plt.plot(time_array, result_array, label=label_array)
    plt.plot(time_array, result_array, label=label_array)
    
    plt.legend()
    plt.show()
