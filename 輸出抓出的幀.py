from ultralytics import YOLO
import torch
import pandas as pd
import numpy as np
import cv2
import glob


model = YOLO("yolov8x-pose-p6.pt")
frame = [2095, 3109, 3112, 3317, 3319, 3364, 4697, 4698]

for i in range(len(frame)):
    frame.insert(i, frame[i] - 1)
    frame.pop(i + 1)

for i in frame:
    results = model(
        source=f"frame/dance1_{i}.jpg", show=True, conf=0.79, save=True, stream=False
    )
