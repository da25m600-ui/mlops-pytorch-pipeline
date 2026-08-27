import io
import torch
import torch.nn.functional as F
from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image
from torchvision import transforms
from src.model import get_model

app = FastAPI()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = None

CLASSES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

'''
@app.on_event("startup")
def load_checkpoint():
    global model
    model = get_model(num_classes=10)
    try:
        model.load_state_dict(torch.load("./models/best_model.pth", map_location=device))
        model.to(device)
        model.eval()
    except Exception:
        model = None
'''

@app.on_event("startup")
def load_checkpoint():
    global model
    model = get_model(num_classes=10)
    try:
        # Pull checkpoint explicitly out of the external volume binding mount
        model.load_state_dict(torch.load("/app/checkpoints/best_model.pth", map_location=device))
        model.to(device)
        model.eval()
    except Exception:
        model = None

@app.get("/health")
def health_check():
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "ok"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert("RGB")
    
    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
    ])
    tensor = transform(image).unsqueeze(0).to(device)
    
    with torch.no_grad():
        outputs = model(tensor)
        probs = F.softmax(outputs, dim=1)[0]
        
    return {CLASSES[i]: float(probs[i]) for i in range(len(CLASSES))}
