# Presenter Script: Traffic Sign Classification Using AlexNet (26-Slide Outline)

This document contains the detailed presenter script and speaker notes for the **German Traffic Sign Classification using AlexNet** project. The outline and slide headings here correspond exactly to the slides in the updated `gtsrb_alexnet_presentation.pptx`.

---

## Slide 1: Title Slide
**Slide Heading:** *Image Classification Using CNN Architectures: AlexNet Classification on German Traffic Sign Recognition Benchmark (GTSRB)*

### Presenter Speech:
> "Good day everyone. Welcome to our final project presentation for CMPE 362 Pattern Recognition. We are Group 1: Carlos Jerico Dela Torre, Joshua Mistal, and Aidan Tiu, working under the guidance of Professor Mon Arjay Malbog. 
> 
> Our research focuses on implementing and evaluating the AlexNet Convolutional Neural Network architecture for Traffic Sign Recognition using the GTSRB dataset. We will walk you through our objectives, methodology, evaluation metrics, and future recommendations."

---

## Slide 2: Project Overview & Executive Summary
**Slide Heading:** *Project Overview & Executive Summary*

### Presenter Speech:
> "To begin with our executive summary: Traffic Sign Recognition (TSR) is a critical perception module in modern Driver Assistance Systems (ADAS) and self-driving platforms. 
> 
> Our research utilizes a transfer learning approach with a pre-trained AlexNet CNN. We froze the convolutional layers to preserve low-level features and retrained only the customized classifier head to output predictions for the 43 target classes of the GTSRB dataset.
> 
> Our model achieved outstanding metrics: a final classification accuracy of **98.91%**, a macro-averaged F1-score of **0.9910**, and a macro-averaged ROC-AUC of **1.0000**. The pipeline successfully overcomes real-world environmental noise and severe dataset imbalance."

---

## Slide 3: Chapter 1: Introduction - Background & Problem Statement
**Slide Heading:** *Chapter 1: Background & Problem Statement*

### Presenter Speech:
> "Let's review the background and problem statement. Drivers and autonomous agents rely on traffic signs to negotiate safety guidelines. Standard computer vision models often struggle with physical noise like motion blur, dynamic shadows, and bad lighting.
> 
> Furthermore, the GTSRB dataset presents a severe class imbalance: some signs have thousands of training samples, while others have only a few hundred. Standard models trained on this data become biased toward majority classes. 
> 
> Finally, vehicle edge processors require computationally efficient models that process frames at high speed without wasting energy. This creates the need for a balanced, low-latency deep learning architecture."

---

## Slide 4: Chapter 1: Project Objectives
**Slide Heading:** *Chapter 1: Project Objectives*

### Presenter Speech:
> "To address these issues, we set three main objectives:
> 
> *   **Objective 1: Data Preprocessing.** Standardize input dimensions by scaling images to 256x256, center-cropping to a 224x224x3 shape, and applying channel normalization.
> *   **Objective 2: Architecture Adaptation.** Freeze convolutional layers of a pre-trained PyTorch AlexNet model and reconstruct the classifier head to map features to the 43 target output classes.
> *   **Objective 3: Model Evaluation.** Train the classifier head, apply early stopping to prevent overfitting, and evaluate performance using metrics like accuracy, precision, recall, and ROC-AUC."

---

## Slide 5: Chapter 2: Literature Review
**Slide Heading:** *Chapter 2: Literature Review*

### Presenter Speech:
> "Moving to Chapter 2, literature shows that early TSR systems relied on color segmentation and geometric matching, which were fragile in outdoor settings.
> 
> Sermanet and LeCun in 2011 demonstrated that Convolutional Neural Networks can exceed human-level classification performance on the benchmark. 
> 
> To improve efficiency, Ma et al. customized AlexNet specifically for TSR, using smaller convolution kernels to prevent overfitting. Recently, Arcos-Garcia et al. showed that while deeper networks like VGG or ResNet provide slight accuracy gains, AlexNet offers a superior speed-accuracy trade-off, making it ideal for edge computing."

---

## Slide 6: Chapter 2: CNN Architecture Overview
**Slide Heading:** *Chapter 2: CNN Architecture Overview*

### Presenter Speech:
> "Unlike standard neural networks that flatten images and destroy spatial structures, CNNs preserve local 2D relationships using sliding kernels.
> 
> Key CNN concepts include:
> *   **Local Receptive Fields:** sliding filters extract visual features like edges and curves.
> *   **Weight Sharing:** reusing kernel parameters dramatically reduces the training parameter count, preventing overfitting.
> *   **Hierarchical Layout:** early layers extract low-level geometry, while deeper layers extract high-level semantic abstractions."

---

## Slide 7: Table: CNN Basic Layers
**Slide Heading:** *CNN Structural Layer Summary*

### Presenter Speech:
> "Table 1 on the slide summarizes the basic structural layers of a CNN:
> *   **Convolutional Layers** apply kernel filters to generate spatial feature maps.
> *   **Activation (ReLU) Layers** introduce non-linearity to learn complex boundaries.
> *   **Pooling Layers** reduce spatial resolution, compute, and parameter overhead.
> *   **Fully Connected Layers** aggregate high-level features to output class logits."

---

## Slide 8: Chapter 2: AlexNet Architecture Details
**Slide Heading:** *Chapter 2: AlexNet Architecture Details*

### Presenter Speech:
> "AlexNet consists of 5 convolutional layers followed by 3 fully connected layers.
> 
> The PyTorch implementation standardizes the input grid to 224x224x3 using a padding of 2 in the first layer. 
> 
> To combat overfitting in the fully connected layers, the network applies Dropout regularization with a probability of 0.5. During training, half of the activations are randomly deactivated, promoting robust redundant features."

---

## Slide 9: Figure 1: AlexNet Architectural Layout Diagram (Dedicated Visual Slide)
**Slide Heading:** *Figure 1: AlexNet Architectural Layout Diagram*

### Presenter Speech:
> "Here, in Figure 1, you can see the complete architectural diagram of AlexNet. It illustrates the sequence of convolutional filters, pooling reductions, flattening, and fully connected classification layers that make up the network's processing pipeline."

---

## Slide 10: Chapter 3: Methodology Overview
**Slide Heading:** *Chapter 3: Methodology Overview*

### Presenter Speech:
> "Now, we will review Chapter 3: Methodology.
> 
> Our implementation was coded in Python 3 with CUDA GPU acceleration.
> *   We used **PyTorch and Torchvision** to model the network graphs and image transforms.
> *   **Scikit-Learn** generated our stratified dataset splits.
> *   **Matplotlib and Seaborn** plotted our evaluation metrics and performance curves."

---

## Slide 11: Figure 2: Sample Signs Across all 43 GTSRB Classes (Dedicated Visual Slide)
**Slide Heading:** *Figure 2: Sample Signs Across all 43 GTSRB Classes*

### Presenter Speech:
> "Figure 2 shows sample traffic signs across all 43 categories of the GTSRB dataset. It illustrates the wide variation in color, shape, borders, and symbols that the model must learn to classify."

---

## Slide 12: Figure 3: Class-wise Sample Distribution Heatmap (Dedicated Visual Slide)
**Slide Heading:** *Figure 3: Class-wise Sample Distribution Heatmap*

### Presenter Speech:
> "Figure 3 visualizes the class-wise sample distribution in the dataset. This highlights the severe class imbalance, showing that majority classes have thousands of samples while minority classes have only a few hundred."

---

## Slide 13: Chapter 3: Data Loading & Split
**Slide Heading:** *Chapter 3: Data Loading & Split*

### Presenter Speech:
> "To address this class imbalance, we pooled the training and testing datasets and performed a stratified 70% training, 15% validation, and 15% testing split.
> 
> Stratification ensures that minority classes are represented equally across all three splits, preventing bias. We loaded training data with dynamic shuffling, and kept validation and testing loaders static for reproducible metrics."

---

## Slide 14: Custom Dataset Implementation (Code Card Slide)
**Slide Heading:** *Methodology: PyTorch Dataset Class*

### Presenter Speech:
> "On this slide, you can see the code implementation of our custom `GTSRBDataset` class. It inherits from PyTorch's `Dataset` class, mapping relative paths and class IDs from our CSV metadata.
> 
> It converts all images to the RGB color space to ensure three-channel compatibility and applies the designated transformations."

---

## Slide 15: Chapter 3: Preprocessing & Augmentation
**Slide Heading:** *Chapter 3: Preprocessing & Augmentation*

### Presenter Speech:
> "To help the model generalize, we designed separate preprocessing pipelines:
> *   **Training Pipeline:** Scales images to 256x256, applies random rotation (up to 15°) to simulate camera tilt, and color jitter (0.2) to simulate lighting changes. It then center-crops to 224x224 and normalizes.
> *   **Validation/Test Pipeline:** Scales images to 256x256, center-crops directly to 224x224, and normalizes. We omit random rotations and color jitters to ensure clean and reproducible evaluation metrics."

---

## Slide 16: Chapter 3: Transfer Learning Setup
**Slide Heading:** *Chapter 3: Transfer Learning Setup*

### Presenter Speech:
> "Our transfer learning strategy is straightforward:
> *   **Freeze Feature Layers:** We disable gradients (`requires_grad=False`) on the pre-trained convolutional feature extraction layers, preserving ImageNet visual filters.
> *   **Classifier Head Swap:** We replace the final linear layer (index 6) with a new linear layer mapping 4,096 inputs to 43 output logits, training only these classification parameters."

---

## Slide 17: Model Customization and Freezing (Code Card Slide)
**Slide Heading:** *Methodology: Model Initialization*

### Presenter Speech:
> "This slide displays our PyTorch initialization code. It shows how the pre-trained weights are loaded, how convolutional parameters are frozen, and how the final linear classifier layer is modified and pushed to the GPU."

---

## Slide 18: Chapter 3: Training Process Configuration
**Slide Heading:** *Chapter 3: Training & Optimization Settings*

### Presenter Speech:
> "We optimized the model using **Cross Entropy Loss** and the **Adam optimizer** at a learning rate of **0.0001**, updating only the classifier weights.
> 
> We trained the model for a maximum of 15 epochs and integrated early stopping with a validation loss patience of 3. If validation loss failed to improve for three consecutive epochs, training would stop to prevent overfitting."

---

## Slide 19: Chapter 4: Results - Classification Summary
**Slide Heading:** *Chapter 4: Results - Classification Summary*

### Presenter Speech:
> "This brings us to Chapter 4: Results and Discussion. The model was evaluated on the unseen testing set.
> 
> The results show high sensitivity and specificity. The macro Precision of 0.9924 and Recall of 0.9899 confirm accurate predictions across all classes. The F1-score of 0.9910 indicates that the model successfully handles the dataset's class imbalance without bias toward heavily populated classes."

---

## Slide 20: Overall Performance Score Sheet (Table 2)
**Slide Heading:** *Overall Performance Score Sheet*

### Presenter Speech:
> "Table 2 summarizes our test metrics:
> *   **Test Accuracy:** **98.91%**
> *   **Precision (Macro Avg):** **0.9924**
> *   **Recall (Macro Avg):** **0.9899**
> *   **F1-Score (Macro Avg):** **0.9910**
> *   **ROC-AUC (Macro Avg):** **1.0000**"

---

## Slide 21: Figure 4: Loss/Accuracy Curves (Dedicated Visual Slide)
**Slide Heading:** *Figure 4: Training and Validation Loss/Accuracy History*

### Presenter Speech:
> "Figure 4 displays our training and validation curves.
> 
> The training loss decreased smoothly from 0.8950 to 0.1263, while validation loss dropped from 0.2851 to 0.0311, showing that the model learned features without overfitting. Validation accuracy reached a peak of **99.06%** in the final epoch."

---

## Slide 22: Figure 5: Confusion Matrix for 43 Classes (Dedicated Visual Slide)
**Slide Heading:** *Figure 5: Confusion Matrix for 43 Classes*

### Presenter Speech:
> "Figure 5 shows the confusion matrix for the test set. 
> 
> The strong diagonal line indicates that almost all instances were correctly classified, with minimal confusion even among visually similar signs like different speed limit classes."

---

## Slide 23: Figure 6: Macro-Average Receiver Operating Curve (Dedicated Visual Slide)
**Slide Heading:** *Figure 6: Macro-Average Receiver Operating Curve (ROC)*

### Presenter Speech:
> "Figure 6 shows the macro-averaged ROC curve. The Area Under the Curve (AUC) is **1.0000**, representing near-perfect class separation boundaries and high model confidence."

---

## Slide 24: Figure 7: Qualitative Predictions on 20 Test Images (Dedicated Visual Slide)
**Slide Heading:** *Figure 7: Qualitative Predictions on 20 Test Images*

### Presenter Speech:
> "Figure 7 displays a random batch of 20 test images classified by our model. The model correctly classified all 20 signs, demonstrating robustness under challenging conditions like motion blur, low lighting, and perspective tilt."

---

## Slide 25: Chapter 5: Conclusions
**Slide Heading:** *Chapter 5: Conclusions*

### Presenter Speech:
> "In conclusion, this project successfully implemented and evaluated the AlexNet CNN on the GTSRB dataset.
> 
> Our key findings are:
> 1.  **Transfer Learning:** Freezing feature layers and training only the classifier head is a highly efficient strategy for TSR.
> 2.  **Accuracy:** Achieved a test accuracy of 98.91%, matching deeper networks at a fraction of the training time.
> 3.  **Imbalance Handling:** Stratification successfully prevented bias towards majority categories, yielding an F1-score of 0.9910."

---

## Slide 26: Chapter 5: Recommendations & Future Work
**Slide Heading:** *Chapter 5: Recommendations & Future Work*

### Presenter Speech:
> "Finally, we recommend the following for future research:
> 
> 1.  **Gradual Unfreezing:** Explore gradual unfreezing of early convolutional layers to fine-tune filters for traffic sign boundaries.
> 2.  **Synthetic Augmentation:** Apply generative models to produce blurred and occluded training signs, improving noise tolerance.
> 3.  **Edge Deployment:** Deploy the model on edge hardware (Jetson/Pi) and evaluate inference latency and power efficiency in active driver assistance systems.
> 
> Thank you. We are now happy to take any questions."
