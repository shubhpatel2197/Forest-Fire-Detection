from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np
import base64
from io import BytesIO
from utills import ff  # Assuming your model is in a file named model.py
from PIL import Image

app = FastAPI()

# Enable CORS to allow requests from all origins (you can specify specific origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify specific origins like ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load the model
fire_model = ff()


def detect_fire(frame: np.ndarray) -> bool:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 50, 50])
    upper = np.array([35, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    fire_pixels = cv2.countNonZero(mask)
    total_pixels = frame.shape[0] * frame.shape[1]
    return (fire_pixels / total_pixels) > 0.01

# Endpoint to handle image upload and prediction
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read the image
    image_bytes = await file.read()

    # Convert bytes to numpy array for processing
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Make prediction using the model
    prediction = fire_model.predict(img)

    # Convert image back to base64 for returning to frontend
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    buffered = BytesIO()
    pil_img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return {"prediction": prediction, "image_base64": img_str}

@app.post("/predict_video/")
async def predict_video(file: UploadFile = File(...)):
    contents = await file.read()
    with open("temp_video.mp4", "wb") as f:
        f.write(contents)

    cap = cv2.VideoCapture("temp_video.mp4")
    fire_detected_frames = []

    while True:
        ret, frame = cap.read()
        if not ret: break
        if detect_fire(frame):
            ts = cap.get(cv2.CAP_PROP_POS_MSEC)
            fire_detected_frames.append(int(ts))
    cap.release()

    return {"fire_detected_frames": fire_detected_frames}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
