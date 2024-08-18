import numpy as np
import matplotlib.pyplot as plt
import media_movel

if __name__ == "__main__":
    # dados do arquivo com o seno
    sweep_path = "./sweep_20hz_2000hz.pcm"
    buffer = open(sweep_path, 'rb').read()
    sweep = np.frombuffer(buffer, dtype='int16')
    
    fs = 400
    ts = 1/fs
    n = np.arange(0, len(sweep))

    sweep_filtrado = media_movel.media_movel(sweep, 100)
    fig, (ax_entrada, ax_saida) = plt.subplots(2, 1)
    ax_entrada.stem(n, sweep)
    ax_saida.stem(n, sweep_filtrado)
    plt.show()
