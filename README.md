# Aplicación Web de apoyo a la clasificación de lesiones cutáneas

Este repositorio contiene el código principal, la interfaz de usuario en Flask y los scripts de soporte para la ejecución local de la aplicación web de apoyo al diagnóstico y mapas de calor (Grad-CAM).

---

## 1. Descarga del Proyecto (Estructura de Carpetas)

Antes de realizar cualquier otra acción, es indispensable que disponga de toda la estructura de archivos localmente en su equipo. Para ello, descargue el directorio completo en formato comprimido haciendo clic en el botón verde superior derecho `Code` -> `Download ZIP`, y extraiga su contenido en una carpeta local de su ordenador.

---

## 2. ⚠️ Importante: Descarga y Colocación de los Modelos (.pth)

Debido a las limitaciones de tamaño de archivos que establece GitHub para el almacenamiento en el repositorio, los archivos con los pesos de los modelos entrenados (`.pth`) correspondientes a las redes EfficientNet-B0 y ResNet50 no están subidos de forma directa en este código fuente.

Una vez que haya descargado o clonado el proyecto en su equipo local (Paso 1), siga estas instrucciones para que la aplicación funcione correctamente:

1. **Descargue los archivos de pesos** desde el siguiente enlace de Google Drive:
   * 🔗 [Descargar pesos de los modelos (.pth)](https://drive.google.com/drive/folders/1xBVrNfdy6yj-XJxDGIf4iU19oNDpyZJd?usp=drive_link)

2. **Coloque ambos archivos** descargados directamente en la raíz de la carpeta del proyecto (`proyecto1`), de manera que queden situados en el mismo nivel que el archivo `run.py`. Esto permitirá que el backend de Flask pueda localizarlos y cargarlos correctamente al iniciarse la aplicación.

---

## 3. Instrucciones de Ejecución en Visual Studio Code (VS Code)

Para ejecutar la aplicación web localmente utilizando VS Code, siga estos pasos:

1. **Abrir el proyecto:**
   * Abra VS Code.
   * Vaya a `Archivo` -> `Abrir carpeta...` (o `Open Folder...`) y seleccione la carpeta principal extraída de este repositorio (`proyecto1`).

2. **Seleccionar el intérprete de Python:**
   * Abra cualquier archivo `.py` (por ejemplo, `run.py`).
   * En la esquina inferior derecha de VS Code (o pulsando `Ctrl + Shift + P` y buscando *Python: Select Interpreter*), asegúrese de tener seleccionado su intérprete de Python activo.

3. **Instalar las dependencias:**
   * Abra la terminal integrada de VS Code presionando las teclas ``Ctrl + ` `` (o vaya al menú superior: `Terminal` -> `Nueva terminal`).
   * En la terminal que se despliegue en la parte inferior, ejecute el siguiente comando para instalar de forma automatizada todas las librerías necesarias:
     ```bash
     pip install -r requirements.txt
     ```

4. **Arrancar la aplicación:**
   * En esa misma terminal de VS Code, inicie el servidor de Flask ejecutando:
     ```bash
     python run.py
     ```
   * Abra su navegador web e introduzca la dirección que le aparecerá en pantalla, o haga clic sobre ella presionando `Ctrl`: `http://127.0.0.1:5000/`
