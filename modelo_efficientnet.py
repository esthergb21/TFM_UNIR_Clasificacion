import torch
import torchvision.models as models
import torchvision.transforms as transforms
import torch.nn as nn
from PIL import Image

model = models.efficientnet_b0()
model.classifier[1] = nn.Linear(model.classifier[1].in_features, 7)

# Cambiamos 'modelo_skin.pth' por el nuevo nombre exacto:
model.load_state_dict(torch.load('pesos_efficientnet.pth', map_location='cpu'))
model.eval()

tx = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def predecir_efficientnet(ruta_imagen):
    img = Image.open(ruta_imagen).convert('RGB')
    tensor = tx(img).unsqueeze(0)
    
    with torch.no_grad():
        out = model(tensor)
        probabilidades = torch.nn.functional.softmax(out[0], dim=0)
        pred_idx = out.argmax(dim=1).item()
        
    return pred_idx, round(probabilidades[pred_idx].item() * 100, 2)