"""Functions to visualize data structures."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import colors


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    """
    Truncate a colormap to have less color range.
    
    From unutbu on stackoverflow.
    """
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap


def show_array(
    x, 
    color=None, 
    figsize=(2, 2), 
    title=None, 
    remove_x=False, 
    remove_y=False,
    cmap="Blues",
):
    """Display an array with indices, color, and values."""
    if color is None:
        color = x
    elif not isinstance(color, np.ndarray):
        color = np.full(shape=x.shape, fill_value=color)
    fig, ax = plt.subplots(figsize=figsize)
    cmap = plt.get_cmap(cmap)
    im = ax.imshow(color, cmap=truncate_colormap(cmap, 0.1, 0.6))
    if not remove_x:
        ax.set_xticks(range(x.shape[1]))
    else:
        ax.set_xticks([])
    if not remove_y:
        ax.set_yticks(range(x.shape[0]))
    else:
        ax.set_yticks([])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            ax.add_patch(Rectangle((j-.5, i-.5), 1, 1, fill=False, edgecolor="k"))
            ax.text(j, i, x[i, j], ha="center", va="center", color="k")
    if title is not None:
        ax.set_title(title)
    return fig
