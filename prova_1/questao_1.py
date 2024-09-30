import numpy as np
import matplotlib.pyplot as plt

def impulso_unitario(n):
    sinal = np.where(n == 0, 1, 0)
    return np.int16(sinal)

def degrau_unitario(n):
    sinal = np.where(n>=0, 1, 0)
    return np.int16(sinal)

def salva_sinal(sinal, sample_rate, nome='saida.pcm', path='./'):
    write(path+nome, sample_rate, sinal)

def echo(sinal, d, a0, a1):
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
    n = np.arange(-2, 200)
    impulso = impulso_unitario(n)

    degrau = degrau_unitario(n)
    
    fig, ((ax_entrada, ax_saida), (ax_2_entrada, ax_2_saida)) = plt.subplots(2, 2)

    ax_entrada.stem(n, impulso)

    ax_2_entrada.stem(n, degrau)

    # parametros do novo sinal
    delay = 16
    a0=1
    a1=0.9
    
    sinal_echo = echo(impulso, d= delay, a0=a0, a1=a1)
    ax_saida.stem(n, sinal_echo)

    sinal_2_echo = echo(degrau, d= delay, a0=a0, a1=a1)
    ax_2_saida.stem(n, sinal_2_echo)

    plt.show()

