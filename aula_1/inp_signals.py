import numpy as np
import matplotlib.pyplot as plt

def degrau_unitario(n):
    sinal = np.where(n>=0, 1, 0)
    return sinal

def impulso_unitario(n):
    sinal = np.where(n == 0, 1, 0)
    return sinal

def sinusoidal(n, f, ganho=1, fi=0):
    sinal = ganho*np.sin(2*np.pi*f*n + fi)
    return sinal

if __name__ == "__main__":
    # definição de parametros iniciais
    f_samp = 100
    ts = 1/f_samp
    inicio = -0.1
    fim = 0.1
    n = np.arange(inicio, fim, ts)
    n = np.round(n, decimals=12)
    
    # testes com o degrau
    degrau = degrau_unitario(n)
    
    relu = n*degrau
    
    #testes com o impulso
    
    imp = impulso_unitario(n)
    
    imp_pi = np.pi * imp
    
    fig, ((ax_degrau, ax_relu), (ax_impulso, ax_pi_impulso), (ax_sinu, ax_sin_teste), (ax_exp, ax_exp_teste)) = plt.subplots(4, 2)
    ax_degrau.stem(n, degrau)
    ax_degrau.set_title("Função degrau")

    ax_relu.stem(n, relu)
    ax_relu.set_title("Função relu (step * x)")

    ax_impulso.stem(n, imp)
    ax_impulso.set_title("Função impulso")

    ax_pi_impulso.stem(n, imp_pi)
    ax_pi_impulso.set_title("Função impulso * pi")
    
    plt.subplots_adjust(hspace=0.5)
    plt.show()
