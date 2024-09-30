import numpy as np
import matplotlib.pyplot as plt

def impulso_unitario(n):
    sinal = np.where(n == 0, 1, 0)
    return np.int16(sinal)

def degrau_unitario(n):
    sinal = np.where(n>=0, 1, 0)
    return np.int16(sinal)

def sistema(sinal, n):
    R = 0.95
    y = list()
    hist_x = np.zeros(2)
    hist_y = 0
    n.round(decimals=12)

    for i, value in enumerate(sinal):
        hist_x[0] = value
        if i >  1:
            hist_x[1] = sinal[int(i - 1)]
            hist_y = y[int(i -1)]
        saida_buffer = hist_x[0] - hist_x[1] + R * hist_y
        y.append(saida_buffer)
    return np.array(y, dtype='f')


if __name__ == "__main__":
    sinal_q3_path = "./Anexo_41743457.pcm"
    buffer = open(sinal_q3_path, 'rb').read()
    sinal_q3 = np.frombuffer(buffer, dtype='int16')
    n_sinal = np.arange(len(sinal_q3))

    n = np.arange(-2, 50)
    impulso = impulso_unitario(n)

    degrau = degrau_unitario(n)
    
    fig, ((ax_entrada, ax_saida), (ax_2_entrada, ax_2_saida),(ax_3_entrada, ax_3_saida)) = plt.subplots(3, 2)

    ax_entrada.stem(n, impulso)

    ax_2_entrada.stem(n, degrau)
    
    ax_3_entrada.stem(n_sinal, sinal_q3)

    # parametros do novo sinal
    sinal= sistema(impulso, n)
    ax_saida.stem(n, sinal)

    sinal_2= sistema(degrau, n)
    ax_2_saida.stem(n, sinal_2)

    sinal_3= sistema(sinal_q3, n)
    ax_3_saida.stem(n_sinal, sinal_3)
    plt.show()

