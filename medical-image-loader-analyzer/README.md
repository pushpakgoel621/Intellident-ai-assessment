# Medical Image Loader & Analyzer

## Project Overview

This project demonstrates a foundational computer vision pipeline focused on **image data handling and preprocessing**, which are critical steps in any AI/ML system, especially in medical imaging.

The goal is not to train a model, but to show **clear thinking, correct data handling, and structured code design** before ML is applied.

![Output](output (2).png)
![Input image](data/img1.jpg)
![Output image](output/img1.jpg)



---

## Objectives Demonstrated

This project explicitly demonstrates:

### Python Fundamentals
- Modular code structure
- Use of functions and reusable components
- Clean control flow and error handling
- File system operations

### Data Handling & APIs
- Image I/O using OpenCV
- Handling multiple image formats
- Converting raw image data into numerical arrays
- Saving processed outputs to disk

### Basic AI / ML Thinking
- Standardizing input data (grayscale + fixed size)
- Reducing dimensionality before learning
- Extracting numeric features (mean pixel intensity)
- Preparing data in a model-ready format

### Code Clarity & Documentation
- Separation of concerns (loader, processor, analyzer)
- Readable variable names
- Minimal but meaningful comments
- Predictable execution flow

### Clear Thinking & Clean Structure
- Deterministic pipeline
- No hidden assumptions
- Each step has a clear purpose
- Output is human-verifiable

---

## Project Structure

medical-image-loader-analyzer/
│
├── data/# Input images provided by the user
│
├── output/# Grayscale and resized images
│
├── src/
│ ├── image_loader.py # Image loading logic
│ ├── image_processor.py # Grayscale + resize operations
│ └── analyzer.py # Image statistics computation
│
├── main.py # End-to-end pipeline execution
├── requirements.txt
└── README.md


This structure mirrors how real ML pipelines are organized.

---

## Processing Pipeline

The pipeline follows a strict and logical order:

1. **Load Images**
   - Reads all images from a directory
   - Skips unreadable or corrupted files safely

2. **Preprocess Images**
   - Convert images to grayscale
   - Resize all images to a fixed resolution (256 × 256)

3. **Analyze Images**
   - Extract image resolution
   - Compute mean pixel intensity

4. **Save & Report**
   - Save processed images to disk
   - Print statistics for each image

Each step is isolated and testable.
