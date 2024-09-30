import numpy as np
import matplotlib.pyplot as plt

def degrau_unitario(n):
    sinal = np.where(n>=0, 1, 0)
    return np.int16(sinal)

def gera_sinal_h(n):
    y = list()
    for i in n:
        if i == 0:
            y.append(0.1)
        elif i == 1:
            y.append(0.2)
        elif i == 2:
            y.append(0.4)
        elif i == 3:
            y.append(0.2)
        elif i == 4:
            y.append(0.1)
        else:
            y.append(0)
    return np.array(y)

def impulso_unitario(n):
    sinal = np.where(n == 0, 1, 0)
    return np.int16(sinal)

if __name__ == "__main__":
    n = np.arange(10)
    x = np.where(np.logical_and(n>=0, n<=1), 1, 0)
    h = gera_sinal_h(n)
    y = np.convolve(x, h)
    n_y = np.arange(len(y))

    impulso = impulso_unitario(n)
    y_2 = np.convolve(impulso, h)
    n_y_2 = np.arange(len(y_2))

    fig, (ax_x, ax_h, ax_y, ax_y_2) = plt.subplots(4, 1)
    ax_x.stem(n, x)
    ax_x.grid(True)
    ax_x.set_title("Função porta")

    ax_h.stem(n, h)
    ax_h.grid(True)
    ax_h.set_title("sinal dado")

    ax_y.stem(n_y, y)
    ax_y.grid(True)
    ax_y.set_title("porta * h")

    ax_y_2.stem(n_y_2, y_2)
    ax_y_2.grid(True)
    ax_y_2.set_title("impulso * h")
    fig.tight_layout()
    plt.show()
