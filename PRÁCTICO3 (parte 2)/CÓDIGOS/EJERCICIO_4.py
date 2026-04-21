import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
img = plt.imread("IMAGEN.jpg")

# Si la imagen tiene 3 canales (RGB), convertir a gris
if len(img.shape) == 3:
    img = np.mean(img, axis=2)

# FFT 2D
fft_img = np.fft.fft2(img)
fft_shift = np.fft.fftshift(fft_img)

# Espectro de magnitud
magnitud = np.log(np.abs(fft_shift) + 1)

# Crear filtro pasa-bajo
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2

mask = np.zeros((rows, cols))
radio = 30
mask[crow-radio:crow+radio, ccol-radio:ccol+radio] = 1

# Aplicar filtro
fft_filtrado = fft_shift * mask

# Transformada inversa
fft_ishift = np.fft.ifftshift(fft_filtrado)
img_filtrada = np.fft.ifft2(fft_ishift)
img_filtrada = np.abs(img_filtrada)

# Mostrar resultados
plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(magnitud, cmap='gray')
plt.title("Espectro")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(img_filtrada, cmap='gray')
plt.title("Filtrada")
plt.axis("off")

plt.show()