# Importamos librerias
import cv2

# Leemos la img
imagen =cv2.imread('img.png')

# Vamos a redimensionar
# red = cv2.resize(img, outimg, fx, fy, interpolation)

# Red 1
red1 = cv2.resize(imagen, None, fx = 1.5, fy = 1.5)

# Red 2
red2 = cv2.resize(imagen, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_AREA)

# Red 3
red3 = cv2.resize(imagen, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)

# Red 4
ancho = 400
alto = 500
tam = (ancho, alto)
red4 = cv2.resize(imagen, tam, interpolation = cv2.INTER_CUBIC)


# Mostramos el recorte
cv2.imshow('IMAGEN ORIGINAL', imagen)
#cv2.imshow('REDIMENSION 1', red1)
#cv2.imshow('REDIMENSION 2', red2)
#cv2.imshow('REDIMENSION 3', red3)
cv2.imshow('REDIMENSION 4', red4)

cv2.waitKey(0)
