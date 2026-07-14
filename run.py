import os
from flask import Flask, render_template, request, redirect
from modelo_efficientnet import predecir_efficientnet
from modelo_resnet50 import predecir_resnet
from gradcam import generar_mapa_gradcam

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CLASES = {
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
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            modelo_seleccionado = request.form.get('modelo')
            
            if modelo_seleccionado == 'efficientnet':
                idx_pred, confianza = predecir_efficientnet(filepath)
                resultado_prediccion = CLASES[idx_pred]
            else:
                idx_pred, confianza = predecir_resnet(filepath)
                resultado_prediccion = CLASES[idx_pred]
            
            nombre_gradcam = generar_mapa_gradcam(filepath,
                                                  modelo_seleccionado,
                                                  idx_pred,
                                                  app.config['UPLOAD_FOLDER'],
                                                  file.filename)
            
            return render_template('index.html', 
                                   imagen_subida=filepath, 
                                   imagen_gradcam=nombre_gradcam,
                                   prediccion=resultado_prediccion, 
                                   confianza=confianza,
                                   modelo=modelo_seleccionado)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)