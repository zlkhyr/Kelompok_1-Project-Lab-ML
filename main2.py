from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from numpy import argmax
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import io
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load_model("traffic-sign-cnn.h5")

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    img = await file.read()
    img = load_img(io.BytesIO(img), target_size=(32, 32))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0


    predict_value = model.predict(img)
    predict_class = int(argmax(predict_value))

    labels = ['Speed limit (20km/h)', 'Speed limit (30km/h)',
       'Speed limit (50km/h)', 'Speed limit (60km/h)',
       'Speed limit (70km/h)', 'Speed limit (80km/h)',
       'End of speed limit (80km/h)', 'Speed limit (100km/h)',
       'Speed limit (120km/h)', 'No passing',
       'No passing for vehicles over 3.5 metric tons',
       'Right-of-way at the next intersection', 'Priority road', 'Yield',
       'Stop', 'No vehicles', 'Vehicles over 3.5 metric tons prohibited',
       'No entry', 'General caution', 'Dangerous curve to the left',
       'Dangerous curve to the right', 'Double curve', 'Bumpy road',
       'Slippery road', 'Road narrows on the right', 'Road work',
       'Traffic signals', 'Pedestrians', 'Children crossing',
       'Bicycles crossing', 'Beware of ice/snow', 'Wild animals crossing',
       'End of all speed and passing limits', 'Turn right ahead',
       'Turn left ahead', 'Ahead only', 'Go straight or right',
       'Go straight or left', 'Keep right', 'Keep left',
       'Roundabout mandatory', 'End of no passing',
       'End of no passing by vehicles over 3.5 metric tons']

    return JSONResponse(content={'class': labels[predict_class]})