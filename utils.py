import numpy as np
import matplotlib.pyplot as plt

def plot_trajectory(ax, t, sol, keys=['w1', 'w2', 'w1+w2'], save_image=True, title='plot'):
    ax.plot(t, sol, label=keys)
    ax.set_xlabel('time(s)')
    ax.set_ylabel('value')
    ax.set_title(title)
    ax.legend()
    ax.grid()
    
    
