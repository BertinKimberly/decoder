import cv2
from pdf417decoder import PDF417Decoder
from PIL import Image
import os
import numpy as np

def decode_pdf417(image_path):
    # Validating image path
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    try:
        # Image loading using OpenCV
        cv_image = cv2.imread(image_path)
        if cv_image is None:
            raise ValueError("Invalid image format or unable to read the image")

        # Converting to RGB (PIL expects RGB format)
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

        # Converting OpenCV image (numpy array) to PIL Image
        pil_image = Image.fromarray(rgb_image)

        # Initializing PDF417 decoder with PIL Image
        decoder = PDF417Decoder(pil_image)

        # Decoding barcode
        decode_result = decoder.decode()

        if decode_result > 0:
            # Extracting decoded data
            decoded_data = decoder.barcode_data_index_to_string(0)

            # Returning data
            return decoded_data
        else:
            return "No barcode detected"

    except ValueError as ve:
        raise ve
    except Exception as e:
        raise RuntimeError(f"Decoding error: {str(e)}")

if __name__ == "__main__":
    try:
        result = decode_pdf417("IMG_1903.jpg")
        print(f"Decoded Data: \n{result}")
    except Exception as e:
        print(f"Error: {str(e)}")
