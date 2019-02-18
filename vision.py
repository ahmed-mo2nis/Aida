import cv2
import numpy as np
import pickle
import sys
import time
from skimage.measure import compare_ssim

def ssim(A, B):
    return compare_ssim(A, B, data_range=A.max()-A.min())

def mse(A, B):
    return ((A-B)**2).mean()

cap = cv2.VideoCapture(0)

current_frame = None
previous_frame = None
first_frame = True
frame_counter = 0

while True:
    if frame_counter == 0:
        previous_frame = current_frame
    _, current_frame = cap.read()
    if current_frame is None:
        break

    current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    if first_frame:
        previous_frame = current_frame
        first_frame = False

    if frame_counter == 9:
        ssim_index = ssim(current_frame, previous_frame)
        frame_counter = 0

    cv2.imshow("app", current_frame)
    frame_counter = frame_counter + 1

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
