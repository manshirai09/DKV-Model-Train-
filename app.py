from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from PIL import Image
import torch
import torchvision.transforms.functional as TF

from model import CNN


app = FastAPI(
    title="Plant Disease Detection API",
    description="Plant disease prediction using PyTorch CNN",
    version="1.0"
)

# --------------------------------
# CORS (allow the HTML frontend, opened from any origin/port, to call this API)
# --------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------
# Device
# --------------------------------

device = torch.device("cpu")


# --------------------------------
# Classes
# --------------------------------

class_names = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",

    "Blueberry___healthy",

    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",

    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",

    "Orange___Haunglongbing_(Citrus_greening)",

    "Peach___Bacterial_spot",
    "Peach___healthy",

    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",

    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",

    "Raspberry___healthy",

    "Soybean___healthy",

    "Squash___Powdery_mildew",

    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",

    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]


# --------------------------------
# Load Model
# --------------------------------

model = CNN(39)

model.load_state_dict(
    torch.load(
        "model/plant_disease_model_1_latest.pt",
        map_location=device
    )
)

model.to(device)

model.eval()


# --------------------------------
# Routes
# --------------------------------

@app.get("/")
def home():
    return {
        "message": "Plant Disease Detection API is running"
    }


@app.get("/ui")
def ui():
    """Serves the frontend directly from the backend, so you can just
    open http://127.0.0.1:8000/ui instead of running a separate server."""
    return FileResponse("index.html")


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    image = Image.open(file.file).convert("RGB")
    image = image.resize((224, 224))

    input_data = TF.to_tensor(image)
    input_data = input_data.view(-1, 3, 224, 224)
    input_data = input_data.to(device)

    with torch.no_grad():
        output = model(input_data)
        prediction = torch.argmax(output, dim=1).item()

    raw_label = class_names[prediction]

    if "___" in raw_label:
        plant_raw, disease_raw = raw_label.split("___", 1)
    else:
        plant_raw, disease_raw = raw_label, ""

    plant = plant_raw.replace("_", " ").strip()
    disease = disease_raw.replace("_", " ").strip()
    is_healthy = disease.lower() == "healthy" or disease == ""

    return {
        "filename": file.filename,
        "class_index": prediction,
        "prediction": raw_label,
        "plant": plant,
        "disease": "No disease detected" if is_healthy else disease,
        "is_healthy": is_healthy
    }