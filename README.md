## ⚠️ Nota importante para el correcto funcionamiento del código

Debido a las limitaciones de tamaño de archivos que establece GitHub para el almacenamiento en el repositorio, los archivos con los pesos de los modelos entrenados (".pth") correspondientes a las redes EfficientNet-B0 y ResNet50 no están subidos de forma directa en este repositorio.

Para que el código de la aplicación web funcione correctamente en su entorno local, siga estos sencillos pasos:

1. **Descargue los archivos de pesos** desde el siguiente enlace de Google Drive:
   * 🔗 [Descargar pesos de los modelos (.pth)](https://drive.google.com/drive/folders/1xBVrNfdy6yj-XJxDGIf4iU19oNDpyZJd?usp=drive_link)

2. **Coloque los archivos** descargados dentro de la carpeta del proyecto en la ruta correspondiente para que el backend de Flask pueda cargarlos al iniciarse la aplicación.
