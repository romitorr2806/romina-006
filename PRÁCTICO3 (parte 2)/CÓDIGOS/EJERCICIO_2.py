import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import warnings

# Quitar warnings (opcional)
warnings.filterwarnings("ignore")

# 1. Cargar audio
fs, audio = wavfile.read("AUDIO.wav")

# 2. Convertir a mono si es estéreo
if len(audio.shape) > 1:
    audio = audio[:, 0]

# 3. Convertir a float (IMPORTANTE)
audio = audio.astype(float)

# 4. Número de muestras
N = len(audio)

# 5. FFT de la señal original
fft_audio = np.fft.fft(audio)
frecuencias = np.fft.fftfreq(N, 1/fs)
magnitud = np.abs(fft_audio)

# 6. Generar ruido gaussiano
ruido = np.random.normal(0, 0.02, N)

# 7. Crear señal con ruido
audio_ruidoso = audio + ruido

# 8. FFT de la señal con ruido
fft_ruido = np.fft.fft(audio_ruidoso)
magnitud_ruido = np.abs(fft_ruido)

# 9. Graficar comparación
plt.figure(figsize=(10,5))
plt.plot(frecuencias[:N//2], magnitud[:N//2], label="Señal original")
plt.plot(frecuencias[:N//2], magnitud_ruido[:N//2], label="Señal con ruido")
plt.title("Comparación del espectro FFT")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()
plt.grid()
plt.show()