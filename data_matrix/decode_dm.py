import cv2
import numpy as np
from pylibdmtx.pylibdmtx import decode

# Step 1: Load the image
image_path = 'IMG_2019.jpg'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load image. Please check the file path.")
    exit()

# Step 2: Resize the image to make the Data Matrix code larger
scale_percent = 200  # Increase size by 200% (adjust as needed)
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

# Step 3: Apply thresholding to make the code more readable
_, thresholded_image = cv2.threshold(resized_image, 128, 255, cv2.THRESH_BINARY)

# Step 4: Optionally, apply noise reduction
denoised_image = cv2.medianBlur(thresholded_image, 3)

# Step 5: Crop the image to focus on the center (zoom in)
height, width = denoised_image.shape
crop_size = 300  # Adjust this value based on the size of the code
start_x = width // 2 - crop_size // 2
start_y = height // 2 - crop_size // 2
cropped_image = denoised_image[start_y:start_y + crop_size, start_x:start_x + crop_size]

# Save the preprocessed and cropped image for debugging
cv2.imwrite('preprocessed_image.jpg', denoised_image)
cv2.imwrite('cropped_image.jpg', cropped_image)

# Step 6: Decode the Data Matrix code
decoded_objects = decode(cropped_image)

# Step 7: Check if the code was successfully decoded
if decoded_objects:
    for obj in decoded_objects:
        print("Decoded Data:", obj.data.decode('utf-8'))
else:
    print("No Data Matrix code found or unable to decode.")