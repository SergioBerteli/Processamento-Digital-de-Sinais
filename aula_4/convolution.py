import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    n = np.arange(10)
    x = np.where(np.logical_and(n>=0, n<6), 1, 0)
    h = np.where(np.logical_and(n>=0, n<4), 0.5**n, 0)
    y = np.convolve(x, h)
    n_y = np.arange(len(y))

    fig, (ax_x, ax_h, ax_y) = plt.subplots(3, 1)
    ax_x.stem(n, x)
    ax_h.stem(n, h)
    ax_y.stem(n_y, y)
    plt.show()
