import cv2

vid = cv2.VideoCapture("dance1.mp4")

# 放入要取出的幀
fram_nums = [2095, 3109, 3112, 3317, 3319, 3364, 4697, 4698]

for i in range(len(fram_nums)):
    fram_nums.insert(i, fram_nums[i] - 1)
    fram_nums.pop(i + 1)


for i in range(int(vid.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret, frame = vid.read()
    if i in fram_nums:
        cv2.imwrite("frame/dance1_{}.jpg".format(i), frame)

vid.release()
