import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# 1. Cargar el audio
fs, audio = wavfile.read("AUDIO.wav")

# 2. Si es estéreo, tomar solo un canal
if len(audio.shape) > 1:
    audio = audio[:, 0]

# 3. Calcular FFT
N = len(audio)
fft_audio = np.fft.fft(audio)

# 4. Obtener frecuencias
frecuencias = np.fft.fftfreq(N, 1/fs)

# 5. Magnitud del espectro
magnitud = np.abs(fft_audio)

# 6. Graficar (solo mitad positiva)
plt.plot(frecuencias[:N//2], magnitud[:N//2])
plt.title("Espectro de Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.show()

# 7. Frecuencia dominante
indice_max = np.argmax(magnitud[:N//2])
frecuencia_dominante = frecuencias[indice_max]

print("Frecuencia dominante:", frecuencia_dominante, "Hz")