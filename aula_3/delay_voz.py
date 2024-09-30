import numpy as np
import matplotlib.pyplot as plt
from delay import delay
from scipy.io.wavfile import write

def normaliza_sinal(output):
    max_value = np.max(np.abs(output))

    if max_value > 2**16/2-1:
        output = output*((2**16-1)/max_value)
    output = output.astype(np.int16)
    return output

def salva_sinal(sinal, sample_rate, nome='saida.pcm', path='./'):
    write(path+nome, sample_rate, sinal)

if __name__ == "__main__":
    alou_path = "./alou.pcm"
    buffer = open(alou_path, 'rb').read()
    alou = np.frombuffer(buffer, dtype='int16')
    
    fs = 8*10**3
    ts = 1/fs
    n = np.arange(len(alou)) *ts

    fig, (ax_entrada, ax_saida) = plt.subplots(2, 1)

    ax_entrada.stem(n, alou)

    n1 = 150*10**-3
    n2 = 200*10**-3
    n1_amotras = n1 * fs
    n2_amotras = n2 * fs
    a0=0.5 
    a1=0.3 
    a2=0.2
    alou_delay= delay(alou, n, fs, a0=a0, a1=a1, a2=a2, n1=n1_amotras, n2=n2_amotras)
    
    alou_delay = normaliza_sinal(alou_delay)
    alou_delay = np.int16(alou_delay)
    salva_sinal(alou_delay, fs, nome='alou_delay.pcm')
    ax_saida.stem(n, alou)
    plt.show()
