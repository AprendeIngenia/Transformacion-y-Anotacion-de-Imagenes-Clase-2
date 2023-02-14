# Importamos librerias
import cv2

# Leemos la img
imagen =cv2.imread('dibujo.png')

# Redimensionamos
imagen = red3 = cv2.resize(imagen, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)

# Linea
# img = cv2.line(img, pt1(x,y), pt2, color, grosorlinea(thickness), tipolinea(lineType))
linea = cv2.line(imagen, (int(1070/2),int(194/2)), (int(1152/2),int(461/2)), (0,255,0), thickness = 5, lineType = cv2.LINE_AA)

# Circulo
# img = cv2.circle(img, pt1(x,y), radio, color, grosorlinea(thickness), tipolinea(lineType))
circulo = cv2.circle(imagen, (int(1080/2),int(185/2)), 70, (255,255,0), thickness = 1, lineType = cv2.LINE_AA)

# Rectangulo
# img = cv2.rectangle(img, pt1(x,y), pt2, color,grosorlinea(thickness),tipolinea(lineType))
rectangulo = cv2.rectangle(imagen, (int(1010/2),int(425/2)), (int(1381/2),int(566/2)), (255,0,255), thickness = 3, lineType = cv2.LINE_AA)

# Texto
# img = cv2.puText(img, texto, pt1(x,y), tipo letra, tam letra , color, grosorlinea(thickness), tipolinea(lineType))
texto = 'ROBOT DETECTADO'
tpletra = cv2.FONT_ITALIC
tmletra = 1.1
color = (0,255,0)
grosor = 2
texto = cv2.putText(imagen, texto, (int(995/2),int(650/2)), tpletra, tmletra, color, grosor)

# Mostramos imagenes
cv2.imshow('IMAGEN', imagen)
cv2.waitKey(0)