import cv2

vid = cv2.VideoCapture("舞蹈影片/VID20230422213134.mp4")

# 放入要取出的幀
fram_nums = list(range(219, 231))

for i in range(len(fram_nums)):
    fram_nums.insert(i, (int(fram_nums[i]) - 1))
    fram_nums.pop(i + 1)


for i in range(int(vid.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret, frame = vid.read()
    if i in fram_nums:
        cv2.imwrite("frame/VID{}.jpg".format(i+1), frame)

vid.release()
