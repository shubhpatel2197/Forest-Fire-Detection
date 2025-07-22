# Forest Fire Detection

## What It Is
A web application that lets you upload images or videos and automatically detects the presence of forest fire by analyzing color properties in each frame or image.

## Tools Used
- **Backend:**  
  - [FastAPI](https://fastapi.tiangolo.com/)  
  - [Uvicorn](https://www.uvicorn.org/)  
- **Computer Vision:**  
  - [OpenCV](https://opencv.org/)  
  - [NumPy](https://numpy.org/)  
- **Frontend:**  
  - HTML, CSS, JavaScript

## Algorithms and Methods
1. **Color Space Conversion**  
   - Convert input from BGR (OpenCV’s default) to HSV for robust color segmentation.

2. **HSV Thresholding**  
   - Define a “fire-like” HSV range (Hue: 0–35, Saturation: 50–255, Value: 50–255).  
   - Generate a binary mask of pixels within that range.

3. **Pixel Ratio Analysis**  
   - Count mask (fire) pixels vs. total pixels.  
   - Fire is flagged when fire-pixel ratio exceeds a threshold (e.g., 1% of the frame).

4. **Frame-by-Frame Video Processing**  
   - Use OpenCV’s `VideoCapture` to read each video frame.  
   - Apply the same HSV-thresholding pipeline to every frame.  
   - Record and return the timestamps (in milliseconds) of all frames where fire is detected.
