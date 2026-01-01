# FastAPI Image Upload API

## Project Overview
This project demonstrates core **Python backend fundamentals** using FastAPI.  
It focuses on clean API design, data handling, and ML-ready thinking rather than model training.

The application exposes a single endpoint that accepts an image file and returns basic image metadata. This mirrors the **input validation and preprocessing stage** of real AI/ML systems.


![Output](output/output.jpg)

---

## Objectives Demonstrated

### 1. Python Fundamentals
- Clear function definitions
- Exception handling
- Type-aware logic
- Modular file structure

---

### 2. Data Handling & APIs
- REST API built using FastAPI
- Multipart file upload handling
- Input validation
- Structured JSON response

---

### 3. Basic AI / ML Thinking
Although no model is used, the project reflects ML system design:
- Image ingestion
- Input validation
- Metadata extraction
- Pre-inference processing mindset

This is the first step in any image-based ML pipeline.

---

### 4. Code Clarity & Documentation
- Minimal, readable code
- Clear separation of responsibilities
- Descriptive variable names
- Explicit error messages

---

### 5. Clear Thinking & Clean Structure
- Simple folder hierarchy
- Single responsibility per file
- No unnecessary dependencies
- Easy to extend for future ML inference

---

### 6. Ability to Learn & Explain
The project is intentionally small and focused:
- Easy to reason about
- Easy to test
- Easy to extend
- Easy to explain in interviews or reviews

---

## Project Structure

fastapi-image-upload/
│
├── app/
│ ├── init.py
│ └── main.py
│
├── requirements.txt
└── README.md



POST /upload-image


### Input
- Multipart form data
- Key: `file`
- Value: Image file (JPEG, PNG, etc.)

---

### Output (JSON)
```json
{
  "width": xxxx,
  "height": xxxx,
  "format": "xxxx"
}
