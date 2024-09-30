import numpy as np
import matplotlib.pyplot as plt


def degrau_unitario(n):
    sinal = np.where(n>=0, 1, 0)
    return sinal
def seq_exp(n, base, ganho=1):
    sinal = ganho*base**n
    return sinal

def media_movel(fn, k):
    hist = np.zeros(k)
    y = list()
    for x in fn:
        hist[-1] = x
        res = np.sum(1/k * hist)
        y.append(res)
        hist = np.roll(hist, -1)
    return np.array(y, dtype='f')


if __name__ == "__main__":
    inicio = 0
    fim = 100
    n = np.arange(inicio, fim, 1)
    n = np.round(n, decimals=12)
    fn = degrau_unitario(n)
    media = media_movel(fn, 10)

    fig, (ax_inp, ax_out) = plt.subplots(2, 1)

    ax_inp.stem(n, fn)

    ax_out.stem(n, media)

    plt.show()

