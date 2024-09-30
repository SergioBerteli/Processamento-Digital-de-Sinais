from dft import normaliza_sinal
import numpy as np
import matplotlib.pyplot as plt

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

def importa_sinal(path):
    buffer = open(path, 'rb').read()
    sinal = np.frombuffer(buffer, dtype='int16')
    return sinal

if __name__ == "__main__":
    fs = 8000
    ts = 1/fs
    N = 300 # definir janela para amostragem
    tom_ruido = importa_sinal('./tarefa.pcm')
    tom_ruido = tom_ruido[:N] # amostrando o sinal
    n = np.arange(N) * ts # convertendo eixo x para segundos
    tom_freq = dft(tom_ruido, N) # aplicando a DFT
    tom_freq = np.abs(tom_freq) # pegando o modulo da DFT

    fig, (ax_sin, ax_n_freq) = plt.subplots(2, 1)

    ax_sin.stem(n, tom_ruido)
    ax_sin.grid(True)

    # escalando o eixo x para exibir a frequencia em hertz
    n2 = np.arange(len(tom_freq)//2) 
    n2 = n2*fs/len(tom_freq)
    
    # normalizando o sinal
    tom_freq = tom_freq/len(tom_freq)
    # encurtando o sinal 
    tom_freq = tom_freq[:len(tom_freq)//2]
    ax_n_freq.stem(n2, tom_freq)
    ax_n_freq.grid(True)

    fig.tight_layout()

    plt.show()
