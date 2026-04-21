import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
t = np.arange(0, 1, 1/Fs)

# Frecuencia aleatoria
f = np.random.randint(50, 200)

# Señal
x = np.sin(2 * np.pi * f * t)

# FFT
X = np.fft.fft(x)
frecuencias = np.fft.fftfreq(len(x), 1/Fs)

# Frecuencia dominante
frecuencia_dominante = frecuencias[np.argmax(np.abs(X))]
print("Frecuencia real:", f, "Hz")
print("Frecuencia detectada:", frecuencia_dominante, "Hz")

# Gráfica
plt.plot(frecuencias[:len(frecuencias)//2], np.abs(X)[:len(X)//2])
plt.title("Espectro de Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()
plt.show()