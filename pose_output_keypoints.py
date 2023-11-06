from ultralytics import YOLO
import torch
import pandas as pd
import numpy as np
import cv2


model = YOLO("yolov8x-pose-p6.pt")
results = model(source="dance1.mp4", show=True, conf=0.75, save=True, stream=True)

# for result in results:
#     continue
grade = []
bigger = []
smaller = []
i = 1
for result in results:
    """
    for i in range(0, 18):
        keypoints = result.keypoints.cpu().xy.numpy()
        cv2.circle(img, (int(keypoints[0, i, 0:1]), int(keypoints[0, i, 1:])), 1, (255, 0, 0), 5)
    cv2.imwrite(f"{i}.jpg", img)
    """
    keypoints = result.keypoints.cpu().xy.numpy()
    if keypoints.size > 68:
        x = np.zeros((68,))
        grade.append(x)
        bigger.append(i)
    elif keypoints.size < 68:
        x = np.zeros((68,))
        grade.append(x)
        smaller.append(i)
    else:
        keypoints = keypoints.reshape(68)
        grade.append(keypoints)
    i += 1

dance1_df = pd.DataFrame(grade)
dance1_df.to_csv("dance1_df.csv", index=None)

print(bigger, "\n", smaller)
