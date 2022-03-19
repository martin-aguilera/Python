import cv2, numpy as np
from imageio import imread, imwrite

img = imread("00.jpg")
arr = img * np.array([0.1, 0.2, 0.5])
arr2 = (255 * arr / arr.max()).astype(np.uint8)
imwrite("out.png", arr2)
img2 = cv2.imread("out.png")
gamma = 2  # more gamma equals more darkness
gamma_img = np.array(255 * (img2 / 255) ** gamma, dtype="uint8")
cv2.imwrite("night_final.png", gamma_img)
print("Done")
