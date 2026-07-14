import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

def predecir_resnet(image_path):
    # 1. Configurar dispositivo
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # 2. Reconstruir la arquitectura exacta del notebook
    model = models.resnet50(weights=None) 
    in_features = model.fc.in_features
    model.fc = nn.Linear(in_features, 7)
    
    # 3. Cargar los pesos guardados
    model.load_state_dict(torch.load('pesos_resnet50.pth', map_location=device))
    model = model.to(device)
    model.eval()
    
    # 4. Transformaciones idénticas a las de validación del notebook
    val_tx = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # 5. Procesar la imagen
    img = Image.open(image_path).convert('RGB')
    img_t = val_tx(img).unsqueeze(0).to(device)
    
    # 6. Predicción e inferencia de confianza
    with torch.no_grad():
        outs = model(img_t)
        probabilities = torch.softmax(outs, dim=1)
        confianza, pred_idx = torch.max(probabilities, 1)
        
    return pred_idx.item(), round(confianza.item() * 100, 2)