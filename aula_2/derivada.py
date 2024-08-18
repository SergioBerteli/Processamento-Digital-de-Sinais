import numpy as np
import matplotlib.pyplot as plt

def degrau_unitario(n):
    sinal = np.where(n>=0, 1, 0)
    return sinal

def derivada(fn):
    x_ant = 0
    y = list()
    for x in fn:
        res = x - x_ant
        y.append(res)
        x_ant = x
    return np.array(y, dtype=np.int16)
if __name__ == "__main__":
    inicio = -2
    fim = 7
    n = np.arange(inicio, fim)
    n = np.round(n, decimals=12)
    degrau = degrau_unitario(n)
    diff_degrau = derivada(degrau)
    
    fg, (ax_inp, ax_out) = plt.subplots(2, 1)

    ax_inp.stem(n, degrau)
    ax_out.stem(n, diff_degrau)
    plt.show()
