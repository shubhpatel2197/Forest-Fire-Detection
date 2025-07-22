# Forest Fire Detection

A dual-method system for detecting forest fires in still images and video streams. It combines a lightweight, rule-based HSV-thresholding pipeline with a more robust machine-learning classifier built on handcrafted wavelet features.

---

## 📋 Summary

This project offers two complementary approaches to spot fire:
1. **HSV-Thresholding** (in `api.py`): Converts frames or images to HSV color space, masks for “fire-like” hues, and flags a scene whenever fire-pixel coverage exceeds a threshold.  
2. **Machine-Learning Model** (in `model.py`): Extracts texture and intensity features via wavelet transforms, then classifies “fire” vs. “no fire” using a pre-trained Random Forest.

Together, they let you choose between ultra-fast color-based detection and a slightly heavier—but more accurate—ML pipeline.

---

## 🔧 Tools & Technologies

- **Backend**  
  - [FastAPI](https://fastapi.tiangolo.com/) & [Uvicorn](https://www.uvicorn.org/)  
  - Python 3.8+  
- **Core Libraries**  
  - [OpenCV](https://opencv.org/) (image/video I/O & color conversions)  
  - [NumPy](https://numpy.org/) (array operations)  
  - [PyWavelets](https://pywavelets.readthedocs.io/) (wavelet decomposition)  
  - [Scikit-learn](https://scikit-learn.org/) (Random Forest classifier)  
- **Frontend**  
  - HTML, CSS, JavaScript (simple upload forms + AJAX)



