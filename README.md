# Parkinson’s Disease Screening Using Spiral Drawings

## Overview
This project presents a deep learning–based approach for automated screening
of Parkinson’s disease using **hand-drawn spiral images**.
Motor impairments such as tremors and irregular motion patterns,
which are characteristic of Parkinson’s disease,
are reflected in spiral drawings and analyzed using a CNN model.

This is an academic research project intended to provide
objective support for neurological screening.

## Medical Background
Parkinson’s disease is a progressive neurodegenerative disorder
caused by the loss of dopamine-producing neurons.
Common motor symptoms include tremors, rigidity,
slowed movement, and impaired coordination.

Early detection is challenging because diagnosis is largely clinical
and subjective, with no simple laboratory test.

## Dataset
• Spiral drawing images labeled as **Healthy** or **Parkinson’s**  
• Data loaded from preprocessed `.npz` files  

> The dataset is not included due to licensing restrictions.

## Methodology
• Image resizing to 128×128 resolution  
• Grayscale conversion and normalization  
• Data augmentation (rotation, flipping) to increase robustness  
• CNN-based image classification using Keras  
• Softmax-based probability prediction  

## Model Architecture
• Convolutional layers for feature extraction  
• Dropout layers to prevent overfitting  
• Dense classification layer with softmax  

## Training & Performance
• Optimizer: Adam  
• Loss function: Categorical Cross-Entropy  
• Validation Accuracy: **~91.5%**  

## Key Advantage
Provides a **fast, low-cost, and objective screening tool**
that can potentially be deployed on mobile or tablet platforms.

## Disclaimer
This project is for **educational and research purposes only**  
and is **not intended for clinical diagnosis**.

## Author
Prawin M – Biomedical Engineering
