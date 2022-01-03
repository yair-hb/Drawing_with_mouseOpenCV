import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

azulbajo= np.array([75,185,88],np.uint8)
azulalto= np.array([112,255,255],np.uint8)

#colores del lapiz 
colorAzul = (255,113,82)
colorAmarillo = (89,222,255)
colorRosa = (128,0,255)
colorVerde = (0,255,36)
limpiarPantalla = (29,112,246) #solo para mostrar el cuadro

#grosor de linea recuadros superior
grosorAzul = 6
grosorAmarillo = 2
grosorRosa = 2
grosorVerde = 2

#grosor de la linea  de recuadros  superior derecha
grosorMini = 6
grosorMedium = 1
grosorBig = 1

#---------------- VARIABLES QUE TENDRA EL MARCADOR AL INICIO ----------
color = colorAzul
grosor = 3
x1 = None
y1 = None
imAux = None

while True:
    ret,frame = cap.read()
    if ret == False:
        break
    frame = cv2.flip(frame,1)
