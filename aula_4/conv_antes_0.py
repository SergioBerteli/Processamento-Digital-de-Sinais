import numpy as np
import matplotlib.pyplot as plt

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
    impulso_path = "./impulso.pcm"
    buffer = open(impulso_path, 'rb').read()
    impulso = np.frombuffer(buffer, dtype='int16')

    degrau_path = "./degrau.pcm"
    buffer = open(impulso_path, 'rb').read()
    degrau = np.frombuffer(buffer, dtype='int16')

    fs = 8*10**3
    ts = 1/fs
    n= np.arange(len(impulso))
    plt.stem(n, degrau)
    plt.show()
