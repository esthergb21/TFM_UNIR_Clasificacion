# pylint: disable=no-member
# pyright: reportGeneralTypeIssues=false
import os
import cv2  # type: ignore
import numpy as np
import torch
import torch.nn as nn
from PIL import Image
from torchvision import models, transforms

_G_GRADIENTS = None
_G_ACTIVATIONS = None

def hook_backward(module, grad_input, grad_output):
    global _G_GRADIENTS
    if grad_output and len(grad_output) > 0:
        _G_GRADIENTS = grad_output[0]

def hook_forward(module, input_tensor, output_tensor):
    global _G_ACTIVATIONS
    _G_ACTIVATIONS = output_tensor

def generar_mapa_gradcam(filepath, modelo_seleccionado, pred_idx, upload_folder, filename):
    global _G_GRADIENTS, _G_ACTIVATIONS
    
    _G_GRADIENTS = None
    _G_ACTIVATIONS = None
    
    if modelo_seleccionado == 'efficientnet':
        model = models.efficientnet_b0()
        model.classifier[1] = nn.Linear(model.classifier[1].in_features, 7)
        model.load_state_dict(torch.load('pesos_efficientnet.pth', map_location='cpu'))
        target_layer = model.features[7]
    else:
        model = models.resnet50(weights=None)
        model.fc = nn.Linear(model.fc.in_features, 7)
        model.load_state_dict(torch.load('pesos_resnet50.pth', map_location='cpu'))
        target_layer = model.layer4

    model.eval()
    
    h_f = target_layer.register_forward_hook(hook_forward)
    h_b = target_layer.register_full_backward_hook(hook_backward)
    
    tx = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    img = Image.open(filepath).convert('RGB')
    img_resized = img.resize((224, 224))
    tensor_in = tx(img_resized).unsqueeze(0)
    tensor_in.requires_grad_()
    
    out = model(tensor_in)
    
    model.zero_grad()
    class_loss = out[0, pred_idx]
    class_loss.backward()
    
    h_f.remove()
    h_b.remove()
    
    if _G_GRADIENTS is None or _G_ACTIVATIONS is None:
        return ""
        
    pooled_gradients = torch.mean(_G_GRADIENTS, dim=[0, 2, 3], keepdim=True)
    heatmap = torch.mean(_G_ACTIVATIONS * pooled_gradients, dim=1).squeeze()
    heatmap = np.maximum(heatmap.detach().cpu().numpy(), 0)
    
    max_val = np.max(heatmap)
    if max_val != 0:
        heatmap /= max_val
        
    heatmap = np.uint8(255 * heatmap)
    heatmap_resized = cv2.resize(heatmap, (224, 224))
    heatmap_colored = cv2.applyColorMap(heatmap_resized, cv2.COLORMAP_JET)
    heatmap_colored = cv2.cvtColor(heatmap_colored, cv2.COLOR_BGR2RGB)
    
    img_cv = np.array(img_resized)
    superimposed_img = heatmap_colored * 0.4 + img_cv * 0.6
    superimposed_img = np.clip(superimposed_img, 0, 255).astype(np.uint8)
    
    nombre_gradcam = "gradcam_" + filename
    ruta_guardado = os.path.join(upload_folder, nombre_gradcam)
    
    cv2.imwrite(ruta_guardado, cv2.cvtColor(superimposed_img, cv2.COLOR_RGB2BGR))
    
    return nombre_gradcam