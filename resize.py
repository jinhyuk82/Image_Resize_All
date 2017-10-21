"""This is a program for resizing."""

import cv2
import os

image_names = ["galaxy.jpg", "kangaroos-rain-australia_71370_990x742.jpg", "Lighthouse.jpg", "Moon sinking, sun rising.jpg"]

path_resized = "resized/"
if not os.path.exists(path_resized):
    os.makedirs(path_resized)

for image in image_names:
    print("sample-images/"+image)
    img = cv2.imread("sample-images/"+image, 1)
    resized_image = cv2.resize(img, (100, 100))
    cv2.imwrite("resized/"+image, resized_image)
