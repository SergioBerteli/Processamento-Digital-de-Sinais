import numpy as np
import matplotlib.pyplot as plt
import inp_signals as sinais

def normaliza_sinal(output):
    max_value = np.max(np.abs(output))

    if max_value > 2**16/2-1:
        output = output*((2**16-1)/max_value)
    output = output.astype(np.int16)
    return output

if __name__ == "__main__":
    f_samp = 8*10**3
    ts = 1/f_samp
    inicio = -1
    fim = 3
    n = np.arange(inicio, fim, ts)
    n = np.round(n, decimals=12)

    degrau = np.int16(2**14*sinais.degrau_unitario(n))

    sinais.salva_sinal(degrau, f_samp, 'degrau.pcm')

    imp = np.int16(2**14*sinais.impulso_unitario(n))
    
    sinais.salva_sinal(imp, f_samp, 'impulso.pcm')

    seq_sin = sinais.sinusoidal(n, f=400, ganho=2**14)
    sinais.salva_sinal(seq_sin, f_samp, 'sin.pcm')

    exp_teste = sinais.seq_exp(n, base=100, ganho=1)
    exp_normalizado = normaliza_sinal(exp_teste)
    sinais.salva_sinal(exp_normalizado, f_samp, 'exp.pcm')

    plt.stem(n, exp_normalizado)
    plt.show()
