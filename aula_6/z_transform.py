import numpy as np
import matplotlib.pyplot as plt

def z_trans_uni(signal, n=None, z=None):
    y = list()
    if n is None:
        n = np.arange(len(signal))
    if z is None:
        z = np.arange(len(signal))
    for i in z:
        temp = 0
        for k in n:
            if i == 0 and k != 0:
                temp += 0  
            else:
                temp += signal[k] / (i**k)
        y.append(temp) 
    return np.array(y)

def impulso_unitario(n):
    sinal = np.where(n == 0, 1, 0)
    return np.int16(sinal)

if __name__ == "__main__":
    n = np.arange(10)
    sinal = 4*impulso_unitario(n)
    sinal_z =  z_trans_uni(sinal, n)
    
    fig, (ax_signal, ax_z_signal) = plt.subplots(2, 1)
    ax_signal.stem(n, sinal)
    ax_z_signal.stem(n, sinal_z)
    plt.show()
