import cv2
import os

# Create a directory if it doesn't exist
data_dir = "face_data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Initialize webcam
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Get user details
user_name = input("Enter your name: ").strip()
user_folder = os.path.join(data_dir, user_name)

# Create user-specific folder if it doesn't exist
if not os.path.exists(user_folder):
    os.makedirs(user_folder)

count = 0
max_images = 20  # Number of images to capture

print("Capturing face images... Press 'q' to stop.")

while count < max_images:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = frame[y:y + h, x:x + w]
        file_name = os.path.join(user_folder, f"{count}.jpg")
        cv2.imwrite(file_name, face_img)  # Save face image
        count += 1
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face Capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(f"Captured {count} images for {user_name}.")
cap.release()
cv2.destroyAllWindows()
