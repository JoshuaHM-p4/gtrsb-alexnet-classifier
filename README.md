---
title: GTSRB AlexNet Traffic Sign Classifier
emoji: 🚦
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 6.2.0
app_file: app.py
pinned: false
---

# GTSRB AlexNet Traffic Sign Classifier

This is a demonstration repository for a fine-tuned AlexNet model on the German Traffic Sign Recognition Benchmark (GTSRB) dataset. It uses a Gradio app to provide:

1. Traffic sign image classification (43 classes).
2. Prediction confidence display.
3. Visualization of the model architecture and transfer learning setup.

## Project Structure

*   `app.py`: The Gradio web application for interactive image classification.
*   `requirements.txt`: Python package dependencies.
*   `alexnet_gtsrb_finetuned.pth`: Fine-tuned PyTorch model weights (tracked via Git LFS).
*   `docu/`: Contains research paper drafts (`main.tex` and compiled `main.pdf`), PowerPoint presentation (`gtsrb_alexnet_presentation.pptx`), and presenter notes (`presentation_script.md` and compiled `presentation_script.pdf`).
*   `generate_pptx.py`: Python script to programmatically build the PowerPoint presentation.
*   `convert_script_to_pdf.py`: Python script to parse speaker notes and compile them to PDF.

## Setup Instructions

### 1. Prerequisites
Ensure you have Python 3.10+ installed. You will also need `git-lfs` to pull the large model weights file (`.pth`) properly.

```bash
# Install Git LFS if not already installed (Debian/Ubuntu)
sudo apt-get install git-lfs
git lfs install
```

### 2. Clone and Pull Weights
Clone the repository and pull the LFS weights:
```bash
git clone <repository-url>
cd gtsrb-alexnet-classifier
git lfs pull
```

### 3. Install Dependencies
Install all required Python libraries:
```bash
pip install -r requirements.txt
```

### 4. Run the Gradio App Locally
To start the interactive web application:
```bash
python app.py
```
Open your browser and navigate to `http://localhost:7860` to access the classifier interface.

### 5. Generate Presentation Assets
To modify or regenerate the presentation slides and notes:
```bash
# Build the PowerPoint presentation slide deck
python generate_pptx.py

# Build the speaker notes PDF
python convert_script_to_pdf.py
```

