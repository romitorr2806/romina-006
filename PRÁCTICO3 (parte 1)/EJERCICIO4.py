import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# CASO 1: CON ALIASING (Fs = 500)
# -------------------------------

Fs1 = 500  # Frecuencia de muestreo insuficiente
t1 = np.arange(0, 1, 1/Fs1)

# Señal
x1 = np.sin(2*np.pi*250*t1) + np.sin(2*np.pi*1000*t1)

# FFT
X1 = np.fft.fft(x1)
frecuencias1 = np.fft.fftfreq(len(x1), 1/Fs1)

# Gráfica
plt.figure()
plt.plot(frecuencias1[:len(frecuencias1)//2], np.abs(X1)[:len(X1)//2])
plt.title("Espectro con Aliasing (Fs = 500 Hz)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()
plt.show()


# -------------------------------
# CASO 2: SIN ALIASING (Fs = 3000)
# -------------------------------

Fs2 = 3000  # Frecuencia de muestreo adecuada
t2 = np.arange(0, 1, 1/Fs2)

# Señal
x2 = np.sin(2*np.pi*250*t2) + np.sin(2*np.pi*1000*t2)

# FFT
X2 = np.fft.fft(x2)
frecuencias2 = np.fft.fftfreq(len(x2), 1/Fs2)

# Gráfica
plt.figure()
plt.plot(frecuencias2[:len(frecuencias2)//2], np.abs(X2)[:len(X2)//2])
plt.title("Espectro sin Aliasing (Fs = 3000 Hz)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()
plt.show()