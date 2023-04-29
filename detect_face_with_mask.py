 #. importe a biblioteca opencv
import cv2
  
# defina um objeto de captura de vídeo
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture o vídeo quadro a quadro
    ret, frame = vid.read()
  
    # Exiba o quadro resultante
    cv2.imshow('quadro', frame)
      
    # Saia da tela com a barra de espaço
    key = cv2.waitKey(1)
    
    if key == 32:
        break
  
# Após o loop, libere o objeto capturado
vid.release()

# Destrua todas as janelas
cv2.destroyAllWindows()