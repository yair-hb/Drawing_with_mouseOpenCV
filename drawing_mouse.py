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
#se debe crear el ciclo que lea los frames de la captura
while True:
    ret,frame = cap.read()
    if ret == False:
        break
    frame = cv2.flip(frame,1)

frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

if imAux is None: imAux = np.zeros(frame.shape, dtype=np.uint8)

#------SECCION SUPERIOR ----------
#cuadros dibujados en la parte superior de la ventana
cv2.rectangle(frame,(0,0),(50,50),colorAmarillo,grosorAmarillo)
cv2.rectangle(frame,(50,0),(100,50),colorRosa,grosorRosa)
cv2.rectangle(frame,(100,0),(150,50),colorVerde,grosorVerde)
cv2.rectangle(frame,(150,0),(200,50),colorAzul,grosorAzul)

#rectanguloSuperior para limpiar la pantalla
cv2.rectangle(frame,(300,0),(400,50),limpiarPantalla,1)
cv2.putText(frame,"LIMPIAR",(320,20),(6,0.6,limpiarPantalla,1,cv2.LINE_AA))

#cuadros dibujados en la parte sup derecha(grosor del marcador)
cv2.rectangle(frame,(490,0),(540,50),(0,0,0),grosorMini)
cv2.circle(frame, (515,25),3,(0,0,0),-1)
cv2.rectangle(frame,(540,0),(590,50),(0,0,0),grosorMedium)
cv2.circle(frame,(565,25),7,(0,0,0),-1)
cv2.rectangle(frame,(590,0),(640,50),(0,0,0),grosorBig)
cv2.circle(frame,(615,25),11,(0,0,0),-1)

cap.release()
cv2.destroyAllWindows()