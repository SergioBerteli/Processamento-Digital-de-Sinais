import numpy as np
import matplotlib.pyplot as plt

def degrau_unitario(inicio, fim):
    sinal = [1 if i >= 0 else 0 for i in range(inicio, fim)]
    return np.array(sinal)

def impulso_unitario(inicio, fim):
    sinal = [1 if i == 0 else 0 for i in range(inicio, fim)]
    return np.array(sinal)

def sinusoidal(n, f, ganho=1, fi=0):
    sinal = ganho*np.sin(2*np.pi*f*n + fi)
    return sinal

if __name__ == "__main__":
    degrau = degrau_unitario(-1, 4)
    print(degrau)
    impulso = impulso_unitario(-2, 2)
    print(impulso)

    inicio = -2
    fim = 1
    freq_amostragem = 800
    ts = 1/freq_amostragem
    n = np.arange(inicio, fim, ts)
    sin_teste = sinusoidal(n, 400)

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    ax1.stem(np.arange(-1, 4, 1), degrau)
    ax2.stem(np.arange(-2, 2, 1), impulso)
    ax3.stem(n, sin_teste)
    plt.show()
