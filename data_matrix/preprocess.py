import cv2
import numpy as np
from pylibdmtx.pylibdmtx import decode

# Load the image
image = cv2.imread('IMG_2019.jpg', cv2.IMREAD_GRAYSCALE)

# Resize the image to make the data matrix code larger
scale_percent = 200  # Increase size by 200%
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

# Apply thresholding to make the code more readable
_, thresholded_image = cv2.threshold(resized_image, 128, 255, cv2.THRESH_BINARY)

# Optionally, apply some noise reduction
denoised_image = cv2.medianBlur(thresholded_image, 3)

# Save the preprocessed image for debugging
cv2.imwrite('preprocessed_image.jpg', denoised_image)