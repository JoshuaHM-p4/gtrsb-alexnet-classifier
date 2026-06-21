import gradio as gr
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models, transforms
from PIL import Image
import os

# Class mapping dictionary for GTSRB
CLASSES = {
    0: "Speed limit (20km/h)",
    1: "Speed limit (30km/h)",
    2: "Speed limit (50km/h)",
    3: "Speed limit (60km/h)",
    4: "Speed limit (70km/h)",
    5: "Speed limit (80km/h)",
    6: "End of speed limit (80km/h)",
    7: "Speed limit (100km/h)",
    8: "Speed limit (120km/h)",
    9: "No passing",
    10: "No passing for vehicles over 3.5 metric tons",
    11: "Right-of-way at the next intersection",
    12: "Priority road",
    13: "Yield",
    14: "Stop",
    15: "No vehicles",
    16: "Vehicles over 3.5 metric tons prohibited",
    17: "No entry",
    18: "General caution",
    19: "Dangerous curve to the left",
    20: "Dangerous curve to the right",
    21: "Double curve",
    22: "Bumpy road",
    23: "Slippery road",
    24: "Road narrows on the right",
    25: "Road work",
    26: "Traffic signals",
    27: "Pedestrians",
    28: "Children crossing",
    29: "Bicycles crossing",
    30: "Beware of ice/snow",
    31: "Wild animals crossing",
    32: "End of all speed and passing limits",
    33: "Turn right ahead",
    34: "Turn left ahead",
    35: "Ahead only",
    36: "Go straight or right",
    37: "Go straight or left",
    38: "Keep right",
    39: "Keep left",
    40: "Roundabout mandatory",
    41: "End of no passing",
    42: "End of no passing by vehicles over 3.5 metric tons"
}

# Preprocessing transforms (matches test split transforms)
preprocess = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Load model
model_path = "alexnet_gtsrb_finetuned.pth"
if not os.path.exists(model_path):
    # Try looking in parent folder in case app is executed in app/ directory
    model_path = "../alexnet_gtsrb_finetuned.pth"

model = models.alexnet(weights=None)
num_ftrs = model.classifier[6].in_features
model.classifier[6] = nn.Linear(num_ftrs, 43)

try:
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")

model.eval()

def predict(image):
    if image is None:
        return {}
    
    # Preprocess image
    tensor = preprocess(image).unsqueeze(0)
    
    # Predict
    with torch.no_grad():
        output = model(tensor)
        probabilities = F.softmax(output, dim=1)[0]
    
    # Create label dict for top 5 predictions
    top_prob, top_indices = torch.topk(probabilities, 5)
    return {CLASSES[int(idx)]: float(prob) for prob, idx in zip(top_prob, top_indices)}

# Description text for model architecture
architecture_explanation = """
## Model Architecture Explanation: Adapted AlexNet

This application uses the **AlexNet** Convolutional Neural Network architecture fine-tuned on the **German Traffic Sign Recognition Benchmark (GTSRB)** dataset using transfer learning.

### 1. Feature Extraction Layers (Frozen)
The convolutional layers of the network are pre-trained on the ImageNet dataset and kept **frozen** during fine-tuning. This preserves the network's ability to extract general image features like edges, curves, colors, and textures without needing extensive training resources.
* **Conv 1**: 64 kernels ($11 \\times 11$, stride 4, padding 2) + ReLU + MaxPool ($3 \\times 3$, stride 2)
* **Conv 2**: 192 kernels ($5 \\times 5$, stride 1, padding 2) + ReLU + MaxPool ($3 \\times 3$, stride 2)
* **Conv 3**: 384 kernels ($3 \\times 3$, stride 1, padding 1) + ReLU
* **Conv 4**: 256 kernels ($3 \\times 3$, stride 1, padding 1) + ReLU
* **Conv 5**: 256 kernels ($3 \\times 3$, stride 1, padding 1) + ReLU + MaxPool ($3 \\times 3$, stride 2)

### 2. Adaptive Average Pooling
Rescales the outputs from the convolutional block to a fixed size of $6 \\times 6$ across all 256 feature maps, producing an intermediate vector of size $9,216$ when flattened.

### 3. Classifier Head (Modified & Trained)
The classifier block contains three fully connected layers with Dropout regularization ($p=0.5$) applied between them to combat overfitting. The final layer was modified from its original $1,000$-class output (ImageNet) to **43 classes** representing the traffic sign categories of GTSRB.
* **Linear 1**: $9,216 \\rightarrow 4,096$ units + ReLU
* **Linear 2**: $4,096 \\rightarrow 4,096$ units + ReLU
* **Linear 3 (Modified)**: $4,096 \\rightarrow 43$ units (Traffic Sign classes) + Softmax Activation
"""

# Define Gradio layout
with gr.Blocks() as demo:
    gr.Markdown("# 🚦 GTSRB Traffic Sign Classifier (AlexNet)")
    gr.Markdown("An interactive research tool for classifying traffic signs from the German Traffic Sign Recognition Benchmark dataset using fine-tuned AlexNet.")
    
    with gr.Tabs():
        with gr.Tab("Classifier"):
            with gr.Row():
                with gr.Column():
                    input_img = gr.Image(type="pil", label="Upload Traffic Sign Image")
                    btn = gr.Button("Classify Image", variant="primary")
                with gr.Column():
                    output_label = gr.Label(num_top_classes=5, label="Predicted Class & Confidence Score")
            
            btn.click(predict, inputs=input_img, outputs=output_label)
            
        with gr.Tab("Architecture"):
            gr.Markdown(architecture_explanation)

demo.launch(theme=gr.themes.Soft(primary_hue="blue", secondary_hue="green"), ssr_mode=False)

