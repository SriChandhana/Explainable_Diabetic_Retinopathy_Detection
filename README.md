# 🩺 Explainable AI for Diabetic Retinopathy Detection

An explainable deep learning system for automated diabetic retinopathy grading from retinal fundus images. The project combines high-accuracy classification, lesion localization using Grad-CAM, and automated clinical PDF report generation to improve interpretability and clinical relevance.

---

## 📄 Research Contribution

This work has been submitted as a research paper to a peer-reviewed publication venue.

The project focuses on bridging the gap between deep learning predictions and clinical usability by providing visual explanations and structured diagnostic reports.

---

## 🚀 Features

### 🔍 Automated DR Classification

* Five-class diabetic retinopathy severity grading
* EfficientNet-B0 based deep learning architecture
* Retinal image preprocessing and enhancement

### 🧠 Explainable AI

* Grad-CAM heatmap generation
* Lesion localization and visualization
* Visual evidence supporting model predictions
* Improved model transparency and interpretability

### 📋 Clinical Report Generation

* Automated PDF report generation
* Severity assessment reporting
* Lesion visualization integration
* Clinically relevant diagnostic summaries

### 👨‍⚕️ Clinical Relevance

* Focus on explainability for medical decision support
* Visual interpretation of affected retinal regions
* Improved trust in AI-assisted diagnosis

---

## 🏗️ System Architecture

```text
Retinal Fundus Image
            │
            ▼
      Preprocessing
            │
            ▼
      EfficientNet-B0
            │
            ▼
  DR Severity Prediction
            │
            ▼
     Grad-CAM Analysis
            │
            ▼
 Lesion Localization
            │
            ▼
 Clinical PDF Report
            │
            ▼
    Diagnostic Output
```

---

## 📊 Results

| Metric            | Value                |
| ----------------- | -------------------- |
| Model             | EfficientNet-B0      |
| Accuracy          | 86%                  |
| Classes           | 5 DR Severity Levels |
| Explainability    | Grad-CAM             |
| Report Generation | PDF Clinical Reports |

### Key Outcomes

* Achieved 86% accuracy on diabetic retinopathy classification.
* Generated Grad-CAM visualizations highlighting clinically significant retinal regions.
* Produced automated PDF reports containing severity levels and lesion evidence.
* Improved interpretability and clinical usability of AI predictions.

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* TensorFlow
* Keras
* EfficientNet-B0

### Data Processing

* OpenCV
* NumPy
* Pandas

### Visualization

* Matplotlib
* Grad-CAM

### Reporting

* PDF Report Generation

---

## 📸 Screenshots

### Dataset Sample

Place image here:

```text
docs/sample-retina.png
```

```markdown
![Dataset Sample](docs/sample-retina.png)
```

---

### Model Prediction

Place image here:

```text
docs/prediction-result.png
```

```markdown
![Prediction Result](docs/prediction-result.png)
```

---

### Grad-CAM Heatmap

Place image here:

```text
docs/gradcam-heatmap.png
```

```markdown
![GradCAM](docs/gradcam-heatmap.png)
```

---

### Generated Clinical PDF Report

Place image here:

```text
docs/pdf-report.png
```

```markdown
![Clinical Report](docs/pdf-report.png)
```

---


## 🔮 Future Improvements

* Vision Transformer based architectures
* Ensemble learning approaches
* Real-time clinical deployment
* Multi-modal retinal diagnosis
* Integration with hospital information systems

---

## 👩‍💻 Author

Kandula Sri Chandhana
B.Tech CSE (AI & ML), VNR VJIET
