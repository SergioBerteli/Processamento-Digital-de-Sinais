import numpy as np
import matplotlib.pyplot as plt


def delay(sinal, n, fs, a0, a1, a2, n1, n2):
    ts = 1/fs
    hist = np.zeros(3)
    y = list()
    n.round(decimals=12)

    for i, value in enumerate(sinal):
        #to do: arrumar essa logica porca
        hist[0] = value
        
        if i>=n1:
            hist[1] = sinal[int(i- n1)]

        if i>=n2:
            hist[2] = sinal[int(i- n2)]
                   
        saida_temp = hist[0]*a0 + hist[1]*a1 + hist[2]*a2 
        y.append(saida_temp)
    return np.array(y, dtype='f')


if __name__ == "__main__":
    impulso_path = "./impulso.pcm"
    buffer = open(impulso_path, 'rb').read()
    impulso = np.frombuffer(buffer, dtype='int16')
    
    fs = 8*10**3
    ts = 1/fs
    n = np.arange(-1*fs, len(impulso)-1*fs) *ts

    fig, (ax_entrada, ax_saida) = plt.subplots(2, 1)

    ax_entrada.stem(n, impulso)

    n1 = 10*10**-3
    n2 = 15*10**-3
    n1_amotras = n1 * fs
    n2_amotras = n2 * fs
    a0=0.5 
    a1=0.3 
    a2=0.2
    imp_delay = delay(impulso, n, fs, a0=a0, a1=a1, a2=a2, n1=n1_amotras, n2=n2_amotras)
    
    ax_saida.stem(n, imp_delay)
    plt.show()
