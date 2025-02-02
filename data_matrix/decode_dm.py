from pylibdmtx.pylibdmtx import decode
import cv2
import sys

def load_image(image_path):
    """
    Load an image from the specified path in grayscale mode.
    :param image_path: Path to the image file.
    :return: Loaded image or None if loading fails.
    """
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise FileNotFoundError(f"Image file not found or could not be opened: {image_path}")
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def decode_data_matrix(image):
    """
    Decode Data Matrix barcodes from the given image.
    :param image: Grayscale image containing Data Matrix barcodes.
    :return: List of decoded objects or None if decoding fails.
    """
    try:
        decoded_objects = decode(image)
        if not decoded_objects:
            print("No Data Matrix barcodes found in the image.")
        return decoded_objects
    except Exception as e:
        print(f"Error decoding Data Matrix: {e}")
        return None

def save_image(image, output_path):
    """
    Save the image to the specified output path.
    :param image: Image to save.
    :param output_path: Path to save the image.
    :return: True if successful, False otherwise.
    """
    try:
        success = cv2.imwrite(output_path, image)
        if not success:
            raise IOError(f"Failed to save image to: {output_path}")
        print(f"Annotated image saved successfully as: {output_path}")
        return True
    except Exception as e:
        print(f"Error saving image: {e}")
        return False

def display_image(image, window_name="Barcode with Annotation"):
    """
    Display the image in a window.
    :param image: Image to display.
    :param window_name: Name of the window.
    """
    try:
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error displaying image: {e}")

def main():
    # Path to the input image
    input_image_path = "IMG_2019.jpg"
    # Path to save the output image
    output_image_path = "image2_datamatrix.jpg"

    # Step 1: Load the image
    image = load_image(input_image_path)
    if image is None:
        sys.exit(1)  # Exit if the image cannot be loaded

    # Step 2: Decode Data Matrix barcodes
    decoded_objects = decode_data_matrix(image)
    if decoded_objects is None:
        sys.exit(1)  # Exit if decoding fails

    # Step 3: Print decoded data
    for obj in decoded_objects:
        try:
            data = obj.data.decode("utf-8")
            print("Decoded Data:", data)
        except UnicodeDecodeError:
            print("Error: Failed to decode the barcode data as UTF-8.")

    # Step 4: Save the image
    if not save_image(image, output_image_path):
        sys.exit(1)  # Exit if saving the image fails

    # Step 5: Display the image
    display_image(image)

if __name__ == "__main__":
    main()