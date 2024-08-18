import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

def degrau_unitario(n):
    sinal = np.where(n>=0, 1, 0)
    return np.int16(sinal)

def impulso_unitario(n):
    sinal = np.where(n == 0, 1, 0)
    return np.int16(sinal)

def sinusoidal(n, f, ganho=1, fi=0):
    sinal = ganho*np.sin(2*np.pi*f*n + fi)
    return np.int16(sinal)

def seq_exp(n, base, ganho=1):
    sinal = ganho*base**n
    return np.int16(sinal)

def calcula_energia(sinal):
    energia = np.sum(sinal**2)
    return np.int16(energia)

def salva_sinal(sinal, sample_rate, nome='saida.pcm', path='./'):
    write(path+nome, sample_rate, sinal)


if __name__ == "__main__":
    # TODO: SALVAR SINAIS INICIAS PARA CARREGAR DEPOIS
    # definição de parametros iniciais
    f_samp = 8*10**3
    ts = 1/f_samp
    inicio = 0
    fim = 3
    n = np.arange(inicio, fim, ts)
    n = np.round(n, decimals=12)
    
    # testes com o degrau
    degrau = np.int16(2**14*degrau_unitario(n))

    salva_sinal(degrau, f_samp, 'degrau.pcm')
    
    relu = n*degrau
    
    #testes com o impulso
    
    imp = np.int16(2**13*impulso_unitario(n))
    
    imp_pi = np.pi * imp

    salva_sinal(imp, f_samp, 'impulso.pcm')

    # testes com sequência sinusoidal

    fs_sin = 0.1*10**3
    ts_sin = 1/fs_sin
    n_sin = np.arange(-1, 1, ts_sin)
    seq_sin = sinusoidal(n_sin, f=2)

    sin_teste = degrau_unitario(n_sin) * seq_sin

    #testes com a sequência exponencial

    inicio = 0
    fim = 5
    n_exp = np.arange(inicio, fim, 1)
    exp_teste = seq_exp(n_exp, base=2, ganho=1)

    exp_negativo_teste = seq_exp(n_exp, base=-0.5, ganho=1)

    #plots

    fig, ((ax_degrau, ax_relu), (ax_impulso, ax_pi_impulso), (ax_sinu, ax_sin_teste), (ax_exp, ax_exp_teste)) = plt.subplots(4, 2)
    ax_degrau.stem(n, degrau)
    ax_degrau.set_title("Função degrau")
    ax_degrau.grid(True)

    ax_relu.stem(n, relu)
    ax_relu.set_title("Função relu (step * x)")
    ax_relu.grid(True)

    ax_impulso.stem(n, imp)
    ax_impulso.set_title("Função impulso")
    ax_impulso.grid(True)

    ax_pi_impulso.stem(n, imp_pi)
    ax_pi_impulso.set_title("Função impulso * pi")
    ax_pi_impulso.grid(True)
    
    ax_sinu.stem(n_sin, seq_sin)
    ax_sinu.set_title("Sequência sinusoidal")
    ax_sinu.grid(True)

    ax_sin_teste.stem(n_sin, sin_teste)
    ax_sin_teste.set_title("Seno * degrau")
    ax_sin_teste.grid(True)

    ax_exp.stem(n_exp, exp_teste)
    ax_exp.set_title("Sequência exponencial (base positiva)")
    ax_exp.grid(True)

    ax_exp_teste.stem(n_exp, exp_negativo_teste)
    ax_exp_teste.set_title("Sequência exponencial (base negativa)")
    ax_exp_teste.grid(True)

    plt.subplots_adjust(hspace=0.5)
    plt.show()

