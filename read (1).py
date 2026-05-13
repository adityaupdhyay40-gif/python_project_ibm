import cv2
from pyzbar.pyzbar import decode
import csv
from datetime import datetime

# Open webcam
cap = cv2.VideoCapture(1)

print("Press Q to Exit")

while True:
    success, img = cap.read()

    # Detect QR and Barcode
    for barcode in decode(img):

        # Decode data
        data = barcode.data.decode('utf-8')
        print("Detected:", data)
 # Rectangle coordinates
        x, y, w, h = barcode.rect

        # Draw rectangle
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display text
        cv2.putText(img, data, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255, 0, 0), 2)

        # Save scan history
        with open('history.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now(),
                data
            ])
 # Show camera window
    cv2.imshow("QR & Barcode Scanner", img)

    # Exit condition
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()