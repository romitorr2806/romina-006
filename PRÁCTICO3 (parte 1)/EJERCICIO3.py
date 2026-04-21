import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
t = np.arange(0, 1, 1/Fs)

# Señal
x = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*200*t)

# FFT
X = np.fft.fft(x)
frecuencias = np.fft.fftfreq(len(x), 1/Fs)

# Graficar espectro (solo positivo)
plt.plot(frecuencias[:len(frecuencias)//2], np.abs(X)[:len(X)//2])
plt.title("Espectro de Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.show()