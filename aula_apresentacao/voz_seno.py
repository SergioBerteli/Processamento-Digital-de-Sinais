import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

if __name__ == "__main__":
    sample_rate = 8*10**3
    sine_path = "./audio_files/seno_teste.wav"
    voice_path = "./audio_files/voz.wav"
    
    # dados do arquivo com o seno
    buffer = open(sine_path, 'rb').read()
    sine_data = np.frombuffer(buffer, dtype='int16')

    # dados do arquivo com a voz 
    buffer = open(voice_path, 'rb').read()
    voice_data = np.frombuffer(buffer, dtype='int16')

    data_len = len(sine_data)
    t = np.arange(0, data_len/sample_rate, 1/sample_rate)

    output = voice_data[:len(t)] + sine_data[:len(t)]

    # normalizando o array de saida
    max_value = np.max(np.abs(output))

    if max_value > 2**16/2-1:
        output = output*((2**16-1)/max_value)
    output = output.astype(np.int16)

    # Salvando o arquivo 
    write('saida.pcm', sample_rate, output)
    
    #plots 
    fig, (ax_sin, ax_voice, ax_sum) = plt.subplots(3, 1)

    ax_sin.plot(t, sine_data, label='seno')
    ax_sin.set_title("Seno de 400hz")
    ax_sin.set_xlabel("Tempo(s)")
    ax_sin.set_ylabel("Amplitude")
    ax_sin.legend()

    ax_voice.plot(t, voice_data, label='Voz')
    ax_voice.set_title("Voz gravada")
    ax_voice.set_xlabel("Tempo(s)")
    ax_voice.set_ylabel("Amplitude")
    ax_voice.legend()

    ax_sum.plot(t, output, label='Resultado')
    ax_sum.set_title("Resultado da soma da voz com o seno")
    ax_sum.set_xlabel("Tempo(s)")
    ax_sum.set_ylabel("Amplitude")
    ax_sum.legend()

    plt.tight_layout()

    plt.show()
