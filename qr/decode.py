import cv2
from pyzbar.pyzbar import decode
import numpy as np

# Load the image
image_path = "IMG_2027.jpg"  # Change this to your QR code image file
image = cv2.imread(image_path)

# Decode the QR code
qr_codes = decode(image)

for qr in qr_codes:
    data = qr.data.decode("utf-8")
    print(f"QR Code Data: {data}")

    # Draw a rectangle around the QR code
    points = qr.polygon
    if len(points) == 4:
        pts = [(point.x, point.y) for point in points]
        cv2.polylines(image, [np.array(pts, dtype=np.int32)], isClosed=True, color=(0, 255, 0), thickness=2)

    # Display the decoded text on the image
    x, y = points[0].x, points[0].y
    cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Show the image with annotations
cv2.imshow("QR Code", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
