import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    fim = 20*10**-3
    t = np.linspace(0, fim, 10**6)
    ganho = 1
    f0 = 100
    sinal_analogico = ganho*np.sin(2*np.pi*f0*t)

    f_samp = 8*10**3
    
    ts = 1/f_samp

    t_discreto = np.arange(10*10**-3, 17.5*10**-3, ts)

    sinal_amostrado = ganho*np.sin(2*np.pi*f0*t_discreto)

    sinal_discreto = ganho*np.sin(2*np.pi*f0*t_discreto)


    fig, (ax_sinaisad, ax_discreto) = plt.subplots(2, 1)
    ax_sinaisad.plot(t, sinal_analogico, color='orange', linewidth=3)
    ax_sinaisad.stem(t_discreto, sinal_amostrado)
    ax_sinaisad.grid(True)

    ax_discreto.stem(t_discreto, sinal_discreto)
    ax_discreto.grid(True)

    plt.tight_layout()
    plt.show()
