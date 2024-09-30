import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    n_vet = np.arange(10)

    impulso = impulso_unitario(n_vet)

    resp_imp= media_movel(impulso, 8)
