import numpy as np
import matplotlib.pyplot as plt

def salva_sinal(sinal, sample_rate, nome='saida.pcm', path='./'):
    write(path+nome, sample_rate, sinal)

def echo(sinal, d, a0, a1):
    ts = 1/fs
    hist = np.zeros(3)
    y = list()
    n.round(decimals=12)

    for i, value in enumerate(sinal):
        #to do: arrumar essa logica porca
        hist[0] = value
        
        if i>=d:
            hist[1] = y[int(i- d)]
                   
        saida_temp = hist[0]*a0 + hist[1]*a1  
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

    # parametros do novo sinal
    d_segundos = 100*10**-3
    d_amotras = d_segundos * fs
    a0=1
    a1=0.7
    
    sinal_echo = echo(impulso, d= d_amotras, a0=a0, a1=a1)
    ax_saida.stem(n, sinal_echo)

    plt.show()

