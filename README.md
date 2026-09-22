````markdown
# 🌱 Digital KrishiVaani — Plant Disease Detection CNN

An AI-powered plant disease detection system developed as part of the **Digital KrishiVaani** project.

The system uses a **Convolutional Neural Network (CNN)** to analyze plant leaf images and classify them into **39 supported plant disease/health classes**.

---

## 🚀 Project Overview

Digital KrishiVaani's Plant Disease Detection module is designed to help identify potential crop diseases from plant leaf images.

The system accepts an image, processes it using a trained CNN model, and generates a disease classification result.

### Core Workflow

```text
Plant Leaf Image
       ↓
Image Preprocessing
       ↓
CNN Model
       ↓
Disease Classification
       ↓
Prediction Result
````

---

## 🧠 CNN Model

The project uses a deep CNN architecture consisting of multiple:

* Convolutional Layers
* ReLU Activation
* Batch Normalization
* Max Pooling
* Dropout
* Fully Connected / Linear Layers

### Model Specifications

| Specification              |      Value |
| -------------------------- | ---------: |
| Input Image Size           |  224 × 224 |
| Output Classes             |         39 |
| Total Parameters           | 52,595,399 |
| Approx. Parameters         | 5.26 Crore |
| Trainable Parameters       | 52,595,399 |
| Non-Trainable Parameters   |          0 |
| Framework                  |    PyTorch |
| Model Format               |      `.pt` |
| Parameter Size             |  200.64 MB |
| Estimated Total Model Size |  345.17 MB |

---

## 📊 Model Performance

The current trained model achieved the following accuracy:

| Metric              | Accuracy |
| ------------------- | -------: |
| Training Accuracy   |    96.7% |
| Validation Accuracy |    98.7% |
| Test Accuracy       |    98.9% |

> Accuracy values are based on the current training and evaluation experiment and may vary depending on dataset split, preprocessing, augmentation, and evaluation conditions.

---

## 🏗️ Project Structure

```text
DKV-Model-Train/
│
├── app.py
├── model.py
│
├── model/
│   └── plant_disease_model_1_latest.pt
│
├── frontend/
│   ├── images/
│   │   └── OUR LOGO.png
│   └── index (1).html
│
├── .gitignore
├── .gitattributes
└── README.md
```

---

## ⚙️ Technologies Used

### Machine Learning

* Python
* PyTorch
* Convolutional Neural Network (CNN)
* Image Classification
* Batch Normalization
* ReLU
* Max Pooling
* Dropout

### Backend

* FastAPI
* Uvicorn
* Python

### Frontend

* HTML
* CSS
* JavaScript

### Version Control

* Git
* GitHub
* Git Large File Storage (Git LFS)

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/manshirai09/DKV-Model-Train-.git
```

### 2. Navigate to the Project

```bash
cd DKV-Model-Train-
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server using:

```bash
uvicorn app:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

### API Documentation

Interactive Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative API documentation using ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## 📡 API Prediction Flow

The backend processes plant leaf images through the following pipeline:

```text
Image Upload
      ↓
FastAPI API
      ↓
Image Preprocessing
      ↓
CNN Model Inference
      ↓
39-Class Classification
      ↓
Prediction Result
```

---

## 🔬 Model Architecture

Simplified CNN architecture:

```text
Input Image
224 × 224 RGB
      ↓
Convolution
      ↓
ReLU
      ↓
Batch Normalization
      ↓
Convolution
      ↓
ReLU
      ↓
Batch Normalization
      ↓
Max Pooling
      ↓
Convolution Blocks
      ↓
Max Pooling
      ↓
Dropout
      ↓
Fully Connected Layer
1024 Neurons
      ↓
ReLU
      ↓
Dropout
      ↓
Output Layer
39 Classes
```

---

## 📈 Training Results

```text
Training Accuracy    : 96.7%
Validation Accuracy  : 98.7%
Test Accuracy        : 98.9%

Total Parameters     : 52,595,399
Trainable Parameters : 52,595,399
Output Classes       : 39
```

---

## 💾 Model Storage

The trained CNN model is larger than the standard GitHub file limit, so **Git LFS (Git Large File Storage)** is used.

Model:

```text
model/plant_disease_model_1_latest.pt
```

To work with the model after cloning the repository:

```bash
git lfs install
git lfs pull
```

---

## 🌾 Plant Disease Detection

The trained model is designed to classify plant leaf images into **39 supported classes**.

The model can be integrated into the Digital KrishiVaani platform to provide AI-assisted crop health information to farmers.

---

## 🔄 Future Improvements

* [ ] Improve disease classification accuracy
* [ ] Add prediction confidence score
* [ ] Add disease-specific advisory
* [ ] Add treatment recommendations
* [ ] Add multilingual farmer support
* [ ] Add voice-based interaction through VAANI
* [ ] Integrate weather-based disease risk
* [ ] Add crop-specific recommendations
* [ ] Integrate with the Digital KrishiVaani platform
* [ ] Deploy the AI inference API
* [ ] Optimize model size and inference speed
* [ ] Validate the model using real-world field images

---

## 🌱 Digital KrishiVaani

This CNN model is part of **Digital KrishiVaani**, an agricultural technology project focused on providing AI-powered agricultural advisory and crop health assistance.

The larger Digital KrishiVaani ecosystem aims to combine:

* AI-based crop intelligence
* Plant disease detection
* Agricultural advisory
* Weather intelligence
* Multilingual interaction
* Voice-based assistance
* Farmer-focused digital services

---

## ⚠️ Disclaimer

This system is an **AI-assisted plant disease classification tool** and should not be considered a replacement for professional agricultural or plant pathology advice.

Prediction performance may be affected by:

* Image quality
* Lighting conditions
* Camera quality
* Crop variety
* Disease stage
* Background noise
* Differences between training data and real-world field images

---

## 👩‍💻 Developer

**Manshi Rai**

Digital KrishiVaani

AI/ML • Backend • Software Development

---

## 📄 License

License information will be added in a future release.






