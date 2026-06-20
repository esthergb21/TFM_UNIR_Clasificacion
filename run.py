import os
from flask import Flask, render_template, request, redirect, url_for
# Si usas TensorFlow, descomenta la siguiente línea cuando lo instales:
# from tensorflow.keras.models import load_model
# import numpy as np

app = Flask(__name__)

# Configuración de la carpeta donde se guardarán temporalmente las imágenes subidas
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ==========================================
# 🤖 AQUÍ SE CARGARÁN TUS MODELOS DEL TFM
# ==========================================
# NOTA: Cargar los modelos aquí fuera evita que se recarguen en cada clic, 
# ahorrando memoria RAM y tiempo.
# MODELO_RESNET = load_model('modelos/resnet50_ham100000.h5')
# MODELO_EFFICIENT = load_model('modelos/efficientnet50_ham100000.h5')

# Diccionario de clases del dataset HAM100000 (ajusta según tus etiquetas)
CLASES_HAM100000 = {
    0: 'Queratosis actínica (akiec)',
    1: 'Carcinoma basocelular (bcc)',
    2: 'Lesión benigna de tipo queratosis (bkl)',
    3: 'Dermatofibroma (df)',
    4: 'Melanoma (mel)',
    5: 'Nevus melanocítico (nv)',
    6: 'Lesión vascular (vasc)'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 1. Verificar si el usuario subió un archivo
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            # 2. Guardar la imagen en el servidor de forma temporal
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # 3. Saber qué modelo seleccionó el usuario en la web
            modelo_seleccionado = request.form.get('modelo') # 'resnet' o 'efficientnet'
            
            # 4. PREPROCESAMIENTO Y PREDICCIÓN SIMULADA 
            # (Aquí irá el código para redimensionar la imagen e introducirla al modelo)
            resultado_prediccion = "Nevus melanocítico (nv)" # Simulación por ahora
            confianza = 94.5 # Simulación por ahora
            
            return render_template('index.html', 
                                   imagen_subida=filepath, 
                                   prediccion=resultado_prediccion, 
                                   confianza=confianza,
                                   modelo=modelo_seleccionado)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)