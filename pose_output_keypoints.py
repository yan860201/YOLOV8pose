from ultralytics import YOLO
import torch
import pandas as pd
import numpy as np
import cv2


model = YOLO("yolov8x-pose-p6.pt")
results = model(source="D:\python tasks\舞蹈影片\VID20230422213134.mp4", show=False, conf=0.77, save=False, stream=True)

# for result in results:
#     continue
grade = []
bigger = []
smaller = []
i = 1
for result in results:
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
        keypoints = keypoints.reshape(2, 34)
        if (keypoints[0, 0] < keypoints[1, 0]):
            keypoints = keypoints.reshape(68)
        else:
            arr1 = keypoints[0, :]
            arr2 = keypoints[1, :]
            keypoints = np.concatenate((arr2, arr1))
        grade.append(keypoints)
    i += 1

dance1_df = pd.DataFrame(grade)
dance1_df.to_csv("VID.csv", index=None)

print("bigger:", bigger, "\nsmaller:", smaller)
