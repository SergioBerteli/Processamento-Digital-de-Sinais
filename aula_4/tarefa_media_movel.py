import numpy as np
import matplotlib.pyplot as plt

def degrau_unitario(n):
    sinal = np.where(n>=0, 1, 0)
    return np.int16(sinal)

def impulso_unitario(n):
    sinal = np.where(n == 0, 1, 0)
    return np.int16(sinal)

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
    n_vet = np.arange(10)

    impulso = impulso_unitario(n_vet)

    degrau = degrau_unitario(n_vet)

    vet = np.where(np.logical_and(n_vet>=0, n_vet<4), 0.5**n_vet, 0)

    # medias
    mm_impulso = media_movel(impulso, 8)

    mm_degrau = media_movel(degrau, 8)

    mm_vet = media_movel(vet, 8)
    
    #plots

    fig, ((ax_imp, ax_impmm), (ax_degrau, ax_degraumm), (ax_vet, ax_vetmm)) = plt.subplots(3, 2)
    
    ax_imp.stem(n_vet, impulso)
    ax_imp.set_title('Função impulso')
    ax_impmm.stem(n_vet, mm_impulso)
    ax_impmm.set_title('Função impulso após média móvel')
    ax_degrau.stem(n_vet, degrau)
    ax_degrau.set_title('Função degrau')
    ax_degraumm.stem(n_vet, mm_degrau)
    ax_degraumm.set_title('Função degrau após média móvel')
    ax_vet.stem(n_vet, vet)
    ax_vet.set_title('Vetor dos slides')
    ax_vetmm.stem(n_vet, mm_vet)
    ax_vetmm.set_title('Vetor dos slides após média móvel')

    fig.tight_layout()

    plt.show()
