## ⚠️ Nota importante para el correcto funcionamiento del código

Debido a las limitaciones de tamaño de archivos que establece GitHub para el almacenamiento en el repositorio, los archivos con los pesos de los modelos entrenados (".pth") correspondientes a las redes EfficientNet-B0 y ResNet50 no están subidos de forma directa en este repositorio.

Para que la aplicación web funcione correctamente en su entorno local y pueda realizar las inferencias y diagnósticos, sigue estos sencillos pasos:

1. **Descarga los archivos de pesos** desde el siguiente enlace de Google Drive:
   * 🔗 [Descargar pesos de los modelos (.pth)](https://drive.google.com/file/d/1PLuQnStfpHGoFsIDLfTAAugirSt6P0Vz/view?usp=drive_link)

2. **Coloca los archivos** descargados dentro de la carpeta del proyecto en la ruta correspondiente para que el backend de Flask pueda cargarlos al iniciarse la aplicación.
