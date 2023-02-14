# Importamos librerias
import cv2

# Leemos la img
imagen =cv2.imread('img.png')

# Rotacion 1
rot1 = cv2.flip(imagen, 0)

# Rotacion 2
rot2 = cv2.flip(imagen, 1)

# Rotacion 3
rot3 = cv2.flip(imagen, -1)

# Mostramos el recorte
cv2.imshow('IMAGEN ORIGINAL', imagen)
cv2.imshow('ROTACION 1', rot1)
cv2.imshow('ROTACION 2', rot2)
cv2.imshow('ROTACION 3', rot3)


cv2.waitKey(0)