import os
from flask import Flask, render_template, request, redirect
from modelo_efficientnet import predecir_efficientnet

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

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
                resultado_prediccion, confianza = "Modelo ResNet no conectado aún", 0.0
            
            return render_template('index.html', 
                                   imagen_subida=filepath, 
                                   prediccion=resultado_prediccion, 
                                   confianza=confianza,
                                   modelo=modelo_seleccionado)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)