import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import warnings

# (Opcional) eliminar warnings
warnings.filterwarnings("ignore")

# 1. CARGAR EL AUDIO
fs, audio = wavfile.read("AUDIO.wav")

# 2. CONVERTIR A MONO SI ES NECESARIO
if len(audio.shape) > 1:
    audio = audio[:, 0]

# 3. CONVERTIR A FLOAT (IMPORTANTE)
audio = audio.astype(float)

# 4. OBTENER TAMAÑO DE LA SEÑAL
N = len(audio)

# 5. FFT DE LA SEÑAL ORIGINAL
fft_audio = np.fft.fft(audio)
frecuencias = np.fft.fftfreq(N, 1/fs)
magnitud = np.abs(fft_audio)

# 6. GENERAR RUIDO GAUSSIANO
ruido = np.random.normal(0, 0.5, N)

# 7. CREAR SEÑAL CON RUIDO
audio_ruidoso = audio + ruido

# 8. FFT DE LA SEÑAL CON RUIDO
fft_ruido = np.fft.fft(audio_ruidoso)
magnitud_ruido = np.abs(fft_ruido)

# 9. GRAFICAR RESULTADOS
plt.figure(figsize=(10,5))

# Señal original
plt.plot(frecuencias[:N//2], magnitud[:N//2], label="Señal original")

# Señal con ruido
plt.plot(frecuencias[:N//2], magnitud_ruido[:N//2], label="Señal con ruido")

plt.title("Comparación del Espectro FFT")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()
plt.grid()

plt.show()