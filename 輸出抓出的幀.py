from ultralytics import YOLO
import torch
import pandas as pd
import numpy as np
import cv2
import glob


model = YOLO("yolov8x-pose-p6.pt")

# 輸入要輸出的幀(已先抓出至frame資料夾)
fram_nums = list(range(219, 231))

# for i in range(len(fram_nums)):
#     fram_nums.insert(i, fram_nums[i] - 1)
#     fram_nums.pop(i + 1)

for i in fram_nums:
    results = model(
        source=f"frame/VID{i}.jpg", show=True, conf=0.79, save=True, stream=False
    )
