import numpy as np
import matplotlib.pyplot as plt

Fs = 1000  # Frecuencia de muestreo (Hz)
t = np.arange(0, 1, 1/Fs)  # 1 segundo de señal
x = np.sin(2 * np.pi * 40 * t)
X = np.fft.fft(x)
f = np.fft.fftfreq(len(t), 1/Fs)
plt.plot(f, np.abs(X))
plt.title("Espectro de Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()
plt.show()
