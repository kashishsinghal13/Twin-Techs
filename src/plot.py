import numpy as np
import matplotlib.pyplot as plt

def plot(paths_XYs, colours=['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF']):
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))
    
    for i, XYs in enumerate(paths_XYs):
        c = colours[i % len(colours)]
        
        for XY in XYs:
            ax.plot(XY[:, 0], XY[:, 1], c=c, linewidth=2)
    
    ax.set_aspect('equal')
    plt.show()