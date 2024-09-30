import numpy as np
import matplotlib.pyplot as plt

def normaliza_sinal(x, N, fs):
    n = np.arange(N)
    N2 = N//2
    n2 = n[:N2]*fs/N
    x_norm = x[:N2]/N2
    return x_norm, n2

def dft(x, N, M=None):
    if M == None:
        M = len(x)
    y = list()
    k = 2*np.pi/N
    for m in range(M):
        temp = 0
        for n in range(N):
            temp += x[n]*np.e**(-1j*k*n*m)
        y.append(temp)
    return np.array(y)
if __name__ == "__main__":
    fs = 1000
    N = 100 #tamanho do sinal
    n = np.arange(N) # exi x

    freq1 = 60 # frequencia do primeiro seno
    x1 = 1*np.cos(2*np.pi*freq1*n/fs)
    freq2 = 400 # frequencia do segundo seno
    x2 = 0.1*np.cos(2*np.pi*freq2*n/fs)
    
    x = x1 + x2 # sinal a ser analisado
    
    x_dft = dft(x, N) # sinal transformado para o dominio da frequencia

    x_norm, n2 = normaliza_sinal(x_dft, n, fs)

    # normalizando o sinal
    fig, (ax_x, ax_x_dft) = plt.subplots(2, 1)

    ax_x.plot(n, x)
    ax_x.grid(True)
    ax_x_dft.stem(n2, np.abs(x_norm))
    ax_x_dft.grid(True)

    fig.tight_layout()

    plt.show()
