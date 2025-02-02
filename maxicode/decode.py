import zxing
import cv2
import numpy as np

def decode_maxicode(image_path):
    """
    Decodes a MaxiCode from the given image path and annotates the image with the decoded data.
    
    Args:
        image_path (str): Path to the image containing the MaxiCode.
    
    Returns:
        None
    """
    # Initialize the ZXing reader
    reader = zxing.BarCodeReader()

    # Load the image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image from {image_path}.")
        return

    # Decode the MaxiCode using ZXing
    decoded = reader.decode(image_path)

    # Check if the MaxiCode was successfully decoded
    if not decoded:
        print("Failed to decode the MaxiCode.")
        return

    # Print decoded output
    print(f"Decoded Data: {decoded.parsed}")


    # Draw the bounding box around the MaxiCode (if points are available)
    if decoded.points:
        # Convert points to a list of (x, y) tuples
        points = [(int(p.x), int(p.y)) for p in decoded.points]

        # Draw the bounding box
        cv2.polylines(image, [np.array(points, dtype=np.int32)], isClosed=True, color=(0, 255, 0), thickness=2)

        # Annotate the decoded data beside the bounding box
        x, y = points[0]  # Use the first point of the bounding box
        text = f"Data: {decoded.parsed}\nFormat: {decoded.format}"
        y_text = y - 10  # Start text above the bounding box

        # Split the text into lines for better readability
        for i, line in enumerate(text.split('\n')):
            y_line = y_text - i * 20  # Adjust vertical position for each line
            cv2.putText(image, line, (x, y_line), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Display the annotated image
    cv2.imshow("MaxiCode with Annotation", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the annotated image
    output_file = "decoded_maxicode.png"
    cv2.imwrite(output_file, image)
    print(f"Annotated image saved as {output_file}")

# Main execution
if __name__ == "__main__":
    image_path = "maxicode.png"  # Path to the MaxiCode image
    decode_maxicode(image_path)