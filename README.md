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
Ensure you have Python 3.10+ installed. You will also need **Git LFS** to pull the large model weights file (`.pth`) properly.

#### Installing Git LFS:
*   **Linux (Debian/Ubuntu)**:
    ```bash
    sudo apt-get install git-lfs
    git lfs install
    ```
*   **Linux (CentOS/RHEL/Fedora)**:
    ```bash
    sudo dnf install git-lfs
    git lfs install
    ```
*   **Linux (Arch)**:
    ```bash
    sudo pacman -S git-lfs
    git lfs install
    ```
*   **Windows**:
    *   Download and run the installer from the official [git-lfs.com](https://git-lfs.com) website, or install via **winget**:
        ```powershell
        winget install github.git-lfs
        ```
    *   Initialize it in your terminal:
        ```bash
        git lfs install
        ```

### 2. Clone and Pull Weights
Clone the repository and pull the large model weights:
```bash
git clone <repository-url>
cd gtsrb-alexnet-classifier
git lfs pull
```

### 3. Install Dependencies
Install all required Python packages:
*   **Linux / macOS**:
    ```bash
    pip3 install -r requirements.txt
    ```
*   **Windows**:
    ```powershell
    pip install -r requirements.txt
    ```

### 4. Run the Gradio App Locally
Start the local FastAPI/Gradio server:
*   **Linux / macOS**:
    ```bash
    python3 app.py
    ```
*   **Windows**:
    ```powershell
    python app.py
    ```
Once running, open your browser and navigate to `http://localhost:7860` to access the classifier interface.

### 5. Generate Presentation Assets
To rebuild or update the presentation slide deck and speaker notes:
*   **Linux / macOS**:
    ```bash
    # Rebuild PowerPoint slides
    python3 generate_pptx.py
    
    # Compile presenter script/speaker notes to PDF
    python3 convert_script_to_pdf.py
    ```
*   **Windows**:
    ```powershell
    # Rebuild PowerPoint slides
    python generate_pptx.py
    
    # Compile presenter script/speaker notes to PDF
    python convert_script_to_pdf.py
    ```

*Note: Generating the presenter script PDF requires a working LaTeX installation (e.g., `pdflatex` added to system PATH). On Linux, install `texlive-latex-base` and `texlive-latex-recommended`. On Windows, install [MiKTeX](https://miktex.org) or TeX Live for Windows.*


