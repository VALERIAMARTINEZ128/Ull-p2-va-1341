
# Valeria Yaretzi - NC 1341
import cv2
from pathlib import Path

# Buscar desde la carpeta donde está este código
BASE = Path(__file__).resolve().parent

# Buscar images.jfif en el proyecto y sus carpetas
archivos = list(BASE.parent.rglob("images.jfif"))
archivos += list(BASE.rglob("images.jfif"))

# Eliminar rutas duplicadas
archivos = list(dict.fromkeys(archivos))

if archivos:
    ruta = archivos[0]
    print("Imagen encontrada:", ruta)

    imagen = cv2.imread(str(ruta))

    if imagen is not None:
        print("Imagen cargada correctamente")
        cv2.imshow("Congelador - NC 1341", imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("El archivo existe, pero OpenCV no puede leerlo.")
        print("Vuelve a guardar la imagen como JPEG o PNG.")
else:
    print("No se encontro images.jfif.")
    print("Revisa en que carpeta se guardo la imagen.")
