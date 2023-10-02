import matplotlib.pyplot as plt

def plot_solution(x, T, T_exact, title_string):
    # Visulalization of the numerical and exact solution 
    fig, ax = plt.subplots(figsize=(10, 7))

    ax.plot(x, T_exact, label='Exact solution')
    ax.plot(x, T, '^g', label='Approximate solution')

    ax.set_xlabel('$x$')
    ax.set_ylabel('$T$')
    ax.set_title(title_string)
    ax.legend();
    
    plt.show()
