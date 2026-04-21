import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
t = np.arange(0, 1, 1/Fs)

x = np.sin(2 * np.pi * 60 * t) + 0.5 * np.random.randn(len(t))

# FFT
X = np.fft.fft(x)
frecuencias = np.fft.fftfreq(len(x), 1/Fs)

# Gráfica
plt.plot(frecuencias, np.abs(X))
plt.title("Espectro de Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.show()