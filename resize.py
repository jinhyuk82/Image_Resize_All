"""This is a program for resizing."""

import cv2
import os
import glob

image_names = glob.glob("sample-images/*.jpg")

path_resized = "resized/sample-images/"
if not os.path.exists(path_resized):
    os.makedirs(path_resized)

for image in image_names:
    print(image)
    img = cv2.imread(image, 1)
    resized_image = cv2.resize(img, (100, 100))
    cv2.imwrite("resized/"+image, resized_image)
